---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 4
title: Package Pinout and Pin Description
pages: 4-9
---
# 4 Package Pinout and Pin Description



## 4.1 Device Package Pinout

The PMIC5030 device is a 113 ball Flip Chip Fine Pitch BGA (FCBGA) with 11 x 13 ball grid, 0.5mm and 0.7mm ball pitch in x and y direction respectively. The package size is 5.55 mm x 9.0 mm nominal (5.6 mm x 9.05 mm maximum) as defined in MO-360, Terminal Pattern A. The ball diameter is 0.30 mm nominal; 0.25 mm minimum, 0.35 mm maximum.

## 4.2 Package Pinout

The PMIC pinout is shown in Table 2 for Bottom view. Pin A1 is bottom left in Table 2. Table 3 shows the PMIC pinout for Top view. Ball pitch: 0.5 mm x 0.7 mm (x and y dimensions, respectively); Ball size (0.3 mm), SMD Pad SRO (0.275 mm); Package z-height 0.9 mm nominal (1.0 mm maximum).

**Table 2 — Ball Assignment - 113 Ball FCBGA, 11 x 13 Grid, Bottom View**

```text
        1       2        3        4        5        6        7         8        9       10        11
N     PGND/    PGND   PGND     VOUT_    VOUT_     AGND     VIN_     Reset_   PGND      PGND     PGND/      N
       NC                       1.0V     1.8V              Mgmt       n                          NC
M     SWA      SWA    PGND      PGND    SWA_F     CAMP     SWC_     PGND     PGND      SWC      SWC        M
                                          B                 FB

L     SWA      SWA     SWA      PGND                                PGND      SWC      SWC      SWC        L
K     SWA_     VIN_    VIN_                                                   VIN_     VIN_     SWC_       K

      BOOT     Bulk    Bulk                                                   Bulk     Bulk     BOOT
J     SWB_     VIN_    VIN_                       GSI_n                       VIN_     VIN_     SWF_       J

      BOOT     Bulk    Bulk                                                   Bulk     Bulk     BOOT
H     SWB      SWB     SWB      PGND     SWB_     AGND     SWF_     PGND      SWF      SWF      SWF        H
                                          FB                FB
G     SWB      SWB    PGND      PGND              AGND              PGND     PGND      SWF      SWF        G
F     PGND     PGND   PGND               RFU2              RFU1              PGND      PGND     PGND       F
E     PGND                               SWE_     AGND     SWD_                                 PGND       E
                                          FB                FB
D     SWE_     VIN_    VIN_                       AGND                        VIN_     VIN_     SWD_       D
      BOOT     Bulk    Bulk                                                   Bulk     Bulk     BOOT
C     SWE      SWE     SWE      PGND                                PGND      SWD      SWD      SWD        C
B     SWE      SWE    PGND      PGND     RFU3      SDA      SCL     PGND     PGND      SWD      SWD        B
A     PGND/    PGND   PGND     VR_OE     VBIAS    RFU4     VBIAS     PID     PGND      PGND     PGND/      A
       NC                                  1                 2                                   NC
        1       2        3        4        5        6        7         8        9       10        11
```

**Table 3 — Ball Assignment - 113 Ball FCBGA, 11 x 13 Grid, Top View**

```text
       11      10      9       8        7       6       5        4        3          2     1
N     PGND/   PGND   PGND    Reset_   VIN_    AGND    VOUT_   VOUT_     PGND    PGND     PGND/   N
       NC                      n      Mgmt             1.8V    1.0                        NC
M     SWC     SWC    PGND    PGND     SWC_    CAMP    SWA_     PGND     PGND    SWA      SWA     M
                                       FB              FB
L     SWC     SWC    SWC     PGND                              PGND      SWA    SWA      SWA     L
K     SWC_    VIN_   VIN_                                                VIN_   VIN_     SWA_    K
      BOOT    Bulk   Bulk                                                Bulk   Bulk     BOOT
J     SWF_    VIN_   VIN_                     GSI_n                      VIN_   VIN_     SWB_    J
      BOOT    Bulk   Bulk                                                Bulk   Bulk     BOOT
H     SWF     SWF    SWF     PGND     SWF_    AGND    SWB_     PGND      SWB    SWB      SWB     H
                                       FB              FB
G     SWF     SWF    PGND    PGND             AGND             PGND     PGND    SWB      SWB     G
F     PGND    PGND   PGND             RFU1             RFU2             PGND    PGND     PGND    F
E     PGND                            SWD_    AGND    SWE_                               PGND    E
                                       FB              FB
D     SWD_    VIN_   VIN_                     AGND                       VIN_   VIN_     SWE_    D
      BOOT    Bulk   Bulk                                                Bulk   Bulk     BOOT
C     SWD     SWD    SWD     PGND                              PGND      SWE    SWE      SWE     C
B     SWD     SWD    PGND    PGND     SCL      SDA     RFU3    PGND     PGND    SWE      SWE     B

A     PGND/   PGND   PGND     PID     VBIAS   RFU4    VBIAS   VR_OE     PGND    PGND     PGND/   A
       NC                               2               1                                 NC

       11      10      9       8        7       6       5        4        3          2     1

                                                   5.55

                              1   2    3   4   5    6     7   8   9   10   11

                        N
                                                                                0.7 mm
                        M

                        L

                        K

                        J

                        H
                9.0mm

                        G

                        F

                        E

                        D

                        C
                        B

                        A

                              0.5 mm
```

*Figure 1 — Mechanical View - Bottom View* (figure; any text below/above was extracted from the drawing)

## 4.3 PMIC5030 Package Pin List

**Table 4 — PMIC5030 Pin Description**

```text
   Pin Name         Type                                            Description
VIN_Bulk (12x)   I, PWR
                      12 V power input supply pin to the PMIC. All twelve VIN_Bulk input pins must be connected to the 12V
                      input supply even if one or more output regulators are not intended to be used.
VIN_Mgmt       I, PWR 3.3 V power input supply pin to the PMIC for VOUT_1.8V & VOUT_1.0V LDO outputs, sideband
                      management access and internal PMIC operation. Vendor usage of 3.3V input supply may vary.
```

VBIAS1, VBIAS2 O, PWR Vbias LDO output voltage generated by PMIC.

```text
                           PMIC vendors may choose to implement either one LDO output voltage regulator or two LDO output
                           voltage regulators based on their design.
                           If only one LDO output voltage regulator is used, the PMIC may internally tie VBIAS1 and VBIAS2 pin
                           together or may use only VBIAS1 pin and ignore VBIAS2 pin.
                           If two LDO output voltage regulators are used, the PMIC internally keeps VBIAS1 and VBIAS2 separate.
                           However, there is only one common status register, threshold configuration register, clear and mask
                           register for VBIAS. The ADC read out for both VBIAS1 and VBIAS2 LDO regulator is allowed.
                           On DIMM PCB or any other application PCB, VBIAS1 and VBIAS2 pins are treated independently and
                           each pin has its own de-coupling capacitors.
CAMP             IO        Control and Monitor Port.
                           Open Drain Output: The PMIC floats this pin high when VIN_Bulk input supply, all enabled output buck
                           regulators and all LDO regulator tolerance threshold is maintained as configured in the appropriate
                           register. The PMIC drives this pin low when VIN_Bulk input goes below the threshold or when any of the
                           enabled output buck regulator exceeds the threshold configured in the appropriate register or any LDO
                           output regulator exceeds the threshold configured in the appropriate register.
                           Input: The PMIC disables its output regulators when this pin transitions from high to low. The LDO

                           outputs shall remain on.
                           Input: The PMIC enters write-protect mode when the PMIC floats the CAMP output and it is pulled up

                           High by external pullup resistor. The PMIC exits write-protect mode and enters in configuration mode
                           when CAMP input is driven low to the PMIC externally.
SCL              I         I2C/I3C Basic Clock input for management bus.

SDA              IO        I2C/I3C Basic Data Input/Output for management bus.
SWA              O         Output switch node A buck regulator. This pin connects to L1 power inductor.
                           In single phase regulator mode, the SWA output must not be connected to either SWB or SWC or SWE
                           or SWF output even if they are configured as same exact output voltage.
                           In dual phase regulator mode, the SWA+SWB output must not be connected to either SWC or SWE
                           output or SWC+SWF output even if they are configured as same exact output voltage.
                           In three phase regulator mode, the SWA+SWB+SWE output must not be connected to either SWC or
                           SWE or SWC+SWF output even if they are configured as same exact output voltage.
SWA_BOOT         PWR       Bootstrap node for SWA high side NMOS driver. This pin connects to SWA through a high quality
                           capacitor.
SWA_FB           I         This pin connects to DIMM power plane load.
SWB              O         Output switch node B buck regulator. This pin connects to L2 power inductor.
                           In single phase regulator mode, the SWB output must not be connected to either SWA or SWC or SWE
                           or SWF output even if they are configured as same exact output voltage.
                           In dual phase regulator mode, the SWA+SWB output must not be connected to either SWC or SWE
                           output or SWC+SWF output even if they are configured as same exact output voltage.
                           In three phase regulator mode, the SWA+SWB+SWE output must not be connected to either SWC or
                           SWF or SWC+SWF output even if they are configured as same exact output voltage.
SWB_BOOT         PWR       Bootstrap node for SWB high side NMOS driver. This pin connects to SWB through a high quality
                           capacitor.
SWB_FB           I         In single phase regulator mode, this pin connects to DIMM power plane load. In dual phase or three
                           phase regulator mode, this pin must be connected to GND.

  Pin Name       Type                                                Description
SWC          O          Output switch node C buck regulator. This pin connects to L3 power inductor.
                        In single phase regulator mode, the SWC output must not be connected to either SWA or SWB or SWE
                        or SWF or SWA+SWB output even if they are configured as same exact output voltage.
                        In dual phase regulator mode, the SWC+SWF output must not be connected to either SWA or SWB or
                        SWA+SWB or SWA+SWB+SWE output even if they are configured as same exact output voltage
SWC_BOOT     PWR        Bootstrap node for SWC high NMOS driver. This pin connects to SWC through a high quality capacitor.
SWC_FB       I          This pin connects to DIMM power plane load.
SWD          O          Output switch node D buck regulator. This pin connects to L4 power inductor.
SWD_BOOT     PWR        Bootstrap node for SWD high side NMOS driver. This pin connects to SWD through a high quality
                        capacitor.
SWD_FB       I          This pin connects to DIMM power plane load.
SWE          O          Output switch node E buck regulator. This pin connects to L5 power inductor.
                        In single phase regulator mode, the SWE output must not be connected to either SWA or SWB or SWC
                        or SWF or SWA+SWB or SWC+SWF output even if they are configured as same exact output voltage.
                        In three phase regulator mode, the SWA+SWB+SWE output must not be connected to either SWC or
                        SWE or SWC+SWF output even if they are configured as same exact output voltage.
SWE_BOOT     PWR        Bootstrap node for SWE high side NMOS driver. This pin connects to SWE through a high quality
                        capacitor.
SWE_FB       I          In single phase regulator mode, this pin connects to DIMM power plane load. In three phase regulator
                        mode, this pin must be connected to GND.
SWF          O          Output switch node F buck regulator. This pin connects to L6 power inductor.
                        In single phase regulator mode, the SWF output must not be connected to either SWA or SWB or SWE
                        or SWC or SWA+SWB or SWA+SWB+SWE output even if they are configured as same exact output
                        voltage.
                        In dual phase regulator mode, the SWC+SWF output must not be connected to either SWA or SWB or
                        SWA+SWB or SWA+SWB+SWE output even if they are configured as same exact output voltage

SWF_BOOT     PWR        Bootstrap node for SWB high side NMOS driver. This pin connects to SWF through a high quality
                        capacitor.
SWF_FB       I          In single phase regulator mode, this pin connects to DIMM power plane load. In dual phase regulator

                        mode, this pin must be connected to GND.
PID          I          PMIC ID pin for I2C and I3C Basic bus. See Table 34 for ID definition.

VOUT_1.8V    O          1.8V LDO Output.
VOUT_1.0V    O          1.0 V LDO Output.
AGND (5x)    PWR        Analog Ground. Connects to DIMM ground plane.
PGND (38x)   PWR        Power Ground. Connects to DIMM ground plane.
VR_OE        I          PMIC Output Enable.
                        If VR_OE pin function is disabled, this pin shall be pulled high through 200 KΩ resistor to VIN_Bulk on
                        PCB. The PMIC does not turn on the regulators when this pin is high but does turn off the regulator if
                        this pin is low.
                        If VR_OE pin function is enabled, when this pin is high, the PMIC turns on the regulator and when this
                        pin is low, the PMIC turns off the regulator. See clause 6.6 and 6.7 for details.
                        This pin shall not be left floating. For typical DIMM application, this pin is always connected to VIN_Bulk
                        through 200 KΩ on DIMM PCB.
Reset_n      I          Default Reset_n function - Active Low asynchronous reset input. CMOS input. When Low, it causes a
                        reset to PMIC I2C, I3C interface.
GSI_n        O          General Status Interrupt - Open Drain Output.
                        The PMIC asserts this pin low to communicate any one or more events to host. This pin stays asserted
                        until the appropriate registers are explicitly cleared.
RFU[1:4]                These pins must be connected to GND.
```
