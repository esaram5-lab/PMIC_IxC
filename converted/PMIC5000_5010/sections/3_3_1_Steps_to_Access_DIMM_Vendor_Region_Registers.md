---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 3.3.1
title: Steps to Access DIMM Vendor Region Registers
pages: 103-104
---
# 3.3.1 Steps to Access DIMM Vendor Region Registers

The steps to access the DIMM vendor registers are as following:

```text
1. Write to register Table 144, “Register 0x37” = 8 bit password LSB code.
2. Write to register Table 145, “Register 0x38” = 8 bit password MSB code.
3. Write to register Table 146, “Register 0x39” = 0x40.
4. Perform Read operations to DIMM vendor registers as desired.
5. Write to register Table 146, “Register 0x39” = 0x00.
```
