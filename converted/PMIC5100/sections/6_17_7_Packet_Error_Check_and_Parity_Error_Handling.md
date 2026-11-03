---
document: JESD301-2 (PMIC5100 Power Management IC Standard, Rev. 1.03, October 2022)
device: PMIC5100
application: client
section: 6.17.7
title: Packet Error Check and Parity Error Handling
pages: 82-87
---
# 6.17.7 Packet Error Check and Parity Error Handling

There are two types of error checking done by the PMIC device. Parity error checking and Packet Error checking. By default, the parity error checking is always enabled and packet error checking is disabled. The host may enable the packet error checking at any time. The parity error is calculated for each byte. The host sends parity error information in “T” bit. I3C basic defines TE0, TE1, TE2, TE3, TE4, TE5, TE6 error detection for target devices. Only TE1 and TE2 error detection is supported by the PMIC for parity checking. All other errors are not supported and not applicable.

## 6.17.7.1 Write Command Data Packet Error Handling - PEC Disabled

The PMIC device checks for the parity error for each byte in a packet except for the device select code byte that it receives from the host as shown in Table 50.

**Table 50 — Write Command Data Packet; PEC Disabled**

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

Write Command - if no parity error:
    • The PMIC device executes the command.
Write Command - if parity error:

    • The PMIC device discards the byte in the packet that had parity error.

    • The PMIC device discards all sub-sequent bytes in that packet until STOP operation. The PMIC device may or
      may not check the parity for all sub-sequent bytes in that packet.

    • Note that as the packet contains more than one byte, if first byte had no parity error but the second byte had a
      parity error, the PMIC device may or may not execute the first byte operation but second byte and all
      subsequent bytes operations are discarded.
    • The PMIC device sets the register Table 98, “Register 0x0A” [2:1] to ‘11’; P_Err in GETSTATUS CCC to ‘1’;
      updates Pending Interrupts Bits [3:0] to ‘0001’; asserts GSI_n pin if enabled and waits for the next opportunity
      to send in band interrupt if IBI is enabled.
```

## 6.17.7.2 Read Command Data Packet Error Handling - PEC Disabled

The PMIC device checks for parity error for each byte in a packet except for the device select code byte that it receives from the host prior to Repeat Start as shown in Table 51. The PMIC device does not compute the parity when it sends the data to the Host. The Host does not check for parity error for the bytes that PMIC device sends. The PMIC device sends Continuous (‘1’) or Stop (‘0’) information during “T” bit when PMIC device is sending the read data.

**Table 51 — Read Command Data Packet; PEC Disabled**

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

Read Command - If no parity error:
    • The PMIC sends ACK back to the host when Host perform Start Repeat operation.
    • The PMIC device executes the command and sends the data as shown in Table 51.

Read Command - If parity error:
    • The PMIC device discards the one byte in the packet that had a parity error.
    • The PMIC sends NACK back to the host when Host performs a Start Repeat operation. This is shown in the
      RED colored cell in Table 51 above. The NACK represents either a parity error in one byte that it receives
      from the host or that PMIC is not able to start the read operation. The host may re-try Repeat Start again. The
      host may do the Repeat Start as many times as it may desire. If the PMIC device NACKs due to parity error, it
      will always NACK regardless of how many times the host tries Repeat Start.
    • The PMIC does not send the data shown in Table 51 and instead expects Host to perform STOP operation.
    • The PMIC device sets Table 98, “Register 0x0A” [2:1] to ‘11’; P_Err in GETSTATUS CCC to ‘1’; updates
      Pending Interrupt Bits [3:0] in GETSTATUS CCC to ‘0001’; asserts GSI_n pin if enabled and waits for the
      next opportunity to send an in band interrupt if IBI is enabled.
```

## 6.17.7.3 Write Command Data Packet Error Handling - PEC Enabled

The PMIC device checks for the parity error for each byte in a packet except for the device select code byte that it receives from the host as shown in Table 52. Further, the PMIC device checks for the packet error for the entire packet (from Start condition until last byte of Data) that it receives from the host as shown in Table 52.

**Table 52 — Write Command Data Packet; PEC Enabled**

```text
      Start         Bit 7         Bit 6     Bit 5      Bit 4       Bit 3     Bit 2      Bit 1     Bit 0      A/N/T         Stop
     S or Sr          1            X           0         X                   HID                  W=0        A1,2,3
                                                    Address [7:0]                                               T
                              CMD                      W=0          0          0          0          0          T
                                                          Data                                                  T
                                                             ...                                                T
                                                          Data                                                  T
                                                          PEC                                                   T         Sr4 or P
     NOTE 1 See Figure 35 to see how the transition occurs from Target Open Drain (ACK) to Host Push Pull operation (Address bit 7).
     NOTE 2 The PMIC device NACKs if there is a parity or PEC error in a previous transaction when host performs consecutive
            transactions with Repeat Start.
     NOTE 3 The PMIC device does not check for parity or PEC error in subsequent bytes when it determines 7-bit device select code
            issued by the host does not match with its own device code. The PMIC device ignores the entire packet until STOP or next
            Repeat Start operation.
     NOTE 4 Repeat Start or Repeat Start with 7’h7E.
Write Command - if no parity error:
    • The PMIC device waits for the entire packet. If no error in packet, the PMIC device executes the command. If

      there is an error in the packet, the PMIC device discards the entire packet and does not execute that packet and
      waits for STOP, sets the Register Table 98, “Register 0x0A” [3,1] to ‘11’; PEC_Err in GETSTATUS CCC to
      ‘1’; updates Pending Interrupt Bits [3:0] in GETSTATUS CCC to ‘0001’; asserts GSI_n pin enabled and waits

      for the next opportunity to send in band interrupt if IBI is enabled.

Write Command - if parity error:

    • The PMIC device discards that byte and the entire packet until STOP operation.
    • The PMIC device sets the Table 98, “Register 0x0A” [2:1] to ‘11’; P_Err in GETSTATUS CCC to ‘1’; updates
      Pending Interrupt Bits [3:0] in GETSTATUS CCC to ‘0001’; asserts GSI_n pin if enabled and waits for the
      next opportunity to send in band interrupt if IBI is enabled.
    • The PMIC may or may not check the error for the packet. If the device checks for the packet error, likely it will
      detect an error in the packet and the device may also set the Table 98, “Register 0x0A” [3] and PEC_ERR in
      GETSTATUS CCC as well.
```

## 6.17.7.4 Read Command Data Packet Error Handling - PEC Enabled

The PMIC device checks for the parity error for each byte in a packet except for the device select code byte that it receives from the host prior to Repeat Start as shown in Table 53. The PMIC device does not compute the parity when it sends the data to the Host. The Host does not check for parity error for the bytes shown in Table 53. The PMIC device sends Continuous (‘1’) or Stop (‘0’) information during “T” bit when PMIC device is sending the read data. The PMIC device checks for the PEC error for a packet that it receives from the Host from Start condition to Repeat Start condition (from first device select code followed by the address offset and CMD byte). The PMIC device computes the packet error code for the entire packet starting with Repeat Start (device select code and the data PMIC device transmits back to Host).

**Table 53 — Read Command Data Packet; PEC Enabled**

```text
 Start         Bit 7         Bit 6      Bit 5      Bit 4       Bit 3     Bit 2      Bit 1      Bit 0      A/N/T         Stop
S or Sr           1            X          0          X                   HID                   W=0        A1,2,3
           Address [7:0]                                                                                     T
           CMD                                     R=1          0          0          0          0           T
                                                      PEC                                                    T
   Sr             1        X              0          X                   HID                   R=1        A/N4,5
                                                      Data                                                 T=1
                                                         ...                                               T=1
                                                      Data                                                 T=1
                                                      PEC                                                  T=06       Sr7 or P
NOTE 1 See Figure 35 to see how the transition occurs from Target Open Drain (ACK) to Host Push Pull operation (Address bit 7).
NOTE 2 The PMIC device NACKs if there is a parity or PEC error in a previous transaction when host performs consecutive
       transactions with Repeat Start.
NOTE 3 The PMIC device does not check for parity error in subsequent bytes when it determines 7-bit device select code issued by
       the host does not match with its own device code. The PMIC device ignores the entire packet until STOP or next Repeat
       Start operation.
NOTE 4 If PMIC device NACKs during Repeat Start for any reason, the host may re-try Repeat Start again. The host can do the
       Repeat Start as many times it may desire. If PMIC device NACKs due to PEC error or parity error, it will always NACK
       regardless of how many times the Host tries Repeat Start. If there were no parity or PEC errors, the device may eventually

       ACK. The PEC calculation by the PMIC device only includes device select code of the ACK response of the Repeat Start
       operation. In other words, if there are more than one Repeat Start operation, the PMIC device includes device select of
       only the last Repeat Start from the host when it ACKs in PEC calculation and all other NACK responses of the device

       select code of the Repeat Start are not included in PEC calculation.
NOTE 5 See Figure 37 to see how the transition occurs from Host Push Pull Operation to Target Open Drain (ACK).

NOTE 6 See Figure 39 to see how Host ends target device operation followed by Host STOP operation.
NOTE 7 Repeat Start or Repeat Start with 7’h7E.
```

Read command - If no parity error and no PEC error:

```text
    • The PMIC sends ACK back to the host when Host perform a Start Repeat operation.
    • The PMIC device executes the command and sends the data as shown in Table 53.
    • The PMIC computes PEC for the bytes (from Start condition to PEC byte prior to Repeat Start) as shown in
      Table 53.

Read command - if parity or PEC error:
    • The PMIC device discards the byte in the packet that had a parity error.
    • The PMIC device discards second byte in that packet if a parity error occurred in first byte. The PMIC device
      may or may not check parity for the second byte in that packet.
    • The PMIC device discards the packet if there is a PEC error.
    • The PMIC sends NACK back to the host when Host perform Start Repeat operation. This is shown in the RED
      colored cell in Table 53. The NACK represents either PEC error or parity error in one of the two bytes or that
      PMIC is not able to start the read operation. The host may re-try Repeat Start again. The host may do the
      Repeat Start as many times as it may desire. The PEC calculation by PMIC device only includes device select
      code of the ACK responses of the Repeat Start operation.

       In other words, if there are more than one Repeat Start operation, the PMIC device includes the device select
       code of only the last Repeat Start from the Host when it ACKs in PEC calculation and other NACK responses
       of the device select codes of the Repeat Start are not included in PEC calculation. If the PMIC device NACKs
       due to PEC error or parity error in previous bytes from Host, it will always NACK regardless of how many
       times Host tries Repeat Start.
    • The PMIC does not send any data shown in Table 53 and instead expects Host to perform STOP operation.
    • The PMIC device sets Table 98, “Register 0x0A” [3:2] accordingly and Table 98, “Register 0x0A” [1] to ‘1’;
      P_Err, PEC_Err in GETSTATUS CCC to ‘1’ accordingly; updates Pending Interrupt Bits [3:0] in GETSTA-
      TUS CCC to ‘0001’; asserts GSI_n pin if enabled and waits for the next opportunity to send an in band
      interrupt if IBI is enabled.
```
