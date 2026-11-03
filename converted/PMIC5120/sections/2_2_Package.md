---
document: JESD301-6 (PMIC5120 Power Management IC Standard, Version 1.0, February 2025)
device: PMIC5120
application: client
section: 2.2
title: Package
pages: 4-10
---
# 2.2 Package



## 2.2.1 Flip Chip QFN Package (3 mm x 4 mm)

```text
• 28 pins (24 Functional pins; 4 dummy corner pins)

• 3 mm x 4 mm Maximum Package Outline
```

## 2.2.2 Mechanical Drawing

The drawing and dimensions for 28 pins FC QFN package are shown below as reference only. This package is defined in JEDEC standard MO-339A.

```text
                      TERMINAL CORNER                                                                                            3.00                                                                          B
                  3
                      INDEX AREA
                                                                                         1.25

                                                                                                                                                                                                                   0.1 °C

                                                       1.25

                                                                                                                         (DATUM A)
                                               4.00

                                                                                                                                                                                        (DATUM B)
                                                A
                                                                                                         TOP VIEW
                                                                           (0.20)

                                                                                             (0.60)

                                                                                                               (1.00)

                                                                                                                                 (1.40)

                                                                                                                                                   (1.80)

                                                                                                                                                                     (2.20)

                                                                                                                                                                                       (2.60)

                                                                                                                                                                                                     (3.00)
                                                                  (0.00)

                                                                                    (0.40)

                                                                                                      (0.80)

                                                                                                                        (1.20)

                                                                                                                                          (1.60)

                                                                                                                                                            (2.00)

                                                                                                                                                                              (2.40)

                                                                                                                                                                                            (2.80)
                  6

              0.80 MAX                                                         9                                                                                                         15
                                     (4.00)
                                              (3.80)          9                                                                                                                                           15
                                     (3.65)
                                              (3.45)
                                     (3.25)
                                              (3.05)
                                     (2.85)
                                              (2.65)
                                     (3.25)
                                              (3.45)

                                     (1.75)
                                              (1.55)
                  DETAIL A           (1.35)
                                              (1.15)
                                     (0.95)
                                              (0.75)
                                     (0.55)
                                              (0.35)
                                                              1                                                                                                                                           23
                                     (0.20)
                                              (0.00)
                                                                                1                                                                                                        23

SIDE VIEW                         DETAIL B                                                   BOTTOM VIEW
```

*Figure 1 — QFN Package Mechanical Drawing* (figure; any text below/above was extracted from the drawing)

```text
                         4X 0.40±0.05
                         4X 0.20±0.05

         4X 0.20±0.05
4X 0.35±0.05

                 4X 0.40±0.10

                                                                       2X 1.20 ± 0.10
                                                                      2X0.50 ± 0.10
                                                                       0.1 °C B A
                                                                                          4
                          8X0.20±0.05
                                                                       0.05 C
                            0.1 °C B A
                 4
                            0.05 C
                                                                            4X 0.55
                            4X0.20±0.05                               4X 0.40

                     4        0.1 °C B A
                              0.05 C
                                                                      4X 0.40

                                                      C0.125 x 0.125 MAX

               4X 0.65
                                                                  10X 0.40 ± 0.10

                         4X 0.20 MIN
                                                                 10X 0.20±0.05
                                 4X 0.70                            0.07 C A B
                                                                                      4
                                                                    0.05 C

                                                                 10X 0.40

                                            DETAIL B
```

*Figure 2 — QFN Package Mechanical Drawing - Detail Dimensions* (figure; any text below/above was extracted from the drawing)

```text
                   DETAIL C
                                                                                                     0.20
            4X 0.25                                                    0.20

                                                                                            1.72
      4X 0.20
                                                                                            1.35

                                                                                            0.95

                                                                                            0.55

        2X 0.50                                                                             0.00

                                                                                            0.55

                                                                                            0.95

                                                                                            1.35

                                                                                            1.72

C0.125 X 0.125
                                                                     ng                            PKG BOUNDARY
                        1.20

                                 0.80

                                        0.40

                                                  0.00

                                                           0.40

                                                                    0.80

                                                                           1.20

                                               4X 0.625
                               10X 0.25

            10X 0.625                                                                4X 0.575

                                                                                     4X 0.25

                                                                                  8X 0.25

                                                          8X 1.125
                                                         2X 1.400

                                               DETAIL C
```

*Figure 3 — Recommended PCB Pattern (Units: mm)* (figure; any text below/above was extracted from the drawing)

## 2.2.3 Pinout (FC QFN Package - 28 Pins)

```text
                                         3mm

                                           PWR_GOOD
                             SWA_FB_P

                                                      SWC_FB_P
                     VR_EN

                                                                 GSI_n
             1                                                               23 TC/GND
                     28

                             27

                                           26

                                                      25

                                                                 24
   TC/GND

BOOT_SWA     2                                                               22   BOOT_SWC

VIN_Bulk_A       3                                                     21         VIN_Bulk_C

     SWA         4                                                     20         SWC

                                                                                               4mm
    PGND         5                      Top View      ng               19         PGND

      SWB        6                                                     18         SCL

VIN_Bulk_B       7                                                     17         SDA

BOOT_SWB     8                                                               16   VOUT_1.0V
                     10

                             11

                                           12

                                                      13

                                                                 14

   TC/GND    9                                                               15 TC/GND
                                                      AGND
                                           VIN
                             SWB_FB_P

                                                                 VOUT_1.8V
                     PID
```

*Figure 4 — FC QFN Package Pinout - 28 Pins; Top View* (figure; any text below/above was extracted from the drawing)

```text
                                          3mm

                                           PWR_GOOD
                               SWC_FB_P

                                                      SWA_FB_P

                                                                 VR_EN
             23    GSI_N
                   24

                               25

                                           26

                                                      27

                                                                 28
   TC/GND                                                                    1   TC/GND

BOOT_SWC     22                                                              2   BOOT_SWA

VIN_Bulk_C        21                                                     3       VIN_Bulk_A

      SWC         20                                                     4       SWA

                                                                                              4mm
    PGND          19              Bottom View
                                                      ng                 5       PGND

       SCL        18                                                     6       SWB

      SDA         17                                                     7       VIN_Bulk_B

VOUT_1.0V    16                                                              8   BOOT_SWB
                                           12
                   14

                               13

                                                      11

                                                                 10

   TC/GND    15                                                              9   TC/GND
                                                      SWB_FB_P
                               AGND

                                           VIN
                   VOUT_1.8V

                                                                 PID
```

*Figure 5 — FC QFN Package Pinout - 28 Pins; Bottom View* (figure; any text below/above was extracted from the drawing)
