---
document: JESD301-6 (PMIC5120 Power Management IC Standard, Version 1.0, February 2025)
device: PMIC5120
application: client
section: 5
title: DDR5 DIMM Schematic
pages: 26-31
---
# 5 DDR5 DIMM Schematic

Figure 14 shows an example schematic when PMIC is configured in dual phase regulator mode. Table 26, PMIC Schematic Values shows all component details shown in the schematics. Note that the distributed capacitance across the entire DIMM module is not shown in the schematic. The amount of distributed capacitance required is DIMM-specific and so is not part of the PMIC spec. The bulk and decoupling capacitance shown here is a fixed requirement.

```text
                                      VIN_Bulk
                                                                      C1         C17

                                                          L1                            VDD_OUT
                                         SWA
                  VOUT_1.8V
                                                   C2                       C3     C4
 C23        C15
                                    BOOT_SWA
                                                          L2
                                         SWB
   SPD            SCL
                                                   C5
   SPD            SDA               BOOT_SWB
                                     SWA_FB_P
 DIMM                                                                                             DIMM Gold Finger
                  VR_EN
Connector                            SWB_FB_P

                  PID                 VIN_Bulk

                                                                      C6         C18

                  GSI_n

 DIMM             PWR_GOOD            VIN_Bulk
Connector
                                                                       C7         C19

                                                          L3
                  VOUT_1.0V
 C22        C16                          SWC
                                                                             VPP_OUT
                                                   C9          C8
                                    BOOT_SWC

                                     SWC_FB_P
                  AGND

                  PGND (2x)               VIN
                                                    C33         C34
```

*Figure 14 — Dual Phase Regulator - DDR5 DIMM Schematic* (figure; any text below/above was extracted from the drawing)

Figure 15 shows an example schematic when PMIC is configured in single phase regulator mode. Table 26, PMIC Schematic Values shows all component details shown in the schematics. Note that the distributed capacitance across the entire DIMM module is not shown in the schematic. The amount of distributed capacitance required is DIMM-specific and so is not part of the PMIC spec. The bulk and decoupling capacitance shown here is a fixed requirement.

```text
                                       VIN_Bulk
                                                                     C1            C17

                                                           L1
                                                                                               VDD_OUT
                  VOUT_1.8V
                                          SWA
 C23        C15
                                                    C2                     C3

                                     BOOT_SWA
                                                           L2
                                                                                 VXX_OUT
                                          SWB
     SPD          SCL
                                                    C5                     C4
     SPD          SDA                BOOT_SWB

                                      SWA_FB_P
 DIMM             VR_EN                                                                                  DIMM Gold Finger
Connector                             SWB_FB_P

                  PID
                                       VIN_Bulk
                                                      ng             C6                  C18

                  GSI_n

 DIMM             PWR_GOOD             VIN_Bulk

Connector
                                                                          C7              C19

                  VOUT_1.0V                                L3
 C22        C16                           SWC
                                                                                VPP_OUT
                                                    C9          C8
                                     BOOT_SWC

                  AGND
                                      SWC_FB_P

                  PGND (2x)                VIN
                                                         C33         C34
```

*Figure 15 — Single Phase Regulator - DDR5 PMIC Schematic* (figure; any text below/above was extracted from the drawing)

**Table 26 — PMIC Schematic Values**

```text
               Dual Phase Regulator Mode            Single Phase Regulator Mode
Component                                                                               Unit Comment
              Value          Physical Size         Value          Physical Size
    L1                      3.4 x 2.7 x 1.2 mm                   3.4 x 2.7 x 1.2 mm
               0.47                  or             0.47                  or            μH
                            4.3 x 4.3 x 1.2 mm                   4.3 x 4.3 x 1.2 mm
    L2                      3.4 x 2.7 x 1.2 mm                   3.4 x 2.7 x 1.2 mm
               0.47                  or             0.47                  or            μH
                            4.3 x 4.3 x 1.2 mm                   4.3 x 4.3 x 1.2 mm
    L3          1.0     2.7 mm x 2.2 mm x 1.2 mm     1.0     2.7 mm x 2.2 mm x 1.2 mm   μH
    C1        22 (2x)           10 V; 0603         22 (2x)           10 V 0603          μF
    C2          0.1             10 V; 0201           0.1             10 V; 0201         μF
    C3        47 (3x)           6.3 V; 0603        47 (3x)           6.3 V; 0603        μF
    C4        47 (3x)           6.3 V; 0603        47 (3x)           6.3 V; 0603        μF
    C5          0.1             10 V; 0201           0.1             10 V; 0201         μF
    C6        22 (2x)           10 V 0603          22 (2x)           10 V 0603          μF
    C7        22 (2x)           10 V 0603          22 (2x)           10 V 0603          μF
    C8        47 (3x)           6.3 V; 0603        47 (3x)           6.3 V; 0603        μF
    C9          0.1             10 V; 0201           0.1             10 V; 0201         μF
    C15         4.7             6.3 V; 0402          4.7             6.3 V; 0402        μF
    C16         4.7             6.3 V; 0402          4.7             6.3 V; 0402        μF
    C17         0.1             10 V; 0201           0.1             10 V; 0201         μF

    C18         0.1             10 V; 0201           0.1             10 V; 0201         μF
    C19         0.1             10 V; 0201           0.1             10 V; 0201         μF
    C22         0.1             6.3 V; 0201          0.1             6.3 V; 0201        μF

    C23         0.1             6.3 V; 0201          0.1             6.3 V; 0201        μF
    C33         0.1             10 V; 0201           0.1             10 V; 0201         μF

    C34         4.7             10 V; 0402           4.7             10 V; 0402         μF
```

Figure 16 and Figure 17 show PMIC and passive component layout example for DDR5 SODIMM and DDR5 UDIMM. This layout is for reference and final layout may vary.

*Figure 16 — DDR5 DIMM PMIC Layout Example - Top Layer* (figure; any text below/above was extracted from the drawing)

*Figure 17 — DDR5 DIMM PMIC Layout Example - Bottom Layer* (figure; any text below/above was extracted from the drawing)
