---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 7.5.10.8.1
title: DEVCTRL CCC Examples - RegMod = ‘0’
pages: 108-110
---
# 7.5.10.8.1 DEVCTRL CCC Examples - RegMod = ‘0’

Table 93 shows an example of DEVCTRL CCC data packet. It assumes that all devices on the bus are already in I3C Basic mode with PEC function disabled and parity function enabled. In this example, the Host uses DEVCTRL CCC as Multicast command. Host sends Multicast command to all devices with 4-bit LID code of ‘1001’ on I3C Basic bus to do VR Enable followed by all devices with 4-bit LID code of ‘0110’ to disable parity function. The host sends AddrMask = ‘011’ to indicate Multicast command with DevID[6:3] match; StartOffset = ‘00’ to indicate starting Byte 0 and RegMod = ‘0’ to indicates general register. Upon receiving this command, all devices with DevID[6:3] that matches to ‘1001’ will do the VR Enable command and DevID[6:3] that matches to ‘0110’ with disable the parity function.

**Table 93 — DEVCTRL CCC Example - Multicast Command to ‘1001’ and ‘0110’ Devices**

```text
Start      Bit 7       Bit 6         Bit 5         Bit 4         Bit 3       Bit 2         Bit 1          Bit 0        A/N/T        Stop

 S          1            1             1             1              1           1            0            W=0            A[1]

                                                   0x62 (Broadcast)                                                       T

                        011                                 00                        00                    0             T

                                                1001 000                                                    0             T

                                                         0000 0010                                                        T

 Sr         1            1             1             1              1           1            0            W=0            A1

Start     Bit 7       Bit 6      Bit 5       Bit 4        Bit 3     Bit 2        Bit 1       Bit 0       A/N/T        Stop

                                             0x62 (Broadcast)                                              T

                      011                            00                     00                 0           T

                                          0110 000                                             0           T

                                                  0100 0000                                                T           P
 NOTE 1    See Figure 22 to see how the transition occurs from Target Open Drain (ACK) to Host Push Pull Operation.
```

Table 94 shows an example of DEVCTRL CCC data packet. It assumes that all devices on the bus are already in I3C Basic mode with PEC function disabled and parity function enabled. In this example, the Host uses DEVCTRL CCC as Broadcast command to enable PEC function. The host sends AddrMask = ‘111’ to indicate Broadcast command; StartOffset = ‘00’ to indicate starting Byte 0 and RegMod = ‘0’ to indicate general register. Upon receiving this command, all devices will enable PEC function.

**Table 94 — DEVCTRL CCC Example - Broadcast Command to all Devices**

```text
Start     Bit 7       Bit 6      Bit 5       Bit 4        Bit 3   ngBit 2        Bit 1       Bit 0       A/N/T        Stop

 S         1           1           1          1            1          1           0          W=0          A[1]

                                             0x62 (Broadcast)                                              T

                      111                            00                     00                 0           T

                                          0000 000                                             0           T

                                                  1000 0000                                                T           P

 NOTE 1    See Figure 22 to see how the transition occurs from Target Open Drain (ACK) to Host Push Pull Operation.
```

Table 95 shows an example of DEVCTRL CCC data packet. It assumes that all devices on the bus are already in I3C Basic mode with PEC function disabled and parity function enabled. In this example, the Host uses DEVCTRL CCC as Unicast command to enable VR on DIMM5. The host sends AddrMask = ‘000’ to indicate Unicast command; StartOffset = ‘00’ to indicate starting Byte 0 and RegMod = ‘0’ to indicate general register. Upon receiving this command, PMIC on DIMM5 will enable its regulator.

**Table 95 — DEVCTRL CCC Example - Unicast Command to PMIC on DIMM5**

```text
Start     Bit 7       Bit 6      Bit 5       Bit 4        Bit 3     Bit 2        Bit 1       Bit 0       A/N/T        Stop

 S         1           1           1          1            1          1           0          W=0          A[1]

                                             0x62 (Broadcast)                                              T

                      000                            00                     00                 0           T

                                          1001 101                                             0           T

                                                  0000 0010                                                T           P
 NOTE 1    See Figure 22 to see how the transition occurs from Target Open Drain (ACK) to Host Push Pull Operation.
```
