---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 2.10.7
title: Packet Error Check (PEC) Function
pages: 67-67
---
# 2.10.7 Packet Error Check (PEC) Function

In I2C mode, packet error checking is not supported. Only I3C Basic mode supports packet error checking. The PMIC device implement an 8-bit Packet Error Code (PEC) which is appended at the end of all transactions if PECs is enabled through DEVCTRL CCC or by directly writing ‘1’ to Table 142, “Register 0x34” [7]. The PEC is a CRC-8 value calculated on all the messages bytes except for START, STOP, REPEATED START conditions or T-bits, ACK and NACK and IBI header (7’h7E followed W=0) bits. The polynomial for CRC-8 calculations is:

```text
• C(X) = X8 + X2 + X1 + 1
```

The seed value for PEC function is all zero. When Host calculates PEC for PMIC device, it includes LID and HID bits followed by R/W bit.
