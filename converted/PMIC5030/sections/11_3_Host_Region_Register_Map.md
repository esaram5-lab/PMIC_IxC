---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 11.3
title: Host Region Register Map
pages: 124-132
---
# 11.3 Host Region Register Map

**Table 106 — Register Color Coding Scheme**

```text
        Region                                   Register Range                                    Restriction

Host Region + DIMM        Table 126, Register 0x15 to Table 152, Register 0x2F             Register Modification is
Vendor Region + Vendor    Table 155, Register 0x32 [7,5:0],                                NOT allowed in write-
specific Region           Table 159, Register 0x35,                                        protect mode

                          Table 180, Register 0x114 to Table 181, Register 0x115,
                          Table 182, Register 0x11A to Table 191, Register 0x123,
                          Table 192, Register 0x12E to Table 193, Register 0x12F
                          Table 232, Register 0x40 to Table 277, Register 0x6F
                          Register 0x70 to Register 0xFF

Host Region               Table 133, Register 0x1C to Table 150, Register 0x2D             Registers are copied from
                          Table 152, Register 0x2F [2]                                     DIMM Vendor Region
                          Table 182, Register 0x11A to Table 190, Register 0x122           Setting at power on
```

**Table 107 — Host Region - Register Map**: see [`index.md`](../index.md)
