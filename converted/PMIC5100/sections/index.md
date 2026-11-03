# PMIC5100 — Sections

Source: JESD301-2 Rev. 1.03 (October 2022). One file per section; register tables are linked to `../registers/` instead of being repeated.

| Section | Pages | File |
|---|---|---|
| 1 Scope | 1–3 | [1_Scope.md](1_Scope.md) |
| 2 PMIC Pin List and Package | 3–9 | [2_PMIC_Pin_List_and_Package.md](2_PMIC_Pin_List_and_Package.md) |
| 3 Electrical Characteristics | 9–20 | [3_Electrical_Characteristics.md](3_Electrical_Characteristics.md) |
| &nbsp;&nbsp;3.1 Input Supply Electrical Characteristics | 9–10 | [3_1_Input_Supply_Electrical_Characteristics.md](3_1_Input_Supply_Electrical_Characteristics.md) |
| &nbsp;&nbsp;3.2 Switch Regulator Output Electrical Characteristics | 10–11 | [3_2_Switch_Regulator_Output_Electrical_Characteristics.md](3_2_Switch_Regulator_Output_Electrical_Characteristics.md) |
| &nbsp;&nbsp;3.3 LDO Output Regulator Characteristics | 11–12 | [3_3_LDO_Output_Regulator_Characteristics.md](3_3_LDO_Output_Regulator_Characteristics.md) |
| &nbsp;&nbsp;3.4 I2C or I3C Basic DC and AC Electrical Characteristics | 12–16 | [3_4_I2C_or_I3C_Basic_DC_and_AC_Electrical_Characterist.md](3_4_I2C_or_I3C_Basic_DC_and_AC_Electrical_Characterist.md) |
| &nbsp;&nbsp;3.5 Measurement Condition | 16–17 | [3_5_Measurement_Condition.md](3_5_Measurement_Condition.md) |
| &nbsp;&nbsp;3.6 PMIC AC Timing Parameters | 17–18 | [3_6_PMIC_AC_Timing_Parameters.md](3_6_PMIC_AC_Timing_Parameters.md) |
| &nbsp;&nbsp;3.7 Absolute Maximum Ratings | 18–18 | [3_7_Absolute_Maximum_Ratings.md](3_7_Absolute_Maximum_Ratings.md) |
| &nbsp;&nbsp;3.8 ESD Requirements | 18–19 | [3_8_ESD_Requirements.md](3_8_ESD_Requirements.md) |
| &nbsp;&nbsp;3.9 Thermal Characteristics | 19–20 | [3_9_Thermal_Characteristics.md](3_9_Thermal_Characteristics.md) |
| 4 Performance Characteristics | 20–23 | [4_Performance_Characteristics.md](4_Performance_Characteristics.md) |
| 5 DDR5 DIMM Schematic | 23–28 | [5_DDR5_DIMM_Schematic.md](5_DDR5_DIMM_Schematic.md) |
| 6 Functional Operation | 28–105 | [6_Functional_Operation.md](6_Functional_Operation.md) |
| &nbsp;&nbsp;6.1 PMIC Input Voltage Supply and Ramp Condition | 28–28 | [6_1_PMIC_Input_Voltage_Supply_and_Ramp_Condition.md](6_1_PMIC_Input_Voltage_Supply_and_Ramp_Condition.md) |
| &nbsp;&nbsp;6.2 Power Up Initialization Sequence | 28–34 | [6_2_Power_Up_Initialization_Sequence.md](6_2_Power_Up_Initialization_Sequence.md) |
| &nbsp;&nbsp;6.3 PMIC Output Rail Turn On Timing | 34–35 | [6_3_PMIC_Output_Rail_Turn_On_Timing.md](6_3_PMIC_Output_Rail_Turn_On_Timing.md) |
| &nbsp;&nbsp;6.4 Secure Mode and Programmable Mode of Operation | 35–36 | [6_4_Secure_Mode_and_Programmable_Mode_of_Operation.md](6_4_Secure_Mode_and_Programmable_Mode_of_Operation.md) |
| &nbsp;&nbsp;6.5 Power Down Output Regulators | 36–46 | [6_5_Power_Down_Output_Regulators.md](6_5_Power_Down_Output_Regulators.md) |
| &nbsp;&nbsp;6.6 PMIC Output Rail Off Timing | 46–47 | [6_6_PMIC_Output_Rail_Off_Timing.md](6_6_PMIC_Output_Rail_Off_Timing.md) |
| &nbsp;&nbsp;6.7 Power Good (PWR_GOOD) Signal | 47–50 | [6_7_Power_Good_PWR_GOOD_Signal.md](6_7_Power_Good_PWR_GOOD_Signal.md) |
| &nbsp;&nbsp;6.8 Idle State and Quiescent Power State | 50–53 | [6_8_Idle_State_and_Quiescent_Power_State.md](6_8_Idle_State_and_Quiescent_Power_State.md) |
| &nbsp;&nbsp;6.9 GSI_n Signal | 53–53 | [6_9_GSI_n_Signal.md](6_9_GSI_n_Signal.md) |
| &nbsp;&nbsp;6.10 Function Interrupt - PWR_GOOD and GSI_n Output Signals | 53–60 | [6_10_Function_Interrupt_PWR_GOOD_and_GSI_n_Output_Signa.md](6_10_Function_Interrupt_PWR_GOOD_and_GSI_n_Output_Signa.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;6.10.1 Input Over Voltage Protection | 55–56 | [6_10_1_Input_Over_Voltage_Protection.md](6_10_1_Input_Over_Voltage_Protection.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;6.10.2 Output Power Good Status | 56–57 | [6_10_2_Output_Power_Good_Status.md](6_10_2_Output_Power_Good_Status.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;6.10.3 Output Over Voltage Protection | 57–57 | [6_10_3_Output_Over_Voltage_Protection.md](6_10_3_Output_Over_Voltage_Protection.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;6.10.4 Output Under Voltage and VIN_Bulk Under Voltage Lockout Protection | 57–58 | [6_10_4_Output_Under_Voltage_and_VIN_Bulk_Under_Voltage_Lo.md](6_10_4_Output_Under_Voltage_and_VIN_Bulk_Under_Voltage_Lo.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;6.10.5 Output Current Limiter Warning Event | 58–59 | [6_10_5_Output_Current_Limiter_Warning_Event.md](6_10_5_Output_Current_Limiter_Warning_Event.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;6.10.6 Output High Current Consumption Warning Event | 59–59 | [6_10_6_Output_High_Current_Consumption_Warning_Event.md](6_10_6_Output_High_Current_Consumption_Warning_Event.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;6.10.7 PMIC High Temperature Warning and Critical Temperature Protection | 59–60 | [6_10_7_PMIC_High_Temperature_Warning_and_Critical_Tempera.md](6_10_7_PMIC_High_Temperature_Warning_and_Critical_Tempera.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;6.10.8 Packet Error Code (PEC) and Parity Error Event | 60–60 | [6_10_8_Packet_Error_Code_PEC_and_Parity_Error_Event.md](6_10_8_Packet_Error_Code_PEC_and_Parity_Error_Event.md) |
| &nbsp;&nbsp;6.11 Analog to Digital Converter (ADC) | 60–61 | [6_11_Analog_to_Digital_Converter_ADC.md](6_11_Analog_to_Digital_Converter_ADC.md) |
| &nbsp;&nbsp;6.12 PMIC Address ID (PID) | 61–61 | [6_12_PMIC_Address_ID_PID.md](6_12_PMIC_Address_ID_PID.md) |
| &nbsp;&nbsp;6.13 Error Injection | 61–61 | [6_13_Error_Injection.md](6_13_Error_Injection.md) |
| &nbsp;&nbsp;6.14 I2C and I3C Basic Operation | 61–62 | [6_14_I2C_and_I3C_Basic_Operation.md](6_14_I2C_and_I3C_Basic_Operation.md) |
| &nbsp;&nbsp;6.15 Device Interface - Protocol | 62–63 | [6_15_Device_Interface_Protocol.md](6_15_Device_Interface_Protocol.md) |
| &nbsp;&nbsp;6.16 I2C Target Protocol | 63–65 | [6_16_I2C_Target_Protocol.md](6_16_I2C_Target_Protocol.md) |
| &nbsp;&nbsp;6.17 I3C Basic Target Protocol | 65–105 | [6_17_I3C_Basic_Target_Protocol.md](6_17_I3C_Basic_Target_Protocol.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;6.17.1 Write Operation Data Packet | 65–67 | [6_17_1_Write_Operation_Data_Packet.md](6_17_1_Write_Operation_Data_Packet.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;6.17.2 Read Operation Data Packet | 67–71 | [6_17_2_Read_Operation_Data_Packet.md](6_17_2_Read_Operation_Data_Packet.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;6.17.3 Default Read Address Pointer Mode | 71–77 | [6_17_3_Default_Read_Address_Pointer_Mode.md](6_17_3_Default_Read_Address_Pointer_Mode.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;6.17.4 In Band Interrupt (IBI) | 77–81 | [6_17_4_In_Band_Interrupt_IBI.md](6_17_4_In_Band_Interrupt_IBI.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;6.17.5 Packet Error Check Function | 81–82 | [6_17_5_Packet_Error_Check_Function.md](6_17_5_Packet_Error_Check_Function.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;6.17.6 Parity Error Check Function | 82–82 | [6_17_6_Parity_Error_Check_Function.md](6_17_6_Parity_Error_Check_Function.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;6.17.7 Packet Error Check and Parity Error Handling | 82–87 | [6_17_7_Packet_Error_Check_and_Parity_Error_Handling.md](6_17_7_Packet_Error_Check_and_Parity_Error_Handling.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;6.17.8 CCC Packet Error Handling | 87–87 | [6_17_8_CCC_Packet_Error_Handling.md](6_17_8_CCC_Packet_Error_Handling.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;6.17.9 Error Reporting | 87–87 | [6_17_9_Error_Reporting.md](6_17_9_Error_Reporting.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;6.17.10 I3C Basic Common Command Codes (CCC) | 87–102 | [6_17_10_I3C_Basic_Common_Command_Codes_CCC.md](6_17_10_I3C_Basic_Common_Command_Codes_CCC.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.17.10.1 ENEC CCC | 88–90 | [6_17_10_1_ENEC_CCC.md](6_17_10_1_ENEC_CCC.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.17.10.2 DISEC CCC | 90–92 | [6_17_10_2_DISEC_CCC.md](6_17_10_2_DISEC_CCC.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.17.10.3 RSTDAA CCC | 92–92 | [6_17_10_3_RSTDAA_CCC.md](6_17_10_3_RSTDAA_CCC.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.17.10.4 SETAASA CCC | 92–93 | [6_17_10_4_SETAASA_CCC.md](6_17_10_4_SETAASA_CCC.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.17.10.5 GETSTATUS CCC | 93–94 | [6_17_10_5_GETSTATUS_CCC.md](6_17_10_5_GETSTATUS_CCC.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.17.10.6 DEVCAP CCC | 94–95 | [6_17_10_6_DEVCAP_CCC.md](6_17_10_6_DEVCAP_CCC.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.17.10.7 SETHID CCC | 95–96 | [6_17_10_7_SETHID_CCC.md](6_17_10_7_SETHID_CCC.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.17.10.8 DEVCTRL CCC | 96–102 | [6_17_10_8_DEVCTRL_CCC.md](6_17_10_8_DEVCTRL_CCC.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.17.10.8.1 DEVCTRL CCC Examples - RegMod = ‘0’ | 99–101 | [6_17_10_8_1_DEVCTRL_CCC_Examples_RegMod_0.md](6_17_10_8_1_DEVCTRL_CCC_Examples_RegMod_0.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.17.10.8.2 DEVCTRL CCC Examples - RegMod = ‘1’ | 101–102 | [6_17_10_8_2_DEVCTRL_CCC_Examples_RegMod_1.md](6_17_10_8_2_DEVCTRL_CCC_Examples_RegMod_1.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;6.17.11 IO Operation | 102–103 | [6_17_11_IO_Operation.md](6_17_11_IO_Operation.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;6.17.12 Bus Clear | 103–103 | [6_17_12_Bus_Clear.md](6_17_12_Bus_Clear.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;6.17.13 Bus Reset | 103–104 | [6_17_13_Bus_Reset.md](6_17_13_Bus_Reset.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;6.17.14 Command Truth Table | 104–105 | [6_17_14_Command_Truth_Table.md](6_17_14_Command_Truth_Table.md) |
| 7 Volatile Registers Space | 105–168 | [7_Volatile_Registers_Space.md](7_Volatile_Registers_Space.md) |
| &nbsp;&nbsp;7.1 Access Mechanism | 105–106 | [7_1_Access_Mechanism.md](7_1_Access_Mechanism.md) |
| &nbsp;&nbsp;7.2 Registers | 106–168 | [7_2_Registers.md](7_2_Registers.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;7.2.1 Register Map Breakdown | 106–106 | [7_2_1_Register_Map_Breakdown.md](7_2_1_Register_Map_Breakdown.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;7.2.2 Memory Protection | 106–106 | [7_2_2_Memory_Protection.md](7_2_2_Memory_Protection.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;7.2.3 Steps to Access DIMM Vendor Registers | 106–106 | [7_2_3_Steps_to_Access_DIMM_Vendor_Registers.md](7_2_3_Steps_to_Access_DIMM_Vendor_Registers.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;7.2.4 Steps to Change DIMM Vendor Region Password | 106–107 | [7_2_4_Steps_to_Change_DIMM_Vendor_Region_Password.md](7_2_4_Steps_to_Change_DIMM_Vendor_Region_Password.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;7.2.5 Steps to Burn or Program DIMM Vendor Region Registers | 107–107 | [7_2_5_Steps_to_Burn_or_Program_DIMM_Vendor_Region_Regist.md](7_2_5_Steps_to_Burn_or_Program_DIMM_Vendor_Region_Regist.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;7.2.6 Host Region Register Map | 107–112 | [7_2_6_Host_Region_Register_Map.md](7_2_6_Host_Region_Register_Map.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;7.2.7 Register Definition | 112–168 | [7_2_7_Register_Definition.md](7_2_7_Register_Definition.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7.2.7.1 Status Registers | 112–122 | [7_2_7_1_Status_Registers.md](7_2_7_1_Status_Registers.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7.2.7.2 Clear Registers | 122–127 | [7_2_7_2_Clear_Registers.md](7_2_7_2_Clear_Registers.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7.2.7.3 Mask Registers | 127–131 | [7_2_7_3_Mask_Registers.md](7_2_7_3_Mask_Registers.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7.2.7.4 Threshold Registers | 131–152 | [7_2_7_4_Threshold_Registers.md](7_2_7_4_Threshold_Registers.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7.2.7.5 Error Injection Registers | 152–153 | [7_2_7_5_Error_Injection_Registers.md](7_2_7_5_Error_Injection_Registers.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7.2.7.6 Password Input and Command Code | 153–168 | [7_2_7_6_Password_Input_and_Command_Code.md](7_2_7_6_Password_Input_and_Command_Code.md) |
