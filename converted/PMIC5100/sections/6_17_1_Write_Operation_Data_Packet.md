---
document: JESD301-2 (PMIC5100 Power Management IC Standard, Rev. 1.03, October 2022)
device: PMIC5100
application: client
section: 6.17.1
title: Write Operation Data Packet
pages: 65-67
---
# 6.17.1 Write Operation Data Packet

The PMIC device operate on a standard I3C Basic serial interface. Transactions where the PMIC device is the targeted target device begin with the I3C Basic Host issuing a START condition followed by a 7-bit PMIC device address then a read or write bit, RW. All data are transmitted with the most significant bit MSB first. During the address followed by R/W bit transmission, the PMIC device typically replies with an ACK unless there are exceptional conditions when it may passively assert a NACK. See Table 35, “Write Command Data Packet; PEC Disabled,”. The “T” bit carries Parity information from the host for each byte. The PMIC device host region registers that are write protected in secure mode of operation, the PMIC does not execute the operation internally. Similarly, regardless of secure mode or programmable mode of operation, without the correct password, all DIMM vendor region and vendor specific region registers are write protected and PMIC does not execute the operation internally. The Packet Error Code (PEC) function is disabled by default when the PMIC device is put in I3C Basic mode. The host may optionally enable this function through Table 140, “Register 0x34” [7] or DEVCTRL CCC. If enabled, the PEC is appended at the end of all transactions. If PEC is enabled, the host must complete the burst length as indicated in CMD field. In other words, the host must not interrupt the burst length pre-maturely for Write operation.

**Table 35 — Write Command Data Packet; PEC Disabled**

```text
 Start         Bit 7         Bit 6      Bit 5      Bit 4       Bit 3    Bit 2      Bit 1      Bit 0      A/N/T         Stop

S or Sr          1             X          0          X                   HID                  W=0         A1,2,3

           Address [7:0]                                                                                    T
                                                     Data                                                   T

                                                         ...                                                T
                                                     Data                                                   T         Sr4 or P
NOTE 1 See Figure 35 to see how the transition occurs from Target Open Drain (ACK) to Host Push Pull operation (Address bit 7).
NOTE 2 The PMIC device NACKs if there is a parity error in a previous transaction when host performs consecutive transactions
       with Repeat Start.
NOTE 3 The PMIC device does not check for parity error in subsequent bytes when it determines 7-bit device select code issued by
       the host does not match with its own device code. The PMIC device ignores the entire packet until STOP or next Repeat
       Start operation.
NOTE 4 Repeat Start or Repeat Start with 7’h7E.
```

**Table 36 — Write Command Data Packet; PEC Enabled**

```text
 Start         Bit 7         Bit 6      Bit 5     Bit 4        Bit 3    Bit 2      Bit 1      Bit 0      A/N/T         Stop
S or Sr          1             X          0         X                   HID                   W=0        A1,2,3
           Address [7:0]                                                                                    T
           CMD                                    W=0           0         0          0          0           T
                                                     Data                                                   T
                                                         ...                                                T
                                                     Data                                                   T
                                                     PEC                                                    T        Sr4 or P
NOTE 1 See Figure 35 to see how the transition occurs from Target Open Drain (ACK) to Host Push Pull operation (Address bit 7).
NOTE 2 The PMIC device NACKs if there is a parity or PEC error in a previous transaction when host performs consecutive
       transactions with Repeat Start.
NOTE 3 The PMIC device does not check for parity or PEC error in subsequent bytes when it determines 7-bit device select code
       issued by the host does not match with its own device code. The PMIC device ignores the entire packet until STOP or next
       Repeat Start operation.
NOTE 4 Repeat Start or Repeat Start with 7’h7E.
```

The host may optionally allow PMIC device to request IBI. For this case, the transactions to the PMIC device begin with the I3C Basic host issuing a START condition followed by 7’h7E and then write bit. If PMIC device has a pending IBI, it transmits its 7-bit device select code followed by R=1. If PMIC device has no pending IBI, there is no action taken by PMIC. The Table 37 and Table 38 shows the I3C Basic bus write command data packet with optional IBI header for PEC disabled and PEC enabled case, respectively. Note that in Table 38, PEC calculation does not include IBI header byte (7’h7E followed by W=0).

**Table 37 — Write Command Data Packet with IBI Header; PEC Disabled**

```text
Start         Bit 7         Bit 6      Bit 5     Bit 4        Bit 3    Bit 2      Bit 1      Bit 0      A/N/T         Stop
  S             1             1          1          1          1         1          0        W=0         A1,2
  Sr            1             X          0         X                   HID                   W=0        A2,3,4
           Address [7:0]                                                                                   T
                                                    Data                                                   T
                                                        ...                                                T
                                                    Data                                                   T        Sr5 or P
NOTE 1 See Figure 35 to see how the transition occurs from Target Open Drain (ACK) to Host Push Pull operation (Repeat
       Start).
NOTE 2 The PMIC device NACKs if there is a parity error in a previous transaction when host performs consecutive transactions
       with Repeat Start.
NOTE 3 See Figure 37 to see how the transition occurs from Host Push Pull Operation to Target Open Drain (ACK) and
       Figure 35 to see how the transition occurs from Target Open Drain (ACK) to Host Push Pull operation (Address bit 7).
NOTE 4 The PMIC device does not check for parity error in subsequent bytes when it determines 7-bit device select code issued
       by the host does not match with its own device code. The PMIC device ignores the entire packet until STOP or next
       Repeat Start operation.
NOTE 5 Repeat Start or Repeat Start with 7’h7E.
```

**Table 38 — Write Command Data Packet with IBI Header; PEC Enabled**

```text
Start         Bit 7         Bit 6      Bit 5     Bit 4        Bit 3    Bit 2      Bit 1      Bit 0      A/N/T         Stop
   S            1             1          1          1          1         1          0        W=0         A1,2
   Sr           1             X          0         X                   HID                   W=0        A2,3,4
                                               Address [7:0]                                               T
                        CMD                      W=0           0         0          0          0           T
                                                    Data                                                   T
                                                        ...                                                T
                                                    Data                                                   T
                                                    PEC                                                    T        Sr5 or P
NOTE 1 See Figure 35 to see how the transition occurs from Target Open Drain (ACK) to Host Push Pull operation (Repeat
       Start).
NOTE 2 The PMIC device NACKs if there is a parity or PEC error in a previous transaction when host performs consecutive
       transactions with Repeat Start.
NOTE 3 See Figure 37 to see how the transition occurs from Host Push Pull Operation to Target Open Drain (ACK) and
       Figure 35 to see how the transition occurs from Target Open Drain (ACK) to Host Push Pull operation (Address bit 7).
NOTE 4 The PMIC device does not check for parity or PEC error in subsequent bytes when it determines 7-bit device select code
       issued by the host does not match with its own device code. The PMIC device ignores the entire packet until STOP or
       next Repeat Start operation.
NOTE 5 Repeat Start or Repeat Start with 7’h7E.
```
