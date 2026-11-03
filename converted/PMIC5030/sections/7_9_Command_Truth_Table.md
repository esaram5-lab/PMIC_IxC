---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 7.9
title: Command Truth Table
pages: 113-114
---
# 7.9 Command Truth Table

The command truth table as shown in Table 99 only applies in I3C Basic mode with PEC enabled for the CMD field (bits [7:5] for Write and Read data packet). In I2C mode and I3C Basic mode with PEC disabled, the command truth table does not apply.

**Table 99 — For I3C Mode only with PEC Enabled - Command Truth Table**

```text
                                             CMD Code        RW           Address

                                             2nd Byte

                                   Command                2nd Byte       1st Byte
        TS5 Command                  Name    Bits [7:5]    Bit [4]       Bits [7:0]

 Write 1 Byte to Register            W1R        000            0              V

Read 1 Byte from Register            R1R                       1              V

 Write 2 Byte to Register            W2R        001            0              V

Read 2 Byte from Register            R2R                       1              V

 Write 4 Byte to Register            W4R        010            0              V

Read 4 Byte from Register            R4R                       1              V

 Write 16 Byte to Register           W16R       011            0              V

Read 16 Byte from Register           R16R                      1              V

          Reserved                   RSVD       100         RSVD           RSVD
                                              to 111
```
