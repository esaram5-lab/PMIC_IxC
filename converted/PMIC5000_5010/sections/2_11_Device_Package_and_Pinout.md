---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 2.11
title: Device Package and Pinout
pages: 91-99
---
# 2.11 Device Package and Pinout

The PMIC device is packaged in 5 mm x 5 mm FCQFN.

## 2.11.1 Package Pinout

The PMIC pinout is shown in Figure 26 and Figure 27 for TOP view and BOTTOM view, respectively.

```text
                              SWAB_FB_N

                                          SWAB_FB_P

                                                                       SWC_FB_N
                                                        SWC_FB_P
                     CAMP

                                                                                  GSI_n

                                                                                                              RFU2
                                                                                          SDA

                                                                                                 SCL
             NC

                                                                                                                         NC
                                                         32

                                                                       31

                                                                                  30

                                                                                          29

                                                                                                  28

                                                                                                              27

                                                                                                                         26
                     35

                              34

                                          33
              1

SWA_BOOT      2                                                                                                          25   SWC_BOOT

    VIN_Bulk 3                                                                                                           24 VIN_Bulk

        SWA 4                                                                                                            23   SWC
                                                                 Top View
     PGND     5                                                                                                               PGND

      SWB     6                                         DDR5 PMIC                                                        22   SWD
                                                       5 mm x 5 mm

    VIN_Bulk 7                                                                                                           21 VIN_Bulk
                                                          FCQFN

SWB_BOOT      8                                                                                                          20 SWD_BOOT
                     10

                              11

                                          12

                                                         13

                                                                       14

                                                                                  15

                                                                                          16

                                                                                                 17

                                                                                                             18

                                                                                                                         19
              9

                                                                                                 VOUT_1.8V
                                                        SWD_FB_N/PID

                                                                                                             VOUT_1.0V
                                                                       SWD_FB_P
                              SWB_FB_P
              NC

                                                                                                                         NC
                                                                                  Vbias
                                          VIN_Mgmt

                                                                                          AGND
                     RFU1
```

*Figure 26 — PMIC Pinout - TOP View* (figure; any text below/above was extracted from the drawing)

```text
                                                                                               SWAB_FB_N
                                                                                   SWAB_FB_P
                                                                    SWC_FB_P
                                                         SWC_FB_N

                                                                                                           CAMP
                                                 GSI_n
                  RFU2

                                         SDA
                              SCL
           NC

                                                                                                                  NC
            26

                 27

                             28

                                         29

                                                 30

                                                         31

                                                                    32

                                                                                   33

                                                                                               34

                                                                                                           35

                                                                                                                  1
SWC_BOOT   25                                                                                                      2   SWA_BOOT

   VIN_Bulk 24                                                                                                     3 VIN_Bulk

      SWC 23                                                                                                       4   SWA
                                                Bottom View
    PGND                                                                                                           5   PGND

     SWD   22                                    DDR5 PMIC                                                         6   SWB
                                                5 mm x 5 mm
   VIN_Bulk 21                                     FCQFN                                                           7 VIN_Bulk
SWD_BOOT   20                                                                                                      8 SWB_BOOT
                 18

                             17

                                         16

                                                 15

                                                         14

                                                                    13

                                                                                   12
            19

                                                                                               11

                                                                                                           10

                                                                                                                  9
                                                                    SWD_FB_N/PID

                                                                                               SWB_FB_P
                                                         SWD_FB_P
            NC

                 VOUT_1.0V

                                                                                                                  NC
                                                                                   VIN_Mgmt
                             VOUT_1.8V

                                         AGND

                                                 Vbias

                                                                                                           RFU1
```

*Figure 27 — PMIC Pinout - BOTTOM View* (figure; any text below/above was extracted from the drawing)

## 2.11.2 PMIC Package Pin List

.

**Table 86 — PMIC Pin Description**

```text
      Pin Name       Type                                        Description
    VIN_Bulk (4x)    I   12 V power input supply pin to the PMIC. All four VIN_Bulk input pins must be
                         connected to the 12V input supply even if one or more output regulators are not intended
                         to be used.
    VIN_Mgmt         I   3.3 V power input supply pin to the PMIC for VOUT_1.8V and VOUT_1.0V LDO
                         output, side band management access, internal memory read operation. Vendor usage of
                         3.3V input supply may vary.
    CAMP             IO  Control and Monitor Port. Open drain output. The PMIC floats this pin when VIN_Bulk
                         input supply, as well as all enabled output buck regulators and all LDO regulators
                         tolerance threshold is maintained as configured in the appropriate register. The PMIC
                         drives this pin low when VIN_Bulk input goes below the threshold or when any of the
                         enabled output buck regulator exceeds the thresholds configured in the appropriate
                         register or when any LDO output regulator exceeds the threshold configured in the
                         appropriate register.
                         Input: The PMIC disables its output regulator when this pin transitions from high to low.
                         The LDO outputs shall remain on.
                         Input: The PMIC enters write protect mode when it is high and configuration mode when
                         it is low.
    GSI_n            O   General Status Interrupt. Open drain output. The PMIC asserts this pin low to
                         communicate any one or more critical event to host. This pin stays asserted until the

                         appropriate registers are explicitly cleared.
    VBias            PWR Vbias Voltage generated by PMIC.

    SCL              I   I2C/I3C Basic Clock Input for management bus.

    SDA              IO  I2C/I3C Basic Data Input/Output for management bus.
    SWA              O   Output switch node A buck regulator. This pin connects to L1 power inductor.
                         In single phase regulator mode of operation, the SWA output must not be connected to
                         either SWB or SWC output even if they are configured as same exact output voltage.
    SWA_BOOT         PWR Bootstrap node for SWA high side NMOS driver. This pin connects to SWA through a
                         high quality capacitor.
    SWAB_FB_P        I   In single phase regulator mode or dual phase regulator mode of operation, this pin
                         connects to DIMM power plane load.
    SWAB_FB_N        I   In single phase regulator mode or dual phase regulator mode of operation, this pin
                         connects to DIMM ground plane.
    SWB              O   Output switch node B buck regulator. This pin connects to L2 power inductor.
                         In single phase regulator mode of operation, the SWB output must not be connected to
                         either SWA or SWC output even if they are configured as same exact output voltage.
    SWB_BOOT         PWR Bootstrap node for SWB high side NMOS driver. This pin connects to SWB through a
                         high quality capacitor.
    SWB_FB_P         I   In single phase regulator mode of operation, this pin connects to DIMM power plane load.
                         If not used, this pin must be connected to GND.
                         In dual phase regulator mode of operation, this pin must be connected to GND.
    SWC              O   Output switch node C buck regulator. This pin connects to L3 power inductor. The output
                         of SWC must not be connected to the output of either SWA or SWB or SWA+SWB even
                         if they are configured as same exact output voltage.

   Pin Name    Type                                     Description
SWC_BOOT       PWR Bootstrap node for SWC high NMOS driver. This pin connects to SWC through a high
                   quality capacitor.
SWC_FB_P       I   This pin connects to DIMM power plane load.
SWC_FB_N       I   This pin connects to DIMM ground plane.
SWD            O   Output switch node D buck regulator. This pin connects to L4 power inductor.
SWD_BOOT       PWR Bootstrap node for SWD high side NMOS driver. This pin connects to SWD through a
                   high quality capacitor.
SWD_FB_P       I   This pin connects to DIMM power plane load.
SWD_FB_N/      I   This pin connects to DIMM ground plane when PMIC is used in differential remote
PID                sensing mode of operation.
                   This pin connects to DIMM ground plane or VOUT_1.8V rail or left floating when PMIC
                   is used in a single ended remote sensing mode of operation.
VOUT_1.8V      O   1.8V LDO Output.
VOUT_1.0V      O   1.0 V LDO Output.
AGND           PWR Analog Ground. Connects to DIMM ground plane.
PGND           PWR Power Ground. Connects to DIMM ground plane.
RFU1, RFU2         This pins must be connected to GND.
NC                 No Connect. This pin is not connected internally in the package to the die. Typical
                   application connects this pin to GND on PCB for better thermal performance.
```

## 2.11.3 Package Mechanical Drawing

*Figure 28 — Package Mechanical Outline* (figure; any text below/above was extracted from the drawing)

*Figure 29 — Detail A Drawing* (figure; any text below/above was extracted from the drawing)

*Figure 30 — Detail B Drawing* (figure; any text below/above was extracted from the drawing)

*Figure 31 — Reference PCB Land Pattern* (figure; any text below/above was extracted from the drawing)
