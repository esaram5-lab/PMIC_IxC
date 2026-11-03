---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 2.10.12.6
title: DEVCAP CCC
pages: 79-80
---
# 2.10.12.6 DEVCAP CCC

The DEVCAP CCC is only supported after device is put in I3C Basic mode. In I2C mode, it is illegal for host to issue this CCC. Table 71 to Table 72 show an example of a single DEVCAP CCC. Table 73 defines the encoding for DEVCAP CCC. If PEC function is enabled, the PEC calculation starts with Start or Repeat Start operation but does not include 7’h7E with W=0 byte in PEC calculation.

**Table 71 — DEVCAP CCC - Direct**

```text
 Start       Bit 7        Bit 6        Bit 5        Bit 4         Bit 3       Bit 2        Bit 1        Bit 0       A/N/T        Stop
S or Sr         1            1            1           1            1            1            0          W=0           A1

                                                     0xE0 (Direct)                                                     T
  Sr                                            DevID[6:0]                                               R=1          A1

                                         MSB (Each bit defines capability)                                             T

                                          LSB (Each bit defines capability)                                            T       Sr2 or P
NOTE 1 The PMIC NACKs if there is a parity error in a previous transaction when host performs consecutive transactions with Repeat Start.
NOTE 2 Repeat Start or Repeat Start with 7’h7E.
```

**Table 72 — DEVCAP CCC - Direct with PEC**

```text
 Start       Bit 7        Bit 6        Bit 5        Bit 4         Bit 3       Bit 2        Bit 1        Bit 0       A/N/T        Stop
S or Sr         1            1            1           1            1            1            0          W=0           A1
                                                     0xE0 (Direct)                                                     T
                                                            PEC                                                        T
  Sr                                            DevID[6:0]                                               R=1          A1
                                         MSB (Each bit defines capability)                                             T
                                          LSB (Each bit defines capability)                                            T
                                                            PEC                                                        T       Sr2 or P
NOTE 1 The PMIC NACKs if there is a parity or PEC error in a previous transaction when host performs consecutive transactions with
       Repeat Start.
NOTE 2 Repeat Start or Repeat Start with 7’h7E.
```

**Table 73 — DEVCAP CCC Byte Encoding**

```text
           Bit                                Encoding                                            Notes
     MSB [7]             RFU                                                    Coded as ‘0’
     MSB[6]              RFU                                                    Coded as ‘0’
     MSB[5]              RFU                                                    Coded as ‘0’
     MSB[4]              RFU                                                    Coded as ‘0’
     MSB[3]              RFU                                                    Coded as ‘0’
                         0 = No Support for Timer based Reset                   Coded as ‘1’
     MSB[2]
                         1 = Supports Timer based Reset
    MSB[1:0]             RFU                                                    Coded as ‘00’
     LSB[7:0]            RFU                                                    Coded as ‘0x00’

2.10.12.7 SETHID CCC
```

The SETHID CCC is supported only when device is in I2C mode. In I2C mode, when host issues this CCC, to guarantee that this CCC is registered by the device without any error, the host shall limit the maximum speed operation for this CCC to 1 MHz. In I3C Basic mode, it is illegal for host to issue this CCC. When SETHID CCC is registered by the PMIC, it updates Table 142, “Register 0x34” [3:1] with the HID code received by the PMIC and it takes in effect at the next Start operation (i.e., after STOP operation). Table 74 shows an example of a single SETHID

CCC. As the device is in I2C mode when SETHID CCC is issued, the PEC function is not supported.

Once PMIC receives SETHID CCC and updates its 3-bit HID code, after the Stop operation, PMIC device only responds to updated 7-bit address. The 4-bit LID code of the PMIC device remains as is.

The Host may issue SETHID CCC more than one time.

**Table 74 — SETHID CCC - Broadcast**

```text
 Start          Bit 7      Bit 6     Bit 5       Bit 4     Bit 3       Bit 2        Bit 1        Bit 0   A/N/T   Stop
S or Sr          1            1        1          1            1        1            0           W=0      A
                                                 0x61 (Broadcast)                                         T
                 0            0        0          0                 HID[2:0]                      0       T       P
```
