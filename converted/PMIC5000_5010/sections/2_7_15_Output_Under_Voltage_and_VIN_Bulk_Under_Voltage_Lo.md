---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 2.7.15
title: Output Under Voltage and VIN_Bulk Under Voltage Lockout Protection
pages: 41-42
---
# 2.7.15 Output Under Voltage and VIN_Bulk Under Voltage Lockout Protection

An output under voltage lockout protection mechanism is implemented to limit the voltages on the PMIC output regulators. The PMIC actively monitors the output voltage on each enabled regulators. There are five possibilities where PMIC recognizes the under voltage lockout event.

```text
1.   SWA output regulator goes below the threshold set in register Table 124, “Register 0x22” [3:2].
2.   SWB output regulator goes below the threshold set in register Table 126, “Register 0x24” [3:2].
3.   SWC output regulator goes below the threshold set in register Table 128, “Register 0x26” [3:2].
4.   SWD output regulator goes below the threshold set in register Table 130, “Register 0x28” [3:2].
5.   VBias LDO output regulator goes below the vendor specific threshold or VIN_Bulk Input Voltage goes
     below vendor specific threshold.
```

## 2.7.15.1 DDR5 RDIMM/LRDIMM Environment - Table 166, “Register 0x4F” [7] = ‘0’:

In non write protect mode, if any output under voltage condition (among five possibilities listed above) or VIN_Bulk input voltage condition as listed above persists greater than tOutput_UV_VR_Disable time then PMIC internally generates VR Disable command and disables all of its switching output regulators, sets register Table 101, “Register 0x0B” [3:0], Table 141, “Register 0x33” [3] appropriately, asserts CAMP and asserts GSI_n output signal. The PMIC keeps its VOUT_1.8V and VOUT_1.0V LDO output regulators active. The PMIC allows access to all registers. The host is responsible for taking any specific action. The host may query the PMIC register space to determine the cause of the CAMP signal assertion and GSI_n signal assertion. Once host determines the cause, the host must first clear the appropriate output under voltage status register as well as any other relevant status registers individually or by writing ‘1’ to global status clear register Table 110, “Register 0x14” [0] which triggers the GSI_n signal to be de-asserted. Once the status register is cleared and GSI_n output signal is de-asserted, the host may re-enable the PMIC’s output switching regulator by issuing VR Enable command assuming valid VIN_Bulk input voltage. The PMIC enables output switching regulators and floats CAMP signal when all of its output regulators are normal.

In write protect mode, if any output under voltage condition (among five possibilities listed above) or VIN_Bulk input voltage condition as listed above persists greater than tOutput_UV_VR_Disable time then PMIC internally generates VR Disable command and disables all of its switching output regulators by executing Power Off Sequence configuration registers, asserts CAMP signal low and returns to configuration mode. The PMIC keeps its

VOUT_1.8V and VOUT_1.0V LDO output regulators active.

## 2.7.15.2 DDR5 NVDIMM or other Custom Environment - Table 166, “Register 0x4F” [7]=‘1’

```text
[7]=‘1’
```

In non write protect mode, if any output under voltage condition (First four possibilities listed above) as listed above persists greater than tOutput_UV_VR_Disable time then PMIC internally generates VR Disable command to disable only the affected switching output regulator, sets register Table 101, “Register 0x0B” [3:0] appropriately, asserts CAMP and asserts GSI_n output signal and continues to operate normal on other output regulators. Note that if the fifth condition (VBias LDO output goes below vendor specific threshold or VIN_Bulk input goes below vendor specific threshold) listed above persists greater than tOutput_UV_VR_Disable time, then the PMIC internally generates VR Disable command and disables all of its switching output regulators, sets register Table 101, “Register 0x0B” [3:0] and Table 141, “Register 0x33” [3] appropriately, asserts CAMP and asserts GSI_n output signal. The PMIC keeps its VOUT_1.8V and VOUT_1.0V LDO output regulators active. The PMIC allows access to all registers. The host is responsible for taking any specific action. The host may query the PMIC register space to determine the cause of the CAMP signal assertion and GSI_n signal assertion. Once host determines the cause, the host must first clear the appropriate output under voltage status register as well as any other relevant status registers individually or by writing ‘1’ to global status clear register Table 110, “Register 0x14” [0] which triggers the GSI_n signal to be de-asserted. Once the status register is cleared and GSI_n output signal is de-asserted, the host may re-enable the PMIC’s output switching regulator by issuing VR Enable command. The PMIC enables output switching regulator and ensures CAMP signal is floated when all of its output regulators are normal. Note that in this case, though Host issues VR Enable command, it only turns on the only affected regulator that was disabled. The write protect mode is not allowed when Table 166, “Register 0x4F” [7] = ‘1’.
