---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 4.13
title: SWB_Disable Input Pin Function
pages: 59-59
---
# 4.13 SWB_Disable Input Pin Function

The PMIC offers a method to override SWB output rail enable function in power on sequence config0 to power on sequence config 3 registers. The SWB_Disable input pin, if enabled, communicates to PMIC to not turn on SWB output regulator even if SWB output regulator is enabled in power on sequence config0 to config3 register. By default, the SWB_Disable input pin is enabled when PMIC powers up. The host can disable the SWB_Disable pin by clearing register Table 150, Register 0x2E [5] = ‘0’. When the SWB_Disable input pin is disabled, the PMIC input receiver is off and PMIC follows the power on sequence config0 to power on sequence config3 registers and turns on appropriate rails as configured. The status register Table 173, Register 0x109 [0] does not apply and it may be either ‘0’ or ‘1’. When SWB_Disable input pin is enabled, the PMIC checks the SWB_Disable input pin level status at the time of VR Enable command (either via VR_EN pin or I2C/I3C bus command or auto power on).

▪ If the SWB_Disable input pin is low, the PMIC updates the status register Table 173, Register 0x109 [0] to ‘0’ and executes power on sequence config 0 to power on sequence config3 registers and turns on all rails including SWB accordingly as configured.

▪ If the SWB_Disable input pin is high, the PMIC updates the status register Table 173, Register 0x109 [0] to ‘1’, executes power on sequence config 0 to power on sequence config3 registers and turns on all rails except for SWB output rail. The PMIC overrides the SWB output rail in all four power on sequence config0 to config3 registers and ensures that PMIC does not turn on SWB output regulator. The PMIC follows all settings including the idle delay as configured in power on sequence config0 to power on sequence config3 registers.
