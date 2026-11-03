---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 8
title: Example Schematic
pages: 114-119
---
# 8 Example Schematic

Figure 30 shows an example schematic when PMIC is configured in one three phase regulator, one dual phase regulator and one single phase regulator mode configuration. Table 100 shows all component details shown in the schematics. Note that distributed capacitance across the entire DIMM module is not shown in the schematic.

```text
                                                  VIN_Bulk
                                                               P5030           VIN_Bulk
        C32        C31                                                                               C1          C2
                                       L6                                                       L1                                        VOUT_A

                                                  SWF                             SWA
              C36         C35   C34         C33                                           C3         C4               C5           C6
                                                  SWF_BOOT                   SWA_BOOT
                                                  SWF_FB                        SWA_FB
                                       L3
                                                                                                                                        VIN_Bulk
                                                                               VIN_Bulk
VOUT_CF                                                                                                                      C8
                                                                                                     C7
                                                  SWC
                                                                                                L2
              C30         C29   C28         C27
                                                  SWC_BOOT
                                                                                  SWB
                                                  SWC_FB                                  C9         C10           C11            C12
                                                                             SWB_BOOT
                                                  VIN_Bulk
        C26        C25                                                          SWB_FB
                                                  VOUT_1.8V
                                      C39   C40
_Bulk                                                                          VIN_Bulk

                                                                                                     C13                     C14
                                                                                                L5
                                                  VOUT_1.0V
                                      C41   C42
                                                                                  SWE

                                                                                          C15        C16           C17            C18
                                                  VBIAS1
                                            C44                              SWE_BOOT
                                      C43

                                                                                SWE_FB

                                                  VBIAS2
                                      C45   C46                                VIN_Bulk
                                                                                                     C19         C20
                                                                                                L4
                                                  Reset_n
                                                                                                                                        VOUT_D
                                                   SDA                            SWD
                          R1                       SCL                                    C21        C22           C23            C24
        VIN_Bulk                                  VR_OE                      SWD_BOOT
                                                  PID                           SWD_FB
                                                  CAMP                       VIN_Mgmt
                                                  GSI_n                                                    C37         C38
                                                                   RFU, PGND, AGND, GND
```

*Figure 30 — Three Phase+ Dual Phase + Single Phase (3-2-1) Regulator Example Schematic* (figure; any text below/above was extracted from the drawing)

**Table 100 — PMIC Schematic Values**

```text
 Remark       Component         Quantity         Value           Physical Size                Unit    Comment
  SWA             L1               1              0.47      4.3 mm x 4.3 mm x 2.0 mm          μH
  SWB             L2               1              0.47      4.3 mm x 4.3 mm x 2.0 mm          μH
  SWE             L3               1              0.47      4.3 mm x 4.3 mm x 2.0 mm          μH
  SWC             L4               1              0.47      4.3 mm x 4.3 mm x 2.0 mm          μH
  SWF             L5               1              0.47      4.3 mm x 4.3 mm x 2.0 mm          μH
  SWD             L6               1              1.0       4.3 mm x 4.3 mm x 2.0 mm          μH
  SWA            C1                1              0.1              0201; 25V                   μF
                C2[1]              2               22              0805; 25V                   μF        2x22
                 C3                1              0.1              0201; 25V                   μF
                 C4                1               47              0603; 6.3V                  μF
                 C5                1               47              0603; 6.3V                  μF
                C6[1]              2               47              0603; 6.3V                  μF        2x47
  SWB            C7                1              0.1              0201; 25V                   μF
                C8[1]              2               22              0805; 25V                   μF        2x22
                 C9                1              0.1              0201; 25V                   μF
                 C10               1               47              0603; 6.3V                  μF
                 C11               1               47              0603; 6.3V                  μF
                C12[1]             2               47              0603; 6.3V                  μF        2x47
  SWE            C13               1              0.1              0201; 25V                   μF
                C14[1]             2               22              0805; 25V                   μF        2x22
                 C15               1              0.1              0201; 25V                   μF
                 C16               1               47              0603; 6.3V                  μF
                 C17               1               47              0603; 6.3V                  μF
               C18[1],[2]          2               47              0603; 6.3V                  μF        2x47

  SWC            C25               1              0.1              0201; 25V                   μF
                C26[1]             2               22              0805; 25V                   μF        2x22
                 C27               1              0.1              0201; 25V                   μF

                 C28               1               47              0603; 6.3V                  μF
                 C29               1               47              0603; 6.3V                  μF
                C30[1]             2               47              0603; 6.3V                  μF        2x47

  SWF            C31               1              0.1              0201; 25V                   μF
                C32[1]             2               22              0805; 25V                   μF        2x22
                 C33               1              0.1              0201; 25V                   μF
                 C34               1               47              0603; 6.3V                  μF
                 C35               1               47              0603; 6.3V                  μF
                C36[1]             2               47              0603; 6.3V                  μF        2x47
  SWD            C19               1              0.1              0201; 25V                   μF
                C20[1]             2               22              0805; 25V                   μF        2x22
                 C21               1              0.1              0201; 25V                   μF
                 C22               1               47              0603; 6.3V                  μF
                 C23               1               47              0603; 6.3V                  μF
                 C24               1               47              0603; 6.3V                  μF
VIN_Mgmt         C37               1              0.1              0201; 6.3V                  μF
                 C38               1              4.7              0402; 6.3V                  μF
VOUT_1.8V        C39               1              0.1              0201; 6.3V                  μF
                 C40               1              4.7              0402; 6.3V                  μF
VOUT_1.0V        C41               1              0.1              0201; 6.3V                  μF
                 C42               1              4.7              0402; 6.3V                  μF
 VBIAS1          C43               1              0.1              0201; 6.3V                  μF
                 C44               1              4.7              0402; 6.3V                  μF
 VBIAS2          C45               1              0.1              0201; 6.3V                  μF
                 C46               1              4.7              0402; 6.3V                  μF
 VR_OE           R1                1              200                 0201                    KΩ
 NOTE 1     This represents physically two different capacitors. Each with value as shown in “Value” column.
 NOTE 2     For three phase DIMM design, due to component placement limitation of bulk output capacitance for
            SWE, some of the bulk output capacitance can be substituted with distributed capacitance to overcome
            the physical limitation of the PCB.
```

Figure 31 shows an example schematic when PMIC is configured as two dual phase regulators and one single phase regulator mode configuration. Table 100 shows all component details shown in the schematics. Note that distributed capacitance across the entire DIMM module is not shown in the schematic.

```text
                                                  VIN_Bulk
                                                              P5030           VIN_Bulk
        C32        C31                                                                                  C1          C2
                                       L6                                                        L1                                          VOUT_

                                                  SWF                            SWA
              C36         C35   C34         C33                                           C3            C4               C5           C6
                                                  SWF_BOOT                  SWA_BOOT
                                                  SWF_FB                       SWA_FB
                                       L3
                                                                                                                                           VIN_Bulk
                                                                              VIN_Bulk
VOUT_CF                                                                                                                         C8
                                                                                                        C7
                                                  SWC
                                                                                                 L2
              C30         C29   C28         C27
                                                  SWC_BOOT
                                                                                 SWB
                                                  SWC_FB                                  C9           C10            C11            C12
                                                                            SWB_BOOT
                                                  VIN_Bulk
        C26        C25                                                         SWB_FB
                                                  VOUT_1.8V
                                      C39   C40
_Bulk                                                                         VIN_Bulk
                                                                                                       C13                      C14
                                                  VOUT_1.0V
                                      C41   C42
                                                                                 SWE     Float

                                                  VBIAS1
                                            C44                             SWE_BOOT             Float (Do NOT connect to GND)
                                      C43
                                                                               SWE_FB

                                                  VBIAS2
                                      C45   C46                               VIN_Bulk
                                                                                                        C19         C20

                                                                                                 L4
                                                  Reset_n
                                                                                                                                           VOUT_D
                                                   SDA                           SWD
                          R1                       SCL                                    C21          C22            C23            C24
        VIN_Bulk                                  VR_OE                     SWD_BOOT
                                                  PID                          SWD_FB
                                                  CAMP                      VIN_Mgmt
                                                  GSI_n                                                       C37         C38
                                                                  RFU, PGND, AGND, GND
```

*Figure 31 — Dual Phase + Dual Phase + Single Phase (2-2-1) Regulator Example Schematic* (figure; any text below/above was extracted from the drawing)

Figure 32 shows an example schematic when PMIC is configured as one dual phase regulator and two single phase regulators mode configuration. Table 100 shows all component details shown in the schematics. Note that distributed capacitance across the entire DIMM module is not shown in the schematic.

```text
                                                                  VIN_Bulk
                                                                               P5030           VIN_Bulk
         C32        C31                                                                                                  C1          C2
                                                                                                                  L1                                          VOUT_

                                                          Float   SWF                             SWA
                                                                                                           C3            C4               C5           C6
                          Float (Do NOT connect to GND)           SWF_BOOT                   SWA_BOOT
                                                                  SWF_FB                        SWA_FB
                                                    L3
                                                                                                                                                            VIN_Bulk
                                                                                               VIN_Bulk
VOUT_C                                                                                                                                           C8
                                                                                                                         C7
                                                                  SWC
                                                                                                                  L2
               C30              C29         C28            C27
                                                                  SWC_BOOT
                                                                                                  SWB
                                                                  SWC_FB                                   C9            C10           C11            C12
                                                                                             SWB_BOOT
                                                                  VIN_Bulk
         C26        C25                                                                         SWB_FB
                                                                  VOUT_1.8V
                                                  C39       C40
_Bulk                                                                                          VIN_Bulk
                                                                                  ng                                     C13                     C14
                                                                  VOUT_1.0V
                                                  C41       C42
                                                                                                  SWE     Float

                                                                  VBIAS1
                                                            C44                              SWE_BOOT             Float (Do NOT connect to GND)
                                                  C43
                                                                                                SWE_FB

                                                                  VBIAS2
                                                  C45       C46                                VIN_Bulk
                                                                                                                                     C20

                                                                                                                         C19
                                                                                                                  L4
                                                                  Reset_n
                                                                                                                                                            VOUT_D
                                                                   SDA                            SWD
                                R1                                 SCL                                    C21            C22           C23            C24
         VIN_Bulk                                                 VR_OE                      SWD_BOOT
                                                                  PID                           SWD_FB
                                                                  CAMP
                                                                                             VIN_Mgmt
                                                                  GSI_n                                                        C37         C38
                                                                                   RFU, PGND, AGND, GND
```

*Figure 32 — Dual Phase + Single Phase + Single Phase (2-1-1) Regulator Example Schematic* (figure; any text below/above was extracted from the drawing)

Figure 33 shows an example schematic when PMIC is configured as four single phase regulators configuration. Table 100 shows all component details shown in the schematics. Note that distributed capacitance across the entire DIMM module is not shown in the schematic.

```text
                                                                 VIN_Bulk
                                                                             P5030           VIN_Bulk
        C32        C31                                                                                                C1          C2
                                                                                                                L1

                                                                                                                                                            VOUT_
                                                         Float   SWF                            SWA
                                                                                                         C3           C4               C5           C6
                         Float (Do NOT connect to GND)           SWF_BOOT                  SWA_BOOT
                                                                 SWF_FB                       SWA_FB
                                                L3
                                                                                                                                                         VIN_Bulk
                                                                                             VIN_Bulk
VOUT_C                                                                                                                                        C8
                                                                                                                      C7
                                                                 SWC
                                                                                                                L2
              C30            C29        C28              C27
                                                                 SWC_BOOT                                                                                 VOUT_B
                                                                                                SWB
                                                                 SWC_FB                                  C9           C10           C11            C12
                                                                                           SWB_BOOT
                                                                 VIN_Bulk
        C26        C25                                                                        SWB_FB
                                                                 VOUT_1.8V
                                               C39       C40
_Bulk                                                                                        VIN_Bulk
                                                                                ng                                    C13                     C14
                                                                 VOUT_1.0V
                                               C41       C42
                                                                                                SWE     Float

                                                                 VBIAS1
                                                         C44                               SWE_BOOT             Float (Do NOT connect to GND)
                                               C43
                                                                                              SWE_FB

                                                                 VBIAS2
                                               C45       C46                                 VIN_Bulk
                                                                                                                      C19         C20

                                                                                                                L4
                                                                 Reset_n
                                                                                                                                                         VOUT_D
                                                                  SDA                           SWD
                             R1                                   SCL                                    C21          C22           C23            C24
        VIN_Bulk                                                 VR_OE                     SWD_BOOT
                                                                 PID                          SWD_FB
                                                                 CAMP                      VIN_Mgmt
                                                                 GSI_n                                                      C37         C38
                                                                                 RFU, PGND, AGND, GND
```

*Figure 33 — Single Phase + Single Phase + Single Phase + Single Phase (1-1-1-1) Regulator* (figure; any text below/above was extracted from the drawing)

```text
Example Schematic
```
