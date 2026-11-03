---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 8.2
title: Register Map Breakdown
pages: 125-127
---
# 8.2 Register Map Breakdown

**Table 105 — Register Map Breakdown**

```text
Register Range               Region                                       Comments
  0x00 - 0x3F              Host Region        Host Accessible Registers
  0x40 - 0x6F             CAMM2 Vendor        CAMM2 Vendor Registers - Non Volatile Memory
                             Region           Allows CAMM2 vendors to program the PMIC for a given DRAM/CAMM2
                                              vendor designs.
                                              These are password protected registers and password is selected by
                                              CAMM2 vendor. Under normal operation, these registers are not used by
                                              any host.
                                              These registers require password for read access. Access to these registers
                                              without correct password will return all data as ‘0’.
                                            These registers require complete power cycle before it takes effect.
                                            Changing these registers under normal operation is considered an illegal
                                            operation.
  0x70 - 0xFF        Vendor Specific Region Vendor Specific Registers - Non Volatile Memory
                                              These are vendor specific password protected registers. Under normal
                                              operation these registers are not used by any host.
                                              These registers require password for read access. Access to these registers
                                              without correct password will return all data as ‘0’.
 0x100 - 0x13F             Host Region        Host Accessible Registers
```

## 8.2.1 Memory Protection

The CAMM2 vendor region registers (0x40 - 0x6F) are password protected registers. Both Read and Write access to CAMM2 vendor registers are blocked unless it is unlocked by providing the correct password. The default password for CAMM2 vendor register is 0x9473. The PMIC offers each CAMM2 vendors to select their own password for CAMM2 vendor registers.

## 8.2.2 Steps to Access CAMM2 Vendor Registers

The steps to access CAMM2 vendor registers are as follows:

```text
1.      Write to register Table 159, Register 0x37 = 8 bit password LSB code
2.      Write to register Table 160, Register 0x38 = 8 bit password MSB code
3.      Write to register Table 161, Register 0x39 = 0x40.
4.      Perform Read operations to CAMM2 vendor registers as desired.
5.      Write to register Table 161, Register 0x39 = 0x00.
```

## 8.2.3 Steps to Change CAMM2 Vendor Region Password

By default, the CAMM2 vendor region register password is 0x9473. The steps to change password from default password are as follows:

```text
1.      Write to register Table 159, Register 0x37 = 0x73.

2.      Write to register Table 160, Register 0x38 = 0x94.
3.      Write to register Table 161, Register 0x39 = 0x40.

4.      Write to register Table 159, Register 0x37 = New 8 bit password LSB code as desired by CAMM2
        vendor.

5.      Write to register Table 160, Register 0x38 = New 8 bit password MSB code as desired by CAMM2
        vendor.
6.      Write to register Table 161, Register 0x39 = 0x80.
7.      Wait 200 ms.
8.      Write to register Table 161, Register 0x39 = 0x00.
9.      Power cycle the PMIC. (Remove VIN_Bulk supply from the PMIC. The new password is in effect
        after the power cycle)
```

## 8.2.4 Steps to Burn or Program CAMM2 Vendor Region Registers

The steps to burn or to program CAMM2 vendor registers are as follows:

```text
1.      Write to register Table 159, Register 0x37 = 8 bit password LSB code
2.      Write to register Table 160, Register 0x38 = 8 bit password MSB code
3.      Write to register Table 161, Register 0x39 = 0x40.
4.      Programming CAMM2 vendor registers are done at block level. Block 40 addresses: 0x40 - 0x4F;
        Block 50 addresses: 0x50 - 0x5F; Block 60 addresses: 0x60 - 0x6F. Perform write operation to each
        block as desired.

5.        Burn each block one at a time: Block 40 addresses: Write register Table 161, Register 0x39 = 0x81.
          Block 50 addresses: Write register Table 161, Register 0x39 = 0x82. Block 60 addresses: Write
          register Table 161, Register 0x39 = 0x85. Note that there is an exception to Block 60 addresses.
          Four registers (Table 211, Register 0x6D [4,0], Table 212, Register 0x6E [4,0]) require different code
          which is Table 161, Register 0x39 = 0x86.
6.        Wait time 200 ms.
7.        To check if programming is complete: Perform read from register Table 161, Register 0x39. The
          code 0x5A indicates it is complete. It takes approximately 200 ms per page to program.
8.        To verify if programming is done correctly: Perform read operation from appropriate block
          addresses.
9.        Write to register Table 161, Register 0x39 = 0x00.
```
