---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 2.10.5.1
title: Write Operation - Data Packet
pages: 50-52
---
# 2.10.5.1 Write Operation - Data Packet

**Table 35 — Write Command Data Packet; PEC Disabled**

```text
 Start       Bit 7      Bit 6      Bit 5      Bit 4         Bit 3   Bit 2     Bit 1      Bit 0      A/N/T          Stop
S or Sr        1          X          0          X                   HID                  W=0         A1,2,3
                                              Address [7:0]                                             T
                                                    Data                                                T
                                                      ...                                               T
                                                    Data                                                T        Sr4 or P
NOTE 1 See Figure 18 to see how the transition occurs from Target Open Drain (ACK) to Host Push Pull Operation (1st bit
       of Addr, bit [7]).
NOTE 2 The PMIC device NACKs if there is a parity error in a previous transaction when host performs consecutive
       transactions with Repeat Start.
NOTE 3 The PMIC device does not check for parity error in subsequent bytes when it determines the 7-bit device select code
       issued by the host does not match with its own device code. The PMIC device ignores the entire packet until STOP
       or next Repeat Start operation.
NOTE 4 Repeat Start or Repeat Start with 7’h7E.
```

**Table 36 — Write Command Data Packet; PEC Enabled**

```text
 Start       Bit 7      Bit 6      Bit 5      Bit 4         Bit 3   Bit 2     Bit 1      Bit 0      A/N/T          Stop

S or Sr        1          X          0          X                   HID                  W=0         A1,2,3
                                              Address [7:0]                                             T

                       CMD                    W=0                        0000                           T

                                                    Data                                                T
                                                      ...                                               T
                                                    Data                                                T
                                                    PEC                                                 T        Sr4 or P
NOTE 1 See Figure 18 to see how the transition occurs from Target Open Drain (ACK) to Host Push Pull Operation (1st bit
       of Addr, bit [7]).
NOTE 2 The PMIC device NACKs if there is a parity or PEC error in a previous transaction when host performs consecutive
       transactions with Repeat Start.
NOTE 3 The PMIC device does not check for parity or PEC error in subsequent bytes when it determines the 7-bit device
       select code issued by the host does not match with its own device code. The PMIC device ignores the entire packet
       until STOP or next Repeat Start operation.
NOTE 4 Repeat Start or Repeat Start with 7’h7E.
```

The host may optionally allow PMIC device to request IBI. For this case, the transactions to the PMIC device begin with the I3C host issuing a START condition followed by 7’h7E and then write bit. If PMIC device has a pending IBI, it transmits its 7-bit device select code followed by R=1. If PMIC device has no pending IBI, there is no action taken by PMIC. The Table 37 and Table 38 shows the I3C Basic bus write command data packet with optional IBI header for PEC disabled and PEC enabled case respectively. Note that in Table 38, PEC calculation does not include IBI header byte (7’h7E followed by W=0).

**Table 37 — Write Command Data Packet with IBI Header; No Pending IBI, PEC Disabled**

```text
Start        Bit 7   Bit 6      Bit 5      Bit 4         Bit 3   Bit 2      Bit 1      Bit 0      A/N/T         Stop
    S         1         1         1          1            1        1          0        W=0         A1,2
    Sr        1        X          0          X                   HID                   W=0        A2,3,4
                                           Address [7:0]                                             T
                                                 Data                                                T
                                                   ...                                               T
                                                 Data                                                T        Sr5 or P
NOTE 1 See Figure 18 to see how the transition occurs from Target Open Drain (ACK) to Host Push Pull Operation
       (Repeat Start)
NOTE 2 The PMIC device NACKs if there is a parity error in a previous transaction when host performs consecutive
       transactions with Repeat Start.
NOTE 3 See Figure 20 to see how the transition occurs from Host Push Pull Operation to Target Open Drain (ACK) and
       See Figure 18 to see how the transition occurs from Target Open Drain (ACK) to Host Push Pull Operation (1st
       bit of Addr, bit [7]).
NOTE 4 The PMIC device does not check for parity error in subsequent bytes when it determines the 7-bit device select
       code issued by the host does not match with its own device code. The PMIC device ignores the entire packet until
       STOP or next Repeat Start operation.
NOTE 5 Repeat Start or Repeat Start with 7’h7E.
```

**Table 38 — Write Command Data Packet with IBI Header; No Pending IBI, PEC Enabled**

```text
Start        Bit 7   Bit 6      Bit 5      Bit 4         Bit 3   Bit 2      Bit 1      Bit 0      A/N/T         Stop

    S         1         1         1          1            1        1          0        W=0         A1,2
    Sr        1        X          0          X                   HID                   W=0        A2,3,4
                                           Address [7:0]                                             T
                     CMD                   W=0                         0000                          T
                                                 Data                                                T
                                                   ...                                               T
                                                 Data                                                T
                                                 PEC                                                 T        Sr5 or P
NOTE 1 See Figure 18 to see how the transition occurs from Target Open Drain (ACK) to Host Push Pull Operation
       (Repeat Start)
NOTE 2 The PMIC device NACKs if there is a parity or PEC error in a previous transaction when host performs
       consecutive transactions with Repeat Start.
NOTE 3 See Figure 20 to see how the transition occurs from Host Push Pull Operation to Target Open Drain (ACK) and
       See Figure 18 to see how the transition occurs from Target Open Drain (ACK) to Host Push Pull Operation (1st
       bit of Addr, bit [7]).
NOTE 4 The PMIC device does not check for parity or PEC error in subsequent bytes when it determines the 7-bit device
       select code issued by the host does not match with its own device code. The PMIC device ignores the entire
       packet until STOP or next Repeat Start operation.
NOTE 5 Repeat Start or Repeat Start with 7’h7E.
```
