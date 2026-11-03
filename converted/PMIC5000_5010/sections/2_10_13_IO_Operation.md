---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 2.10.13
title: IO Operation
pages: 87-88
---
# 2.10.13 IO Operation

At power on, by default, the PMIC device comes up in legacy I2C mode of operation with Open Drain IO for its interface. The maximum speed is limited to 1 MHz and supported IO voltage levels are from 1.0 V to 3.3 V.

After power on, the host may put the PMIC device in I3C Basic mode of operation.

In I3C Basic mode, the host may drive the SCL clock input of the PMIC device using either Push-Pull output driver or using the open-drain output driver. It is expected that for all DDR5 DIMM family environment, the host may always drive the SCL clock input using a Push-Pull output driver. To support in band interrupt, the PMIC device supports dynamic switching between Open Drain mode and Push Pull mode on its SCL and SDA bus for various event. The Table 84 below describes the different mode of operation by the PMIC device for each cycle.

**Table 84 — PMIC Device Dynamic IO Operation Mode Switching**

```text
                                                     Open Drain Mode         Push Pull Mode
          START + Device Select Code                         Yes                    No
        START + 7’h7E IBI Header Byte                        Yes                    No
     REPEAT START + Device Select Code                       No                    Yes
     REPEAT START + 7’h7E Header Byte                        No                    Yes
   CCC Bytes (i.e., after 7’h7E+W=0+ACK)                     No                    Yes
                     STOP                                    No                     Yes
            ACK/NACK Responses                               Yes                    No
 Command, Block Address, Address Operation                   No                     Yes
Interrupt Request by Target + Device Select Code             Yes                    No
                  IBI Payload                                No                     Yes
           Write Data, T-bit sequence                        No                     Yes
           Read Data, T-bit sequence                         No                     Yes
              PEC, T-bit sequence                  ng        No                     Yes
```
