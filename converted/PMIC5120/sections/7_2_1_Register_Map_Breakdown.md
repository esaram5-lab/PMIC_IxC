---
document: JESD301-6 (PMIC5120 Power Management IC Standard, Version 1.0, February 2025)
device: PMIC5120
application: client
section: 7.2.1
title: Register Map Breakdown
pages: 112-112
---
# 7.2.1 Register Map Breakdown

**Table 92 — Register Map Breakdown**

```text
Register Range            Region                                          Comments
 0x00 - 0x3F            Host Region           Host Accessible Registers
                                              DIMM Vendor Registers - Non Volatile Memory
                                              Allows DIMM vendors to program the PMIC for a given DRAM/
                                              DIMM vendor designs.
                                              These are password protected registers and password is selected by
                                              DIMM vendor. Under normal operation, these registers are not used
  0x40 - 0x6F      DIMM Vendor Region         by any host.
                                              These registers require password for read access. Access to these
                                              registers without correct password will return all data as ‘0’.
                                              These registers require complete power cycle before it takes in
                                              effect. Changing these registers under normal operation is considered
                                              an illegal operation.
                                              Vendor Specific Registers - Non Volatile Memory
                                              These are vendor specific password protected registers. Under
  0x70 - 0xFF      Vendor Specific Region     normal operation these registers are not used by any host.
                                              These registers require password for read access. Access to these
                                              registers without correct password will return all data as ‘0’.
```
