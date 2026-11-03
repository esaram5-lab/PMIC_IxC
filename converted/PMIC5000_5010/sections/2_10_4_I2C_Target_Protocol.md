---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 2.10.4
title: I2C Target Protocol
pages: 48-49
---
# 2.10.4 I2C Target Protocol

The PMIC device operate on a standard I2C serial interface. Transactions where the PMIC device is the targeted target device begin with the Host issuing a START condition followed by a 7-bit PMIC device address then a read or write bit, RW. All data are transmitted with the most significant bit MSB first. During the address followed by R/W bit transmission, the PMIC device typically replies with an ACK unless there are exceptional conditions when it may passively assert a NACK. The PMIC device host region registers that are write protected in write protect mode of operation, the PMIC ACKs the host request but the PMIC does not execute the operation internally. Similarly, regardless of write protect mode or non write protect mode of operation, without the correct password, all DIMM vendor and vendor specific region registers are write protected and PMIC ACKs the host request but the PMIC does not execute the operation internally. The PMIC device accepts 1 byte of address which covers 256 bytes of registers. The PMIC device register space does not require page selection process as all registers are within first 256 bytes.

## 2.10.4.1 Write Operation - Data Packet

**Table 32 — Write Command Data Packet**

```text
  Start         Bit 7       Bit 6      Bit 5      Bit 4     Bit 3       Bit 2      Bit 1      Bit 0      A/N        Stop
          1      1           X          0          X                    HID                   W=0         A
S or Sr
                                                  Address [7:0]                                           A
                                                       Data                                               A

                                                        ...                                               A
                                                       Data                                               A           P
                    2
  NOTE 1 In I C mode, Start or Repeat Start operation followed by 7’h7E with W=0 is only allowed for the purpose of

              issuing CCCs that are allowed in I2C mode. Any other operation including another Repeat Start is considered
              an illegal operation.
```

## 2.10.4.2 Read Operation - Data Packet

**Table 33 — Read Command Data Packet**

```text
   Start         Bit 7       Bit 6     Bit 5      Bit 4     Bit 3       Bit 2      Bit 1      Bit 0       A/N       Stop
           1      1           X         0          X                    HID                   W=0          A
 S or Sr
                                                  Address [7:0]                                            A
     Sr                  1    X          0         X                    HID                    R=1        A2
                                                       Data                                               A
                                                        ...                                               A
                                                       Data                                               N3          P
                 2
NOTE 1 In I C mode, Start or Repeat Start operation followed by 7’h7E with W=0 is only allowed for the purpose of
       issuing CCCs that are allowed in I2C mode. Any other operation including another Repeat Start is considered an
       illegal operation.
NOTE 2 If target device NACKs during Repeat Start for any reason, the host my re-try Repeat Start again. The host can
       do the Repeat Start as many times it may desire. The PMIC may eventually ACK.
NOTE 3 When PMIC device reaches last byte within the region (either Host region or DIMM vendor region), it will
       continue to return data but returned data will be 0x00 if there is no valid password for DIMM vendor region or
       Vendor specific region. Once the address counter reaches R255, it will reset to address R00 and it will continue
       to return the data. Only Host can perform STOP operation.
```

## 2.10.4.3 Default Read Address Pointer Mode

During normal operation of the DDR5 DIMM, the host periodically may poll critical information from the same location. An example may be the PMIC device’s status registers or current or power measurement register readout. To help improve the efficiency of the I2C bus protocol, the PMIC offers a default read address pointer mode so that whenever the PMIC device sees the STOP operation on its SCL and SDA bus, its read address pointer is always resets to default address. The default read pointer address mode is enabled through register Table 147, “Register 0x3A” [6] and default starting address for read operation is selectable through register Table 147, “Register 0x3A” [5:4]. This allows host to read the read command data packet as shown in Table 34. The default read address pointer reduces the packet overhead by 2 bytes. The host typically enables this mode at last after VR Enable command when the normal operation of the DDR5 DIMM begins.

**Table 34 — Read Command Data Packet with Default Address Pointer Mode**

```text
 Start       Bit 7      Bit 6      Bit 5      Bit 4         Bit 3   Bit 2       Bit 1      Bit 0      A/N        Stop
S or Sr        1          X           0         X                    HID                   R=1          A
                                                    Data                                                A
                                                      ...                                               A
                                                    Data                                               N1          P
NOTE 1 When PMIC device reaches last byte within the region (either Host region or DIMM vendor region), it will
       continue to return data but returned data will be 0x00 if there is no valid password for DIMM vendor region or
       Vendor specific region. Once the address counter reaches R255, it will reset to address R00 and it will continue
       to return the data. Only Host can perform STOP operation.
```
