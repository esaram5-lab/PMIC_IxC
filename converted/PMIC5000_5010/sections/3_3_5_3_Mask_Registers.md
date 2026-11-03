---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 3.3.5.3
title: Mask Registers
pages: 128-134
---
# 3.3.5.3 Mask Registers

For each Real Time Status Registers (Table 98, “Register 0x08” [7:0], Table 99, “Register 0x09” [7:0], Table 100, “Register 0x0A” [7:1], Table 101, “Register 0x0B” [7:0], Table 141, “Register 0x33” [4:2]), the PMIC offers a way to mask the status of each event interrupt. The mask registers are Table 111, “Register 0x15” [7,5:0], Table 112, “Register 0x16” [7:0], Table 113, “Register 0x17” [7:2], Table 114, “Register 0x18” [7:0], and Table 115, “Register 0x19” [4:2] respectively. The mask registers only masks the event interrupt on GSI_n and PWR_GOOD signal. There is also a global mask bits register control Table 137, “Register 0x2F” [1:0] to control the GSI_n and PWR_GOOD output signal. When all mask registers are Table 111, “Register 0x15” [7,5:0], Table 112, “Register 0x16” [7:0], Table 113, “Register 0x17” [7:2], Table 114, “Register 0x18” [7:0], and Table 115, “Register 0x19” [4:2] configured as ‘0’, the setting in Table 137, “Register 0x2F” [1:0] does not matter. The setting in Table 137, “Register 0x2F” [1:0] only matters when one or more mask registers Table 111, “Register 0x15” [7,5:0], Table 112, “Register 0x16” [7:0], Table 113, “Register 0x17” [7:2], Table 114, “Register 0x18” [7:0], and Table 115, “Register 0x19” [4:2] are configured to ‘1’. For any failure events that causes the PMIC to generate VR Disable command on its own, the mask register bits (Table 111, “Register 0x15” [0], Table 113, “Register 0x17” [7:4], Table 114, “Register 0x18” [3:0], Table 115, “Register 0x19” [3], Table 137, “Register 0x2F” [1:0]) do not apply and PMIC will assert PWR_GOOD output signal regardless of the setting in mask registers. The PMIC still updates the status registers appropriately when any event occurs. When masked, the host is expected to read the status registers periodically to learn if any of the event has occurred or not. The host can mask or unmask each event individually. The host can mask or un-mask at any time in non write protect mode. In write protect mode of operation, the mask registers are locked.

**Table 111 — Register 0x15**: see [`registers/0x15.md`](../registers/0x15.md)

**Table 112 — Register 0x16**: see [`registers/0x16.md`](../registers/0x16.md)

**Table 113 — Register 0x17**: see [`registers/0x17.md`](../registers/0x17.md)

**Table 114 — Register 0x18**: see [`registers/0x18.md`](../registers/0x18.md)

**Table 115 — Register 0x19**: see [`registers/0x19.md`](../registers/0x19.md)
