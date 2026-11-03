---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 7.5.5
title: Packet Error Check (PEC) Function
pages: 90-91
---
# 7.5.5 Packet Error Check (PEC) Function

In I2C mode, packet error checking is not supported. Only I3C Basic mode supports packet error checking. The PMIC device implements an 8-bit Packet Error Code (PEC) which is appended at the end of all transactions if PECs is enabled through DEVCTRL CCC. The PEC is a CRC-8 value calculated on all the messages bytes except for START, STOP, REPEATED START conditions or T-bits, ACK and NACK and IBI header (7’h7E followed W=0) bits. The polynomial for CRC-8 calculations is:

```text
▪ C(X) = X8 + X2 + X1 + 1
```

The seed value for PEC function is all zero. When Host calculates PEC for PMIC device, it includes LID and HID bits followed by R/W bit.
