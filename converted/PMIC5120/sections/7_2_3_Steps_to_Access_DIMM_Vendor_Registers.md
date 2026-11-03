---
document: JESD301-6 (PMIC5120 Power Management IC Standard, Version 1.0, February 2025)
device: PMIC5120
application: client
section: 7.2.3
title: Steps to Access DIMM Vendor Registers
pages: 112-112
---
# 7.2.3 Steps to Access DIMM Vendor Registers

The steps to access the DIMM vendor registers are as following:

```text
1.   Write to register Table 151, Register 0x37 = 8 bit password LSB code.
2.   Write to register Table 152, Register 0x38 = 8 bit password MSB code.
3.   Write to register Table 153, Register 0x39 = 0x40.
4.   Perform Read operations to DIMM vendor registers as desired.
5.   Write to register Table 153, Register 0x39 = 0x00.
```
