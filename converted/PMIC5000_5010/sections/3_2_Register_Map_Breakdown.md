---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 3.2
title: Register Map Breakdown
pages: 103-103
---
# 3.2 Register Map Breakdown

**Table 91 — Register Map Breakdown**

```text
Register Range        Region                                         Comments
 0x00 - 0x3F        Host Region         Host Accessible Registers
                                        DIMM Vendor Registers - Non Volatile Memory
                                        Allows DIMM vendors to program the PMIC for a given DRAM/DIMM
                                        vendor designs.
                                        These are password protected registers and password is selected by
                                        DIMM vendor. Under normal operation, these registers are not used by
                   DIMM Vendor
  0x40 - 0x6F                           any host.
                      Region
                                        These registers require password for read access. Access to these
                                        registers without correct password will return all data as ‘0’.
                                        These registers require complete power cycle before it takes in effect.
                                        Changing these registers under normal operation is considered an illegal
                                        operation.
                                        Vendor Specific Registers - Non Volatile Memory
                                        These are vendor specific password protected registers. Under normal
                   Vendor Specific
 0x70 - 0xFF                            operation these registers are not used by any host.
                      Region
                                        These registers require password for read access. Access to these
                                        registers without correct password will return all data as ‘0’.
```
