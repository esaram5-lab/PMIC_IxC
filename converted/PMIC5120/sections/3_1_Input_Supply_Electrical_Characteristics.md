---
document: JESD301-6 (PMIC5120 Power Management IC Standard, Version 1.0, February 2025)
device: PMIC5120
application: client
section: 3.1
title: Input Supply Electrical Characteristics
pages: 10-11
---
# 3.1 Input Supply Electrical Characteristics

**Table 3 — Input Supply DC + AC Specification1**

```text
                Parameter                       Symbol                            Min     Typ       Max       Unit Notes
Bulk Input Supply Voltage                      VIN_Bulk                           4.25    5.0       5.5        V     2
Bulk Input Supply Maximum AC Voltage        VIN_Bulk_AC                             -      -        6.5        V
Maximum voltage on VIN_Bulk during soft                                                                               3,4,5
                                        VIN_Bulk_Soft_Stop_Max                      -       -       5.55       V
stop
Bulk Input Supply Voltage Ramp Up Rate    VIN_Bulk_Ramp_Up                        0.1       -        3.0     V/ms       6
Bulk Input Supply Voltage Ramp Down
                                         VIN_Bulk_Ramp_Down                       0.5       -        1.0     V/ms       7
Rate
Bulk Input Supply Voltage Start Up
                                        VIN_Bulk_OS_STARTUP                         -       -       TBD      V*µs       8
Overshoot
Maximum Input Current for VIN_Bulk
                                               IVIN_Bulk                            -       -        3.5       A        9
Input Supply Voltage
VIN_Bulk Input Quiescent Current           IVIN_Bulk_Quiescent                      -       -        25        µA      10
VIN_Bulk Input Idle Current                  IVIN_Bulk_Idle                         -       -       TBD        µA       11

NOTE 1  Input supply is referred in this table are VIN_Bulk and VIN.

NOTE 2  During first power on, the input voltage supply must reach minimum 4.25 V for PMIC to detect valid input supply.
NOTE 3  The maximum VIN_Bulk input supply voltage rise during soft stop for SWx soft stop operation.
NOTE 4  The maximum VIN_Bulk input supply voltage rise is tested with max VIN_Bulk = 5.5V, including DC or AC offset.

        SWA and SWB = 1.1V, SWC = 1.8V, and using the recommended setting from the “PMIC Register setting for the Soft
        Stop” table in JESD323 or JESD324, depending on the DIMM type. The test condition assumes input VIN_Bulk

        supply is not capable of sinking current. The maximum VIN_Bulk input supply voltage rise is tested with module
        VIN_Bulk and output rail decoupling from any relevant passed CSODIMM or CUDIMM RC ballot, and with bulk
        output capacitance for SWx listed in Section 5, “DDR5 DIMM Schematic”.
NOTE 5 This specification defines the DC component of the voltage during soft stop. AC noise that is less than 1µs can be
        ignored when testing against this spec. The maximum voltage rise is measured under 1 MHz bandwidth limiting during
        soft stop shut down
NOTE 6 The ramp up rate between 300 mV and 4.0 V.
NOTE 7 The ramp down rate between 4.0 V and 300 mV.
NOTE 8 The area under the curve above VIN_Bulk = 5.5 V. VIN_Bulk_AC spec must also be satisfied.
NOTE 9 This is a platform spec, the maximum input current delivered by the platform through the DIMM gold finger.
NOTE 10 VIN_Bulk = 5.0 V. Measured at room temperature. All circuitry including output regulators and LDOs are off.
        VR_EN signal is static Low or High; GSI_n signal is pulled High. I2C or I3C Basic interface access is not allowed and
        bus is pulled High. PID signal is pulled either High or Low.
NOTE 11 VIN_Bulk = 5.0 V. Measured at room temperature. All output regulators and LDOs are on with 0 A output load.
        VR_EN signal is static Low or High. GSI_n signal is pulled High. I2C or I3C Basic interface access is allowed and
        bus is pulled High. PID signal is pulled either High or Low
```
