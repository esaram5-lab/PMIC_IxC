---
document: JESD301-2 (PMIC5100 Power Management IC Standard, Rev. 1.03, October 2022)
device: PMIC5100
application: client
section: 7.2.7.3
title: Mask Registers
pages: 127-131
---
# 7.2.7.3 Mask Registers

For each Real Time Status Registers (Table 96, “Register 0x08” [6:5,3:2,0], Table 97, “Register 0x09” [7,5,3,1:0], Table 98, “Register 0x0A” [7,5:1], Table 99, “Register 0x0B” [7,5:3,1:0], Table 139, “Register 0x33” [2]), the PMIC offers a way to mask the status of each event interrupt. The mask registers are Table 109, “Register 0x15” [5,3:2,0], Table 110, “Register 0x16” [7,5,3,1:0], Table 111, “Register 0x17” [7,5:2], Table 112, “Register 0x18” [7,5:3,1:0], and Table 113, “Register 0x19” [2] respectively. The mask registers only masks the event interrupt on GSI_n and PWR_GOOD signal. There is also a global mask register bits control Table 135, “Register 0x2F” [1:0] to control the GSI_n and PWR_GOOD output signal. When all mask registers are Table 109, “Register 0x15” [5,3:2,0], Table 110, “Register 0x16”[7,5,3,1:0], Table 111, “Register 0x17”[7,5:2], Table 112, “Register 0x18” [7,5:3,1:0], Table 113, “Register 0x19” [2] configured as ‘0’, the setting in Table 135, “Register 0x2F” [1:0] does not matter. The setting in Table 135, “Register 0x2F” [1:0] only matters when one or more mask registers Table 109, “Register 0x15” [5,3:2,0], Table 110, “Register 0x16” [7,5,3,1:0], Table 111, “Register 0x17” [7,5:2], Table 112, “Register 0x18” [7,5:3,1:0], Table 113, “Register 0x19” [2] are configured to ‘1’. For any failure events that cause the PMIC to generate VR Disable command on its own, the mask register bits (Table 109, “Register 0x15” [0], Table 111, “Register 0x17” [7,5:4], Table 112, “Register 0x18” [3,1:0], and Table 135, “Register 0x2F” [1:0]) do not apply and PMIC will assert PWR_GOOD output signal regardless of the setting in mask registers. The PMIC still updates the status registers appropriately when any event occurs. When masked, the host is expected to read the status registers periodically to learn if any of the event has occurred or not. The host can mask or un-mask each event individually. The host can mask or un-mask at any time in programmable mode. In secure mode of operation, the mask registers are locked.

**Table 109 — Register 0x15**: see [`registers/0x15.md`](../registers/0x15.md)

**Table 110 — Register 0x16**: see [`registers/0x16.md`](../registers/0x16.md)

**Table 111 — Register 0x17**: see [`registers/0x17.md`](../registers/0x17.md)

**Table 112 — Register 0x18**: see [`registers/0x18.md`](../registers/0x18.md)

**Table 113 — Register 0x19**: see [`registers/0x19.md`](../registers/0x19.md)
