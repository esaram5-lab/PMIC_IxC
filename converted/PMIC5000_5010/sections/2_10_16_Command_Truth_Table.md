---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 2.10.16
title: Command Truth Table
pages: 90-91
---
# 2.10.16 Command Truth Table

The command truth table as shown in Table 85 only applies in I3C Basic mode with PEC enabled. In I2C mode and I3C Basic mode with PEC disabled, the command truth table does not apply.

**Table 85 — For I3C Mode only with PEC Enabled - Command Truth Table**

```text
                                               CMD Code           RW        Address
                               Command          2nd Byte       2nd Byte    1st Byte
     TS5 Command                 Name           Bits [7:5]      Bit [4]    Bits [7:0]
 Write 1 Byte to Register        W1R                              0            V
                                                   000
Read 1 Byte from Register        R1R                              1            V
 Write 2 Byte to Register        W2R                              0            V
                                                   001
Read 2 Byte from Register        R2R                              1            V
 Write 4 Byte to Register        W4R                              0            V
                                                   010
Read 4 Byte from Register        R4R                              1            V
 Write 16 Byte to Register      W16R                              0            V
                                                   011
Read 16 Byte from Register       R16R                             1            V
         Reserved               RSVD           100 to 111       RSVD        RSVD
```
