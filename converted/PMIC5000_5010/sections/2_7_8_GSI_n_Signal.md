---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 2.7.8
title: GSI_n Signal
pages: 33-33
---
# 2.7.8 GSI_n Signal

General Status Interrupt (GSI_n) is an Open Drain output signal. By default at power on, GSI_n output is disabled. The host can enable the GSI_n output by setting Table 117, “Register 0x1B” [3] = ‘1’. Typically, GSI_n output is pulled up to 1 KΩ resistor to 1.8 V or 3.3 V. The PMIC asserts GSI_n output for the events as described in Table 27, “Events Interrupt Summary”.
