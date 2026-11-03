---
document: JESD301-2 (PMIC5100 Power Management IC Standard, Rev. 1.03, October 2022)
device: PMIC5100
application: client
section: 6.17.14
title: Command Truth Table
pages: 104-105
---
# 6.17.14 Command Truth Table

The command truth table only applies in I3C mode with PEC enabled. In I2C mode and in I3C Basic mode with PEC disabled, the command truth table does not apply.

**Table 85 — I3C Basic Mode with PEC Enabled Command Truth Table**

```text
                                                   Command                                PMIC 8 bit Register
                                                     Code               RW                  Address [7:0]

                                     Command        2nd Byte
PMIC Command (CMD Field)               Name         Bits [7:5]     2nd Byte Bit [4]         1st Byte Bits [7:0]
   Write 1 Byte to Register            W1R                               0                          V
                                                        000
  Read 1 Byte from Register             R1R                              1                          V
   Write 2 Byte to Register            W2R                               0                          V
                                                        001
  Read 2 Byte from Register             R2R                              1                          V
   Write 4 Byte to Register            W4R                               0                          V
                                                        010
  Read 4 Byte from Register             R4R                              1                          V
   Write 16 Byte to Register           W16R                              0                          V
                                                        011
  Read 16 Byte from Register           R16R                              1                          V
           Reserved                    RSVD             100            RSVD                       RSVD
           Reserved                    RSVD             101            RSVD                       RSVD
           Reserved                    RSVD             110            RSVD                       RSVD
           Reserved                    RSVD             111            RSVD                       RSVD
```
