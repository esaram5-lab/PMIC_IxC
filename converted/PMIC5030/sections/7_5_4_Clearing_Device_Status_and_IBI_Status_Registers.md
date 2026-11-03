---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 7.5.4
title: Clearing Device Status and IBI Status Registers
pages: 90-90
---
# 7.5.4 Clearing Device Status and IBI Status Registers

The PMIC device provides the IBI status in Table 115, Register 0x0A [1] by setting it to ‘1’. The PMIC device clears the IBI status register Table 115, Register 0x0A [1] to ‘0’ automatically when it sends a complete IBI (including payload and without interruption) and it also clears Pending Interrupt Bits [3:0] to ‘0000’. Once IBI status register is cleared, the PMIC does not request for an IBI again unless another event occurs. The PMIC device provides the device status in Table 113, Register 0x08 [7:0], Table 114, Register 0x09 [7:0], Table 115, Register 0x0A [7:2], Table 116, Register 0x0B [7:0] and Table 157, Register 0x33 [4:2] registers. The status information in Table 113, Register 0x08 [7:0], Table 114, Register 0x09 [7:0], Table 115, Register 0x0A [7:2], Table 116, Register 0x0B [7:0] and Table 157, Register 0x33 [4:2] registers are latched and remains set even after the PMIC device sends IBI payload and clears the IBI status register Table 115, Register 0x0A [1] to ‘0’. The host must explicitly clear the status register through Clear command by writing ‘1’ for appropriate status or by issuing a Global clear command.

After Host issues clear command, if the condition is no longer present, the PMIC device clears the appropriate status register, clears the IBI status register Table 115, Register 0x0A [1] to ‘0’ and Pending

Interrupt Bits [3:0] to ‘0000’ even if the PMIC device has not sent the IBI. After Host issues clear command, if the condition is still present, the device will again set the appropriate status register, sets the IBI status register Table 115, Register 0x0A [1] to ‘1’ and Pending Interrupt Bits [3:0] to ‘0001’ even if the device has already sent the IBI and entire IBI payload.
