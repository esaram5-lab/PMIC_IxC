---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 5.4.5
title: Packet Error Check Function
pages: 97-98
---
# 5.4.5 Packet Error Check Function

In I2C mode, packet error checking is not supported. Only I3C Basic mode supports packet error checking. The PMIC device implements an 8-bit Packet Error Code (PEC) which is appended at the end of all transactions if PEC is enabled through DEVCTRL CCC. The PEC is a CRC-8 value calculated on all the messages bytes except for START, REPEAT START, STOP conditions or T-bits, ACK, NACK and IBI header (7’h7E followed by W=0) bits. The polynomial for CRC-8 calculations is:

```text
• C(X) = X8 + X2 + X1 + 1
```

The seed value for PEC function is all zeros. When Host calculates PEC for PMIC device, it includes LID and HID bits followed by R/W bit.
