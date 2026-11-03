---
document: JESD301-6 (PMIC5120 Power Management IC Standard, Version 1.0, February 2025)
device: PMIC5120
application: client
section: 6.10.6
title: Output High Current Consumption Warning Event
pages: 62-62
---
# 6.10.6 Output High Current Consumption Warning Event

The PMIC supports high output current consumption warning mechanism for each of its regulator output. If enabled, the PMIC actively monitors the average output current of the regulator.

There are three possibilities where PMIC recognizes the high output current consumption.

```text
1.   SWA output regulator average current goes above the threshold set in register Table 124, Register 0x1C

     [7:0].
2.   SWB output regulator average current goes above the threshold set in register Table 126, Register 0x1E

     [7:0].
3.   SWC output regulator average current goes above the threshold set in register Table 127, Register 0x1F
     [7:0].
```

When either event occurs then PMIC sets the register Table 105, Register 0x09 [3,1:0] appropriately, drives GSI_n output signal as shown in Table 30 at the same time. The PMIC continues to operate as normal. The PMIC allows access to all registers. The host is responsible for taking any specific action. The host may query the PMIC register space to determine the cause of the GSI_n signal assertion. Once host determines the cause, the host may clear the appropriate output current consumption warning status register as well as any other status registers individually or by writing ‘1’ to global status clear register in Table 116, Register 0x14 [0] which triggers the GSI_n signal to be de-asserted. If the output current consumption warning condition is still present then PMIC will continue to assert GSI_n output signal and the appropriate status register in Table 105, Register 0x09 [3,1:0] will remain at ‘1’. If the output current consumption warning condition persists, the host may set the appropriate mask register to remove GSI_n output signal as shown in Table 31 and Table 32.
