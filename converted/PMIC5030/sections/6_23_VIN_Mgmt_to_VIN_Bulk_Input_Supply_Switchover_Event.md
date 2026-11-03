---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 6.23
title: VIN_Mgmt to VIN_Bulk Input Supply Switchover Event
pages: 55-56
---
# 6.23 VIN_Mgmt to VIN_Bulk Input Supply Switchover Event

After VR Enable command is registered, the PMIC automatically switches over from VIN_Mgmt to VIN_Bulk input supply under the following condition.

1. VIN_Mgmt goes below the threshold set in register Table 152, Register 0x2F [7]. When the above event occurs for a period longer than tInput_PWR_GOOD_GSI_Assertion time then PMIC sets the register Table 114, Register 0x09 [4] and drives GSI_n output signal as shown in Table 27 at the same time. The PMIC continues to operate as normal. The host is responsible for taking any specific action. The host may query the PMIC register space to determine the cause of the GSI_n signal assertion. Once host determines the cause, the host may clear the status register individually or by writing ‘1’ to global status clear register in Table 125, Register 0x14 [0] which triggers the GSI_n signal to be de-asserted. No further action is needed by the host or the PMIC at this point. Note that this event is treated differently by the PMIC. When host clears this event, the PMIC must remove the GSI_n signal assertion even though PMIC does not see valid VIN_Mgmt. This is to simplify host because host knows that there is no VIN_Mgmt and yet host expects the PMIC (as well as system) to continue to run normal and host should not have to worry about masking this event in PMIC. It is assumed that at some point VIN_Mgmt supply will come back up again, PMIC will detect it and assert GSI_n output signal as described in clause 6.24. At this point, PMIC will be ready to assert GSI_n output signal again if VIN_Mgmt input supply goes below the threshold set in register Table 152, Register 0x2F [7].
