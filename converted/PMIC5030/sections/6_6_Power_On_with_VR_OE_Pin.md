---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 6.6
title: Power On with VR_OE Pin
pages: 33-35
---
# 6.6 Power On with VR_OE Pin

The PMIC offers a feature to turn on the output regulators with a dedicated pin by setting Table 263, Register 0x5F [5] = ‘1’. When this feature is enabled VR_OE pin must be held at Low while VIN_Bulk and VIN_Mgmt input supplies are ramping up. When valid stable VIN_Bulk and VIN_Mgmt input supplies are present, the PMIC executes VR Enable command (i.e., Table 155, Register 0x32 [7] = ‘1’) when VR_OE input pin is asserted to High. The PMIC executes power on sequence configuration registers (Table 232, Register 0x40 to Table 236, Register 0x44 and Table 265, Register 0x61), floats CAMP signal and enters in write-protect mode if Table 152, Register 0x2F [2] = ‘0’. The VR_OE pin must remain at stable high level for entire power on sequence.

The PMIC executes VR Disable command (i.e., Table 155, Register 0x32 [7] = ‘0’), when VR_OE input pin is de-asserted to Low. The PMIC executes power off sequence configuration registers (Table 256, Register 0x58 to Table 260, Register 0x5C and Table 266, Register 0x62), asserts CAMP signal low and PMIC returns to non-write-protect mode. The PMIC executes VR Disable command (i.e., Table 155, Register 0x32 [7] = ‘0’) even if Table 263, Register 0x5F [5] = ‘0’ when VR_OE input pin is Low. The VR_OE pin must remain at stable low level for entire power off sequence. When the Table 263, Register 0x5F [5] = ‘1’ is burned in the DIMM vendor region, the PMIC requires valid stable VIN_Bulk and VIN_Mgmt input supplies. However, first time when this register is burned, the VR_OE pin shall be held low. The PMIC requires complete power cycle in order to take the effect of burning the Table 263, Register 0x5F [5] = ‘1’. The PMIC considers the setting of Table 263, Register 0x5F [6:5] = ‘11’ as illegal configuration; the PMIC may not execute Power On Sequence Configuration registers.

```text
     Vin_Bulk                    tVIN_Bulk_to_Enable

  Vin_MGMT                        tVIN_Mgmt_to_Enable

  VLDO_1.8V

  VLDO_1.0V

     I2C/I3C              X                  R32 = 0x20     R32 = 0xA0       R32 = 0x20      R32 = 0xA0

  VR_OE_PIN

SWA/B/C/E/F

        SWD

       CAMP              Hi-Z
```

*Figure 18 — PMIC Power On with VR_OE Pin* (figure; any text below/above was extracted from the drawing)
