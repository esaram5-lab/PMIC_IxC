---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 6.20
title: Output High Current Consumption Warning Event
pages: 54-54
---
# 6.20 Output High Current Consumption Warning Event

The PMIC supports high output current consumption warning mechanism for each of its regulator output. If enabled, the PMIC actively monitors the average output current of the regulator. There are six possibilities where PMIC recognizes the high output current consumption.

1. SWA output regulator average current goes above the threshold set in register Table 133, Register 0x1C [7:0].

2. SWB output regulator average current goes above the threshold set in register Table 134, Register 0x1D [7:0].

3. SWC output regulator average current goes above the threshold set in register Table 135, Register 0x1E [7:0].

4. SWD output regulator average current goes above the threshold set in register Table 136, Register 0x1F [7:0].

5. SWE output regulator average current goes above the threshold set in register Table 182, Register 0x11A [7:0].

6. SWF output regulator average current goes above the threshold set in register Table 183, Register 0x11B [7:0]. When either event occurs then PMIC sets the register Table 114, Register 0x09 [3:0],Table 175, Register 0x108 [5:4] appropriately, drives GSI_n output signal as shown in Table 27 at the same time. The PMIC continues to operate as normal. The host is responsible for taking any specific action. The host may query the PMIC register space to determine the cause of the GSI_n signal assertion. Once host determines the cause, the host may clear the appropriate output current consumption warning status register as well as any other status registers individually or by writing ‘1’ to global status clear register in Table 125, Register 0x14 [0] which triggers the GSI_n signal to be de-asserted. If the output current consumption warning condition is still present then PMIC will continue to assert GSI_n output signal and the appropriate status register in Table 114, Register 0x09 [3:0],Table 175, Register 0x108 [5:4] will remain at ‘1’. If the output current consumption warning condition persists, the host may set the appropriate mask register to remove GSI_n output signal as shown in Table 28 and Table 29.
