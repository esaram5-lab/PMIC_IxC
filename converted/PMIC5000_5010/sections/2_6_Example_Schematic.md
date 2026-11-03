---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 2.6
title: Example Schematic
pages: 20-23
---
# 2.6 Example Schematic

Figure 9 shows an example schematic when PMIC is configured in dual phase regulator mode. Table 26, “PMIC Schematic Values” shows all component details shown in the schematics. Note that capacitors C25, C26, C27, C29, C30, and C31 represent the lump sum of distributed capacitance across the entire DIMM.

VIN_Mgmt

```text
                  VIN_Mgmt                VIN_Bulk
                                                                          C1          C17
  C24       C14

                                                               L1                               VDD_OUT
                                             SWA
                  VOUT_1.8V
                                                         C2                     C3         C4              C27        C31
   C23      C15
                                       SWA_BOOT
                                                               L2
                                             SWB
                  SCL
                                                        C5
                  SDA                  SWB_BOOT

                  SWB_FB_P             SWAB_FB_P
                  RFU1/RFU2                                                                               DIMM Gold Finger
                                       SWAB_FB_N

                                          VIN_Bulk
                                                          ng              C6          C18

                  GSI_n
 DIMM             CAMP                    VIN_Bulk

Connector
                                                                           C7             C19
                                                               L3
                  VOUT_1.0V

   C22      C16                              SWC
                                                                                VDDQ_OUT
                                                         C9         C8                                    C25       C29

                                       SWC_BOOT

                                        SWC_FB_P

                                        SWC_FB_N

                  VBias                   VIN_Bulk
   C21      C13                                                           C10             C20

                                                               L4

                                             SWD
                  AGND                                                          VPP_OUT
                                                         C12        C11                          C26        C30

                                       SWD_BOOT
                  PGND (2x)
                                        SWD_FB_P

                                     SWD_FB_N/PID
```

*Figure 9 — Dual Phase Regulator Example Schematic* (figure; any text below/above was extracted from the drawing)

Figure 10 shows an example schematic when PMIC is configured in single phase regulator mode. Table 26, “PMIC Schematic Values” shows all component details shown in the schematics. Note that capacitors C25, C26, C27, C28, C29, C30, C31, and C32 represent the lump sum of distributed capacitance across the entire DIMM.

VIN_Mgmt

```text
                  VIN_Mgmt             VIN_Bulk
 C24        C14                                                        C1             C17

                                                             L1
                  VOUT_1.8V                                                                   VDD_OUT
                                           SWA
 C23        C15                                                                                                         C31
                                                      C2                     C3                            C27

                                     SWA_BOOT
                                                             L2
                                           SWB
                  SCL                                                                      VXX_OUT
                                                      C5                     C4                            C28          C32
                  SDA                SWB_BOOT

                                    SWAB_FB_P
                  RFU1/RFU2                                                                                DIMM Gold Finger
                                    SWAB_FB_N

                                       VIN_Bulk
                                                                       C6                   C18
                                       SWB_FB_P
                  GSI_n

 DIMM             CAMP                 VIN_Bulk
Connector

                                                                            C7               C19
                                                             L3
                  VOUT_1.0V
 C22        C16                            SWC

                                                                                 VDDQ_OUT
                                                      C9          C8                                       C25          C29
                                     SWC_BOOT

                                     SWC_FB_P

                                     SWC_FB_N
                  VBias
 C21        C13
                                        VIN_Bulk
                                                                         C10                 C20
                                                             L4

                                           SWD
                  AGND                                                           VPP_OUT
                                                       C12         C11                               C26          C30
                                     SWD_BOOT
                  PGND (2x)

                                      SWD_FB_P

                                   SWD_FB_N/PID
```

*Figure 10 — Single Phase Regulator Example Schematic* (figure; any text below/above was extracted from the drawing)

**Table 26 — PMIC Schematic Values**

```text
                     Dual Phase Regulator Mode                     Single Phase Regulator Mode
Component                                                                                                       Unit    Comment
                   Value         Physical Size/Rating             Value         Physical Size/Rating
     L1         0.47 - 0.68           4.0 x 4.0 x 2.0          0.47 - 0.68          4.0 x 4.0 x 2.0             μH
     L2         0.47 - 0.68           4.0 x 4.0 x 2.0          0.47 - 0.68          4.0 x 4.0 x 2.0             μH
     L3         0.47 - 0.68           4.0 x 4.0 x 2.0          0.47 - 0.68          4.0 x 4.0 x 2.0             μH
     L4          0.68 - 1.2           4.0 x 4.0 x 2.0           0.68 - 1.2          4.0 x 4.0 x 2.0             μH
     C1            2x; 22                  25V                    2x; 22                 25V                    μF
     C2             0.1                 16V; 0201                  0.1                16V; 0201                 μF
     C3            3x; 47               6.3V; 0805                3x; 47              6.3V; 0805                μF
     C4            3x; 47               6.3V; 0805                3x; 47              6.3V; 0805                μF
     C5             0.1                 16V; 0201                  0.1                16V; 0201                 μF
     C6            2x; 22                  25V                    2x; 22                 25V                    μF
     C7            2x; 22                  25V                    2x; 22                 25V                    μF
     C8            3x; 47               6.3V; 0805                3x; 47              6.3V; 0805                μF
     C9             0.1                 16V; 0201                  0.1                16V; 0201                 μF
     C10           2x; 22                  25V                    2x; 22                 25V                    μF
     C11           3x; 47               6.3V; 0805                3x; 47              6.3V; 0805                μF
     C12            0.1                 16V; 0201                  0.1                16V; 0201                 μF
     C13            4.7                 6.3V; 0402                 4.7                6.3V; 0402                μF

     C14            4.7                 6.3V; 0402                 4.7                6.3V; 0402                μF
     C15            4.7                 6.3V; 0402                 4.7                6.3V; 0402                μF

     C16            4.7                 6.3V; 0402                 4.7                6.3V; 0402                μF
     C17            0.1              25V, X6S; 0201                0.1             25V, X6S; 0201               μF

     C18            0.1              25V, X6S; 0201                0.1             25V, X6S; 0201               μF
     C19            0.1              25V, X6S; 0201                0.1             25V, X6S; 0201               μF
     C20            0.1              25V, X6S; 0201                0.1             25V, X6S; 0201               μF
     C21            0.1                 6.3V; 0201                 0.1                6.3V; 0201                μF
     C22            0.1                 6.3V; 0201                 0.1                6.3V; 0201                μF
     C23            0.1                 6.3V; 0201                 0.1                6.3V; 0201                μF
     C24            0.1                 6.3V; 0201                 0.1                6.3V; 0201                μF
     C25            175                    6.3V                    175                   6.3V                   μF
     C26            175                    6.3V                    175                   6.3V                   μF
                                                                                                                              1
     C27            350                    6.3V                    175                   6.3V                   μF
     C28            N/A                    N/A                     175                   6.3V                   μF
     C29            175                    6.3V                    175                   6.3V                   μF
     C30            175                    6.3V                    175                   6.3V                   μF
                                                                                                                              1
     C31            350                    6.3V                    175                   6.3V                   μF
     C32            N/A                                            175                   6.3V                   μF
NOTE 1 These capacitor values represent the distributed capacitance for the entire DIMM assuming max Itdc and Ipeakmax defined in
       Electrical characteristics for each SWx. For a given DIMM design, the distributed capacitance for each SWx varies and is a
       function of Itdc and Ipeakmax current requirement for that DIMM design. See actual DIMM design for total distributed
       capacitance.
```
