---
document: JESD301-2 (PMIC5100 Power Management IC Standard, Rev. 1.03, October 2022)
device: PMIC5100
application: client
section: 5
title: DDR5 DIMM Schematic
pages: 23-28
---
# 5 DDR5 DIMM Schematic

Figure 16 shows an example schematic when PMIC is configured in dual phase regulator mode. Table 24, “PMIC Schematic Values” shows all component details shown in the schematics. Note that capacitors C25, C26, and C27 represent the lump sum of distributed capacitance across the entire DIMM.

```text
                                        VIN_Bulk
                                                                      C1            C17

                                                            L1                             VDD_OUT
                                           SWA
                    VOUT_1.8V
                                                      C2                     C3       C4              C27        C31
   C23        C15
                                      SWA_BOOT
                                                            L2
                                           SWB
    SPD             SCL
                                                      C5
    SPD             SDA               SWB_BOOT

                                       SWA_FB_P
   DIMM             VR_EN                                                                            DIMM Gold Finger
  Connector                            SWB_FB_P
                    PID                 VIN_Bulk
                                                                      C6            C18

                    GSI_n

 DIMM               PWR_GOOD            VIN_Bulk
Connector
                                                                        C7           C19

                                                            L3
                    VOUT_1.0V
   C22        C16                          SWC
                                                                              VPP_OUT
                                                      C9         C8                                  C25         C29
                                      SWC_BOOT

                    AGND               SWC_FB_P

                    PGND (2x)                VIN
                                                           C33    C34
```

*Figure 16 — Dual Phase Regulator - DDR5 DIMM Schematic* (figure; any text below/above was extracted from the drawing)

Figure 17 shows an example schematic when PMIC is configured in single phase regulator mode. Table 24, “PMIC Schematic Values” shows all component details shown in the schematics. Note that capacitors C25, C26, C27, and C28 represent the lump sum of distributed capacitance across the entire DIMM.

```text
                                         VIN_Bulk
                                                                        C1                 C17

                                                              L1                                   VDD_OUT
                                            SWA
                    VOUT_1.8V
                                                       C2                      C3                             C27        C31
   C23        C15
                                       SWA_BOOT
                                                              L2
                                                                                         VXX_OUT
                                            SWB
    SPD             SCL
                                                       C5                           C4                        C28        C32
    SPD             SDA                SWB_BOOT

                                        SWA_FB_P
   DIMM             VR_EN                                                                                    DIMM Gold Finger
  Connector
                                        SWB_FB_P
                    PID                  VIN_Bulk
                                                        ng              C6                C18

                    GSI_n
 DIMM               PWR_GOOD             VIN_Bulk

Connector
                                                                          C7               C19
                                                              L3
                    VOUT_1.0V

   C22        C16                           SWC
                                                                                VPP_OUT
                                                       C9          C8                                         C25        C29

                                       SWC_BOOT

                    AGND                SWC_FB_P

                                              VIN
                    PGND (2x)
                                                            C33     C34
```

*Figure 17 — Single Phase Regulator - DDR5 PMIC Schematic* (figure; any text below/above was extracted from the drawing)

**Table 24 — PMIC Schematic Values**

```text
                       Dual Phase Regulator Mode                       Single Phase Regulator Mode
Component                                                                                                             Unit     Comment
                    Value               Physical Size                Value               Physical Size
     L1             0.68       3.2 mm x 3.2 mm x 1.2 mm               0.68       3.2 mm x 3.2 mm x 1.2 mm              μH            1
     L2             0.68       3.2 mm x 3.2 mm x 1.2 mm               0.68       3.2 mm x 3.2 mm x 1.2 mm              μH            1
     L3              1.5       2.7 mm x 2.2 mm x 1.2 mm                1.5       2.7 mm x 2.2 mm x 1.2 mm              μH            2
     C1            22 (2x)               10 V                        22 (2x)               10 V                        μF
     C2              0.1              10 V; 0201                       0.1              10 V; 0201                     μF
     C3            47 (2x)            6.3 V; 0603                    47 (2x)            6.3 V; 0603                    μF
     C4            47 (2x)            6.3 V; 0603                    47 (2x)            6.3 V; 0603                    μF
     C5              0.1              10 V; 0201                       0.1              10 V; 0201                     μF
     C6            22 (2x)               10 V                        22 (2x)               10 V                        μF
     C7            22 (2x)               10 V                        22 (2x)               10 V                        μF
     C8            47 (2x)            6.3 V; 0603                    47 (2x)            6.3 V; 0603                    μF
     C9              0.1              10 V; 0201                       0.1              10 V; 0201                     μF
     C15             4.7              6.3 V; 0402                      4.7              6.3 V; 0402                    μF
     C16             4.7              6.3 V; 0402                      4.7              6.3 V; 0402                    μF
     C17             0.1              10 V; 0201                       0.1              10 V; 0201                     μF
     C18             0.1              10 V; 0201                       0.1              10 V; 0201                     μF
     C19             0.1              10 V; 0201                       0.1              10 V; 0201                     μF
     C22             0.1              6.3 V; 0201                      0.1              6.3 V; 0201                    μF

     C23             0.1              6.3 V; 0201                      0.1              6.3 V; 0201                    μF
     C33             0.1              10 V; 0201                       0.1              10 V; 0201                     μF

     C34             4.7              10 V; 0402                       4.7              10 V; 0402                     μF

     C25             75                  6.3 V                         75                  6.3 V                       μF
     C27            350                  6.3 V                        175                  6.3 V                       μF            3
     C28            N/A                   N/A                         175                  6.3 V                       μF
     C29             75                  6.3 V                         75                  6.3 V                       μF
     C31            350                  6.3 V                        175                  6.3 V                       μF            3
     C32            N/A                   N/A                         175                  6.3 V                       μF
NOTE 1 The usage of 0.47 μH inductor may be allowed by the PMIC vendor.
NOTE 2 The usage of 1.0 μH inductor may be allowed by the PMIC vendor.
NOTE 3 These capacitor values represent the distributed capacitance for the entire DIMM assuming max Itdc and Ipeakmax defined in Electrical
       Characteristics for each SWx. For a given DIMM design, the distributed capacitance for each SWx varies and is a function of Itdc and
       Ipeakmax current requirement for that DIMM design. See actual DIMM design for total distributed capacitance.
```

Figure 18 and Figure 19 show PMIC and passive component layout example for DDR5 SODIMM and DDR5 UDIMM. This layout is for reference and final layout may vary.

*Figure 18 — DDR5 DIMM PMIC Layout Example - Top Layer* (figure; any text below/above was extracted from the drawing)

*Figure 19 — DDR5 DIMM PMIC Layout Example - Bottom Layer* (figure; any text below/above was extracted from the drawing)
