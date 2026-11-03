---
document: JESD301-6 (PMIC5120 Power Management IC Standard, Version 1.0, February 2025)
device: PMIC5120
application: client
section: 6.18.10.3
title: RSTDAA CCC
pages: 96-97
---
# 6.18.10.3 RSTDAA CCC

The RSTDAA CCC is only supported after device is put in I3C Basic mode. In I2C mode, this CCC is ignored (i.e., the RSTDAA command is not executed internally and any bytes arriving after the 0x06 RSTDAA Broadcast CCC are ignored for all purposes, including parity checking, until the next STOP operation or Repeat START with 7’h7E is received). When RSTDAA CCC is registered by the PMIC, it updates Table 146, Register 0x32 [6] = ‘0’, it disables PEC and IBI function (Table 148, Register 0x34 [7:6] = ‘00’) and clears parity function Table 148, Register 0x34 [5] = ‘0’) and it takes in effect at the next Start operation (i.e., after STOP operation).

Table 69 and Table 70 show an example of a single RSTDAA CCC.

If PEC function is enabled, the PEC calculation starts with Start or Repeat Start operation but does not include 7’h7E with W=0 byte in PEC calculation.

**Table 69 — RSTDAA CCC - Broadcast**

```text
  Start      Bit 7       Bit 6        Bit 5      Bit 4         Bit 3    Bit 2      Bit 1       Bit 0    A/N/T       Stop

 S or Sr       1           1            1          1            1         1          0         W=0        A1
                                                 0x06 (Broadcast)                                          T          P
NOTE 1      The PMIC device NACKs if there is a parity error in a previous transaction when host performs consecutive
            transactions with Repeat Start.
```

**Table 70 — RSTDAA CCC - Broadcast with PEC**

```text
  Start      Bit 7       Bit 6        Bit 5      Bit 4         Bit 3    Bit 2      Bit 1       Bit 0    A/N/T       Stop
 S or Sr       1           1            1          1            1         1          0         W=0        A1
                                                 0x06 (Broadcast)                                          T
                                                         PEC                                               T          P
NOTE 1      The PMIC device NACKs if there is a parity or PEC error in a previous transaction when host performs consecutive
            transactions with Repeat Start.
```
