---
document: JESD301-6 (PMIC5120 Power Management IC Standard, Version 1.0, February 2025)
device: PMIC5120
application: client
section: 7.2.8
title: Mask Registers
pages: 115-116
---
# 7.2.8 Mask Registers

For each Real Time Status Registers (Table 104, Register 0x08 [6:5,3:2,0], Table 105, Register 0x09 [7,5,3,1:0], Table 106, Register 0x0A [7,5:1], Table 107, Register 0x0B [7,5:3,1:0], Table 147, Register 0x33 [2]), the PMIC offers a way to mask the status of each event interrupt. The mask registers are Table 117, Register 0x15 [5,3:2,0], Table 118, Register 0x16 [7,5,3,1:0], Table 119, Register 0x17 [7,5:2], Table 120, Register 0x18 [7,5:3,1:0] and Table 121, Register 0x19 [2] respectively. The mask registers only masks the event interrupt on GSI_n and PWR_GOOD signal.

There is also a global mask register bits control Table 143, Register 0x2F [1:0] to control the GSI_n and PWR_GOOD output signal. When all mask registers are Table 117, Register 0x15 [5,3:2,0], Table 118, Register 0x16[7,5,3,1:0], Table 119, Register 0x17[7,5:2], Table 120, Register 0x18 [7,5:3,1:0], Table 121, Register 0x19 [2] configured as ‘0’, the setting in Table 143, Register 0x2F [1:0] does not matter. The setting in Table 143, Register 0x2F [1:0] only matters when one or more mask registers Table 117, Register 0x15 [5,3:2,0], Table 118, Register 0x16 [7,5,3,1:0], Table 119, Register 0x17 [7,5:2], Table 120, Register 0x18 [7,5:3,1:0], Table 121, Register 0x19 [2] are configured to ‘1’.

For any failure events that causes the PMIC to generate VR Disable command on its own, the mask register bits (Table 117, Register 0x15 [0], Table 119, Register 0x17 [7,5:4], Table 120, Register 0x18 [3,1:0] and Table 143, Register 0x2F [1:0]) do not apply and PMIC will assert PWR_GOOD output signal regardless of the setting in mask registers. The PMIC still updates the status registers appropriately when any event occurs. When masked, the host is expected to read the status registers periodically to learn if any of the event has occurred or not. The host can mask or un-mask each event individually. The host can mask or un-mask at any time in programmable mode. In secure mode of operation, the mask registers are locked.
