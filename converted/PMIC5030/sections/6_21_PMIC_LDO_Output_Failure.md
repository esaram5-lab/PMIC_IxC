---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 6.21
title: PMIC LDO Output Failure
pages: 54-54
---
# 6.21 PMIC LDO Output Failure

In the event where PMIC LDO outputs (VOUT_1.8V Table 114, Register 0x09 [5] or VOUT_1.0V Table 157, Register 0x33 [2]) failure occurs and PMIC cannot reliably support external communication, the PMIC has no control of CAMP signal and it is floated. The PMIC returns to “offline” state. Note that the PMIC operation itself may not be guaranteed as PMIC internally may use the LDO output voltages for its own internal operation.
