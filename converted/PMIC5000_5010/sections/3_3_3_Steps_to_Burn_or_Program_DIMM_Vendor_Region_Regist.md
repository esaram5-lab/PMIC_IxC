---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 3.3.3
title: Steps to Burn or Program DIMM Vendor Region Registers
pages: 104-105
---
# 3.3.3 Steps to Burn or Program DIMM Vendor Region Registers

The steps to burn or to program the DIMM vendor registers are as following:

```text
1. Write to register Table 144, “Register 0x37” = 8 bit password LSB code.
2. Write to register Table 145, “Register 0x38” = 8 bit password MSB code.
3. Write to register Table 146, “Register 0x39” = 0x40.

4. Programming DIMM vendor registers are done at block level. Block 40 addresses: 0x40 - 0x4F; Block 50
   addresses: 0x50 - 0x5F; Block 60 addresses: 0x60 - 0x6F. Perform write operation to each block as desired.

5. Burn each block one at a time: Block 40 addresses: Write register Table 146, “Register 0x39” = 0x81. Block

   50 addresses: Write register Table 146, “Register 0x39” = 0x82. Block 60 addresses: Write register
   Table 146, “Register 0x39” = 0x85.
6. Wait time 200 ms.
7.   To check if programming is complete: Perform read from register Table 146, “Register 0x39”. The code
     0x5A indicates it is complete. It takes 200 ms per page to program.
8. To verify if programming is done correctly: Perform read operation from appropriate block addresses.
9. Write to register Table 146, “Register 0x39” = 0x00.
```
