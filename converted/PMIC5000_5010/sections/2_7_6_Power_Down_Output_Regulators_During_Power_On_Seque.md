---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 2.7.6
title: Power Down Output Regulators During Power On Sequence
pages: 31-31
---
# 2.7.6 Power Down Output Regulators During Power On Sequence

During power on, as described in clause 2.7.2, it is possible that PMIC can trigger VR Disable command on its own as described in Table 27, “Events Interrupt Summary” when one or more regulators are already turned on even while other remaining output regulators are not yet turned on because PMIC has not completed the power on sequence config registers. For these type of cases, the PMIC will not execute the remaining power on sequence config registers and will immediately jump to executing the power off sequence config0 to power off sequence config3 registers. The PMIC will update the status registers and error log registers appropriately as normal because it generated VR Disable command on its own. The CAMP output signal would remain low.
