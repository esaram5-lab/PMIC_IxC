---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 4.10
title: GSI_n Pin Function
pages: 50-51
---
# 4.10 GSI_n Pin Function

```text
General Status Interrupt (GSI_n) is an open drain output signal. By default at power on, GSI_n output is
disabled. The host can enable the GSI_n output by setting Table 131, Register 0x1B [3] = ‘1’. Typically
GSI_n output is pulled up to 1 KΩ resistor to 1.8 V or 3.3 V. The PMIC asserts GSI_n output for the event
as described in Table 27.
```
