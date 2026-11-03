---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 9
title: Inductor Specification
pages: 119-120
---
# 9 Inductor Specification



## 9.1 Mechanical Specification

The inductor package dimensions and its recommended land patterns are defined in Table 101.

**Table 101 — Inductor Mechanical Specification**

```text
      Package Size             Reference Drawing            Recommended Land Pattern
 L (mm)        4.3 Max               Figure 34                           Figure 34
W (mm)         4.3 Max              (Left Picture)                   (Right Picture)

H (mm)         2.0 Max
```

*Figure 34 — Reference Drawing and Recommended Land Pattern* (figure; any text below/above was extracted from the drawing)

## 9.2 Electrical Specification

The inductor electrical specifications are defined in Table 102.

**Table 102 — Inductor Electrical Specification[1]**

```text
                   L @ 0.5-1 MHz;
                                                        Max ACR                               Min L @         Max L @
  Switch Rail          0 Bias          Max DCR                             Ipeakmax[4]
                                                       @ 1 MHz[2],[3]                       (Ipeakmax        Ipeakmax
    Target             + 20%            (mΩ)                                   (A)
                                                           (mΩ)                                (μH)             (μH)
                        (μH)
SWA, SWB, SWC,           0.47             4.2                120               9.5               0.21           0.47
  SWE, SWF
     SWD                  1.0             8.9                250               6.0               0.45            1.0
 NOTE 1    Test condition: Ambient Temperature = 20 + 2 0C; Ambient Humidity = 65 + 5% Rh
 NOTE 2    ACR definition: ACR = Rs @ 1 MHz - DCR. Measured current (1 MHz/sinusoidal): 0.52 A rms for 0.47 μH, 0.25 A
           rms for 1.0 μH; with no DC Bias for all cases.
 NOTE 3    For Rs measurement, it is recommended to measure by Iwatsu SY-8218 (BH Analyzer, with NF IE-1125B), its upper
           compatible instruments or other instruments which is guaranteed on the measurement accuracy by inductor vendors.
 NOTE 4    Minimum and maximum inductance is defined at DC bias current given by definition in Ipeakmax of PMIC5030.
```
