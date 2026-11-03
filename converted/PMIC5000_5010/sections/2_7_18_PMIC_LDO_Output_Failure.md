---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 2.7.18
title: PMIC LDO Output Failure
pages: 43-43
---
# 2.7.18 PMIC LDO Output Failure

In the event where PMIC LDO outputs (VOUT_1.8V or VOUT_1.0V) failure occurs and PMIC cannot reliably support external communication, the PMIC has no control of CAMP signal and it is floated. The PMIC returns to “offline” state. Note that the PMIC operation itself may not be guaranteed as PMIC internally may use the LDO output voltages for its own internal operation.
