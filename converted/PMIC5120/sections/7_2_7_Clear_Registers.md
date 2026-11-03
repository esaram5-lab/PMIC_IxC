---
document: JESD301-6 (PMIC5120 Power Management IC Standard, Version 1.0, February 2025)
device: PMIC5120
application: client
section: 7.2.7
title: Clear Registers
pages: 115-115
---
# 7.2.7 Clear Registers

For each Real Time Status Registers (Table 104, Register 0x08 [6:5,3:2,0], Table 105, Register 0x09 [7,5,3,1:0], Table 106, Register 0x0A [7,5:1], Table 107, Register 0x0B [7,5:3,1:0], Table 147, Register 0x33 [2]), the DDR5 PMIC offers a way to clear the status of each event. The clear registers are Table 112, Register 0x10 [5,3:2,0], Table 113, Register 0x11 [7,5,3,1:0], Table 114, Register 0x12 [7,5:2], Table 115, Register 0x13 [7,5:3,1:0] and to Table 116, Register 0x14 [2] respectively. All clear registers are write ‘1’ only registers. When ‘1’ is written to any of the clear registers, the PMIC updates the status registers to default state and removes the interrupt condition on GSI_n and PWR_GOOD output signal assuming that event is no longer present. If the failing condition is still present, the status register will still remain at ‘1’. Note that GSI_n and PWR_GOOD interrupt is only applicable if that event is not masked. GSI_n output signal can be disabled.

When ‘1’ is written to any of the clear registers, there are three categories of response by the PMIC.

```text
1.   PMIC removes GSI_n interrupt (PWR_GOOD interrupt is not applicable. Related status registers are:
     Table 113, Register 0x11 [7,3,1:0], Table 115, Register 0x13 [7,5:4].
2.   PMIC removes GSI_n and PWR_GOOD interrupt. Related status registers are: Table 112, Register
     0x10 [5,3:2], Table 113, Register 0x11 [5], Table 116, Register 0x14 [2].

3.   PMIC only removes GSI_n interrupt and does not remove PWR_GOOD interrupt. Related status regis-
     ters are: Table 112, Register 0x10 [0], Table 114, Register 0x12 [7,5:4], Table 115, Register 0x13

     [3,1:0]. The host is expected to either power cycle the PMIC or re-issue the VR Enable command if

     PMIC is in programmable mode.
```

The PMIC offers a Global Clear command by writing ‘1’ to registers Table 116, Register 0x14 [0]. This command works same way as individual clear command. This command can alternatively be used by the host if more than one clear command is required to different registers.
