---
document: JESD301-2 (PMIC5100 Power Management IC Standard, Rev. 1.03, October 2022)
device: PMIC5100
application: client
section: 6.10.1
title: Input Over Voltage Protection
pages: 55-56
---
# 6.10.1 Input Over Voltage Protection

An input over voltage protection mechanism is implemented to limit the voltages to the PMIC. The PMIC actively monitors the input voltage VIN_Bulk rail. There is one possibility where PMIC recognizes the input over voltage event.

```text
1. VIN_Bulk input goes above the threshold set in register Table 115, “Register 0x1B” [7].
```

When this event occurs for a period longer than tInput_OV_GSI_Assertion time then PMIC sets the register Table 96, “Register 0x08” [0] accordingly and drives GSI_n output signal as shown in Table 28 at the same time. Note that at this point, the PMIC does not assert PWR_GOOD output signal. The PMIC allows access to all registers and PMIC continues to operate as normal. The host is responsible for taking any specific action.

The host may clear the VIN_Bulk input over voltage status register by writing ‘1’ to register Table 104, “Register 0x10” [0] appropriately or by writing ‘1’ to global status clear register Table 108, “Register 0x14” [0]. If the input over voltage condition is still present then PMIC will continue to assert GSI_n output signal and the status register Table 96, “Register 0x08” [0] will remain at ‘1’. In programmable mode (i.e., Table 135, “Register 0x2F” [2] = ‘1’), if VIN_Bulk input supply over voltage condition persists greater than tInput_OV_VR_Disable time then PMIC internally generates VR Disable command and disables all of its switching output regulators and asserts PWR_GOOD signal. The PMIC keeps its VOUT_1.8V and VOUT_1.0V LDO output regulators active. The PMIC allows access to all registers. The host is responsible for taking any specific action. The host may query the PMIC register space to determine the cause of the PWR_GOOD signal assertion and GSI_n signal assertion. Once host determines the cause, the host must first clear the VIN_Bulk input over voltage status register as well as any other relevant status registers individually or by writing ‘1’ to global status clear register Table 108, “Register 0x14” [0] which triggers the GSI_n signal to be de-asserted. If the input over voltage condition is still present then PMIC will continue to assert GSI_n output signal and the status register Table 96, “Register 0x08” [0] will remain at ‘1’. Once the status register is cleared and GSI_n output signal is de-asserted, the host may re-enable the PMIC’s output switching regulator by issuing VR Enable command. The PMIC enables output switching regulators and ensures PWR_GOOD signal is floated when all of its output regulators are normal and input over voltage condition is no longer present. In secure mode (i.e., Table 135, “Register 0x2F” [2] = ‘0’), if VIN_Bulk input supply over voltage condition persists greater than tInput_OV_VR_Disable time then PMIC internally generates VR Disable command and disables all of its switching output regulators and asserts PWR_GOOD signal. The PMIC keeps its VOUT_1.8V and VOUT_1.0V LDO output regulators active. The PMIC allows access to all registers. The host is responsible for taking the action of power cycling the PMIC.
