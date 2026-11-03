---
document: JESD301-6 (PMIC5120 Power Management IC Standard, Version 1.0, February 2025)
device: PMIC5120
application: client
section: 6.10.4
title: Output Under Voltage and VIN_Bulk Under Voltage Lockout Protection
pages: 61-62
---
# 6.10.4 Output Under Voltage and VIN_Bulk Under Voltage Lockout Protection

An output under voltage lockout protection mechanism is implemented to limit the voltages on the PMIC output regulators. The PMIC actively monitors the output voltage on each enabled regulators.

There are four possibilities where PMIC recognizes the under voltage lockout event.

```text
1.   SWA output regulator goes below the threshold set in register Table 130, Register 0x22, [3:2].

2.   SWB output regulator goes below the threshold set in register Table 134, Register 0x26, [3:2].
3.   SWC output regulator goes below the threshold set in register Table 136, Register 0x28, [3:2].

4.   VIN_Bulk input voltage goes below vendor specific voltage.
```

In programmable mode (i.e., Table 143, Register 0x2F [2] = ‘1’), if any output under voltage condition or VIN_Bulk input voltage condition as listed above persists greater than tOutput_UV_VR_Disable time then PMIC internally generates VR Disable command and disables all of its switching output regulators, sets register Table 107, Register 0x0B [3,1:0], Table 147, Register 0x33 [3] appropriately, asserts PWR_GOOD and asserts GSI_n output signal. The PMIC keeps its VOUT_1.8V and VOUT_1.0V LDO output regulators active. The PMIC allows access to all registers. The host is responsible for taking any specific action. The host may query the PMIC register space to determine the cause of the PWR_GOOD signal assertion and GSI_n signal assertion. Once host determines the cause, the host must first clear the appropriate output under voltage status register as well as any other relevant status registers individually or by writing ‘1’ to global status clear register Table 116, Register 0x14 [0] which triggers the GSI_n signal to be de-asserted. Once the status register is cleared and GSI_n output signal is de-asserted, the host may re-enable the PMIC’s output switching regulator by issuing VR Enable command assuming valid VIN_Bulk input voltage. The PMIC enables output switching regulators and floats PWR_GOOD signal High when all of its output regulators are normal.

In secure mode (i.e., Table 143, Register 0x2F [2] = ‘0’), if any output under voltage condition or VIN_Bulk input voltage condition as listed above persists greater than tOutput_UV_VR_Disable time then PMIC internally generates VR Disable command and disables all of its switching output regulators, sets register Table 107, Register 0x0B [3,2:0], Table 147, Register 0x33 [3] appropriately, asserts PWR_GOOD and asserts GSI_n output signal. The PMIC keeps its VOUT_1.8V and VOUT_1.0V LDO output regulators active. The PMIC allows access to all registers. The host is responsible for taking the action of power cycling the PMIC.
