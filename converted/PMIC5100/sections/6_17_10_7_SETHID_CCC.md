---
document: JESD301-2 (PMIC5100 Power Management IC Standard, Rev. 1.03, October 2022)
device: PMIC5100
application: client
section: 6.17.10.7
title: SETHID CCC
pages: 95-96
---
# 6.17.10.7 SETHID CCC

The SETHID CCC is supported only when device is in I2C mode. In I2C mode, when host issues this CCC to guarantee that this CCC is registered by the device without any error, the host shall limit the maximum speed of operation for this CCC to 1 MHz. In I3C Basic mode, it is illegal for host to issue this CCC. When SETHID CCC is registered by the PMIC, it updates Table 140, “Register 0x34” [3:1] with the HID code received by the PMIC and it takes in effect at the next Start operation (i.e., after STOP operation). Table 74 shows an example of a single SETHID CCC. As the device is in I2C mode when SETHID CCC is issued, the PEC function is not supported. Once PMIC receives SETHID CCC and updates its 3-bit HID code, after the Stop operation, PMIC device only responds to updated 7-bit address. The 4-bit LID code of the PMIC device remains as is. The Host may issue SETHID CCC more than one time.

**Table 74 — SETHID CCC - Broadcast**

```text
 Start      Bit 7      Bit 6          Bit 5     Bit 4      Bit 3       Bit 2   Bit 1       Bit 0     A/N/T      Stop
S or Sr       1          1             1          1          1          1        0         W=0          A
                                                 0x61 (Broadcast)                                       T
                               0000                                    HID                   0          T         P
```
