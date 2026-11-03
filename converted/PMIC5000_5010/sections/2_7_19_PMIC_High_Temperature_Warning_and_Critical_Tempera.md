---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 2.7.19
title: PMIC High Temperature Warning and Critical Temperature Protection
pages: 43-44
---
# 2.7.19 PMIC High Temperature Warning and Critical Temperature Protection

The PMIC provides a high temperature warning mechanism as well as critical temperature shutdown. There are two registers associated with PMIC temperature: The high temperature warning threshold register Table 117, “Register 0x1B” [2:0] and shutdown temperature threshold register Table 136, “Register 0x2E” [2:0]. The value programmed in the shutdown temperature register must be equal or greater than value programmed in a warning threshold register. There is one possibility where PMIC recognizes the high temperature event.

```text
1. The PMIC temperature goes above the threshold set in register Table 117, “Register 0x1B” [2:0].
```

When the above event occurs for a period longer than tHigh_Temp_Warning time, the PMIC sets the register Table 99, “Register 0x09” [7] and drives GSI_n output signal as shown in Table 27 at the same time. The PMIC continues to operate as normal. The PMIC allows access to all registers. The host is responsible for taking any specific action. The host is responsible for taking any specific action. The host may query the PMIC register space to determine the cause of the GSI_n signal assertion. Once host determines the cause, the host may clear the temperature warning status register as well as any other status registers individually or by writing ‘1’ to global status clear register in Table 110, “Register 0x14” [0] which triggers the GSI_n signal to be de-asserted. If the high temperature warning condition is still present then PMIC will continue to assert GSI_n output signal and the appropriate status register in Table 99, “Register 0x09” [7] will remain at ‘1’. If the high temperature warning condition persists, the host may set the appropriate mask register to remove GSI_n output signal as shown in Table 28 and Table 29.

If the PMIC temperature goes above the threshold set in register Table 136, “Register 0x2E” [2:0] for a period longer than tShut_Down_Temp time, the PMIC internally generates VR Disable command and disables all of its switching output regulators as well as Vbias voltage regulator (optional), sets the code in register Table 95, “Register 0x05” [2:0], updates Table 98, “Register 0x08” [6], drives GSI_n and CAMP output signal as shown in Table 27 at the same time. The PMIC keeps its VOUT_1.8V LDO and VOUT_1.0V LDO output regulator active. The PMIC allows access to all registers. The host is responsible for taking any specific action. The host is expected to monitor the temperature status registers. When the temperature drops below the threshold, the host must re-start the PMIC by going through the power cycle of the VIN_Mgmt and VIN_Bulk input supply. If the PMIC is in VIN_Bulk input supply switchover state, the host must re-start the PMIC by going through the power cycle of the VIN_Bulk input supply.
