---
document: JESD301-2 (PMIC5100 Power Management IC Standard, Rev. 1.03, October 2022)
device: PMIC5100
application: client
section: 6.17.10.1
title: ENEC CCC
pages: 88-90
---
# 6.17.10.1 ENEC CCC

The ENEC CCC is only supported after device is put in I3C Basic mode. In I2C mode, it is illegal for host to issue this

CCC. When ENEC CCC is registered by the PMIC, it updates Table 140, “Register 0x34” [6] = ‘1’ and it takes in effect at the next Start operation (i.e., after STOP operation). Table 55 and Table 57 show an example of a single

ENEC CCC. Table 59 shows the encoding definition for ENEC CCC. If PEC function is enabled, the PEC calculation starts with Start or Repeat Start operation but does not include 7’h7E with W=0 byte in PEC calculation.

**Table 55 — ENEC CCC - Broadcast**

```text
 Start      Bit 7        Bit 6        Bit 5        Bit 4        Bit 3        Bit 2        Bit 1       Bit 0       A/N/T         Stop
S or Sr        1            1           1            1            1            1            0         W=0           A1
                                                   0x00 (Broadcast)                                                  T
                                                   0x00                                              ENINT           T         Sr2 or P
NOTE 1 The PMIC device NACKs if there is a parity error in a previous transaction when host performs consecutive transactions with
       Repeat Start.
NOTE 2 Repeat Start or Repeat Start with 7’h7E.
```

**Table 56 — ENEC CCC - Broadcast with PEC**

```text
Start        Bit 7        Bit 6        Bit 5        Bit 4         Bit 3       Bit 2        Bit 1         Bit 0      A/N/T         Stop
S or Sr        1            1            1            1             1            1            0          W=0          A1
                                                   0x00 (Broadcast)                                                    T
                                                    0x00                                               ENINT           T
                                                            PEC                                                        T        Sr2 or P
NOTE 1 The PMIC device NACKs if there is a parity or PEC error in a previous transaction when host performs consecutive transactions
       with Repeat Start.
NOTE 2 Repeat Start or Repeat Start with 7’h7E.
```

**Table 57 — ENEC CCC - Direct**

```text
Start        Bit 7        Bit 6        Bit 5        Bit 4         Bit 3       Bit 2        Bit 1         Bit 0      A/N/T         Stop
S or Sr        1            1            1            1             1            1            0          W=0          A1
                                                     0x80 (Direct)                                                     T
  Sr                                            DevID[6:0]                                               W=0          A1,2

                                                    0x00                                               ENINT           T        Sr3 or P
NOTE 1 The PMIC device NACKs if there is a parity error in a previous transaction when host performs consecutive transactions with
       Repeat Start.

NOTE 2 The PMIC device does not check for parity error in subsequent bytes when it determines 7-bit device select code issued by the host
       does not match with its own device code. The PMIC device ignores the entire packet until STOP operation or next Repeat Start

       operation.
NOTE 3 Repeat Start or Repeat Start with 7’h7E.
```

**Table 58 — ENEC CCC - Direct with PEC**

```text
Start        Bit 7        Bit 6        Bit 5        Bit 4         Bit 3       Bit 2        Bit 1         Bit 0      A/N/T         Stop
S or Sr        1            1            1            1             1            1            0          W=0          A1
                                                     0x80 (Direct)                                                     T
                                                            PEC                                                        T
  Sr                                            DevID[6:0]                                               W=0          A1,2
                                                    0x00                                               ENINT           T
                                                            PEC                                                        T        Sr3 or P
NOTE 1 The PMIC device NACKs if there is a parity or PEC error in a previous transaction when host performs consecutive transactions
       with Repeat Start.
NOTE 2 The PMIC device does not check for parity or PEC error in subsequent bytes when it determines 7-bit device select code issued by
       the host does not match with its own device code. The PMIC device ignores the entire packet until STOP operation or next Repeat
       Start operation.
NOTE 3 Repeat Start or Repeat Start with 7’h7E.
```

**Table 59 — ENEC CCC Byte Encoding**

```text
     Bit                        Encoding                                          Notes
                  0 = No Action                             It is illegal for Host to issue ENEC CCC
ENINT
                  1 = Enable IBI Interrupt                  with ENINT bit = ‘0’
```
