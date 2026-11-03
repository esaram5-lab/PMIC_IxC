---
document: JESD301-6 (PMIC5120 Power Management IC Standard, Version 1.0, February 2025)
device: PMIC5120
application: client
section: 6.18.5
title: Packet Error Check (PEC) Function
pages: 86-86
---
# 6.18.5 Packet Error Check (PEC) Function

In I2C mode, packet error checking is not supported. Only I3C Basic mode supports packet error checking.

The PMIC device implement an 8-bit Packet Error Code (PEC) which is appended at the end of all transactions if PECs is enabled through DEVCTRL CCC or by directly writing ‘1’ to Table 148, Register 0x34 [7]. The PEC is a CRC-8 value calculated on all the messages bytes except for START, REPEAT START, STOP conditions or T-bits, ACK, NACK and IBI header (7’h7E followed by W=0) bits.

The polynomial for CRC-8 calculations is:

```text
• C(X) = X8 + X2 + X1 + 1
```

The seed value for PEC function is all zeros.

When Host calculates PEC for PMIC device, it includes LID and HID bits followed by R/W bit.
