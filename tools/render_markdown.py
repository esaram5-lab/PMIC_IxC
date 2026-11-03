#!/usr/bin/env python3
"""Render registers.json into Markdown for retrieval / small-model use.

Usage:
    python3 tools/render_markdown.py converted/PMIC5030/registers.json converted/PMIC5030

Writes:
    <out>/registers/<addr>.md      one file per register, every value listed
    <out>/register_summary.md      all registers in one file, values as printed in the spec
"""
import json
import os
import re
import sys

BASE = {"RO": "Read Only (writes have no effect)", "RW": "Read/Write",
        "WO": "Write Only (reads return 0)", "W": "Write Only (reads return 0)",
        "RV": "Reserved (reads 0; host must not modify)"}
MOD = {"P": "Protected (writable only after the password is written)",
       "E": "Persistent across power cycle, erasable by command",
       "N": "Persistent across power cycle, not erasable by command",
       "A": "Persistent, set by the PMIC vendor at manufacturing"}
INTERP = "*"


def attr_text(a):
    if a == "1O":
        return "1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)"
    base = next((b for b in ("RO", "RW", "WO", "RV", "W") if a.startswith(b)), None)
    if base is None:
        return a
    parts = [BASE[base]]
    rest = a[len(base):]
    if rest.startswith("1O"):
        parts.append("Write '1' Only")
        rest = rest[2:]
    parts += [MOD[c] for c in rest if c in MOD]
    return f"{a} — " + "; ".join(parts)


def code_hex(code):
    if not re.fullmatch(r"[01]+", code) or len(code) < 4:
        return ""
    return f"0x{int(code, 2):0{(len(code) + 3) // 4}X}"


def default_meaning(field):
    d = re.sub(r"\s", "", field["default"])
    if not re.fullmatch(r"[01]+", d):
        return None
    hits = []
    for g in field["value_groups"]:
        for v in g["values"]:
            c = v["code"]
            if len(c) == len(d) and all(x in "xX" or x == y for x, y in zip(c, d)):
                hits.append((g["condition"], v["meaning"]))
    if not hits:
        return None
    if len(hits) == 1 or not any(h[0] for h in hits):
        return hits[0][1]
    return "; ".join(f"{m} (if {c})" for c, m in hits)


def front_matter(doc, reg):
    return "\n".join([
        "---",
        f"document: {doc['id']} ({doc['title']}, {doc['revision']}, {doc['date']})",
        f"device: {doc['device']}",
        f"application: {doc['application']} ({', '.join(doc['modules'])})",
        f"register: {reg['address']} ({reg['name']})",
        f"region: {reg.get('region', '')}",
        f"source: {doc['id']} Table {reg['source_table']}, page {reg['page']}",
        "---", ""])


def field_title(f):
    return f.get("name") or "(unnamed)"


def render_values(f, full=True):
    out = []
    if any(re.fullmatch(r"[01xX]+", v["code"]) and len(v["code"]) != f["width"]
           for g in f["value_groups"] for v in g["values"]):
        out.append(f"- Note: the codes below are wider than this {f['width']}-bit field; the encoding combines "
                   "bits from more than one field/register (see Description).")
    any_interp = False
    for g in f["value_groups"]:
        if g["condition"]:
            out.append(f"\n**When: {g['condition']}**\n")
        else:
            out.append("")
        show_hex = any(code_hex(v["code"]) for v in g["values"])
        out.append("| Code (bin) |" + (" Field hex |" if show_hex else "") + " Meaning |")
        out.append("|---|" + ("---|" if show_hex else "") + "---|")
        skipping = False
        for v in g["values"]:
            if v.get("interpolated"):
                any_interp = True
                if not full:
                    if not skipping:
                        out.append("| ... |" + (" ... |" if show_hex else "") + " ... |")
                    skipping = True
                    continue
            skipping = False
            mark = f" {INTERP}" if v.get("interpolated") and full else ""
            hx = f" {code_hex(v['code'])} |" if show_hex else ""
            meaning = v["meaning"].replace("|", "\\|")
            out.append(f"| {v['code']}{mark} |{hx} {meaning} |")
    if any_interp and full:
        out.append(f"\n{INTERP} Filled in from the listed pattern; the spec abbreviates this range with '...'.")
    return out


def render_field(f, full=True, level="##"):
    out = [f"{level} [{f['bits']}] {field_title(f)}", ""]
    if f.get("description"):
        out.append(f"- Description: {f['description']}")
    out.append(f"- Attribute: {attr_text(f['attribute'])}")
    dm = default_meaning(f)
    out.append(f"- Default: {f['default']}" + (f" → {dm}" if dm else ""))
    for e in f.get("source_errata", []):
        out.append(f"- Source correction: {e}")
    if f["value_groups"] and any(g["values"] for g in f["value_groups"]):
        out += render_values(f, full)
    elif f.get("name") != "RESERVED":
        out.append("- Values: no per-value encoding is listed in the spec for this field.")
    out.append("")
    return out


def render_register(doc, reg, related, full=True, front=True):
    names = ", ".join(field_title(f) for f in reg["fields"] if f.get("name") != "RESERVED") or "Reserved"
    out = [front_matter(doc, reg)] if front else []
    out.append(f"# {doc['device']} {reg['name']} ({reg['address']}) — {names}")
    out.append("")
    meta = [f"Region: {reg.get('region', '')}", f"Source: {doc['id']} Table {reg['source_table']}, p.{reg['page']}"]
    if reg.get("subtitle"):
        meta.insert(0, f"Title: {reg['subtitle']}")
    if reg.get("alias_of"):
        meta.append(f"Encoding: same as {reg['alias_of']} (spec: 'See encoding definition in "
                    f"{reg['alias_of'][2:]}[7:0]')")
    out.append(" | ".join(meta))
    out.append("")
    out.append("| Bits | Field | Attribute | Default |")
    out.append("|---|---|---|---|")
    for f in reg["fields"]:
        out.append(f"| {f['bits']} | {field_title(f)} | {f['attribute']} | {f['default']} |")
    out.append("")
    lvl = "##" if front else "###"
    for f in reg["fields"]:
        out += render_field(f, full, lvl)
    if reg["notes"]:
        out.append(f"{lvl} Notes" if front else "**Notes**")
        out.append("")
        out += [f"- {n}" for n in reg["notes"]]
        out.append("")
    for t in related:
        out.append(f"{lvl} Related: Table {t['table']} — {t['title']} (p.{t['page']})")
        out.append("")
        out.append("```text")
        out.append(t["text"])
        out.append("```")
        out.append("")
    return "\n".join(out)


def fname(addr):
    return f"{addr}.md"


def main():
    src, outdir = sys.argv[1:3]
    data = json.load(open(src, encoding="utf-8"))
    doc, regs = data["document"], data["registers"]
    rel = {}
    for t in data.get("related_tables", []):
        rel.setdefault(t["after"], []).append(t)
    rdir = os.path.join(outdir, "registers")
    os.makedirs(rdir, exist_ok=True)
    for f in os.listdir(rdir):
        if f.endswith(".md"):
            os.remove(os.path.join(rdir, f))
    for r in regs:
        with open(os.path.join(rdir, fname(r["address"])), "w", encoding="utf-8") as fh:
            fh.write(render_register(doc, r, rel.get(r["address"], [])))
    # one-file summary (values as printed in the spec; elided ranges stay elided)
    lines = [f"# {doc['device']} Register Map Summary", "",
             f"Source: {doc['id']} — {doc['title']}, {doc['revision']} ({doc['date']}). "
             f"Application: {doc['application']} ({', '.join(doc['modules'])}).", "",
             "Elided ranges ('...') follow the linear pattern of the neighbouring codes; "
             "see registers/<addr>.md for every value spelled out.", ""]
    for r in sorted(regs, key=lambda r: r["addr_int"]):
        lines.append(render_register(doc, r, rel.get(r["address"], []), full=False, front=False)
                     .replace(f"# {doc['device']} ", "## ", 1))
    with open(os.path.join(outdir, "register_summary.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    # index: one line per register, for lookup by address or field name
    idx = [f"# {doc['device']} Register Index", "",
           f"Source: {doc['id']} {doc['revision']} ({doc['date']}). One row per register; "
           "click through for every value and its meaning.", "",
           "| Address | Region | Fields (bits: name) | Source |", "|---|---|---|---|"]
    for r in sorted(regs, key=lambda r: r["addr_int"]):
        fl = "<br>".join(f"[{f['bits']}] {field_title(f)}" for f in r["fields"]
                         if f.get("name") != "RESERVED") or "Reserved"
        if r.get("alias_of"):
            fl += f"<br>(same encoding as {r['alias_of']})"
        title = f"{r['subtitle']}<br>" if r.get("subtitle") else ""
        idx.append(f"| [{r['address']}](registers/{fname(r['address'])}) | {r.get('region', '').split(' (')[0]} "
                   f"| {title}{fl} | Table {r['source_table']}, p.{r['page']} |")
    errata = [(r["address"], f["bits"], e) for r in regs for f in r["fields"] for e in f.get("source_errata", [])]
    if errata:
        idx += ["", "## Source corrections", "",
                "Obvious typos in the spec tables that were corrected during conversion:", ""]
        idx += [f"- {a} [{b}]: {e}" for a, b, e in errata]
    with open(os.path.join(outdir, "index.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(idx) + "\n")
    print(f"wrote {len(regs)} register files", file=sys.stderr)


if __name__ == "__main__":
    main()
