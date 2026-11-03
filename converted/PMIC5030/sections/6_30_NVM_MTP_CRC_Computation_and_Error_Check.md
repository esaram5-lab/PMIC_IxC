---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 6.30
title: NVM MTP CRC Computation and Error Check
pages: 59-62
---
# 6.30 NVM MTP CRC Computation and Error Check

The PMIC has non-volatile MTP for DIMM vendor region and PMIC vendor specific region. The PMIC5030 shall perform the non-volatile MTP memory error check at first power on when VIN_Mgmt input supply is applied. The PMIC checks for MTP memory error (due to memory loss or bit flipping or any other internal functional or timing fault related to MTP memory) to ensure that PMIC does not inadvertently turn on the regulators with incorrect MTP memory content. This increases the PMIC reliability in the system.

The PMIC performs two independent checks. One for DIMM vendor memory region and other for PMIC vendor memory region.

## 6.30.1 DIMM Vendor Region MTP Check

During the assembly phase of the DIMM, the DIMM vendor programs the entire DIMM region; computes and programs the 8-bit CRC code in Table 277, Register 0x6F [7:0] using the polynomial as noted below. The seed value is all zero.

```text
▪ C(X) = X8 + X2 + X1 + 1
```

The CRC computation shall include the DIMM vendor region as shown below in the exact same order. All reserved bits must be included as ‘0’ in the computation. Total of 376 bits.

```text
▪ R40 [7:0], R41 [7:0], R42 [7:0], ..., R4E [7:0], R4F [7:0]
▪ R50 [7:0], R51 [7:0], R52 [7:0], ..., R5E [7:0], R5F [7:0]
▪ R60 [7:0], R61 [7:0], R62 [7:0], ..., R6E [7:0]
```

The PMIC performs DIMM vendor region MTP memory check at power on and sets the Table 177, Register 0x10A [7] = ‘1’ to inform controller that PMIC has performed this check. The PMIC performs the same computation of the DIMM vendor region as noted above to generate the 8-bit CRC code and compares it against what the DIMM vendor has programmed in Table 277, Register 0x6F [7:0]. If there is no mismatch in CRC code, the PMIC keeps Table 177, Register 0x10A [6] = ‘0’ and allows normal operation to enable the output regulators.

If there is mismatch in CRC code, the PMIC sets the Table 177, Register 0x10A [6] = ‘1’ and blocks PMIC to turn on the regulator with any method (via I2C/I3C bus command or via VR_OE pin or Auto turn on) if Table 163, Register 0x3A [1] = ‘0’. The PMIC also updates the error counter in Table 108, Register 0x03 [7:4]. All VR Enable commands from this point on are ignored by the PMIC. At this point, there are three options controller may take:

```text
▪ Re-cycle the power to the PMIC and try again.
▪ Isolate and map out the PMIC as described in Section 10.
▪ Instruct PMIC to bypass the DIMM CRC Error Status in Table 177, Register 0x10A [6] by setting
  Table 163, Register 0x3A [1] = ‘1’ and execute subsequent VR Enable command to turn on the
  regulators.
```

The status registers Table 177, Register 0x10A [7:6] cannot be cleared by the controller. The error log register Table 108, Register 0x03 [7:4] cannot be cleared by the controller and MTP cannot be erased by the controller. Note that only if the status register Table 177, Register 0x10A [6] = ‘1’, the PMIC blocks the VR enable command. The error log register Table 108, Register 0x03 [7:4] does not block the VR enable command. When error injection function is applied, the PMIC shall not update Table 108, Register 0x03 [7:4]; it only updates Table 177, Register 0x10A [6] = ‘1’. This error injection feature is only allowed prior to VR Enable command.

## 6.30.2 PMIC Vendor Region MTP Check

The PMIC vendor region memory check is implementation specific. The PMIC may choose to implement similar method as DIMM vendor region where it may compute and program the 8-bit CRC code in its own proprietary register space and check at power on. Alternatively, PMIC may choose to implement a different method. Regardless of which method PMIC chooses to implement, the PMIC shall check and guarantee that its memory content is valid at power on. If there is an error in PMIC’s own memory content, PMIC sets Table 177, Register 0x10A [4] = ‘1’ and blocks PMIC to turn on the regulator with any method (via I2C/I3C bus command or via VR_OE pin or Auto turn on). The PMIC also updates the error counter in Table 108, Register 0x03 [3:0]. All VR Enable command from this point on are ignored by the PMIC. At this point, the controller may take one of the two options as noted in Clause 6.30.1. The status registers Table 177, Register 0x10A [5:4] cannot be cleared by the controller. The error log register Table 108, Register 0x03 [3:0] cannot be cleared by the controller and MTP cannot be erased by the controller. Note that only if the status register Table 177, Register 0x10A [4] = ‘1’, the PMIC blocks the VR enable command. The error log register Table 108, Register 0x03 [3:0] does not block the VR enable command. When error injection function is applied, the PMIC shall not update Table 108, Register 0x03 [3:0]; it only updates Table 177, Register 0x10A [4] = ‘1’. This error injection feature is only allowed prior to VR Enable command.

## 6.30.3 DIMM Vendor Region CRC Check on Demand

During the assembly phase of the DIMM, the DIMM vendor programs the entire DIMM region including the 8-bit CRC code as described in Clause 6.30.1. To aid DIMM vendor to make sure that DIMM vendor region value and the corresponding CRC code is correct prior to burning the DIMM vendor region and the 8-bit CRC code, the PMIC offers a mechanism to do a test to ensure there is no error in CRC code. The steps are outlined as follows:

1. DIMM vendor computes 8-bit CRC code of the DIMM region (0x40 to 0x6E)

2. DIMM vendor writes entire DIMM region including the CRC code (R0x40 to R0x6F) in the PMIC. At

```text
this point, the burn command is not issued.
```

3. Write Table 163, Register 0x3A [0] = ‘1’ to instruct PMIC to compute 8-bit CRC code of DIMM

```text
region (0x40 to 0x6E) and check against the value programmed in R0x6F.
```

4. PMIC sets Table 176, Register 0x109 [0] = ‘1’ if 8-bit CRC code it computed does not match with

```text
the 8-bit CRC code written by the DIMM vendor in Table 277, Register 0x6F; if there is a match,
the PMIC keeps the Table 176, Register 0x109 [0] = ‘0’.
```

5. DIMM vendor reads the Table 176, Register 0x109 [0] status. If it is set to ‘1’, the DIMM vendor

```text
clears this status register by writing Table 179, Register 0x10F [0] = ‘1’ and repeats steps 1 to 3. If
it is ‘0’, the DIMM vendor performs the burn command by writing Table 162, Register 0x39 for each
of the three blocks.
```
