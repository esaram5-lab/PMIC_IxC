---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 7.5.10.8
title: DEVCTRL CCC
pages: 105-111
---
# 7.5.10.8 DEVCTRL CCC

On a typical I3C Basic bus there can be up to 120 devices. For DDR5 DIMM application environment, there are up to 8 SPD5 Hub devices and behind each SPD5 Hub devices, there are 4 local target devices totaling up to 40 or more devices on I3C Basic bus. For certain operations such as enable or disable functions that are common to all devices (i.e., Packet Error Check), the host must go through one device at a time which takes significant amount of time at initial power up. Further, it requires additional complexity on the host because it must speak different protocol depending on how it may access the device until all devices are configured identically.

To help expedite this configuration operation and to simplify the host complexity, the device supports the DEVCTRL CCC. The DEVCTRL CCC is supported either in I2C mode or I3C Basic mode of operation. In

I2C mode, when host issues this CCC, to guarantee that this CCC is registered by the device without any error, the host shall limit the maximum speed operation for this CCC to 1 MHz. Table 89 through Table 90 show an example of a single DEVCTRL CCC. In I3C mode only, if PEC function is enabled, the PEC calculation starts with Start or Repeat Start operation but does not include 7’h7E with W=0 byte in PEC calculation. The host shall pay attention to DEVCTRL CCC. If DEVCTRL CCC is used to access device specific registers (e.g., RegMod = ‘1’), the host shall still follow any device specific register restriction. For example, if device specific register requires STOP operation for device to take in the effect of the setting, the host must also use STOP operation when using DEVCTRL CCC to access device specific register.

**Table 89 — DEVCTRL CCC - Broadcast**

```text
 Start    Bit 7        Bit 6        Bit 5        Bit 4         Bit 3        Bit 2        Bit 1         Bit 0        A/N/T        Stop

S or Sr    1             1            1            1             1            1            0           W=0           A[1]

                                                 0x62 (Broadcast)                                                     T

                   AddrMask[2:0]                  StartOffset[1:0]            PEC BL[1:0]            RegMod           T

                                              DevID[6:0]                                                 0           T[2]

                                               Byte 0 Data Payload                                                    T

                                               Byte 1 Data Payload                                                    T

                                               Byte 2 Data Payload                                                    T

                                               Byte 3 Data Payload                                                    T        Sr[3] or P
 NOTE 1   The PMIC NACKs if there is a parity or PEC error in a previous transaction when host performs consecutive transactions
          with Repeat Start.
 NOTE 2   An exception is made for DEVCTRL CCC. The PMIC does not report parity error when it determines 7-bit device select
          code issues by the host does not match with its own device code. If 7-bit device select code does not match but if parity
          is still valid, the device does not check for parity error in subsequent bytes; ignores the entire packet and waits until STOP
          or Repeat Start operation.
 NOTE 3   Repeat Start or Repeat Start with 7’h7E.
```

**Table 90 — DEVCTRL CCC - Broadcast with PEC[1]**

```text
 Start    Bit 7        Bit 6        Bit 5        Bit 4         Bit 3        Bit 2        Bit 1         Bit 0        A/N/T        Stop

S or Sr    1             1            1            1             1            1            0           W=0           A[2]

                                                 0x62 (Broadcast)                                                     T

                   AddrMask[2:0]                  StartOffset[1:0]            PEC BL[1:0]            RegMod           T

                                              DevID[6:0]                                                 0           T[3]

                                               Byte 0 Data Payload                                                    T

                                               Byte 1 Data Payload                                                    T

                                               Byte 2 Data Payload                                                    T

                                               Byte 3 Data Payload                                                    T

                                                         PEC                                                          T        Sr[4] or P
 NOTE 1   DEVCTRL CCC with PEC check is only supported in I3C mode.
 NOTE 2   The PMIC NACKs if there is a parity or PEC error in a previous transaction when host performs consecutive transactions
          with Repeat Start.
 NOTE 3   An exception is made for DEVCTRL CCC. The PMIC does not report parity error when it determines 7-bit device select
          code issues by the host does not match with its own device code. The device does not check for PEC as all subsequent
          bytes are discarded due to parity error. If 7-bit device select code does not match but if parity is still valid, the device does
          not check for parity error in subsequent bytes; ignores the entire packet and waits until STOP or Repeat Start operation.
 NOTE 4   Repeat Start or Repeat Start with 7’h7E.
```

**Table 91 — DEVCTRL CCC Command Definition**

```text
  Parameter                                                    Definition

AddrMask[2:0]       Broadcast, Unicast or Multicast Command Selection

                    000 = Unicast Command; PMIC device responds if DevID[6:0] field matches with PMIC
                    device’s own 7-bit address (4-bit LID + 3-bit HID)
                    011 = Multicast Command; PMIC device and possible other device responds if DevID[6:3]
                    field matches with PMIC device’s own 4-bit LID address
                    111 = Broadcast Command; All devices respond to this command
                    All other encodings are reserved

StartOffset[1:0]    Only applicable if RegMod = ‘0’
                    Identifies the starting Byte (Byte 0 or Byte 1 or Byte 2 or Byte 3) for DEVCTRL CCC. Host can
                    start at any Byte (from Byte 0 to Byte 3) and has continuous access to next byte until STOP
                    operation. If Byte 3 is reached, the host is responsible for applying STOP operation.

                    00 = Byte 0
                    01 = Byte 1
                    10 = Byte 2
                    11 = Byte 3

 PEC BL[1:0]        Only applicable if RegMod = ‘0’ and PEC function is enabled.

                    Identifies the burst length just for this DEVCTRL CCC. The device uses the setting in this field
                    to know when the PEC byte is expected after the data bytes.

                    00 = 1 Byte

                    01 = 2 Byte
                    10 = 3 Byte
                    11 = 4 Byte

   RegMod           Identifies if DEVCTRL is going to be used for General Registers as identified in Byte 0 to Byte
                    3 or device specific address offset register.

                    0 = Access to General Registers in Byte 0 to Byte 3 (i.e., StartOffset[1:0] = Valid)
                    1 = Device Specific Offset Address (i.e., StartOffset[1:0] & PECBL[1:0] is a don’t care and
                    does not apply). The Host shall NOT use RegMod = ‘1’ with Broadcast Command if there are
                    different types of devices on the I3C Basic bus.

  DevID[6:0]        Identifies 7-bit device address. Device responds to DEVCTRL CCC data packet depending on
                    AddrMask[2:0].

                    If AddrMask[2:0] = ‘111’, DevID[6:0] is a don’t care and device always responds.
                    If AddrMask[2:0] = ‘000’, DevID[6:0] must match for device to respond
                    If AddrMask[2:0] = ‘011’, DevID[6:3] must match for device to respond. DevID[2:0] is don’t
                    care.
                    For any other codes for AddrMask[2:0], the device always NACKs.
```

**Table 92 — DEVCTRL CCC Data Payload Definition**

```text
Byte #     Bit #      Function                            Definition                                      Comment

Byte 0         [7]       PEC                              0 = Disable                     Table 158, Register 0x34 [7] is updated
                        Enable                            1 = Enable

               [6]      Parity                            0 = Enable                      Table 158, Register 0x34 [5] is updated
                       Disable                            1 = Disable

            [5:2]        RFU                                 RFU

               [1]    VR Enable                      0 = VR Disable                       Table 155, Register 0x32 [7] is updated.
                                                        1 = VR Enable

               [0]       RFU                                 RFU

Byte 1      [7:4]        RFU                                 RFU

               [3]     Global &                         0 = No Action                     Table 125, Register 0x14 [0] is updated.
                       IBI Clear          1 = Clear All Event and pending IBI[1]

            [2:0]        RFU                                 RFU

Byte 2      [7:0]        RFU                                 RFU
Byte 3      [7:0]        RFU                                 RFU
 NOTE 1     After target device clears the event, the device can still have certain registers set to ‘1’ if the event is still present, in

            which case, the device will generate an IBI again at the next opportunity.
```

## Subsections

- [7.5.10.8.1 DEVCTRL CCC Examples - RegMod = ‘0’](7_5_10_8_1_DEVCTRL_CCC_Examples_RegMod_0.md)
- [7.5.10.8.2 DEVCTRL CCC Examples - RegMod = ‘1’](7_5_10_8_2_DEVCTRL_CCC_Examples_RegMod_1.md)
