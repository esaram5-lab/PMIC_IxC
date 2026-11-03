---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 5.1.1
title: Input Supply Electrical Characteristics
pages: 9-10
---
# 5.1.1 Input Supply Electrical Characteristics

**Table 5 — Input Supply DC + AC Specification**

```text
                    Parameter                                     Symbol                 Min       Typ      Max        Unit     Notes

Bulk Input Supply Voltage DC Voltage                             VIN_Bulk               4.25       12        15         V        [1],[2]

Bulk Input Supply Maximum AC Voltage                           VIN_Bulk_AC                -         -        18         V

Bulk Input Supply Maximum Voltage Start up                 VIN_Bulk_OS_Startup            -         -        33       V*μs        [3]
Overshoot

Bulk Input Supply Voltage Ramp Up Rate                     VIN_Bulk_Ramp_Up             0.01        -        3.0      V/ms        [4]

Bulk Input Supply Voltage Ramp Down Rate                  VIN_Bulk_Ramp_Down            0.01        -        1.0      V/ms        [5]

Management Input Supply Voltage                                  VIN_Mgmt                3.0       3.3       3.6        V         [6]

Management Input Supply Ramp Up and Down Rate                VIN_Mgmt_Ramp              0.15                  3       V/ms
Minimum Management Input Supply Current                           IVIN_Mgmt              250        -         -        mA         [7]

Bulk Input Supply Current                                         IVIN_Bulk                         -         4         A         [8]

 NOTE 1     During first pow er on, the input voltage supply must reach minimum value based on default from register Table 131, Register
            0x1A [7:5] + 1.0V for PMIC to detect valid input supply.

 NOTE 2     The PMIC efficiency is optimized for nominal input supply of 12 V or lower. The PMIC efficiency above 13.8 V is degraded and
            thermal impact must be considered. The PMIC operation above 14.2 V should not be greater than 20% duty cycle at any time

            and should be limited to a maximum contiguous period of 10 minutes.
 NOTE 3     The area under the curve above VIN_Bulk = 15 V. VIN_Bulk_AC spec must also be satisfied.
 NOTE 4     The ramp up rate between 300 mV and 8.0 V.
 NOTE 5     The ramp down rate between 8.0 V and 300 mV.
 NOTE 6     During first power on, the input voltage supply must reach minimum value of 2.8 V for PMIC to detect valid input supply.
 NOTE 7     This is a platform spec. The minimum input current delivered by the platform through the DIMM gold finger to deliver the
            maximum load on LDO outputs (1.8V LDO output + 1.0V LDO output = 25 mA + 20 mA) plus the current required by the PMIC
            for its own usage.
 NOTE 8     This is a platform requirement spec. The maximum input supply voltage current requirement spec delivered by the platform
            through the DIMM gold finger.
```
