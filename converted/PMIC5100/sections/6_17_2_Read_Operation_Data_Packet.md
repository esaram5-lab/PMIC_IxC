---
document: JESD301-2 (PMIC5100 Power Management IC Standard, Rev. 1.03, October 2022)
device: PMIC5100
application: client
section: 6.17.2
title: Read Operation Data Packet
pages: 67-71
---
# 6.17.2 Read Operation Data Packet

The PMIC device operate on a standard I3C Basic serial interface. Transactions where the PMIC device is the targeted target device begin with the I3C Basic Host issuing a START condition followed by a 7-bit PMIC device address then a read or write bit, RW. All data are transmitted with the most significant bit MSB first. During the address followed by R/W bit transmission, the PMIC device typically replies with an ACK unless there are exceptional conditions when it may passively assert a NACK. See Table 35. The “T” bit carries Parity information from the host for each byte prior to Repeat START. After Repeat START, “T” bit carries information from PMIC device to Host indicating Continuous (‘1’) or Stop (‘0’) whether it is transmitting the last byte or not. The Packet Error Code (PEC) function is disabled by default when PMIC device is put in I3C Basic mode. The host may optionally enable this function through Table 140, “Register 0x34” [7] or DEVCTRL CCC. If enabled, the PEC is appended as shown in Table . If PEC is enabled, the host must complete the burst length as indicated in CMD field. In other words, the host must not interrupt the burst length pre-maturely for Read operation.

**Table 39 — Read Command Data Packet; PEC Disabled**

```text
 Start         Bit 7         Bit 6      Bit 5      Bit 4       Bit 3    Bit 2      Bit 1      Bit 0      A/N/T         Stop
S or Sr          1             X          0          X                   HID                  W=0         A1,2,3
                                                Address [7:0]                                               T
   Sr            1             X          0          X                   HID                   R=1       A/N4,5
                                                     Data                                                  T=1
                                                         ...                                               T=1
                                                     Data                                                T=16,7       Sr8 or P
NOTE 1 See Figure 35 to see how the transition occurs from Target Open Drain (ACK) to Host Push Pull operation (Address bit 7).
NOTE 2 The PMIC device NACKs if there is a parity error in a previous transaction when host performs consecutive transactions
       with Repeat Start.
NOTE 3 The PMIC device does not check for parity error in subsequent bytes when it determines 7-bit device select code issued by
       the host does not match with its own device code. The PMIC device ignores the entire packet until STOP or next Repeat
       Start operation.
NOTE 4 If PMIC device NACKs during Repeat Start for any reason, the host may re-try Repeat Start again. The host can do the
       Repeat Start as many times it may desire. If PMIC device NACKs due to parity error, it will always NACK regardless of
       how many times the host tries Repeat Start. If there were no parity errors, the device may eventually ACK.
NOTE 5 See Figure 37 to see how the transition occurs from Host Push Pull Operation to Target Open Drain (ACK).
NOTE 6 See Figure 38 to see how Host ends target device operation.
NOTE 7 When PMIC device reaches last byte within the region (either Host region or DIMM Vendor region), it will continue to
       return data but returned data will be 0x00 if there is no valid password for DIMM Vendor region or Vendor Specific

       region. Once the address counter reaches R255, it will reset to address R00 and it will continue to return the data. Only
       host can perform the STOP operation.
NOTE 8 Repeat Start or Repeat Start with 7’h7E.
```

**Table 40 — Read Command Data Packet; PEC Enabled**

```text
 Start         Bit 7         Bit 6      Bit 5      Bit 4       Bit 3     Bit 2      Bit 1      Bit 0      A/N/T         Stop
S or Sr           1            X          0          X                   HID                   W=0        A1,2,3
                                                Address [7:0]                                                T
                          CMD                      R=1          0          0          0          0           T
                                                      PEC                                                    T
   Sr             1            X          0          X                   HID                   R=1        A/N4,5
                                                      Data                                                 T=1
                                                         ...                                               T=1
                                                      Data                                                 T=1
                                                      PEC                                                  T=06       Sr7 or P
NOTE 1 See Figure 35 to see how the transition occurs from Target Open Drain (ACK) to Host Push Pull operation (Address bit 7).
NOTE 2 The PMIC device NACKs if there is a parity or PEC error in a previous transaction when host performs consecutive
       transactions with Repeat Start.
NOTE 3 The PMIC device does not check for parity or PEC error in subsequent bytes when it determines 7-bit device select code
       issued by the host does not match with its own device code. The PMIC device ignores the entire packet until STOP or next
       Repeat Start operation.
NOTE 4 If PMIC device NACKs during Repeat Start for any reason, the host may re-try Repeat Start again. The host can do the
       Repeat Start as many times it may desire. If PMIC device NACKs due to PEC error or parity error, it will always NACK

       regardless of how many times the Host tries Repeat Start. If there were no parity or PEC errors, the device may eventually
       ACK.The PEC calculation by the PMIC device only includes device select code of the ACK response of the Repeat Start
       operation. In other words, if there are more than one Repeat Start operation, the PMIC device includes device select of

       only the last Repeat Start from the host when it ACKs in PEC calculation and all other NACK responses of the device
       select code of the Repeat Start are not included in PEC calculation.

NOTE 5 See Figure 37 to see how the transition occurs from Host Push Pull Operation to Target Open Drain (ACK).
NOTE 6 See Figure 39 to see how Host ends target device operation followed by Host STOP operation.
NOTE 7 Repeat Start or Repeat Start with 7’h7E.
```

The host may optionally allow PMIC device to request IBI. For this case, the transactions to the PMIC device begin with the I3C Basic host issuing a START condition followed by 7’h7E and then write bit. If PMIC device has a pending IBI, it transmits its 7-bit device select code followed by R=1. If PMIC device has no pending IBI, there is no action taken by PMIC. Table 41 and Table 42 show the I3C Basic bus read command data packet with optional IBI header for PEC disabled and PEC enabled case respectively. Note that in Table 42, PEC calculation (from Host to PMIC) does not include IBI header byte (7’h7E followed by W=0).

**Table 41 — Read Command Data Packet with IBI Header; PEC Disabled**

```text
 Start         Bit 7         Bit 6      Bit 5      Bit 4       Bit 3    Bit 2      Bit 1      Bit 0      A/N/T         Stop
   S             1             1          1          1          1          1          0       W=0          A1,2
   Sr            1             X          0          X                   HID                  W=0         A2,3,4
                                                Address [7:0]                                               T
   Sr            1             X          0          X                   HID                   R=1       A/N5,6
                                                     Data                                                  T=1
                                                         ...                                               T=1
                                                     Data                                                T=17,8       Sr9 or P
NOTE 1 See Figure 35 to see how the transition occurs from Target Open Drain (ACK) to Host Push Pull operation (Repeat Start).
NOTE 2 The PMIC device NACKs if there is a parity error in a previous transaction when host performs consecutive transactions
       with Repeat Start.
NOTE 3 See Figure 37 to see how the transition occurs from Host Push Pull Operation to Target Open Drain (ACK) and Figure 35
       to see how the transition occurs from Target Open Drain (ACK) to Host Push Pull operation (Address bit 7).
NOTE 4 The PMIC device does not check for parity or PEC error in subsequent bytes when it determines 7-bit device select code
       issued by the host does not match with its own device code. The PMIC device ignores the entire packet until STOP or next
       Repeat Start operation.
NOTE 5 See Figure 37 to see how the transition occurs from Host Push Pull Operation to Target Open Drain (ACK).
NOTE 6 If PMIC device NACKs during Repeat Start for any reason, the host may re-try Repeat Start again. The host can do the
       Repeat Start as many times it may desire. If PMIC device NACKs due to parity error, it will always NACK regardless of

       how many times the host tries Repeat Start. If there were no parity errors, the device may eventually ACK.
NOTE 7 See Figure 38 to see how Host ends target device operation.
NOTE 8 When PMIC device reaches last byte within the region (either Host region or DIMM Vendor region), it will continue to

       return data but returned data will be 0x00 if there is no valid password for DIMM Vendor region or Vendor Specific
       region. Once the address counter reaches R255, it will reset to address R00 and it will continue to return the data. Only

       host can perform the STOP operation.
NOTE 9 Repeat Start or Repeat Start with 7’h7E.
```

**Table 42 — Read Command Data Packet with IBI Header; PEC Enabled**

```text
 Start         Bit 7         Bit 6      Bit 5      Bit 4       Bit 3     Bit 2      Bit 1      Bit 0      A/N/T         Stop
    S             1            1          1          1          1          1          0        W=0         A1,2
    Sr            1            X          0          X                   HID                   W=0        A2,3,4
                                                Address [7:0]                                                T
                          CMD                      R=1          0          0          0          0           T
                                                      PEC                                                    T
    Sr            1            X          0          X                   HID                   R=1        A/N5,6
                                                      Data                                                 T=1
                                                         ...                                               T=1
                                                      Data                                                 T=1
                                                      PEC                                                  T=07       Sr8 or P
NOTE 1 See Figure 35 to see how the transition occurs from Target Open Drain (ACK) to Host Push Pull operation (Repeat Start).
NOTE 2 The PMIC device NACKs if there is a parity or PEC error in a previous transaction when host performs consecutive
       transactions with Repeat Start.
NOTE 3 The PMIC device does not check for parity or PEC error in subsequent bytes when it determines 7-bit device select code
       issued by the host does not match with its own device code. The PMIC device ignores the entire packet until STOP or next
       Repeat Start operation.
NOTE 4 See Figure 37 to see how the transition occurs from Host Push Pull Operation to Target Open Drain (ACK) and Figure 35

       to see how the transition occurs from Target Open Drain (ACK) to Host Push Pull operation (Address bit 7).
NOTE 5 See Figure 37 to see how the transition occurs from Host Push Pull Operation to Target Open Drain (ACK).

NOTE 6 If PMIC device NACKs during Repeat Start for any reason, the host may re-try Repeat Start again. The host can do the
       Repeat Start as many times it may desire. If PMIC device NACKs due to PEC error or parity error, it will always NACK

       regardless of how many times the Host tries Repeat Start. If there were no parity or PEC errors, the device may eventually
       ACK. The PEC calculation by the PMIC device only includes device select code of the ACK response of the Repeat Start
       operation. In other words, if there are more than one Repeat Start operation, the PMIC device includes device select of
       only the last Repeat Start from the host when it ACKs in PEC calculation and all other NACK responses of the device
       select code of the Repeat Start are not included in PEC calculation.
NOTE 7 See Figure 39 to see how Host ends target device operation followed by Host STOP operation.
NOTE 8 Repeat Start or Repeat Start with 7’h7E.
```
