---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 8.4.2
title: Clear Registers
pages: 146-149
---
# 8.4.2 Clear Registers

For each Real Time Status Registers (Table 112, Register 0x08 [6:2,0], Table 113, Register 0x09 [7,5,3:0], Table 114, Register 0x0A [7:1], Table 115, Register 0x0B [7:0], and Table 155, Register 0x33 [3:2]), the CAMM2 PMIC offers a way to clear the status of each event. The clear registers are Table 120, Register 0x10 [5:2,0], Table 121, Register 0x11 [7,5,3:0], Table 122, Register 0x12 [7:2] Table 123, Register 0x13 [7:0], and Table 124, Register 0x14 [3:2], respectively. All clear registers are write ‘1’ only registers. When ‘1’ is written to any of the clear registers, the PMIC updates the status registers to default state and removes the interrupt condition on GSI_n and PWR_GOOD output signal, assuming that event is no longer present. If the failing condition is still present, the status register will still remain at ‘1’. Note that GSI_n and PWR_GOOD interrupt is only applicable if that event is not masked. GSI_n output signal can be disabled. When ‘1’ is written to any of the clear registers, there are three categories of response by the PMIC.

• PMIC removes GSI_n interrupt (PWR_GOOD interrupt is not applicable). Related status registers

```text
are: Table 121, Register 0x11 [7,3:0], Table 122, Register 0x12 [3:2], Table 123, Register 0x13 [7:4].
```

• PMIC removes GSI_n and PWR_GOOD interrupt. Related status registers are: Table 120, Register

```text
0x10 [5:2], Table 121, Register 0x11 [5], Table 124, Register 0x14 [2].
```

• PMIC only removes GSI_n interrupt and does not remove PWR_GOOD interrupt. Related status

```text
registers are: Table 120, Register 0x10 [0], Table 122, Register 0x12 [7:4], Table 123, Register 0x13
[3:0], Table 124, Register 0x14 [3]. The host is expected to either power cycle the PMIC or re-issue
the VR Enable command if PMIC is in programmable mode.
```

Note that PMIC does not allow controller to clear these status registers via I2C/I3C bus command:

Table 114, Register 0x0A [0], Table 155, Register 0x33 [1:0] and Table 173, Register 0x109 [0]. The PMIC offers a Global Clear command by writing ‘1’ to registers Table 124, Register 0x14 [0]. This command works same way as individual clear command. This command can alternatively be used by the host if more than one clear command is required for different registers.

**Table 120 — Register 0x10**: see [`registers/0x10.md`](../registers/0x10.md)

**Table 121 — Register 0x11**: see [`registers/0x11.md`](../registers/0x11.md)

**Table 122 — Register 0x12**: see [`registers/0x12.md`](../registers/0x12.md)

**Table 123 — Register 0x13**: see [`registers/0x13.md`](../registers/0x13.md)

**Table 124 — Register 0x14**: see [`registers/0x14.md`](../registers/0x14.md)
