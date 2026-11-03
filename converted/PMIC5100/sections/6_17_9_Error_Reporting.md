---
document: JESD301-2 (PMIC5100 Power Management IC Standard, Rev. 1.03, October 2022)
device: PMIC5100
application: client
section: 6.17.9
title: Error Reporting
pages: 87-87
---
# 6.17.9 Error Reporting

All error conditions detected by the PMIC devices are captured in Table 96, “Register 0x08” to Table 99, “Register 0x0B” and Table 139, “Register 0x33” registers. There are four different possible ways error information can be communicated to the host.

```text
1. The host makes the read request to Table 96, “Register 0x08” to Table 99, “Register 0x0B” and Table 139,

   “Register 0x33” registers.
2. The host starts any transaction with Start condition followed by 7’h7E IBI header.

3. The PMIC device sends in band interrupt if enabled, when its SCL and SDA input has been idle for tAVAL

   time.
4. The PMIC asserts GSI_n pin if enabled.
```
