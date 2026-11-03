---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 3.3.4
title: Host Region Register Map
pages: 105-110
---
# 3.3.4 Host Region Register Map

**Table 92 — Register Color Coding Scheme**

```text
        Region                                   Register Range                              Restriction
                             Table 111, “Register 0x15” to Table 137, “Register 0x2F”
Host Region + DIMM           Table 140, “Register 0x32” [7,5:0],                        Register Modification is
Vendor Region + Vendor       Table 143, “Register 0x35”                                 NOT allowed in write
specific Region              Table 152, “Register 0x40” to Register 0x6F                protect mode
                             Register 0x70 to Register 0xFF
                                                                                        Registers are copied from
                             Table 122, “Register 0x20” to
      Host Region                                                                       DIMM Vendor Region
                             Table 135, “Register 0x2D”
                                                                                        Setting at power on
```

.

**Table 93 — Host Region - Register Map**: see [`index.md`](../index.md)
