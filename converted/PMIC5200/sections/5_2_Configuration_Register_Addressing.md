---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 5.2
title: Configuration Register Addressing
pages: 73-73
---
# 5.2 Configuration Register Addressing

At first power on, by default, the PMIC accepts one byte address which covers first 256 bytes of configuration registers. To address configuration registers beyond first 256 bytes (up to 4096 bytes), the PMIC must be in a two byte address mode. The two byte address mode is configured by setting Table 152, Register 0x30 [2] = ‘1’. The PMIC supports one byte and two byte address mode in both I2C and I3C mode of operation. The PMIC returns to one byte address mode when Bus Reset event occurs or when it registers RSTDAA CCC.
