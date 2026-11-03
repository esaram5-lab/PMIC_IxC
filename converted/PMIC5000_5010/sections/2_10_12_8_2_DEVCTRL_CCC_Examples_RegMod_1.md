---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 2.10.12.8.2
title: DEVCTRL CCC Examples - RegMod = ‘1’
pages: 86-87
---
# 2.10.12.8.2 DEVCTRL CCC Examples - RegMod = ‘1’

Table 82 shows an example of DEVCTRL CCC data packet for the purpose of configuring device specific address offset register. It assumes that all devices on the bus are already in I3C Basic mode with PEC function enabled and parity function enabled. In this example, the Host sends Multicast command to all devices with 4-bit LID code of ‘0010’ on the I3C Basic bus to write to address offset of 0x1C and 0x1D with data 0xFF and 0x55 respectively followed by all devices with 4-bit LID of ‘1001’ on the I3C Basic bus to write to address offset of 0x15 with data 0x78. The PEC calculation starts with Start or Repeat Start operation but does not include 7’h7E with W=0 byte in PEC calculation.

**Table 82 — DEVCTRL CCC Example - Multicast Command to ‘0010’ and ‘1001’ Devices**

```text
Start      Bit 7        Bit 6       Bit 5        Bit 4        Bit 3       Bit 2        Bit 1         Bit 0        A/N/T   Stop
  S          1            1            1           1            1            1           0           W=0           A1

                                              0x62 (Broadcast)                                                     T
                         011                        00                   00                            1           T
                                           0010 000                                                    0           T
                                      0001 1100 (address offset 0x1C)                                              T
                                   0010 0000 (CMD field = 2 bytes of data)                                         T
                                              1111 1111 (data)                                                     T
                                              0101 0101 (data)                                                     T
                                                    PEC                                                            T
 Sr          1            1            1           1            1            1           0           W=0           A1
                                              0x62 (Broadcast)                                                     T
                         011                        00                   00                            1           T
                                            1001 000                                                   0           T
                                       0001 0101 (address offset 0x15)                                             T
                                    0000 0000 (CMD field = 1 byte of data)                                         T
                                              0111 1000 (data)                                                     T
                                                    PEC                                                            T       P
NOTE 1 See Figure 18 to see how the transition occurs from Target Open Drain (ACK) to Host Push Pull Operation.
```

Table 83 shows an example of DEVCTRL CCC data packet for the purpose of configuring device specific address offset register. It assumes that all devices on the bus are already in I3C Basic mode with PEC function disabled and parity function enabled. In this example, the Host sends Multicast command to all devices with 4-bit LID code of ‘1001’ on the I3C Basic bus to write to address offset of 0x13 with data 0xFF and it continues to write data 0x01 to the next address.

**Table 83 — DEVCTRL CCC Example - Multicast Command to ‘1001’ Devices**

```text
Start      Bit 7        Bit 6       Bit 5        Bit 4         Bit 3      Bit 2        Bit 1         Bit 0        A/N/T   Stop
  S          1            1            1           1            1            1           0           W=0           A1
                                                  0x62 (Broadcast)                                                 T
                         011                              00                      00                   1           T
                                               1001 000                                                0           T
                                           0001 0011 (address offset 0x13)                                         T
                                                  1111 1111 (data)                                                 T
                                                  0000 0001 (data)                                                 T       P
NOTE 1 See Figure 18 to see how the transition occurs from Target Open Drain (ACK) to Host Push Pull Operation.
```
