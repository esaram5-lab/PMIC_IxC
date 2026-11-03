---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 7.2
title: Configuration Register Addressing
pages: 63-64
---
# 7.2 Configuration Register Addressing

At first power on, by default, the PMIC accepts one byte address which covers first 256 bytes of configuration registers. To address configuration registers beyond first 256 bytes (up to 4096 bytes), the PMIC must be in a two byte address mode. The two byte address mode is configured by setting Table 153, Register 0x30 [2] = ‘1’. The PMIC supports one byte and two byte address mode in both I2C and I3C mode of operation. The PMIC returns to one byte address mode when Bus Reset event occurs or when it registers RSTDAA CCC.
