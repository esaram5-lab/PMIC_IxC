---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 7
title: I2C and I3C Basic Interface Operation
pages: 62-114
---
# 7 I2C and I3C Basic Interface Operation

At power on, by default, the PMIC device comes up in legacy I2C mode of operation. Following applies in I2C mode:

1. The maximum operation speed is limited to 1 MHz

2. In-band interrupts are not supported

3. Bus reset is supported.

4. Parity check is not supported except for supported CCCs.

5. Packet Error check is not supported.

The PMIC device shall operate in the legacy I2C mode until put into I3C Basic mode via command. The host may put the PMIC device in I3C Basic mode by issuing SETAASA CCC. Following applies in I3C Basic mode.

1. The max operation speed is up to 12.5 MHz

2. In-band interrupts are supported

3. Bus reset is supported.

4. Parity check is always enabled by default.

5. Packet error check is supported and by default is disabled.

## Subsections

- [7.1 Device Interface - Protocol](7_1_Device_Interface_Protocol.md)
- [7.2 Configuration Register Addressing](7_2_Configuration_Register_Addressing.md)
- [7.3 I2C Target Protocol](7_3_I2C_Target_Protocol.md)
- [7.4 I3C Basic Target Protocol](7_4_I3C_Basic_Target_Protocol.md)
- [7.5 In Band Interrupt (IBI)](7_5_In_Band_Interrupt_IBI.md)
- [7.6 IO Operation](7_6_IO_Operation.md)
- [7.7 Bus Clear](7_7_Bus_Clear.md)
- [7.8 Bus Reset](7_8_Bus_Reset.md)
- [7.9 Command Truth Table](7_9_Command_Truth_Table.md)
