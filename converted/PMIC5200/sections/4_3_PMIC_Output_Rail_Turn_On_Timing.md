---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 4.3
title: PMIC Output Rail Turn On Timing
pages: 30-31
---
# 4.3 PMIC Output Rail Turn On Timing

Figure 19 shows the timing relationship once the PMIC receives VR Enable command (either with VR_EN pin or on I2C/I3C Basic bus) and when it floats PWR_GOOD output signal; timing parameter tPMIC_PWR_GOOD_OUT applies. This timing parameter is a sum of maximum soft start time and configured delay for each power on sequence configuration registers that are executed plus additional 5 ms timing margin error. The waveform shows each buck regulator output soft start time and delay time once the soft start time expires for each power on sequence config0 to power on sequence config3 registers. Note that if more than one regulator are enabled in a power on sequence config register and if those regulators have different soft start time programmed, then the larger value of that soft start time is used as a reference for delay timer to start. Each regulator will still follow different soft start time to turn on the buck regulator. The specific example in Figure 19 uses three power on sequence config0 to config3 registers and only one buck regulator is enabled in each power on sequence config 0 to config 3 registers.

```text
                                                   tPMIC_PWR_GOOD_OUT

VR Enable         SWC_Soft_Start
                    R2D [3:1]

   SWC
                                                   SWB_Soft_Start
                                                     R2D [7:5]
                                     Power_On
                                   Config0_Delay
                                      R40 [2:0]
    SWB

                                                                                     SWA_Soft_Start
                                                                                       R2C [7:5]
                                                                      Power_On
                                                                    Con fig1_Delay
                                                                       R41 [2:0]
    SWA
PWR_GOOD

                     Power On Sequence               Power On Sequence Power On Sequence
                          Config0                         Config1           Config2
```

*Figure 19 — PMIC Power On Timing* (figure; any text below/above was extracted from the drawing)
