---
document: JESD301-6 (PMIC5120 Power Management IC Standard, Version 1.0, February 2025)
device: PMIC5120
application: client
section: 3.7
title: Absolute Maximum Ratings
pages: 19-20
---
# 3.7 Absolute Maximum Ratings

The absolute maximum ratings are stress ratings only. Stresses greater than those listed in Table 15, Absolute Maximum Rating, Table 16, ESD Requirement, and Table 17, EOS Requirement may cause permanent damage to the device. Functional operation of the DDR5 PMIC at absolute maximum ratings is not implied. Exposure to absolute maximum rating condition for extended periods may affect long term reliability.

**Table 15 — Absolute Maximum Rating**

```text
                                                                           Maximum Rating
                          Pin                                                                                     Unit
                                                                 DC                       AC
VIN_BULK, VIN                                                 -0.3 to 6         TBD (Duration < 25 ns)             V
VOUT_1.8V, VOUT_1.0V                                         -0.3 to 2.2                    -                      V
SWA, SWB, SWC                                                 -0.3 to 6        -3 to 9 (Duration < 25 ns)          V
BOOT_SWA, BOOT_SWB, BOOT_SWC (to GND)                        -0.3 to 12      -0.3 to 15 (Duration < 25 ns)         V
BOOT_SWA, BOOT_SWB, BOOT_SWC (to SWx)                         -0.3 to 6                  TBD                       V
SWA_FB_P, SWB_FB_P, SWC_FB_P (to AGND)                       -0.3 to 2.2                    -                      V
PWR_GOOD, GSI_n, VR_EN                                       -0.3 to 5.0                    -                      V
SCL, SDA; I2C Mode only                                      -0.3 to 5.0                                           V
SCL, SDA; I3C Mode only                                      -0.3 to 2.1                                           V
PID                                                          -0.3 to 2.2                     TBD                   V
AGND, PGND                                                   -0.3 to 0.3                      -                    V
```
