---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 5.4.10.6
title: DEVCAP CCC
pages: 109-110
---
# 5.4.10.6 DEVCAP CCC

The DEVCAP CCC is only supported after device is put in I3C Basic mode. In I2C mode, it is illegal for host to issue this CCC; the PMIC ignore it or subsequent PMIC operation may not be guaranteed and the PMIC may require Bus Reset. Table 84 to Table 85 show an example of a single DEVCAP CCC. Table 86 defines the encoding for DEVCAP CCC. If PEC function is enabled, the PEC calculation starts with Start or Repeat Start operation but does not include 7’h7E with W=0 byte in PEC calculation.

**Table 84 — DEVCAP CCC - Direct**

```text
    Start           Bit 7       Bit 6       Bit 5       Bit 4      Bit 3     Bit 2      Bit 1      Bit 0     A/N/T       Stop
   S or Sr            1           1           1           1         1          1         0         W=0        A[1]
                                                         0xE0 (Direct)                                         T
     Sr                                               DevID[6:0]                                    R=1        A1
                                              MSB (Each bit defines capability)                               T=1
                                              LSB (Each bit defines capability)                               T=0      Sr[2] or P
NOTE 1 The PMIC device NACKs if there is a parity error in a previous transaction when host performs consecutive transactions
       with Repeat Start.
NOTE 2 Repeat Start or Repeat Start with 7’h7E.
```

**Table 85 — DEVCAP CCC - Direct with PEC**

```text
    Start        Bit 7      Bit 6     Bit 5       Bit 4         Bit 3   Bit 2      Bit 1        Bit 0     A/N/T        Stop
   S or Sr        1          1          1          1             1       1           0          W=0           A[1]
                                                   0xE0 (Direct)                                               T
                                                          PEC                                                  T
     Sr                                       DevID[6:0]                                        R=1           A1
                                        MSB (Each bit defines capability)                                     T=1
                                         LSB (Each bit defines capability)                                    T=1
                                                          PEC                                                 T=0    Sr[2] or P
NOTE 1 The PMIC device NACKs if there is a parity or PEC error in a previous transaction when host performs consecutive
       transactions with Repeat Start.
NOTE 2 Repeat Start or Repeat Start with 7’h7E.
```

**Table 86 — DEVCAP CCC Byte Encoding**

```text
     Bit                               Encoding                                                  Notes
MSB [7]          RFU                                                       Coded as ‘0’

 MSB[6]          RFU                                                       Coded as ‘0’
 MSB[5]          RFU                                                       Coded as ‘0’

 MSB[4]          RFU                                                       Coded as ‘0’

 MSB[3]          RFU                                                       Coded as ‘0’
 MSB[2]          0 = No Support for Timer based Reset                      PMIC hard codes this to ‘1’.
                 1 = Supports Timer based Reset
MSB[1:0]         RFU                                                       Coded as ‘00’
LSB[7:0]         RFU                                                       Coded as ‘0x00’
```
