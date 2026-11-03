---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 6.5
title: Auto Power On
pages: 32-33
---
# 6.5 Auto Power On

The PMIC offers auto power on feature by setting Table 263, Register 0x5F [6] = ‘1’. When this feature is enabled, the PMIC automatically executes the VR Enable command (i.e., Table 155, Register 0x32 [7] = ‘1’) after both VIN_Bulk and VIN_Mgmt input supplies reach at stable valid levels (VR_OE pin is pulled to High via 200KΩ resistor). The PMIC executes power on sequence configuration registers (Table 232, Register 0x40 to Table 236, Register 0x44 and Table 265, Register 0x61) and floats CAMP signal. Figure 17 shows an example of Auto Power on. Once the auto power on is complete, it shows an example of VIN_Bulk fault event followed by re-enabling the output regulators with a VR Enable command on I2C bus once the VIN_Bulk is valid. VR_OE pin is pulled up High to VIN_Bulk on DIMM PCB. When the Table 263, Register 0x5F [6] = ‘1’ is burned in the DIMM vendor region, the PMIC requires valid stable VIN_Bulk and VIN_Mgmt input supplies. However, first time when this register is burned, the PMIC does not execute the VR Enable command (i.e., Table 155, Register 0x32 [7] = ‘1’) even though valid VIN_Bulk and VIN_Mgmt input supply is present. The PMIC requires complete power cycle in order to take the effect of burning the Table 263, Register 0x5F [6] = ‘1’. The PMIC considers the setting of Table 263, Register 0x5F [6:5] = ‘11’ as illegal configuration and the PMIC may not execute Power On Sequence Configuration registers.

```text
                                          Error Event:
                                        Ex. Vin_Bulk UV

      Vin_Bulk

  Vin_MGMT

  VLDO_1.8V

  VLDO_1.0V                                                                                  I2C VR_EN
                                                                                             command

       I2C/I3C           X                 R32[7]=1                  R32[7]=0
                                                                        Clear Flags             R32[7] = 1

     VR_OE Pin

SWA/B/C/E/F

                                                              VR keep disabled
                                                              until VR_EN command R32[7]=1

          SWD

        CAMP            Hi-Z
```

*Figure 17 — PMIC Auto Power On Timing* (figure; any text below/above was extracted from the drawing)
