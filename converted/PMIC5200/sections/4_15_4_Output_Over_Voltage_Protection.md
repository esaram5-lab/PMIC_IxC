---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 4.15.4
title: Output Over Voltage Protection
pages: 65-66
---
# 4.15.4 Output Over Voltage Protection

An output over voltage protection mechanism is implemented to limit the voltages on the PMIC output regulators. The PMIC actively monitors the output voltage on each enabled regulator. There are four possibilities where PMIC recognizes the over voltage event.

```text
1.    SWA output regulator goes above the threshold set in register Table 138, Register 0x22, [5:4].
2.    SWD output regulator goes above the threshold set in register Table 140, Register 0x24 [5:4].
3.    SWB output regulator goes above the threshold set in register Table 142, Register 0x26, [5:4].
4.    SWC output regulator goes above the threshold set in register Table 144, Register 0x28, [5:4].
```

In programmable mode (i.e., Table 151, Register 0x2F [2] = ‘1’), if any output over voltage condition persists greater than tOutput_OV_VR_Disable time, then PMIC internally generates VR Disable command and disables all of its switching output regulators, sets register Table 114, Register 0x0A [7:4] appropriately, and asserts PWR_GOOD output signal. The PMIC keeps its VOUT_1.8V and VOUT_1.0V LDO output regulators active. The PMIC allows access to all registers. The host is responsible for taking any specific action. The host may query the PMIC register space to determine the cause of the PWR_GOOD signal assertion. Once host determines the cause, the host must first clear the appropriate output over voltage status register as well as any other relevant status registers individually or by writing ‘1’ to global status clear register Table 124, Register 0x14 [0]. Once the status register is cleared, the host may re-enable the PMIC’s output switching regulator by issuing VR Enable command. The PMIC enables output switching regulators and ensures PWR_GOOD signal is floated when all of its output regulators are normal. In secure mode (i.e., Table 151, Register 0x2F [2] = ‘0’), if any output over voltage condition persists greater than tOutput_OV_VR_Disable time, then PMIC internally generates VR Disable command and disables all of its switching output regulators, sets register Table 114, Register 0x0A [7:4] appropriately, and asserts PWR_GOOD The PMIC keeps its VOUT_1.8V and VOUT_1.0V LDO output regulators active. The PMIC allows access to all registers. The host is responsible for taking the action of power cycling the PMIC.
