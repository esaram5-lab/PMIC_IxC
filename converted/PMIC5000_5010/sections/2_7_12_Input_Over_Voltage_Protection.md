---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 2.7.12
title: Input Over Voltage Protection
pages: 38-39
---
# 2.7.12 Input Over Voltage Protection

An input over voltage protection mechanism is implemented to limit the voltages to the PMIC. The PMIC actively monitors the input voltage VIN_Bulk and VIN_Mgmt rail. There are two possibilities where PMIC recognizes the input over voltage event.

```text
1. VIN_Mgmt input goes above the threshold set in register Table 117, “Register 0x1B” [5].
2. VIN_Bulk input goes above the threshold set in register Table 117, “Register 0x1B” [7].
```

When either one or both event occurs for a period longer than tInput_OV_GSI_Assertion time then PMIC sets the register Table 98, “Register 0x08” [1:0] accordingly and drives GSI_n output signal as shown in Table 27 at the same time. Note that at this point, the PMIC does not assert CAMP output signal. The PMIC allows access to all registers and PMIC continues to operate as normal. The host is responsible for taking any specific action. The host may clear the VIN_Mgmt or VIN_Bulk input over voltage status register by writing ‘1’ to register Table 106, “Register 0x10” [1:0] appropriately or by writing ‘1’ to global status clear register Table 110, “Register 0x14” [0]. If the input over voltage condition is still present then PMIC will continue to assert GSI_n output signal and the status register Table 98, “Register 0x08” [1:0] will remain at ‘1’. In non write protect mode, if VIN_Bulk input supply over voltage condition persists greater than tInput_OV_VR_-Disable time then PMIC internally generates VR Disable command and disables all of its switching output regulators and asserts CAMP signal. The PMIC keeps its VOUT_1.8V and VOUT_1.0V LDO output regulators active. The PMIC allows access to all registers. The host is responsible for taking any specific action. The host may query the PMIC register space to determine the cause of the CAMP signal assertion and GSI_n signal assertion. Once host determines the cause, the host must first clear the VIN_Bulk input over voltage status register as well as any other relevant status registers individually or by writing ‘1’ to global status clear register Table 110, “Register 0x14” [0] which triggers the GSI_n signal to be de-asserted. If the input over voltage condition is still present then PMIC will continue to assert GSI_n output signal and the status register Table 98, “Register 0x08” [0] will remain at ‘1’. Once the status register is cleared and GSI_n output signal is de-asserted, the host may re-enable the PMIC’s output switching regulator by issuing VR Enable command. The PMIC enables output switching regulators and ensures CAMP signal is floated when all of its output regulators are normal and input over voltage condition is no longer present. In write protect mode, if VIN_Bulk input supply over voltage condition persists greater than tInput_OV_VR_Disable time then PMIC internally generates VR Disable command and disables all of its switching output regulators by executing Power Off Sequence configuration registers, asserts CAMP signal low and returns to configuration mode. The PMIC keeps its VOUT_1.8V and VOUT_1.0V LDO output regulators active.
