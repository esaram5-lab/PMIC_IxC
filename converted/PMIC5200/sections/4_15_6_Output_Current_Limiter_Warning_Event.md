---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 4.15.6
title: Output Current Limiter Warning Event
pages: 66-67
---
# 4.15.6 Output Current Limiter Warning Event

The PMIC has output current limiter mechanism to limit the current on the PMIC output voltage regulators. This feature is supported regardless of whether ADC is enabled or disabled. There are four possibilities where PMIC recognizes the current limiter event.

```text
1.    SWA output regulator current goes above the threshold set in register Table 136, Register 0x20
      [7:6].
2.    SWD output regulator current goes above the threshold set in register Table 136, Register 0x20
      [5:4].
3.    SWB output regulator current goes above the threshold set in register Table 136, Register 0x20
      [3:2].
4.    SWC output regulator current goes above the threshold set in register Table 136, Register 0x20
      [1:0].
```

When either event occurs for a period longer than tOutput_Current_Limiter time, then PMIC sets the register Table 115, Register 0x0B [7:4] appropriately. The PMIC continues to operate as normal and PWR_GOOD output remains high as shown Table 27. The PMIC allows access to all registers. The host is responsible for taking any specific action. The host may query the PMIC register space. Once host determine the cause, the host may clear the appropriate output current limiter status register as well as any other status registers individually or by writing ‘1’ to global status clear register in Table 124, Register 0x14 [0]. If the output current limiter condition is still present then PMIC continues to assert the appropriate status register in Table 115, Register 0x0B [7:4] to ‘1’.
