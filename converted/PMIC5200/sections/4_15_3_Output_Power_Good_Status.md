---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 4.15.3
title: Output Power Good Status
pages: 64-65
---
# 4.15.3 Output Power Good Status

The PMIC provides the voltage tolerance information to host that its output regulator may have crossed the desired DC+AC voltage tolerance from its nominal programmed setting. The nominal programmed setting for output regulator SWA, SWD, SWB, and SWC is programmed in register Table 137, Register 0x21, [7:1], Table 139, Register 0x23, [7:1], Table 141, Register 0x25, [7:1], and Table 143, Register 0x27, [7:1], respectively. The PMIC offers the PWR_GOOD condition to be set independently for low side and high side. In addition, PMIC has two LDO regulators: VOUT_1.8V and VOUT_1.0V There are four possibilities where PMIC recognizes the output power good event for any output regulator.

```text
1.    Output voltage goes below the threshold set in register Table 137, Register 0x21, [0] for SWA, or
      Table 139, Register 0x23, [0] for SWD, or Table 141, Register 0x25, [0] for SWB, or Table 143, Reg-
      ister 0x27, [0] for SWC.
2.    Output voltage goes above the threshold set in register Table 138, Register 0x22, [7:6] for SWA, or

      Table 140, Register 0x24 [7:6] for SWD, or Table 142, Register 0x26, [7:6] for SWB, or Table 144,
      Register 0x28, [7:6] for SWC.

3.    LDO output VOUT_1.8V goes below the threshold set in register Table 130, Register 0x1A [2].

4.    LDO output VOUT_1.0V goes below the threshold set in register Table 130, Register 0x1A [0].
```

When either event occurs for a period longer than tOutput_PWR_GOOD_Assertion time, then PMIC sets the register Table 112, Register 0x08 [5:2] or Table 113, Register 0x09 [5] or Table 155, Register 0x33 [2] appropriately and asserts PWR_GOOD signal as shown in Table 27 at the same time. The PMIC may continue to operate but PMIC5200 functionality may not be guaranteed. The PMIC allows access to all registers. The host is responsible for taking any specific action. The host may query the PMIC register space to determine and identify the cause of the PWR_GOOD signal assertion. Once host determines the cause, the host may clear the appropriate status register individually or by writing ‘1’ to global status clear register Table 124, Register 0x14 [0] and PMIC floats the PWR_GOOD signal. If the output power not good condition is still present then PMIC continues to assert PWR_GOOD signal and the appropriate status register Table 112, Register 0x08 [5:2], or Table 113, Register 0x09 [5], or Table 155, Register 0x33 [2] remains at ‘1’.
