---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 6
title: Schematics
pages: 120-122
---
# 6 Schematics



## 6.1 CAMM2 Schematic

Figure 39 shows an example schematic. Table 99 shows all component details shown in the schematics. Note that distributed capacitance across the entire CAMM is not shown in the schematic.

```text
                               P5200              VIN
                                                                     C25   C26

                                              VIN_Bulk
                                                                     C1     C2
                                                                L1

                                                 SWA                                             VOUTA
                 VOUT_1.8V                                C3         C4          C5   C6
C27        C28
                                            SWA_BOOT
                                               SWA_FB

                 VOUT_1.0V
C29        C30                                VIN_Bulk
                                                                     C7     C8

                                                                L2
                 VBIAS

C31        C32
                                                 SWB                                             VOUTB
                                                          C9         C10      C11     C12
                                             SWB_BOOT
                  SDA
                                               SWB_FB
                  SCL

                 VR_EN                        VIN_Bulk
                                                                     C13   C14
                  PID
                                                                L3
                 PWR_GOOD
                                                 SWC                                             VOUTC
                 AGND                                     C15        C16      C17     C18
                                             SWC_BOOT
                 PGND                          SWC_FB

                                              VIN_Bulk
                 SWB_Disable                                         C19    C20
      R1                                                        L4

                                                 SWD                                             VOUTD
                 GSI_n                                    C21        C22      C23     C24
                 Unlock                      SWD_BOOT
                 DVFSQ_n                       SWD_FB
```

*Figure 39 — PMIC5200 Schematic* (figure; any text below/above was extracted from the drawing)

**Table 99 — PMIC Schematic Values**

```text
  Remark      Component    Quantity   Value        Physical Size         Unit   Comment
   SWA            L1          1        0.47   4.3 mm x 4.3 mm x 1.2 mm    μH
   SWB            L2          1         1.0   3.4 mm x 2.7 mm x 1.2 mm    μH
   SWC            L3          1         1.5   2.7 mm x 2.2 mm x 1.2 mm    μH
   SWD            L4          1         1.5   2.7 mm x 2.2 mm x 1.2 mm    μH
   SWA            C1          1         0.1          0201; 10V            μF
                  C2          4         22           0603; 10V            μF
                  C3          1         0.1          0201; 10V            μF
                  C4          2         47           0603; 6.3V           μF
                  C5          1         47           0603; 6.3V           μF
                  C6          1         47           0603; 6.3V           μF
   SWB            C7          1         0.1          0201; 10V            μF
                  C8          2         22           0603; 10V            μF
                  C9          1         0.1          0201; 10V            μF
                 C10          1         47           0603; 6.3V           μF
                  C11         1         47           0603; 6.3V           μF

                 C12          1         47           0603; 6.3V           μF    Optional
   SWC           C13          1         0.1          0201; 10V            μF
                 C14          2         22           0603; 10V            μF

                 C15          1         0.1          0201; 10V            μF

                 C16          1         47           0603; 6.3V           μF
                 C17          1         47           0603; 6.3V           μF
                 C18          1         47           0603; 6.3V           μF    Optional
   SWD           C19          1         0.1          0201; 10V            μF
                 C20          2         22           0603; 10V            μF
                 C21          1         0.1          0201; 10V            μF
                 C22          1         47           0603; 6.3V           μF
                 C23          1         47           0603; 6.3V           μF
                 C24          1         47           0603; 6.3V           μF    Optional
    VIN          C25          1         0.1          0201; 10V            μF
                 C26          1         4.7          0402; 10V            μF
VOUT_1.8V        C27          1         0.1          0201; 6.3V           μF
                 C28          1         4.7          0402; 6.3V           μF
VOUT_1.0V        C29          1         0.1          0201; 6.3V           μF
                 C30          1         4.7          0402; 6.3V           μF
  VBIAS          C31          1         0.1          0201; 6.3V           μF
                 C32          1         4.7          0402; 6.3V           μF
SWB_Disable       R1          1        100             0201               KΩ
```
