---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 6.10
title: GSI_n Signal
pages: 41-41
---
# 6.10 GSI_n Signal

General Status Interrupt (GSI_n) is an Open Drain output signal. By default at power on, GSI_n output is disabled. The host can enable the GSI_n output by setting Table 132, Register 0x1B [3] = ‘1’. Typically, GSI_n output is pulled up to 1 KΩ resistor to 1.8 V or 3.3 V. The PMIC asserts GSI_n output for the events as described in Table 27.
