---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 7.5.10.2
title: DISEC CCC
pages: 99-101
---
# 7.5.10.2 DISEC CCC

The DISEC CCC is only supported after device is put in I3C Basic mode. In I2C mode, it is illegal for host to issue this CCC; the PMIC may ignore it or subsequent PMIC operation may not be guaranteed and the PMIC may require Bus Reset. When DISEC CCC is registered by the PMIC, it updates Table 158, Register 0x34 [6] = ‘0’and it takes in effect at the next Start operation (i.e., after STOP operation). Table 74 through Table 77 show an example of a single DISEC CCC. Table 78 shows the encoding definition for DISEC CCC. If PEC function is enabled, the PEC calculation starts with Start or Repeat Start operation but does not include 7’h7E with W=0 byte in PEC calculation.

**Table 74 — DISEC CCC - Broadcast**

```text
 Start     Bit 7       Bit 6        Bit 5        Bit 4         Bit 3      Bit 2      Bit 1         Bit 0    A/N/T       Stop

S or Sr      1           1            1            1            1          1           0           W=0       A[1]

                                                 0x01 (Broadcast)                                             T

                                                 7’h00                                          DISINT        T       Sr[2] or P
 NOTE 1    The PMIC NACKs if there is a parity error in a previous transaction when host performs consecutive transactions with
           Repeat Start.
 NOTE 2    Repeat Start or Repeat Start with 7’h7E.
```

**Table 75 — DISEC CCC - Broadcast with PEC**

```text
 Start     Bit 7       Bit 6        Bit 5        Bit 4         Bit 3      Bit 2      Bit 1         Bit 0    A/N/T       Stop

S or Sr      1           1            1            1            1          1           0           W=0       A[1]

                                                 0x01 (Broadcast)                                             T

                                                 7’h00                                          DISINT        T

                                                         PEC                                                  T       Sr[2] or P
 NOTE 1    The PMIC NACKs if there is a parity or PEC error in a previous transaction when host performs consecutive transactions
           with Repeat Start.
 NOTE 2    Repeat Start or Repeat Start with 7’h7E.
```

**Table 76 — DISEC CCC - Direct**

```text
Start     Bit 7       Bit 6        Bit 5        Bit 4         Bit 3     Bit 2        Bit 1        Bit 0    A/N/T       Stop

S or Sr     1           1            1            1            1          1           0           W=0        A[1]

                                                  0x81 (Direct)                                               T

  Sr                                          DevID[6:0]                                          W=0       A1,[2]

                                                0x00                                           DISINT         T      Sr[3] or P
NOTE 1    The PMIC NACKs if there is a parity error in a previous transaction when host performs consecutive transactions with
          Repeat Start.
NOTE 2    The PMIC device does not check for parity error in subsequent bytes when it determines 7-bit device select code issued
          by the Host does not match with its own device code. The PMIC device ignores the entire packet until STOP operation
          or next Repeat Start operation.
NOTE 3    Repeat Start or Repeat Start with 7’h7E.
```

**Table 77 — DISEC CCC - Direct with PEC**

```text
Start     Bit 7       Bit 6        Bit 5        Bit 4         Bit 3     Bit 2        Bit 1        Bit 0    A/N/T       Stop

S or Sr     1           1            1            1            1          1           0           W=0        A[1]

                                                  0x81 (Direct)                                               T

                                                        PEC                                                   T

  Sr                                          DevID[6:0]                                          W=0       A1,[2]

                                                0x00                                           DISINT         T

                                                        PEC                                                   T      Sr[3] or P
NOTE 1    The PMIC NACKs if there is a parity or PEC error in a previous transaction when host performs consecutive transactions
          with Repeat Start.
NOTE 2    The PMIC device does not check for parity error in subsequent bytes when it determines 7-bit device select code issued
          by the Host does not match with its own device code. The PMIC device ignores the entire packet until STOP operation
          or next Repeat Start operation.
NOTE 3    Repeat Start or Repeat Start with 7’h7E.
```

**Table 78 — DISEC CCC Byte Encoding**

```text
  Bit                       Encoding                                                     Notes

DISINT                     0 = No Action                  It is illegal for Host to issue DISEC CCC with DISINT bit = ‘0’; the
                   1 = Disable IBI Interrupt                PMIC may ignore it or subsequent PMIC operation may not be
                                                                     guaranteed and the PMIC may require Bus Reset
```
