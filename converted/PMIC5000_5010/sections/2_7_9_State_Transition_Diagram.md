---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 2.7.9
title: State Transition Diagram
pages: 33-35
---
# 2.7.9 State Transition Diagram

Following is a summary of high level description of basic PMIC states. Offline State:

```text
• VIN_Mgmt is invalid and VIN_Bulk = X (valid or invalid); LDOs are invalid
• All registers are reset to specified default values

• CAMP is Hi-Z
```

Configuration (non write protect) state:

• At initial configuration state, all registers follow the register attributes as defined and read/write accessible.

```text
    • The I2C/I3C bus interface is alive and running.
    • LDOs are valid; switch regulators are off
    • CAMP is low

Regulation (non write protect) state:
```

• All registers are read/write accessible.

• All enabled output rails are active

• Internal power good is floated; external CAMP is low

Online (write protect) state:

```text
• All registers are readable. All non protect registers are writable.
• All enabled output rails are active,i.e., PMIC has registered VR Enable command with Table 137, “Register
  0x2F” = ‘0’.
• CAMP is high
• Note: Prior to PMIC registering VR Enable command, PMIC may be configured to not execute VR Enable
  command and float its CAMP PWR_GOOD output signal (Table 140, “Register 0x32” = 0x08) with default
  configuration of Table 137, “Register 0x2F” = ‘0’. In this configuration, PMIC also enters write protect state
  when CAMP signal is pulled high.
```

Figure 17 shows high level simplified state diagram. Specific transition details are function of PMIC’s configuration register settings (e.g., R2F, R32, etc., as well as CAMP signal and input/output supplies). Please refer to detail functional description and configuration register definition for PMIC operation. Consider an example of a valid PMIC operation: When the PMIC first powers up from an offline state, the PMIC register Table 137, “Register 0x2F” [2] can be configured to ‘1’ followed by VR Enable command. After PMIC turns on all regulators and floats CAMP signal such that it is pulled up High, PMIC is in online state but allows all register write/read access as PMIC is not in write protect state. In this state, the PMIC does allow to clear Table 137, “Register 0x2F” [2] to ‘0’ which will cause PMIC to enter in write protect state as the CAMP signal was already pulled up High and the PMIC was in regulation.

```text
                                                      Offline

                                                                         Valid VIN_Mgmt;
                                                                      Valid 1.8V & 1.0V LDOs
 Invalid LDO or invalid
VIN_Bulk & VIN_Mgmt                                                       Invalid 1.8V or 1.0V LDOs

                                                  Configuration
                                                   Non Write
                                                    Protect

                                                                                   VR Disable

                                                                                   VR Enable

                                                   Regulation                          PMIC isolation with
                                                                                       CAMP @ logic high
                                                   Non Write
                                                    Protect

VIN_Bulk invalid or CAMP                                                           CAMP @ logic
@ logic low & R32[4] = 0                                                         low & R32[4] = 1

                                                                                    CAMP @
                                                                                   logic high

                                                    Online
                                                     Write
                                                    Protect
```

*Figure 17 — High Level State Transitions* (figure; any text below/above was extracted from the drawing)
