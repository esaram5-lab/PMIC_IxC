---
document: JESD301-6 (PMIC5120 Power Management IC Standard, Version 1.0, February 2025)
device: PMIC5120
application: client
section: 6.15
title: I2C and I3C Basic Operation
pages: 66-66
---
# 6.15 I2C and I3C Basic Operation

At power on, by default, the PMIC device comes up in legacy I2C mode of operation. Following applies in I2C mode:

```text
1.   The max operation speed is limited to 1 MHz
2.   In-band interrupts are not supported
3.   Bus reset is supported.
4.   Parity check is not supported except for supported CCCs.
5.   Packet Error check is not supported.
```

The PMIC device shall operate in the legacy I2C mode until put into I3C Basic mode via command.

The host may put the PMIC device in I3C Basic mode by issuing SETAASA CCC.

Following applies in I3C Basic mode.

```text
1.   The max operation speed is up to 12.5 MHz
2.   In-band interrupts are supported
3.   Bus reset is supported.
4.   Parity check is always enabled by default.
5.   Packet error check is supported and by default is disabled.
```
