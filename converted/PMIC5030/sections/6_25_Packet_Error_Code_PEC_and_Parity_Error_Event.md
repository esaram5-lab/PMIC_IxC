---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 6.25
title: Packet Error Code (PEC) and Parity Error Event
pages: 56-56
---
# 6.25 Packet Error Code (PEC) and Parity Error Event

In I3C Basic mode, on PMIC’s primary management interface, PEC function and Parity function can be enabled. If enabled, when PMIC detects either PEC error or Parity Error, the PMIC sets the register Table 115, Register 0x0A [3:2] appropriately, drives GSI_n output signal as shown in Table 27 and it continues to operate as normal and allows access to all registers. See clauses 7.5.6 to 7.5.7 for additional details. The host is responsible for taking any specific action. The host may query the PMIC register space to determine the cause of the GSI_n signal assertion. Once host determines the cause, the host may clear the status register individually or by writing ‘1’ to global status clear register in Table 125, Register 0x14 [0] which triggers the GSI_n signal to be de-asserted. No further action is needed by the host from this point on.
