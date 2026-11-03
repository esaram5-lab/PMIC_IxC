---
document: JESD301-6 (PMIC5120 Power Management IC Standard, Version 1.0, February 2025)
device: PMIC5120
application: client
section: 6.9
title: GSI_n Signal
pages: 56-56
---
# 6.9 GSI_n Signal

General Status Interrupt (GSI_n) is an Open Drain output signal. By default at power on, GSI_n output is disabled. The host can enable the GSI_n output by setting Table 123, Register 0x1B [3] = ‘1’. Typically, GSI_n output is pulled up to 1KΩ resistor to 1.8 V or 3.3 V. The PMIC asserts GSI_n output for the events as described in Table 30.
