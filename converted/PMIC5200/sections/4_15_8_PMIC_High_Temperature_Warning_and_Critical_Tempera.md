---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 4.15.8
title: PMIC High Temperature Warning and Critical Temperature Protection
pages: 67-68
---
# 4.15.8 PMIC High Temperature Warning and Critical Temperature Protection

The PMIC provides a high temperature warning mechanism, as well as a critical temperature shutdown. This feature is supported regardless of whether ADC is enabled or disabled. There are two registers associated with PMIC temperature: The high temperature warning threshold register Table 131, Register 0x1B [2:0] and shutdown temperature threshold register Table 150, Register 0x2E [2:0]. The value programmed in the shutdown temperature register must be equal or greater than value programmed in a warning threshold register. There is one possibility where PMIC recognizes the high temperature event.

```text
1.    The PMIC temperature goes above the threshold set in register Table 131, Register 0x1B [2:0].

4.15.8      PMIC High Temperature Warning and Critical Temperature Protection
            (cont’d)
```

When the high-temperature event occurs for a period longer than tHigh_Temp_Warning time, the PMIC sets the register Table 113, Register 0x09 [7]. The PMIC continues to operate as normal. The PMIC allows access to all registers. The host is responsible for taking any specific action. The host may query the PMIC register space to determine the cause. Once host determines the cause, the host may clear the temperature warning status register, as well as any other status registers individually or by writing ‘1’ to global status clear register in Table 124, Register 0x14 [0]. If the high temperature warning condition is still present, then PMIC continues to status register in Table 113, Register 0x09 [7] to ‘1’. If the PMIC temperature goes above the threshold set in register Table 150, Register 0x2E [2:0] for a period longer than tShut_Down_Temp time, the PMIC internally generates VR Disable command and disables all of its switching output regulators, sets the code in register Table 109, Register 0x05 [2:0], updates Table 112, Register 0x08 [6], and PWR_GOOD output signal as shown in Table 27 at the same time. The PMIC keeps its VOUT_1.8V LDO and VOUT_1.0V LDO output regulator active. The PMIC allows access to all registers. The host is responsible for taking any specific action. The host is expected to monitor the temperature status registers. When the temperature drops below the threshold, the host must re-start the PMIC by going through the power cycle of the VIN_Bulk input supply.
