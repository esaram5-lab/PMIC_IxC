---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 4.15.7
title: Output High Current Consumption Warning Event
pages: 67-67
---
# 4.15.7 Output High Current Consumption Warning Event

The PMIC supports high output current consumption warning mechanism for each of its regulator output. If ADC is enabled (Table 152, Register 0x30 [7] = ‘1’), the PMIC actively monitors the average output current of the regulator and reports high output current consumption warning. There are four possibilities where PMIC recognizes the high output current consumption.

```text
1.    SWA output regulator average current goes above the threshold set in register Table 132, Register
      0x1C [7:0].
2.    SWD output regulator average current goes above the threshold set in register Table 133, Register
      0x1D [7:0].
3.    SWB output regulator average current goes above the threshold set in register Table 134, Register

      0x1E [7:0].
4.     SWC output regulator average current goes above the threshold set in register Table 135, Register

       0x1F [7:0].
```

When either event occurs then PMIC sets the register Table 113, Register 0x09 [3:0] appropriately. The PMIC continues to operate as normal and PWR_GOOD output remains high as shown Table 27. The PMIC allows access to all registers. The host is responsible for taking any specific action. The host may query the PMIC register space. Once host determines the cause, the host may clear the appropriate output current consumption warning status register as well as any other status registers individually or by writing ‘1’ to global status clear register in Table 124, Register 0x14 [0]. If the output current consumption warning condition is still present then PMIC continues to assert the appropriate status register in Table 113, Register 0x09 [3:0] to ‘1’.
