---
document: JESD301-6 (PMIC5120 Power Management IC Standard, Version 1.0, February 2025)
device: PMIC5120
application: client
section: 7.2.6
title: Status Registers
pages: 113-115
---
# 7.2.6 Status Registers

The DDR5 PMIC offers status registers that are grouped into four different categories.

```text
1.   Global History of Error Log Register (Table 100, Register 0x04 [7:4])
2.   Error Log Registers (Table 101, Register 0x05 [6,4:0], Table 102, Register 0x06[7,5:3,1:0], Table 103,
     Register 0x07 [7:0]; Table 103, Register 0x07 [7:0] is currently defined as Reserved)
3.   Real time Status Registers (Table 104, Register 0x08 [6:5,3:2,0], Table 105, Register 0x09 [7,5,3,1:0],
     Table 106, Register 0x0A [7,5:1], Table 107, Register 0x0B [7,5:3,1:0], Table 147, Register 0x33 [2])
4.   Periodic Status Registers (Table 108, Register 0x0C [7:0], Table 110, Register 0x0E [7:0], Table 111,
     Register 0x0F [7:0], Table 147, Register 0x33 [7:5])
```

Global History of Error Log Register (Table 100, Register 0x04 [7:4]) - This register records the PMIC state at each abnormal power down cycle. This register reports the cumulative error of each abnormal power down sequence. The PMIC writes this register on its own when it internally generates VR Disable command on its own due to failure. The host can erase this register in MTP memory and clear the status register by writing the code 0x74 in Table 153, Register 0x39.

Error Log Registers (Table 101, Register 0x05 [6,4:0], Table 102, Register 0x06 [7,5:3,1:0],Table 103, Register 0x07 [7:0]).

```text
       • These registers record the PMIC state at each power down sequence. The PMIC may report an abnormal
         power down sequence or a normal power down sequence. The PMIC writes these registers and updates
         MTP when it internally generates a VR Disable command on its own due to failure. At the next power up,
         the registers are restored from MTP to be read by the host, and MTP is cleared by the PMIC. A value of
         ‘0’ in the register indicates that no fault event occurred prior to the previous power down cycle.
       • The host can clear the status registers and MTP by writing the code 0x74 in Table 153, Register 0x39.
       • See Figure 42 for illustration. The top waveform illustrates how PMIC captures Error Log Registers (R05
         to R07) when there is a fault and how PMIC reports error log registers when PMIC goes through power
         cycle. The bottom waveform illustrates same as top waveform with one exception. It shows no fault con-
         dition when PWR_GOOD is asserted to turn off switch regulator outputs with power down sequence.
       • The phrase “Power Cycle” is used interchangeably with “Power Down Cycle” as illustrated in both figures
         and it means the VIN_Bulk input supply is removed and re-applied. “Power Down Sequence” means exe-
         cution of Power Off Sequence configuration registers (Table 176, Register 0x58 to Table 179, Register
         0x5B).

                                Power (Down) Cycle: Off + On

  VIN_Bulk

PWR_GOOD
                                                                                        ng         No Fault

   VOUTx

               VR                                            VR                                                                        VR

              Enable                                        Enable                                                                    Enable
                       Fault   R05, R06             Read             Fault   R05, R06    Read       No Event            Read                   Fault   R05, R06    Read
                       Event     Log                Error            Event     Log       Error         To               Error                  Event     Log       Error
                               Capture               Log                     Capture     Log        Capture              Log                           Capture     Log
                                                                                                                      R05, R06
                                                  R05, R06                              R05, R06                                                                  R05, R06
                                                                                                                       = 0x00

                                Power (Down) Cycle: Off + On

  VIN_Bulk

PWR_GOOD

   VOUTx

               VR                                            VR                                    VR                                  VR
              Enable                                        Enable                                Enable                              Enable
                       Fault   R05, R06             Read             Fault   R05, R06     Read             No Event         Read               Fault   R05, R06    Read
                       Event     Log                Error            Event     Log        Error               to             Error             Event     Log       Error
                               Capture               Log                     Capture      Log              Capture           Log                       Capture     Log
                                                                                                                           R05, R06
                                                  R05, R06                              R05, R06                                                                  R05, R06
                                                                                                                            = 0x00
```

*Figure 42 — Error Log (R05 to R07) Registers Behavior with Power Cycle* (figure; any text below/above was extracted from the drawing)

Real Time Status Registers (Table 104, Register 0x08 [6:5,3:2,0], Table 105, Register 0x09 [7,5,3,1:0], Table 106, Register 0x0A [7,5:1], to Table 107, Register 0x0B [7,5:3,1:0], Table 147, Register 0x33 [2]): These registers are updated to ‘1’ any time based on any event that occurs. The status registers will remain at ‘1’ even if the failing condition is no longer present until the Clear Register command is received by the PMIC. The GSI_n interrupt or PWR_GOOD interrupt may be generated by the PMIC at the same time depending on the type of event. The interrupts are only generated if they are not masked. The status registers Table 104, Register 0x08 [7], Table 105, Register 0x09 [5] and Table 147, Register 0x33 [2] is only valid once valid VIN_Bulk input supply is valid at the PMIC input pin. The remaining status registers are valid after VR Enable command is registered.

Periodic Status Registers (Table 108, Register 0x0C [7:0], Table 110, Register 0x0E [7:0], Table 111, Register 0x0F [7:0], Table 147, Register 0x33 [7:5]) - These registers are updated periodically. These registers are only valid after VR Enable command is registers.

All Read Only (RO) registers except for registers Table 108, Register 0x0C [7:0], Table 110, Register 0x0E [7:0] and Table 111, Register 0x0F [7:0] are one time latched registers. In other words, once PMIC sets those register flag, the host must explicitly clear those registers appropriately. The PMIC does not automatically update the registers on its own even if the event that triggered the status is no longer present. The registers Table 108, Register 0x0C [7:0], Table 110, Register 0x0E [7:0] and Table 111, Register 0x0F [7:0] are dynamically updated by the PMIC at certain frequency and they represent the status at that point.
