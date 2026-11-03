---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 5.4.14
title: Command Truth Table
pages: 119-120
---
# 5.4.14 Command Truth Table

The command truth table only applies in I3C mode with PEC enabled for the CMD field (bits [7:5] for Write and Read data packet). In I2C mode and in I3C Basic mode with PEC disabled, the command truth table does not apply.

**Table 98 — I3C Basic Mode with PEC Enabled Command Truth Table**

```text
                                                                             PMIC 8 bit
                                             Command                          Register
                                               Code             RW          Address [7:0]
                              Command         2nd Byte      2nd Byte Bit    1st Byte Bits
PMIC Command (CMD Field)        Name          Bits [7:5]        [4]             [7:0]
  Write 1 Byte to Register       W1R             000              0               V
 Read 1 Byte from Register       R1R                              1               V
  Write 2 Byte to Register       W2R             001              0               V
 Read 2 Byte from Register       R2R                              1               V
  Write 4 Byte to Register       W4R             010              0               V
 Read 4 Byte from Register       R4R                              1               V
  Write 16 Byte to Register      W16R            011              0               V
 Read 16 Byte from Register      R16R                             1               V

         Reserved                RSVD            100           RSVD             RSVD
         Reserved                RSVD            101           RSVD             RSVD

         Reserved                RSVD            110           RSVD             RSVD
         Reserved                RSVD            111           RSVD             RSVD
```
