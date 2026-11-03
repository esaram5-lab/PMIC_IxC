---
document: JESD301-2 (PMIC5100 Power Management IC Standard, Rev. 1.03, October 2022)
device: PMIC5100
application: client
section: 6.9
title: GSI_n Signal
pages: 53-53
---
# 6.9 GSI_n Signal

General Status Interrupt (GSI_n) is an Open Drain output signal. By default at power on, GSI_n output is disabled. The host can enable the GSI_n output by setting Table 115, “Register 0x1B” [3] = ‘1’. Typically, GSI_n output is pulled up to 1 KΩ resistor to 1.8 V or 3.3 V. The PMIC asserts GSI_n output for the events as described in Table 28.
