---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 3.6
title: Absolute Maximum Ratings
pages: 22-23
---
# 3.6 Absolute Maximum Ratings

The absolute maximum ratings are stress ratings only. Stresses greater than those listed in Table 18, “Absolute Maximum Rating” and Table 19, “ESD Requirement”, and Table 20, “EOS Requirement” may cause permanent damage to the device. Functional operation of PMIC5200 at absolute maximum ratings is not implied. Exposure to absolute maximum rating condition for extended periods may affect long term reliability.

**Table 18 — Absolute Maximum Rating**

```text
                                                                            Maximum Rating

                             Pin                                 DC                       AC                  Unit

VIN_BULK, VIN, SWB_Disable                                     -0.3 to 6        TBD (Duration < 25 ns)         V

VOUT_1.8V, VOUT_1.0V                                          -0.3 to 2.2                   -                  V

SWA, SWD, SWB, SWC                                             -0.3 to 6       -3 to 9 (Duration < 25 ns)      V

BOOT_SWA, BOOT_SWD, BOOT_SWB, BOOT_SWC (to GND)         ng    -0.3 to 12      -0.3 to 15 (Duration < 25 ns)    V

BOOT_SWA, BOOT_SWD, BOOT_SWB, BOOT_SWC (to SWx)                -0.3 to 6                  TBD                  V

SWA_FB, SWD_FB, SWB_FB, SWC_FB (to AGND)                      -0.3 to 2.2                   -                  V

PWR_GOOD, GSI_n, VR_EN, Unlock, DVFSQ_n                       -0.3 to 5.0                   -                  V

SCL, SDA; I2C Mode only                                       -0.3 to 5.0

SCL, SDA; I3C Mode only                                       -0.3 to 2.1

PID                                                           -0.3 to 2.2                 TBD                  V

AGND, PGND                                                    -0.3 to 0.3                   -                  V
```
