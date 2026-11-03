---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 2.9
title: I2C and I3C Basic Interface Operation
pages: 46-46
---
# 2.9 I2C and I3C Basic Interface Operation

At power on, by default, the PMIC device comes up in legacy I2C mode of operation. Following applies in I2C mode:

```text
1.   The max operation speed is limited to 1 MHz
2.   In-band interrupts are not supported
3.   Bus reset is supported.
4.   Parity check is not supported except for supported CCCs.
5.   Packet Error check is not supported.
```

The PMIC device shall operate in the legacy I2C mode until put into I3C Basic mode via command. The host may put the PMIC device in I3C Basic mode by issuing SETAASA CCC. Following applies in I3C Basic mode.

```text
1.   The max operation speed is up to 12.5 MHz
2.   In-band interrupts are supported
3.   Bus reset is supported.
4.   Parity check is always enabled by default.
5.   Packet error check is supported and by default is disabled.
```
