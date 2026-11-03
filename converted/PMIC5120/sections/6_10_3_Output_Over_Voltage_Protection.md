---
document: JESD301-6 (PMIC5120 Power Management IC Standard, Version 1.0, February 2025)
device: PMIC5120
application: client
section: 6.10.3
title: Output Over Voltage Protection
pages: 60-61
---
# 6.10.3 Output Over Voltage Protection

An output over voltage protection mechanism is implemented to limit the voltages on the PMIC output regulators. The PMIC actively monitors the output voltage on each enabled regulators.

There are three possibilities where PMIC recognizes the over voltage event.

```text
1.   SWA output regulator goes above the threshold set in register Table 130, Register 0x22, [5:4].
2.   SWB output regulator goes above the threshold set in register Table 134, Register 0x26, [5:4].
3.   SWC output regulator goes above the threshold set in register Table 136, Register 0x28, [5:4].
```

In programmable mode (i.e., Table 143, Register 0x2F [2] = ‘1’), if any output over voltage condition persists greater than tOutput_OV_VR_Disable time then PMIC internally generates VR Disable command and disables all of its switching output regulators, sets register Table 106, Register 0x0A [7,5:4] appropriately, asserts PWR_GOOD and asserts GSI_n output signal. The PMIC keeps its VOUT_1.8V and VOUT_1.0V LDO output regulators active. The PMIC allows access to all registers. The host is responsible for taking any specific action. The host may query the PMIC register space to determine the cause of the PWR_GOOD signal assertion and GSI_n signal assertion. Once host determines the cause, the host must first clear the appropriate output over voltage status register as well as any other relevant status registers individually or by writing ‘1’ to global status clear register Table 116, Register 0x14 [0] which triggers the GSI_n signal to be de-asserted. Once the status register is cleared and GSI_n output signal is de-asserted, the host may re-enable the PMIC’s output switching regulator by issuing VR Enable command. The PMIC enables output switching regulators and ensures PWR_GOOD signal is floated when all of its output regulators are normal.

In secure mode (i.e., Table 143, Register 0x2F [2] = ‘0’), if any output over voltage condition persists greater than tOutput_OV_VR_Disable time then PMIC internally generates VR Disable command and disables all of its switching output regulators, sets register Table 106, Register 0x0A [7,5:4] appropriately, asserts PWR_GOOD and asserts GSI_n output signal. The PMIC keeps its VOUT_1.8V and VOUT_1.0V LDO output regulators active. The PMIC allows access to all registers. The host is responsible for taking the action of power cycling the PMIC.
