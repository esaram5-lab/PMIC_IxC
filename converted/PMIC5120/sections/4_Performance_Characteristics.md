---
document: JESD301-6 (PMIC5120 Power Management IC Standard, Version 1.0, February 2025)
device: PMIC5120
application: client
section: 4
title: Performance Characteristics
pages: 22-26
---
# 4 Performance Characteristics



## 4.1 Efficiency

The PMIC efficiency spec is defined for the reference test board only and it is not applicable for any DIMM application board which varies from the reference test board. The reference test board includes the inductor and the PCB characteristics which complies with the footnote 8 in Table 20. The efficiency spec is only measured for one switch regulator at a time; all other switch regulators must be disabled. The PMIC switching frequency must comply with the footnote 11 in Table 20. The typical DIMM application environment, which deviates from the reference test board in that all buck regulators are turned on simultaneously, external load is carried on the LDOs, and signal interface pins may not be held static, will have lower efficiency than defined in Table 20. The combination of all variation for application environment is not subject to the efficiency spec as defined in Table 20.

### 4.1.1 Efficiency with Inductor Footprint

**Table 20 — Efficiency Characteristics1**

```text
                                          Efficiency       Efficiency (% of Max Itdc Load) Unit                Notes
        Switch Node Output
                                                       2    25%     50%       75%      100%
                                         Light Load
             SWA or SWB
                                               83           > 90     > 88     > 85      > 82      %
    (Single Phase Regulator Mode)
             SWA + SWB                                                                                  3,4,5,6,7,8,9,10,11,12
                                               83           > 90     > 88     > 85      > 82      %
     (Dual Phase Regulator Mode)

                SWC                            85           > 90     > 89     > 87      > 85      %
NOTE 1  The efficiency numbers assume the inductor specification as noted in Section 4.2.

NOTE 2  Light Load is defined as 100 mA for SWA and SWB for single phase regulator mode; 200 mA for SWA+SWB for
        dual phase regulator mode; 50 mA for SWC. Acoustic Noise prevention may be disabled in Table 150, Register 0x36

        [3:1] when measuring Light Load Efficiency.
NOTE 3 VIN_Bulk = 5 V
NOTE 4 The maximum Itdc as specified in Table 4 through Table 6, appropriately.
NOTE 5 When the efficiency of any given output regulator is being measured, all other switching output regulators are
        disabled.
NOTE 6 No external load on VOUT_1.8V, VOUT_1.0V LDO is applied.
NOTE 7 I2C/I3C Basic bus is pulled High and held static. PWR_GOOD and GSI_n signals are pulled High and held static.
NOTE 8 The efficiency includes the buck regulator loss, the PCB loss (< 4 mΩ or less). See Section 4.2 assumption for DCR
        and ACR.
NOTE 9 Efficiency calculation equation: (VOUT * IOUT) / [(VIN_Bulk * IVIN_Bulk)+(VIN * IVIN)]; where VOUT, IOUT, VIN_Bulk,
        IVIN_Bulk, VIN, IVIN parameters are actual measured values.
NOTE 10 Applies at maximum ambient temperature of 65 °C (PMIC Junction temperature of 105 °C). The DCR characteristics
        noted above applies inductor temperature of 105 °C.
NOTE 11 The output buck regulator switching frequency can be set to 750 KHz.
NOTE 12 For input supply rail, probing is done at the input high frequency filter cap (0.1 uF) to PMIC pin. For output rail,
        probing is done at the output cap location at the inductor load side.
```

## 4.2 Inductor Specification



### 4.2.1 Mechanical Specification

The inductor package dimensions and its recommended land patterns are defined in Table 21 and Table 22 for SWA and SWB, and Table 23 for SWC.

**Table 21 — Inductor Mechanical Specifications for SWA and SWB**

```text
    Package Size                                         Reference Drawing                Recommended Land Pattern

  L                                                      L:Perpendiculardirection
               3.4 Max
[mm]                            W:Paralleldirection       toeachterminal                          1.2 mm min
                                toeachterminal

                                                                                          2.7 mm max
 W
               2.7 Max
[mm]

                                                                                                           3.4 mm max
  H
                                               H

               1.2 Max
[mm]

                                                                          *Not to scale                                 *Not to scale
```

**Table 22 — Selectable Optional Mechanical Specifications for SWA and SWB by the**

```text
               Implemented Acceptable DIMM (in UDIMM and SODIMM) Design

    Package Size                                         Reference Drawing                Recommended Land Pattern

  L                                                      L:Perpendiculardirection
               4.3 Max                                                                                     1.1 mm min
[mm]                                                         toeachterminal
                                W:Paralleldirection
                                toeachterminal

                                                                                          4.3 mm max

 W
               4.3 Max
[mm]

                                                                                                           4.3 mm max

  H
                                               H

               1.2 Max
[mm]

                                                                          *Not to scale                                 *Not to scale
```

**Table 23 — Inductor Mechanical Specifications for SWC**

```text
    Package Size                                            Reference Drawing                       Recommended Land Pattern

  L                                                          L:Perpendiculardirection                           1.Ϯmmmin
                2.7 Max
[mm]                                                             toeachterminal

                                   W:Paralleldirection
                                   toeachterminal

                                                                                                      2.Ϭmmmax
 W
                2.2 Max
[mm]

                                                                                                                  Ϯ͘ϴmmmax

  H
                                                  H

                1.2 Max
[mm]

                                                                            ng*Not to scale                                     *Not to scale
```

### 4.2.2 Electrical Specifications

The inductor electrical specifications are defined in Table 24 for SWA and SWB (1.1V), and Table 25 for SWC

(1.8V), respectively.

**Table 24 — Inductor Electrical Specifications for SWA and SWB (1.1V)**

```text
                       L @ 0.5-1 MHz                                          Max ACR                                  Min L         Max L
                                                 Max DCR                                          Ipeakmax
   Size Selection         (0 Bias)                                            @ 1 MHz1,2                             @Ipeakmax     @Ipeakmax
                            [μH]
                                                  [mΩ]                                               (A)3               [μH]          (uH)
                                                                                 [mΩ]
 3.4 x 2.7 x 1.2 mm
                          0.47 + 20%                               11.0            93                8.5                 0.2               0.38
         max
 4.3 x 4.3 x1.2 mm
                          0.47 + 20%                               8.5             93                8.5                 0.27              0.47
        max
NOTE 1    ACR definition: ACR = Rs@1MHz – DCR Measured Current (1MHz/sinusoidal): 0.49Arms with No DC Bias for all
          cases.
NOTE 2    On the Rs measurement, it will be recommended to measure by Iwatsu SY-8218 (BH Analyzer, with NF IE-1125B),
          its upper compatible instruments, or other instruments which is guaranteed on the measurement accuracy by inductor
          vendors.
NOTE 3    Minimum and Maximum inductance is defined at DC bias current given by the definition of Ipeakmax.
```

 Test condition for all: Ambient Temperature=20±2 ℃, Ambient Humidity=65±5%Rh.

**Table 25 — Inductor Electrical Specifications for SWC (1.8V)**

```text
    L @ 0.5-1 MHz                                         Max ACR                    Min L
                                 Max DCR
       (0 Bias)
                                  [mΩ]                    @ 1 MHz1,2               @Ipeakmax3
         [μH]                                                [mΩ]                     [μH]
      1.0 + 20%                      36                        182                       0.5
NOTE 1    ACR definition: ACR = Rs@1MHz – DCR Measured Current (1MHz/sinusoidal): 0.33 Arms with No
          DC Bias for all cases.
NOTE 2    On the Rs measurement, it will be recommended to measure by Iwatsu SY-8218 (BH
          Analyzer, with NF IE-1125B), its upper compatible instruments, or other instruments which is
          guaranteed on the measurement accuracy by inductor vendors.
NOTE 3    Minimum Inductance is defined at DC bias current given by definition of Ipeakmax in PMIC5120.
```

 Test condition for all: Ambient Temperature=20±2 ℃, Ambient Humidity=65±5%Rh
