---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 5
title: I2C and I3C Basic Operation
pages: 72-120
---
# 5 I2C and I3C Basic Operation

At power on, by default, the PMIC device comes up in I2C mode of operation. Following applies in I2C mode:

```text
1.   The max operation speed is limited to 1 MHz
1.   In-band interrupts are not supported
1.   Bus reset is supported.
1.   Parity check is not supported except for supported CCCs.
1.   Packet Error check is not supported.
```

The PMIC device shall operate in the I2C mode until put into I3C Basic mode via command. The host may put the PMIC device in I3C Basic mode by issuing SETAASA CCC. Following applies in I3C Basic mode.

```text
1.      The max operation speed is up to 12.5 MHz
2.      In-band interrupts are supported
3.      Bus reset is supported.
4.      Parity check is always enabled by default.
5.      Packet error check is supported and by default is disabled.
```

## Subsections

- [5.1 Device Interface - Protocol](5_1_Device_Interface_Protocol.md)
- [5.2 Configuration Register Addressing](5_2_Configuration_Register_Addressing.md)
- [5.3 I2C Target Protocol](5_3_I2C_Target_Protocol.md)
- [5.4 I3C Basic Target Protocol](5_4_I3C_Basic_Target_Protocol.md)
