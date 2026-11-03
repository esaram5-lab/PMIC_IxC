---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 2
title: Package
pages: 3-7
---
# 2 Package



## 2.1 Package Pinout

The PMIC device is packaged in 5 mm x 5 mm FCQFN. The PMIC pinout is shown in Figure 1 and Figure 2 for Top view and Bottom view, respectively.

```text
                                                                                                                 SWB_Disable 28
                                     PWR_GOOD 34

                                                                                     DVFSQ_n 30

                                                                                                                                              TC/GND
                         SWD_FB 35

                                                                                                                                  SWB_FB 27
            TC/GND

                                                   VR_EN 33

                                                                         Unlock 31

                                                                                                  GSI_n 29
                                                                PID
                                                                32

                                                                                                                                                 26
            1

SWD_BOOT 2                                                                                                                                        25   SWB_BOOT

  VIN_Bulk 3                                                                                                                                      24   VIN_Bulk

     SWD 4                                                               Top View                                                                 23   SWB

    PGND                                                                                                                                               PGND
                                                                                                                                                 5
                                                              CAMM2 LPDDR5 PMIC
     SWA    6                                                                                                                                     22   SWC
                                                                 5mm x 5mm
                                                                   FCQFN
 VIN_Bulk   7                                                                                                                                     21 VIN_Bulk

SWA_BOOT    8                                                                                                                                     20 SWC_BOOT
                                                                                                                                                 19
            9

                                                                                                                 17 VOUT_1.0V

                                                                                                                                  18 SWC_FB
                         10 SWA_FB

                                     11 VBIAS

                                                   12 SCL

                                                                13 SDA

                                                                         14 VIN

                                                                                     15 AGND

                                                                                                  16 VOUT_1.8V
                TC/GND

                                                                                                                                              TC/GND
```

*Figure 1 — PMIC Package - Top View* (figure; any text below/above was extracted from the drawing)

```text
                                      SWB_Disable 28

                                                                                                                       PWR_GOOD 34
                                                                       DVFSQ_n 30
                        SWB_FB 27

                                                                                                                                                 TC/GND
                                                                                                                                     SWD_FB 35
              TC/GND

                                                                                       Unlock 31

                                                                                                            VR_EN 33
                                                       GSI_n 29

                                                                                                   PID 32
             26

                                                                                                                                                    1
SWB_BOOT 25                                                                                                                                               2   SWD_BOOT

  VIN_Bulk 24                                                                                                                                             3   VIN_Bulk

     SWB 23                                                                         Bottom View                                                           4   SWD

    PGND                                                                                                                                                      PGND

                                                                                                                                                    5
                                                                      CAMM2 LPDDR5 PMIC
     SWC 22                                                              5mm x 5mm                                                                        6 SWA

                                                                           FCQFN
 VIN_Bulk    21                                                                                                                                           7 VIN_Bulk

SWC_BOOT     20                                                                                                                                           8 SWA_BOOT
             19

                                                                                                                                                    9
                                                                                                                       11 VBIAS

                                                                                                                                     10 SWA_FB
                        18 SWC_FB

                                     17 VOUT_1.0V

                                                       16 VOUT_1.8V

                                                                       15 AGND

                                                                                       14 VIN

                                                                                                   13 SDA

                                                                                                            12 SCL
               TC/GND

                                                                                                                                                 TC/GND
```

*Figure 2 — PMIC Package - Bottom View* (figure; any text below/above was extracted from the drawing)

## 2.2 Pin List

**Table 2 — PMIC Pin Description**

```text
      Pin Name      Type                                                  Description
VIN_Bulk (4x)         I    5 V power input supply pin to the PMIC. All four VIN_Bulk input pins must be connected to the 5V input
                           supply even if one or more output regulators are not intended to be used.
VIN                   I    5 V power input supply pin to the PMIC for analog circuits.
PWR_GOOD             IO    Power good indicator.
                           Open drain output. The PMIC floats this pin high when VIN_Bulk input supply as well as enabled output
                           buck regulators and all LDO regulator tolerance threshold is maintained as configured in appropriate
                           register. The PMIC dives this pin low when VIN_Bulk input goes below the threshold or when any of the
                           enabled switch output regulators exceeds the threshold configured in the appropriate register or any LDO
                           output regulator exceeds the threshold tolerance.
                           Input: The PMIC disables its output regulators when this pin transitions from high to low. The LDO outputs
                           shall remain on.
VBias               PWR Vbias Voltage generated by PMIC.
SCL                   I    I2C/I3C Basic Clock Input for management bus.
SDA                  IO    I2C/I3C Basic Data Input/Output for management bus.
SWA                  O     Output switch node A buck regulator. This pin connects to L1 power inductor.
                           The SWA output must not be connected to SWB output even if they are configured as same exact output

                           voltage.
SWA_BOOT            PWR Bootstrap node for SWA high side NMOS driver. This pin connects to SWA through a high quality

                        capacitor.
SWA_FB                I    This pin connects to CAMM2 power plane load.

SWB                  O     Output switch node B buck regulator. This pin connects to L2 power inductor.
                           The SWB output must not be connected to SWA output even if they are configured as same exact output
                           voltage.
SWB_BOOT            PWR Bootstrap node for SWB high side NMOS driver. This pin connects to SWB through a high quality
                        capacitor.
SWB_FB                I    This pin connects to CAMM2 power plane load.
SWC                  O     Output switch node C buck regulator. This pin connects to L3 power inductor.
SWC_BOOT            PWR Bootstrap node for SWC high NMOS driver. This pin connects to SWC through a high quality capacitor.
SWC_FB                I    This pin connects to CAMM2 power plane load.
SWD                  O     Output switch node D buck regulator. This pin connects to L4 power inductor.
SWD_BOOT            PWR Bootstrap node for SWD high side NMOS driver. This pin connects to SWD through a high quality
                        capacitor.
SWD_FB                I    This pin connects to CAMM2 power plane load.
PID                   I    PMIC ID pin for I2C and I3C Basic bus. This pin connects to CAMM2 ground plane or VOUT_1.8V rail or
                           left floating.
VOUT_1.8V            O     1.8V LDO Output.
VOUT_1.0V            O     1.0 V LDO Output.
AGND                PWR Analog Ground. Connects to CAMM2 ground plane.
PGND                PWR Power Ground. Connects to CAMM2 ground plane.

   Pin Name   Type                                                   Description
VR_EN          I     PMIC Enable. When this pin is high, the PMIC turns on the regulator. When this pin is low, the PMIC turns
                     off the regulator. This pin shall not be left floating. If it is not used, it shall be tied to GND.
SWB_Disable    I     If SWB_Disable input pin function is enabled, the PMIC keeps the SWB output regulator disabled when
                     the SWB_Disable input pin is high at the time of VR Enable command.
                     If SWB_Disable input pin function is enabled, the PMIC follows the normal power on sequence config 0 to
                     power on sequence config 3 registers when the SWB_Disable input pin is low at the time of VR Enable
                     command.
                     If SWB_Disable input pin is disabled, the PMIC input receiver is off and PMIC follows the normal power on
                     sequence config0 to config3 registers.
                     On the CAMM2 PCB, this pin has an external 100KΩ pulldown resistor to GND. This pin shall not be left
                     floating.
TC/GND               Thermal connection to GND. This pin is connected to GND on the PCB and may or may not be connected
                     to GND on the die.
Unlock         I     Active High Asynchronous input.
                     If Unlock pin function is enabled, register R2F[2] value follows the Unlock input pin level. When this input
                     pin is high, it updates R2F[2] to ‘1’ and puts PMIC in a programmable mode; when this input pin is low, it
                     updates R2F[2] to ‘0’ and puts PMIC in a secure mode.
                     If Unlock pin function is disabled, the input receiver is disabled and this pin has no effect on PMIC. The
                     register R2F[2] definition applies for secure and programmable mode operation.
DVFSQ_n        I     Active Low Asynchronous input. Edge triggered, Active low.

                     If DVFSQ_n pin function is enabled, when this input pin transitions from high to low while in the P3 state,
                     the PMIC enters DVFSQ state where the PMIC SWB output voltage is as defined in register R3E[7:1] and
                     R2B [3] at slew rate defined in R2E[7:6]. When this input pin transitions from low to high while in DVFSQ

                     state, the PMIC SWB output voltage is as defined in register R25[7:1] and R2B[3] at slew rate defined in
                     R2E[7:6].

                     If DVFSQ_n pin is disabled, the input receiver is disabled and this pin has no effect on SWB output
                     voltage, and entry into the DVFSQ power state is disabled.
GSI_n          O     General Status Interrupt; Open Drain Output. When this pin is enabled, the PMIC asserts this pin low to
                     communicate any one or more events to host. This pin stays asserted until the appropriate registers are
                     explicitly cleared and the event is no longer present.
```
