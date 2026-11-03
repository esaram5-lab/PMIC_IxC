---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 4.15.1
title: Input Power Good Status
pages: 63-63
---
# 4.15.1 Input Power Good Status

There is one possibility where PMIC recognizes the input supply fail.

```text
1.     VIN_Bulk goes below the threshold set in register Table 130, Register 0x1A [7:6]
```

When this event occurs for a period longer than tInput_PWR_GOOD_GSI_Assertion time, then PMIC sets the register Table 112, Register 0x08 [7] and drives GSI_n and PWR_GOOD output signal as shown in Table 27 at the same time. The PMIC allows access to all registers and PMIC continues to operate as normal as long as VIN_Bulk input remains above 3.0 V. See also Section 4.15.5. The host is responsible for taking any specific action. The host may clear the VIN_Bulk input power good status register by writing ‘1’ to register Table 120, Register 0x10 [7] or by writing ‘1’ to global status clear register Table 124, Register 0x14 [0]. If the input power not good condition is still present, then PMIC will continue to drive GSI_n and PWR_GOOD output signal as in Table 27 and the status register Table 112, Register 0x08 [7] will remain at ‘1’. If the input power not good condition persists, the host may set the appropriate mask register to remove GSI_n or PWR_GOOD output signal as shown in Table 28 and Table 29.
