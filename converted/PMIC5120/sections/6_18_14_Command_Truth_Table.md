---
document: JESD301-6 (PMIC5120 Power Management IC Standard, Version 1.0, February 2025)
device: PMIC5120
application: client
section: 6.18.14
title: Command Truth Table
pages: 109-109
---
# 6.18.14 Command Truth Table

The command truth table only applies in I3C Basic mode with PEC enabled. In I2C mode and in I3C Basic mode with PEC disabled, the command truth table does not apply.

**Table 89 — I3C Basic Mode Only with PEC Enabled Command Truth Table**

```text
                                                                                  PMIC 8 bit
                                                     Command                       Register
                                                       Code            RW        Address [7:0]

                                     Command         2nd Byte       2nd Byte      1st Byte Bits
PMIC Command (CMD Field)               Name          Bits [7:5]      Bit [4]          [7:0]
     Write 1 Byte to Register           W1R                             0               V
                                                        000
   Read 1 Byte from Register            R1R                             1               V
     Write 2 Byte to Register           W2R                             0               V
                                                        001
   Read 2 Byte from Register            R2R                             1               V
     Write 4 Byte to Register           W4R                             0               V
                                                        010
   Read 4 Byte from Register            R4R                             1               V
    Write 16 Byte to Register          W16R                             0               V
                                                         011
   Read 16 Byte from Register           R16R                            1               V
            Reserved                   RSVD             100           RSVD           RSVD

            Reserved                   RSVD             101           RSVD           RSVD

            Reserved                   RSVD              110          RSVD           RSVD
            Reserved                   RSVD              111          RSVD           RSVD
```
