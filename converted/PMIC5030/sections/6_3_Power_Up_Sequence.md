---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 6.3
title: Power Up Sequence
pages: 28-31
---
# 6.3 Power Up Sequence

Figure 12 shows the power up initialization sequence. After VIN_Bulk supply is valid and stable, the PMIC powers up its output regulators when the system host sends VR Enable command either via I2C/I3C bus command (VR_OE pin must be pulled High via 200KΩ resistor and Table 263, Register 0x5F [5] = ‘0’) or via assertion of VR_OE pin high (if Table 263, Register 0x5F [5] = ‘1’). The PMIC shall generate its bias voltage (VBias) on its own using VIN_Bulk input supply. Further it executes Power On Sequence Config0 to Config5 as configured in register Table 232, Register 0x40 to Table 236, Register 0x44 and Table 265, Register 0x61 to enable its output regulators in the sequence as specified. The PMIC ensures CAMP signal is floated within maximum of tPMIC_PWR_GOOD_OUT after registering VR Enable command.

```text
                                               tVIN_MGMT_to_Enable
VIN_MGMT                                            tMan agement_Ready
                    tVIN_MGMT_Ramp

VOUT_1.8V
                                     t1.8V_Read y

 VOUT_1.0V                                           t1.0V_Read y
                                                        tVIN_BULK_Ramp

                                                               tVIN_BULK_to_Enable

 VIN_BULK
                                                                                           tPMIC_PWR_G OOD_OUT

  2
  I C/I3C                                                                      VR Enable       tVPP_Ramp

                                                                                                       tVDDQ_Ramp

   SWD

  SWCF

  SWABE                                                                                                    tVDD_Ramp

  CAMP                  Hi-Z
```

*Figure 12 — PMIC Power Up Sequence; VIN_Mgmt followed by VIN_Bulk* (figure; any text below/above was extracted from the drawing)

```text
                                                  tVIN_MGMT_to_Enable
VIN_MGMT                                           tMan agement_Ready
                       tVIN_MGMT_Ramp

 VOUT_1.8V
                                        t1.8V_Read y

 VOUT_1.0V                                             t1.0V_Read y

                   tVIN_BULK_Ramp                                                   tPMIC_PWR_G OOD_OUT
 VIN_BULK
                                          tVIN_BULK_to_Enable

                                                                                        tVPP_Ramp
   I2C/I3C                                                              VR Enable
                                                                                                tVDDQ_Ramp

   SWD

   SWCF
  SWABE                                                                                             tVDD_Ramp

   CAMP                      Hi-Z
```

*Figure 13 — PMIC Power Up Sequence; VIN_Bulk followed by VIN_Mgmt* (figure; any text below/above was extracted from the drawing)

```text
                                                    tVIN_Mgmt_Ramp
                                                                       tVIN_Mgmt_Ramp

VIN_Mgmt

 VOUT_1.8V
   (Valid)                                                           valid

 VOUT_1.0V
   (Valid)                                                           valid

 VIN_Bulk
  (Valid)

                  VR
  I2C/I3C
                Enable                                               valid
                            tVPP_Ramp

                                                                     valid
                                    tVDDQ_Ramp

   SWD                                                               valid

   SWCF                                                              valid
  SWABE                                 tVDD_Ramp

  CAMP
```

*Figure 14 — VIN_Mgmt Input Supply to VIN_Bulk Input Supply Switchover Function* (figure; any text below/above was extracted from the drawing)

```text
                                                      tVIN_Mgmt_Ramp
                                                                                       tVIN_Mgmt_Ramp

VIN_Mgmt

VOUT_1.8V
  (Valid)                                                                           valid

VOUT_1.0V
  (Valid)                                                                           valid

 VIN_Bulk
                                                                         VIN_Bulk can reach
  (Valid)                                                                 as low as 4.25 V

                  VR
  I2C/I3C
                Enable                                                              valid
                              tVPP_Ramp

                                                                                    valid
                                      tVDDQ_Ramp

   SWD                                                                              valid

   SWCF                                               ng                            valid

  SWABE                                   tVDD_Ramp

  CAMP
```

*Figure 15 — VIN_Bulk Transition* (figure; any text below/above was extracted from the drawing)

The timing waveform example in Figure 15 assumes VIN_Bulk threshold is set to 4.25 V in Table 131, Register 0x1A [7:5] and hence CAMP signal remains at valid High level.
