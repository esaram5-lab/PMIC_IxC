---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 5.4.9
title: Error Reporting
pages: 102-103
---
# 5.4.9 Error Reporting

All error conditions detected by the PMIC devices are captured in Table 112, Register 0x08 to Table 115, Register 0x0B and Table 155, Register 0x33 registers. There are four different possible ways error information can be communicated to the host.

```text
1.      The host makes the read request to Table 112, Register 0x08 to Table 115, Register 0x0B and
        Table 155, Register 0x33 registers.
2.      The host starts any transaction with Start condition followed by 7’h7E IBI header if IBI is enabled
        (Only applicable in I3C Basic mode).
3.      The PMIC device sends in band interrupt if enabled, when its SCL and SDA input has been idle for
        tAVAL time.
4.      The PMIC asserts GSI_n pin if enabled.
```
