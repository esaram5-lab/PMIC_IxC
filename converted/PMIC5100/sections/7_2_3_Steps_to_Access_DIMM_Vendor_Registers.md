---
document: JESD301-2 (PMIC5100 Power Management IC Standard, Rev. 1.03, October 2022)
device: PMIC5100
application: client
section: 7.2.3
title: Steps to Access DIMM Vendor Registers
pages: 106-106
---
# 7.2.3 Steps to Access DIMM Vendor Registers

The steps to access DIMM vendor registers are as following:

```text
1.   Write to register Table 142, “Register 0x37” = 8 bit password LSB code
2.   Write to register Table 143, “Register 0x38” = 8 bit password MSB code
3.   Write to register Table 144, “Register 0x39” = 0x40.
4.   Perform Read operations to DIMM vendor registers as desired.
5.   Write to register Table 144, “Register 0x39” = 0x00.
```
