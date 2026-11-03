#!/usr/bin/env python3
"""Extract per-register tables from a JEDEC PMIC spec (pdftotext -layout output).

Usage:
    pdftotext -layout spec.pdf spec.txt
    python3 tools/extract_registers.py spec.txt meta.json out.json

meta.json holds document metadata (doc id, device, revision, application, ...).
The output JSON contains one entry per "Table N — Register 0xXX" table with
fields, per-value meanings, notes, source table number and page.
"""
import copy
import json
import re
import sys

WATERMARK = {"Sa", "m", "su", "ng"}

HEADING_RE = re.compile(r"^\s*Table (\d+) — (.+?)\s*$")
REG_HEADING_RE = re.compile(r"^Register 0x([0-9A-Fa-f]+)$")
CONT_RE = re.compile(r"\(cont[’']d\)\s*$")
SECTION_RE = re.compile(r"^\d+(\.\d+)*\s{2,}[A-Z][a-z]")  # column 0 only; rows are indented
PAGE_RE = re.compile(r"^\s*Page (\d+)\s*$")
BITS_RE = re.compile(r"^\d+(:\d+)?(\s*,\s*\d+(:\d+)?)*$")
NOTE_RE = re.compile(r"^\s*NOTE\s*(\d*)\s+(.*)$")
FIELD_REF_RE = re.compile(r"^R[0-9A-Fa-f]+\s*\[[^\]]*\]\s*:?\s*(.*)$")
BIN_VALUE_RE = re.compile(r"^((?:[01xX]{1,4} ?){1,4}?)\s*(>\s*=|<\s*=|=|>|<|≥|≤)\s*(.*)$")
HEX_VALUE_RE = re.compile(r"^(0x[0-9A-Fa-f]{2}|[0-9A-Fa-f]{2}h)\s*[:=]\s*(.*)$")
ELLIPSIS = {"...", "..", "…", "• • •", "."}
NUM_RE = re.compile(r"(?<![0-9A-Za-z.\[])([+-]?\d+(?:\.\d+)?)(\s*)(mA/mW|A/W|mV|V|mA|A|mW|W|°C|%|ms|μs|us|ns|kHz|MHz|mΩ|Ω)?(?![0-9A-Za-z\]/])")
UNIT_SCALE = {"mA/mW": 1e-3, "A/W": 1, "mV": 1e-3, "V": 1, "mA": 1e-3, "A": 1, "mW": 1e-3, "W": 1, "ms": 1e-3, "μs": 1e-6,
              "us": 1e-6, "ns": 1e-9, "kHz": 1e3, "MHz": 1e6, "mΩ": 1e-3, "Ω": 1, "°C": 1, "%": 1, "": 1}
# footnote markers like "Reading[1]" or "[3],[4]" -- but not bit references like "0x1A[1]" / "0x2B [5]"
FOOTNOTE_RE = re.compile(r"(?<!0x[0-9A-Fa-f]{2})(?<!0x[0-9A-Fa-f]{3})(?<!0x[0-9A-Fa-f]{2} )(?<!0x[0-9A-Fa-f]{3} )"
                         r"(?<!R[0-9A-Fa-f]{2})(?<!R[0-9A-Fa-f]{3})(?<!R[0-9A-Fa-f]{2} )(?<!R[0-9A-Fa-f]{3} )"
                         r"\[\d+\](?:,\s*\[\d+\])*")


def clean_lines(text):
    """Strip page furniture and the diagonal watermark; keep page numbers as markers."""
    out = []
    for raw in text.split("\n"):
        line = raw.replace("\f", "").rstrip()
        s = line.strip()
        if not s:
            out.append("")
            continue
        if s.startswith("Downloaded by") or s.startswith("JEDEC Standard No.") or \
                re.fullmatch(r"Revision \d+(\.\d+)*", s):
            continue
        m = PAGE_RE.match(line)
        if m:
            out.append(("PAGE", int(m.group(1))))
            continue
        if s in WATERMARK:
            continue
        line = re.sub(r"(?<=\S)\s+(Sa|m|su|ng)$", "", line)  # trailing watermark fragment
        line = re.sub(r"(\d)0 C\b", r"\1 °C", line)  # degree sign extracted as a superscript '0' 
        out.append(line)
    return out


def split_segments(lines, start_marker):
    started, page, segs, cur = False, None, [], None
    for ln in lines:
        if isinstance(ln, tuple):
            page = ln[1]
            continue
        if not started:
            if re.match(start_marker, ln.strip() or "-"):
                started = True
            continue
        s = ln.strip()
        m = HEADING_RE.match(ln)
        if m:
            title = m.group(2)
            if CONT_RE.search(title):
                continue
            cur = {"table": int(m.group(1)), "title": title, "page": page, "lines": []}
            segs.append(cur)
            continue
        if re.match(r"^\d+(\.\d+)+\s{2,}\S", s) and CONT_RE.search(s):
            continue  # indented "11.6 ... (cont'd)" page header
        if SECTION_RE.match(ln):
            if not CONT_RE.search(s):
                cur = None  # prose section begins
            continue
        if cur is not None:
            cur["lines"].append(ln)
    return segs


def parse_register(seg, addr, parser="rows", digit_footnotes=False):
    if parser == "columns":
        rows, notes, subtitle = parse_register_columns(seg, addr, digit_footnotes)
        if digit_footnotes:
            for n in notes:
                n["text"] = normalize_digit_footnotes(n["text"])
        return finish_register(seg, addr, rows, notes, subtitle)
    rows, notes, pending = [], [], []
    subtitle, mode = None, "pre"
    for ln in seg["lines"]:
        s = ln.strip()
        if not s:
            continue
        if re.match(r"^Bits\s+Attribute\s+Default", s):
            if mode == "pre":
                mode = "rows"
            continue
        if mode == "pre":
            subtitle = s
            continue
        parts = re.split(r"\s{2,}", s)
        if len(parts) >= 3 and BITS_RE.match(parts[0]) and re.match(r"^[A-Z0-9]{1,6}$", parts[1]):
            desc = " ".join(parts[3:])
            rows.append({"bits": re.sub(r"\s+", "", parts[0]), "attr": parts[1], "default": parts[2],
                         "lines": pending + ([desc] if desc else [])})
            pending = []
            mode = "rows"
            continue
        nm = NOTE_RE.match(ln)
        if nm and mode in ("rows", "notes"):
            if pending and rows:
                rows[-1]["lines"].extend(pending)
                pending = []
            notes.append({"n": nm.group(1), "text": nm.group(2).strip()})
            mode = "notes"
            continue
        if mode == "notes":
            notes[-1]["text"] += " " + s
            continue
        if not rows:
            pending.append(s)
            continue
        row = rows[-1]
        # second half of an 8-bit default printed on the next line, e.g. "0011" / "1100"
        dm = re.match(r"^([01]{4})(?:\s{2,}(.*))?$", s)
        if dm and re.fullmatch(r"[01]{4}", row["default"]) and len(bit_list(row["bits"])) == 8:
            row["default"] += " " + dm.group(1)
            if dm.group(2):
                row["lines"].append(dm.group(2))
            continue
        # field header printed above its bits row (vertically centred cell)
        if pending or (FIELD_REF_RE.match(s) and any(FIELD_REF_RE.match(x) for x in row["lines"])
                       and not re.match(r"^R[0-9A-Fa-f]+\s*\[[^\]]*\]\s*(=|is|must|and|or|,)", s)):
            pending.append(s)
            continue
        row["lines"].append(s)
    if pending and rows:
        rows[-1]["lines"].extend(pending)
    return finish_register(seg, addr, rows, notes, subtitle)


def finish_register(seg, addr, rows, notes, subtitle):
    fields = [build_field(r) for r in rows]
    return {
        "address": f"0x{addr:02X}",
        "addr_int": addr,
        "name": f"R{addr:02X}",
        "subtitle": subtitle if subtitle and subtitle != f"R{addr:02X}" else None,
        "source_table": seg["table"],
        "page": seg["page"],
        "fields": fields,
        "notes": [f"NOTE {n['n']}: {n['text']}" if n["n"] else f"NOTE: {n['text']}" for n in notes],
    }


FIELD_START_RE = re.compile(r"^R[0-9A-Fa-f]+\s*\[[\d:,\s]+\]\s*(:|Reserved\b)")
HEADER_RE = re.compile(r"Bits\s+Attribute\s+Default")


def normalize_digit_footnotes(s):
    """Docs that print footnotes as bare superscript digits: 'Setting3,4' -> 'Setting[3],[4]'."""
    fn = lambda d: ",".join(f"[{x}]" for x in d.split(","))
    s = re.sub(r"(?<=\d)(\s?(?:mV|mA|mW|ms|μs|ns|°C|V|A|W|%))(\d{1,2}(?:,\d{1,2})*)\b",
               lambda m: m.group(1) + fn(m.group(2)), s)
    s = re.sub(r"\b(Config\d)(\d{1,2}(?:,\d{1,2})*)\b", lambda m: m.group(1) + fn(m.group(2)), s)
    s = re.sub(r"\b((?!Config\d)[A-Za-z_]*[a-z])(\d{1,2}(?:,\d{1,2})*)\b",
               lambda m: m.group(1) + fn(m.group(2)), s)
    s = re.sub(r"([\]”\)])(\d{1,2}(?:,\d{1,2})*)\b", lambda m: m.group(1) + fn(m.group(2)), s)
    s = re.sub(r"(?<=[a-z])([:.])(\d{1,2}(?:,\d{1,2})*)(?=\s|$)", lambda m: m.group(1) + fn(m.group(2)), s)
    return s


def parse_register_columns(seg, addr, digit_footnotes=False):
    """Column-position parser for tables whose cells are vertically centred.

    Field boundaries come from the description column ('Rxx [b:a]: NAME'); bits/attribute/default
    tokens in the left columns are assigned to whichever field's line span they sit in.
    """
    lines = [ln for ln in seg["lines"] if ln.strip()]
    rows, notes, subtitle = [], [], []
    cols = None
    mode = "pre"
    body = []  # (left_tokens, right_text)
    for ln in lines:
        s = ln.strip()
        hm = HEADER_RE.search(ln) or re.search(r"^\s*Bits\s+(e\s+)?Default\s+Description", ln)
        if hm:
            xb = ln.index("Bits")
            xd = ln.index("Default")
            if "Attribute" in ln:
                xa = ln.index("Attribute")
            else:  # header wrapped as "Attribut" / "e"
                prev = [l for l in lines[:lines.index(ln)] if "Attribut" in l]
                xa = prev[-1].index("Attribut") if prev else (xb + xd) // 2
                if subtitle and "Attribut" in subtitle[-1]:
                    subtitle.pop()
            cols = {"b_a": (xb + 4 + xa) / 2, "a_d": (xa + 9 + xd) / 2, "d_end": xd + 7}
            mode = "rows"
            continue
        if mode == "pre":
            if not re.fullmatch(r"R[0-9A-Fa-f]+|[\d,\s]+|R[0-9A-Fa-f]+\s+[\d,]+", s):
                subtitle.append(s)
            continue
        if re.match(r"^\s*\d+(\.\d+)+\s+[A-Z].*\(cont[’']d\)\s*$", ln) or \
                re.match(r"^\d+(\.\d+)+\s+[A-Z][a-z]", ln):
            continue  # section running header
        nm = NOTE_RE.match(ln)
        if nm and (len(ln) - len(ln.lstrip())) < 4:
            notes.append({"n": nm.group(1), "text": nm.group(2).strip()})
            mode = "notes"
            continue
        if mode == "notes":
            if (len(ln) - len(ln.lstrip())) >= 4 or not re.fullmatch(r"R[0-9A-Fa-f]+|[\d,\s]+", s):
                notes[-1]["text"] += " " + s
            continue
        if re.fullmatch(r"R[0-9A-Fa-f]+(\s+[\d,]+)?|[\d,\s]+", s) and not re.fullmatch(r"\d+(:\d+)?", s):
            continue  # repeated table sub-heading on a continuation page
        if re.match(r"^\d+(\.\d+)+\s+[A-Z][a-z]", ln):
            continue  # section running header at column 0
        body.append((ln, cols))
    if not body:
        return rows, notes, " ".join(subtitle) or None
    # description column per page section: the most common start of a field header ("Rxx [b:a]:")
    def field_start(ln, c):
        for m in re.finditer(r"R[0-9A-Fa-f]+\s*\[[\d:,\s]+\]\s*(:|Reserved\b)", ln):
            if m.start() > c["a_d"] and not ln[:m.start()].strip().endswith(("=", ",")):
                return m.start()
        return None

    xdescs = {}
    for c in {id(c): c for _, c in body}.values():
        starts = [x for x in (field_start(ln, c) for ln, cc in body if cc is c) if x is not None]
        xdescs[id(c)] = max(set(starts), key=starts.count) - 2 if starts else None
    known = [x for x in xdescs.values() if x is not None]
    items = []
    for ln, cols in body:
        fs = field_start(ln, cols)
        xdesc = xdescs[id(cols)]
        if xdesc is None:  # continuation page without a field header: estimate from the first section
            xdesc = max(cols["d_end"] + 2, (known[0] if known else 0) + int(cols["a_d"] - body[0][1]["a_d"]))
        if fs is not None:
            xdesc = fs
        left, right = ln[:xdesc], ln[xdesc:].strip()
        if 0 < xdesc < len(ln) and ln[xdesc - 1] != " " and ln[xdesc] != " ":
            # a description token straddles the split point: cut at the last gap before it
            gaps = [m.end() for m in re.finditer(r"\s{2,}", ln[:xdesc])] or \
                   [m.end() for m in re.finditer(r"\s", ln[:xdesc])]
            cut = gaps[-1] if gaps else 0
            left, right = ln[:cut], ln[cut:].strip()
        toks = []
        for m in re.finditer(r"\S+(?: \S+)*", left):
            x = m.start()
            kind = "bits" if x < cols["b_a"] else "attr" if x < cols["a_d"] else "default"
            toks.append((kind, m.group(0)))
        if digit_footnotes:
            right = normalize_digit_footnotes(right)
        items.append((toks, right))
    # split into fields at description field headers
    spans = []
    for toks, right in items:
        if right and FIELD_START_RE.match(right) or not spans:
            spans.append({"toks": [], "lines": []})
        spans[-1]["toks"] += toks
        if right:
            spans[-1]["lines"].append(right)
    for sp in spans:
        get = lambda k: [t for kind, t in sp["toks"] if kind == k]
        bits = "".join(t for t in get("bits") if BITS_RE.match(t.replace(" ", ""))).replace(" ", "")
        if not bits:
            # header-less leading text (e.g. a sub-heading) -> attach to next span
            continue
        row = {"bits": bits, "attr": "".join(get("attr")).replace(" ", ""),
               "default": " ".join(get("default")) or "-", "lines": sp["lines"]}
        hb = re.match(r"^R[0-9A-Fa-f]+\s*\[([\d:,\s]+)\]", sp["lines"][0]) if sp["lines"] else None
        if hb and re.sub(r"\s", "", hb.group(1)) != bits:
            row["header_bits"] = re.sub(r"\s", "", hb.group(1))
        # 8-bit default whose second nibble landed at the start of a description line ("0000 Switch ...")
        if re.fullmatch(r"[01]{4}", row["default"]) and len(bit_list(bits)) == 8:
            for i, l in enumerate(row["lines"][1:3], 1):
                m = re.match(r"^([01]{4})\s+(?![=><≥≤])(\S.*)$", l)
                if m:
                    row["default"] += " " + m.group(1)
                    row["lines"][i] = m.group(2)
                    break
        rows.append(row)
    # leading spans without bits: prepend their lines to the following row
    out, carry = [], []
    for sp in spans:
        if not any(k == "bits" and BITS_RE.match(t.replace(" ", "")) for k, t in sp["toks"]):
            carry += sp["lines"]
            continue
        row = next(r for r in rows if r["lines"] is sp["lines"])
        row["lines"] = carry + row["lines"]
        carry = []
        out.append(row)
    if carry and out:
        out[-1]["lines"] += carry
    # Bits column vs field header disagreement (a spec typo in one of them): keep whichever gives
    # exact coverage of bits 7..0, and record the choice on the field.
    def covers(rs, use_header):
        bl = []
        for r in rs:
            bl += bit_list(r.get("header_bits", r["bits"]) if use_header else r["bits"])
        return sorted(bl) == list(range(8))
    if any("header_bits" in r for r in out):
        use_header = not covers(out, False) and covers(out, True)
        for r in out:
            if "header_bits" not in r:
                continue
            hb = r.pop("header_bits")
            if use_header:
                r["errata"] = [f"Bits column shows [{r['bits']}] but the field header says [{hb}]; "
                               f"[{hb}] is used because it makes the fields cover bits 7..0 exactly."]
                r["bits"] = hb
            else:
                r["errata"] = [f"Field header says [{hb}] but the Bits column shows [{r['bits']}]; "
                               f"the Bits column is used."]
    return out, notes, " ".join(subtitle) or None


def bit_list(bits):
    out = []
    for part in bits.split(","):
        if ":" in part:
            hi, lo = map(int, part.split(":"))
            out.extend(range(hi, lo - 1, -1))
        else:
            out.append(int(part))
    return out


def build_field(row):
    # a bare superscript note right after a bit reference: "Register 0x09 [2]2" -> "... [2][2]"
    lines = [re.sub(r"\](\d{1,2}(?:,\d{1,2})*)\b",
                    lambda m: "]" + ",".join(f"[{x}]" for x in m.group(1).split(",")), l) for l in row["lines"]]
    name = None
    if lines:
        fm = FIELD_REF_RE.match(lines[0])
        if fm:
            rest = fm.group(1).strip()
            lines = lines[1:]
            if re.match(r"^[A-Z0-9_.]+$", rest):
                name = rest
            elif not rest and lines and re.match(r"^[A-Z0-9_.]+$", lines[0]):
                name = lines.pop(0)
            elif rest:
                lines.insert(0, rest)
    # field names wrapped over lines: "..._THRESHOLD_" + "SETTING" or "..._WARNING" + "_STATUS"
    if name:
        name = re.sub(r"\s+_", "_", name)
        while lines and re.fullmatch(r"_?[A-Z0-9_.]+", lines[0]) and (name.endswith("_") or lines[0].startswith("_")):
            name += lines.pop(0)
    values, text, condition = [], [], None
    row_width = len(bit_list(row["bits"]))
    lines = [l for i, l in enumerate(lines) if not (l in ELLIPSIS and i > 0 and lines[i - 1] in ELLIPSIS)]

    def cond_has_values():
        return any(v["condition"] == condition for v in values)

    for idx, s in enumerate(lines):
        bm, hm = BIN_VALUE_RE.match(s), HEX_VALUE_RE.match(s)
        nxt = BIN_VALUE_RE.match(lines[idx + 1]) if idx + 1 < len(lines) else None
        if bm and bm.group(1).strip():
            op = re.sub(r"\s", "", bm.group(2)).replace(">=", "≥").replace("<=", "≤")
            meaning = bm.group(3).strip()
            trailing_ellipsis = re.search(r"\s+(\.\.\.|…)$", meaning)
            if trailing_ellipsis:
                meaning = meaning[:trailing_ellipsis.start()]
            values.append({"code": re.sub(r"\s", "", bm.group(1)),
                           "meaning": meaning if op == "=" else f"{op} {meaning}", "condition": condition})
            if trailing_ellipsis:
                values.append({"code": "...", "meaning": "...", "condition": condition})
        elif hm:
            values.append({"code": hm.group(1), "meaning": hm.group(2).strip(), "condition": condition})
        elif re.fullmatch(r"(?:[01]{1,4} ?){1,4}", s) and len(re.sub(r"\s", "", s)) == row_width:
            values.append({"code": re.sub(r"\s", "", s), "meaning": "(code value; no separate meaning listed)",
                           "condition": condition})
        elif s in ELLIPSIS:
            values.append({"code": "...", "meaning": "...", "condition": condition})
        elif re.match(r"^If .*?[’']\s*:\s*\S", s) and "Register" in s:
            head, tail = re.match(r"^(If .*?[’'])\s*:\s*(.*)$", s).groups()
            condition = f"{head} — {tail}"
        elif (re.search(r":\s*(\[\d+\](,\s*\[\d+\])*)?\s*$", s) and
              (s.startswith("If ") or "Codes" in s or "code" in s.lower())) or \
                (s.startswith("If ") and "Register" in s and nxt is not None):
            condition = re.sub(r":\s*((\[\d+\](,\s*\[\d+\])*)?)\s*$", r" \1", s).strip()
        elif condition and not cond_has_values():
            condition += " — " + s  # sub-heading of a condition block
        elif values and nxt and re.fullmatch(r"0+", re.sub(r"\s", "", nxt.group(1))):
            # an un-coloned heading followed by a code list restarting at 0: a new value group
            if condition is None:
                head = " ".join(text).strip() or "(first group)"
                for v in values:
                    v["condition"] = head
            condition = s
        elif re.match(r"^(All other|Other|Any other)\b", s):
            text.append(s)
        elif values and values[-1]["code"] != "..." and values[-1]["condition"] == condition:
            values[-1]["meaning"] += " " + s
        else:
            text.append(s)
    if row["attr"] == "RV" or (name and name.upper().startswith("RESERVED")) or \
            (not name and not values and re.search(r"\breserved\b", " ".join(text), re.I)):
        name = name or "RESERVED"
    bl = bit_list(row["bits"])
    if not any(v["condition"] for v in values):
        for v in values:
            del v["condition"]
    field = {
        **({"source_errata": list(row["errata"])} if row.get("errata") else {}),
        "bits": row["bits"],
        "width": len(bl),
        "attribute": row["attr"],
        "default": row["default"],
        "name": name,
        "description": " ".join(text).strip(),
        "values": values,
    }
    return field


def _nums(meaning):
    return [(float(m.group(1)), m.group(3) or "") for m in NUM_RE.finditer(FOOTNOTE_RE.sub("", meaning))]


def expand_ellipses(field):
    """Fill '...' gaps of linear encodings; verified against every listed point after the gap start."""
    vals = field["values"]
    if not any(v["code"] == "..." for v in vals):
        return
    out = []
    for i, v in enumerate(vals):
        if v["code"] != "...":
            out.append(v)
            continue
        before = [x for x in vals[:i] if x["code"] != "..." and x.get("condition") == v.get("condition")]
        after = [x for x in vals[i + 1:] if x["code"] != "..." and x.get("condition") == v.get("condition")]
        filled = _fill_gap(before, after)
        if filled is None:
            out.append(v)  # leave the ellipsis; not provably linear
        else:
            out.extend(filled)
    field["values"] = out


def _fill_gap(before, after):
    if len(before) < 2 or not after:
        return None
    dc = lambda c: int(re.sub(r"^[xX]+", lambda m: "0" * len(m.group(0)), c), 2)  # leading don't-care bits
    try:
        codes = [dc(x["code"]) for x in before]
        b, z = before[-1], after[0]
        cb, cz = codes[-1], dc(z["code"])
    except ValueError:
        return None
    if cz <= cb + 1:
        return None
    # step size from the closest pair of consecutive codes listed before the gap
    pair = next(((before[i - 1], before[i]) for i in range(len(before) - 1, 0, -1)
                 if codes[i] - codes[i - 1] == 1), None)
    if pair is None:
        return None
    na, nb2 = _nums(pair[0]["meaning"]), _nums(pair[1]["meaning"])
    nb, nz = _nums(b["meaning"]), _nums(z["meaning"])
    if not nb or len(na) != len(nb) or len(nb2) != len(nb) or len(nz) != len(nb):
        return None
    tmpl_units = [u for _, u in nb]
    base = [x * UNIT_SCALE[u] for x, u in nb]
    step = [(y * UNIT_SCALE[u]) - (x * UNIT_SCALE[w]) for (x, w), (y, u) in zip(na, nb2)]
    if any(abs(st) < 1e-15 for st in step):
        return None
    # verify the far end of the gap (and anything after it) lies on the same line
    for pt in after:
        try:
            c = dc(pt["code"])
        except ValueError:
            return None
        np_ = _nums(pt["meaning"])
        if len(np_) != len(nb):
            return None
        for k, (x, u) in enumerate(np_):
            exp = base[k] + step[k] * (c - cb)
            got = x * UNIT_SCALE[u]
            if abs(exp - got) > max(1e-9, abs(exp) * 2e-3):
                return None
        break  # only the end point bounding this gap is required
    width = len(b["code"])
    tmpl = FOOTNOTE_RE.sub("", b["meaning"])
    filled = []
    for c in range(cb + 1, cz):
        it = iter(range(len(nb)))

        def repl(mo):
            k = next(it)
            val = (base[k] + step[k] * (c - cb)) / UNIT_SCALE[tmpl_units[k]]
            txt = f"{val:.4f}".rstrip("0").rstrip(".")
            return f"{txt}{mo.group(2)}{mo.group(3) or ''}"

        item = {"code": format(c, f"0{width}b"), "meaning": NUM_RE.sub(repl, tmpl), "interpolated": True}
        if "condition" in b:
            item["condition"] = b["condition"]
        filled.append(item)
    return filled


def apply_errata(regs, errata):
    """Correct obvious typos in the source tables; each fix is recorded on the field."""
    by_addr = {r["address"]: r for r in regs}
    for e in errata:
        reg = by_addr[e["address"]]
        for f in reg["fields"]:
            if f["bits"] != e["bits"]:
                continue
            hits = [v for v in f["values"] if v["code"] == e["from_code"]
                    and e.get("meaning_contains", "") in v["meaning"]
                    and (e.get("condition") is None or v.get("condition") == e["condition"])]
            if len(hits) != 1:
                raise SystemExit(f"erratum did not match exactly once: {e}")
            hits[0]["code"] = e["to_code"]
            f.setdefault("source_errata", []).append(
                f"Spec lists code {e['from_code']} for '{hits[0]['meaning']}'; corrected to {e['to_code']}. {e['note']}")


def fix_value_footnotes(line, f1, f2):
    """'125{f1} or 31.25{f2} mA/mW' (superscript notes glued to numbers) -> '125 mA/mW[f1] or 31.25 mA/mW[f2]'."""
    return re.sub(rf"(\d+(?:\.\d+)?){f1} or (\d+(?:\.\d+)?){f2} (mA/mW|A/W)\b",
                  lambda m: f"{m.group(1)} {m.group(3)}[{f1}] or {m.group(2)} {m.group(3)}[{f2}]", line)


def apply_recovered_values(regs, items):
    """The spec omits the 'code =' prefix of a value line; move that sentence from the description into a value."""
    by_addr = {r["address"]: r for r in regs}
    for it in items:
        f = next(f for f in by_addr[it["address"]]["fields"] if f["bits"] == it["bits"])
        i = f["description"].find(it["text_prefix"])
        if i < 0:
            raise SystemExit(f"recover_values did not match: {it}")
        f["values"].append({"code": it["code"], "meaning": f["description"][i:].strip()})
        f["description"] = f["description"][:i].strip()
        f.setdefault("source_errata", []).append(it["note"])


def apply_value_fills(regs, fills):
    """Replace an elided '...' with values derived by hand from the listed pattern (documented in meta)."""
    by_addr = {r["address"]: r for r in regs}
    for fl in fills:
        f = next(f for f in by_addr[fl["address"]]["fields"] if f["bits"] == fl["bits"])
        i = next(i for i, v in enumerate(f["values"]) if v["code"] == "...")
        f["values"][i:i + 1] = [dict(v, interpolated=True) for v in fl["values"]]
        f.setdefault("source_errata", []).append(fl["note"])


def group_values(field):
    """values -> value_groups: [{condition, values:[{code, meaning, interpolated?}]}]."""
    groups = []
    for v in field.pop("values"):
        cond = v.pop("condition", None)
        if not groups or groups[-1]["condition"] != cond:
            groups.append({"condition": cond, "values": []})
        groups[-1]["values"].append(v)
    field["value_groups"] = groups


def split_or_values(regs, items):
    """'X mA/mW[4] or Y mA/mW[5]' where notes 4/5 are conditions -> two value groups, one per condition."""
    by_addr = {r["address"]: r for r in regs}
    for it in items:
        f = next(f for f in by_addr[it["address"]]["fields"] if f["bits"] == it["bits"])
        out = []
        for g in f["value_groups"]:
            if not any(" or " in v["meaning"] for v in g["values"]):
                out.append(g)
                continue
            for k, cond in enumerate(it["conditions"]):
                vals = []
                for v in g["values"]:
                    parts = v["meaning"].split(" or ")
                    m = parts[k] if len(parts) == len(it["conditions"]) else v["meaning"]
                    nv = dict(v, meaning=FOOTNOTE_RE.sub("", m).strip())
                    vals.append(nv)
                c = f"{g['condition']} and {cond}" if g["condition"] else cond
                out.append({"condition": c, "values": vals})
        f["value_groups"] = out
        f.setdefault("source_errata", []).append(it["note"])


def resolve_aliases(regs):
    """'See encoding definition in 140[7:0]' -> copy field definitions from that register."""
    by_addr = {r["addr_int"]: r for r in regs}
    for r in regs:
        if len(r["fields"]) != 1:
            continue
        f = r["fields"][0]
        m = re.search(r"See encoding definition in (?:R|0x)?([0-9A-Fa-f]+)\s*\[7:0\]", f["description"])
        if not m:
            continue
        src = by_addr.get(int(m.group(1), 16))
        if not src:
            continue
        r["alias_of"] = src["address"]
        r["fields"] = [dict(copy.deepcopy(sf), attribute=f["attribute"], default=f["default"])
                       for sf in src["fields"]]


def main():
    txt, meta_path, out_path = sys.argv[1:4]
    meta = json.load(open(meta_path, encoding="utf-8"))
    raw = open(txt, encoding="utf-8").read()
    lines = clean_lines(raw)
    # the document's own list of tables gives the authoritative start page of each table
    toc, toc_addr = {}, {}
    for m in re.finditer(r"Table (\d+) — Register (0x[0-9A-Fa-f]+),?\s*\.{5,}\s*(\d+)", raw):
        toc[int(m.group(1))] = int(m.group(3))
        toc_addr[int(m.group(1))] = int(m.group(2), 16)
    segs = split_segments(lines, meta.get("start_marker", r"^11\s+Registers$"))
    regs, extra = [], []
    for seg in segs:
        hm = re.match(r"^Register (0x[0-9A-Fa-f]+)", seg["title"])
        if hm:
            # heading may carry a footnote ("Register 0x211,2" = 0x21 + notes 1,2): trust the TOC
            addr = toc_addr.get(seg["table"], int(hm.group(1), 16))
            seg["page"] = toc.get(seg["table"], seg["page"])
            for fx in meta.get("value_footnote_fix", []):
                if int(fx["address"], 16) == addr:
                    seg["lines"] = [fix_value_footnotes(l, fx["f1"], fx["f2"]) for l in seg["lines"]]
            regs.append(parse_register(seg, addr, meta.get("parser", "rows"),
                                       meta.get("digit_footnotes", False)))
        elif regs and seg["table"] not in meta.get("skip_tables", []):
            extra.append({"after": regs[-1]["address"], "table": seg["table"], "title": seg["title"],
                          "page": seg["page"], "text": "\n".join(l for l in seg["lines"] if l.strip())})
    apply_errata(regs, meta.get("errata", []))
    apply_value_fills(regs, meta.get("value_fills", []))
    apply_recovered_values(regs, meta.get("recover_values", []))
    for r in regs:
        for f in r["fields"]:
            expand_ellipses(f)
    resolve_aliases(regs)
    for r in regs:
        for lo, hi, region in meta["regions"]:
            if int(lo, 16) <= r["addr_int"] <= int(hi, 16):
                r["region"] = region
    for r in regs:
        for f in r["fields"]:
            group_values(f)
    split_or_values(regs, meta.get("split_or_values", []))
    out = json.dumps({"document": meta["document"], "registers": regs, "related_tables": extra},
                     ensure_ascii=False, indent=1)
    # one value object per line keeps the file compact and diff-friendly
    out = re.sub(r'\{\n\s*("code": [^{}]*?)\n\s*\}',
                 lambda m: "{" + re.sub(r"\n\s*", " ", m.group(1)) + "}", out)
    open(out_path, "w", encoding="utf-8").write(out + "\n")
    print(f"{len(regs)} registers, {len(extra)} related tables", file=sys.stderr)


if __name__ == "__main__":
    main()
