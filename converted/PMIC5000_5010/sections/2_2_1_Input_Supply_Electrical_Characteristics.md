---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 2.2.1
title: Input Supply Electrical Characteristics
pages: 3-4
---
# 2.2.1 Input Supply Electrical Characteristics

**Table 2 — Input Supply DC + AC Specification**

```text
               Parameter                                      Symbol                   Min         Typ       Max        Unit      Notes
Bulk Input Supply Voltage DC Voltage                         VIN_Bulk                  4.25         12       15          V          1,2
Bulk Input Supply Maximum AC Voltage                       VIN_Bulk_AC                   -           -       18          V
Bulk Input Supply Maximum Voltage Start
                                                      VIN_Bulk_OS_Startup                 -          -         33       V*μs         3
up Overshoot
Bulk Input Supply Voltage Ramp Up Rate                 VIN_Bulk_Ramp_Up                 0.1          -        3.0       V/ms         4
Bulk Input Supply Voltage Ramp Down
                                                     VIN_Bulk_Ramp_Down                   -          -        1.0       V/ms         5
Rate
Management Input Supply Voltage                              VIN_Mgmt                   3.0        3.3        3.6         V          6
Management Input Supply Ramp Up and
                                                         VIN_Mgmt_Ramp                 0.15                    3        V/ms
Down Rate
Minimum Management Input Supply
                                                              IVIN_Mgmt                 110          -          -        mA          7
Current
Bulk Input Supply Current                                       IVIN_Bulk                             -        2.5         A           8
NOTE 1   During first power on, the input voltage supply must reach minimum value based on default from register Table 116, “Register 0x1A”
         [7:5] + 1.0V for PMIC to detect valid input supply.
NOTE 2   The PMIC efficiency is optimized for nominal input supply of 12 V or lower. The PMIC efficiency above 13.8 V is degraded and
         thermal impact must be considered. The PMIC operation above 14.2V should not be greater than 20% duty cycle at any time and should

         be limited to a maximum contiguous period of 10 minutes.
NOTE 3   The area under the curve above VIN_Bulk = 15V. VIN_Bulk_AC spec must also be satisfied.
NOTE 4   The ramp up rate between 300 mV and 8.0 V.

NOTE 5   The ramp down rate between 8.0 V and 300 mV.
NOTE 6   During first power on, the input voltage supply must reach minimum value of 2.8 V for PMIC to detect valid input supply.
NOTE 7   This is a platform spec. The minimum input current delivered by the platform through the DIMM gold finger to deliver the maximum

         load on LDO outputs (1.8V LDO output + 1.0V LDO output = 25 mA + 20 mA) plus the current required by the PMIC for its own
         usage.
NOTE 8   This is a platform spec. The maximum input current delivered by the platform through the DIMM gold finger.
```
