---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 3.3.2
title: Steps to Change DIMM Vendor Region Password
pages: 104-104
---
# 3.3.2 Steps to Change DIMM Vendor Region Password

By default, the DIMM vendor region register password is 0x9473. The steps to change the password from default password are as following:

```text
1. Write to register Table 144, “Register 0x37” = 0x73.
2. Write to register Table 145, “Register 0x38” = 0x94.
3. Write to register Table 146, “Register 0x39” = 0x40.
4. Write to register Table 144, “Register 0x37” = New 8 bit password LSB code as desired by DIMM vendor.
5. Write to register Table 145, “Register 0x38” = New 8 bit password MSB code as desired by DIMM vendor.
6. Write to register Table 146, “Register 0x39” = 0x80.
7. Wait 200 ms.
8. Write to register Table 146, “Register 0x39” = 0x00.
9. Power cycle the PMIC. (Remove VIN_Bulk and VIN_Mgmt supply from the PMIC. The new password is in
   effect after the power cycle.
```

To change the password again from this point on, repeat steps 1 to 8 but note that in steps 1 and 2 current password is required.
