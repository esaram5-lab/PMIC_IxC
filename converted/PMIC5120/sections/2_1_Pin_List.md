---
document: JESD301-6 (PMIC5120 Power Management IC Standard, Version 1.0, February 2025)
device: PMIC5120
application: client
section: 2.1
title: Pin List
pages: 3-4
---
# 2.1 Pin List

**Table 2 — PMIC Pin Description**

```text
Pin Count    Pin Name    Type                                  Description
            VIN_Bulk_A       5 V power input supply to the PMIC for SWA, SWB and SWC respectively.
    3       VIN_Bulk_B    I All three VIN_Bulk input pins must be connected to the 5 V input supply even
            VIN_Bulk_C       if one or more output regulators are not intended to be used.
    1           VIN       I 5 V power input supply to the PMIC for analog circuits.
    2         PGND       PWR Power Ground. Connects to DIMM ground plane.
    1         AGND       PWR Analog Ground. Connects to DIMM ground plane.
                             Switch node A output buck regulator. This pin connects to L1 power inductor.
                             In single phase regulator mode of operation, the SWA output must not be con-
                             nected to SWB output even if they are configured to same exact output volt-
    1           SWA       O
                             age.
                             In dual phase regulator mode of operation, the SWA and SWB outputs are con-
                             nected.
                             Switch node B output buck regulator. This pin connects to L2 power inductor.
                             In single phase regulator mode of operation, the SWA output must not be con-

                             nected to either SWB output even if they are configured to same exact output
    1           SWB       O
                             voltage.

                             In dual phase regulator mode of operation, the SWA and SWB outputs are con-
                             nected.

    1           SWC       O Switch node C output buck regulator. This pin connects to L3 power inductor.
                             Bootstrap node for SWA high side NMOS driver. This pin connects to SWA
    1       BOOT_SWA     PWR
                             through a high quality capacitor.
                             Bootstrap node for SWB high side NMOS driver. This pin connects to SWB
    1       BOOT_SWB     PWR
                             through a high quality capacitor.
                             Bootstrap node for SWC high side NMOS driver. This pin connects to SWC
    1       BOOT_SWC     PWR
                             through a high quality capacitor.
                             Switch node A output buck regulator positive feedback. In single phase or dual
    1       SWA_FB_P      I phase regulator mode of operation, this pin connects to DIMM power plane
                             load.
                             Switch node B output buck regulator positive feedback. In single phase regula-
    1       SWB_FB_P      I tor mode of operation, this pin connects to DIMM power plane load. In dual
                             phase regulator mode of operation, this pin is connected to GND.
                             Switch node C output buck regulator positive feedback. This pin connects to
    1       SWC_FB_P      I
                             DIMM power plane load.
    1       VOUT_1.8V     O 1.8V LDO Output
    1       VOUT_1.0V     O 1.0V LDO Output

Pin Count      Pin Name      Type                                           Description
                                     Power good indicator. Open Drain output. The PMIC floats this pin high when
                                     VIN_Bulk input supply as well as all enabled output buck regulators and all
                                     LDO regulator tolerance threshold is maintained as configured in appropriate
                                     register. The PMIC drives this pin low when VIN_Bulk input goes below the
    1        PWR_GOOD          IO    threshold or when any of the enabled switch output regulators exceeds the
                                     threshold configured in the appropriate register or any LDO output regulator
                                     exceeds the threshold tolerance.
                                     Input: The PMIC disables its output regulators when this pin transitions from
                                     high to low. The LDO outputs shall remain on.
                                     PMIC Enable. When this pin is high, the PMIC turns on the regulator. When
    1           VR_EN          I     this pin is low, the PMIC turns off the regulator. This pin shall not be left float-
                                     ing. If it is not used, it shall be tied to GND.
    1            SCL            I    Clock input for I2C and I3C Basic bus management interface.
    1            SDA           IO    Data input and output for I2C and I3C Basic bus management interface.
                                     General Status Interrupt. Open Drain Output. This PMIC asserts this pin low to
    1           GSI_n          O     communicate any or more events to host. This pin stays asserted until the
                                     appropriate registers are explicitly cleared and event is no longer present.
    1             PID          I     PMIC ID pin for I2C and I3C Basic bus.
                                     Thermal connection to GND. This pin is connected to GND on the PCB and
    4          TC/GND
                                     may be connected to GND on the die.
```
