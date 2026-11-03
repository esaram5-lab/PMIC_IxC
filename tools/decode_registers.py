#!/usr/bin/env python3
"""Decode PMIC register values into field-by-field meanings.

Usage:
    python3 tools/decode_registers.py converted/PMIC5030/registers.json 0x21=0x78 0x2B=0x20
    python3 tools/decode_registers.py converted/PMIC5030/registers.json --dump dump.txt

Dump file: one register per line, "ADDR VALUE" or "ADDR=VALUE" or "ADDR: VALUE" (hex, 0x optional).
If a condition register (e.g. 0x1A, 0x32) is also in the input, it is shown next to
the matching value group so the right interpretation can be picked.
"""
import json
import re
import sys


def bit_list(bits):
    out = []
    for part in bits.split(","):
        if ":" in part:
            hi, lo = map(int, part.split(":"))
            out.extend(range(hi, lo - 1, -1))
        else:
            out.append(int(part))
    return out


def parse_pairs(items):
    pairs = []
    for it in items:
        m = re.match(r"^\s*(?:0x)?([0-9A-Fa-f]+)\s*[=:\s]\s*(?:0x)?([0-9A-Fa-f]{1,2})\s*$", it)
        if not m:
            if it.strip() and not it.strip().startswith("#"):
                print(f"skip: {it!r}", file=sys.stderr)
            continue
        pairs.append((int(m.group(1), 16), int(m.group(2), 16)))
    return pairs


def match(code, value_bits):
    c = code.lower()
    if re.fullmatch(r"0x[0-9a-f]+", c):
        return int(c, 16) == int(value_bits, 2)
    if re.fullmatch(r"[0-9a-f]{2}h", c):
        return int(c[:-1], 16) == int(value_bits, 2)
    if not re.fullmatch(r"[01x]+", c):
        return False
    return len(code) == len(value_bits) and all(c in "xX" or c == v for c, v in zip(code, value_bits))


COND_RE = re.compile(r"Register (0x[0-9A-Fa-f]+),?\s*\[(\d+)(?::(\d+))?\]\s*=\s*[‘'](\d+)[’']")


def eval_condition(cond, known):
    """True/False if the condition names a register present in the input, else None."""
    if not cond:
        return None
    result = None
    for m in COND_RE.finditer(cond):  # every named register condition must hold
        addr = int(m.group(1), 16)
        if addr not in known:
            continue
        hi = int(m.group(2))
        lo = int(m.group(3)) if m.group(3) else hi
        bits = "".join(str((known[addr] >> b) & 1) for b in range(hi, lo - 1, -1))
        if bits != m.group(4):
            return False
        result = True
    return result


def combined_code(text, addr, known, own_bits="7:0"):
    """Assemble a multi-field code, e.g. 'bits [7:6] and bit [0]' or 'Register 0x100 [7:6] plus this 8 bit register'."""
    refs = []
    m = re.search(r"bits \[(\d+:\d+)\] and bit \[(\d+)\]", text)
    braces = re.search(r"\{(R[0-9A-Fa-f]+\[[\d:]+\](?:\s*,\s*R[0-9A-Fa-f]+\[[\d:]+\])+)\}", text)
    if braces:  # "3-bit encoding with {R36[7],R22[1:0]}"
        refs = [(int(a, 16), b) for a, b in re.findall(r"R([0-9A-Fa-f]+)\[([\d:]+)\]", braces.group(1))]
    elif m:
        refs = [(addr, m.group(1)), (addr, m.group(2))]
    else:
        for ra, rb in re.findall(r"Register (0x[0-9A-Fa-f]+),?\s*\[(\d+(?::\d+)?)\](?!\s*=)", text):
            refs.append((int(ra, 16), rb))
        if re.search(r"this (\d+|one|two|three|four|five|six|seven|eight) bit register", text):
            refs.append((addr, own_bits))
    if not refs or any(a not in known for a, _ in refs):
        return None
    return "".join(str((known[a] >> b) & 1) for a, bits in refs for b in bit_list(bits))


def decode(reg, val, known):
    out = [f"{reg['address']} ({reg['name']}) = 0x{val:02X} = {val:08b}b"
           f"   [{reg.get('region', '')}; Table {reg['source_table']}, p.{reg['page']}]"]
    for f in reg["fields"]:
        bl = bit_list(f["bits"])
        code = "".join(str((val >> b) & 1) for b in bl)
        name = f.get("name") or "(unnamed)"
        head = f"  [{f['bits']}] {name} = {code}b"
        if name == "RESERVED":
            out.append(head + "  (reserved)")
            continue
        hits, missing = [], []
        for g in f["value_groups"]:
            c = code
            widths = {len(v["code"]) for v in g["values"]
                      if re.fullmatch(r"[01xX]+", v["code"]) and not v["code"].lower().startswith("0x")}
            if widths and f["width"] not in widths:
                c = combined_code(f["description"] + " " + (g["condition"] or ""), reg["addr_int"], known, f["bits"])
                if c is None or len(c) not in widths:
                    missing.append((g["condition"], widths))
                    continue
            hits += [(g["condition"], v, c) for v in g["values"] if match(v["code"], c)]
        if missing and not hits:
            w = "/".join(str(x) for _, ws in missing for x in sorted(ws))
            out.append(head + f"  -> combined {w}-bit encoding; add the other register(s) named in the "
                       f"spec to the input to decode. See registers/{reg['address']}.md")
            continue
        if True:
            if not hits:
                out.append(head + ("  -> no listed encoding for this code (reserved/undefined)"
                                   if f["value_groups"] else f"  -> {f['description'][:160]}"))
                continue
            applicable = [h for h in hits if eval_condition(h[0], known) is not False]
            if len(applicable) == 1:
                cond, v, c = applicable[0]
                extra = f" (combined code {c}b)" if c != code else ""
                tag = ""
                if cond:
                    tag = "   [applies: " if eval_condition(cond, known) else "   [if "
                    tag += re.sub(r"^If\s+", "", cond) + "]"
                out.append(head + extra + f"  -> {v['meaning']}" + tag)
            else:
                out.append(head)
                for cond, v, c in applicable:
                    out.append(f"      -> {v['meaning']}   [if {re.sub(r'^If\\s+', '', cond or '')}]")
    return "\n".join(out)


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    data = json.load(open(sys.argv[1], encoding="utf-8"))
    regs = {r["addr_int"]: r for r in data["registers"]}
    args = sys.argv[2:]
    if args[0] == "--dump":
        items = open(args[1], encoding="utf-8").read().splitlines()
    else:
        items = args
    pairs = parse_pairs(items)
    known = dict(pairs)  # also used to evaluate conditions and multi-register encodings
    print(f"# {data['document']['device']} ({data['document']['id']} {data['document']['revision']})")
    for addr, val in pairs:
        reg = regs.get(addr)
        if reg is None:
            print(f"0x{addr:02X} = 0x{val:02X}: not defined in this register map "
                  f"(vendor-specific, password-protected or reserved address)")
            continue
        print(decode(reg, val, known))


if __name__ == "__main__":
    main()
