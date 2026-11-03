---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 6.4
title: Enabling PMIC Output Switch Voltage Regulators
pages: 31-32
---
# 6.4 Enabling PMIC Output Switch Voltage Regulators

After first power on, the PMIC automatically enables VOUT_1.8V and VOUT_1.0V LDO output regulators and primary I2C/I3C Basic port based on valid VIN_Mgmt input. Figure 16 shows the timing relationship once the PMIC receives VR Enable command and when it floats CAMP output signal; timing parameter tPMIC_PWR_GOOD_OUT applies. This timing parameter is a sum of maximum soft start time and configured delay for each power on sequence config registers that are executed plus additional 5 ms timing margin error. The waveform shows each buck regulator output soft start time and delay time once the soft start time expires for each power on sequence config0 to power on sequence config3 registers. Note that if more than one regulators are enabled in a power on sequence config register and if those regulators have different soft start time programmed, then the larger value of that soft start time is used as a reference for delay timer to start. Each regulator will still follow different soft start time to turn on the buck regulator. The specific example in Figure 16 uses only three power on sequence config0 to config2 registers and only one buck regulator is enabled in power on sequence config 0 register, power on sequence config 1 register and power on sequence config 2 register. The power on sequence config 2 register enables three phase regulator for SWA, SWB and SWE and power on sequence config 1 register enables dual phase regulator for SWC and SWF.

```text
                                                    tPMIC_PWR _G OOD_OUT

VR Enable         SWD_Soft_Start
                    R2D [3:1]

   SWD
                                                    SWC_Soft_Start
                                                      R2D [7:5]
                                     Power_On
                                   Con fig0_Delay
                                      R40 [2:0]
   SWCF

                                                                                     SWAB_So ft_Start
                                                                                        R2C [7:5]
                                                                       Power_On
                                                                     Config1_Delay
                                                                        R41 [2:0]
   SWABE

   CAMP
                     Power On Sequence                Power On Sequence Power On Sequence
                          Config0                          Config1           Config2
```

*Figure 16 — PMIC Power On Timing* (figure; any text below/above was extracted from the drawing)
