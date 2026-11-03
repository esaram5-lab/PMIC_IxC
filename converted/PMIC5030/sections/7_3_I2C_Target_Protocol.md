---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 7.3
title: I2C Target Protocol
pages: 64-66
---
# 7.3 I2C Target Protocol

The PMIC device operates on a standard I2C serial interface. Transactions where the PMIC device is the targeted target device begin with the Host issuing a START condition followed by a 7-bit PMIC device address then a read or write bit, RW. All data are transmitted with the most significant bit MSB first. During the address followed by R/W bit transmission, the PMIC device typically replies with an ACK unless there are exceptional conditions when it may passively assert a NACK. The PMIC device host region registers that are write-protected in write-protect mode of operation, the PMIC ACKs the host request but the PMIC does not execute the operation internally. Similarly, regardless of write-protect mode or non write-protect mode of operation, without the correct password, all DIMM vendor and vendor specific region registers are write-protected and PMIC ACKs the host request but the PMIC does not execute the operation internally. The PMIC device accepts 1 byte of address which covers 256 bytes of registers. The PMIC device register space does not require page selection process as all registers are within first 256 bytes.

## 7.3.1 Write Operation - Data Packet

The PMIC supports Byte Write or Block Write operation as shown in Table 36 and Table 37 for one byte and two byte address mode respectively. For Byte Write operation, only one data byte is transferred followed by Stop operation.

**Table 36 — Write Command Data Packet; 1 Byte Address Mode**

```text
  Start        Bit 7      Bit 6     Bit 5     Bit 4          Bit 3   Bit 2    Bit 1    Bit 0      A/N       Stop

S or Sr[1]         1         X        0         X                     HID              W=0         A

                                               Address [7:0]                                       A

                                                     Data                                          A

                                                       ...                                         A

                                                     Data                                          A          P
  NOTE 1        In I2C mode, Start or Repeat Start operation followed by 7’h7E with W=0 is only allowed for the
                purpose of issuing CCCs that are allowed in I2C mode. Any other operation including another Repeat
                Start is considered an illegal operation; the PMIC may ignore it and still ACK or it may NACK.
```

**Table 37 — Write Command Data Packet; 2 Byte Address Mode**

```text
  Start           Bit 7        Bit 6      Bit 5     Bit 4         Bit 3    Bit 2   Bit 1     Bit 0       A/N/T           Stop
S or Sr[1]          1             X        0          X                    HID               W=0            A
                                                  Address [7:0]                                             A
                    0         0            0          0                   Address [11:8]                    A

                                                      Data                                                  A
                                                      Data                                                  A
                                                          ...                                               A
                                                      Data                                                  A           Sr or P
  NOTE 1       In I2C mode, Start or Repeat Start operation followed by 7’h7E with W=0 is only allowed for the purpose of issuing
               CCCs that are allowed in I2C mode. Any other operation including another Repeat Start is considered an illegal
               operation; the PMIC may ignore it and still ACK or it may NACK.
```

## 7.3.2 Read Operation - Data Packet

The PMIC supports Byte Read or Block Read operation as shown in Table 38 and Table 39 for one byte and two address mode respectively. For Byte Read operation, only one data byte is transferred followed by Stop operation.

**Table 38 — Read Command Data Packet; 1 Byte Address Mode**

```text
    Start         Bit 7     Bit 6      Bit 5     Bit 4          Bit 3   Bit 2    Bit 1      Bit 0      A/N       Stop

S or Sr[1]            1         X          0       X                     HID                W=0         A

                                                  Address [7:0]                                         A

     Sr               1         X          0       X                     HID                R=1        A[2]

                                                        Data                                            A

                                                          ...                                           A

                                                        Data                                           N[3]        P
    NOTE 1        In I2C mode, Start or Repeat Start operation followed by 7’h7E with W=0 is only allowed for the
                  purpose of issuing CCCs that are allowed in I2C mode. Any other operation including another Repeat
                  Start is considered an illegal operation; the PMIC may ignore it and still ACK or it may NACK.
    NOTE 2        If target device NACKs during Repeat Start for any reason, the host my re-try Repeat Start again.
                  The host can do the Repeat Start as many times it may desire. The PMIC may eventually ACK.
    NOTE 3        When PMIC device reaches last byte within the region (either Host region or DIMM vendor region),
                  it will continue to return data but returned data will be 0x00 if there is no valid password for DIMM
                  vendor region or Vendor specific region. Once the address counter reaches 0x1FF, it will reset to

                  address 0x00 and it will continue to return the data. Only Host can perform STOP operation.
```

**Table 39 — Read Command Data Packet; 2 Byte Address Mode**

```text
  Start              Bit 7        Bit 6     Bit 5      Bit 4         Bit 3    Bit 2    Bit 1      Bit 0        A/N            Stop
S or Sr[1]             1             X          0        X                    HID                 W=0            A
                                                     Address [7:0]                                               A
                       0         0          0            0                   Address [11:8]                      A

    Sr                 1             X          0        X                    HID                 R=1          A[2]
                                                          Data                                                   A
                                                          Data                                                   A
                                                             ...                                                 A
                                                          Data                                                 N[3]          Sr or P
 NOTE 1          In I2C mode, Start or Repeat Start operation followed by 7’h7E with W=0 is only allowed for the purpose of issuing
                 CCCs that are allowed in I2C mode. Any other operation including another Repeat Start is considered an illegal
                 operation; the PMIC may ignore it and still ACK or it may NACK.
 NOTE 2          If the PMIC NACKs during Repeat Start for any reason, the host may re-try Repeat Start again. The host can do the
                 Repeat Start as many times it may desire. The PMIC may eventually ACK.
 NOTE 3          When PMIC device reaches last byte within the region (either Host region or DIMM vendor region), it will continue
                 to return data but returned data will be 0x00 if there is no valid password for DIMM vendor region or Vendor specific
                 region. Once the address counter reaches 0x1FF, it will reset to address 0x00 and it will continue to return the data.
                 Only Host can perform STOP operation.
```

## 7.3.3 Default Read Address Pointer Mode

During normal operation of the DDR5 DIMM, the host periodically may poll critical information from the same location. An example may be the PMIC device’s status registers or current or power measurement register readout. To help improve the efficiency of the I2C bus protocol, the PMIC offers a default read address pointer mode so that whenever the PMIC device sees the STOP operation on its SCL and SDA bus, its read address pointer is always resets to default address. The default read pointer address mode is enabled through register Table 163, Register 0x3A [6] and default starting address for read operation is selectable through register Table 163, Register 0x3A [5:4]. This allows host to read the read command data packet as shown in Table 40. The default read address pointer reduces the packet overhead by 2 bytes. The host typically enables this mode at last after VR Enable command when the normal operation of the DDR5 DIMM begins.

**Table 40 — Read Command Data Packet with Default Address Pointer Mode**

```text
 Start      Bit 7      Bit 6     Bit 5     Bit 4         Bit 3   Bit 2     Bit 1     Bit 0      A/N       Stop

S or Sr       1         X          0         X                   HID                  R=1         A

                                                 Data                                             A

                                                   ...                                            A

                                                 Data                                           N[1]        P
 NOTE 1      When PMIC device reaches last byte within the region (either Host region or DIMM vendor region),
             it will continue to return data but returned data will be 0x00 if there is no valid password for DIMM
             vendor region or Vendor specific region. Once the address counter reaches 0x1FF, it will reset to

             address 0x00 and it will continue to return the data. Only Host can perform STOP operation.
```
