---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 6.29
title: Error Log Count Enhancement
pages: 59-59
---
# 6.29 Error Log Count Enhancement

The PMIC5030 enhances the global history of error log register definition by storing the detail fault information for first fifteen fault events. The history of fault information is not erasable by the controller. This enhances the PMIC’s ability to debug the failure mechanism in the event when PMIC is returned to the PMIC vendor. There is no change in the definition for Table 109, Register 0x04 [7:4] compared to previous generation of PMIC5020 or PMIC5000 or PMIC5010 definition. The PMIC5030 defines the additional register Table 109, Register 0x04 [3:0] which indicates how many times the fault has occurred and for each fault it points to additional registers for detail log information as shown in the description for Table 109, Register 0x04 [3:0]. When there are multiple buck regulator faults in one event (e.g., SWAB, SWE and SWF UV fault occurs at the same time) that causes the PMIC to turn off all the output regulators, it counts as one error and corresponding detail error log register captures all three faults. When error injection function is applied, the PMIC updates Table 109, Register 0x04 [7:4], Table 110, Register 0x05 [7:0], Table 111, Register 0x06 [7:0], Table 112, Register 0x07 [7:0], The PMIC shall not update Table 109, Register 0x04 [3:0] and Table 201, Register 0x140 [7:0] to Table 230, Register 0x15D [7:0].
