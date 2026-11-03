---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 7.5.3
title: Interrupt Arbitration
pages: 88-90
---
# 7.5.3 Interrupt Arbitration

As there are multiple devices I3C Basic bus, multiple device may request an interrupt when the Host I3C Basic bus is inactive for tAVAL period. Arbitration process is required. For DDR5 DIMM application environment, there could be up to total of 13 difference devices including the PMIC on I3C bus. On a typical DDR5 DIMM application environment, all devices have the same 3-bit HID code. Hence the arbitration is always won by the lowest 4-bit LID code. For example, if one target device has LID code of ‘0010’ and other device (PMIC) has a LID code of ‘1001’, through the arbitration process, the target device LID code of ‘0010’ wins. The PMIC device with a LID code of ‘1001’ must release the bus and wait for next opportunity to request an interrupt. Table 63 shows the arbitration priority based on the LID code for all devices. The Green color cells in Table 63 are the likely devices that will be on a standard DDR5 RDIMM or DDR5 LRDIMM. The Olive color cells in Table 63 do not apply.

**Table 63 — Interrupt Arbitration - Among All Devices**

```text
                             HID Code =     Arbitration
 Device         LID Code        ‘111’        Priority

  N/A             0000          N/A             N/A

  RFU             0001          111              1

  TS0             0010          111              2

  RFU             0011          111              3

  RFU             0100          111              4

  RFU             0101          111              5

  TS1             0110          111              6

  RFU             0111          111              7

 PMIC1            1000          111              8

 PMIC0            1001          111              9

SPD Hub           1010          N/A             N/A
  RCD             1011          111             10

 PMIC2            1100          111             11

  RFU             1101          111             12

  RFU             1110          111             13

  N/A             1111          N/A             N/A
```

In an uncommon but possible scenario would be that at the exact same time as when the Hub or local target devices (i.e., PMIC) are requesting an interrupt, the host is starting an operation to the Hub or local target devices (i.e., PMIC). When this happens, Host also gets involved in the arbitration process along with the Hub or the local target devices (PMIC). During the arbitration phase, there will be always only one winning device and it could be either Hub or the local target device (i.e., PMIC) or the Host. If the host wins during the arbitration phase, it continues with normal operation. The losing Hub or local target device (i.e., PMIC) waits for next opportunity to send an interrupt. If the host loses during the arbitration phase, it host must let go of the bus. When Host loses during the arbitration, the host must let the Hub or local target device (i.e., PMIC) finish sending their 4-bit LID code followed by 3-bit HID code followed by R/W = ‘1’. At this point, during the 9th bit, the host has two options to take the action as noted below: Host sends an ACK to accept the interrupt and hence accepts the IBI payload from the winning Hub or local target device (i.e., PMIC). After the IBI payload, the host issues STOP operation. Host sends an NACK followed by STOP operation. In a rare but still possible scenario would be that at the exact same time as when the PMIC is requesting an interrupt, the host is starting an operation to the same PMIC. When this happens, neither Host nor the PMIC knows it is a winner until the 8th bit and Host always wins. This is because, the PMIC sends R=1 (8th bit) during the interrupt. The host sets W=0 (8th bit) during the operation. As a result, the host wins and the PMIC must let go of the bus and wait for the next opportunity to send an interrupt.

In an extremely rare but still possible scenario would be that at the same exact time as when PMIC device is requesting an interrupt, the host is requesting a read operation with the default read address pointer mode to the PMIC device. When this happens, there is no winning device. This is the only time there is no winning device. This is because, the PMIC device sends R=1 (8th bit) during the interrupt and Host also sends R=1 for read request with default read address pointer mode. As a result, there is no winner because Host is waiting for PMIC to ACK and PMIC is waiting for Host to ACK. In this case, neither Host nor PMIC will ACK. Since there is no ACK (i.e., NACK) by either device, the Host must time out and repeat the read request with Repeat Start. When Host repeats the read request with Repeat Start, the PMIC does not send an interrupt because of Repeat Start.
