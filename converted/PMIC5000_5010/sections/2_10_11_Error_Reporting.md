---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 2.10.11
title: Error Reporting
pages: 72-72
---
# 2.10.11 Error Reporting

All error conditions detected by the PMIC devices are captured in Table 98, “Register 0x08” [7:0], Table 99, “Register 0x09” [7:0], Table 100, “Register 0x0A” [7:1] Table 101, “Register 0x0B” [7:0], and Table 141, “Register 0x33” [4:2] registers. There are four different possible ways error information can be communicated to the host.

```text
1.    The host makes the read request to Table 98, “Register 0x08”, Table 99, “Register 0x09”,
   Table 100, “Register 0x0A”, Table 101, “Register 0x0B” and Table 141, “Register 0x33” registers.
2. The host starts any transactions with Start condition followed by 7’h7E IBI header (Only applicable in I3C

   Basic mode).
3. The PMIC device sends in band interrupt if enabled, when its SCL and SDA input has been idle for tAVAL
   time (Only applicable in I3C Basic mode).

4. The PMIC device asserts GSI_n pin if enabled.
```
