---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 4.4
title: Auto Power On
pages: 31-31
---
# 4.4 Auto Power On

The PMIC offers auto power on feature by setting Table 206, Register 0x5F [6] = ‘1’. When this feature is enabled, the PMIC automatically executes the VR Enable command (i.e., Table 154, Register 0x32 [7] = ‘1’) after VIN_Bulk input supply reach at stable valid level. The PMIC executes power on sequence configuration registers (Table 182, Register 0x40 to Table 185, Register 0x43) and floats PWR_GOOD signal. When the Table 206, Register 0x5F [6] = ‘1’ is burned in the PMIC5200 vendor region, the PMIC requires valid stable VIN_Bulk input supply. However, first time when this register is burned, the PMIC does not execute the VR Enable command (i.e., Table 154, Register 0x32 [7] = ‘1’) even though valid VIN_Bulk input supply is present. The PMIC requires complete power cycle in order to take the effect of burning the Table 206, Register 0x5F [6] = ‘1’.
