---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 2.10.2
title: Switch from I2C Mode to I3C Basic Mode
pages: 47-47
---
# 2.10.2 Switch from I2C Mode to I3C Basic Mode

By default when PMIC first powers on, it operates in legacy I2C mode. The PMIC device shall operate in I2C mode until put into I3C Basic mode via command.

In I2C mode, the host is allowed to issued only 3 CCCs (DEVCTRL, SETHID, SETAASA). All other CCCs are not supported and the PMIC device may simply ignore it. The Host must issue DEVCTRL and SETHID CCC first (if required) followed by SETAASA CCC.

The Host puts the PMIC device in I3C Basic mode by issuing SETAASA CCC. When SETAASA CCC is registered by the PMIC device, it updates the Table 140, “Register 0x32” [6] to ‘1’. When SETHID CCC is registered by the PMIC device, it updates the Table 142, “Register 0x34” [3:1].
