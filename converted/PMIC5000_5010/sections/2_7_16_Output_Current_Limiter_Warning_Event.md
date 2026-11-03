---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 2.7.16
title: Output Current Limiter Warning Event
pages: 42-42
---
# 2.7.16 Output Current Limiter Warning Event

The PMIC has output current limiter mechanism to limit the current on the PMIC output voltage regulators. There are four possibilities where PMIC recognizes the current limiter event.

```text
1.   SWA output regulator current goes above the threshold set in register Table 122, “Register 0x20” [7:6].
2.   SWB output regulator current goes above the threshold set in register Table 122, “Register 0x20” [5:4].
3.   SWC output regulator current goes above the threshold set in register Table 122, “Register 0x20” [3:2].
4.   SWD output regulator current goes above the threshold set in register Table 122, “Register 0x20” [1:0].
```

When either event occurs for a period longer than tOutput_Current_Limiter time then PMIC sets the register Table 101, “Register 0x0B” [7:4] appropriately, drives GSI_n output signal as shown in Table 27 at the same time. The PMIC continues to operate as normal. The PMIC allows access to all registers. The host is responsible for taking any specific action. The host may query the PMIC register space to determine the cause of the GSI_n signal assertion. Once host determine the cause, the host may clear the appropriate output current limiter status register as well as any other status registers individually or by writing ‘1’ to global status clear register in Table 110, “Register 0x14” [0] which triggers the GSI_n signal to be de-asserted. If the output current limiter condition is still present then PMIC will continue to assert GSI_n output signal and the appropriate status register in Table 101, “Register 0x0B” [7:4] will remain at ‘1’. If the output current limiter condition persists, the host may set the appropriate mask register to remove the GSI_n output signal as shown in Table 28 and Table 29.
