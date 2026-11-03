---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 11.4.2
title: Clear Registers
pages: 146-152
---
# 11.4.2 Clear Registers

For each Real Time Status Registers (Table 113, Register 0x08 [7:0], Table 114, Register 0x09 [7:0],

Table 115, Register 0x0A [7:1], Table 116, Register 0x0B [7:0], Table 157, Register 0x33 [4:2], Table 175, Register 0x108 [7:0] and Table 176, Register 0x109 [7:6]), the PMIC offers a way to clear the status of each event. The clear registers are Table 121, Register 0x10 [7,5:0], Table 122, Register 0x11 [7:0], Table 123, Register 0x12 [7:2], Table 124, Register 0x13 [7:0], Table 125, Register 0x14 [4:2,0], Table 178,

Register 0x10E [7:0] and Table 179, Register 0x10F [7:6] respectively. All clear registers are Write ‘1’ only registers. When ‘1’ is written to any of the clear registers, the PMIC updates the status registers to default state and removes the interrupt condition on GSI_n and PWR_GOOD output signal assuming that event is no longer present. If the failing condition is still present, the status register will still remain at ‘1’. Note that GSI_n and PWR_GOOD interrupt is only applicable if that event is not masked. GSI_n output signal can be disabled. When ‘1’ is written to any of the clear registers, there are three categories of response by the PMIC.

1. PMIC removes GSI_n interrupt (PWR_GOOD interrupt is not applicable. Related status registers are: Table 121, Register 0x10 [1], Table 122, Register 0x11 [7,4:0], Table 124, Register 0x13 [7:4], Table 125, Register 0x14 [4], Table 178, Register 0x10E [5:4, 1:0].

2. PMIC removes GSI_n and PWR_GOOD interrupt. Related status registers are: Table 121, Register 0x10 [7,5:2], Table 122, Register 0x11 [6:5], Table 125, Register 0x14 [2], Table 178, Register 0x10E [7:6].

3. PMIC only removes GSI_n interrupt and does not remove PWR_GOOD interrupt. Related status registers are: Table 121, Register 0x10 [0], Table 123, Register 0x12 [7:4], Table 124, Register 0x13 [3:0], Table 125, Register 0x14 [3], Table 178, Register 0x10E [3:2], Table 179, Register 0x10F [7:6]. The host is expected to either power cycle the PMIC or re-issue the VR Enable command if PMIC is in non write-protect mode. The PMIC offers a Global Clear command by writing ‘1’ to registers Table 125, Register 0x14 [0]. This command works same way as individual clear command. This command can alternatively be used by the host if more than one clear command is required to different registers.

**Table 121 — Register 0x10**: see [`registers/0x10.md`](../registers/0x10.md)

**Table 122 — Register 0x11**: see [`registers/0x11.md`](../registers/0x11.md)

**Table 123 — Register 0x12**: see [`registers/0x12.md`](../registers/0x12.md)

**Table 124 — Register 0x13**: see [`registers/0x13.md`](../registers/0x13.md)

**Table 125 — Register 0x14**: see [`registers/0x14.md`](../registers/0x14.md)
