---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 6.24
title: Valid VIN_Mgmt Supply Detection in Switchover Mode
pages: 56-56
---
# 6.24 Valid VIN_Mgmt Supply Detection in Switchover Mode

When PMIC is in switchover mode as described in clause 6.23, the VIN_Mgmt input supply may power back up at any time. When VIN_Mgmt input supply re-powers back up, the PMIC sets the register Table 157, Register 0x33 [4] and drives GSI_n output signal as shown in Table 27 at the same time. The PMIC continues to operate as normal and automatically switches back to VIN_Mgmt input supply. The host is responsible for taking any specific action. The host may query the PMIC register space to determine the cause of the GSI_n signal assertion. Once host determines the cause, the host may clear the status register individually or by writing ‘1’ to global status clear register in Table 125, Register 0x14 [0] which triggers the GSI_n signal to be de-asserted. No further action is needed by the host or the PMIC at this point. Note that this event is treated differently by the PMIC. When host clears this event, the PMIC must remove the GSI_n signal assertion even though PMIC still sees valid VIN_Mgmt. This is to simplify host because host knows that VIN_Mgmt input supply is back and so host expects the PMIC (as well as system) to continue to run normal and host should not have to worry about masking this event in PMIC. It is assumed that if at some point VIN_Mgmt supply goes below the threshold again, PMIC will detect it and assert GSI_n output signal as described in Clause 6.23. At this point, PMIC will be ready to assert GSI_n output signal again if VIN_Mgmt input supply re-powers back up again.
