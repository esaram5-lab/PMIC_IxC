---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 11.2
title: Register Map Breakdown
pages: 122-124
---
# 11.2 Register Map Breakdown

**Table 105 — Register Map Breakdown**

```text
Register Range              Region                                                 Comments
   0x00 - 0x3F            Host Region        Host Accessible Registers
   0x40 - 0x6F            DIMM Vendor        DIMM Vendor Registers - Non Volatile Memory
                             Region          Allows DIMM vendors to program the PMIC for a given DRAM/DIMM vendor
                                             designs.
                                             These are password protected registers and password is selected by DIMM
                                             vendor. Under normal operation, these registers are not used by any host.
                                             These registers require password for read access. Access to these registers
                                             without correct password will return all data as ‘0’.
                                             These registers require complete power cycle before it takes in effect.
                                             Changing these registers under normal operation is considered an illegal
                                             operation.
   0x70 - 0xFF           Vendor Specific     Vendor Specific Registers - Non Volatile Memory
                            Region           These are vendor specific password protected registers. Under normal
                                             operation these registers are not used by any host.
                                             These registers require password for read access. Access to these registers
                                             without correct password returns all data as ‘0’.
  0x100 - 0x15D           Host Region        Host Accessible Registers
```

## 11.2.1 Register Memory Protection

The PMIC DIMM vendors registers (0x40 - 0x6F) are password protected registers. Both Read and Write access to DIMM vendor registers are blocked unless it is unlocked by providing the correct password. The default password for DIMM vendor registers is 0x9473. The PMIC offers DIMM vendors to select their own password for DIMM vendor registers.

## 11.2.2 Steps to Access DIMM Vendor Region Registers

The steps to access the DIMM vendor registers are as follows:

```text
1.   Write to register Table 160, Register 0x37 = 8 bit password LSB code.
2.   Write to register Table 161, Register 0x38 = 8 bit password MSB code.
3.   Write to register Table 162, Register 0x39 = 0x40.
4.   Perform Read operations to DIMM vendor registers as desired.
5.   Write to register Table 162, Register 0x39 = 0x00.
```

## 11.2.3 Steps to Change DIMM Vendor Region Password

By default, the DIMM vendor region register password is 0x9473. The steps to change the password from default password are as follows:

1.  Write to register Table 160, Register 0x37 = 0x73.

2.  Write to register Table 161, Register 0x38 = 0x94.

3.  Write to register Table 162, Register 0x39 = 0x40.

4.  Write to register Table 160, Register 0x37 = New 8 bit password LSB code as desired by DIMM vendor.

5.  Write to register Table 161, Register 0x38 = New 8 bit password MSB code as desired by DIMM vendor.

6.  Write to register Table 162, Register 0x39 = 0x80.

7.  Wait 200 ms.

8.  Write to register Table 162, Register 0x39 = 0x00.

9.  Power cycle the PMIC. (Remove VIN_Bulk and VIN_Mgmt supply from the PMIC. The new password

```text
is in effect after the power cycle.
```

To change the password again from this point on, repeat steps 1 to 8 but note that in steps 1 and 2 current password is required.

## 11.2.4 Steps to Burn or Program DIMM Vendor Region Registers

The steps to burn or to program the DIMM vendor registers are as follows:

```text
1.   Write to register Table 160, Register 0x37 = 8 bit password LSB code.
2.   Write to register Table 161, Register 0x38 = 8 bit password MSB code.
3.   Write to register Table 162, Register 0x39 = 0x40.
4.   Programming DIMM vendor registers are done at block level. Block 40 addresses: 0x40 - 0x4F; Block
     50 addresses: 0x50 - 0x5F; Block 60 addresses: 0x60 - 0x6F. Perform write operation to each block as
     desired.
5.   Burn each block one at a time: Block 40 addresses: Write register Table 162, Register 0x39 = 0x81.
     Block 50 addresses: Write register Table 162, Register 0x39 = 0x82. Block 60 addresses: Write register
     Table 162, Register 0x39 = 0x85.
6.   Wait time 200 ms.
7.   To check if programming is complete: Perform read from register Table 162, Register 0x39. The code
     0x5A indicates it is complete. It takes 200 ms per block to program.
8.   To verify if programming is done correctly: Perform read operation from appropriate block addresses.
9.   Write to register Table 162, Register 0x39 = 0x00.
```
