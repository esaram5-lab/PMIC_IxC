---
document: JESD301-2 (PMIC5100 Power Management IC Standard, Rev. 1.03, October 2022)
device: PMIC5100
application: client
section: 3.8
title: ESD Requirements
pages: 18-19
---
# 3.8 ESD Requirements

**Table 15 — ESD Requirement**

```text
  Test Model                  Pin               Maximum Rating                Unit

HBM                           All                   + 2000                     V
CDM                           All                   + 500                      V
```

**Table 16 — EOS Requirement**

```text
               Pin                                 Maximum Rating                      Unit           Notes
            VIN_BULK                                    10                              V             1,2,3,4
NOTE 1   The test is performed on DDR5 DIMM module without any input capacitor on VIN_BULK
NOTE 2   The input source needs to follow the waveform and condition as shown in Figure 13 and Table 17.
NOTE 3   Probing is performed at the VIN_BULK pin of PMIC.
NOTE 4   Applies to VIN_Bulk and VIN pin.
```

**Table 17 — Input Source Condition**

```text
               Item                                         Value                            Notes
T (rise from 30% to 90% of peak)                      0.72 μs (+ 30%)
           T1 (rise time)                              1.2 μs (+ 30%)                     T1 = 1.67*T
 T2 (duration time to half value)                      50 μs (+ 20%)
         Output Impedance                                    2Ω
      VUNDERSHOOT Voltage                                30 % Max
```

*Figure 13 — Impulse Waveform for EOS Test (IEC 61000-4-5)* (figure; any text below/above was extracted from the drawing)
