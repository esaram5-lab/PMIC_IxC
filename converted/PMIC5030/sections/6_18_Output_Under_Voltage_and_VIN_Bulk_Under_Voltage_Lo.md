---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 6.18
title: Output Under Voltage and VIN_Bulk Under Voltage Lockout Protection
pages: 52-53
---
# 6.18 Output Under Voltage and VIN_Bulk Under Voltage Lockout Protection

```text
Protection
```

An output under voltage lockout protection mechanism is implemented to limit the voltages on the PMIC output regulators. The PMIC actively monitors the output voltage on each enabled regulators. The PMIC also implements the VIN_Bulk under voltage and VBIAS under voltage lockout protection mechanism to limit the voltages. There are seven possibilities where PMIC recognizes the under voltage lockout event.

1. SWA output regulator goes below the threshold set in register Table 139, Register 0x22 [3:2].

2. SWB output regulator goes below the threshold set in register Table 141, Register 0x24 [3:2].

3. SWC output regulator goes below the threshold set in register Table 143, Register 0x26 [3:2].

4. SWD output regulator goes below the threshold set in register Table 145, Register 0x28 [3:2].

5. SWE output regulator goes below the threshold set in register Table 186, Register 0x11E [3:2].

6. SWF output regulator goes below the threshold set in register Table 188, Register 0x120 [3:2].

7. VBias LDO output regulator goes below the vendor specific threshold or VIN_Bulk Input Voltage goes below vendor specific threshold.

```text
6.18    Output Under Voltage and VIN_Bulk Under Voltage Lockout Protection
        (cont’d)
```

In non write-protect mode, if any output under voltage condition or VIN_Bulk input voltage condition as listed above persists greater than tOutput_UV_VR_Disable time then PMIC internally generates VR Disable command and disables all of its switching output regulators, sets register Table 116, Register 0x0B [3:0], Table 176, Register 0x109 [7:6], Table 157, Register 0x33 [3] appropriately, asserts CAMP and asserts GSI_n output signal. The PMIC keeps its VOUT_1.8V and VOUT_1.0V LDO output regulators active. The host is responsible for taking any specific action. The host may query the PMIC register space to determine the cause of the CAMP signal assertion and GSI_n signal assertion. Once host determines the cause, the host must first clear the appropriate output under voltage status register as well as any other relevant status registers individually or by writing ‘1’ to global status clear register Table 125, Register 0x14 [0] which triggers the GSI_n signal to be de-asserted. Once the status register is cleared and GSI_n output signal is de-asserted, the host may re-enable the PMIC’s output switching regulator by issuing VR Enable command assuming valid VIN_Bulk input voltage. The PMIC enables output switching regulators and floats CAMP signal when all of its output regulators are normal. In write-protect mode, if any output under voltage condition or VIN_Bulk input voltage condition as listed above persists greater than tOutput_UV_VR_Disable time then PMIC internally generates VR Disable command and disables all of its switching output regulators by executing Power Off Sequence configuration registers, asserts CAMP signal low and returns to configuration mode. The PMIC keeps its VOUT_1.8V and VOUT_1.0V LDO output regulators active.
