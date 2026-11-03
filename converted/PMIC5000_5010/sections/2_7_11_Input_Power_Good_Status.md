---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 2.7.11
title: Input Power Good Status
pages: 38-38
---
# 2.7.11 Input Power Good Status

There is one possibility where PMIC recognizes the input supply fail.

```text
1. VIN_Bulk goes below the threshold set in register Table 116, “Register 0x1A” [7:5].
```

When this event occurs for a period longer than tInput_PWR_GOOD_GSI_Assertion time then PMIC sets the register Table 98, “Register 0x08” [7] and drives GSI_n and CAMP output signal as shown in Table 27 at the same time. The PMIC allows access to all registers and PMIC continues to operate as normal as long as VIN_Bulk input remains above 4.25 V. See also clause 2.7.15. The host is responsible for taking any specific action. The host may clear the VIN_Bulk input power good status register by writing ‘1’ to register Table 98, “Register 0x08” [7] or by writing ‘1’ to global status clear register Table 110, “Register 0x14” [0]. If the input power not good condition is still present then PMIC will continue to drive GSI_n and CAMP output signal as in Table 27 and the status register Table 98, “Register 0x08” [7] will remain at ‘1’. If the input power not good condition persists, the host may set the appropriate mask register to remove GSI_n or CAMP output signal as shown in Table 28 and Table 29.

Note that after VR enable command, when VIN_Mgmt input goes below the threshold set in register Table 137, “Register 0x2F” [7], it is reported as switchover event as described in clause 2.7.20. Prior to VR Enable command, the VIN_Mgmt is always required to be above 2.8 V to guarantee PMIC’s functionality as described in clause 2.7.2.
