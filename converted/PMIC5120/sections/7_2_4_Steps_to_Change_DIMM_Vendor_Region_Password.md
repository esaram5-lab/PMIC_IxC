---
document: JESD301-6 (PMIC5120 Power Management IC Standard, Version 1.0, February 2025)
device: PMIC5120
application: client
section: 7.2.4
title: Steps to Change DIMM Vendor Region Password
pages: 112-113
---
# 7.2.4 Steps to Change DIMM Vendor Region Password

By default, the DIMM vendor region register password is 0x9473. The steps to change the password from default password are as following:

```text
1.   Write to register Table 151, Register 0x37 = 0x73.
2.   Write to register Table 152, Register 0x38 = 0x94.
3.   Write to register Table 153, Register 0x39 = 0x40.
4.   Write to register Table 151, Register 0x37 = New 8 bit password LSB code as desired by DIMM vendor.
5.   Write to register Table 152, Register 0x38 = New 8 bit password MSB code as desired by DIMM
     vendor.

6.   Write to register Table 153, Register 0x39 = 0x80.
7.   Wait 200 ms.
8.   Write to register Table 153, Register 0x39 = 0x00.
9.   Power cycle the PMIC. (Remove VIN_Bulk supply from the PMIC. The new password is in effect after
     the power cycle.
```
