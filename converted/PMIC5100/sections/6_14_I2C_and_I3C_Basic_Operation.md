---
document: JESD301-2 (PMIC5100 Power Management IC Standard, Rev. 1.03, October 2022)
device: PMIC5100
application: client
section: 6.14
title: I2C and I3C Basic Operation
pages: 61-62
---
# 6.14 I2C and I3C Basic Operation

At power on, by default, the PMIC device comes up in I2C mode of operation. Following applies in I2C mode:

```text
1.   The max operation speed is limited to 1 MHz
2.   In-band interrupts are not supported
3.   Bus reset is supported.
4.   Parity check is not supported except for supported CCCs.
5.   Packet Error check is not supported.
```

The PMIC device shall operate in the I2C mode until put into I3C Basic mode via command. The host may put the PMIC device in I3C Basic mode by issuing SETAASA CCC. Following applies in I3C Basic mode.

```text
1. The max operation speed is up to 12.5 MHz
2. In-band interrupts are supported
3. Bus reset is supported.
4. Parity check is always enabled by default.
5. Packet error check is supported and by default is disabled.
```
