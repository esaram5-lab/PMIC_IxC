---
document: JESD301-6 (PMIC5120 Power Management IC Standard, Version 1.0, February 2025)
device: PMIC5120
application: client
section: 3.9
title: Thermal Characteristics
pages: 21-22
---
# 3.9 Thermal Characteristics

**Table 19 — Thermal Characteristics**

```text
                Parameter                             Symbol         Maximum Rating            Unit       Notes
Thermal resistance junction to case                     ΘJC               TBD                  °C/W        1,2,3
Junction operating temperature                          TJ              -10 to 125              °C
Case operating temperature                              TC             -10 to TBD               °C           3
Storage temperature                                    TSTG3            -55 to 150              °C           3
Lead temperature (soldering, 10s)                     TLEAD                260                  °C           3

NOTE 1     The maximum power dissipation is PD(MAX) = (TJMAX - TC)/ ΘJC. Exceeding the maximum
           allowable power dissipation results in excessive die temperature and the device will enter thermal
           shutdown.
NOTE 2     This thermal rating was calculated on JEDEC 51 standard 4 layer board with dimensions 3” x 4.5”
           in still air conditions. Actual thermal resistance is affected by PCB size, solder joint quality, layer
           count, copper thickness, air flow, altitude and other unlisted variables.
NOTE 3     This specification is compliant with JESD402-1 Temperature Grade and Measurement
           Specification for Components and Modules, operating temperature range MT, storage
           temperature range TSTG3. See JESD402-1 for details, including measurement point.
```
