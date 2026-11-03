---
document: JESD301-2 (PMIC5100 Power Management IC Standard, Rev. 1.03, October 2022)
device: PMIC5100
application: client
section: 3.1
title: Input Supply Electrical Characteristics
pages: 9-10
---
# 3.1 Input Supply Electrical Characteristics

**Table 2 — Input Supply DC + AC Specification1**

```text
               Parameter                                      Symbol                       Min         Typ       Max        Unit       Notes
Bulk Input Supply Voltage                                    VIN_Bulk                      4.25        5.0       5.5         V          2
Bulk Input Supply Maximum AC Voltage                       VIN_Bulk_AC                       -          -        6.5         V
Bulk Input Supply Voltage Ramp Up Rate                   VIN_Bulk_Ramp_Up                  0.1          -        3.0        V/ms          3
Bulk Input Supply Voltage Ramp Down
                                                        VIN_Bulk_Ramp_Down                  0.5          -        1.0       V/ms          4
Rate
Bulk Input Supply Voltage Start Up
                                                      VIN_Bulk_OS_STARTUP                    -           -       TBD        V*μs          5
Overshoot
Maximum Input Current for VIN_Bulk
                                                                 IVIN_Bulk                 0.05          -        2.0          A          6
Input Supply Voltage
VIN_Bulk Input Quiescent Current                            IVIN_Bulk_Quiescent              -           -        25          μA          7
VIN_Bulk Input Idle Current                                   IVIN_Bulk_Idle                 -           -       TBD          μA          8
NOTE 1 Input supply is referred in this table are VIN_Bulk and VIN.
NOTE 2 During first power on, the input voltage supply must reach minimum 4.25 V for PMIC to detect valid input supply.
NOTE 3 The ramp up rate between 300 mV and 4.0 V.
NOTE 4 The ramp down rate between 4.0 V and 300 mV.

NOTE 5 The area under the curve above VIN_Bulk = TBD V. VIN_Bulk_AC spec must also be satisfied.
NOTE 6 The minimum input current requirement is to deliver the maximum output current on VOUT_1.8V and VOUT_1.0V LDO plus the

       current required by the PMIC for its own use. The maximum input current PMIC may see on its all VIN_Bulk input.
NOTE 7 VIN_Bulk = 5.0 V. Measured at room temperature. All circuitry including output regulators and LDOs are off. VR_EN signal is static

       Low or High; GSI_n signal is pulled High. I2C or I3C Basic interface access is not allowed and bus is pulled High. PID signal is pulled
       either High or Low.
NOTE 8 VIN_Bulk = 5.0 V. Measured at room temperature. All output regulators and LDOs are on with 0 A output load. VR_EN signal is static
          Low or High. GSI_n signal is pulled High. I2C or I3C Basic interface access is allowed and bus is pulled High. PID signal is pulled
          either High or Low
```
