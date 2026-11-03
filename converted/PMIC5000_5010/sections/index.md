# PMIC5000/PMIC5010 — Sections

Source: JESD301-1A.03 Rev. 1.8.5 (February 2025). One file per section; register tables are linked to `../registers/` instead of being repeated.

| Section | Pages | File |
|---|---|---|
| 1 Scope | 1–1 | [1_Scope.md](1_Scope.md) |
| 2 Device Standard | 1–102 | [2_Device_Standard.md](2_Device_Standard.md) |
| &nbsp;&nbsp;2.1 Description | 1–3 | [2_1_Description.md](2_1_Description.md) |
| &nbsp;&nbsp;2.2 Input Supply and Output Regulator Electrical Characteristics | 3–12 | [2_2_Input_Supply_and_Output_Regulator_Electrical_Chara.md](2_2_Input_Supply_and_Output_Regulator_Electrical_Chara.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;2.2.1 Input Supply Electrical Characteristics | 3–4 | [2_2_1_Input_Supply_Electrical_Characteristics.md](2_2_1_Input_Supply_Electrical_Characteristics.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;2.2.2 Switch Regulator Output Electrical Characteristics | 4–9 | [2_2_2_Switch_Regulator_Output_Electrical_Characteristics.md](2_2_2_Switch_Regulator_Output_Electrical_Characteristics.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;2.2.3 Switch Regulator Efficiency | 9–10 | [2_2_3_Switch_Regulator_Efficiency.md](2_2_3_Switch_Regulator_Efficiency.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;2.2.4 LDO Output Regulator Characteristics | 10–11 | [2_2_4_LDO_Output_Regulator_Characteristics.md](2_2_4_LDO_Output_Regulator_Characteristics.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;2.2.5 PMIC AC Timing Parameters | 11–12 | [2_2_5_PMIC_AC_Timing_Parameters.md](2_2_5_PMIC_AC_Timing_Parameters.md) |
| &nbsp;&nbsp;2.3 I2C, I3C Basic and Interface DC and AC Electrical Characteristics | 12–17 | [2_3_I2C_I3C_Basic_and_Interface_DC_and_AC_Electrical_C.md](2_3_I2C_I3C_Basic_and_Interface_DC_and_AC_Electrical_C.md) |
| &nbsp;&nbsp;2.4 Thermal Characteristics | 17–18 | [2_4_Thermal_Characteristics.md](2_4_Thermal_Characteristics.md) |
| &nbsp;&nbsp;2.5 Absolute Maximum Rating | 18–20 | [2_5_Absolute_Maximum_Rating.md](2_5_Absolute_Maximum_Rating.md) |
| &nbsp;&nbsp;2.6 Example Schematic | 20–23 | [2_6_Example_Schematic.md](2_6_Example_Schematic.md) |
| &nbsp;&nbsp;2.7 Functional Operation | 23–45 | [2_7_Functional_Operation.md](2_7_Functional_Operation.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;2.7.1 PMIC Input Voltage Supplies and Ramp Condition | 23–23 | [2_7_1_PMIC_Input_Voltage_Supplies_and_Ramp_Condition.md](2_7_1_PMIC_Input_Voltage_Supplies_and_Ramp_Condition.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;2.7.2 Power Up Initialization Sequence | 23–25 | [2_7_2_Power_Up_Initialization_Sequence.md](2_7_2_Power_Up_Initialization_Sequence.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;2.7.3 Power Up Sequence | 25–29 | [2_7_3_Power_Up_Sequence.md](2_7_3_Power_Up_Sequence.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;2.7.4 Enabling PMIC Output Switch Voltage Regulators | 29–30 | [2_7_4_Enabling_PMIC_Output_Switch_Voltage_Regulators.md](2_7_4_Enabling_PMIC_Output_Switch_Voltage_Regulators.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;2.7.5 Power Down Output Regulators | 30–31 | [2_7_5_Power_Down_Output_Regulators.md](2_7_5_Power_Down_Output_Regulators.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;2.7.6 Power Down Output Regulators During Power On Sequence | 31–31 | [2_7_6_Power_Down_Output_Regulators_During_Power_On_Seque.md](2_7_6_Power_Down_Output_Regulators_During_Power_On_Seque.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;2.7.7 CAMP Signal | 31–33 | [2_7_7_CAMP_Signal.md](2_7_7_CAMP_Signal.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;2.7.8 GSI_n Signal | 33–33 | [2_7_8_GSI_n_Signal.md](2_7_8_GSI_n_Signal.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;2.7.9 State Transition Diagram | 33–35 | [2_7_9_State_Transition_Diagram.md](2_7_9_State_Transition_Diagram.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;2.7.10 Function Interrupt - CAMP and GSI_n Output Signals | 35–38 | [2_7_10_Function_Interrupt_CAMP_and_GSI_n_Output_Signals.md](2_7_10_Function_Interrupt_CAMP_and_GSI_n_Output_Signals.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;2.7.11 Input Power Good Status | 38–38 | [2_7_11_Input_Power_Good_Status.md](2_7_11_Input_Power_Good_Status.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;2.7.12 Input Over Voltage Protection | 38–39 | [2_7_12_Input_Over_Voltage_Protection.md](2_7_12_Input_Over_Voltage_Protection.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;2.7.13 Output Power Good Status | 39–40 | [2_7_13_Output_Power_Good_Status.md](2_7_13_Output_Power_Good_Status.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;2.7.14 Output Over Voltage Protection | 40–41 | [2_7_14_Output_Over_Voltage_Protection.md](2_7_14_Output_Over_Voltage_Protection.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;2.7.15 Output Under Voltage and VIN_Bulk Under Voltage Lockout Protection | 41–42 | [2_7_15_Output_Under_Voltage_and_VIN_Bulk_Under_Voltage_Lo.md](2_7_15_Output_Under_Voltage_and_VIN_Bulk_Under_Voltage_Lo.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;2.7.16 Output Current Limiter Warning Event | 42–42 | [2_7_16_Output_Current_Limiter_Warning_Event.md](2_7_16_Output_Current_Limiter_Warning_Event.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;2.7.17 Output High Current Consumption Warning Event | 42–43 | [2_7_17_Output_High_Current_Consumption_Warning_Event.md](2_7_17_Output_High_Current_Consumption_Warning_Event.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;2.7.18 PMIC LDO Output Failure | 43–43 | [2_7_18_PMIC_LDO_Output_Failure.md](2_7_18_PMIC_LDO_Output_Failure.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;2.7.19 PMIC High Temperature Warning and Critical Temperature Protection | 43–44 | [2_7_19_PMIC_High_Temperature_Warning_and_Critical_Tempera.md](2_7_19_PMIC_High_Temperature_Warning_and_Critical_Tempera.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;2.7.20 VIN_Mgmt to VIN_Bulk Input Supply Switchover Event | 44–44 | [2_7_20_VIN_Mgmt_to_VIN_Bulk_Input_Supply_Switchover_Event.md](2_7_20_VIN_Mgmt_to_VIN_Bulk_Input_Supply_Switchover_Event.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;2.7.21 Valid VIN_Mgmt Supply Detection in Switchover Mode | 44–45 | [2_7_21_Valid_VIN_Mgmt_Supply_Detection_in_Switchover_Mode.md](2_7_21_Valid_VIN_Mgmt_Supply_Detection_in_Switchover_Mode.md) |
| &nbsp;&nbsp;2.8 Analog to Digital Converter (ADC) | 45–46 | [2_8_Analog_to_Digital_Converter_ADC.md](2_8_Analog_to_Digital_Converter_ADC.md) |
| &nbsp;&nbsp;2.9 I2C and I3C Basic Interface Operation | 46–46 | [2_9_I2C_and_I3C_Basic_Interface_Operation.md](2_9_I2C_and_I3C_Basic_Interface_Operation.md) |
| &nbsp;&nbsp;2.10 Device Interface - Protocol | 46–91 | [2_10_Device_Interface_Protocol.md](2_10_Device_Interface_Protocol.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;2.10.1 Serial Address of PMIC Device | 47–47 | [2_10_1_Serial_Address_of_PMIC_Device.md](2_10_1_Serial_Address_of_PMIC_Device.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;2.10.2 Switch from I2C Mode to I3C Basic Mode | 47–47 | [2_10_2_Switch_from_I2C_Mode_to_I3C_Basic_Mode.md](2_10_2_Switch_from_I2C_Mode_to_I3C_Basic_Mode.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;2.10.3 Switch from I3C Basic Mode to I2C Mode | 47–48 | [2_10_3_Switch_from_I3C_Basic_Mode_to_I2C_Mode.md](2_10_3_Switch_from_I3C_Basic_Mode_to_I2C_Mode.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;2.10.4 I2C Target Protocol | 48–49 | [2_10_4_I2C_Target_Protocol.md](2_10_4_I2C_Target_Protocol.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;2.10.5 I3C Basic Target Protocol | 49–62 | [2_10_5_I3C_Basic_Target_Protocol.md](2_10_5_I3C_Basic_Target_Protocol.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.10.5.1 Write Operation - Data Packet | 50–52 | [2_10_5_1_Write_Operation_Data_Packet.md](2_10_5_1_Write_Operation_Data_Packet.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.10.5.2 Read Operation - Data Packet | 52–56 | [2_10_5_2_Read_Operation_Data_Packet.md](2_10_5_2_Read_Operation_Data_Packet.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.10.5.3 Default Read Address Pointer Mode | 56–62 | [2_10_5_3_Default_Read_Address_Pointer_Mode.md](2_10_5_3_Default_Read_Address_Pointer_Mode.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;2.10.6 In Band Interrupt (IBI) | 62–67 | [2_10_6_In_Band_Interrupt_IBI.md](2_10_6_In_Band_Interrupt_IBI.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;2.10.7 Packet Error Check (PEC) Function | 67–67 | [2_10_7_Packet_Error_Check_PEC_Function.md](2_10_7_Packet_Error_Check_PEC_Function.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;2.10.8 Parity Error Check Function | 67–67 | [2_10_8_Parity_Error_Check_Function.md](2_10_8_Parity_Error_Check_Function.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;2.10.9 Packet Error Check and Parity Error Handling | 67–72 | [2_10_9_Packet_Error_Check_and_Parity_Error_Handling.md](2_10_9_Packet_Error_Check_and_Parity_Error_Handling.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;2.10.10 CCC Packet Error Handling | 72–72 | [2_10_10_CCC_Packet_Error_Handling.md](2_10_10_CCC_Packet_Error_Handling.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;2.10.11 Error Reporting | 72–72 | [2_10_11_Error_Reporting.md](2_10_11_Error_Reporting.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;2.10.12 I3C Basic Common Command Codes (CCC) | 72–87 | [2_10_12_I3C_Basic_Common_Command_Codes_CCC.md](2_10_12_I3C_Basic_Common_Command_Codes_CCC.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.10.12.1 ENEC CCC | 73–75 | [2_10_12_1_ENEC_CCC.md](2_10_12_1_ENEC_CCC.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.10.12.2 DISEC CCC | 75–76 | [2_10_12_2_DISEC_CCC.md](2_10_12_2_DISEC_CCC.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.10.12.3 RSTDAA CCC | 76–77 | [2_10_12_3_RSTDAA_CCC.md](2_10_12_3_RSTDAA_CCC.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.10.12.4 SETAASA CCC | 77–77 | [2_10_12_4_SETAASA_CCC.md](2_10_12_4_SETAASA_CCC.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.10.12.5 GETSTATUS CCC | 77–79 | [2_10_12_5_GETSTATUS_CCC.md](2_10_12_5_GETSTATUS_CCC.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.10.12.6 DEVCAP CCC | 79–80 | [2_10_12_6_DEVCAP_CCC.md](2_10_12_6_DEVCAP_CCC.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.10.12.8 DEVCTRL CCC | 80–87 | [2_10_12_8_DEVCTRL_CCC.md](2_10_12_8_DEVCTRL_CCC.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.10.12.8.1 DEVCTRL CCC Examples - RegMod = ‘0’ | 84–86 | [2_10_12_8_1_DEVCTRL_CCC_Examples_RegMod_0.md](2_10_12_8_1_DEVCTRL_CCC_Examples_RegMod_0.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.10.12.8.2 DEVCTRL CCC Examples - RegMod = ‘1’ | 86–87 | [2_10_12_8_2_DEVCTRL_CCC_Examples_RegMod_1.md](2_10_12_8_2_DEVCTRL_CCC_Examples_RegMod_1.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;2.10.13 IO Operation | 87–88 | [2_10_13_IO_Operation.md](2_10_13_IO_Operation.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;2.10.14 Bus Clear | 88–89 | [2_10_14_Bus_Clear.md](2_10_14_Bus_Clear.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;2.10.15 Bus Reset | 89–90 | [2_10_15_Bus_Reset.md](2_10_15_Bus_Reset.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;2.10.16 Command Truth Table | 90–91 | [2_10_16_Command_Truth_Table.md](2_10_16_Command_Truth_Table.md) |
| &nbsp;&nbsp;2.11 Device Package and Pinout | 91–99 | [2_11_Device_Package_and_Pinout.md](2_11_Device_Package_and_Pinout.md) |
| &nbsp;&nbsp;2.12 Inductor Specification | 99–100 | [2_12_Inductor_Specification.md](2_12_Inductor_Specification.md) |
| &nbsp;&nbsp;2.13 Application Notes | 100–102 | [2_13_Application_Notes.md](2_13_Application_Notes.md) |
| 3 Registers Space | 102–191 | [3_Registers_Space.md](3_Registers_Space.md) |
| &nbsp;&nbsp;3.1 Register Attribute Definition | 102–103 | [3_1_Register_Attribute_Definition.md](3_1_Register_Attribute_Definition.md) |
| &nbsp;&nbsp;3.2 Register Map Breakdown | 103–103 | [3_2_Register_Map_Breakdown.md](3_2_Register_Map_Breakdown.md) |
| &nbsp;&nbsp;3.3 Register Memory Protection | 103–191 | [3_3_Register_Memory_Protection.md](3_3_Register_Memory_Protection.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;3.3.1 Steps to Access DIMM Vendor Region Registers | 103–104 | [3_3_1_Steps_to_Access_DIMM_Vendor_Region_Registers.md](3_3_1_Steps_to_Access_DIMM_Vendor_Region_Registers.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;3.3.2 Steps to Change DIMM Vendor Region Password | 104–104 | [3_3_2_Steps_to_Change_DIMM_Vendor_Region_Password.md](3_3_2_Steps_to_Change_DIMM_Vendor_Region_Password.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;3.3.3 Steps to Burn or Program DIMM Vendor Region Registers | 104–105 | [3_3_3_Steps_to_Burn_or_Program_DIMM_Vendor_Region_Regist.md](3_3_3_Steps_to_Burn_or_Program_DIMM_Vendor_Region_Regist.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;3.3.4 Host Region Register Map | 105–110 | [3_3_4_Host_Region_Register_Map.md](3_3_4_Host_Region_Register_Map.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;3.3.5 Host Region Registers | 110–166 | [3_3_5_Host_Region_Registers.md](3_3_5_Host_Region_Registers.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.3.5.1 Status Registers | 110–123 | [3_3_5_1_Status_Registers.md](3_3_5_1_Status_Registers.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.3.5.2 Clear Registers | 123–128 | [3_3_5_2_Clear_Registers.md](3_3_5_2_Clear_Registers.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.3.5.3 Mask Registers | 128–134 | [3_3_5_3_Mask_Registers.md](3_3_5_3_Mask_Registers.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.3.5.4 Threshold and Configuration Registers | 134–166 | [3_3_5_4_Threshold_and_Configuration_Registers.md](3_3_5_4_Threshold_and_Configuration_Registers.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;3.3.6 DIMM Vendor Region Registers | 166–191 | [3_3_6_DIMM_Vendor_Region_Registers.md](3_3_6_DIMM_Vendor_Region_Registers.md) |
| 4 Annex A (Informative) - Differences between Revisions | 191–194 | [4_Annex_A_Informative_Differences_between_Revisions.md](4_Annex_A_Informative_Differences_between_Revisions.md) |
