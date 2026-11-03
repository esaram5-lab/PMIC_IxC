---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 4.15.2
title: Input Over Voltage Protection
pages: 63-64
---
# 4.15.2 Input Over Voltage Protection

An input over voltage protection mechanism is implemented to limit the voltages to the PMIC. The PMIC actively monitors the input voltage VIN_Bulk rail. There is one possibility where PMIC recognizes the input over voltage event.

```text
1.     VIN_Bulk input goes above the threshold set in register Table 131, Register 0x1B [7].
```

When this event occurs for a period longer than tInput_OV time, then PMIC sets the register Table 112,

Register 0x08 [0]. Note that at this point, the PMIC does not assert PWR_GOOD output signal. The PMIC allows access to all registers and PMIC continues to operate as normal. The host is responsible for taking any specific action. The host may clear the VIN_Bulk input over voltage status register by writing ‘1’ to register Table 120, Register 0x10 [0] or by writing ‘1’ to global status clear register Table 124, Register 0x14 [0]. If the input over voltage condition is still present then PMIC continues to assert the status register Table 112, Register 0x08 [0] to ‘1’. In programmable mode (i.e., Table 151, Register 0x2F [2] = ‘1’), if VIN_Bulk input supply over voltage condition persists greater than tInput_OV_VR_Disable time then PMIC internally generates VR Disable command and disables all of its switching output regulators and asserts PWR_GOOD signal. The PMIC keeps its VOUT_1.8V and VOUT_1.0V LDO output regulators active. The PMIC allows access to all registers. The host is responsible for taking any specific action. The host may query the PMIC register space to determine the cause of the PWR_GOOD signal assertion. Once host determines the cause, the host must first clear the VIN_Bulk input over voltage status register as well as any other relevant status registers individually or by writing ‘1’ to global status clear register Table 124, Register 0x14 [0]. If the input over voltage condition is still present then PMIC continues to assert the status register Table 112, Register 0x08 [0] to ‘1’. Once the status register is cleared, the host may re-enable the PMIC’s output switching regulator by issuing VR Enable command. The PMIC enables output switching regulators and ensures PWR_GOOD signal is floated when all of its output regulators are normal and input over voltage condition is no longer present.

In secure mode (i.e., Table 151, Register 0x2F [2] = ‘0’), if VIN_Bulk input supply over voltage condition persists greater than tInput_OV_VR_Disable time then PMIC internally generates VR Disable command and disables all of its switching output regulators and asserts PWR_GOOD signal. The PMIC keeps its VOUT_1.8V and VOUT_1.0V LDO output regulators active. The PMIC allows access to all registers. The host is responsible for taking the action of power cycling the PMIC.
