---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 5.4
title: Absolute Maximum Rating
pages: 24-26
---
# 5.4 Absolute Maximum Rating

The absolute maximum ratings are stress ratings only. Stresses greater than those listed in Table 21, Absolute Maximum Rating, Table 22, ESD Requirement, and Table 23, EOS Requirement may cause permanent damage to the device. Functional operation of the PMIC at absolute maximum ratings is not implied. Exposure to absolute maximum rating condition for extended periods may affect long term reliability.

**Table 21 — Absolute Maximum Rating**

```text
                                                                                     Maximum Rating
                                Pin                                       DC                           AC                    Unit
VIN_BULK, VR_OE                                                       -0.3 to 16.2       TBD (Duration < 25 ns)               V
VIN_Mgmt, VBIAS1, VBIAS2                                              -0.3 to 6.0                      -                      V
VOUT_1.8V, VOUT_1.0V                                                  -0.3 to 2.2                      -                      V
SWA, SWB, SWC, SWD, SWE, SWF                                          -0.3 to 16.2     -4.5 to 20 (Duration < 25 ns)          V
SWA_BOOT, SWB_BOOT, SWC_BOOT, SWD_BOOT,                               -0.3 to 21.0     -0.3 to 24 (Duration < 25 ns)          V
SWE_BOOT, SWF_BOOT (to GND)
SWA_BOOT, SWB_BOOT, SWC_BOOT, SWD_BOOT,                               -0.3 to 6.0                    TBD                      V
SWE_BOOT, SWF_BOOT (to SWx)
SWA_FB, SWB_FB, SWC_FB, SWD_FB, SWE_FB, SWF_FB (to                    -0.3 to 2.2                      -                      V
AGND)
PID                                                                   -0.3 to 2.2                      -                      V
CAMP[1], GSI_n, Reset_n                                               -0.3 to 5.0                      -                      V

SCL, SDA; I2C Mode only                                               -0.3 to 5.0                    TBD                      V
SCL, SDA; I3C Mode only                                               -0.3 to 2.1                    TBD                      V

AGND, PGND                                                            -0.3 to 0.3                      -                      V

 NOTE 1    CAMP pins shall withstand the stress when connected to maximum of 15 V DC source through 250 Ohm series resistor for
           10 seconds.
```

**Table 22 — ESD Requirement**

```text
Test Model              Pin              Maximum Rating               Unit
      HBM               All                    + 2000                  V
      CDM               All                     + 500                  V
```

**Table 23 — EOS Requirement**

```text
               Pin                            Maximum Rating                  Unit                Notes
           VIN_BULK                                   37                        V               [1],[2],[3],[4]

           VIN_Mgmt                                   10                        V
NOTE 1     The test is performed on DDR5 DIMM module without any input capacitor on VIN_BULK and
           VIN_Mgmt
NOTE 2     The input source needs to follow the waveform and condition as shown in Figure 11 and Table 24.
NOTE 3     Probing is performed at the VIN_BULK and VIN_Mgmt pin of PMIC.
NOTE 4     Each net test is performed individually.
```

**Table 24 — Input Source Condition**

```text
              Item                               Value               Notes

T (rise from 30% to 90% of peak)            0.72 μs (+ 30%)

          T1 (rise time)                     1.2 μs (+ 30%)        T1 = 1.67*T

 T2 (duration time to half value)            50 μs (+ 20%)

       Output Impedance                           2Ω

     VUNDERSHOOT Voltage                       30% Max
```

*Figure 11 — Impulse Waveform for EOS Test (IEC 61000-4-5)* (figure; any text below/above was extracted from the drawing)
