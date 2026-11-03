---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 2.5
title: Absolute Maximum Rating
pages: 18-20
---
# 2.5 Absolute Maximum Rating

The absolute maximum ratings are stress ratings only. Stresses greater than those listed in Table 22, “Absolute Maximum Rating”, Table 23, “ESD Requirement”, and Table 24, “EOS Requirement” may cause permanent damage to the device. Functional operation of the PMIC at absolute maximum ratings is not implied. Exposure to absolute maximum rating condition for extended periods may affect long term reliability.

**Table 22 — Absolute Maximum Rating**

```text
                                                                               Maximum Rating
                             Pin                                                                                       Unit
                                                                     DC                        AC
VIN_BULK                                                        -0.3 to 16.2        TBD (Duration < 25 ns)               V
VIN_Mgmt, VBIAS                                                  -0.3 to 6.0                    -                        V
VOUT_1.8V, VOUT_1.0V                                             -0.3 to 2.2                    -                        V
SWA, SWB, SWC, SWD                                              -0.3 to 16.2      -4.5 to 20 (Duration < 25 ns)          V
SWA_BOOT, SWB_BOOT, SWC_BOOT,
                                                                -0.3 to 21.0      -0.3 to 24 (Duration < 25 ns)          V
SWD_BOOT (to GND)
SWA_BOOT, SWB_BOOT, SWC_BOOT,
                                                                 -0.3 to 6.0                   TBD                       V
SWD_BOOT (to SWx)
SWAB_FB_P, SWB_FB_P, SWC_FB_P,
                                                                 -0.3 to 2.2                       -                     V
SWD_FB_P (to AGND)
SWAB_FB_N, SWC_FB_N, SWD_FB_N/PID                                -0.3 to 2.2                       -                     V
        1                                                        -0.3 to 5.0                       -                     V
CAMP , GSI_n
SCL, SDA; I2C Mode only                                          -0.3 to 5.0                   TBD                       V
SCL, SDA; I3C Mode only                                          -0.3 to 2.1                   TBD                       V
AGND, PGND                                                       -0.3 to 0.3                    -                        V

 NOTE 1 CAMP pins shall withstand the stress when connected to maximum of 15V DC source through 250 Ohm series resistor for 10
        seconds.
```

**Table 23 — ESD Requirement**

```text
  Test Model                 Pin              Maximum Rating               Unit
HBM                          All                  + 2000                    V
CDM                          All                  + 500                     V
```

**Table 24 — EOS Requirement**

```text
                Pin                                Maximum Rating                     Unit           Notes
             VIN_BULK                                   37                             V
                                                                                                    1,2,3,4
             VIN_Mgmt                                   10                             V
NOTE 1    The test is performed on DDR5 DIMM module without any input capacitor on VIN_BULK and VIN_Mgmt
NOTE 2    The input source needs to follow the waveform and condition as shown in Figure 8 and Table 25.
NOTE 3    Probing is performed at the VIN_BULK and VIN_Mgmt pin of PMIC.
NOTE 4    Each net test is performed individually.
```

**Table 25 — Input Source Condition**

```text
               Item                             Value                 Notes
T (rise from 30% to 90% of peak)           0.72 μs (+ 30%)
           T1 (rise time)                  1.2 μs (+ 30%)           T1 = 1.67*T
 T2 (duration time to half value)           50 μs (+ 20%)
         Output Impedance                        2Ω
      VUNDERSHOOT Voltage                     30% Max
```

*Figure 8 — Impulse Waveform for EOS Test (IEC 61000-4-5)* (figure; any text below/above was extracted from the drawing)
