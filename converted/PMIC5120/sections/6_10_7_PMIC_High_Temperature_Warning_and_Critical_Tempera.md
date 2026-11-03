---
document: JESD301-6 (PMIC5120 Power Management IC Standard, Version 1.0, February 2025)
device: PMIC5120
application: client
section: 6.10.7
title: PMIC High Temperature Warning and Critical Temperature Protection
pages: 62-63
---
# 6.10.7 PMIC High Temperature Warning and Critical Temperature Protection

The PMIC provides a high temperature warning mechanism as well as critical temperature shutdown. There are two registers associated with PMIC temperature: The high temperature warning threshold register Table 123, Register 0x1B [2:0] and shutdown temperature threshold register Table 142, Register 0x2E [2:0]. The value programmed in the shutdown temperature register must be equal or greater than value programmed in a warning threshold register.

There is one possibility where PMIC recognizes the high temperature event.

```text
1.   The PMIC temperature goes above the threshold set in register Table 123, Register 0x1B [2:0].
```

When the above event occurs for a period longer than tHigh_Temp_Warning time, the PMIC sets the register Table 105, Register 0x09 [7] and drives GSI_n output signal as shown in Table 30 at the same time. The PMIC continues to operate as normal. The PMIC allows access to all registers. The host is responsible for taking any specific action. The host may query the PMIC register space to determine the cause of the GSI_n signal assertion. Once host determines the cause, the host may clear the temperature warning status register as well as any other status registers individually or by writing ‘1’ to global status clear register in Table 116, Register 0x14 [0] which triggers the GSI_n signal to be de-asserted. If the high temperature warning condition is still present then PMIC will continue to assert GSI_n output signal and the appropriate status register in Table 105, Register 0x09 [7] will remain at ‘1’. If the high temperature warning condition persists, the host may set the appropriate mask register to remove GSI_n output signal as shown in Table 31 and Table 32.

If the PMIC temperature goes above the threshold set in register Table 142, Register 0x2E [2:0] for a period longer than tShut_Down_Temp time, the PMIC internally generates VR Disable command and disables all of its switching output regulators, sets the code in register Table 101, Register 0x05 [2:0], updates Table 104, Register 0x08 [6], drives GSI_n and PWR_GOOD output signal as shown in Table 30 at the same time. The PMIC keeps its VOUT_1.8V LDO and VOUT_1.0V LDO output regulator active. The PMIC allows access to all registers. The host is responsible for taking any specific action. The host is expected to monitor the temperature status registers. When the temperature drops below the threshold, the host must re-start the PMIC by going through the power cycle of the VIN_Bulk input supply.
