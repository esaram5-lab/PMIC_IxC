# PMIC5120 — Sections

Source: JESD301-6 Version 1.0 (February 2025). One file per section; register tables are linked to `../registers/` instead of being repeated.

| Section | Pages | File |
|---|---|---|
| 1 PMIC5120 Power Management IC Standard | 1–3 | [1_PMIC5120_Power_Management_IC_Standard.md](1_PMIC5120_Power_Management_IC_Standard.md) |
| 2 PMIC Pin List and Package | 3–10 | [2_PMIC_Pin_List_and_Package.md](2_PMIC_Pin_List_and_Package.md) |
| &nbsp;&nbsp;2.1 Pin List | 3–4 | [2_1_Pin_List.md](2_1_Pin_List.md) |
| &nbsp;&nbsp;2.2 Package | 4–10 | [2_2_Package.md](2_2_Package.md) |
| 3 Electrical Characteristics | 10–22 | [3_Electrical_Characteristics.md](3_Electrical_Characteristics.md) |
| &nbsp;&nbsp;3.1 Input Supply Electrical Characteristics | 10–11 | [3_1_Input_Supply_Electrical_Characteristics.md](3_1_Input_Supply_Electrical_Characteristics.md) |
| &nbsp;&nbsp;3.2 Switch Regulator Output Electrical Characteristics | 11–12 | [3_2_Switch_Regulator_Output_Electrical_Characteristics.md](3_2_Switch_Regulator_Output_Electrical_Characteristics.md) |
| &nbsp;&nbsp;3.3 LDO Output Regulator Characteristics | 12–13 | [3_3_LDO_Output_Regulator_Characteristics.md](3_3_LDO_Output_Regulator_Characteristics.md) |
| &nbsp;&nbsp;3.4 I2C or I3C Basic DC and AC Electrical Characteristics | 13–18 | [3_4_I2C_or_I3C_Basic_DC_and_AC_Electrical_Characterist.md](3_4_I2C_or_I3C_Basic_DC_and_AC_Electrical_Characterist.md) |
| &nbsp;&nbsp;3.5 Measurement Condition | 18–18 | [3_5_Measurement_Condition.md](3_5_Measurement_Condition.md) |
| &nbsp;&nbsp;3.6 MIC AC Timing Parameters | 18–19 | [3_6_MIC_AC_Timing_Parameters.md](3_6_MIC_AC_Timing_Parameters.md) |
| &nbsp;&nbsp;3.7 Absolute Maximum Ratings | 19–20 | [3_7_Absolute_Maximum_Ratings.md](3_7_Absolute_Maximum_Ratings.md) |
| &nbsp;&nbsp;3.8 ESD Requirements | 20–21 | [3_8_ESD_Requirements.md](3_8_ESD_Requirements.md) |
| &nbsp;&nbsp;3.9 Thermal Characteristics | 21–22 | [3_9_Thermal_Characteristics.md](3_9_Thermal_Characteristics.md) |
| 4 Performance Characteristics | 22–26 | [4_Performance_Characteristics.md](4_Performance_Characteristics.md) |
| 5 DDR5 DIMM Schematic | 26–31 | [5_DDR5_DIMM_Schematic.md](5_DDR5_DIMM_Schematic.md) |
| 6 Functional Operation | 31–111 | [6_Functional_Operation.md](6_Functional_Operation.md) |
| &nbsp;&nbsp;6.1 PMIC Input Voltage Supply and Ramp Condition | 31–31 | [6_1_PMIC_Input_Voltage_Supply_and_Ramp_Condition.md](6_1_PMIC_Input_Voltage_Supply_and_Ramp_Condition.md) |
| &nbsp;&nbsp;6.2 Power Up Initialization Sequence | 31–36 | [6_2_Power_Up_Initialization_Sequence.md](6_2_Power_Up_Initialization_Sequence.md) |
| &nbsp;&nbsp;6.3 PMIC Output Rail Turn On Timing | 36–37 | [6_3_PMIC_Output_Rail_Turn_On_Timing.md](6_3_PMIC_Output_Rail_Turn_On_Timing.md) |
| &nbsp;&nbsp;6.4 Secure Mode and Programmable Mode of Operation | 37–38 | [6_4_Secure_Mode_and_Programmable_Mode_of_Operation.md](6_4_Secure_Mode_and_Programmable_Mode_of_Operation.md) |
| &nbsp;&nbsp;6.5 Power Down Output Regulators | 38–49 | [6_5_Power_Down_Output_Regulators.md](6_5_Power_Down_Output_Regulators.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;6.5.1 Normal Power Down Sequence | 38–39 | [6_5_1_Normal_Power_Down_Sequence.md](6_5_1_Normal_Power_Down_Sequence.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;6.5.2 Programmable Mode Operation; R1A[4] = ‘0’ | 39–42 | [6_5_2_Programmable_Mode_Operation_R1A_4_0.md](6_5_2_Programmable_Mode_Operation_R1A_4_0.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;6.5.3 Programmable Mode Operation; R1A[4] = ‘1’ | 42–45 | [6_5_3_Programmable_Mode_Operation_R1A_4_1.md](6_5_3_Programmable_Mode_Operation_R1A_4_1.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;6.5.4 Secure Mode Operation; R1A[4] = ‘0’ | 45–46 | [6_5_4_Secure_Mode_Operation_R1A_4_0.md](6_5_4_Secure_Mode_Operation_R1A_4_0.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;6.5.5 Secure Mode Operation; R1A[4] = ‘1’ | 46–49 | [6_5_5_Secure_Mode_Operation_R1A_4_1.md](6_5_5_Secure_Mode_Operation_R1A_4_1.md) |
| &nbsp;&nbsp;6.6 PMIC Output Rail Off Timing | 49–50 | [6_6_PMIC_Output_Rail_Off_Timing.md](6_6_PMIC_Output_Rail_Off_Timing.md) |
| &nbsp;&nbsp;6.7 Power Good (PWR_GOOD) Signal | 50–53 | [6_7_Power_Good_PWR_GOOD_Signal.md](6_7_Power_Good_PWR_GOOD_Signal.md) |
| &nbsp;&nbsp;6.8 Idle Condition and Quiescent Power State | 53–56 | [6_8_Idle_Condition_and_Quiescent_Power_State.md](6_8_Idle_Condition_and_Quiescent_Power_State.md) |
| &nbsp;&nbsp;6.9 GSI_n Signal | 56–56 | [6_9_GSI_n_Signal.md](6_9_GSI_n_Signal.md) |
| &nbsp;&nbsp;6.10 Function Interrupt - PWR_GOOD and GSI_n Output Signals | 56–63 | [6_10_Function_Interrupt_PWR_GOOD_and_GSI_n_Output_Signa.md](6_10_Function_Interrupt_PWR_GOOD_and_GSI_n_Output_Signa.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;6.10.1 Input Over Voltage Protection | 59–60 | [6_10_1_Input_Over_Voltage_Protection.md](6_10_1_Input_Over_Voltage_Protection.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;6.10.2 Output Power Good Status | 60–60 | [6_10_2_Output_Power_Good_Status.md](6_10_2_Output_Power_Good_Status.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;6.10.3 Output Over Voltage Protection | 60–61 | [6_10_3_Output_Over_Voltage_Protection.md](6_10_3_Output_Over_Voltage_Protection.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;6.10.4 Output Under Voltage and VIN_Bulk Under Voltage Lockout Protection | 61–62 | [6_10_4_Output_Under_Voltage_and_VIN_Bulk_Under_Voltage_Lo.md](6_10_4_Output_Under_Voltage_and_VIN_Bulk_Under_Voltage_Lo.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;6.10.5 Output Current Limiter Warning Event | 62–62 | [6_10_5_Output_Current_Limiter_Warning_Event.md](6_10_5_Output_Current_Limiter_Warning_Event.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;6.10.6 Output High Current Consumption Warning Event | 62–62 | [6_10_6_Output_High_Current_Consumption_Warning_Event.md](6_10_6_Output_High_Current_Consumption_Warning_Event.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;6.10.7 PMIC High Temperature Warning and Critical Temperature Protection | 62–63 | [6_10_7_PMIC_High_Temperature_Warning_and_Critical_Tempera.md](6_10_7_PMIC_High_Temperature_Warning_and_Critical_Tempera.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;6.10.8 Packet Error Code (PEC) and Parity Error Event | 63–63 | [6_10_8_Packet_Error_Code_PEC_and_Parity_Error_Event.md](6_10_8_Packet_Error_Code_PEC_and_Parity_Error_Event.md) |
| &nbsp;&nbsp;6.11 Analog to Digital Converter (ADC) | 63–64 | [6_11_Analog_to_Digital_Converter_ADC.md](6_11_Analog_to_Digital_Converter_ADC.md) |
| &nbsp;&nbsp;6.12 PMIC Address ID (PID) | 64–65 | [6_12_PMIC_Address_ID_PID.md](6_12_PMIC_Address_ID_PID.md) |
| &nbsp;&nbsp;6.13 Error Injection | 65–65 | [6_13_Error_Injection.md](6_13_Error_Injection.md) |
| &nbsp;&nbsp;6.14 Acoustic Noise | 65–66 | [6_14_Acoustic_Noise.md](6_14_Acoustic_Noise.md) |
| &nbsp;&nbsp;6.15 I2C and I3C Basic Operation | 66–66 | [6_15_I2C_and_I3C_Basic_Operation.md](6_15_I2C_and_I3C_Basic_Operation.md) |
| &nbsp;&nbsp;6.16 Device Interface - Protocol | 66–67 | [6_16_Device_Interface_Protocol.md](6_16_Device_Interface_Protocol.md) |
| &nbsp;&nbsp;6.17 I2C Target Protocol | 67–69 | [6_17_I2C_Target_Protocol.md](6_17_I2C_Target_Protocol.md) |
| &nbsp;&nbsp;6.18 I3C Basic Target Protocol | 69–109 | [6_18_I3C_Basic_Target_Protocol.md](6_18_I3C_Basic_Target_Protocol.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;6.18.1 Write Operation Data Packet | 69–71 | [6_18_1_Write_Operation_Data_Packet.md](6_18_1_Write_Operation_Data_Packet.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;6.18.2 Read Operation Data Packet | 71–76 | [6_18_2_Read_Operation_Data_Packet.md](6_18_2_Read_Operation_Data_Packet.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;6.18.3 Default Read Address Pointer Mode | 76–82 | [6_18_3_Default_Read_Address_Pointer_Mode.md](6_18_3_Default_Read_Address_Pointer_Mode.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;6.18.4 In Band Interrupt (IBI) | 82–86 | [6_18_4_In_Band_Interrupt_IBI.md](6_18_4_In_Band_Interrupt_IBI.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;6.18.5 Packet Error Check (PEC) Function | 86–86 | [6_18_5_Packet_Error_Check_PEC_Function.md](6_18_5_Packet_Error_Check_PEC_Function.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;6.18.6 Parity Error Check Function | 86–87 | [6_18_6_Parity_Error_Check_Function.md](6_18_6_Parity_Error_Check_Function.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;6.18.7 Packet Error Check and Parity Error Handling | 87–91 | [6_18_7_Packet_Error_Check_and_Parity_Error_Handling.md](6_18_7_Packet_Error_Check_and_Parity_Error_Handling.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;6.18.8 CCC Packet Error Handling | 91–91 | [6_18_8_CCC_Packet_Error_Handling.md](6_18_8_CCC_Packet_Error_Handling.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;6.18.9 Error Reporting | 91–92 | [6_18_9_Error_Reporting.md](6_18_9_Error_Reporting.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;6.18.10 I3C Basic Common Command Codes (CCC) | 92–107 | [6_18_10_I3C_Basic_Common_Command_Codes_CCC.md](6_18_10_I3C_Basic_Common_Command_Codes_CCC.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.18.10.1 ENEC CCC | 92–94 | [6_18_10_1_ENEC_CCC.md](6_18_10_1_ENEC_CCC.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.18.10.2 DISEC CCC | 94–96 | [6_18_10_2_DISEC_CCC.md](6_18_10_2_DISEC_CCC.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.18.10.3 RSTDAA CCC | 96–97 | [6_18_10_3_RSTDAA_CCC.md](6_18_10_3_RSTDAA_CCC.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.18.10.4 SETAASA CCC | 97–97 | [6_18_10_4_SETAASA_CCC.md](6_18_10_4_SETAASA_CCC.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.18.10.5 GETSTATUS CCC | 97–98 | [6_18_10_5_GETSTATUS_CCC.md](6_18_10_5_GETSTATUS_CCC.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.18.10.6 DEVCAP CCC | 98–100 | [6_18_10_6_DEVCAP_CCC.md](6_18_10_6_DEVCAP_CCC.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.18.10.7 SETHID CCC 1 | 0–0 | [6_18_10_7_SETHID_CCC_1.md](6_18_10_7_SETHID_CCC_1.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.18.10.8 DEVCTRL CCC | 100–107 | [6_18_10_8_DEVCTRL_CCC.md](6_18_10_8_DEVCTRL_CCC.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.18.10.8.1 DEVCTRL CCC Examples - RegMod = ‘0’ | 103–105 | [6_18_10_8_1_DEVCTRL_CCC_Examples_RegMod_0.md](6_18_10_8_1_DEVCTRL_CCC_Examples_RegMod_0.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6.18.10.8.2 DEVCTRL CCC Examples - RegMod = ‘1’ | 105–107 | [6_18_10_8_2_DEVCTRL_CCC_Examples_RegMod_1.md](6_18_10_8_2_DEVCTRL_CCC_Examples_RegMod_1.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;6.18.11 IO Operation | 107–107 | [6_18_11_IO_Operation.md](6_18_11_IO_Operation.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;6.18.12 Bus Clear | 107–108 | [6_18_12_Bus_Clear.md](6_18_12_Bus_Clear.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;6.18.13 Bus Reset | 108–109 | [6_18_13_Bus_Reset.md](6_18_13_Bus_Reset.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;6.18.14 Command Truth Table | 109–109 | [6_18_14_Command_Truth_Table.md](6_18_14_Command_Truth_Table.md) |
| &nbsp;&nbsp;6.19 Application Notes | 109–111 | [6_19_Application_Notes.md](6_19_Application_Notes.md) |
| 7 Volatile Registers Space | 111–186 | [7_Volatile_Registers_Space.md](7_Volatile_Registers_Space.md) |
| &nbsp;&nbsp;7.1 Access Mechanism | 111–112 | [7_1_Access_Mechanism.md](7_1_Access_Mechanism.md) |
| &nbsp;&nbsp;7.2 Registers | 112–186 | [7_2_Registers.md](7_2_Registers.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;7.2.1 Register Map Breakdown | 112–112 | [7_2_1_Register_Map_Breakdown.md](7_2_1_Register_Map_Breakdown.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;7.2.2 Memory Protection | 112–112 | [7_2_2_Memory_Protection.md](7_2_2_Memory_Protection.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;7.2.3 Steps to Access DIMM Vendor Registers | 112–112 | [7_2_3_Steps_to_Access_DIMM_Vendor_Registers.md](7_2_3_Steps_to_Access_DIMM_Vendor_Registers.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;7.2.4 Steps to Change DIMM Vendor Region Password | 112–113 | [7_2_4_Steps_to_Change_DIMM_Vendor_Region_Password.md](7_2_4_Steps_to_Change_DIMM_Vendor_Region_Password.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;7.2.5 Steps to Burn or Program DIMM Vendor Region Registers | 113–113 | [7_2_5_Steps_to_Burn_or_Program_DIMM_Vendor_Region_Regist.md](7_2_5_Steps_to_Burn_or_Program_DIMM_Vendor_Region_Regist.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;7.2.6 Status Registers | 113–115 | [7_2_6_Status_Registers.md](7_2_6_Status_Registers.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;7.2.7 Clear Registers | 115–115 | [7_2_7_Clear_Registers.md](7_2_7_Clear_Registers.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;7.2.8 Mask Registers | 115–116 | [7_2_8_Mask_Registers.md](7_2_8_Mask_Registers.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;7.2.9 Host Region Register Map | 116–121 | [7_2_9_Host_Region_Register_Map.md](7_2_9_Host_Region_Register_Map.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;7.2.10 DIMM Vendor Region Register Map | 121–123 | [7_2_10_DIMM_Vendor_Region_Register_Map.md](7_2_10_DIMM_Vendor_Region_Register_Map.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;7.2.11 Register Definition | 123–186 | [7_2_11_Register_Definition.md](7_2_11_Register_Definition.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7.2.11.1 Threshold Registers | 142–164 | [7_2_11_1_Threshold_Registers.md](7_2_11_1_Threshold_Registers.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7.2.11.2 Error Injection Registers | 164–166 | [7_2_11_2_Error_Injection_Registers.md](7_2_11_2_Error_Injection_Registers.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7.2.11.3 Password Input and Command Code | 166–186 | [7_2_11_3_Password_Input_and_Command_Code.md](7_2_11_3_Password_Input_and_Command_Code.md) |
