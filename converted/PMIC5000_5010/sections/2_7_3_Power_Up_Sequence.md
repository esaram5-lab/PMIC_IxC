---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 2.7.3
title: Power Up Sequence
pages: 25-29
---
# 2.7.3 Power Up Sequence

Figure 11 shows the power up initialization sequence. After VIN_Bulk supply is valid and stable, the PMIC powers up its output regulators when the system host sends VR Enable command. The PMIC generates its bias voltage (VBias) on its own using VIN_Bulk input supply. Further it executes Power On Sequence Config0 to Config3 as configured in register Table 152, “Register 0x40” to Table 155, “Register 0x43” to enable its output regulators in the sequence as specified. The PMIC also follows the settings as specified in register 0x44 to register 0x6F for each of the enabled output. The PMIC ensures CAMP signal is floated within maximum of tPMIC_PWR_GOOD_OUT after registering VR Enable command.

```text
                                               tVIN_MGMT_to_Enable
VIN_MGMT                                            tManagement_Ready
                     tVIN_MGMT_Ramp

 VOUT_1.8V
                                      t1.8V_Ready

 VOUT_1.0V                                           t1.0V_Ready

                                                        tVIN_BULK_Ramp

                                                              tVIN_BULK_to_Enable

 VIN_BULK
                                                                                          tPMIC_PWR_GOOD_OUT

   I2C/I3C                                                                    VR Enable      tVPP_Ramp
                                                                                                     tVDDQ_Ramp

    SWD

    SWC

   SWAB

                                                                                                         tVDD_Ramp

   CAMP                  Hi-Z
```

*Figure 11 — PMIC Power Up Sequence; VIN_Mgmt Followed by VIN_Bulk* (figure; any text below/above was extracted from the drawing)

```text
                                               tVIN_MGMT_to_Enable
VIN_MGMT                                        tManagement_Ready
                     tVIN_MGMT_Ramp

 VOUT_1.8V
                                      t1.8V_Ready

 VOUT_1.0V                                          t1.0V_Ready

                 tVIN_BULK_Ramp                                                  tPMIC_PWR_GOOD_OUT
 VIN_BULK
                                        tVIN_BULK_to_Enable

                                                                                    tVPP_Ramp
   I2C/I3C                                                           VR Enable
                                                                                            tVDDQ_Ramp

   SWD

   SWC

   SWAB                                                                                         tVDD_Ramp
   CAMP                    Hi-Z
```

*Figure 12 — PMIC Power Up Sequence; VIN_Bulk Followed by VIN_Mgmt* (figure; any text below/above was extracted from the drawing)

```text
                                                    tVIN_Mgmt_Ramp
                                                                               tVIN_Mgmt_Ramp

VIN_Mgmt

VOUT_1.8V
  (Valid)                                                                    valid

VOUT_1.0V
  (Valid)                                                                    valid

 VIN_Bulk
  (Valid)

                  VR
  I2C/I3C
                Enable                                                       valid
                            tVPP_Ramp

                                                                             valid
                                    tVDDQ_Ramp

   SWD                                                                       valid

   SWC                                              ng                       valid

  SWAB                                  tVDD_Ramp

  CAMP
```

*Figure 13 — VIN_Mgmt Input Supply to VIN_Bulk Input Supply Switchover Function* (figure; any text below/above was extracted from the drawing)

```text
                                                    tVIN_Mgmt_Ramp
                                                                                   tVIN_Mgmt_Ramp

VIN_Mgmt

VOUT_1.8V
  (Valid)                                                                       valid

VOUT_1.0V
  (Valid)                                                                       valid

 VIN_Bulk
                                                                     VIN_Bulk can reach
  (Valid)                                                              as low as 4.25 V

                  VR
  I2C/I3C
                Enable                                                          valid
                            tVPP_Ramp

                                                                                valid
                                    tVDDQ_Ramp

   SWD                                                                          valid

   SWC                                                                          valid
  SWAB                                  tVDD_Ramp

  CAMP
```

*Figure 14 — VIN_Bulk Transition* (figure; any text below/above was extracted from the drawing)

The timing waveform example in Figure 14 assumes VIN_Bulk threshold is set to 4.25 V in Table 116, “Register 0x1A” [7:5] and hence CAMP signal remains at valid High level.
