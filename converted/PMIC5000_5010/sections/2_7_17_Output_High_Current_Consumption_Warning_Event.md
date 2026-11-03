---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 2.7.17
title: Output High Current Consumption Warning Event
pages: 42-43
---
# 2.7.17 Output High Current Consumption Warning Event

The PMIC supports high output current consumption warning mechanism for each of its regulator output. If enabled, the PMIC actively monitors the average output current of the regulator.

There are four possibilities where PMIC recognizes the high output current consumption.

```text
1. SWA output regulator average current goes above the threshold set in register Table 118, “Register 0x1C”

    [7:2].

2. SWB output regulator average current goes above the threshold set in register Table 119, “Register 0x1D”
    [7:2].
3. SWC output regulator average current goes above the threshold set in register Table 120, “Register 0x1E”
    [7:2].
4. SWD output regulator average current goes above the threshold set in register Table 121, “Register 0x1F”
    [7:2].
```

When either event occurs then PMIC sets the register Table 99, “Register 0x09” [3:0] appropriately, drives GSI_n output signal as shown in Table 27 at the same time. The PMIC continues to operate as normal. The PMIC allows access to all registers. The host is responsible for taking any specific action. The host may query the PMIC register space to determine the cause of the GSI_n signal assertion. Once host determines the cause, the host may clear the appropriate output current consumption warning status register as well as any other status registers individually or by writing ‘1’ to global status clear register in Table 110, “Register 0x14” [0] which triggers the GSI_n signal to be de-asserted. If the output current consumption warning condition is still present then PMIC will continue to assert GSI_n output signal and the appropriate status register in Table 99, “Register 0x09” [3:0] will remain at ‘1’. If the output current consumption warning condition persists, the host may set the appropriate mask register to remove GSI_n output signal as shown in Table 28 and Table 29.
