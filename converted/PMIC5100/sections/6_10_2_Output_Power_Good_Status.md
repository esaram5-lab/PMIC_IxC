---
document: JESD301-2 (PMIC5100 Power Management IC Standard, Rev. 1.03, October 2022)
device: PMIC5100
application: client
section: 6.10.2
title: Output Power Good Status
pages: 56-57
---
# 6.10.2 Output Power Good Status

The PMIC provides the voltage tolerance information to host that its output regulator may have crossed the desired dc+ac voltage tolerance from its nominal programmed setting. The nominal programmed setting for output regulator SWA, SWB and SWC is programmed in register Table 121, “Register 0x21” [7:1], Table 125, “Register 0x25” [7:1], and Table 127, “Register 0x27” [7:1] respectively. The PMIC offers the PWR_GOOD condition to be set independently for low side and high side. In addition, PMIC has two LDO regulators: VOUT_1.8V and VOUT_1.0V There are four possibilities where PMIC recognizes the output power good event for any output regulator.

```text
1. Output voltage goes below the threshold set in register Table 121, “Register 0x21” [0] for SWA or Table 125,
   “Register 0x25” [0] for SWB, or Table 127, “Register 0x27” [0] for SWC.
2. Output voltage goes above the threshold set in register Table 122, “Register 0x22” [7:6] for SWA or
   Table 126, “Register 0x26” [7:6] for SWB, or Table 128, “Register 0x28” [7:6] for SWC.
3. LDO output VOUT_1.8V goes below the threshold set in register Table 114, “Register 0x1A” [2].
4. LDO output VOUT_1.0V goes below the threshold set in register Table 114, “Register 0x1A” [0].
```

When either event occurs for a period longer than Output_PWR_GOOD_GSI_Assertion time then PMIC sets the register Table 96, “Register 0x08” [5,3:2] or Table 97, “Register 0x09” [5] or Table 139, “Register 0x33” [2] appropriately and drives PWR_GOOD and GSI_n output signal as shown in Table 28 at the same time. The PMIC may continue to operate but DDR5 DIMM functionality may not be guaranteed. The PMIC allows access to all registers. The host is responsible for taking any specific action. The host may query the PMIC register space to determine and identify the cause of the PWR_GOOD signal assertion and GSI_n signal assertion. Once host determines the cause, the host may clear the appropriate status register individually or by writing ‘1’ to global status clear register Table 108, “Register 0x14” [0] which triggers the GSI_n signal to be de-asserted and PWR_GOOD signal to be asserted.

If the output power not good condition is still present then PMIC will continue to assert GSI_n output signal and assert PWR_GOOD signal and the appropriate status register Table 96, “Register 0x08” [5,3:2], or Table 97, “Register 0x09” [5] or Table 139, “Register 0x33” [2] will remain at ‘1’. If the output power not good condition persists, the host may set the appropriate mask register to remove GSI_n or PWR_GOOD output signal as shown in Table 29 and Table 30.
