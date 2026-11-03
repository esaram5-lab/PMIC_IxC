---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 7
title: Inductor Specification
pages: 122-125
---
# 7 Inductor Specification



## 7.1 Mechanical Specification

The inductor package dimensions and its recommended land patterns are defined in Figure 40 to Figure 42.

*Figure 40 — Reference Drawing and Recommended Land Pattern; SWA* (figure; any text below/above was extracted from the drawing)

*Figure 41 — Reference Drawing and Recommended Land Pattern; SWB* (figure; any text below/above was extracted from the drawing)

*Figure 42 — Reference Drawing and Recommended Land Pattern; SWC, SWD* (figure; any text below/above was extracted from the drawing)

## 7.2 Electrical Specification

The inductor electrical specifications are defined in Table 100 to Table 102.

**Table 100 — Inductor Electrical Specification; SWA[1]**

```text
  Package Height       L @ 0.5-1 MHz; 0 Bias        Max DCR            Max ACR @ 1               Min L @ Ipeakmax of [4]
        (mm)                    (μH)                  (mΩ)             MHz[2],[3] (mΩ)                      (μH)
      1.2 Max                0.47 + 20%                8.5                    93                            0.24
NOTE1    Test condition: Ambient Temperature = 20 + 2 0C; Ambient Humidity = 65 + 5% Rh
NOTE2    ACR definition: ACR = Rs @ 1 MHz - DCR. Measured current (1 MHz/sinusoidal): 0.52A rms with no DC Bias for all cases.
NOTE3    For Rs measurement, it is recommended to measure by Iwatsu SY-8218 (BH Analyzer, with NF IE-1125B), its upper
         compatible instruments or other instruments which is guaranteed on the measurement accuracy by inductor vendors.
NOTE4    Minimum inductance is defined at DC bias current given by definition in Ipeakmax; Table 4.
```

**Table 101 — Inductor Electrical Specification; SWB[1]**

```text
  Package Height       L @ 0.5-1 MHz; 0 Bias        Max DCR            Max ACR @ 1               Min L @ Ipeakmax of [4]
        (mm)                    (μH)                  (mΩ)             MHz[2],[3] (mΩ)                      (μH)
      1.2 Max                1.0 + 20%                  22                   185                             0.7
NOTE1    Test condition: Ambient Temperature = 20 + 2 0C; Ambient Humidity = 65 + 5% Rh

NOTE2    ACR definition: ACR = Rs @ 1 MHz - DCR. Measured current (1 MHz/sinusoidal): 0.13A rms with no DC Bias for all cases.
NOTE3    For Rs measurement, it is recommended to measure by Iwatsu SY-8218 (BH Analyzer, with NF IE-1125B), its upper

         compatible instruments or other instruments which is guaranteed on the measurement accuracy by inductor vendors.
NOTE4    Minimum inductance is defined at DC bias current given by definition in Ipeakmax; Table 6.
```

**Table 102 — Inductor Electrical Specification; SWC, SWD[1]**

```text
  Package Height       L @ 0.5-1 MHz; 0 Bias        Max DCR            Max ACR @ 1               Min L @ Ipeakmax of [4]
        (mm)                    (μH)                  (mΩ)             MHz[2],[3] (mΩ)                      (μH)
     1.2 Max                 1.5 + 20%                  36                   300                             1.0
NOTE1    Test condition: Ambient Temperature = 20 + 2 0C; Ambient Humidity = 65 + 5% Rh
NOTE2    ACR definition: ACR = Rs @ 1 MHz - DCR. Measured current (1 MHz/sinusoidal): 0.22A rms with no DC Bias for all cases.
NOTE3    For Rs measurement, it is recommended to measure by Iwatsu SY-8218 (BH Analyzer, with NF IE-1125B), its upper
         compatible instruments or other instruments which is guaranteed on the measurement accuracy by inductor vendors.
NOTE4    Minimum inductance is defined at DC bias current given by definition in Ipeakmax, Table 5, and Table 7.
```
