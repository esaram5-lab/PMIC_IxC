---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 4.7
title: PMIC Output Rail Off Timing Due to Fault Event
pages: 43-44
---
# 4.7 PMIC Output Rail Off Timing Due to Fault Event

Figure 28 shows the timing relationship once the PMIC registers VR Disable command internally due to fault condition on SWA output as listed in Table 27, Events Interrupt Summary. The waveform shows each buck regulator output soft stop time and delay time once the soft stop time expires from each power off sequence config0 to power off sequence config3 registers. Note that, if more than one regulator is disabled in a power off sequence config register and if those regulators have different soft stop time programmed, then the larger value of that soft stop time is used as a reference for delay timer to start. Each regulator will still follow different soft stop time to turn off the buck regulator. The specific example in Figure 28 uses four power off sequence config0 to config3 registers and only one buck regulator is disabled in each power off sequence config 0, config 1,config2, and config 3 registers.

Internal VR Disable Due to Fault Event

```text
    SWA

                      SWA Soft
                      Stop Time
                                  Power Off Config0
                                   Delay R58[2:0]
                                                      SWB Soft
                                                      Stop Time
     SWB

                                                                  Power Off Config1
                                                                   Delay R59[2:0]

    SWC                                                                               SWC Soft
                                                                                      Stop Time

                                                                                                                            SWD Soft
   SWD                                                                                                                      Stop Time
                                                                                                     Power Off Config3
                                                                                 ng                   Delay R5A[2 :0]

PWR_GOOD

                   Power Off Sequence Config0         Power Off Sequence              Power Off Sequence Config2         Power Off Sequence Config3
                                                           Config1
```

*Figure 28 — PMIC Power Off Timing Due to Internal Fault Condition* (figure; any text below/above was extracted from the drawing)

## 4.7.1 Power Down Output Regulators During Power On Sequence

During power on as described in Clause 4.2, it is possible that PMIC can trigger VR Disable command on its own as described in Table 27, Events Interrupt Summary when one or more regulators are already turned on even while other remaining output regulators are not yet turned on because PMIC has not completed the power on sequence config registers. For these types of cases, the PMIC will not execute the remaining power on sequence config registers and will immediately jump to executing the power off sequence config0 to power off sequence config3 registers. The PMIC will update the status registers and error log registers appropriately as normal because it generated VR Disable command on its own. The PWR_GOOD output signal would remain low.
