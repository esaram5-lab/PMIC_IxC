---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 2.12
title: Inductor Specification
pages: 99-100
---
# 2.12 Inductor Specification



## 2.12.1 Mechanical Specification

The inductor package dimensions and its recommended land patterns are defined in Table 87.

**Table 87 — Inductor Mechanical Specification**

```text
     Package Size          Reference Drawing            Recommended Land Pattern
 L (mm)      4.3 Max
                                Figure 32                      Figure 32
W (mm)       4.3 Max
                              (Left Picture)                (Right Picture)
 H (mm)      2.0 Max
```

*Figure 32 — Reference Drawing and Recommended Land Pattern* (figure; any text below/above was extracted from the drawing)

## 2.12.2 Electrical Specification

The inductor electrical specifications are defined in Table 88.

**Table 88 — Inductor Electrical Specification1**

```text
               L @ 0.5-1 MHz; 0                                                         Min L @ 3.5 A           Min L @ 6 A
 Package                                                      Max ACR @ 1               (Ipeakmax of            (Ipeakmax of
                     Bias                Max DCR
  Height
  (mm)
                    + 20%                 (mΩ)                MHz2,3(mΩ)                PMIC5010)4              PMIC5000)5
                     (μH)                                                                     (μH)                    (μH)
                        0.47                 6.9                     90                       0.30                    0.30
                        0.68                 8.4                     145                      0.38                    0.38
 2.0 Max
                         1.0                 15.5                    250                      0.56                    0.56
                         1.2                 16.5                    300                      0.67                    0.67
NOTE 1 Test condition: Ambient Temperature = 20 + 2 0C; Ambient Humidity = 65 + 5% Rh
NOTE 2 ACR definition: ACR = Rs @ 1 MHz - DCR. Measured current (1 MHz/sinusoidal): 0.52A rms for 0.47 μH, 0.36A rms for 0.68
       μH, 0.25 A rms for 1.0 μH, and 0.2 A rms for 1.2 μH; with no DC Bias for all cases.
NOTE 3 For Rs measurement, it is recommended to measure by Iwatsu SY-8218 (BH Analyzer, with NF IE-1125B), its upper compatible
       instruments or other instruments which is guaranteed on the measurement accuracy by inductor vendors.
NOTE 4 Minimum inductance is defined at DC bias current given by definition in Ipeakmax of PMIC5010; Table 5, Table 8, and
       Table 10.
NOTE 5 Minimum inductance is defined at DC bias current given by definition in Ipeakmax of PMIC5000; Table 3, Table 7, and Table 9.
```
