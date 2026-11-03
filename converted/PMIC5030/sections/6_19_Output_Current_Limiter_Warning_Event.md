---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 6.19
title: Output Current Limiter Warning Event
pages: 53-54
---
# 6.19 Output Current Limiter Warning Event

The PMIC has output current limiter mechanism to limit the current on the PMIC output voltage regulators.

There are six possibilities where PMIC recognizes the current limiter event.

1. SWA output regulator current goes above the threshold set in register Table 137, Register 0x20 [7:6].

2. SWB output regulator current goes above the threshold set in register Table 137, Register 0x20 [5:4].

3. SWC output regulator current goes above the threshold set in register Table 137, Register 0x20 [3:2].

4. SWD output regulator current goes above the threshold set in register Table 137, Register 0x20 [1:0].

5. SWE output regulator current goes above the threshold set in register Table 184, Register 0x11C [7:6].

6. SWF output regulator current goes above the threshold set in register Table 184, Register 0x11C [5:4].

When either event occurs for a period longer than tOutput_Current_Limiter time then PMIC sets the register Table 116, Register 0x0B [7:4],Table 175, Register 0x108 [1:0] appropriately, drives GSI_n output signal as shown in Table 27 at the same time. The PMIC continues to operate as normal. The host is responsible for taking any specific action. The host may query the PMIC register space to determine the cause of the GSI_n signal assertion. Once host determine the cause, the host may clear the appropriate output current limiter status register as well as any other status registers individually or by writing ‘1’ to global status clear register in Table 125, Register 0x14 [0] which triggers the GSI_n signal to be de-asserted. If the output current limiter condition is still present then PMIC will continue to assert GSI_n output signal and the appropriate status register in Table 116, Register 0x0B [7:4],Table 175, Register 0x108 [1:0] will remain at ‘1’. If the output current limiter condition persists, the host may set the appropriate mask register to remove the GSI_n output signal as shown in Table 28 and Table 29.
