---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 2.10.3
title: Switch from I3C Basic Mode to I2C Mode
pages: 47-48
---
# 2.10.3 Switch from I3C Basic Mode to I2C Mode

The Host can put the PMIC device back in I2C mode from I3C Basic mode at any time by issuing RSTDAA CCC. When RSTDAA CCC is registered by the PMIC device, it updates the Table 140, “Register 0x32” [6] to ‘0’.
