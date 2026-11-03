---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 8.4.1
title: Status Registers
pages: 133-146
---
# 8.4.1 Status Registers

The DDR5 PMIC offers status registers that are grouped into four different categories.

```text
1.      Global History of Error Log Register (Table 108, Register 0x04 [7:4])
2.      Error Log Registers (Table 109, Register 0x05 [6:0], Table 110, Register 0x06 [7:0], Table 111,
        Register 0x07 [7:0]; Table 111, Register 0x07 [7:0] is currently defined as Reserved)
3.      Real time Status Registers (Table 112, Register 0x08 [6:2,0], Table 113, Register 0x09 [7,5,3:0],
        Table 114, Register 0x0A [7:0], Table 115, Register 0x0B [7:0], Table 155, Register 0x33 [4:2],
        Table 173, Register 0x109 [0])
4.      Periodic Status Registers (Table 116, Register 0x0C, Table 117, Register 0x0D, Table 118, Register
        0x0E, Table 119, Register 0x0F, Table 155, Register 0x33 [7:5], Table 168, Register 0x100,
        Table 169, Register 0x102, Table 170, Register 0x103, Table 171, Register 0x104, Table 172,
        Register 0x105)
```

Global History of Error Log Register (Table 108, Register 0x04 [7:4]) - This register records the PMIC state at each abnormal power down cycle. This register reports the cumulative error of each abnormal power down sequence. The PMIC writes this register on its own when it internally generates VR Disable command on its own due to failure. The host can erase this register in MTP memory and clear the status register by writing the code 0x74 in Table 161, Register 0x39.

```text
   ▪ Error Log Registers (Table 109, Register 0x05 [6:0], Table 110, Register 0x06 [7:0], Table 111,
     Register 0x07 [7:0]) - These registers record the PMIC state at each power down sequence. The

     PMIC may report an abnormal power down sequence or a normal power down sequence. The
     PMIC writes these registers and updates MTP when it internally generates a VR Disable command

     on its own due to failure. At the next power up, the registers are restored from MTP to be read by
     the host, and MTP is cleared by the PMIC. A value of ‘0’ in the register indicates no fault event
     occurred prior to previous power down cycle.
   ▪ The host can clear the status registers and MTP by writing the code 0x74 in Table 161, Register
     0x39.
   ▪ See Figure 43 for illustration. The top waveform illustrates how PMIC captures Error Log Registers
     (Table 109, Register 0x05 to Table 111, Register 0x07) when there is a fault and how PMIC reports
     error log registers when PMIC goes through power cycle. The bottom waveform illustrates same as
     top waveform with one exception. It shows no fault condition when PWR_GOOD is asserted to turn
     off switch regulator outputs with power down sequence. The phrase “Power Cycle” is used
     interchangeably with “Power Down Cycle” as illustrated in both figures and it means VIN_Bulk input
     supply is removed and re-applied. “Power Down Sequence” means execution of Power Off
     Sequence configuration registers (Table 200, Register 0x58 to Table 203, Register 0x5B).

                                         Power (Down) Cycle: Off + On

VIN_Bulk

PWR_GOOD

                                                                                                                No Fault
           VOUTx

                      VR                                                   VR                                                                  VR
                    Enable                                               Enable                                                              Enable
                             Fault                                                Fault                                                               Fault
                                     R05, R06                    Read                     R05, R06    Read         No Event         Read                      R05, R06    Read
                             event                                                event                                                               event
                                       Log                       Error                      Log       Error           to            Error                       Log       Error
                                     capture                      Log                     capture      Log         Capture           Log                      capture      Log
                                                                                                                                  R05, R06
                                                               R05, R06                              R05, R06                                                            R05, R06
                                                                                                                                   = 0x00

                                          Power (Down) Cycle: Off + On

VIN_Bulk

PWR_GOOD

           VOUTx

                      VR                                                   VR                                   VR                             VR
                    Enable                                               Enable                               Enable                         Enable
                             Fault                                                Fault                                                               Fault
                                     R05, R06                    Read                     R05, R06    Read                          Read                      R05, R06    Read
                             event                                                event                                                               event
                                       Log                       Error                      Log       Error                         Error                       Log       Error
                                     capture                      Log                     capture      Log                           Log                      capture      Log

                                                               R05, R06
                                                                                                     R05, R06
                                                                                                                       No Event   R05, R06
                                                                                                                                                                         R05, R06
                                                                                                                          to       = 0x00
                                                                                                                       captu re
```

*Figure 43 — Error Log (R05 to R07) Registers Behavior with Power Cycle* (figure; any text below/above was extracted from the drawing)

Real Time Status Registers (Table 112, Register 0x08 [6:2,0], Table 113, Register 0x09 [7,5,3:0], Table 114, Register 0x0A [7:1], Table 115, Register 0x0B [7:0], Table 155, Register 0x33 [2]) - These registers are updated to ‘1’ any time based on any event that occurs. The status registers will remain at ‘1’ even if the failing condition is no longer present until the Clear Register command is received by the PMIC. Note that any switch regulator related status registers are only applicable after VR Enable command is registered by the PMIC. The PMIC updates switch regulators related status registers after VR Enable command is registered within tPMIC_PWR_GOOD_OUT time if there is any issue and host shall check these status registers if there is any event related to switch regulators in future. The PWR_GOOD interrupt may be generated by the PMIC at the same time depending on the type of event. The interrupts are only generated if they are not masked. The status registers Table 112, Register 0x08 [7], Table 113, Register 0x09 [5], and Table 155, Register 0x33 [2] is only valid once valid VIN_Bulk input supply is valid at the PMIC input pin. The remaining status registers are valid after VR Enable command is registered. Periodic Status Registers (Table 116, Register 0x0C, Table 117, Register 0x0D, Table 118, Register 0x0E, Table 119, Register 0x0F, Table 155, Register 0x33 [7:5]) - These registers are updated periodically. These registers are only valid after VR Enable command is registered. All Read Only (RO) registers except for registers Table 116, Register 0x0C, Table 117, Register 0x0D, Table 118, Register 0x0E, Table 119, Register 0x0F, and Table 155, Register 0x33 [7:5] are one time latched registers. In other words, once PMIC sets those register flag, the host must explicitly clear those registers appropriately. The PMIC does not automatically update the registers on its own even if the event that triggered the status is no longer present. The registers Table 116, Register 0x0C, Table 117, Register 0x0D, Table 118, Register 0x0E, Table 119, Register 0x0F, and Table 155, Register 0x33 are dynamically updated by the PMIC at certain frequency and they represent the status at that point.

**Table 108 — Register 0x04**: see [`registers/0x04.md`](../registers/0x04.md)

**Table 109 — Register 0x05**: see [`registers/0x05.md`](../registers/0x05.md)

**Table 110 — Register 0x06**: see [`registers/0x06.md`](../registers/0x06.md)

**Table 111 — Register 0x07**: see [`registers/0x07.md`](../registers/0x07.md)

**Table 112 — Register 0x08**: see [`registers/0x08.md`](../registers/0x08.md)

**Table 113 — Register 0x09**: see [`registers/0x09.md`](../registers/0x09.md)

**Table 114 — Register 0x0A**: see [`registers/0x0A.md`](../registers/0x0A.md)

**Table 115 — Register 0x0B**: see [`registers/0x0B.md`](../registers/0x0B.md)

**Table 116 — Register 0x0C**: see [`registers/0x0C.md`](../registers/0x0C.md)

**Table 117 — Register 0x0D**: see [`registers/0x0D.md`](../registers/0x0D.md)

**Table 118 — Register 0x0E**: see [`registers/0x0E.md`](../registers/0x0E.md)

**Table 119 — Register 0x0F**: see [`registers/0x0F.md`](../registers/0x0F.md)
