---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 6.12
title: State Transition Diagram
pages: 41-45
---
# 6.12 State Transition Diagram

Following is a summary of high level description of basic PMIC states. Offline State:

```text
▪ VIN_Mgmt is invalid and VIN_Bulk = X (valid or invalid); LDOs are invalid
▪ All registers are reset to specified default values
▪ CAMP is Hi-Z
```

Configuration (non write-protect) state:

```text
    ▪ At initial configuration state, all registers follow the register attributes as defined and read/write
      accessible.
    ▪ The I2C/I3C bus interface is alive and running.
    ▪ LDOs are valid; switch regulators are off
    ▪ CAMP is low

Regulation (non write-protect) state:
    ▪ All registers are read/write accessible.
    ▪ All enabled output rails are active
    ▪ Internal power good is floated; external CAMP is low

Online (write-protect) state:
    ▪ All registers are readable. All non protect registers are writable.
    ▪ All enabled output rails are active (i.e., PMIC has registered VR Enable command with Table 152,
      Register 0x2F [2] = ‘0’.
    ▪ CAMP is high
    ▪ Note: Prior to PMIC registering VR Enable command, PMIC may be configured to not execute VR

      Enable command and float its CAMP PWR_GOOD output signal (Table 155, Register 0x32 [7:0] =
      0x08) with default configuration of Table 152, Register 0x2F [2] = ‘0’. In this configuration, PMIC

      also enters write-protect state when CAMP signal is pulled high.
```

Figure 21 shows high level simplified state diagram. Specific transition details are function of PMIC’s configuration register settings (e.g., R2F, R32, etc., as well as CAMP signal and input/output supplies). Please refer to detail functional description and configuration register definition for PMIC operation. Consider an example of a valid PMIC operation: When the PMIC first powers up from an offline state, the PMIC register Table 152, Register 0x2F [2] can be configured to ‘1’ followed by VR Enable command. After PMIC turns on all regulators and floats CAMP signal such that it is pulled up High, PMIC is in online state but allows all register write/read access as PMIC is not in write-protect state. In this state, the PMIC does allow to clear Table 152, Register 0x2F [2] to ‘0’ which will cause PMIC to enter in write-protect state as the CAMP signal was already pulled up High and the PMIC was in regulation.

## 6.12.1 State Transition with VR_OE Pin

Table 26 shows the high level state transition with using VR OE pin if Table 263, Register 0x5F [5] = ‘1’. The table only shows the transition using the VR OE pin to turn on and turn off the regulators along with CAMP signal transition. The PMIC LDOs must be valid to turn on the rails with the VR OE pin. The failure in LDOs returns PMIC in offline state regardless of the VR OE pin level.

**Table 26 — State Transitions with VR Enable Pin**

```text
                                                             Register Setting                                          Power
                                                                                                          CAMP          Cycle
 Start State                  Activity                R2F[2]     R32[5]     R32[4]      End State        Output[1]    Required?     Note

   Offline         Valid VIN_Bulk & VIN_Mgmt            N/A        N/A       N/A      Configuration         Low          N/A

Configuration        VR_OE Pin; Low to High              X          0           X     Configuration         Low          No
   State                                                                                                                              [2]
                                                         X          1           X     Regulation -->       Hi-Z          No
                                                                                         Online

   Online            VR_OE Pin; High to Low              X          X           X     Configuration         Low          No           [3]

   Online            CAMP Input; High to Low             X          X           0     Configuration         Low          No           [4]

                                                         X          X           1      Regulation          Hi-Z          No           [5]

                   Internal VR Disable Event or          X          X           X     Configuration         Low          No
                         VIN_Bulk Invalid

                   Invalid VIN_Bulk & VIN_Mgmt           X          X           X         Offline       Undefined        N/A
 NOTE 1        This represents PMIC’s CAMP output signal.
 NOTE 2        The PMIC transitions to regulation state first and then to online state when CAMP signal is pulled up high. The Table 152,
               Register 0x2F [2] decides whether PMIC is in write-protect state or non-write-protect state. The PMIC updates the Table 155,
               Register 0x32 [7] to ‘1’ when it transitions to regulation state.

 NOTE 3        The PMIC updates the Table 155, Register 0x32 [7] to ‘0’ when it transitions to configuration state.
 NOTE 4        The PMIC returns to non-write-protect configuration state.

 NOTE 5        The PMIC returns to non-write-protect regulation state.

                                                     Offline

                                                                     Valid VIN_Mgmt;
                                                                  Valid 1.8V & 1.0V LDOs
      Invalid LDO or invalid
     VIN_Bulk & VIN_Mgmt                                              Invalid 1.8V or 1.0V LDOs

                                                  Configuration
                                                   Non Write
                                                    Protect
                                                                               VR Disable

                                                                               VR Enable

                                                   Regulation                      PMIC isolation with
                                                                                   CAMP @ logic high
                                                   Non Write
                                                    Protect

     VIN_Bulk invalid or CAMP                                                  CAMP @ logic
     @ logic low & R32[4] = 0                                                low & R32[4] = 1

                                                                                CAMP @
                                                                               logic high

                                                    Online
                                                     Write
                                                    Protect
```

*Figure 21 — High Level State Transitions* (figure; any text below/above was extracted from the drawing)
