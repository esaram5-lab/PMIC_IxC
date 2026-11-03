---
document: JESD301-2 (PMIC5100 Power Management IC Standard, Rev. 1.03, October 2022)
device: PMIC5100
application: client
section: 6.10.8
title: Packet Error Code (PEC) and Parity Error Event
pages: 60-60
---
# 6.10.8 Packet Error Code (PEC) and Parity Error Event

In I3C mode, PEC function and parity function can be enabled. If enabled, when PMIC detects either PEC error or parity error, the PMIC sets the register Table 98, “Register 0x0A” [3:2] appropriately, drives GSI_n output signal as shown in Table 28 and it continues to operate as normal and allows access to all registers. See clauses 6.17.5 to 6.17.9 for additional details. The host is responsible for taking any specific action. The host may query the PMIC register space to determine the cause of the GSI_n signal assertion. Once host determines the cause, the host may clear the status register individually or by writing ‘1’ to global status clear register in Table 108, “Register 0x14” [0] which triggers the GSI_n signal to be de-asserted. In I2C mode, for supported CCC, the PMIC supports parity function. When PMIC detects parity error, the PMIC sets the register Table 98, “Register 0x0A” [2], drives GSI_n output signal as shown in Table 28 and it continues to operate as normal and allows access to all registers. See Clauses 6.17.6 to 6.17.9 for additional details. The host is responsible for taking any specific action. The host may query the PMIC register space to determine the cause of the GSI_n signal assertion. Once host determines the cause, the host may clear the status register individually or by writing ‘1’ to global status clear register in Table 108, “Register 0x14” [0] which triggers the GSI_n signal to be de-asserted.
