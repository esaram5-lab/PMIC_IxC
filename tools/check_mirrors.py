#!/usr/bin/env python3
"""Compare each Host register with the DIMM/CAMM2 Vendor register it is copied from at power-on.

Usage: python3 tools/check_mirrors.py converted/PMIC5030/registers.json
Pairs come from notes like "configured identically by PMIC on its own as Table N, Register 0xXX".
Differences are either spec differences or extraction errors; review each one.
"""
import json,sys,re,collections
d=json.load(open(sys.argv[1])); R={r["addr_int"]:r for r in d["registers"]}
host=[r for r in d["registers"] if r.get("region","").startswith("Host")]
vend=[r for r in d["registers"] if "Vendor Region" in r.get("region","") and not r.get("region","").startswith("Vendor Specific")]
pairs=[]
for r in host:
    for n in r["notes"]:
        m=re.search(r"configured identically by PMIC on its own as Table \d+, “?Register (0x[0-9A-Fa-f]+)",n)
        if m: pairs.append((r["addr_int"],int(m.group(1),16)))
def sig(f):
    return (f["bits"], [ (v["code"],re.sub(r"\[\d+\]|\s+","",v["meaning"]).lower()) for g in f["value_groups"] for v in g["values"]])
diff=0
for h,v in pairs:
    if v not in R: print("  missing vendor reg",hex(v)); continue
    A=[f for f in R[h]["fields"]]; B=[f for f in R[v]["fields"]]
    sa={f["bits"]:f for f in A}; sb={f["bits"]:f for f in B}
    for b in sorted(set(sa)|set(sb)):
        fa,fb=sa.get(b),sb.get(b)
        if not fa or not fb: print(f"  {hex(h)}<->{hex(v)} [{b}] field only in {'host' if fa else 'vendor'}"); diff+=1; continue
        if fa["name"]!=fb["name"]: print(f"  {hex(h)}<->{hex(v)} [{b}] name {fa['name']} vs {fb['name']}"); diff+=1
        if sig(fa)!=sig(fb):
            va={c:m for c,m in sig(fa)[1]}; vb={c:m for c,m in sig(fb)[1]}
            ks=[k for k in set(va)|set(vb) if va.get(k)!=vb.get(k)]
            print(f"  {hex(h)}<->{hex(v)} [{b}] values differ ({len(ks)} codes) e.g. {ks[:1]} host={va.get(ks[0]) if ks else ''!s:.50} vendor={vb.get(ks[0]) if ks else ''!s:.50}"); diff+=1
        if re.sub(r"\s","",fa["default"])!=re.sub(r"\s","",fb["default"]): print(f"  {hex(h)}<->{hex(v)} [{b}] default {fa['default']} vs {fb['default']}"); diff+=1
print(f"host {len(host)} vendor {len(vend)} mirrored pairs {len(pairs)} field diffs {diff}")
