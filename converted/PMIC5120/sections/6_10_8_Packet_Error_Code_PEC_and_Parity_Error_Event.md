---
document: JESD301-6 (PMIC5120 Power Management IC Standard, Version 1.0, February 2025)
device: PMIC5120
application: client
section: 6.10.8
title: Packet Error Code (PEC) and Parity Error Event
pages: 63-63
---
# 6.10.8 Packet Error Code (PEC) and Parity Error Event

In I3C mode, PEC function and parity function can be enabled. If enabled, when PMIC detects either PEC error or

Parity Error, the PMIC sets the register Table 106, Register 0x0A [3:2] appropriately, drives GSI_n output signal as shown in Table 30 and it continues to operate as normal and allows access to all registers. See Section 6.18.6 to

6.18.9 for additional details. The host is responsible for taking any specific action. The host may query the PMIC register space to determine the cause of the GSI_n signal assertion. Once host determines the cause, the host may clear the status register individually or by writing ‘1’ to global status clear register in Table 116, Register 0x14 [0] which triggers the GSI_n signal to be de-asserted.

In I2C mode, for supported CCC, the PMIC supports parity function. When PMIC detects parity error, the PMIC sets the register Table 106, Register 0x0A [2], drives GSI_n output signal as shown in Table 30 and it continues to operate as normal and allows access to all registers. See Section 6.18.6 to 6.18.9 for additional details. The host is responsible for taking any specific action. The host may query the PMIC register space to determine the cause of the GSI_n signal assertion. Once host determines the cause, the host may clear the status register individually or by writing ‘1’ to global status clear register in Table 116, Register 0x14 [0] which triggers the GSI_n signal to be deasserted.
