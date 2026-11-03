---
document: JESD301-2 (PMIC5100 Power Management IC Standard, Rev. 1.03, October 2022)
device: PMIC5100
application: client
section: 4
title: Performance Characteristics
pages: 20-23
---
# 4 Performance Characteristics



## 4.1 Efficiency



### 4.1.1 Efficiency with Inductor Footprint

**Table 19 — Efficiency Characteristics1**

```text
                                                Efficiency            Efficiency (% of Max Itdc Load)                   Unit          Notes
        Switch Node Output
                                               Light Load2           25%          50%           75%         100%
         SWA or SWB
                                                     83              > 90          > 88         > 85         > 82         %
(Single Phase Regulator Mode)
                                                                                                                                   3,4,5,6,7,8,
         SWA + SWB
                                                     83              > 90          > 88         > 85         > 82         %        9,10,11,12
 (Dual Phase Regulator Mode)
            SWC                                      85              > 90          > 89         > 87         > 85         %
NOTE 1 The efficiency numbers assume the inductor specification as noted in Clause 4.2.
NOTE 2 Light Load is defined as 100 mA for SWA and SWB for single phase regulator mode; 200 mA for SWA+SWB for dual phase
       regulator mode; 50 mA for SWC.
NOTE 3 VIN_Bulk = 5 V
NOTE 4 The maximum Itdc as specified in Table appropriately.
NOTE 5 When the efficiency of any given output regulator is being measured, all other switching output regulators are disabled.
NOTE 6 No external load on VOUT_1.8V, VOUT_1.0V LDO is applied.
NOTE 7 I2C/I3C Basic bus is pulled High and held static. PWR_GOOD and GSI_n signals are pulled High and held static.

NOTE 8 The efficiency includes the buck regulator loss, the PCB loss (< 4 mΩ or less). See Clause 4.2 for inductor specification assumption
       for DCR and ACR.

NOTE 9 Efficiency calculation equation: (VOUT * IOUT) / [(VIN_Bulk * IVIN_Bulk)+(VIN * IVIN)]; where VOUT, IOUT, VIN_Bulk, IVIN_Bulk, VIN,
       IVIN parameters are actual measured values.

NOTE 10 Applies at maximum ambient temperature of 65 0C (PMIC Junction temperature of 105 0C). The DCR characteristics noted above
        applies inductor temperature of 105 0C.
NOTE 11 The output buck regulator switching frequency can be set to 750 KHz.
NOTE 12 For input supply rail, probing is done at the input high frequency filter cap (0.1 uF) to PMIC pin. For output rail, probing is done at the
        output cap location at the inductor load side.
```

## 4.2 Inductor Specification



### 4.2.1 Mechanical Specification

The inductor package dimensions and its recommended land patterns are defined in Table 20.

**Table 20 — Inductor Mechanical Specification; SWA, SWB**

```text
      Package Size                  Reference Drawing                 Recommended Land Pattern
 L (mm)          3.4 Max
                                          Figure 14                               Figure 14
W (mm)           3.2 Max
                                        (Left Picture)                          (Right Picture)
 H (mm)          1.2 Max
```

**Table 21 — Inductor Mechanical Specification; SWC**

```text
    Package Size       Reference Drawing      Recommended Land Pattern
 L (mm)    2.7 Max
                            Figure 15                  Figure 15
W (mm)     2.2 Max
                          (Left Picture)             (Right Picture)
H (mm)     1.2 Max
```

*Figure 14 — Reference Drawing and Recommended Land Pattern; SWA, SWB* (figure; any text below/above was extracted from the drawing)

*Figure 15 — Reference Drawing and Recommended Land Pattern; SWC* (figure; any text below/above was extracted from the drawing)

### 4.2.2 Electrical Specification

The inductor electrical specifications are defined in Table 22 and Table 23.

**Table 22 — Inductor Electrical Specification; SWA, SWB1**

```text
 Package       L @ 0.5-1 MHz;                                                              Min L @ 6 A
  Height           0 Bias              Max DCR             Max ACR @ 1                    (Ipeakmax of 4
  (mm)              (μH)                (mΩ)               MHz2,3 (mΩ)                         (μH)
                  0.47 + 20%               14.5                    93                          0.30
 1.2 Max
                  0.68 + 20%               18.5                   113                          0.38
NOTE 1   Test condition: Ambient Temperature = 20 + 2 0C; Ambient Humidity = 65 + 5% Rh
NOTE 2 ACR definition: ACR = Rs @ 1 MHz - DCR. Measured current (1 MHz/sinusoidal): 0.49 A rms for 0.47 μH,
       0.34 A rms for 0.68 μH; with no DC Bias for all cases.
NOTE 3 For Rs measurement, it is recommended to measure by Iwatsu SY-8218 (BH Analyzer, with NF IE-1125B), its
       upper compatible instruments or other instruments which is guaranteed on the measurement accuracy by
       inductor vendors.
NOTE 4 Minimum inductance is defined at DC bias current given by definition in Ipeakmax; Table 3, Table 4, and
       Table 5.
```

**Table 23 — Inductor Electrical Specification; SWC1**

```text
 Package       L @ 0.5-1 MHz;                                                              Min L @ 2 A

  Height           0 Bias              Max DCR             Max ACR @ 1                    (Ipeakmax of 4
  (mm)              (μH)                (mΩ)               MHz2,3 (mΩ)                         (μH)

                   1.0 + 20%               48.0                   182                          0.56
 1.2 Max
                   1.5 + 20%               75.0                   300                          0.82

NOTE 1   Test condition: Ambient Temperature = 20 + 2 0C; Ambient Humidity = 65 + 5% Rh
NOTE 2 ACR definition: ACR = Rs @ 1 MHz - DCR. Measured current (1 MHz/sinusoidal): 0.33A rms for 1.0 μH,
       0.22A rms for 1.5 μH; with no DC Bias for all cases.
NOTE 3 For Rs measurement, it is recommended to measure by Iwatsu SY-8218 (BH Analyzer, with NF IE-1125B), its
       upper compatible instruments or other instruments which is guaranteed on the measurement accuracy by
       inductor vendors.
NOTE 4 Minimum inductance is defined at DC bias current given by definition in Ipeakmax; Table 3, Table 4, and
       Table 5.
```
