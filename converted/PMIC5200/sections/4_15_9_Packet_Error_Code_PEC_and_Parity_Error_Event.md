---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 4.15.9
title: Packet Error Code (PEC) and Parity Error Event
pages: 68-68
---
# 4.15.9 Packet Error Code (PEC) and Parity Error Event

In I3C mode, PEC function and parity function can be enabled. If enabled, when PMIC detects either PEC error or parity error, the PMIC sets the register Table 114, Register 0x0A [3:2] appropriately, and it continues to operate as normal and allows access to all registers. See clause 5.4.5 to 5.4.9 for additional details. The host is responsible for taking any specific action. The host may query the PMIC register space to determine the cause. Once host determines the cause, the host may clear the status register individually or by writing ‘1’ to global status clear register in Table 124, Register 0x14 [0].

In I2C mode, for supported CCC, the PMIC supports parity function. When PMIC detects parity error, the PMIC sets the register Table 114, Register 0x0A [2], and it continues to operate as normal and allows access to all registers. See Section 5.4.6 to 5.4.9 for additional details. The host is responsible for taking any specific action. The host may query the PMIC register space to determine the cause. Once host determines the cause, the host may clear the status register individually or by writing ‘1’ to global status clear register in Table 124, Register 0x14 [0].
