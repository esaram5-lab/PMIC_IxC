---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 4.15
title: Function Interrupt - PWR_GOOD Output Signal
pages: 60-68
---
# 4.15 Function Interrupt - PWR_GOOD Output Signal

This clause defines the output functionality of PWR_GOOD (Table 154, Register 0x32 [5] = ‘0’) pin. When mask register bits are not set, the PMIC asserts its GSI_n output signal and PWR_GOOD output signal as shown in Table 27 when any event occurs. The table also highlights 11 events that cause the PMIC to generate internally VR Disable command. For remaining events that do not trigger internal VR Disable command, the PMIC continues to operate as normal.

**Table 27 — Events Interrupt Summary**

```text
                                 Status    Clear     Mask                           Trigger VR   PWR_GOOD   GSI_n
            Event                  Bit      Bit       Bit      Threshold Bits        Disable?      Output   Output
    VIN_Bulk Power Good          R08 [7]   R10 [7]   R15 [7]       R1A [7:6]           No          Low       Low
    VIN_Bulk Over Voltage        R08 [0]   R10 [0]   R15[0]         R1B [7]            Yes         Low       Low
   SWA Output Power Good         R08 [5]   R10 [5]   R15 [5]   R21 [0]; R22 [7:6]      No          Low       Low
   SWD Output Power Good         R08 [4]   R10 [4]   R15 [4]   R23 [0]; R24 [7:6]      No          Low       Low
   SWB Output Power Good         R08 [3]   R10 [3]   R15 [3]   R25 [0]; R26 [7:6]      No          Low       Low
   SWC Output Power Good         R08 [2]   R10 [2]   R15 [2]   R27 [0]; R28 [7:6]      No          Low       Low
    1.8 V LDO Power Good         R09 [5]   R11 [5]   R16 [5]   ng   R1A [2]            No          Low       Low
    1.0 V LDO Power Good         R33 [2]   R14 [2]   R19 [2]        R1A [0]            No          Low       Low
   SWA Output Over Voltage       R0A [7]   R12 [7]   R17[7]        R22 [5:4]           Yes         Low       Low
  SWD Output Over Voltage        R0A [6]   R12 [6]   R17[6]        R24 [5:4]           Yes         Low       Low

   SWB Output Over Voltage       R0A [5]   R12 [5]   R17[5]        R26 [5:4]           Yes         Low       Low
  SWC Output Over Voltage        R0A [4]   R12 [4]   R17[4]        R28 [5:4]           Yes         Low       Low

  SWA Output Under Voltage       R0B [3]   R13 [3]   R18[3]        R22 [3:2]           Yes         Low       Low

  SWD Output Under Voltage       R0B [2]   R13 [2]   R18[2]        R24 [3:2]           Yes         Low       Low
  SWB Output Under Voltage       R0B [1]   R13 [1]   R18[1]        R26 [3:2]           Yes         Low       Low
  SWC Output Under Voltage       R0B [0]   R13 [0]   R18[0]        R28 [3:2]           Yes         Low       Low
 VIN_Bulk Input Under Voltage    R33[3]    R14[3]    R19[3]     Vendor Specific        Yes         Low       Low
   SWA Output Current Limit      R0B [7]   R13 [7]   R18 [7]       R20 [7:6]           No          High      Low
   SWD Output Current Limit      R0B [6]   R13 [6]   R18 [6]       R20 [5:4]           No          High      Low
   SWB Output Current Limit      R0B [5]   R13 [5]   R18 [5]       R20 [3:2]           No          High      Low
   SWC Output Current Limit      R0B [4]   R13 [4]   R18 [4]       R20 [1:0]           No          High      Low
SWA Output High Current/Power    R09 [3]   R11 [3]   R16 [3]       R1C [7:2]           No          High      Low
SWD Output High Current/Power    R09 [2]   R11 [2]   R16 [2]       R1D [7:2]           No          High      Low
SWB Output High Current/Power    R09 [1]   R11 [1]   R16 [1]       R1E [7:2]           No          High      Low
SWC Output High Current/Power    R09 [0]   R11 [0]   R16 [0]       R1F [7:2]           No          High      Low
  High Temperature Warning       R09 [7]   R11 [7]   R16 [7]       R1B [2:0]           No          High      Low
     Critical Temperature        R08 [6]    N/A       N/A          R2E [2:0]           Yes         Low       Low
          PEC Error              R0A [3]   R12 [3]   R17 [3]          N/A              No          High      Low
          Parity Error           R0A [2]   R12 [2]   R17 [2]          N/A              No          High      Low
        DVFSQ_n Pin              R33[1]     N/A       N/A             N/A              No          High      N/A
          Unlock Pin             R33[0]     N/A       N/A             N/A              No          High      N/A
      SWB_Disable Pin            R109[0]    N/A       N/A             N/A              No          High      N/A
```

The host is expected to read appropriate status registers to determine and isolate the cause of GSI_n signal or PWR_GOOD signal assertion. The host may attempt to clear or mask the appropriate corresponding interrupt event. The PMIC keeps the GSI_n signal or PWR_GOOD signal asserted until the appropriate corresponding registers are explicitly cleared or masked by the host. Table 28 and Table 29 show the PMIC’s response of GSI_n signal and PWR_GOOD output signal for each event before and after host issues the Clear command. Table 28 and Table 29 assume that all mask bits are either ‘0’ or ‘1’ for simplicity.

**Table 28 — PMIC Response for Clear Command by Host - 1**

```text
                                                       Clear Command;                               Clear Command;
                                Event Occurred; All                          Event Occurred; All
                                                      Event Not Present;                           Event Not Present;
                                  Mask Bits = ‘0’                              Mask Bits = ‘1’
                                                      All Mask Bits = ‘0’                          All Mask Bits = ‘1’
                                                      R2F [1:0] = ‘00’ or
                                                                               R2F [1:0] = ‘00’     R2F [1:0] = ‘00’
                                                           ‘01’ or ‘10’
                                 PWR_                  PWR_                   PWR_                 PWR_
                                           GSI_n                    GSI_n                GSI_n                GSI_n
            Event               GOOD                  GOOD                   GOOD                  GOOD
                                           Output                   Output               Output               Output
                                Output                Output                 Output                Output
    VIN_Bulk Power Good          Low         Low        High         High     Low         High      High       High
    VIN_Bulk Over Voltage        Low         Low        Low          High     Low         High      Low        High
   SWA Output Power Good         Low         Low        High         High     Low         High      High       High

   SWD Output Power Good          Low        Low       High        High        Low        High      High       High
   SWB Output Power Good          Low        Low       High        High        Low        High      High       High
   SWC Output Power Good          Low        Low       High        High        Low        High      High       High

    1.8 V LDO Power Good          Low        Low       High        High        Low        High      High       High

    1.0 V LDO Power Good          Low        Low       High        High        Low        High      High       High
   SWA Output Over Voltage        Low        Low       Low         High        Low        High      Low        High
  SWD Output Over Voltage         Low        Low        Low        High        Low        High      Low        High
   SWB Output Over Voltage        Low        Low        Low        High        Low        High      Low        High
  SWC Output Over Voltage         Low        Low        Low        High        Low        High      Low        High
  SWA Output Under Voltage        Low        Low        Low        High        Low        High      Low        High
  SWD Output Under Voltage        Low        Low        Low        High        Low        High      Low        High
  SWB Output Under Voltage        Low        Low        Low        High        Low        High      Low        High
  SWC Output Under Voltage        Low        Low       Low         High        Low        High      Low        High
 VIN_Bulk Input Under Voltage     Low        Low       Low         High        Low        High      Low        High
   SWA Output Current Limit       High       Low       High        High        High       High      High       High
   SWD Output Current Limit       High       Low       High        High        High       High      High       High
   SWB Output Current Limit       High       Low       High        High        High       High      High       High
  SWC Output Current Limit        High       Low       High        High        High       High      High       High
SWA Output High Current/Power     High       Low       High        High        High       High      High       High
SWD Output High Current/Power     High       Low       High        High        High       High      High       High
SWB Output High Current/Power     High       Low       High        High        High       High      High       High
SWC Output High Current/Power     High       Low       High        High        High       High      High       High
  High Temperature Warning        High       Low       High        High        High       High      High       High
     Critical Temperature         Low        Low       P/C[1]      P/C[1]      Low        Low       P/C[1]     P/C[1]
         PEC Error                High       Low       High        High        High       High      High       High
         Parity Error             High       Low       High        High        High       High      High       High
  NOTE 1   P/C = Power Cycle
```

**Table 29 — PMIC Response for Clear Command by Host - 2**

```text
                                                         Clear Command;                              Clear Command;
                                  Event Occurred; All   Event Not Present;    Event Occurred; All   Event Not Present;
                                    Mask Bits = ‘1’     All Mask Bits = ‘1’     Mask Bits = ‘1’     All Mask Bits = ‘1’
                                    R2F [1:0] = ‘01’     R2F [1:0] = ‘01’       R2F [1:0] = ‘10’     R2F [1:0] = ‘10’
                                   PWR_                 PWR_                   PWR_                 PWR_
                                  GOOD        GSI_n     GOOD       GSI_n      GOOD        GSI_n     GOOD       GSI_n
            Event                 Output      Output    Output     Output     Output      Output    Output     Output
    VIN_Bulk Power Good             High       Low       High       High        High       High      High       High
    VIN_Bulk Over Voltage           Low        Low       Low        High        Low        High      Low        High
   SWA Output Power Good            High       Low       High       High        High       High      High       High
   SWD Output Power Good            High       Low       High       High        High       High      High       High
   SWB Output Power Good            High       Low       High       High        High       High      High       High
   SWC Output Power Good            High       Low       High       High        High       High      High       High
    1.8 V LDO Power Good            High       Low       High       High        High       High      High       High
    1.0 V LDO Power Good            High       Low       High       High        High       High      High       High
   SWA Output Over Voltage          Low        Low       Low        High        Low        High      Low        High
  SWD Output Over Voltage           Low        Low       Low        High        Low        High      Low        High

   SWB Output Over Voltage          Low        Low       Low        High        Low        High      Low        High
  SWC Output Over Voltage           Low        Low       Low        High        Low        High      Low        High

  SWA Output Under Voltage          Low        Low       Low        High        Low        High      Low        High
  SWD Output Under Voltage          Low        Low       Low        High        Low        High      Low        High

  SWB Output Under Voltage          Low        Low       Low        High        Low        High      Low        High
  SWC Output Under Voltage          Low        Low       Low        High        Low        High      Low        High
 VIN_Bulk Input Under Voltage       Low        Low       Low        High        Low        High      Low        High
   SWA Output Current Limit         High       Low       High       High        High       High      High       High
   SWD Output Current Limit         High       Low       High       High        High       High      High       High
   SWB Output Current Limit         High       Low       High       High        High       High      High       High
   SWC Output Current Limit         High       Low       High       High        High       High      High       High
SWA Output High Current/Power       High       Low       High       High        High       High      High       High
SWD Output High Current/Power       High       Low       High       High        High       High      HIgh       High
SWB Output High Current/Power       High       Low       High       High        High       High      High       High
SWC Output High Current/Power       High       Low       High       High        High       High      High       High
  High Temperature Warning          High       Low       High       High        High       High      High       High
     Critical Temperature           Low        Low       P/C[1]     P/C[1]      Low        Low       P/C[1]     P/C[1]
          PEC Error                 High       Low       High       High        High       High      High       High
         Parity Error               High       Low       High       High        High       High      High       High
  NOTE 1 P/C = Power Cycle.
```

Note that when host masks any of the event in appropriate register, it only masks the assertion of GSI_n output signal or PWR_GOOD output signal. The PMIC functional behavior remains the same as noted for each event other than assertion of GSI_n output signal and the assertion of PWR_GOOD output signal.

## Subsections

- [4.15.1 Input Power Good Status](4_15_1_Input_Power_Good_Status.md)
- [4.15.2 Input Over Voltage Protection](4_15_2_Input_Over_Voltage_Protection.md)
- [4.15.3 Output Power Good Status](4_15_3_Output_Power_Good_Status.md)
- [4.15.4 Output Over Voltage Protection](4_15_4_Output_Over_Voltage_Protection.md)
- [4.15.5 Output Under Voltage and VIN_Bulk Under Voltage Lockout Protection](4_15_5_Output_Under_Voltage_and_VIN_Bulk_Under_Voltage_Lo.md)
- [4.15.6 Output Current Limiter Warning Event](4_15_6_Output_Current_Limiter_Warning_Event.md)
- [4.15.7 Output High Current Consumption Warning Event](4_15_7_Output_High_Current_Consumption_Warning_Event.md)
- [4.15.8 PMIC High Temperature Warning and Critical Temperature Protection](4_15_8_PMIC_High_Temperature_Warning_and_Critical_Tempera.md)
- [4.15.9 Packet Error Code (PEC) and Parity Error Event](4_15_9_Packet_Error_Code_PEC_and_Parity_Error_Event.md)
