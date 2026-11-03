---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 8.4.3
title: Mask Registers
pages: 149-154
---
# 8.4.3 Mask Registers

For each real time Status Registers (Table 112, Register 0x08 [6:2,0], Table 113, Register 0x09 [7,5,3:0], Table 114, Register 0x0A [7:1], Table 115, Register 0x0B [7:0], Table 155, Register 0x33 [3:2]), the PMIC offers a way to mask the status of each event interrupt. The mask registers are Table 125, Register 0x15 [7,5:0], Table 126, Register 0x16 [7,5,3:0], Table 127, Register 0x17 [7:2], Table 128, Register 0x18 [7:0], and Table 129, Register 0x19 [3:2], respectively. The mask registers only mask the event interrupt on GSI_n and PWR_GOOD signal. It does not mask the actual status in the register. There is also global mask register bits control Table 151, Register 0x2F [1:0] to control the GSI_n and PWR_GOOD output signal. When all mask registers (Table 125, Register 0x15 [7,5:0], Table 126, Register 0x16 [7,5,3:0], Table 127, Register 0x17 [7:2], Table 128, Register 0x18 [7:0], and Table 129, Register 0x19 [3:2]) are configured as ‘0’, the setting in Table 151, Register 0x2F [1:0] does not matter. The setting Table 151, Register 0x2F [1:0] only matters when one or more mask registers (Table 125, Register 0x15 [7,5:0], Table 126, Register 0x16 [7,5,3:0], Table 127, Register 0x17 [7:2], Table 128, Register 0x18 [7:0], and Table 129, Register 0x19 [3:2]) are configured as ‘1’. For any failure events that causes the PMIC to generate VR Disable command on its own, the mask register bits (Table 125, Register 0x15 [0], Table 127, Register 0x17 [7:4], Table 128, Register 0x18 [3:0], Table 129, Register 0x19 [3], and Table 151, Register 0x2F [1:0]) do not apply and PMIC always asserts PWR_GOOD output signal regardless of the setting in mask registers. The PMIC still updates the status registers appropriately when any event occurs. When masked, the host is expected to read the status registers periodically to learn if any of the events have occurred or not. The host can mask or unmask each event individually. The host can mask or unmask at any time in programmable mode. In secure mode of operation, the mask registers are locked.

**Table 125 — Register 0x15**: see [`registers/0x15.md`](../registers/0x15.md)

**Table 126 — Register 0x16**: see [`registers/0x16.md`](../registers/0x16.md)

**Table 127 — Register 0x17**: see [`registers/0x17.md`](../registers/0x17.md)

**Table 128 — Register 0x18**: see [`registers/0x18.md`](../registers/0x18.md)

**Table 129 — Register 0x19**: see [`registers/0x19.md`](../registers/0x19.md)
