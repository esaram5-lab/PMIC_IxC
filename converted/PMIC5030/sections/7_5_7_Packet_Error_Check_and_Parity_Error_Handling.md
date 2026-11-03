---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 7.5.7
title: Packet Error Check and Parity Error Handling
pages: 91-96
---
# 7.5.7 Packet Error Check and Parity Error Handling

There are two types of error checking done by the PMIC device. Parity error checking and Packet Error checking. By default, the parity error checking is always enabled and packet error checking is disabled. The host may enable the packet error checking at any time. The parity error is checked for each byte in a packet except for the device select code byte from the host. The host sends parity error information in “T” bit. I3C Basic defines TE0, TE1, TE2, TE3, TE4, TE5, and TE6 error detections for target devices. Only TE1 and TE2 error detections are supported by the PMIC for parity checking. All other errors are not supported and not applicable.

## 7.5.7.1 Write Command Data Packet Error Handling - PEC Disabled

The PMIC device checks for the parity error for each byte in a packet that it receives from the host except for the device select code byte that it receives from the host as shown in Table 64.

**Table 64 — Write Command Data Packet; PEC Disabled; 1 Byte Address Mode**

```text
 Start       Bit 7          Bit 6         Bit 5       Bit 4      Bit 3      Bit 2        Bit 1     Bit 0      A/N/T           Stop

 S or Sr      1               X             0          X                    HID                    W=0       A[1],[2],[3]

                                                  Address [7:0]                                                   T

                                                        Data                                                      T

                                                           ...                                                    T

                                                        Data                                                      T         Sr[4] or P
 NOTE 1    See Figure 22 to see how the transition occurs from Target Open Drain (ACK) to Host Push Pull Operation (1st bit of Addr,
           bit [7]).
 NOTE 2    The PMIC NACKs if there is a parity error in a previous transaction when host performs consecutive transactions with
           Repeat Start.
 NOTE 3    The PMIC does not check for parity error in subsequent bytes when it determines the 7-bit device select code issues by
           the host does not match with its own device code. The PMIC ignores the entire packet until STOP or next Repeat Start
           operation.
 NOTE 4    Repeat Start or Repeat Start with 7’h7E.

Write command - if no parity error:
    ▪ The PMIC device executes the command.

Write command - if parity error:
    ▪ The PMIC device discards the byte in the packet that had a parity error.
    ▪ The PMIC device discards all subsequent bytes in that packet until the STOP operation. The PMIC
      device may or may not check parity for all sub-sequent bytes in that packet.
    ▪ Note that as the packet contains more than one byte, if first byte had no parity error but the second
      byte had a parity error, the PMIC device may or may not execute the first byte operation but second
      byte and all subsequent bytes operations are discarded.
    ▪ The PMIC device sets the Table 115, Register 0x0A [2:1] to ‘11’; P_Err in GETSTATUS CCC to ‘1’;
      updates Pending Interrupt Bits [3:0] in GETSTATUS CCC to ‘0001’; asserts GSI_n pin if enabled
      and waits for the next opportunity to send an in band interrupt if IBI is enabled.
```

## 7.5.7.2 Read Command Data Packet Error Handling - PEC Disabled

The PMIC device checks for parity error for each byte in a packet except for the device select code byte that it receives from the host prior to Repeat Start as shown in Table 65. The PMIC device does not compute the parity when it sends the data to the Host. The Host does not check for parity error for the bytes shown in Table 65. The device sends Continuous (‘1’) or Stop (‘0’) information during “T” bit when PMIC device is sending the read data.

**Table 65 — Read Command Data Packet; PEC Disabled; 1 Byte Address Mode**

```text
 Start      Bit 7           Bit 6         Bit 5       Bit 4      Bit 3      Bit 2        Bit 1      Bit 0      A/N/T           Stop

 S or Sr      1               X             0          X                     HID                    W=0       A[1],[2],[3]

                                                  Address [7:0]                                                    T

   Sr         1               X             0          X                     HID                    R=1       A/N[4],[5]

                                                        Data                                                     T=1

                                                           ...                                                   T=1

                                                        Data                                                  T=1[6],[7]     Sr[8] or P
  NOTE 1   See Figure 22 to see how the transition occurs from Target Open Drain (ACK) to Host Push Pull Operation (1st bit of
           Addr, bit [7]).
  NOTE 2   The PMIC NACKs if there is a parity error in a previous transaction when host performs consecutive transactions with
           Repeat Start.
  NOTE 3   The PMIC does not check for parity error in subsequent bytes when it determines the 7-bit device select code issues by
           the host does not match with its own device code. The PMIC ignores the entire packet until STOP or next Repeat Start
           operation.
  NOTE 4   If target device NACKs during Repeat Start for any reason, the host my re-try Repeat Start again. The host can do the
           Repeat Start as many times it may desire. If target device NACKs due to parity error in previous bytes, it will always NACK
           regardless of how many times the Host tries Repeat Start. If there were no parity errors, the PMIC may eventually ACK.
  NOTE 5   See Figure 24 to see how the transition occurs from Host Push Pull Operation to Target Open Drain (ACK).
  NOTE 6   See Figure 25 to see how Host ends target device operation.
  NOTE 7   When PMIC device reaches last byte within the region (either Host region or DIMM vendor region), it will continue to
           return data but returned data will be 0x00 if there is no valid password for DIMM vendor region or Vendor specific region.
           Once the address counter reaches the address 0x1FF, it will reset to address 0x00 and it will continue to return the data.
           Only Host can perform STOP operation.
  NOTE 8   Repeat Start or Repeat Start with 7’h7E.

Read Command - If no parity error:
    ▪ The PMIC sends ACK back to the host when Host performs Repeat Start operation.
    ▪ The PMIC device executes the command and sends the data as shown in Table 65.
Read Command - If parity error:
    ▪ The PMIC device discards the byte in the packet that had a parity error.
    ▪ The PMIC device sends NACK back to the host when Host performs a Repeat Start operation. This
      is shown in the RED color cell in Table 65. The NACK represents either a parity error in one of the
      two bytes or that PMIC is not able to start the read operation. The host may re-try Repeat Start
      again. The host may do the Repeat Start as many times as it may desire. If the PMIC target device
      NACKs due to parity error in a previous byte from the host, it will always NACK regardless of how
      many times Host tries Repeat Start.
    ▪ The PMIC does not send the data shown in Table 65 and instead expects Host to perform STOP
      operation.
    ▪ The PMIC device sets Table 115, Register 0x0A [2:1] to ‘11’; P_Err in GETSTATUS CCC to ‘1’;
      updates Pending Interrupt Bits [3:0] in GETSTATUS CCC to ‘0001’; asserts GSI_n pin if enabled
      and waits for the next opportunity to send an in band interrupt if IBI is enabled.
```

## 7.5.7.3 Write Command Data Packet Error Handling - PEC Is Enabled

The PMIC device checks for the parity error for each byte in a packet that it receives from the host except for the device select code byte that it receives from the host as shown in Table 66. Further, the PMIC device checks for the packet error for the entire packet (from Start condition until last byte of Data) that it receives from the host as shown in Table 66.

**Table 66 — Write Command Data Packet; PEC Enabled; 1 Byte Address Mode**

```text
 Start      Bit 7           Bit 6         Bit 5        Bit 4      Bit 3    Bit 2        Bit 1     Bit 0     A/N/T           Stop

 S or Sr      1               X             0           X                  HID                    W=0      A[1],[2],[3]

                                                  Address [7:0]                                                 T

                          CMD                          W=0         0         0           0          0          T

                                                         Data                                                  T

                                                            ...                                                T

                                                         Data                                                  T

                                                         PEC                                                   T          Sr[4] or P
  NOTE 1    See Figure 22 to see how the transition occurs from Target Open Drain (ACK) to Host Push Pull Operation (Address
            bit 7).
  NOTE 2    The PMIC NACKs if there is a parity or PEC error in a previous transaction when host performs consecutive transactions
            with Repeat Start.
  NOTE 3    The PMIC does not check for parity or PEC error in subsequent bytes when it determines the 7-bit device select code
            issues by the host does not match with its own device code. The PMIC ignores the entire packet until STOP or next
            Repeat Start operation.
  NOTE 4    Repeat Start or Repeat Start with 7’h7E.

Write command - if no parity error:
    ▪ The PMIC device waits for the entire packet. If no error in packet, the PMIC device executes the
      command. If there is an error in the packet, the PMIC device discards the entire packet and does
      not execute the packet and waits for STOP; sets the Table 115, Register 0x0A [3,1] to ‘11’; PEC_Err
      in GETSTATUS CCC to ‘1’; updates Pending Interrupt Bits [3:0] in GETSTATUS CCC to ‘0001’;
      asserts GSI_n pin if enabled and waits for the next opportunity to send an in band interrupt if IBI is
      enabled.

Write command - if parity error:
    ▪ The PMIC device discards that byte and the entire packet until STOP operation.
    ▪ The PMIC device sets the Table 115, Register 0x0A [2:1] to ‘11’; P_Err in GETSTATUS CCC to ‘1’;
      updates Pending Interrupt Bits [3:0] in GETSTATUS CCC to ‘0001’; asserts GSI_n pin if enabled
      and waits for the next opportunity to send an in band interrupt if IBI is enabled.
    ▪ The PMIC device may or may not check the error for the packet. If the PMIC device checks for the
      packet error, likely it will detect an error in the packet and the device may also set Table 115,
      Register 0x0A [3] and PEC_Err in GETSTATUS CCC as well.
```

## 7.5.7.4 Read Command Data Packet Error Handling - PEC Is Enabled

The PMIC device checks for parity error for each byte in a packet except for the device select code byte that it receives from the host prior to Repeat Start as shown in Table 67. The PMIC device does not compute the parity when it sends the data to the Host. The Host does not check for parity error for the bytes shown in Table 67. The device sends Continuous (‘1’) or Stop (‘0’) information during “T” bit when PMIC device is sending the read data.

The PMIC device checks for the PEC error in a packet that it receives from Host from Start condition to Repeat Start (from first device select code followed by the address offset and CMD byte). The PMIC device computes the packet error code for the entire packet starting with Repeat Start (device select code and the data PMIC device transmits back to Host).

**Table 67 — Read Command Data Packet; PEC Enabled; 1 Byte Address Mode**

```text
Start      Bit 7        Bit 6        Bit 5     Bit 4      Bit 3   Bit 2   Bit 1   Bit 0    A/N/T           Stop

S or Sr      1            X           0         X                 HID             W=0     A[1],[2],[3]

                                             Address [7:0]                                     T

                       CMD                     R=1           0     0       0        0         T

                                                 PEC                                          T

  Sr         1            X           0         X                 HID             R=1     A/N[4],[5]

                                                 Data                                        T=1

                                                    ...                                      T=1

                                                 Data                                        T=1

                                                 PEC                                       T=0[6]        Sr[7] or P

 NOTE 1   See Figure 22 to see how the transition occurs from Target Open Drain (ACK) to Host Push Pull Operation (Address bit
          7).
 NOTE 2   The PMIC NACKs if there is a parity or PEC error in a previous transaction when host performs consecutive transactions
          with Repeat Start.
 NOTE 3   The PMIC does not check for parity or PEC error in subsequent bytes when it determines the 7-bit device select code
          issues by the host does not match with its own device code. The PMIC ignores the entire packet until STOP or next
          Repeat Start operation.
 NOTE 4   If target device NACKs during Repeat Start for any reason, the host my re-try Repeat Start again. The host can do the
          Repeat Start as many times it may desire. If target device NACKs due to PEC error or parity error in previous bytes, it
          will always NACK regardless of how many times the Host tries Repeat Start. If there were no parity or PEC errors, the
          PMIC may eventually ACK. The PEC calculation by the target device only includes device select code of the ACK
          response of the Repeat start operation. In other words, if there are more than one Repeat Start operation, the target
          device includes device select of only the last Repeat Start from the Host when it ACKs in PEC calculation and all other
          NACK responses of the device select code of the Repeat Start are not included in PEC calculation.
 NOTE 5   See Figure 24 to see how the transition occurs from Host Push Pull Operation to Target Open Drain (ACK).
 NOTE 6   See Figure 26 to see how target device ends the operation followed by Host STOP operation.
 NOTE 7   Repeat Start or Repeat Start with 7’h7E.
```

Read command - If no parity error and no PEC error

▪ The PMIC device sends ACK back to the host when Host performs a Repeat Start operation.

▪ The PMIC device executes the command and sends the data as shown in Table 67.

▪ The PMIC computes PEC for the bytes (from Start condition to PEC byte prior to Repeat Start)

```text
shown in the cells in Table 67.
```

Read command - if parity error or PEC error

▪ The PMIC device discards the byte in the packet that had a parity error.

▪ The PMIC device discards second byte in that packet if a parity error occurred in first byte. The

```text
PMIC device may or may not check parity for the second byte in that packet.
```

▪ The PMIC device discards the packet if there is a PEC error.

▪ The PMIC sends NACK back to the host when Host performs Repeat Start operation. This is shown

```text
in the RED color cell in Table 67. The NACK represents either PEC error or a parity error in one of
the three bytes or that PMIC is not able to start the read operation. The host may re-try Repeat Start
again. The host may do the Repeat Start as many times it may desire. The PEC calculation by
PMIC device only includes device select code of the ACK responses of the Repeat Start operation.
In other words, if there are more than one Repeat Start operation, the PMIC device includes the
device select of only the last Repeat Start from the Host when it ACKs in PEC calculation and other
NACK responses of the device select codes of the Repeat Start are not included in PEC calculation.
If the PMIC target device NACKs due to PEC error or a parity error in a previous bytes from Host, it
will always NACK regardless of how many times Host tries Repeat Start.
```

▪ The PMIC device does not send any data shown in Table 67 and instead expects Host to perform

```text
STOP operation.
```

▪ The PMIC device sets Table 115, Register 0x0A [3:2] accordingly and Table 115, Register 0x0A [1]

```text
to ‘1’; P_Err, PEC_Err in GETSTATUS CCC to ‘1’ accordingly; updates Pending Interrupt Bits [3:0]
in GETSTATUS CCC to ‘0001’; asserts GSI_n pin if enabled and waits for the next opportunity to
send an in band interrupt if IBI is enabled.
```
