# PMIC5030 — Sections

Source: JESD301-5 Version 1.00 (January 2026). One file per section; register tables are linked to `../registers/` instead of being repeated.

| Section | Pages | File |
|---|---|---|
| 1 Scope | 1–1 | [1_Scope.md](1_Scope.md) |
| 2 Description | 1–3 | [2_Description.md](2_Description.md) |
| 3 Terms and Definitions | 3–4 | [3_Terms_and_Definitions.md](3_Terms_and_Definitions.md) |
| 4 Package Pinout and Pin Description | 4–9 | [4_Package_Pinout_and_Pin_Description.md](4_Package_Pinout_and_Pin_Description.md) |
| 5 Electrical Specifications | 9–26 | [5_Electrical_Specifications.md](5_Electrical_Specifications.md) |
| &nbsp;&nbsp;5.1 Input Supply and Output Regulator Electrical Characteristics | 9–17 | [5_1_Input_Supply_and_Output_Regulator_Electrical_Chara.md](5_1_Input_Supply_and_Output_Regulator_Electrical_Chara.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;5.1.1 Input Supply Electrical Characteristics | 9–10 | [5_1_1_Input_Supply_Electrical_Characteristics.md](5_1_1_Input_Supply_Electrical_Characteristics.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;5.1.2 Switch Regulator Output Electrical Characteristics | 10–14 | [5_1_2_Switch_Regulator_Output_Electrical_Characteristics.md](5_1_2_Switch_Regulator_Output_Electrical_Characteristics.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;5.1.3 Switch Regulator Efficiency | 14–15 | [5_1_3_Switch_Regulator_Efficiency.md](5_1_3_Switch_Regulator_Efficiency.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;5.1.4 LDO Output Regulator Characteristics | 15–16 | [5_1_4_LDO_Output_Regulator_Characteristics.md](5_1_4_LDO_Output_Regulator_Characteristics.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;5.1.5 PMIC AC Timing Parameters | 16–17 | [5_1_5_PMIC_AC_Timing_Parameters.md](5_1_5_PMIC_AC_Timing_Parameters.md) |
| &nbsp;&nbsp;5.2 I2C, I3C Basic and Interface DC and AC Electrical Characteristics | 17–23 | [5_2_I2C_I3C_Basic_and_Interface_DC_and_AC_Electrical_C.md](5_2_I2C_I3C_Basic_and_Interface_DC_and_AC_Electrical_C.md) |
| &nbsp;&nbsp;5.3 Thermal Characteristics | 23–24 | [5_3_Thermal_Characteristics.md](5_3_Thermal_Characteristics.md) |
| &nbsp;&nbsp;5.4 Absolute Maximum Rating | 24–26 | [5_4_Absolute_Maximum_Rating.md](5_4_Absolute_Maximum_Rating.md) |
| 6 Functional Operation | 26–62 | [6_Functional_Operation.md](6_Functional_Operation.md) |
| &nbsp;&nbsp;6.1 PMIC Input Voltage Supplies and Ramp Condition | 26–26 | [6_1_PMIC_Input_Voltage_Supplies_and_Ramp_Condition.md](6_1_PMIC_Input_Voltage_Supplies_and_Ramp_Condition.md) |
| &nbsp;&nbsp;6.2 Power Up Initialization Sequence | 26–28 | [6_2_Power_Up_Initialization_Sequence.md](6_2_Power_Up_Initialization_Sequence.md) |
| &nbsp;&nbsp;6.3 Power Up Sequence | 28–31 | [6_3_Power_Up_Sequence.md](6_3_Power_Up_Sequence.md) |
| &nbsp;&nbsp;6.4 Enabling PMIC Output Switch Voltage Regulators | 31–32 | [6_4_Enabling_PMIC_Output_Switch_Voltage_Regulators.md](6_4_Enabling_PMIC_Output_Switch_Voltage_Regulators.md) |
| &nbsp;&nbsp;6.5 Auto Power On | 32–33 | [6_5_Auto_Power_On.md](6_5_Auto_Power_On.md) |
| &nbsp;&nbsp;6.6 Power On with VR_OE Pin | 33–35 | [6_6_Power_On_with_VR_OE_Pin.md](6_6_Power_On_with_VR_OE_Pin.md) |
| &nbsp;&nbsp;6.7 Combinations to Turn On and Turn Off PMIC Regulators | 35–35 | [6_7_Combinations_to_Turn_On_and_Turn_Off_PMIC_Regulato.md](6_7_Combinations_to_Turn_On_and_Turn_Off_PMIC_Regulato.md) |
| &nbsp;&nbsp;6.8 Power Down Output Regulators | 35–39 | [6_8_Power_Down_Output_Regulators.md](6_8_Power_Down_Output_Regulators.md) |
| &nbsp;&nbsp;6.9 CAMP Signal | 39–41 | [6_9_CAMP_Signal.md](6_9_CAMP_Signal.md) |
| &nbsp;&nbsp;6.10 GSI_n Signal | 41–41 | [6_10_GSI_n_Signal.md](6_10_GSI_n_Signal.md) |
| &nbsp;&nbsp;6.11 Reset_n Pin Function | 41–41 | [6_11_Reset_n_Pin_Function.md](6_11_Reset_n_Pin_Function.md) |
| &nbsp;&nbsp;6.12 State Transition Diagram | 41–45 | [6_12_State_Transition_Diagram.md](6_12_State_Transition_Diagram.md) |
| &nbsp;&nbsp;6.13 Function Interrupt - CAMP and GSI_n Output Signals | 45–50 | [6_13_Function_Interrupt_CAMP_and_GSI_n_Output_Signals.md](6_13_Function_Interrupt_CAMP_and_GSI_n_Output_Signals.md) |
| &nbsp;&nbsp;6.14 Input Power Good Status | 50–50 | [6_14_Input_Power_Good_Status.md](6_14_Input_Power_Good_Status.md) |
| &nbsp;&nbsp;6.15 Input Over Voltage Protection | 50–51 | [6_15_Input_Over_Voltage_Protection.md](6_15_Input_Over_Voltage_Protection.md) |
| &nbsp;&nbsp;6.16 Output Power Good Status | 51–52 | [6_16_Output_Power_Good_Status.md](6_16_Output_Power_Good_Status.md) |
| &nbsp;&nbsp;6.17 Output Over Voltage Protection | 52–52 | [6_17_Output_Over_Voltage_Protection.md](6_17_Output_Over_Voltage_Protection.md) |
| &nbsp;&nbsp;6.18 Output Under Voltage and VIN_Bulk Under Voltage Lockout Protection | 52–53 | [6_18_Output_Under_Voltage_and_VIN_Bulk_Under_Voltage_Lo.md](6_18_Output_Under_Voltage_and_VIN_Bulk_Under_Voltage_Lo.md) |
| &nbsp;&nbsp;6.19 Output Current Limiter Warning Event | 53–54 | [6_19_Output_Current_Limiter_Warning_Event.md](6_19_Output_Current_Limiter_Warning_Event.md) |
| &nbsp;&nbsp;6.20 Output High Current Consumption Warning Event | 54–54 | [6_20_Output_High_Current_Consumption_Warning_Event.md](6_20_Output_High_Current_Consumption_Warning_Event.md) |
| &nbsp;&nbsp;6.21 PMIC LDO Output Failure | 54–54 | [6_21_PMIC_LDO_Output_Failure.md](6_21_PMIC_LDO_Output_Failure.md) |
| &nbsp;&nbsp;6.22 PMIC High Temperature Warning and Critical Temperature Protection | 54–55 | [6_22_PMIC_High_Temperature_Warning_and_Critical_Tempera.md](6_22_PMIC_High_Temperature_Warning_and_Critical_Tempera.md) |
| &nbsp;&nbsp;6.23 VIN_Mgmt to VIN_Bulk Input Supply Switchover Event | 55–56 | [6_23_VIN_Mgmt_to_VIN_Bulk_Input_Supply_Switchover_Event.md](6_23_VIN_Mgmt_to_VIN_Bulk_Input_Supply_Switchover_Event.md) |
| &nbsp;&nbsp;6.24 Valid VIN_Mgmt Supply Detection in Switchover Mode | 56–56 | [6_24_Valid_VIN_Mgmt_Supply_Detection_in_Switchover_Mode.md](6_24_Valid_VIN_Mgmt_Supply_Detection_in_Switchover_Mode.md) |
| &nbsp;&nbsp;6.25 Packet Error Code (PEC) and Parity Error Event | 56–56 | [6_25_Packet_Error_Code_PEC_and_Parity_Error_Event.md](6_25_Packet_Error_Code_PEC_and_Parity_Error_Event.md) |
| &nbsp;&nbsp;6.26 Analog to Digital Converter (ADC) | 56–58 | [6_26_Analog_to_Digital_Converter_ADC.md](6_26_Analog_to_Digital_Converter_ADC.md) |
| &nbsp;&nbsp;6.27 PMIC Address ID (PID) | 58–58 | [6_27_PMIC_Address_ID_PID.md](6_27_PMIC_Address_ID_PID.md) |
| &nbsp;&nbsp;6.28 Error Injection | 58–59 | [6_28_Error_Injection.md](6_28_Error_Injection.md) |
| &nbsp;&nbsp;6.29 Error Log Count Enhancement | 59–59 | [6_29_Error_Log_Count_Enhancement.md](6_29_Error_Log_Count_Enhancement.md) |
| &nbsp;&nbsp;6.30 NVM MTP CRC Computation and Error Check | 59–62 | [6_30_NVM_MTP_CRC_Computation_and_Error_Check.md](6_30_NVM_MTP_CRC_Computation_and_Error_Check.md) |
| 7 I2C and I3C Basic Interface Operation | 62–114 | [7_I2C_and_I3C_Basic_Interface_Operation.md](7_I2C_and_I3C_Basic_Interface_Operation.md) |
| &nbsp;&nbsp;7.1 Device Interface - Protocol | 62–63 | [7_1_Device_Interface_Protocol.md](7_1_Device_Interface_Protocol.md) |
| &nbsp;&nbsp;7.2 Configuration Register Addressing | 63–64 | [7_2_Configuration_Register_Addressing.md](7_2_Configuration_Register_Addressing.md) |
| &nbsp;&nbsp;7.3 I2C Target Protocol | 64–66 | [7_3_I2C_Target_Protocol.md](7_3_I2C_Target_Protocol.md) |
| &nbsp;&nbsp;7.4 I3C Basic Target Protocol | 66–85 | [7_4_I3C_Basic_Target_Protocol.md](7_4_I3C_Basic_Target_Protocol.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;7.4.1 Write Operation Data Packet | 66–71 | [7_4_1_Write_Operation_Data_Packet.md](7_4_1_Write_Operation_Data_Packet.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;7.4.2 Read Operation - Data Packet | 71–78 | [7_4_2_Read_Operation_Data_Packet.md](7_4_2_Read_Operation_Data_Packet.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;7.4.3 Default Read Address Pointer Mode | 78–85 | [7_4_3_Default_Read_Address_Pointer_Mode.md](7_4_3_Default_Read_Address_Pointer_Mode.md) |
| &nbsp;&nbsp;7.5 In Band Interrupt (IBI) | 85–111 | [7_5_In_Band_Interrupt_IBI.md](7_5_In_Band_Interrupt_IBI.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;7.5.1 Enabling and Disabling In Band Interrupt Function | 85–86 | [7_5_1_Enabling_and_Disabling_In_Band_Interrupt_Function.md](7_5_1_Enabling_and_Disabling_In_Band_Interrupt_Function.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;7.5.2 Mechanics of Interrupt Generation | 86–88 | [7_5_2_Mechanics_of_Interrupt_Generation.md](7_5_2_Mechanics_of_Interrupt_Generation.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;7.5.3 Interrupt Arbitration | 88–90 | [7_5_3_Interrupt_Arbitration.md](7_5_3_Interrupt_Arbitration.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;7.5.4 Clearing Device Status and IBI Status Registers | 90–90 | [7_5_4_Clearing_Device_Status_and_IBI_Status_Registers.md](7_5_4_Clearing_Device_Status_and_IBI_Status_Registers.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;7.5.5 Packet Error Check (PEC) Function | 90–91 | [7_5_5_Packet_Error_Check_PEC_Function.md](7_5_5_Packet_Error_Check_PEC_Function.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;7.5.6 Parity Error Check Function | 91–91 | [7_5_6_Parity_Error_Check_Function.md](7_5_6_Parity_Error_Check_Function.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;7.5.7 Packet Error Check and Parity Error Handling | 91–96 | [7_5_7_Packet_Error_Check_and_Parity_Error_Handling.md](7_5_7_Packet_Error_Check_and_Parity_Error_Handling.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;7.5.8 CCC Packet Error Handling | 96–96 | [7_5_8_CCC_Packet_Error_Handling.md](7_5_8_CCC_Packet_Error_Handling.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;7.5.9 Error Reporting | 96–96 | [7_5_9_Error_Reporting.md](7_5_9_Error_Reporting.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;7.5.10 I3C Basic Common Command Codes (CCC) | 96–111 | [7_5_10_I3C_Basic_Common_Command_Codes_CCC.md](7_5_10_I3C_Basic_Common_Command_Codes_CCC.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7.5.10.1 ENEC CCC | 97–99 | [7_5_10_1_ENEC_CCC.md](7_5_10_1_ENEC_CCC.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7.5.10.2 DISEC CCC | 99–101 | [7_5_10_2_DISEC_CCC.md](7_5_10_2_DISEC_CCC.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7.5.10.3 RSTDAA CCC | 101–101 | [7_5_10_3_RSTDAA_CCC.md](7_5_10_3_RSTDAA_CCC.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7.5.10.4 SETAASA CCC | 101–102 | [7_5_10_4_SETAASA_CCC.md](7_5_10_4_SETAASA_CCC.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7.5.10.5 GETSTATUS CCC | 102–103 | [7_5_10_5_GETSTATUS_CCC.md](7_5_10_5_GETSTATUS_CCC.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7.5.10.6 DEVCAP CCC | 103–104 | [7_5_10_6_DEVCAP_CCC.md](7_5_10_6_DEVCAP_CCC.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7.5.10.7 SETHID CCC | 104–105 | [7_5_10_7_SETHID_CCC.md](7_5_10_7_SETHID_CCC.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7.5.10.8 DEVCTRL CCC | 105–111 | [7_5_10_8_DEVCTRL_CCC.md](7_5_10_8_DEVCTRL_CCC.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7.5.10.8.1 DEVCTRL CCC Examples - RegMod = ‘0’ | 108–110 | [7_5_10_8_1_DEVCTRL_CCC_Examples_RegMod_0.md](7_5_10_8_1_DEVCTRL_CCC_Examples_RegMod_0.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7.5.10.8.2 DEVCTRL CCC Examples - RegMod = ‘1’ | 110–111 | [7_5_10_8_2_DEVCTRL_CCC_Examples_RegMod_1.md](7_5_10_8_2_DEVCTRL_CCC_Examples_RegMod_1.md) |
| &nbsp;&nbsp;7.6 IO Operation | 111–112 | [7_6_IO_Operation.md](7_6_IO_Operation.md) |
| &nbsp;&nbsp;7.7 Bus Clear | 112–112 | [7_7_Bus_Clear.md](7_7_Bus_Clear.md) |
| &nbsp;&nbsp;7.8 Bus Reset | 112–113 | [7_8_Bus_Reset.md](7_8_Bus_Reset.md) |
| &nbsp;&nbsp;7.9 Command Truth Table | 113–114 | [7_9_Command_Truth_Table.md](7_9_Command_Truth_Table.md) |
| 8 Example Schematic | 114–119 | [8_Example_Schematic.md](8_Example_Schematic.md) |
| 9 Inductor Specification | 119–120 | [9_Inductor_Specification.md](9_Inductor_Specification.md) |
| 10 Application Notes | 120–122 | [10_Application_Notes.md](10_Application_Notes.md) |
| 11 Registers | 122–267 | [11_Registers.md](11_Registers.md) |
| &nbsp;&nbsp;11.1 Register Attribute Definition | 122–122 | [11_1_Register_Attribute_Definition.md](11_1_Register_Attribute_Definition.md) |
| &nbsp;&nbsp;11.2 Register Map Breakdown | 122–124 | [11_2_Register_Map_Breakdown.md](11_2_Register_Map_Breakdown.md) |
| &nbsp;&nbsp;11.3 Host Region Register Map | 124–132 | [11_3_Host_Region_Register_Map.md](11_3_Host_Region_Register_Map.md) |
| &nbsp;&nbsp;11.4 Host Region Register Definition | 132–220 | [11_4_Host_Region_Register_Definition.md](11_4_Host_Region_Register_Definition.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;11.4.1 Status Registers | 132–146 | [11_4_1_Status_Registers.md](11_4_1_Status_Registers.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;11.4.2 Clear Registers | 146–152 | [11_4_2_Clear_Registers.md](11_4_2_Clear_Registers.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;11.4.3 Mask Registers | 152–158 | [11_4_3_Mask_Registers.md](11_4_3_Mask_Registers.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;11.4.4 Threshold and Configuration Registers | 158–186 | [11_4_4_Threshold_and_Configuration_Registers.md](11_4_4_Threshold_and_Configuration_Registers.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;11.4.5 Password Input and Command Code | 186–187 | [11_4_5_Password_Input_and_Command_Code.md](11_4_5_Password_Input_and_Command_Code.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;11.4.6 Miscellaneous Registers | 187–220 | [11_4_6_Miscellaneous_Registers.md](11_4_6_Miscellaneous_Registers.md) |
| &nbsp;&nbsp;11.5 DIMM Vendor Region Register Map | 220–223 | [11_5_DIMM_Vendor_Region_Register_Map.md](11_5_DIMM_Vendor_Region_Register_Map.md) |
| &nbsp;&nbsp;11.6 DIMM Vendor Region Register Definition | 223–267 | [11_6_DIMM_Vendor_Region_Register_Definition.md](11_6_DIMM_Vendor_Region_Register_Definition.md) |
| 12 Package Drawings | 267–270 | [12_Package_Drawings.md](12_Package_Drawings.md) |
