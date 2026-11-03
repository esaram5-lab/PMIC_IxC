---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 3.8
title: Thermal Characteristics
pages: 24-25
---
# 3.8 Thermal Characteristics

**Table 22 — Thermal Characteristics**

```text
                  Parameter                            Symbol          Maximum Rating            Unit       Notes

 Thermal resistance junction to case                     ΘJC                  TBD               0C/W       [1],[2],[3]

 Junction operating temperature                           TJ               -10 to 125             0C

 Case operating temperature                               TC               -10 to TBD             0C           3

 Storage temperature                                    TSTG3              -55 to 150             0C           3

 Lead temperature (soldering, 10s)                      TLEAD                  260                0C           3
NOTE 1 The maximum power dissipation is PD(MAX) = (TJMAX - TC)/ ΘJC. Exceeding the maximum allowable power
        dissipation results in excessive die temperature and the device will enter thermal shutdown.
NOTE 2    This thermal rating was calculated on JEDEC 51 standard 4 layer board with dimensions 3” x 4.5” in still
          air conditions. Actual thermal resistance is affected by PCB size, solder joint quality, layer count, copper
          thickness, air flow, altitude and other unlisted variables.
NOTE 3    This specification is compliant with JESD402-1 Temperature Grade and Measurement Specification for
          Components and Modules, operating temperature range MT, storage temperature range TSTG3. See
          JESD402-1 for details, including measurement point.
```
