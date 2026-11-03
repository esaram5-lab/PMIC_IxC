# PMIC5200 — Sections

Source: JESD301-3 Version 1.0 (October 2025). One file per section; register tables are linked to `../registers/` instead of being repeated.

| Section | Pages | File |
|---|---|---|
| 1 Scope | 1–3 | [1_Scope.md](1_Scope.md) |
| 2 Package | 3–7 | [2_Package.md](2_Package.md) |
| 3 Electrical Specifications | 7–25 | [3_Electrical_Specifications.md](3_Electrical_Specifications.md) |
| &nbsp;&nbsp;3.1 Input Supply and Output Regulator Electrical Characteristics | 7–11 | [3_1_Input_Supply_and_Output_Regulator_Electrical_Chara.md](3_1_Input_Supply_and_Output_Regulator_Electrical_Chara.md) |
| &nbsp;&nbsp;3.2 Efficiency | 11–13 | [3_2_Efficiency.md](3_2_Efficiency.md) |
| &nbsp;&nbsp;3.3 I2C or I3C Basic DC and AC Electrical Characteristics | 13–18 | [3_3_I2C_or_I3C_Basic_DC_and_AC_Electrical_Characterist.md](3_3_I2C_or_I3C_Basic_DC_and_AC_Electrical_Characterist.md) |
| &nbsp;&nbsp;3.4 Measurement Condition | 18–18 | [3_4_Measurement_Condition.md](3_4_Measurement_Condition.md) |
| &nbsp;&nbsp;3.5 PMIC AC Timing Parameters | 18–22 | [3_5_PMIC_AC_Timing_Parameters.md](3_5_PMIC_AC_Timing_Parameters.md) |
| &nbsp;&nbsp;3.6 Absolute Maximum Ratings | 22–23 | [3_6_Absolute_Maximum_Ratings.md](3_6_Absolute_Maximum_Ratings.md) |
| &nbsp;&nbsp;3.7 ESD Requirements | 23–24 | [3_7_ESD_Requirements.md](3_7_ESD_Requirements.md) |
| &nbsp;&nbsp;3.8 Thermal Characteristics | 24–25 | [3_8_Thermal_Characteristics.md](3_8_Thermal_Characteristics.md) |
| 4 Functional Operation | 25–72 | [4_Functional_Operation.md](4_Functional_Operation.md) |
| &nbsp;&nbsp;4.1 PMIC Input Voltage Supply and Ramp Condition | 25–25 | [4_1_PMIC_Input_Voltage_Supply_and_Ramp_Condition.md](4_1_PMIC_Input_Voltage_Supply_and_Ramp_Condition.md) |
| &nbsp;&nbsp;4.2 Power Up Initialization Sequence | 25–30 | [4_2_Power_Up_Initialization_Sequence.md](4_2_Power_Up_Initialization_Sequence.md) |
| &nbsp;&nbsp;4.3 PMIC Output Rail Turn On Timing | 30–31 | [4_3_PMIC_Output_Rail_Turn_On_Timing.md](4_3_PMIC_Output_Rail_Turn_On_Timing.md) |
| &nbsp;&nbsp;4.4 Auto Power On | 31–31 | [4_4_Auto_Power_On.md](4_4_Auto_Power_On.md) |
| &nbsp;&nbsp;4.5 Secure Mode and Programmable Mode of Operation | 31–32 | [4_5_Secure_Mode_and_Programmable_Mode_of_Operation.md](4_5_Secure_Mode_and_Programmable_Mode_of_Operation.md) |
| &nbsp;&nbsp;4.6 Power Down Output Regulators | 32–43 | [4_6_Power_Down_Output_Regulators.md](4_6_Power_Down_Output_Regulators.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;4.6.1 Normal Power Down Sequence | 32–34 | [4_6_1_Normal_Power_Down_Sequence.md](4_6_1_Normal_Power_Down_Sequence.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;4.6.2 Programmable Mode Operation; R1A[4] = ‘0’ | 34–36 | [4_6_2_Programmable_Mode_Operation_R1A_4_0.md](4_6_2_Programmable_Mode_Operation_R1A_4_0.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;4.6.3 Programmable Mode Operation; R1A[4] = ‘1’ | 36–39 | [4_6_3_Programmable_Mode_Operation_R1A_4_1.md](4_6_3_Programmable_Mode_Operation_R1A_4_1.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;4.6.4 Secure Mode Operation; R1A[4] = ‘0’ | 39–40 | [4_6_4_Secure_Mode_Operation_R1A_4_0.md](4_6_4_Secure_Mode_Operation_R1A_4_0.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;4.6.5 Secure Mode Operation; R1A[4] = ‘1’ | 40–43 | [4_6_5_Secure_Mode_Operation_R1A_4_1.md](4_6_5_Secure_Mode_Operation_R1A_4_1.md) |
| &nbsp;&nbsp;4.7 PMIC Output Rail Off Timing Due to Fault Event | 43–44 | [4_7_PMIC_Output_Rail_Off_Timing_Due_to_Fault_Event.md](4_7_PMIC_Output_Rail_Off_Timing_Due_to_Fault_Event.md) |
| &nbsp;&nbsp;4.8 Power Good (PWR_GOOD) Signal | 44–47 | [4_8_Power_Good_PWR_GOOD_Signal.md](4_8_Power_Good_PWR_GOOD_Signal.md) |
| &nbsp;&nbsp;4.9 Idle Condition and Quiescent Power State | 47–50 | [4_9_Idle_Condition_and_Quiescent_Power_State.md](4_9_Idle_Condition_and_Quiescent_Power_State.md) |
| &nbsp;&nbsp;4.10 GSI_n Pin Function | 50–51 | [4_10_GSI_n_Pin_Function.md](4_10_GSI_n_Pin_Function.md) |
| &nbsp;&nbsp;4.11 Unlock Pin Function | 51–58 | [4_11_Unlock_Pin_Function.md](4_11_Unlock_Pin_Function.md) |
| &nbsp;&nbsp;4.12 DVFSQ_n Pin Function and DVFSQ State | 58–59 | [4_12_DVFSQ_n_Pin_Function_and_DVFSQ_State.md](4_12_DVFSQ_n_Pin_Function_and_DVFSQ_State.md) |
| &nbsp;&nbsp;4.13 SWB_Disable Input Pin Function | 59–59 | [4_13_SWB_Disable_Input_Pin_Function.md](4_13_SWB_Disable_Input_Pin_Function.md) |
| &nbsp;&nbsp;4.14 VR_EN Input Pin Function | 59–60 | [4_14_VR_EN_Input_Pin_Function.md](4_14_VR_EN_Input_Pin_Function.md) |
| &nbsp;&nbsp;4.15 Function Interrupt - PWR_GOOD Output Signal | 60–68 | [4_15_Function_Interrupt_PWR_GOOD_Output_Signal.md](4_15_Function_Interrupt_PWR_GOOD_Output_Signal.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;4.15.1 Input Power Good Status | 63–63 | [4_15_1_Input_Power_Good_Status.md](4_15_1_Input_Power_Good_Status.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;4.15.2 Input Over Voltage Protection | 63–64 | [4_15_2_Input_Over_Voltage_Protection.md](4_15_2_Input_Over_Voltage_Protection.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;4.15.3 Output Power Good Status | 64–65 | [4_15_3_Output_Power_Good_Status.md](4_15_3_Output_Power_Good_Status.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;4.15.4 Output Over Voltage Protection | 65–66 | [4_15_4_Output_Over_Voltage_Protection.md](4_15_4_Output_Over_Voltage_Protection.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;4.15.5 Output Under Voltage and VIN_Bulk Under Voltage Lockout Protection | 66–66 | [4_15_5_Output_Under_Voltage_and_VIN_Bulk_Under_Voltage_Lo.md](4_15_5_Output_Under_Voltage_and_VIN_Bulk_Under_Voltage_Lo.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;4.15.6 Output Current Limiter Warning Event | 66–67 | [4_15_6_Output_Current_Limiter_Warning_Event.md](4_15_6_Output_Current_Limiter_Warning_Event.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;4.15.7 Output High Current Consumption Warning Event | 67–67 | [4_15_7_Output_High_Current_Consumption_Warning_Event.md](4_15_7_Output_High_Current_Consumption_Warning_Event.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;4.15.8 PMIC High Temperature Warning and Critical Temperature Protection | 67–68 | [4_15_8_PMIC_High_Temperature_Warning_and_Critical_Tempera.md](4_15_8_PMIC_High_Temperature_Warning_and_Critical_Tempera.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;4.15.9 Packet Error Code (PEC) and Parity Error Event | 68–68 | [4_15_9_Packet_Error_Code_PEC_and_Parity_Error_Event.md](4_15_9_Packet_Error_Code_PEC_and_Parity_Error_Event.md) |
| &nbsp;&nbsp;4.16 Analog to Digital Converter (ADC) | 68–70 | [4_16_Analog_to_Digital_Converter_ADC.md](4_16_Analog_to_Digital_Converter_ADC.md) |
| &nbsp;&nbsp;4.17 PMIC Address ID (PID) | 70–70 | [4_17_PMIC_Address_ID_PID.md](4_17_PMIC_Address_ID_PID.md) |
| &nbsp;&nbsp;4.18 Error Injection | 70–71 | [4_18_Error_Injection.md](4_18_Error_Injection.md) |
| &nbsp;&nbsp;4.19 Acoustic Noise | 71–72 | [4_19_Acoustic_Noise.md](4_19_Acoustic_Noise.md) |
| 5 I2C and I3C Basic Operation | 72–120 | [5_I2C_and_I3C_Basic_Operation.md](5_I2C_and_I3C_Basic_Operation.md) |
| &nbsp;&nbsp;5.1 Device Interface - Protocol | 72–73 | [5_1_Device_Interface_Protocol.md](5_1_Device_Interface_Protocol.md) |
| &nbsp;&nbsp;5.2 Configuration Register Addressing | 73–73 | [5_2_Configuration_Register_Addressing.md](5_2_Configuration_Register_Addressing.md) |
| &nbsp;&nbsp;5.3 I2C Target Protocol | 73–76 | [5_3_I2C_Target_Protocol.md](5_3_I2C_Target_Protocol.md) |
| &nbsp;&nbsp;5.4 I3C Basic Target Protocol | 76–120 | [5_4_I3C_Basic_Target_Protocol.md](5_4_I3C_Basic_Target_Protocol.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;5.4.1 Write Operation Data Packet | 76–80 | [5_4_1_Write_Operation_Data_Packet.md](5_4_1_Write_Operation_Data_Packet.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;5.4.2 Read Operation Data Packet | 80–87 | [5_4_2_Read_Operation_Data_Packet.md](5_4_2_Read_Operation_Data_Packet.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;5.4.3 Default Read Address Pointer Mode | 87–93 | [5_4_3_Default_Read_Address_Pointer_Mode.md](5_4_3_Default_Read_Address_Pointer_Mode.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;5.4.4 In Band Interrupt (IBI) | 93–97 | [5_4_4_In_Band_Interrupt_IBI.md](5_4_4_In_Band_Interrupt_IBI.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;5.4.5 Packet Error Check Function | 97–98 | [5_4_5_Packet_Error_Check_Function.md](5_4_5_Packet_Error_Check_Function.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;5.4.6 Parity Error Check Function | 98–98 | [5_4_6_Parity_Error_Check_Function.md](5_4_6_Parity_Error_Check_Function.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;5.4.7 Packet Error Check and Parity Error Handling | 98–102 | [5_4_7_Packet_Error_Check_and_Parity_Error_Handling.md](5_4_7_Packet_Error_Check_and_Parity_Error_Handling.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;5.4.8 CCC Packet Error Handling | 102–102 | [5_4_8_CCC_Packet_Error_Handling.md](5_4_8_CCC_Packet_Error_Handling.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;5.4.9 Error Reporting | 102–103 | [5_4_9_Error_Reporting.md](5_4_9_Error_Reporting.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;5.4.10 I3C Basic Common Command Codes (CCC) | 103–117 | [5_4_10_I3C_Basic_Common_Command_Codes_CCC.md](5_4_10_I3C_Basic_Common_Command_Codes_CCC.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.4.10.1 ENEC CCC | 103–105 | [5_4_10_1_ENEC_CCC.md](5_4_10_1_ENEC_CCC.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.4.10.2 DISEC CCC | 105–107 | [5_4_10_2_DISEC_CCC.md](5_4_10_2_DISEC_CCC.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.4.10.3 RSTDAA CCC | 107–107 | [5_4_10_3_RSTDAA_CCC.md](5_4_10_3_RSTDAA_CCC.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.4.10.4 SETAASA CCC | 107–108 | [5_4_10_4_SETAASA_CCC.md](5_4_10_4_SETAASA_CCC.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.4.10.5 GETSTATUS CCC | 108–109 | [5_4_10_5_GETSTATUS_CCC.md](5_4_10_5_GETSTATUS_CCC.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.4.10.6 DEVCAP CCC | 109–110 | [5_4_10_6_DEVCAP_CCC.md](5_4_10_6_DEVCAP_CCC.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.4.10.7 SETHID CCC | 110–111 | [5_4_10_7_SETHID_CCC.md](5_4_10_7_SETHID_CCC.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.4.10.8 DEVCTRL CCC | 111–117 | [5_4_10_8_DEVCTRL_CCC.md](5_4_10_8_DEVCTRL_CCC.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.4.10.8.1 DEVCTRL CCC Examples - RegMod = ‘0’ | 114–115 | [5_4_10_8_1_DEVCTRL_CCC_Examples_RegMod_0.md](5_4_10_8_1_DEVCTRL_CCC_Examples_RegMod_0.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.4.10.8.2 DEVCTRL CCC Examples - RegMod = ‘1’ | 115–117 | [5_4_10_8_2_DEVCTRL_CCC_Examples_RegMod_1.md](5_4_10_8_2_DEVCTRL_CCC_Examples_RegMod_1.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;5.4.11 IO Operation | 117–117 | [5_4_11_IO_Operation.md](5_4_11_IO_Operation.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;5.4.12 Bus Clear | 117–118 | [5_4_12_Bus_Clear.md](5_4_12_Bus_Clear.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;5.4.13 Bus Reset | 118–119 | [5_4_13_Bus_Reset.md](5_4_13_Bus_Reset.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;5.4.14 Command Truth Table | 119–120 | [5_4_14_Command_Truth_Table.md](5_4_14_Command_Truth_Table.md) |
| 6 Schematics | 120–122 | [6_Schematics.md](6_Schematics.md) |
| 7 Inductor Specification | 122–125 | [7_Inductor_Specification.md](7_Inductor_Specification.md) |
| 8 Registers | 125–221 | [8_Registers.md](8_Registers.md) |
| &nbsp;&nbsp;8.1 Register Attribute Definition | 125–125 | [8_1_Register_Attribute_Definition.md](8_1_Register_Attribute_Definition.md) |
| &nbsp;&nbsp;8.2 Register Map Breakdown | 125–127 | [8_2_Register_Map_Breakdown.md](8_2_Register_Map_Breakdown.md) |
| &nbsp;&nbsp;8.3 Host Region Register Map | 127–133 | [8_3_Host_Region_Register_Map.md](8_3_Host_Region_Register_Map.md) |
| &nbsp;&nbsp;8.4 Register Definition | 133–191 | [8_4_Register_Definition.md](8_4_Register_Definition.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;8.4.1 Status Registers | 133–146 | [8_4_1_Status_Registers.md](8_4_1_Status_Registers.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;8.4.2 Clear Registers | 146–149 | [8_4_2_Clear_Registers.md](8_4_2_Clear_Registers.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;8.4.3 Mask Registers | 149–154 | [8_4_3_Mask_Registers.md](8_4_3_Mask_Registers.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;8.4.4 Threshold and Configuration Registers | 154–182 | [8_4_4_Threshold_and_Configuration_Registers.md](8_4_4_Threshold_and_Configuration_Registers.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;8.4.5 Password Input and Command Code | 182–183 | [8_4_5_Password_Input_and_Command_Code.md](8_4_5_Password_Input_and_Command_Code.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;8.4.6 Miscellaneous Registers | 183–191 | [8_4_6_Miscellaneous_Registers.md](8_4_6_Miscellaneous_Registers.md) |
| &nbsp;&nbsp;8.5 CAMM2 Vendor Region Register Definition | 191–221 | [8_5_CAMM2_Vendor_Region_Register_Definition.md](8_5_CAMM2_Vendor_Region_Register_Definition.md) |
| 9 Package Outline Drawings | 221–224 | [9_Package_Outline_Drawings.md](9_Package_Outline_Drawings.md) |
