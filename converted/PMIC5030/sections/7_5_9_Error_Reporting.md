---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 7.5.9
title: Error Reporting
pages: 96-96
---
# 7.5.9 Error Reporting

All error conditions detected by the PMIC devices are captured in Table 113, Register 0x08 [7:0], Table 114, Register 0x09 [7:0], Table 115, Register 0x0A [7:1] Table 116, Register 0x0B [7:0], Table 157, Register 0x33 [4:2],Table 175, Register 0x108 [7:0] and Table 176, Register 0x109 [7:6,0] registers. There are four different possible ways error information can be communicated to the host.

1. The host makes the read request to Table 113, Register 0x08, Table 114, Register 0x09, Table 115, Register 0x0A, Table 116, Register 0x0B, Table 157, Register 0x33, Table 175, Register 0x108 and Table 176, Register 0x109 registers.

2. The host starts any transactions with Start condition followed by 7’h7E IBI header, if IBI is enabled (Only applicable in I3C Basic mode).

3. The PMIC device sends in band interrupt if enabled, when its SCL and SDA input has been idle for tAVAL time (Only applicable in I3C Basic mode).

4. The PMIC device asserts GSI_n pin if enabled.
