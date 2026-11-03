---
document: JESD301-6 (PMIC5120 Power Management IC Standard, Version 1.0, February 2025)
device: PMIC5120
application: client
section: 6.18.9
title: Error Reporting
pages: 91-92
---
# 6.18.9 Error Reporting

All error conditions detected by the PMIC devices are captured in Table 104, Register 0x08 to Table 107, Register 0x0B, and Table 147, Register 0x33 registers.

There are four different possible ways error information can be communicated to the host.

```text
1.   The host makes the read request to Table 104, Register 0x08 to Table 107, Register 0x0B, and
     Table 147, Register 0x33 registers.
2.   The host starts any transaction with Start condition followed by 7’h7E IBI header.
3.   The PMIC device sends in band interrupt if enabled, when its SCL and SDA input has been idle for
     tAVAL time.
4.   The PMIC device asserts GSI_n pin if enabled.
```
