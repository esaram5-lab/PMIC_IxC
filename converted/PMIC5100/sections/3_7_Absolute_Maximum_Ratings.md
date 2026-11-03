---
document: JESD301-2 (PMIC5100 Power Management IC Standard, Rev. 1.03, October 2022)
device: PMIC5100
application: client
section: 3.7
title: Absolute Maximum Ratings
pages: 18-18
---
# 3.7 Absolute Maximum Ratings

The absolute maximum ratings are stress ratings only. Stresses greater than those listed in Table 14, “Absolute Maximum Rating” and Table 15, “ESD Requirement” and Table 16, “EOS Requirement” may cause permanent damage to the device. Functional operation of the DDR5 PMIC at absolute maximum ratings is not implied. Exposure to absolute maximum rating condition for extended periods may affect long term reliability.

**Table 14 — Absolute Maximum Rating**

```text
                                                                             Maximum Rating
                         Pin                                                                                        Unit
                                                                   DC                        AC
VIN_BULK, VIN                                                   -0.3 to 6          TBD (Duration < 25 ns)            V
VOUT_1.8V, VOUT_1.0V                                           -0.3 to 2.2                     -                     V
SWA, SWB, SWC                                                   -0.3 to 6         -3 to 9 (Duration < 25 ns)         V
BOOT_SWA, BOOT_SWB, BOOT_SWC (to GND)                          -0.3 to 12       -0.3 to 15 (Duration < 25 ns)        V
BOOT_SWA, BOOT_SWB, BOOT_SWC (to SWx)                           -0.3 to 6                   TBD                      V
SWA_FB_P, SWB_FB_P, SWC_FB_P (to AGND)                         -0.3 to 2.2                     -                     V
PWR_GOOD, GSI_n, VR_EN                                         -0.3 to 5.0                     -                     V
SCL, SDA; I2C Mode only                                        -0.3 to 5.0
SCL, SDA; I3C Mode only                                        -0.3 to 2.1
PID                                                            -0.3 to 2.2                     TBD                   V
AGND, PGND                                                     -0.3 to 0.3                      -                    V
```
