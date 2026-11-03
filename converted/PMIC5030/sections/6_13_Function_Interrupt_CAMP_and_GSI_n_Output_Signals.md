---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 6.13
title: Function Interrupt - CAMP and GSI_n Output Signals
pages: 45-50
---
# 6.13 Function Interrupt - CAMP and GSI_n Output Signals

This clause defines the output functionality of GSI_n pin and CAMP pin. When mask register bits are not set, the PMIC asserts its GSI_n output and CAMP output signals as shown in Table 27 when any event occurs. The table also highlights 15 events that cause the PMIC to generate an internal VR Disable command. For remaining events that do not trigger an internal VR Disable command, the PMIC continues to operate as normal.

**Table 27 — Events Interrupt Summary**

```text
                                                                                           Trigger
                                   Status     Clear      Mask                                VR      CAMP     GSI_n
              Event                  Bit       Bit        Bit        Threshold Bits       Disable?   Output   Output

VIN_Bulk Power Good               R08 [7]    R10 [7]    R15 [7]         R1A [7:5]           No        Low      Low

VIN_Bulk Over Voltage             R08 [0]    R10 [0]    R15 [0]          R1B [7]            Yes       Low      Low

VIN_Mgmt Over Voltage             R08 [1]    R10 [1]    R15 [1]          R1B [5]            No        High     Low

SWA Output Power Good             R08 [5]    R10 [5]    R15 [5]     R21 [0]; R22 [7:6]      No        Low      Low
SWB Output Power Good             R08 [4]    R10 [4]    R15 [4]     R23 [0]’ R24 [7:6]      No        Low      Low
SWC Output Power Good             R08 [3]    R10 [3]    R15 [3]     R25 [0]; R26 [7:6]      No        Low      Low
SWD Output Power Good             R08 [2]    R10 [2]    R15 [2]     R27 [0]; R28 [7:6]      No        Low      Low
SWE Output Power Good             R108 [7]   R10E [7]   R114 [7]   R11D [0]; R11E [7:6]     No        Low      Low
SWF Output Power Good             R108 [6]   R10E [6]   R114 [6]   R11F [0]; R120 [7:6]     No        Low      Low

1.8 V LDO Power Good              R09 [5]    R11 [5]    R16 [5]          R1A [2]            No        Low      Low
1.0 V LDO Power Good              R33 [2]    R14 [2]    R19 [2]          R1A [0]            No        Low      Low

VBias1 or VBias2 LDO Power Good   R09 [6]    R11 [6]    R16 [6]          R1A [3]            No        Low      Low

SWA Output Over Voltage           R0A [7]    R12 [7]    R17 [7]         R22 [5:4]           Yes       Low      Low
SWB Output Over Voltage           R0A [6]    R12 [6]    R17 [6]         R24 [5:4]           Yes       Low      Low
SWC Output Over Voltage           R0A [5]    R12 [5]    R17 [5]         R26 [5:4]           Yes       Low      Low
SWD Output Over Voltage           R0A [4]    R12 [4]    R17 [4]         R28 [5:4]           Yes       Low      Low
SWE Output Over Voltage           R108 [3]   R10E [3]   R114 [3]       R11E [5:4]           Yes       Low      Low
SWF Output Over Voltage           R108 [2]   R10E [2]   R114 [2]       R120 [5:4]           Yes       Low      Low

SWA Output Under Voltage          R0B [3]    R13 [3]    R18 [3]         R22 [3:2]           Yes       Low      Low
SWB Output Under Voltage          R0B [2]    R13 [2]    R18 [2]         R24 [3:2]           Yes       Low      Low
SWC Output Under Voltage          R0B [1]    R13 [1]    R18 [1]         R26 [3:2]           Yes       Low      Low
SWD Output Under Voltage          R0B [0]    R13 [0]    R18 [0]         R28 [3:2]           Yes       Low      Low
SWE Output Under Voltage          R109 [7]   R10F [7]   R115 [7]       R11E [3:2]           Yes       Low      Low
SWF Output Under Voltage          R109 [6]   R10F [6]   R115 [6]       R120 [3:2]           Yes       Low      Low

VBias1 or VBias 2 LDO Output or   R33 [3]    R14 [3]    R19 [3]      Vendor Specific        Yes       Low      Low
VIN_Bulk Input Under Voltage

SWA Output Current Limit          R0B [7]    R13 [7]    R18 [7]         R20 [7:6]           No        High     Low
SWB Output Current Limit          R0B [6]    R13 [6]    R18 [6]         R20 [5:4]           No        High     Low
SWC Output Current Limit          R0B [5]    R13 [5]    R18 [5]         R20 [3:2]           No        High     Low
SWD Output Current Limit          R0B [4]    R13 [4]    R18 [4]         R20 [1:0]           No        High     Low
SWE Output Current Limit          R108 [1]   R10E [1]   R114 [1]       R11C [7:6]           No        High     Low
SWF Output Current Limit          R108 [0]   R10E [0]   R114 [0]       R11C [5:4]           No        High     Low

                                                                                          Trigger
                                       Status      Clear      Mask                          VR      CAMP     GSI_n
               Event                     Bit        Bit        Bit      Threshold Bits   Disable?   Output   Output

SWA Output High Current/Power          R09 [3]    R11 [3]    R16 [3]      R1C [7:0]        No        High     Low
SWB Output High Current/Power          R09 [2]    R11 [2]    R16 [2]      R1D [7:0]        No        High     Low
SWC Output High Current/Power          R09 [1]    R11 [1]    R16 [1]      R1E [7:0]        No        High     Low
SWD Output High Current/Power          R09 [0]    R11 [0]    R16 [0]      R1F [7:0]        No        High     Low
SWE Output High Current/Power          R108 [5]   R10E [5]   R114 [5]     R11A [7:0]       No        High     Low
SWF Output High Current/Power          R108 [4]   R10E [4]   R114 [4]     R11B [7:0]       No        High     Low

High Temperature Warning               R09 [7]    R11 [7]    R16 [7]      R1B [2:0]        No        High     Low

Critical Temperature                    R08[6]      N/A        N/A        R2E [2:0]        Yes       Low      Low

VIN_Mgmt to VIN_Bulk Switchover        R09 [4]    R11 [4]    R16 [4]       R2F [7]         No        High     Low

Valid VIN_Mgmt in Switchover State     R33 [4]    R14 [4]    R19 [4]         N/A           No        High     Low

PEC Error                              R0A [3]    R12 [3]    R17 [3]         N/A           No        High     Low

Parity Error                           R0A [2]    R12 [2]    R17 [2]         N/A           No        High     Low

    The host is expected to read appropriate status registers to determine and isolate the cause of the GSI_n
    signal assertion or CAMP signal assertion. The host may attempt to clear or mask the appropriate
    corresponding interrupt event. The PMIC keeps the GSI_n signal asserted or CAMP signal asserted until

    the appropriate corresponding registers are explicitly cleared or masked by the host. Table 28 and
    Table 29 shows the PMIC’s response of GSI_n signal and CAMP output signal for each event before and

    after host issues the Clear command. Table 28 and Table 29 assume that all mask bits are either ‘0’ or ‘1’
    for simplicity.
```

**Table 28 — PMIC Response for Clear Command by Host - 1**

```text
                                                           Clear Command;                              Clear Command;
                                    Event Occurred;       Event Not Present;    Event Occurred;       Event Not Present;
                                    All Mask Bits = ‘0’   All Mask Bits = ‘0’   All Mask Bits = ‘1’   All Mask Bits = ‘1’

                                                          R2F [1:0] = ‘00’ or
                                                             ‘01’ or ‘10’        R2F [1:0] = ‘00’       R2F [1:0] = ‘00’

                                    CAMP       GSI_n      CAMP       GSI_n      CAMP       GSI_n      CAMP        GSI_n
              Event                 Output     Output     Output     Output     Output     Output     Output      Output

VIN_Bulk Power Good                   Low        Low       High       High       Low        High       High        High

VIN_Bulk Over Voltage                 Low        Low        Low       High       Low        High        Low        High

VIN_Mgmt Over Voltage                High        Low       High       High       High       High       High        High

SWA Output Power Good                 Low        Low       High       High       Low        High       High        High
SWB Output Power Good                 Low        Low       High       High       Low        High       High        High
SWC Output Power Good                 Low        Low       High       High       Low        High       High        High
SWD Output Power Good                 Low        Low       High       High       Low        High       High        High
SWE Output Power Good                 Low        Low       High
                                                              ng      High       Low        High       High        High
SWF Output Power Good                 Low        Low       High       High       Low        High       High        High

1.8 V LDO Power Good                  Low        Low       High       High       Low        High       High        High

1.0 V LDO Power Good                  Low        Low       High       High       Low        High       High        High
VBias1or VBias2 LDO Power Good        Low        Low       High       High       Low        High       High        High

SWA Output Over Voltage               Low        Low        Low       High       Low        High        Low        High
SWB Output Over Voltage               Low        Low        Low       High       Low        High        Low        High

SWC Output Over Voltage               Low        Low        Low       High       Low        High        Low        High
SWD Output Over Voltage               Low        Low        Low       High       Low        High        Low        High
SWE Output Over Voltage               Low        Low        Low       High       Low        High        Low        High
SWF Output Over Voltage               Low        Low        Low       High       Low        High        Low        High

SWA Output Under Voltage              Low        Low        Low       High       Low        High        Low        High
SWB Output Under Voltage              Low        Low        Low       High       Low        High        Low        High
SWC Output Under Voltage              Low        Low        Low       High       Low        High        Low        High
SWD Output Under Voltage              Low        Low        Low       High       Low        High        Low        High
SWE Output Under Voltage              Low        Low        Low       High       Low        High        Low        High
SWF Output Under Voltage              Low        Low        Low       High       Low        High        Low        High

VBias1 or VBias2 LDO Output or        Low        Low        Low       High       Low        High        Low        High
VIN_Bulk Input Under Voltage

SWA Output Current Limit             High        Low       High       High       High       High       High        High
SWB Output Current Limit             High        Low       High       High       High       High       High        High
SWC Output Current Limit             High        Low       High       High       High       High       High        High
SWD Output Current Limit             High        Low       High       High       High       High       High        High
SWE Output Current Limit             High        Low       High       High       High       High       High        High
SWF Output Current Limit             High        Low       High       High       High       High       High        High

                                                             Clear Command;                              Clear Command;
                                      Event Occurred;       Event Not Present;    Event Occurred;       Event Not Present;
                                      All Mask Bits = ‘0’   All Mask Bits = ‘0’   All Mask Bits = ‘1’   All Mask Bits = ‘1’

                                                            R2F [1:0] = ‘00’ or
                                                               ‘01’ or ‘10’        R2F [1:0] = ‘00’       R2F [1:0] = ‘00’

                                      CAMP       GSI_n      CAMP        GSI_n     CAMP       GSI_n      CAMP        GSI_n
                 Event                Output     Output     Output      Output    Output     Output     Output      Output

SWA Output High Current/Power          High        Low       High        High      High       High       High        High
SWB Output High Current/Power          High        Low       High        High      High       High       High        High
SWC Output High Current/Power          High        Low       High        High      High       High       High        High
SWD Output High Current/Power          High        Low       High        High      High       High       High        High
SWE Output High Current/Power          High        Low       High        High      High       High       High        High
SWF Output High Current/Power          High        Low       High        High      High       High       High        High

High Temperature Warning               High        Low       High        High      High       High       High        High

Critical Temperature                   Low         Low       P/C[1]     P/C[1]     Low         Low       P/C[1]     P/C[1]

VIN_Mgmt to VIN_Bulk Switchover        High        Low       High        High      High       High       High        High

Valid VIN_Mgmt in Switchover           High        Low       High        High      High       High       High        High

PEC Error                              High        Low       High        High      High       High       High        High
Parity Error                           High        Low       High        High      High       High       High        High
 NOTE 1        P/C = Power Cycle
```

**Table 29 — PMIC Response for Clear Command by Host - 2**

```text
                                                             Clear Command;                              Clear Command;

                                      Event Occurred;       Event Not Present;    Event Occurred;       Event Not Present;
                                      All Mask Bits = ‘1’   All Mask Bits = ‘1’   All Mask Bits = ‘1’   All Mask Bits = ‘1’
                                       R2F [1:0] = ‘01’       R2F [1:0] = ‘01’     R2F [1:0] = ‘10’       R2F [1:0] = ‘10’
                                      CAMP       GSI_n      CAMP        GSI_n     CAMP       GSI_n      CAMP        GSI_n
                 Event                Output     Output     Output      Output    Output     Output     Output      Output
VIN_Bulk Power Good                    High        Low       High        High      High       High       High        High
VIN_Bulk Over Voltage                  Low         Low        Low        High      Low        High        Low        High
VIN_Mgmt Over Voltage                  High        Low       High        High      High       High       High        High
SWA Output Power Good                  High        Low       High        High      High       High       High        High
SWB Output Power Good                  High        Low       High        High      High       High       High        High
SWC Output Power Good                  High        Low       High        High      High       High       High        High
SWD Output Power Good                  High        Low       High        High      High       High       High        High
SWE Output Power Good                  High        Low       High        High      High       High       High        High
SWF Output Power Good                  High        Low       High        High      High       High       High        High
1.8 V LDO Power Good                   High        Low       High        High      High       High       High        High
1.0 V LDO Power Good                   High        Low       High        High      High       High       High        High
VBias1 or VBias2 LDO Power Good        High        Low       High        High      High       High       High        High

                                                             Clear Command;                              Clear Command;
                                      Event Occurred;       Event Not Present;    Event Occurred;       Event Not Present;
                                      All Mask Bits = ‘1’   All Mask Bits = ‘1’   All Mask Bits = ‘1’   All Mask Bits = ‘1’
                                       R2F [1:0] = ‘01’       R2F [1:0] = ‘01’     R2F [1:0] = ‘10’       R2F [1:0] = ‘10’
                                      CAMP       GSI_n      CAMP        GSI_n     CAMP       GSI_n      CAMP        GSI_n
                 Event                Output     Output     Output      Output    Output     Output     Output      Output
SWA Output Over Voltage                Low         Low        Low        High      Low        High        Low        High
SWB Output Over Voltage                Low         Low        Low        High      Low        High        Low        High
SWC Output Over Voltage                Low         Low        Low        High      Low        High        Low        High
SWD Output Over Voltage                Low         Low        Low        High      Low        High        Low        High
SWE Output Over Voltage                Low         Low        Low        High      Low        High        Low        High
SWF Output Over Voltage                Low         Low        Low        High      Low        High        Low        High
SWA Output Under Voltage               Low         Low        Low        High      Low        High        Low        High
SWB Output Under Voltage               Low         Low        Low        High      Low        High        Low        High
SWC Output Under Voltage               Low         Low        Low        High      Low        High        Low        High
SWD Output Under Voltage               Low         Low        Low        High      Low        High        Low        High
SWE Output Under Voltage               Low         Low        Low        High      Low        High        Low        High
SWF Output Under Voltage               Low         Low        Low        High      Low        High        Low        High
VBias1 or VBias2 LDO Output or         Low         Low        Low        High      Low        High        Low        High
VIN_Bulk Input Under Voltage
SWA Output Current Limit               High        Low       High        High      High       High       High        High
SWB Output Current Limit               High        Low       High        High      High       High       High        High

SWC Output Current Limit               High        Low       High        High      High       High       High        High
SWD Output Current Limit               High        Low       High        High      High       High       High        High

SWE Output Current Limit               High        Low       High        High      High       High       High        High
SWF Output Current Limit               High        Low       High        High      High       High       High        High

SWA Output High Current/Power          High        Low       High        High      High       High       High        High
SWB Output High Current/Power          High        Low       High        High      High       High       High        High
SWC Output High Current/Power          High        Low       High        High      High       High       High        High
SWD Output High Current/Power          High        Low       High        High      High       High       High        High
SWE Output High Current/Power          High        Low       High        High      High       High       High        High
SWF Output High Current/Power          High        Low       High        High      High       High       High        High
High Temperature Warning               High        Low       High        High      High       High       High        High
Critical Temperature                   Low         Low       P/C[1]     P/C[1]     Low         Low       P/C[1]     P/C[1]
VIN_Mgmt to VIN_Bulk Switchover        High        Low       High        High      High       High       High        High
Valid VIN_Mgmt in Switchover           High        Low       High        High      High       High       High        High
PEC Error                              High        Low       High        High      High       High       High        High
Parity Error                           High        Low       High        High      High       High       High        High
 NOTE 1        P/C = Power Cycle
```

Note that when host masks any of the event in appropriate register, it only masks the assertion of GSI_n output signal or assertion of CAMP output signal for events that do not trigger VR Disable command by the PMIC on its own. The PMIC functional behavior remains the same as noted for each event other than assertion of GSI_n output signal and assertion of CAMP output signal. For any events that cause the PMIC to trigger VR Disable command on its own, the mask register does not apply to CAMP signal and it is always asserted; the mask register does apply to GSI_n signal.
