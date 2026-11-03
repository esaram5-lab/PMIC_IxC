---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 5.4.11
title: IO Operation
pages: 117-117
---
# 5.4.11 IO Operation

At power on, by default, the PMIC device comes up in I2C mode of operation with Open Drain IO for its management interface. The maximum speed is limited to 1 MHz and supported IO voltage levels are from 1.0 V to 3.3 V. After power on, the host may put the interface of the PMIC device in I3C Basic mode of operation. In I3C Basic mode, the host may drive the SCL clock input of the PMIC device using either Push-Pull output driver or the open-drain output driver. It is expected that for all CAMM2 family environment, the host may always drive the SCL clock input using a Push-Pull output driver. To support in band interrupt, the PMIC device supports dynamic switching between Open Drain mode and Push Pull mode on its SDA bus for various events. Table 97 describes the different modes of operation by the PMIC device for each cycle in I3C Basic mode.

**Table 97 — PMIC Device Dynamic IO Operation Mode Switching; I3C Basic Mode**

```text
                                                Open Drain Mode       Push Pull Mode
       START + Device Select Code                     Yes                   No
      START + 7’h7E IBI Header Byte         ng        Yes                   No
   REPEAT START + Device Select Code                   No                   Yes
   REPEAT START + 7’h7E Header Byte                    No                   Yes
   CCC Byte (i.e., after 7’h7E+W=0+ACK)                No                   Yes

                  STOP                                 No                   Yes
          ACK/NACK Responses                          Yes                   No

Command, Block Address, Address Operation              No                   Yes

        Interrupt Request by Target                   Yes                   No
               IBI Payload                             No                   Yes
        Write Data, T-bit sequence                     No                   Yes
        Read Data, T-bit sequence                      No                   Yes
           PEC, T-bit sequence                         No                   Yes
```
