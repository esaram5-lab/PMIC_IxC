---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 5.4.10.4
title: SETAASA CCC
pages: 107-108
---
# 5.4.10.4 SETAASA CCC

The SETAASA CCC is only supported when device is in I2C mode. In I2C mode, when host issues this CCC, to guarantee that this CCC is registered by the device without any parity error the host shall limit the maximum speed of operation for this CCC to 1 MHz. In I3C Basic mode, this CCC is ignored (i.e., the SETAASA CCC is not executed internally). When SETAASA CCC is registered by the PMIC, it updates Table 154, Register 0x32 [6] = ‘1’ and it takes in effect at the next Start operation (i.e., after STOP operation). Table 80 shows an example of a single SETAASA CCC. SETAASA CCC does not support PEC function as device is in I2C mode and there is no PEC function in I2C mode.

**Table 80 — SETAASA CCC - Broadcast**

```text
 Start        Bit 7      Bit 6      Bit 5       Bit 4         Bit 3    Bit 2      Bit 1      Bit 0      A/N/T        Stop
S or Sr        1           1          1           1            1        1           0        W=0           A
                                               0x29 (Broadcast)                                            T           P
```
