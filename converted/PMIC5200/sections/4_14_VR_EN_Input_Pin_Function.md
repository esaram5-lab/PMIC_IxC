---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 4.14
title: VR_EN Input Pin Function
pages: 59-60
---
# 4.14 VR_EN Input Pin Function

The PMIC offers a method to turn on and turn off all output rails with a VR_EN input pin. When valid VIN_Bulk and VIN input supplies are present, the PMIC executes VR Enable command (Table 154, Register 0x32 [7] = ‘1’) when VR_EN input pin is asserted to High. The PMIC executes power on sequence configuration registers (Table 182, Register 0x40 to Table 185, Register 0x43) and floats PWR_GOOD signal. The VR_EN pin must remain at stable high level for entire power on sequence. The PMIC executes VR Disable command (Table 154, Register 0x32 [7] = ‘0’) when VR_EN input pin is de-asserted to Low. The PMIC executes power off sequence configuration registers (Table 200, Register 0x58 to Table 203, Register 0x5B) and asserts PWR_GOOD signal Low. The VR_EN pin must remain at stable low level for entire power off sequence.
