---
document: JESD301-6 (PMIC5120 Power Management IC Standard, Version 1.0, February 2025)
device: PMIC5120
application: client
section: 3.8
title: ESD Requirements
pages: 20-21
---
# 3.8 ESD Requirements

**Table 16 — ESD Requirement**

```text
  Test Model                Pin             Maximum Rating             Unit
HBM                         All                 + 2000                  V
CDM                         All                  + 500                  V
```

**Table 17 — EOS Requirement**

```text
             Pin                             Maximum Rating                  Unit           Notes
          VIN_BULK                                10                          V             1,2,3,4

NOTE 1   The test is performed on DDR5 DIMM module without any input capacitor on VIN_BULK
NOTE 2   The input source needs to follow the waveform and condition as shown in Figure 13 and Table 18.
NOTE 3   Probing is performed at the VIN_BULK pin of PMIC.
NOTE 4   Applies to VIN_Bulk and VIN pin.
```

**Table 18 — Input Source Condition**

```text
               Item                                 Value                            Notes
T (rise from 30% to 90% of peak)               0.72 μs (+ 30%)
           T1 (rise time)                      1.2 μs (+ 30%)                   T1 = 1.67*T

 T2 (duration time to half value)               50 μs (+ 20%)
         Output Impedance                            2Ω

      VUNDERSHOOT Voltage                         30% Max

            V
           1.0
           0.9

           0.5
                              T2
           0.3

           0.1

                     T                               VUNDER                      t
                    T1
```

*Figure 13 — Impulse Waveform for EOS Test (IEC 61000-4-5)* (figure; any text below/above was extracted from the drawing)
