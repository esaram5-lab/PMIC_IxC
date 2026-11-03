---
document: JESD301-6 (PMIC5120 Power Management IC Standard, Version 1.0, February 2025)
device: PMIC5120
application: client
section: 6.6
title: PMIC Output Rail Off Timing
pages: 49-50
---
# 6.6 PMIC Output Rail Off Timing

Figure 32 shows the timing relationship once the PMIC registers VR Disable command internally due to fault condition as listed in Table 30. The waveform shows each buck regulator output soft stop time and delay time once the soft stop time expires from each power off sequence config0 to power off sequence config2 registers. Note that if more than one regulators are disabled in a power off sequence config register and if those regulators have different soft stop time programmed, then the larger value of that soft stop time is used as a reference for delay timer to start. Each regulator will still follow different soft stop time to turn off the buck regulator.

The specific example in Figure 32 uses only three power off sequence config0 to config2 registers and only one buck regulator is disabled in power off sequence config 0, config 1 and config 2 registers.

```text
  VR Disable

     SWA

                    SWA_Soft_Stop
                      R22 [1:0]
                                     Power_Off
                                    Config0_Delay
                                      R58 [2:0]   SWB_Soft_Stop
     SWB                                            R26 [1:0]

                                                                    Power_Off
                                                                  Con fig1_Delay
                                                                     R59 [2:0]
     SWC                                                                           SWC_Soft_Stop
                                                                                     R28 [1:0]

PWR_GOOD

                      Power Off Sequence
                                                   Power Off Sequence Power Off Sequence
                           Config0                      Config1            Config2
```

*Figure 32 — PMIC Power Off Timing Due to Internal Fault Condition* (figure; any text below/above was extracted from the drawing)

## 6.6.1 Power Down Output Regulators During Power On Sequence

During power on as described in Section 6.2 it is possible that PMIC can trigger VR Disable command on its own as described in Table 30 when one or more regulators are already turned on even while other remaining output regulators are not yet turned on because PMIC has not completed the power on sequence config registers. For these type of cases, the PMIC will not execute the remaining power on sequence config registers and will immediately jump to executing the power off sequence config0 to power off sequence config2 registers. The PMIC will update the status registers and error log registers appropriately as normal because it generated VR Disable command on its own. The PWR_GOOD output signal would remain low.
