---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 5.4.10.8
title: DEVCTRL CCC
pages: 111-117
---
# 5.4.10.8 DEVCTRL CCC

On a typical I3C bus, there can be up to 120 devices. For CAMM2 application environment, there are up to 8 SPD5 Hub devices and behind each SPD5 Hub devices, there are 4 local target devices totaling up to 40 or more devices on I3C Basic bus. For certain operations such as enable or disable functions that are common to all devices (i.e., Packet Error Check), the host must go through one device at a time, which takes significant amount of time at initial power up. Further, it requires additional complexity on the host because it must speak different protocol depending on how it may access the device until all devices are configured identically. To help expedite this configuration operation and to simplify the host complexity, the device supports the DEVCTRL CCC. The DEVCTRL CCC is supported in either I2C mode or I3C Basic mode of operation. In

I2C mode, when host issues this CCC, to guarantee that this CCC is registered by the device without any error, the host shall limit the maximum speed of operation for this CCC to 1 MHz.

If PEC function is enabled, the PEC calculation starts with Start or Repeat Start operation but does not include 7’h7E with W=0 byte in PEC calculation.

The host must pay attention to DEVCTRL CCC. If DEVCTRL CCC is used to access device specific registers (i.e., RegMod = ‘1’), the host must still follow any device register restrictions. For instance, if any device specific register, such as IO timing parameter related register requires STOP operation for device to take in the effect of the setting, the host must also use STOP operation when using DEVCTRL CCC to access device specific register. There are additional restrictions that host must pay attention to:

```text
• DEVCTRL CCC must be followed by STOP operation before starting a device specific register
  access. In other words, host shall avoid DEVCTRL CCC followed by Repeat Start to do a device
  specific register operation. Note that host is allowed to do multiple DEVCTRL CCC with Repeat
  Start in between to the same device or across multiple devices.
• DEVCTRL CCC must be followed by STOP operation before starting Default Read Address
  Pointer Mode even across different devices.
```

**Table 88 — DEVCTRL CCC - Broadcast**

```text
    Start         Bit 7       Bit 6       Bit 5        Bit 4         Bit 3     Bit 2       Bit 1        Bit 0        A/N/T         Stop
   S or Sr          1           1           1            1            1          1           0           W=0          A[1]
                                                       0x62 (Broadcast)                                                T
                          AddrMask[2:0]                StartOffset[1:0]          PEC BL[1:0]          RegMod           T
                                                   DevID[6:0]                                              0          T[2]
                                                     Byte 0 Data Payload                                               T
                                                     Byte 1 Data Payload                                               T
                                                     Byte 2 Data Payload                                               T
                                                     Byte 3 Data Payload                                               T        Sr[3] or P
NOTE 1 The PMIC device NACKs if there is a parity error in a previous transaction when host performs consecutive transactions
       with Repeat Start.
NOTE 2 An exception is made for DEVCTRL CCC where device does report a parity error when it determines the 7-bit device
       select code issued by the host does not match with its own device select code. If 7-bit device select code does not match
       but if parity is still valid, the device does not check for parity error in subsequent bytes; ignores the entire packet and
       waits until STOP or next Repeat Start operation.
NOTE 3 Repeat Start or Repeat Start with 7’h7E.
```

**Table 89 — DEVCTRL CCC - Broadcast with PEC**

```text
    Start         Bit 7       Bit 6       Bit 5        Bit 4         Bit 3     Bit 2        Bit 1       Bit 0        A/N/T        Stop

   S or Sr          1           1           1            1            1          1            0          W=0          A[1]
                                                       0x62 (Broadcast)                                                T
                          AddrMask[2:0]                StartOffset[1:0]          PEC BL[1:0]          RegMod           T
                                                   DevID[6:0]                                             0           T[2]
                                                     Byte 0 Data Payload                                               T
                                                     Byte 1 Data Payload                                               T
                                                     Byte 2 Data Payload                                               T
                                                     Byte 3 Data Payload                                               T
                                                               PEC                                                     T        Sr[3] or P
NOTE 1 The PMIC device NACKs if there is a parity or PEC error in a previous transaction when host performs consecutive
       transactions with Repeat Start.
NOTE 2 An exception is made for DEVCTRL CCC where device does report a parity error when it determines the 7-bit device
       select code issued by the host does not match with its own device select code. The device does not check for PEC as
       all subsequent bytes are discarded due to parity error. If 7-bit device select code does not match but if parity is still valid,
       the device does not check for parity error in subsequent bytes; ignores the entire packet and waits until STOP or next
       Repeat Start operation.
NOTE 3 Repeat Start or Repeat Start with 7’h7E.
```

**Table 90 — DEVCTRL CCC Command Definition**

```text
  Parameter                                                   Definition
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
                    operation.

                    00 = Byte 0
                    01 = Byte 1
                    10 = Byte 2
                    11 = Byte 3

 PEC BL[1:0]        Only applicable if RegMod = ‘0’ and PEC function is enabled.
                    Identifies the burst length just for this DEVCTRL CCC. The device uses the setting in this

                    field to know when the PEC byte is expected after the data bytes.

                    00 = 1 Byte
                    01 = 2 Byte
                    10 = 3 Byte
                    11 = 4 Byte
   RegMod           Identifies if DEVCTRL is going to be used for General Registers as identified in Byte 0 to Byte
                    3 or device specific address offset register.

                    0 = Access to General Registers in Byte 0 to Byte 3 (i.e., StartOffset[1:0] = Valid)
                    1 = Device Specific Offset Address (i.e., StartOffset[1:0] and PECBL[1:0] is a don’t care and
                    does not apply). The Host shall NOT use RegMod = ‘1’ with Broadcast Command if there are
                    different types of devices on the I3C Basic bus.
  DevID[6:0]        Identifies 7-bit device address. Device responds to DEVCTRL CCC data packet depending
                    on AddrMask[2:0].

                    If AddrMask[2:0] = ‘111’, DevID[6:0] is a don’t care and device always responds.
                    If AddrMask[2:0] = ‘000’, DevID[6:0] must match for device to respond
                    If AddrMask[2:0] = ‘011’, DevID[6:3] must match for device to respond. DevID[2:0] is don’t
                    care.
                    For any other codes for AddrMask[2:0], the device always NACKs.
```

**Table 91 — DEVCTRL CCC Data Payload Definition**

```text
   Byte #      Bit #      Function                       Definition                                           Comment
   Byte 0       [7]         PEC          0 = Disable                                     Table 156, Register 0x34 [7] is updated
                           Enable        1 = Enable
                [6]         Parity       0 = Enable                                         Table 156, Register 0x34 [5] is updated
                           Disable       1 = Disable
               [5:2]         RFU         RFU
                [1]      VR Enable       0 = VR Disable                                  Table 154, Register 0x32 [7] is updated
                                         1 = VR Enable                                   Only PMIC device responds to this bit. All
                                                                                         other device ignore this bit.
                [0]          RFU         RFU
   Byte 1      [7:4]         RFU         RFU
                [3]       Global &       0 = No Action                                   Table 124, Register 0x14 [0] is updated.
                          IBI Clear      1 = Clear All Event and pending IBI[1]
               [2:0]         RFU         RFU
   Byte 2      [7:0]         RFU         RFU
   Byte 3      [7:0]         RFU         RFU
NOTE 1 After target device clears the event, the device can still have certain registers set to ‘1’ if the event is still present in
       which case, the device will generate an IBI again at the next opportunity.
```

## Subsections

- [5.4.10.8.1 DEVCTRL CCC Examples - RegMod = ‘0’](5_4_10_8_1_DEVCTRL_CCC_Examples_RegMod_0.md)
- [5.4.10.8.2 DEVCTRL CCC Examples - RegMod = ‘1’](5_4_10_8_2_DEVCTRL_CCC_Examples_RegMod_1.md)
