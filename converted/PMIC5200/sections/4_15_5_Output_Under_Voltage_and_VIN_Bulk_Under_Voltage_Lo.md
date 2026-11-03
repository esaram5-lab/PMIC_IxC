---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 4.15.5
title: Output Under Voltage and VIN_Bulk Under Voltage Lockout Protection
pages: 66-66
---
# 4.15.5 Output Under Voltage and VIN_Bulk Under Voltage Lockout Protection

An output under voltage lockout protection mechanism is implemented to limit the voltages on the PMIC output regulators. The PMIC actively monitors the output voltage on each enabled regulator. There are five possibilities where PMIC recognizes the under voltage lockout event.

```text
1.    SWA output regulator goes below the threshold set in register Table 138, Register 0x22, [3:2].
2.    SWD output regulator goes below the threshold set in register Table 140, Register 0x24 [3:2].
3.    SWB output regulator goes below the threshold set in register Table 142, Register 0x26, [3:2].
4.    SWC output regulator goes below the threshold set in register Table 144, Register 0x28, [3:2].
5.    VIN_Bulk input voltage goes below vendor specific voltage.
```

In programmable mode (i.e., Table 151, Register 0x2F [2] = ‘1’), if any output under voltage condition or VIN_Bulk input voltage condition as listed above persists greater than tOutput_UV_VR_Disable time, then PMIC internally generates VR Disable command and disables all of its switching output regulators, sets register Table 115, Register 0x0B [3:0], Table 155, Register 0x33 [3] appropriately, and asserts PWR_GOOD. The PMIC keeps its VOUT_1.8V and VOUT_1.0V LDO output regulators active. The PMIC allows access to all registers. The host is responsible for taking any specific action. The host may query the PMIC register space to determine the cause of the PWR_GOOD signal assertion. Once host determines the cause, the host must first clear the appropriate output under voltage status register as well as any other relevant status registers individually or by writing ‘1’ to global status clear register Table 124,

Register 0x14 [0]. Once the status register is cleared, the host may re-enable the PMIC’s output switching regulator by issuing VR Enable command, assuming a valid VIN_Bulk input voltage. The PMIC enables output switching regulators and floats PWR_GOOD signal High when all of its output regulators are normal.

In secure mode (i.e., Table 151, Register 0x2F [2] = ‘0’), if any output under voltage condition or VIN_Bulk input voltage condition as listed above persists greater than tOutput_UV_VR_Disable time, then PMIC internally generates VR Disable command and disables all of its switching output regulators, sets register Table 115, Register 0x0B [3:0], Table 155, Register 0x33 [3] appropriately, and asserts PWR_GOOD. The PMIC keeps its VOUT_1.8V and VOUT_1.0V LDO output regulators active. The PMIC allows access to all registers. The host is responsible for taking the action of power cycling the PMIC.
