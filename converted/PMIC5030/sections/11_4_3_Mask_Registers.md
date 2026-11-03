---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 11.4.3
title: Mask Registers
pages: 152-158
---
# 11.4.3 Mask Registers

For each Real Time Status Registers (Table 113, Register 0x08 [7:0], Table 114, Register 0x09 [7:0], Table 115, Register 0x0A [7:1], Table 116, Register 0x0B [7:0], Table 157, Register 0x33 [4:2]), Table 175, Register 0x108 [7:0] and Table 176, Register 0x109 [7:6]), the PMIC offers a way to mask the status of each event interrupt. The mask registers are Table 126, Register 0x15 [7,5:0], Table 127, Register 0x16 [7:0], Table 128, Register 0x17 [7:2], Table 129, Register 0x18 [7:0], Table 130, Register 0x19 [4:2], Table 180, Register 0x114 [7:0] and Table 181, Register 0x115 [7:6] respectively. The mask registers only mask the event interrupt on GSI_n and PWR_GOOD signal. There is also a global mask bits register control Table 152, Register 0x2F [1:0] to control the GSI_n and PWR_GOOD output signal. When all mask registers are Table 126, Register 0x15 [7,5:0], Table 127, Register 0x16 [7:0], Table 128, Register 0x17 [7:2], Table 129, Register 0x18 [7:0], Table 130, Register 0x19 [4:2], Table 180, Register 0x114 [7:0] and Table 181, Register 0x115 [7:6] configured as ‘0’, the setting in Table 152, Register 0x2F [1:0] does not matter. The setting in Table 152, Register 0x2F [1:0] only matters when one or more mask registers Table 126, Register 0x15 [7,5:0], Table 127, Register 0x16 [7:0], Table 128, Register 0x17 [7:2], Table 129, Register 0x18 [7:0], Table 130, Register 0x19 [4:2], Table 180, Register 0x114 [7:0] and Table 181, Register 0x115 [7:6] are configured to ‘1’. For any failure events that causes the PMIC to generate VR Disable command on its own, the mask register bits (Table 126, Register 0x15 [0], Table 128, Register 0x17 [7:4], Table 129, Register 0x18 [3:0], Table 130, Register 0x19 [3], Table 152, Register 0x2F [1:0], Table 180, Register 0x114 [3:2], Table 181, Register 0x115 [7:6]) do not apply and PMIC will assert PWR_GOOD output signal regardless of the setting in mask registers. The PMIC still updates the status registers appropriately when any event occurs. When masked, the host is expected to read the status registers periodically to learn if any of the events have occurred or not. The host can mask or unmask each event individually. The host can mask or unmask at any time in non write-protect mode. In write-protect mode of operation, the mask registers are locked.

**Table 126 — Register 0x15**: see [`registers/0x15.md`](../registers/0x15.md)

**Table 127 — Register 0x16**: see [`registers/0x16.md`](../registers/0x16.md)

**Table 128 — Register 0x17**: see [`registers/0x17.md`](../registers/0x17.md)

**Table 129 — Register 0x18**: see [`registers/0x18.md`](../registers/0x18.md)

**Table 130 — Register 0x19**: see [`registers/0x19.md`](../registers/0x19.md)
