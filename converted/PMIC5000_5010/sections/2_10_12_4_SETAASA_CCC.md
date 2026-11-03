---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 2.10.12.4
title: SETAASA CCC
pages: 77-77
---
# 2.10.12.4 SETAASA CCC

The SETAASA CCC is only supported when device is in I2C mode. In I2C mode, when host issues this CCC, to guarantee that this CCC is registered by the device without any error, the host shall limit the maximum speed operation for this CCC to 1 MHz. In I3C Basic mode, this CCC is ignored. When SETAASA CCC is registered by the PMIC, it updates Table 140, “Register 0x32” [6] = ‘1’and it takes in effect at the next Start operation (i.e., after STOP operation). Table 67 shows an example of a single SETAASA CCC.

SETAASA CCC does not support PEC function as device is in I2C mode and there is no PEC function in I2C mode.

**Table 67 — SETAASA CCC - Broadcast**

```text
 Start        Bit 7       Bit 6        Bit 5        Bit 4        Bit 3       Bit 2        Bit 1        Bit 0      A/N/T       Stop
S or Sr         1            1           1            1            1            1            0         W=0           A
                                                   0x29 (Broadcast)                                                  T          P
```
