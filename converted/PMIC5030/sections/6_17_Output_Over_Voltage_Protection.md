---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 6.17
title: Output Over Voltage Protection
pages: 52-52
---
# 6.17 Output Over Voltage Protection

An output over voltage protection mechanism is implemented to limit the voltages on the PMIC output regulators. The PMIC actively monitors the output voltage on each enabled regulators. There are six possibilities where PMIC recognizes the over voltage event.

1. SWA output regulator goes above the threshold set in register Table 139, Register 0x22 [5:4].

2. SWB output regulator goes above the threshold set in register Table 141, Register 0x24 [5:4].

3. SWC output regulator goes above the threshold set in register Table 143, Register 0x26 [5:4].

4. SWD output regulator goes above the threshold set in register Table 145, Register 0x28 [5:4].

5. SWE output regulator goes above the threshold set in register Table 186, Register 0x11E [5:4].

6. SWF output regulator goes above the threshold set in register Table 188, Register 0x120 [5:4].

In non write-protect mode, if any output over voltage condition persists greater than tOutput_OV_VR_Disable time then PMIC internally generates VR Disable command and disables all of its switching output regulators, sets register Table 115, Register 0x0A [7:4],Table 175, Register 0x108 [3:2] appropriately, asserts CAMP and asserts GSI_n output signal. The PMIC keeps its VOUT_1.8V and VOUT_1.0V LDO output regulators active. The host is responsible for taking any specific action. The host may query the PMIC register space to determine the cause of the CAMP signal assertion and GSI_n signal assertion. Once host determines the cause, the host must first clear the appropriate output over voltage status register as well as any other relevant status registers individually or by writing ‘1’ to global status clear register Table 125, Register 0x14 [0] which triggers the GSI_n signal to be de-asserted. Once the status register is cleared and GSI_n output signal is de-asserted, the host may re-enable the PMIC’s output switching regulator by issuing VR Enable command. The PMIC enables output switching regulators and ensures CAMP signal is floated when all of its output regulators are normal.

In write-protect mode, if any output over voltage condition persists greater than tOutput_OV_VR_Disable time then PMIC internally generates VR Disable command and disables all of its switching output regulators by executing Power Off Sequence configuration registers, asserts CAMP signal low and returns to configuration mode. The PMIC keeps its VOUT_1.8V and VOUT_1.0V LDO output regulators active.
