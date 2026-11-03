---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 2.7.21
title: Valid VIN_Mgmt Supply Detection in Switchover Mode
pages: 44-45
---
# 2.7.21 Valid VIN_Mgmt Supply Detection in Switchover Mode

When PMIC is in switchover mode as described in clause 2.7.20, the VIN_Mgmt input supply may power back up at any time. When VIN_Mgmt input supply re-powers backup, the PMIC sets the register Table 141, “Register 0x33” [4] and drives GSI_n output signal as shown in Table 27 at the same time. The PMIC continues to operate as normal and automatically switches back to VIN_Mgmt input supply. The PMIC allows access to all registers. The host is responsible for taking any specific action.The host may query the PMIC register space to determine the cause of the GSI_n signal assertion. Once host determines the cause, the host may clear the status register individually or by writing ‘1’ to global status clear register in Table 110, “Register 0x14” [0] which triggers the GSI_n signal to be de-asserted. No further action is needed by the host or the PMIC at this point.

Note that this event is treated differently by the PMIC. When host clears this event, the PMIC must remove the GSI_n signal assertion even though PMIC still sees valid VIN_Mgmt. This is to simplify host because host knows that VIN_Mgmt input supply is back and so host expects the PMIC (as well as system) to continue to run normal and host should not have to worry about masking this event in PMIC. It is assumed that if at some point VIN_Mgmt supply goes below the threshold again, PMIC will detect it and assert GSI_n output signal as described in clause 2.7.20. At this point, PMIC will be ready to assert GSI_n output signal again if VIN_Mgmt input supply re-powers back up again.

2.7.22 Packet Error Code (PEC) and Parity Error Event In I3C Basic mode, on PMIC’s primary management interface, PEC function and Parity function can be enabled. If enabled, when PMIC detects either PEC error or Parity Error, the PMIC sets the register Table 100, “Register 0x0A” [3:2] appropriately, drives GSI_n output signal as shown in Table 27 and it continues to operate as normal and allows access to all registers. See clause 2.10.8 to 2.10.9 for additional details. The host is responsible for taking any specific action. The host may query the PMIC register space to determine the cause of the GSI_n signal assertion. Once host determines the cause, the host may clear the status register individually or by writing ‘1’ to global status clear register in Table 110, “Register 0x14” [0] which triggers the GSI_n signal to be de-asserted. No further action is needed by the host from this point on.
