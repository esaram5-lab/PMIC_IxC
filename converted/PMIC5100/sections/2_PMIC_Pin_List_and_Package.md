---
document: JESD301-2 (PMIC5100 Power Management IC Standard, Rev. 1.03, October 2022)
device: PMIC5100
application: client
section: 2
title: PMIC Pin List and Package
pages: 3-9
---
# 2 PMIC Pin List and Package



## 2.1 Pin List

**Table 1 — PMIC Pin Description**

```text
Pin Count    Pin Name    Type                                            Description
            VIN_Bulk_A          5 V power input supply to the PMIC for SWA, SWB and SWC respectively. All three
    3       VIN_Bulk_B    I     VIN_Bulk input pins must be connected to the 5 V input supply even if one or more
            VIN_Bulk_C          output regulators are not intended to be used.
    1          VIN        I     5 V power input supply to the PMIC for analog circuits.
    2         PGND       PWR    Power Ground. Connects to DIMM ground plane.
    1         AGND       PWR    Analog Ground. Connects to DIMM ground plane.
                                Switch node A output buck regulator. This pin connects to L1 power inductor.
                                In single phase regulator mode of operation, the SWA output must not be connected to
    1          SWA        O
                                SWB output even if they are configured to same exact output voltage.
                                In dual phase regulator mode of operation, the SWA and SWB outputs are connected.
                                Switch node B output buck regulator. This pin connects to L2 power inductor.
                                In single phase regulator mode of operation, the SWA output must not be connected to
    1          SWB        O
                                either SWB output even if they are configured to same exact output voltage.
                                In dual phase regulator mode of operation, the SWA and SWB outputs are connected.
    1          SWC        O     Switch node C output buck regulator. This pin connects to L3 power inductor.
                                Bootstrap node for SWA high side NMOS driver. This pin connects to SWA through a
    1        BOOT_SWA    PWR
                                high quality capacitor.
                                Bootstrap node for SWB high side NMOS driver. This pin connects to SWB through a
    1       BOOT_SWB     PWR
                                high quality capacitor.

                                Bootstrap node for SWC high side NMOS driver. This pin connects to SWC through a
    1       BOOT_SWC     PWR
                                high quality capacitor.
                                Switch node A output buck regulator positive feedback. In single phase or dual phase

    1        SWA_FB_P     I
                                regulator mode of operation, this pin connects to DIMM power plane load.
                                Switch node B output buck regulator positive feedback. In single phase regulator mode of

    1        SWB_FB_P     I     operation, this pin connects to DIMM power plane load. In dual phase regulator mode of
                                operation, this pin is connected to GND.
                                Switch node C output buck regulator positive feedback. This pin connects to DIMM
    1        SWC_FB_P     I
                                power plane load.
    1        VOUT_1.8V    O     1.8V LDO Output.
    1        VOUT_1.0V    O     1.0V LDO Output
                                Power good indicator. Open Drain output. The PMIC floats this pin high when VIN_Bulk
                                input supply as well as all enabled output buck regulators and all LDO regulator tolerance
                                threshold is maintained as configured in appropriate register. The PMIC drives this pin
                                low when VIN_Bulk input goes below the threshold or when any of the enabled switch
    1       PWR_GOOD      IO
                                output regulators exceeds the threshold configured in the appropriate register or any LDO
                                output regulator exceeds the threshold tolerance.
                                Input: The PMIC disables its output regulators when this pin transitions from high to low.
                                The LDO outputs shall remain on.
                                PMIC Enable. When this pin is high, the PMIC turns on the regulator. When this pin is
    1         VR_EN       I     low, the PMIC turns off the regulator. This pin shall not be left floating. If it is not used, it
                                shall be tied to GND.
    1          SCL         I    Clock input for I2C and I3C Basic bus management interface.
    1          SDA        IO    Data input and output for I2C and I3C Basic bus management interface.
                                General Status Interrupt. Open Drain Output. This PMIC asserts this pin low to
    1          GSI_n      O     communicate any or more events to host. This pin stays asserted until the appropriate
                                registers are explicitly cleared and event is no longer present.
    1           PID       I     PMIC ID pin for I2C and I3C Basic bus.
                                No Connect. This pin is not connected internally in the package to the die. Typical
    4           NC
                                application connects this pin to GND on PCB for better thermal performance.
```

## 2.2 Package



### 2.2.1 Flip Chip QFN Package (3 mm x 4 mm)

```text
• 28 pins (24 Functional pins; 4 dummy corner pins)
• 3 mm x 4 mm Maximum Package Outline
```

### 2.2.2 Mechanical Drawing

The drawing and dimension for 28 pins FC QFN package.

*Figure 1 — QFN Package Mechanical Drawing* (figure; any text below/above was extracted from the drawing)

*Figure 2 — QFN Package Mechanical Drawing - Detail Dimensions* (figure; any text below/above was extracted from the drawing)

*Figure 3 — Recommended PCB Pattern (Units: mm)* (figure; any text below/above was extracted from the drawing)

### 2.2.3 Pinout (FC QFN Package - 28 Pins)

```text
                                          3mm

                                           PWR_GOOD

                                                      SWC_FB_P
                               SWA_FB_P
                       VR_EN

                                                                 GSI_n
                       28

                               27

                                            26

                                                      25

                                                                 24
          NC   1                                                                    23   NC

 BOOT_SWA      2                                                                   22    BOOT_SWC

 VIN_Bulk_A        3                                                          21         VIN_Bulk_C

    SWA            4                                                          20          SWC

                                                                                                      4mm
   PGND            5                                                          19         PGND

    SWB            6                                                          18         SCL

VIN_Bulk_B         7                                                          17         SDA
BOOT_SWB       8                                                                   16    VOUT_1.0V

        NC     9                                                                         NC
                       10

                               11

                                            12

                                                      13

                                                                 14

                                                                                   15
                       PID

                               SWB_FB_P

                                                                  VOUT_1.8V
                                                      AGND
                               m           VIN
```

*Figure 4 — FC QFN Package Pinout - 28 Pins (Top View)* (figure; any text below/above was extracted from the drawing)

```text
                                                3mm

                                                 PWR_GOOD

                                                            SWA_FB_P
                                     SWC_FB_P

                                                                       VR_EN
                          GSI_n
                         24

                                     25

                                                  26

                                                            27

                                                                       28
          NC   23                                                                      1    NC

 BOOT_SWC      22                                                                  2        BOOT_SWA

 VIN_Bulk_C         21                                                         3            VIN_Bulk_A

    SWC             20                                                         4             SWA

                                                                                                         4mm
   PGND             19                                                         5            PGND

    SCL             18                                                         6            SWB

   SDA              17                                                         7           VIN_Bulk_B
VOUT_1.0V      16                                                                  8        BOOT_SWB

          NC   15                                                                           NC
                         14

                                     13

                                                  12

                                                            11

                                                                       10

                                                                                   9
                                                            SWB_FB_P
                         VOUT_1.8V

                                     AGND

                                     m           VIN

                                                                        PID
```

*Figure 5 — FC QFN Package Pinout - 28 Pins (Bottom View)* (figure; any text below/above was extracted from the drawing)
