---
document: JESD301-2 (PMIC5100 Power Management IC Standard, Rev. 1.03, October 2022)
device: PMIC5100
application: client
section: 6.10
title: Function Interrupt - PWR_GOOD and GSI_n Output Signals
pages: 53-60
---
# 6.10 Function Interrupt - PWR_GOOD and GSI_n Output Signals

This clause defines the output functionality of GSI_n pin and PWR_GOOD (Table 138, “Register 0x32” [5] = ‘0’) pin. When mask register bits are not set, the PMIC asserts its GSI_n output and assert PWR_GOOD output signals as shown in Table 28 when any event occurs. The table also highlights 9 events that causes PMIC to generate internally VR Disable command. For remaining events that do not trigger internal VR Disable command, the PMIC continues to operate as normal.

**Table 28 — Events Interrupt Summary**

```text
                                Status    Clear       Mask                            Trigger VR PWR_GOOD   GSI_n
           Event                                                Threshold Bits
                                 Bit       Bit         Bit                             Disable?    Output   Output
    VIN_Bulk Over Voltage       R08 [0]   R10 [0]    R15 [0]         R1B [7]             Yes      Low        Low
   SWA Output Power Good        R08 [5]   R10 [5]    R15 [5]   R21 [1:0]; R22 [7:6]      No       Low        Low
   SWB Output Power Good        R08 [3]   R10 [3]    R15 [3]   R25 [1:0]; R26 [7:6]      No       Low        Low
   SWC Output Power Good        R08 [2]   R10 [2]    R15 [2]   R27 [1:0]; R28 [7:6]      No       Low        Low
    1.8 V LDO Power Good        R09 [5]   R11 [5]    R16 [5]         R1A [2]             No       Low        Low

    1.0 V LDO Power Good        R33 [2]   R14 [2]    R19 [2]         R1A [0]             No       Low        Low
   SWA Output Over Voltage      R0A [7]   R12 [7]    R17 [7]        R22 [5:4]            Yes      Low        Low
   SWB Output Over Voltage      R0A [5]   R12 [5]    R17 [5]        R26 [5:4]            Yes      Low        Low

   SWC Output Over Voltage      R0A [4]   R12 [4]    R17 [4]        R28 [5:4]            Yes      Low        Low
  SWA Output Under Voltage      R0B [3]   R13 [3]    R18 [3]        R22 [3:2]            Yes      Low        Low

  SWB Output Under Voltage      R0B [1]   R13 [1]    R18 [1]        R26 [3:2]            Yes      Low        Low
  SWC Output Under Voltage      R0B [0]   R13 [0]    R18 [0]        R28 [3:2]            Yes      Low        Low
 VIN_Bulk Input Under Voltage    N/A       N/A        N/A       Vendor Specific          Yes      Low        Low
  SWA Output Current Limit      R0B [7]   R13 [7]    R18 [7]        R20 [7:6]            No       High       Low
  SWB Output Current Limit      R0B [5]   R13 [5]    R18 [5]        R20 [3:2]            No       High       Low
  SWC Output Current Limit      R0B [4]   R13 [4]    R18 [4]        R20 [1:0]            No       High       Low
SWA Output High Current/Power   R09 [3]   R11 [3]    R16 [3]        R1C [7:2]            No       High       Low
SWB Output High Current/Power   R09 [1]   R11 [1]    R16 [1]        R1E [7:2]            No       High       Low
SWC Output High Current/Power   R09 [0]   R11 [0]    R16 [0]        R1F [7:2]            No       High       Low
  High Temperature Warning      R09 [7]   R11 [7]    R16 [7]        R1B [2:0]            No       High       Low
      Critical Temperature      R08[6]     N/A        N/A           R2E [2:0]            Yes      Low        Low
           PEC Error            R0A [3]   R12 [3]    R17 [3]          N/A                No       High       Low
           Parity Error         R0A [2]   R12 [2]    R17 [2]          N/A                No       High       Low
```

The host is expected to read appropriate status registers to determine and isolate the cause of the GSI_n signal assertion or PWR_GOOD signal assertion. The host may attempt to clear or mask the appropriate corresponding interrupt event. The PMIC keeps the GSI_n signal asserted or PWR_GOOD signal asserted until the appropriate corresponding registers are explicitly cleared or masked by the host. Table 29 and Table 30 shows the PMIC’s response of GSI_n signal and PWR_GOOD output signal for each event before and after host issues the Clear command. Table 29 and Table 30 assume that all mask bits are either ‘0’ or ‘1’ for simplicity.

**Table 29 — PMIC Response for Clear Command by Host - 1**

```text
                                                      Clear Command;                               Clear Command;
                                Event Occurred; All                          Event Occurred; All
                                                      Event Not Present;                           Event Not Present;
                                  Mask Bits = ‘0’                              Mask Bits = ‘1’
                                                      All Mask Bits = ‘0’                          All Mask Bits = ‘1’
                                                       R2F [1:0] = ‘00’ or
                                                                               R2F [1:0] = ‘00’     R2F [1:0] = ‘00’
                                                          ‘01’ or ‘10’
                                PWR_GO                PWR_GO                 PWR_GO                PWR_GO
                                           GSI_n                  GSI_n                 GSI_n                 GSI_n
           Event                  OD                    OD                     OD                    OD
                                           Output                 Output                Output                Output
                                 Output                Output                 Output                Output
    VIN_Bulk Over Voltage         Low       Low         Low         High       Low        High       Low        High
   SWA Output Power Good          Low       Low         High        High       Low        High       High       High
   SWB Output Power Good          Low       Low         High        High       Low        High       High       High
   SWC Output Power Good          Low       Low         High        High       Low        High       High       High
    1.8 V LDO Power Good          Low       Low         High        High       Low        High       High       High
    1.0 V LDO Power Good          Low       Low         High        High       Low        High       High       High
   SWA Output Over Voltage        Low       Low         Low         High       Low        High       Low        High
   SWB Output Over Voltage        Low       Low         Low         High       Low        High       Low        High
   SWC Output Over Voltage        Low       Low         Low         High       Low        High       Low        High
  SWA Output Under Voltage        Low       Low         Low         High       Low        High       Low        High
  SWB Output Under Voltage        Low       Low         Low         High       Low        High       Low        High
  SWC Output Under Voltage        Low       Low         Low
                                                               ng   High       Low        High       Low        High
 VIN_Bulk Input Under Voltage     Low       Low         N/A         N/A        N/A        N/A        N/A        N/A
  SWA Output Current Limit        High      Low         High        High       High       High       High       High

  SWB Output Current Limit        High      Low         High        High       High       High       High       High
  SWC Output Current Limit        High      Low         High        High       High       High       High       High
SWA Output High Current/Power     High      Low         High        High       High       High       High       High

SWB Output High Current/Power     High      Low         High        High       High       High       High       High
SWC Output High Current/Power     High      Low         High        High       High       High       High       High

  High Temperature Warning        High      Low         High        High       High       High       High       High
      Critical Temperature        Low       Low         P/C         P/C        Low        Low        P/C        P/C
            PEC Error             High      Low         High        High       High       High       High       High
           Parity Error           High      Low         High        High       High       High       High       High
```

**Table 30 — PMIC Response for Clear Command by Host - 2**

```text
                                                        Clear Command;                              Clear Command;
                                Event Occurred; All                           Event Occurred; All
                                                        Event Not Present;                          Event Not Present;
                                  Mask Bits = ‘1’                               Mask Bits = ‘1’
                                                        All Mask Bits = ‘1’                         All Mask Bits = ‘1’
                                  R2F [1:0] = ‘01’       R2F [1:0] = ‘01’       R2F [1:0] = ‘10’     R2F [1:0] = ‘10’
                                PWR_GO                 PWR_GO                 PWR_GO                PWR_GO
                                           GSI_n                   GSI_n                 GSI_n                 GSI_n
           Event                  OD                     OD                     OD                    OD
                                           Output                  Output                Output                Output
                                 Output                 Output                 Output                Output
    VIN_Bulk Over Voltage         Low        Low         Low         High       Low        High       Low        High
   SWA Output Power Good          High       Low         High        High       High       High       High       High
   SWB Output Power Good          High       Low         High        High       High       High       High       High
   SWC Output Power Good          High       Low         High        High       High       High       High       High
    1.8 V LDO Power Good          High       Low         High        High       High       High       High       High
    1.0 V LDO Power Good          High       Low         High        High       High       High       High       High
   SWA Output Over Voltage        Low        Low         Low         High       Low        High       Low        High
   SWB Output Over Voltage        Low        Low         Low         High       Low        High       Low        High
   SWC Output Over Voltage        Low        Low         Low         High       Low        High       Low        High
  SWA Output Under Voltage        Low        Low         Low         High       Low        High       Low        High
  SWB Output Under Voltage        Low        Low         Low         High       Low        High       Low        High
  SWC Output Under Voltage        Low        Low         Low         High       Low        High       Low        High
 VIN_Bulk Input Under Voltage     Low        Low         N/A         N/A        N/A        N/A        N/A        N/A
  SWA Output Current Limit        High       Low         High        High       High       High       High       High
  SWB Output Current Limit        High       Low         High        High       High       High       High       High
  SWC Output Current Limit        High       Low         High        High       High       High       High       High
SWA Output High Current/Power     High       Low         High        High       High       High       High       High

SWB Output High Current/Power     High       Low         High        High       High       High       High       High
SWC Output High Current/Power     High       Low         High        High       High       High       High       High

  High Temperature Warning        High       Low         High        High       High       High       High       High
      Critical Temperature        Low        Low         P/C         P/C        Low        Low        P/C        P/C

            PEC Error             High       Low         High        High       High       High       High       High
           Parity Error           High       Low         High        High       High       High       High       High
```

Note that when host masks any of the event in appropriate register, it only masks the assertion of GSI_n output signal or assertion of PWR_GOOD output signal. The PMIC functional behavior remains the same as noted for each event other than assertion of GSI_n output signal and assertion of PWR_GOOD output signal. The PMIC assumes that there is no fuse protection on VIN_Bulk input rail on the DDR5 DIMM module to prevent short circuit type event.

## Subsections

- [6.10.1 Input Over Voltage Protection](6_10_1_Input_Over_Voltage_Protection.md)
- [6.10.2 Output Power Good Status](6_10_2_Output_Power_Good_Status.md)
- [6.10.3 Output Over Voltage Protection](6_10_3_Output_Over_Voltage_Protection.md)
- [6.10.4 Output Under Voltage and VIN_Bulk Under Voltage Lockout Protection](6_10_4_Output_Under_Voltage_and_VIN_Bulk_Under_Voltage_Lo.md)
- [6.10.5 Output Current Limiter Warning Event](6_10_5_Output_Current_Limiter_Warning_Event.md)
- [6.10.6 Output High Current Consumption Warning Event](6_10_6_Output_High_Current_Consumption_Warning_Event.md)
- [6.10.7 PMIC High Temperature Warning and Critical Temperature Protection](6_10_7_PMIC_High_Temperature_Warning_and_Critical_Tempera.md)
- [6.10.8 Packet Error Code (PEC) and Parity Error Event](6_10_8_Packet_Error_Code_PEC_and_Parity_Error_Event.md)
