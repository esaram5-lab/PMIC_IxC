# PMIC5030 Register Map Summary

Source: JESD301-5 — PMIC5030 Power Management IC Standard, Version 1.00 (January 2026). Application: server (DDR5 RDIMM, DDR5 MRDIMM, CXL modules).

Elided ranges ('...') follow the linear pattern of the neighbouring codes; see registers/<addr>.md for every value spelled out.

## R03 (0x03) — DIMM_VENDOR_REGION_MTP_ERROR_COUNT, PMIC_VENDOR_REGION_MTP_ERROR_COUNT

Region: Host Region | Source: JESD301-5 Table 108, p.135

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:4 | DIMM_VENDOR_REGION_MTP_ERROR_COUNT | RON | 0 |
| 3:0 | PMIC_VENDOR_REGION_MTP_ERROR_COUNT | RON | 0 |

### [7:4] DIMM_VENDOR_REGION_MTP_ERROR_COUNT

- Description: DIMM Vendor Region MTP Error Count[2]
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 0000 | 0x0 | 0 Error |
| 0001 | 0x1 | 1 Error |
| 0010 | 0x2 | 2 Errors |
| ... | ... | ... |
| 1111 | 0xF | > 15 Errors |

### [3:0] PMIC_VENDOR_REGION_MTP_ERROR_COUNT

- Description: PMIC Vendor Region MTP Error Count[2]
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 0000 | 0x0 | 0 Error |
| 0001 | 0x1 | 1 Error |
| 0010 | 0x2 | 2 Errors |
| ... | ... | ... |
| 1111 | 0xF | > 15 Errors |

**Notes**

- NOTE 1: The PMIC shall attempt to write this register into its non-volatile memory. However, it may not be guaranteed depending on how fast the host may shut off the input power to the PMIC. The PMIC needs minimum of 4.0 V for VIN_Bulk voltage and 200 ms duration from CAMP signal assertion to guarantee the write operation into non-volatile memory.
- NOTE 2: See Clause 6.30 for additional details.

## R04 (0x04) — GLOBAL_ERROR_COUNT, GLOBAL_ERROR_LOG_BUCK_OV_OR_UV, GLOBAL_ERROR_LOG_VIN_BULK_OVER_VOLTAGE, GLOBAL_ERROR_LOG_CRITICAL_TEMPERATURE, GLOBAL_ERROR_COUNT_EN

Region: Host Region | Source: JESD301-5 Table 109, p.136

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | GLOBAL_ERROR_COUNT | ROE | 0 |
| 6 | GLOBAL_ERROR_LOG_BUCK_OV_OR_UV | ROE | 0 |
| 5 | GLOBAL_ERROR_LOG_VIN_BULK_OVER_VOLTAGE | ROE | 0 |
| 4 | GLOBAL_ERROR_LOG_CRITICAL_TEMPERATURE | ROE | 0 |
| 3:0 | GLOBAL_ERROR_COUNT_EN | RON | 0 |

### [7] GLOBAL_ERROR_COUNT

- Description: Global Error Count Since Last Erase Operation[4]
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0 → No Error or Only 1 Error since last Erase operation

| Code (bin) | Meaning |
|---|---|
| 0 | No Error or Only 1 Error since last Erase operation |
| 1 | > 1 Error Count since last Erase operation |

### [6] GLOBAL_ERROR_LOG_BUCK_OV_OR_UV

- Description: Global Error Log History for Buck Regulator Output Over or Under Voltage
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0 → No Error Occurred

| Code (bin) | Meaning |
|---|---|
| 0 | No Error Occurred |
| 1 | Error Occurred |

### [5] GLOBAL_ERROR_LOG_VIN_BULK_OVER_VOLTAGE

- Description: Global Error Log History for VIN_Bulk Over Voltage
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0 → No Error Occurred

| Code (bin) | Meaning |
|---|---|
| 0 | No Error Occurred |
| 1 | Error Occurred |

### [4] GLOBAL_ERROR_LOG_CRITICAL_TEMPERATURE

- Description: Global Error Log History for Critical Temperature
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0 → No Error Occurred

| Code (bin) | Meaning |
|---|---|
| 0 | No Error Occurred |
| 1 | Error Occurred |

### [3:0] GLOBAL_ERROR_COUNT_EN

- Description: Global Error Count[5]
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0
- Source correction: Spec lists code 0010 for '3 Errors (See R144/145 for detailed error log)'; corrected to 0011. Duplicate code in Table 109; sequence implies 0011.
- Source correction: Codes 0100-1110 are elided ('...') in the source; filled following the listed pattern (N errors -> fault log R(0x13E+2N)/R(0x13F+2N), ending at R15C/R15D for 15).

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 0000 | 0x0 | 0 Fault |
| 0001 | 0x1 | 1 Error (See R140/R141 for detailed error log) |
| 0010 | 0x2 | 2 Errors (See R142/R143 for detailed error log) |
| 0011 | 0x3 | 3 Errors (See R144/145 for detailed error log) |
| ... | ... | ... |
| 1111 | 0xF | 15 Errors (See R15C/R15D for detailed error log) Errors beyond 15 are not captured. |

**Notes**

- NOTE 1: The PMIC shall attempt to write this register into its non-volatile memory. However, it may not be guaranteed depending on how fast the host may shut off the input power to the PMIC. The PMIC needs minimum of 4.0 V for VIN_Bulk voltage and 200 ms duration from CAMP signal assertion to guarantee the write operation into non-volatile memory.
- NOTE 2: Host must explicitly perform Erase operation to erase the register Table 109, Register 0x04 [7:4] via Table 162, Register 0x39 command. The PMIC needs minimum of 200 ms for Erase operation. Note that Table 109, Register 0x04 [3:0] are not erasable by the command.
- NOTE 3: The error log registers are only updated when there is a VR Disable fault when the buck regulators are under regulation. For any external command registered by the PMIC from the host (i.e., VR Disable command or CAMP assertion), followed by VIN_Bulk input supply removal to the PMIC, the PMIC does not log the error log registers.
- NOTE 4: PMIC counts the error since last erase operation and if more than one error occurs, it sets this bit to ‘1’.
- NOTE 5: See clause 6.29 for additional details.

## R05 (0x05) — SWA_POWER_GOOD, SWB_POWER_GOOD, SWC_POWER_GOOD, SWD_POWER_GOOD, PMIC_ERROR_LOG

Region: Host Region | Source: JESD301-5 Table 110, p.137

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | RESERVED | RV | 0 |
| 6 | SWA_POWER_GOOD | ROE | 0 |
| 5 | SWB_POWER_GOOD | ROE | 0 |
| 4 | SWC_POWER_GOOD | ROE | 0 |
| 3 | SWD_POWER_GOOD | ROE | 0 |
| 2:0 | PMIC_ERROR_LOG | ROE | 0 |

### [7] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [6] SWA_POWER_GOOD

- Description: PMIC Power On - SWA Power Not Good[4]
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0 → Normal Power On

| Code (bin) | Meaning |
|---|---|
| 0 | Normal Power On |
| 1 | SWA Power Not Good |

### [5] SWB_POWER_GOOD

- Description: PMIC Power On - SWB Power Not Good[3],[5]
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0 → Normal Power On

| Code (bin) | Meaning |
|---|---|
| 0 | Normal Power On |
| 1 | SWB Power Not Good |

### [4] SWC_POWER_GOOD

- Description: PMIC Power On - SWC Power Not Good[3]
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0 → Normal Power On

| Code (bin) | Meaning |
|---|---|
| 0 | Normal Power On |
| 1 | SWC Power Not Good |

### [3] SWD_POWER_GOOD

- Description: PMIC Power On - SWD Power Not Good[3]
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0 → Normal Power On

| Code (bin) | Meaning |
|---|---|
| 0 | Normal Power On |
| 1 | SWD Power Not Good |

### [2:0] PMIC_ERROR_LOG

- Description: PMIC Power On - High Level Status Bit to Previous Last Known Power Cycle
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 000 | Normal Power On |
| 001 | Reserved |
| 010 | Buck Regulator Output Over or Under Voltage[6] |
| 011 | Critical Temperature |
| 100 | VIN_Bulk Input Over Voltage |
| 101 | Reserved |
| 110 | Reserved |
| 111 | VIN_Bulk_UV_OR_VBIAS_UV |

**Notes**

- NOTE 1: The PMIC shall attempt to write this register into its non-volatile memory. However, it may not be guaranteed depending on how fast the host may shut off the input power to the PMIC. The PMIC needs minimum of 4.0V for VIN_Bulk voltage and 200 ms duration from CAMP signal assertion to guarantee the write operation into non-volatile memory.
- NOTE 2: This entire register status reflects previous power down cycle of the PMIC and is updated by the PMIC on its own at each power cycle, if update is needed. Because this register is updated only if there is an update needed, there is no NVM life time impact. This register is cleared when host issues the erase command via Table 162, Register 0x39. The PMIC needs minimum of 200 ms for Erase operation.
- NOTE 3: The error log registers are only updated when there is a VR Disable fault when the buck regulators are under regulation. For any external command registered by the PMIC from the host (i.e., VR Disable command or CAMP assertion), followed by VIN_Bulk input supply removal to the PMIC, the PMIC does not log the error log registers.
- NOTE 4: This register is set only if PMIC generates internal VR Disable command due to fault condition.
- NOTE 5: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care.
- NOTE 6: This code is a logical OR function of Table 111, Register 0x06 [7:0] and Table 112, Register 0x07 [7:4] register bits.

## R06 (0x06) — SWA_UNDER_VOLTAGE_LOCKOUT, SWB_UNDER_VOLTAGE_LOCKOUT, SWC_UNDER_VOLTAGE_LOCKOUT, SWD_UNDER_VOLTAGE_LOCKOUT, SWA_OVER_VOLTAGE, SWB_OVER_VOLTAGE, SWC_OVER_VOLTAGE, SWD_OVER_VOLTAGE

Region: Host Region | Source: JESD301-5 Table 111, p.138

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | SWA_UNDER_VOLTAGE_LOCKOUT | ROE | 0 |
| 6 | SWB_UNDER_VOLTAGE_LOCKOUT | ROE | 0 |
| 5 | SWC_UNDER_VOLTAGE_LOCKOUT | ROE | 0 |
| 4 | SWD_UNDER_VOLTAGE_LOCKOUT | ROE | 0 |
| 3 | SWA_OVER_VOLTAGE | ROE | 0 |
| 2 | SWB_OVER_VOLTAGE | ROE | 0 |
| 1 | SWC_OVER_VOLTAGE | ROE | 0 |
| 0 | SWD_OVER_VOLTAGE | ROE | 0 |

### [7] SWA_UNDER_VOLTAGE_LOCKOUT

- Description: PMIC Power On - SWA Under Voltage Lockout
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0 → Normal Power On

| Code (bin) | Meaning |
|---|---|
| 0 | Normal Power On |
| 1 | SWA Under Voltage Lockout |

### [6] SWB_UNDER_VOLTAGE_LOCKOUT

- Description: PMIC Power On - SWB Under Voltage Lockout[4]
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0 → Normal Power On

| Code (bin) | Meaning |
|---|---|
| 0 | Normal Power On |
| 1 | SWB Under Voltage Lockout |

### [5] SWC_UNDER_VOLTAGE_LOCKOUT

- Description: PMIC Power On - SWC Under Voltage Lockout
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0 → Normal Power On

| Code (bin) | Meaning |
|---|---|
| 0 | Normal Power On |
| 1 | SWC Under Voltage Lockout |

### [4] SWD_UNDER_VOLTAGE_LOCKOUT

- Description: PMIC Power On - SWD Under Voltage Lockout
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0 → Normal Power On

| Code (bin) | Meaning |
|---|---|
| 0 | Normal Power On |
| 1 | SWD Under Voltage Lockout |

### [3] SWA_OVER_VOLTAGE

- Description: PMIC Power On - SWA Over Voltage
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0 → Normal Power On

| Code (bin) | Meaning |
|---|---|
| 0 | Normal Power On |
| 1 | SWA Over Voltage |

### [2] SWB_OVER_VOLTAGE

- Description: PMIC Power On - SWB Over Voltage[3]
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0 → Normal Power On

| Code (bin) | Meaning |
|---|---|
| 0 | Normal Power On |
| 1 | SWB Over Voltage |

### [1] SWC_OVER_VOLTAGE

- Description: PMIC Power On - SWC Over Voltage
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0 → Normal Power On

| Code (bin) | Meaning |
|---|---|
| 0 | Normal Power On |
| 1 | SWC Over Voltage |

### [0] SWD_OVER_VOLTAGE

- Description: PMIC Power On - SWD Over Voltage
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0 → Normal Power On

| Code (bin) | Meaning |
|---|---|
| 0 | Normal Power On |
| 1 | SWD Over Voltage |

**Notes**

- NOTE 1: The PMIC shall attempt to write this register into its non-volatile memory. However, it may not be guaranteed depending on how fast the host may shut off the input power to the PMIC. The PMIC needs minimum of 4.0V for VIN_Bulk voltage and 200 ms duration from CAMP signal assertion to guarantee the write operation into non-volatile memory.
- NOTE 2: This entire register status reflects previous power down cycle of the PMIC and is updated by the PMIC on its own at each power cycle, if update is needed. Because this register is updated only if there is an update needed, there is no NVM life time impact. This register is cleared when host issues the erase command via Table 162, Register 0x39. The PMIC needs minimum of 200 ms for Erase operation.
- NOTE 3: The error log registers are only updated when there is a VR Disable fault when the buck regulators are under regulation. For any external command registered by the PMIC from the host (i.e., VR Disable command or CAMP assertion), followed by VIN_Bulk input supply removal to the PMIC, the PMIC does not log the error log registers.
- NOTE 4: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care.

## R07 (0x07) — SWE_UNDER_VOLTAGE_LOCKOUT, SWF_UNDER_VOLTAGE_LOCKOUT, SWE_OVER_VOLTAGE, SWF_OVER_VOLTAGE, SWE_POWER_GOOD, SWF_POWER_GOOD

Region: Host Region | Source: JESD301-5 Table 112, p.139

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | SWE_UNDER_VOLTAGE_LOCKOUT | ROE | 0 |
| 6 | SWF_UNDER_VOLTAGE_LOCKOUT | ROE | 0 |
| 5 | SWE_OVER_VOLTAGE | ROE | 0 |
| 4 | SWF_OVER_VOLTAGE | ROE | 0 |
| 3:2 | RESERVED | RV | 0 |
| 1 | SWE_POWER_GOOD | ROE | 0 |
| 0 | SWF_POWER_GOOD | ROE | 0 |

### [7] SWE_UNDER_VOLTAGE_LOCKOUT

- Description: PMIC Power On - SWE Under Voltage Lockout[4]
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0 → Normal Power On

| Code (bin) | Meaning |
|---|---|
| 0 | Normal Power On |
| 1 | SWE Under Voltage Lockout |

### [6] SWF_UNDER_VOLTAGE_LOCKOUT

- Description: PMIC Power On - SWF Under Voltage Lockout[5]
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0 → Normal Power On

| Code (bin) | Meaning |
|---|---|
| 0 | Normal Power On |
| 1 | SWF Under Voltage Lockout |

### [5] SWE_OVER_VOLTAGE

- Description: PMIC Power On - SWE Over Voltage
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0 → Normal Power On

| Code (bin) | Meaning |
|---|---|
| 0 | Normal Power On |
| 1 | SWE Over Voltage |

### [4] SWF_OVER_VOLTAGE

- Description: PMIC Power On - SWF Over Voltage
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0 → Normal Power On

| Code (bin) | Meaning |
|---|---|
| 0 | Normal Power On |
| 1 | SWF Over Voltage |

### [3:2] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [1] SWE_POWER_GOOD

- Description: PMIC Power On - SWE Power Not Good[3]
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0 → Normal Power On

| Code (bin) | Meaning |
|---|---|
| 0 | Normal Power On |
| 1 | SWE Power Not Good |

### [0] SWF_POWER_GOOD

- Description: PMIC Power On - SWF Power Not Good[4]
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0 → Normal Power On

| Code (bin) | Meaning |
|---|---|
| 0 | Normal Power On |
| 1 | SWF Power Not Good |

**Notes**

- NOTE 1: The PMIC shall attempt to write this register into its non-volatile memory. However, it may not be guaranteed depending on how fast the host may shut off the input power to the PMIC. The PMIC needs minimum of 4.0V for VIN_Bulk voltage and 200 ms duration from CAMP signal assertion to guarantee the write operation into non-volatile memory.
- NOTE 2: This entire register status reflects previous power down cycle of the PMIC and is updated by the PMIC on its own at each power cycle, if update is needed. Because this register is updated only if there is an update needed, there is no NVM life time impact. This register is cleared when host issues the erase command via Table 162, Register 0x39. The PMIC needs minimum of 200 ms for Erase operation.
- NOTE 3: The error log registers are only updated when there is a VR Disable fault when the buck regulators are under regulation. For any external command registered by the PMIC from the host (i.e., VR Disable command or CAMP assertion), followed by VIN_Bulk input supply removal to the PMIC, the PMIC does not log the error log registers.
- NOTE 4: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care.
- NOTE 5: This register is only applicable if Table 247, Register 0x4F [6] = ‘0’. For any other setting in Table 247, Register 0x4F [6], this register does not apply and it is a don’t care.

## R08 (0x08) — VIN_BULK_INPUT_POWER_GOOD_STATUS, CRITICAL_TEMP_SHUTDOWN_STATUS, SWA_OUTPUT_POWER_GOOD_STATUS, SWB_OUTPUT_POWER_GOOD_STATUS, SWC_OUTPUT_POWER_GOOD_STATUS, SWD_OUTPUT_POWER_GOOD_STATUS, VIN_MGMT_INPUT_OVER_VOLTAGE_STATUS, VIN_BULK_INPUT_OVER_VOLTAGE_STATUS

Region: Host Region | Source: JESD301-5 Table 113, p.140

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | VIN_BULK_INPUT_POWER_GOOD_STATUS | RO | 0 |
| 6 | CRITICAL_TEMP_SHUTDOWN_STATUS | RO | 0 |
| 5 | SWA_OUTPUT_POWER_GOOD_STATUS | RO | 0 |
| 4 | SWB_OUTPUT_POWER_GOOD_STATUS | RO | 0 |
| 3 | SWC_OUTPUT_POWER_GOOD_STATUS | RO | 0 |
| 2 | SWD_OUTPUT_POWER_GOOD_STATUS | RO | 0 |
| 1 | VIN_MGMT_INPUT_OVER_VOLTAGE_STATUS | RO | 0 |
| 0 | VIN_BULK_INPUT_OVER_VOLTAGE_STATUS | RO | 0 |

### [7] VIN_BULK_INPUT_POWER_GOOD_STATUS

- Description: VIN_Bulk Input Power Good Status[1]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → Power Good

| Code (bin) | Meaning |
|---|---|
| 0 | Power Good |
| 1 | Power Not Good |

### [6] CRITICAL_TEMP_SHUTDOWN_STATUS

- Description: Critical Temperature Shutdown Status[2]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No Critical Temperature Shutdown

| Code (bin) | Meaning |
|---|---|
| 0 | No Critical Temperature Shutdown |
| 1 | Critical Temperature Shutdown |

### [5] SWA_OUTPUT_POWER_GOOD_STATUS

- Description: Switch Node A Output Power Good Status[3]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → Power Good

| Code (bin) | Meaning |
|---|---|
| 0 | Power Good |
| 1 | Power Not Good |

### [4] SWB_OUTPUT_POWER_GOOD_STATUS

- Description: Switch Node B Output Power Good Status[4]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → Power Good

| Code (bin) | Meaning |
|---|---|
| 0 | Power Good |
| 1 | Power Not Good |

### [3] SWC_OUTPUT_POWER_GOOD_STATUS

- Description: Switch Node C Output Power Good Status[5]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → Power Good

| Code (bin) | Meaning |
|---|---|
| 0 | Power Good |
| 1 | Power Not Good |

### [2] SWD_OUTPUT_POWER_GOOD_STATUS

- Description: Switch Node D Output Power Good Status[6]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → Power Good

| Code (bin) | Meaning |
|---|---|
| 0 | Power Good |
| 1 | Power Not Good |

### [1] VIN_MGMT_INPUT_OVER_VOLTAGE_STATUS

- Description: VIN_Mgmt Input Supply Over Voltage Status[7]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No Over Voltage

| Code (bin) | Meaning |
|---|---|
| 0 | No Over Voltage |
| 1 | Over Voltage |

### [0] VIN_BULK_INPUT_OVER_VOLTAGE_STATUS

- Description: VIN_Bulk Input Supply Over Voltage Status[8]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No Over Voltage

| Code (bin) | Meaning |
|---|---|
| 0 | No Over Voltage |
| 1 | Over Voltage |

**Notes**

- NOTE 1: This register is set when VIN_Bulk input goes below the threshold setting in register Table 131, Register 0x1A [7:5].
- NOTE 2: This register is set when PMIC temperature goes above the threshold setting in register Table 151, Register 0x2E [2:0].
- NOTE 3: This register is set when SWA output voltage goes either below the threshold setting in register Table 138, Register 0x21[1:0] or above the threshold setting in register Table 139, Register 0x22 [7:6].
- NOTE 4: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care. This register is set when SWB output goes either below the threshold setting in register Table 140, Register 0x23[1:0] or above the threshold setting in register Table 141, Register 0x24 [7:6].
- NOTE 5: This register is set when SWC output goes either below the threshold setting in register Table 142, Register 0x25[1:0] or above the threshold setting in register Table 143, Register 0x26 [7:6].
- NOTE 6: This register is set when SWD output goes either below the threshold setting in register Table 144, Register 0x27[1:0] or above the threshold setting in register Table 145, Register 0x28 [7:6].
- NOTE 7: This register is set when VIN_Mgmt input voltage goes above the threshold setting in register Table 132, Register 0x1B [5].
- NOTE 8: This register is set when VIN_Bulk input voltage goes above the threshold setting in register Table 132, Register 0x1B [7].

## R09 (0x09) — PMIC_HIGH_TEMP_WARNING_STATUS, VBIAS_POWER_GOOD_STATUS, VOUT_1.8V_OUTPUT_POWER_GOOD_STATUS, VIN_MGMT_TO_VIN_BULK_INPUT_SUPPLY_SWITCHOVER_STATUS, SWA_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS, SWB_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS, SWC_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS, SWD_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS

Region: Host Region | Source: JESD301-5 Table 114, p.141

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | PMIC_HIGH_TEMP_WARNING_STATUS | RO | 0 |
| 6 | VBIAS_POWER_GOOD_STATUS | RO | 0 |
| 5 | VOUT_1.8V_OUTPUT_POWER_GOOD_STATUS | RO | 0 |
| 4 | VIN_MGMT_TO_VIN_BULK_INPUT_SUPPLY_SWITCHOVER_STATUS | RO | 0 |
| 3 | SWA_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS | RO | 0 |
| 2 | SWB_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS | RO | 0 |
| 1 | SWC_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS | RO | 0 |
| 0 | SWD_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS | RO | 0 |

### [7] PMIC_HIGH_TEMP_WARNING_STATUS

- Description: PMIC High Temperature Warning Status[1]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → Temperature Below the Warning Threshold

| Code (bin) | Meaning |
|---|---|
| 0 | Temperature Below the Warning Threshold |
| 1 | Temperature Exceeded the Warning Threshold |

### [6] VBIAS_POWER_GOOD_STATUS

- Description: VBIAS1 or VBIAS2 Power Good Status[2]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → Power Good

| Code (bin) | Meaning |
|---|---|
| 0 | Power Good |
| 1 | Power Not Good |

### [5] VOUT_1.8V_OUTPUT_POWER_GOOD_STATUS

- Description: VOUT_1.8V LDO Output Power Good Status[3]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → Power Good

| Code (bin) | Meaning |
|---|---|
| 0 | Power Good |
| 1 | Power Not Good |

### [4] VIN_MGMT_TO_VIN_BULK_INPUT_SUPPLY_SWITCHOVER_STATUS

- Description: VIN_Mgmt to VIN_Bulk Input Supply Automatic Switchover Status[4]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → VIN_Mgmt Input Supply is Present

| Code (bin) | Meaning |
|---|---|
| 0 | VIN_Mgmt Input Supply is Present |
| 1 | VIN_Mgmt Input Supply is Removed (i.e., using VIN_Bulk Input Supply) |

### [3] SWA_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS

- Description: Switch Node A High Output Current Consumption Warning Status[5]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No High Current Consumption Warning

| Code (bin) | Meaning |
|---|---|
| 0 | No High Current Consumption Warning |
| 1 | High Current Consumption Warning |

### [2] SWB_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS

- Description: Switch Node B High Output Current Consumption Warning Status[6],[7]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No High Current Consumption Warning

| Code (bin) | Meaning |
|---|---|
| 0 | No High Current Consumption Warning |
| 1 | High Current Consumption Warning |

### [1] SWC_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS

- Description: Switch Node C High Output Current Consumption Warning Status[8]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No High Current Consumption Warning

| Code (bin) | Meaning |
|---|---|
| 0 | No High Current Consumption Warning |
| 1 | High Current Consumption Warning |

### [0] SWD_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS

- Description: Switch Node D High Output Current Consumption Warning Status[9]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No High Current Consumption Warning

| Code (bin) | Meaning |
|---|---|
| 0 | No High Current Consumption Warning |
| 1 | High Current Consumption Warning |

**Notes**

- NOTE 1: This register is set when PMIC temperature goes above the threshold setting in Table 132, Register 0x1B [2:0].
- NOTE 2: This register is set when either VBias1 or VBias2 (depending on PMIC implementation) voltage goes below the threshold setting in register Table 131, Register 0x1A [3].
- NOTE 3: This register is set when VOUT_1.8V output goes below the threshold setting in register Table 131, Register 0x1A [2].
- NOTE 4: This register is set when VIN_Mgmt input supply goes below the threshold setting in register Table 152, Register 0x2F [7].
- NOTE 5: This register is set when SWA output current consumption goes above the threshold setting in Table 133, Register 0x1C [7:0].
- NOTE 6: This register is applicable regardless of the setting in Table 247, Register 0x4F [5,0].
- NOTE 7: This register is set when SWB output current consumption goes above the threshold setting in Table 134, Register 0x1D [7:0]. If Table 247, Register 0x4F [5,0] = ‘01’, the setting in Table 134, Register 0x1D [7:0] and Table 133, Register 0x1C [7:0] must be configured identical. If Table 247, Register 0x4F [5,0] = ‘1x’, the setting in Table 134, Register 0x1D [7:0], Table 133, Register 0x1C [7:0] and Table 182, Register 0x11A [7:0] must be configured identical.
- NOTE 8: This register is set when SWC output current consumption goes above the threshold setting in Table 135, Register 0x1E [7:0]. If Table 247, Register 0x4F [6] = ‘1’, the setting in Table 135, Register 0x1E [7:0] and Table 183, Register 0x11B [7:0] must be configured identical.
- NOTE 9: This register is set when SWD output current consumption goes above the threshold setting in Table 136, Register 0x1F [7:0].

## R0A (0x0A) — SWA_OUTPUT_OVER_VOLTAGE_STATUS, SWB_OUTPUT_OVER_VOLTAGE_STATUS, SWC_OUTPUT_OVER_VOLTAGE_STATUS, SWD_OUTPUT_OVER_VOLTAGE_STATUS, PEC_ERROR_STATUS, PARITY_ERROR_STATUS, IBI_AND_GLOBAL_STATUS

Region: Host Region | Source: JESD301-5 Table 115, p.142

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | SWA_OUTPUT_OVER_VOLTAGE_STATUS | RO | 0 |
| 6 | SWB_OUTPUT_OVER_VOLTAGE_STATUS | RO | 0 |
| 5 | SWC_OUTPUT_OVER_VOLTAGE_STATUS | RO | 0 |
| 4 | SWD_OUTPUT_OVER_VOLTAGE_STATUS | RO | 0 |
| 3 | PEC_ERROR_STATUS | RO | 0 |
| 2 | PARITY_ERROR_STATUS | RO | 0 |
| 1 | IBI_AND_GLOBAL_STATUS | RO | 0 |
| 0 | RESERVED | RV | 0 |

### [7] SWA_OUTPUT_OVER_VOLTAGE_STATUS

- Description: Switch Node A Output Over Voltage Status[1]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No Over Voltage

| Code (bin) | Meaning |
|---|---|
| 0 | No Over Voltage |
| 1 | Over Voltage |

### [6] SWB_OUTPUT_OVER_VOLTAGE_STATUS

- Description: Switch Node B Output Over Voltage Status[2]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No Over Voltage

| Code (bin) | Meaning |
|---|---|
| 0 | No Over Voltage |
| 1 | Over Voltage |

### [5] SWC_OUTPUT_OVER_VOLTAGE_STATUS

- Description: Switch Node C Output Over Voltage Status[3]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No Over Voltage

| Code (bin) | Meaning |
|---|---|
| 0 | No Over Voltage |
| 1 | Over Voltage |

### [4] SWD_OUTPUT_OVER_VOLTAGE_STATUS

- Description: Switch Node D Output Over Voltage Status[4]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No Over Voltage

| Code (bin) | Meaning |
|---|---|
| 0 | No Over Voltage |
| 1 | Over Voltage |

### [3] PEC_ERROR_STATUS

- Description: Packet Error Code Status[5],[6]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No PEC Error

| Code (bin) | Meaning |
|---|---|
| 0 | No PEC Error |
| 1 | PEC Error |

### [2] PARITY_ERROR_STATUS

- Description: T Bit Parity Error Status[5],[7]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No Parity Error

| Code (bin) | Meaning |
|---|---|
| 0 | No Parity Error |
| 1 | Parity Error |

### [1] IBI_AND_GLOBAL_STATUS

- Description: In Band Interrupt and Global Status[8]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No Pending IBI or Outstanding Status

| Code (bin) | Meaning |
|---|---|
| 0 | No Pending IBI or Outstanding Status |
| 1 | Pending IBI or Outstanding Status |

### [0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

**Notes**

- NOTE 1: This register is set when SWA output voltage goes above the threshold setting in Table 139, Register 0x22 [5:4].
- NOTE 2: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care. This register is set when SWB output voltage goes above the threshold setting in Table 141, Register 0x24 [5:4].
- NOTE 3: This register is set when SWC output voltage goes above the threshold setting in Table 143, Register 0x26 [5:4].
- NOTE 4: This register is set when SWD output voltage goes above the threshold setting in Table 145, Register 0x28 [5:4]
- NOTE 5: Applicable in I3C Basic Mode Only and if enabled in register Table 158, Register 0x34 [7].
- NOTE 6: This register is updated when PMIC device goes through bus reset as described in clause 7.8.
- NOTE 7: Applicable in I3C Basic Mode and if enabled in register Table 158, Register 0x34 [5]. Also applicable in I2C mode for supported CCC.
- NOTE 8: This register can be used as Global Status in addition to IBI status. When IBI function is enabled, this register is automatically cleared when PMIC transmits IBI payload; however individual status registers still require an explicit clear command from host.

## R0B (0x0B) — SWA_OUTPUT_CURRENT_LIMITER_WARNING_STATUS, SWB_OUTPUT_CURRENT_LIMITER_WARNING_STATUS, SWC_OUTPUT_CURRENT_LIMITER_WARNING_STATUS, SWD_OUTPUT_CURRENT_LIMITER_WARNING_STATUS, SWA_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS, SWB_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS, SWC_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS, SWD_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

Region: Host Region | Source: JESD301-5 Table 116, p.143

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | SWA_OUTPUT_CURRENT_LIMITER_WARNING_STATUS | RO | 0 |
| 6 | SWB_OUTPUT_CURRENT_LIMITER_WARNING_STATUS | RO | 0 |
| 5 | SWC_OUTPUT_CURRENT_LIMITER_WARNING_STATUS | RO | 0 |
| 4 | SWD_OUTPUT_CURRENT_LIMITER_WARNING_STATUS | RO | 0 |
| 3 | SWA_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS | RO | 0 |
| 2 | SWB_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS | RO | 0 |
| 1 | SWC_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS | RO | 0 |
| 0 | SWD_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS | RO | 0 |

### [7] SWA_OUTPUT_CURRENT_LIMITER_WARNING_STATUS

- Description: Switch Node A Output Current Limiter Warning Status[1]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No Current Limiter Event

| Code (bin) | Meaning |
|---|---|
| 0 | No Current Limiter Event |
| 1 | Current Limiter Event |

### [6] SWB_OUTPUT_CURRENT_LIMITER_WARNING_STATUS

- Description: Switch Node B Output Current Limiter Warning Status[2]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No Current Limiter Event

| Code (bin) | Meaning |
|---|---|
| 0 | No Current Limiter Event |
| 1 | Current Limiter Event |

### [5] SWC_OUTPUT_CURRENT_LIMITER_WARNING_STATUS

- Description: Switch Node C Output Current Limiter Warning Status
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No Current Limiter Event

| Code (bin) | Meaning |
|---|---|
| 0 | No Current Limiter Event |
| 1 | Current Limiter Event |

### [4] SWD_OUTPUT_CURRENT_LIMITER_WARNING_STATUS

- Description: Switch Node D Output Current Limiter Warning Status[3]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No Current Limiter Event

| Code (bin) | Meaning |
|---|---|
| 0 | No Current Limiter Event |
| 1 | Current Limiter Event |

### [3] SWA_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

- Description: Switch Node A Output Under Voltage Lockout Status[4]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No Under Voltage Lockout

| Code (bin) | Meaning |
|---|---|
| 0 | No Under Voltage Lockout |
| 1 | Under Voltage Lockout |

### [2] SWB_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

- Description: Switch Node B Output Under Voltage Lockout Status[5]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No Under Voltage Lockout

| Code (bin) | Meaning |
|---|---|
| 0 | No Under Voltage Lockout |
| 1 | Under Voltage Lockout |

### [1] SWC_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

- Description: Switch Node C Output Under Voltage Lockout Status
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No Under Voltage Lockout

| Code (bin) | Meaning |
|---|---|
| 0 | No Under Voltage Lockout |
| 1 | Under Voltage Lockout |

### [0] SWD_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

- Description: Switch Node D Output Under Voltage Lockout Status[6]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No Under Voltage Lockout

| Code (bin) | Meaning |
|---|---|
| 0 | No Under Voltage Lockout |
| 1 | Under Voltage Lockout |

**Notes**

- NOTE 1: This register is set when SWA output current goes above the threshold setting in Table 137, Register 0x20 [7:6].
- NOTE 2: This register is applicable regardless of the setting in Table 247, Register 0x4F [5,0]. This register is set when SWB output current goes above the threshold setting in Table 137, Register 0x20 [5:4]. If Table 247, Register 0x4F [5,0] = ‘01’, the setting in Table 137, Register 0x20 [5:4] must be identical as Table 137, Register 0x20 [7:6]. If Table 247, Register 0x4F [5,0] = ‘1x’, the setting in Table 137, Register 0x20 [5:4], Table 137, Register 0x20 [7:6] and Table 184, Register 0x11C [7:6] must be configured identical.
- NOTE 3: This register is set when SWD output current goes above the threshold setting in Table 137, Register 0x20 [1:0].
- NOTE 4: This register is set when SWA output voltage goes below the threshold setting in Table 139, Register 0x22 [3:2].
- NOTE 5: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care. This register is set when SWB output voltage goes below the threshold setting in Table 141, Register 0x24 [3:2].
- NOTE 6: This register is set when SWD output voltage goes below the threshold setting in Table 145, Register 0x28 [3:2].

## R0C (0x0C) — SWA_OUTPUT_CURRENT_POWER_MEASUREMENT

Region: Host Region | Source: JESD301-5 Table 117, p.144

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SWA_OUTPUT_CURRENT_POWER_MEASUREMENT | RO | - |

### [7:0] SWA_OUTPUT_CURRENT_POWER_MEASUREMENT

- Description: Switch Node A Output Current or Output Power[3] Measurement[4]
- Attribute: RO — Read Only (writes have no effect)
- Default: -

**When: If Table 131, Register 0x1A[1] = ‘0’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | 125 mA or 125 mW |
| 00000010 | 0x02 | 250 mA or 250 mW |
| ... | ... | ... |
| 11111111 | 0xFF | > 31.875 A or 31.875 W |

**When: If Table 131, Register 0x1A[1] = ‘1’ — Sum of SWA, SWB, SWC and SWD Output Power[5]**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | 125 mW |
| 00000010 | 0x02 | 250 mW |
| ... | ... | ... |
| 11111111 | 0xFF | > 31.875 W |

**Notes**

- NOTE 1: This register is only applicable if Table 155, Register 0x32 [1:0] = ‘00’
- NOTE 2: The PMIC reports current or power measurement as long as there is no output over voltage or output under voltage lockout event that triggers the VR Disable command. If PMIC triggers VR Disable command, PMIC does not report current or power measurement and register content may have stale data. For all other events that causes PMIC’s power good status as Not Good, the PMIC continues to provide current or power measurement.
- NOTE 3: If Table 132, Register 0x1B [6] = ‘0’, the PMIC reports current measurement. If Table 132, Register 0x1B [6] = ‘1’, the PMIC reports power measurement.
- NOTE 4: If Table 247, Register 0x4F [5,0] = ‘01’, host adds the current or power reported in Table 117, Register 0x0C [7:0] and Table 118, Register 0x0D [7:0] for total current or power consumption. If Table 247, Register 0x4F [5,0] = ‘1x’, this register does not apply; the host shall set Table 155, Register 0x32 [1:0] = ‘01’ and read from registers Table 167, Register 0x100 to Table 174, Register 0x107.
- NOTE 5: Register Table 132, Register 0x1B [6] must be configured as ‘1’.

## R0D (0x0D) — SWB_OUTPUT_CURRENT_POWER_MEASUREMENT

Region: Host Region | Source: JESD301-5 Table 118, p.145

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SWB_OUTPUT_CURRENT_POWER_MEASUREMENT | RO | - |

### [7:0] SWB_OUTPUT_CURRENT_POWER_MEASUREMENT

- Description: Switch Node B Output Current or Output Power[3] Measurement[4]
- Attribute: RO — Read Only (writes have no effect)
- Default: -

**When: If Table 131, Register 0x1A[1] = ‘0’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | 125 mA or 125 mW |
| 00000010 | 0x02 | 250 mA or 250 mW |
| ... | ... | ... |
| 11111111 | 0xFF | > 31.875 A or 31.875 W |

**Notes**

- NOTE 1: This register is only applicable if Table 155, Register 0x32 [1:0] = ‘00’
- NOTE 2: The PMIC reports current or power measurement as long as there is no output over voltage or output under voltage lockout event that triggers the VR Disable command. If PMIC triggers VR Disable command, PMIC does not report current or power measurement and register content may have stale data. For all other events that causes PMIC’s power good status as Not Good, the PMIC continues to provide current or power measurement.
- NOTE 3: If Table 132, Register 0x1B [6] = ‘0’, the PMIC reports current measurement. If Table 132, Register 0x1B [6] = ‘1’, the PMIC reports power measurement.
- NOTE 4: If Table 247, Register 0x4F [5,0] = ‘01’, host adds the current or power reported in Table 117, Register 0x0C [7:0] and Table 118, Register 0x0D [7:0] for total current or power consumption. If Table 247, Register 0x4F [5,0] = ‘1x’, this register does not apply; the host shall set Table 155, Register 0x32 [1:0] = ‘01’ and read from registers Table 167, Register 0x100 to Table 174, Register 0x107.

## R0E (0x0E) — SWC_OUTPUT_CURRENT_POWER_MEASUREMENT

Region: Host Region | Source: JESD301-5 Table 119, p.145

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SWC_OUTPUT_CURRENT_POWER_MEASUREMENT | RO | - |

### [7:0] SWC_OUTPUT_CURRENT_POWER_MEASUREMENT

- Description: Switch Node C Output Current or Output Power[3] Measurement[4]
- Attribute: RO — Read Only (writes have no effect)
- Default: -

**When: If Table 131, Register 0x1A[1] = ‘0’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | 125 mA or 125 mW |
| 00000010 | 0x02 | 250 mA or 250 mW |
| ... | ... | ... |
| 11111111 | 0xFF | > 31.875 A or 31.875 W |

**Notes**

- NOTE 1: This register is only applicable if Table 155, Register 0x32 [1:0] = ‘00’
- NOTE 2: The PMIC reports current or power measurement as long as there is no output over voltage or output under voltage lockout event that triggers the VR Disable command. If PMIC triggers VR Disable command, PMIC does not report current or power measurement and register content may have stale data. For all other events that causes PMIC’s power good status as Not Good, the PMIC continues to provide current or power measurement.
- NOTE 3: If Table 132, Register 0x1B [6] = ‘0’, the PMIC reports current measurement. If Table 132, Register 0x1B [6] = ‘1’, the PMIC reports power measurement.
- NOTE 4: If Table 247, Register 0x4F [6] = ‘1’, this register does not apply; the host shall set Table 155, Register 0x32 [1:0] = ‘01’ and read from registers Table 167, Register 0x100 to Table 174, Register 0x107.

## R0F (0x0F) — SWD_OUTPUT_CURRENT_POWER_MEASUREMENT

Region: Host Region | Source: JESD301-5 Table 120, p.146

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SWD_OUTPUT_CURRENT_POWER_MEASUREMENT | RO | - |

### [7:0] SWD_OUTPUT_CURRENT_POWER_MEASUREMENT

- Description: Switch Node D Output Current or Output Power[3] Measurement
- Attribute: RO — Read Only (writes have no effect)
- Default: -

**When: If Table 131, Register 0x1A[1] = ‘0’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | 125 mA or 125 mW |
| 00000010 | 0x02 | 250 mA or 250 mW |
| ... | ... | ... |
| 11111111 | 0xFF | > 31.875 A or 31.875 W |

**Notes**

- NOTE 1: This register is only applicable if Table 155, Register 0x32 [1:0] = ‘00’
- NOTE 2: The PMIC reports current or power measurement as long as there is no output over voltage or output under voltage lockout event that triggers the VR Disable command. If PMIC triggers VR Disable command, PMIC does not report current or power measurement and register content may have stale data. For all other events that causes PMIC’s power good status as Not Good, the PMIC continues to provide current or power measurement.
- NOTE 3: If Table 132, Register 0x1B [6] = ‘0’, the PMIC reports current measurement. If Table 132, Register 0x1B [6] = ‘1’, the PMIC reports power measurement.

## R10 (0x10) — CLEAR_VIN_BULK_INPUT_POWER_GOOD_STATUS, CLEAR_SWA_OUTPUT_POWER_GOOD_STATUS, CLEAR_SWB_OUTPUT_POWER_GOOD_STATUS, CLEAR_SWC_OUTPUT_POWER_GOOD_STATUS, CLEAR_SWD_OUTPUT_POWER_GOOD_STATUS, CLEAR_VIN_MGMT_INPUT_OVER_VOLTAGE_STATUS, CLEAR_VIN_BULK_INPUT_OVER_VOLTAGE_STATUS

Region: Host Region | Source: JESD301-5 Table 121, p.147

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | CLEAR_VIN_BULK_INPUT_POWER_GOOD_STATUS | 1O | 0 |
| 6 | RESERVED | RV | 0 |
| 5 | CLEAR_SWA_OUTPUT_POWER_GOOD_STATUS | 1O | 0 |
| 4 | CLEAR_SWB_OUTPUT_POWER_GOOD_STATUS | 1O | 0 |
| 3 | CLEAR_SWC_OUTPUT_POWER_GOOD_STATUS | 1O | 0 |
| 2 | CLEAR_SWD_OUTPUT_POWER_GOOD_STATUS | 1O | 0 |
| 1 | CLEAR_VIN_MGMT_INPUT_OVER_VOLTAGE_STATUS | 1O | 0 |
| 0 | CLEAR_VIN_BULK_INPUT_OVER_VOLTAGE_STATUS | 1O | 0 |

### [7] CLEAR_VIN_BULK_INPUT_POWER_GOOD_STATUS

- Description: Clear VIN_Bulk Input Power Good Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 113, Register 0x08 [7][2] |

### [6] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [5] CLEAR_SWA_OUTPUT_POWER_GOOD_STATUS

- Description: Clear SWA Output Power Good Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 113, Register 0x08 [5][2] |

### [4] CLEAR_SWB_OUTPUT_POWER_GOOD_STATUS

- Description: Clear SWB Output Power Good Status.[3]
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 113, Register 0x08 [4][2] |

### [3] CLEAR_SWC_OUTPUT_POWER_GOOD_STATUS

- Description: Clear SWC Output Power Good Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 113, Register 0x08 [3][2] |

### [2] CLEAR_SWD_OUTPUT_POWER_GOOD_STATUS

- Description: Clear SWD Output Power Good Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 113, Register 0x08 [2][2] |

### [1] CLEAR_VIN_MGMT_INPUT_OVER_VOLTAGE_STATUS

- Description: Clear VIN_Mgmt Input Supply Over Voltage Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 113, Register 0x08 [1][2] |

### [0] CLEAR_VIN_BULK_INPUT_OVER_VOLTAGE_STATUS

- Description: Clear VIN_Bulk Input Supply Over Voltage Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 113, Register 0x08 [0][2] |

**Notes**

- NOTE 1: Table 121, Register 0x10 [7:0] bits are self-clearing.
- NOTE 2: See Table 28 and Table 29 for GSI_n and POWER_GOOD output signal status change.
- NOTE 3: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care.

## R11 (0x11) — CLEAR_PMIC_HIGH_TEMP_WARNING_STATUS, CLEAR_VBIAS_POWER_GOOD_STATUS, CLEAR_VOUT_1.8V_OUTPUT_POWER_GOOD_STATUS, CLEAR_VIN_MGMT_TO_VIN_BULK_INPUT_SWITCHOVER_STATUS, CLEAR_SWA_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS, CLEAR_SWB_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS, CLEAR_SWC_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS, CLEAR_SWD_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS

Region: Host Region | Source: JESD301-5 Table 122, p.148

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | CLEAR_PMIC_HIGH_TEMP_WARNING_STATUS | 1O | 0 |
| 6 | CLEAR_VBIAS_POWER_GOOD_STATUS | 1O | 0 |
| 5 | CLEAR_VOUT_1.8V_OUTPUT_POWER_GOOD_STATUS | 1O | 0 |
| 4 | CLEAR_VIN_MGMT_TO_VIN_BULK_INPUT_SWITCHOVER_STATUS | 1O | 0 |
| 3 | CLEAR_SWA_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS | 1O | 0 |
| 2 | CLEAR_SWB_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS | 1O | 0 |
| 1 | CLEAR_SWC_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS | 1O | 0 |
| 0 | CLEAR_SWD_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS | 1O | 0 |

### [7] CLEAR_PMIC_HIGH_TEMP_WARNING_STATUS

- Description: Clear PMIC High Temperature Warning Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 114, Register 0x09 [7][2] |

### [6] CLEAR_VBIAS_POWER_GOOD_STATUS

- Description: Clear VBias (applies to both VBias1 and VBias2) Power Good Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 114, Register 0x09 [6][2] |

### [5] CLEAR_VOUT_1.8V_OUTPUT_POWER_GOOD_STATUS

- Description: Clear VOUT_1.8V Output Power Good Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 114, Register 0x09 [5][2] |

### [4] CLEAR_VIN_MGMT_TO_VIN_BULK_INPUT_SWITCHOVER_STATUS

- Description: Clear VIN_Mgmt to VIN_Bulk Input Supply Switchover Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 114, Register 0x09 [4][2] |

### [3] CLEAR_SWA_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS

- Description: Clear Switch Node A High Output Current Consumption Warning Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 114, Register 0x09 [3][2] |

### [2] CLEAR_SWB_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS

- Description: Clear Switch Node B High Output Current Consumption Warning Status.[3]
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0
- Source correction: Table 122 prints 'Clear Register Table 114, Register 0x09 [2]' without the leading '1 =' used by every other bit of R11; treated as the value for code 1.

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 114, Register 0x09 [2][2] |

### [1] CLEAR_SWC_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS

- Description: Clear Switch Node C High Output Current Consumption Warning Status.[4]
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 114, Register 0x09 [1][2] |

### [0] CLEAR_SWD_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS

- Description: Clear Switch Node D High Output Current Consumption Warning Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 114, Register 0x09 [0][2] |

**Notes**

- NOTE 1: Table 122, Register 0x11 [7:0] bits are self-clearing.
- NOTE 2: See Table 28 and Table 29 for GSI_n and POWER_GOOD output signal status change.
- NOTE 3: This register is applicable regardless of the setting in Table 247, Register 0x4F [5,0].
- NOTE 4: This register is applicable regardless of the setting in Table 247, Register 0x4F [6].

## R12 (0x12) — CLEAR_SWA_OUTPUT_OVER_VOLTAGE_STATUS, CLEAR_SWB_OUTPUT_OVER_VOLTAGE_STATUS, CLEAR_SWC_OUTPUT_OVER_VOLTAGE_STATUS, CLEAR_SWD_OUTPUT_OVER_VOLTAGE_STATUS, CLEAR_PEC_ERROR_STATUS, CLEAR_PARITY_ERROR_STATUS

Region: Host Region | Source: JESD301-5 Table 123, p.149

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | CLEAR_SWA_OUTPUT_OVER_VOLTAGE_STATUS | 1O | 0 |
| 6 | CLEAR_SWB_OUTPUT_OVER_VOLTAGE_STATUS | 1O | 0 |
| 5 | CLEAR_SWC_OUTPUT_OVER_VOLTAGE_STATUS | 1O | 0 |
| 4 | CLEAR_SWD_OUTPUT_OVER_VOLTAGE_STATUS | 1O | 0 |
| 3 | CLEAR_PEC_ERROR_STATUS | 1O | 0 |
| 2 | CLEAR_PARITY_ERROR_STATUS | 1O | 0 |
| 1:0 | RESERVED | RV | 0 |

### [7] CLEAR_SWA_OUTPUT_OVER_VOLTAGE_STATUS

- Description: Clear Switch Node A Output Over Voltage Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 115, Register 0x0A [7][2] |

### [6] CLEAR_SWB_OUTPUT_OVER_VOLTAGE_STATUS

- Description: Clear Switch Node B Output Over Voltage Status.[3]
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 115, Register 0x0A [6][2] |

### [5] CLEAR_SWC_OUTPUT_OVER_VOLTAGE_STATUS

- Description: Clear Switch Node C Output Over Voltage Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 115, Register 0x0A [5][2] |

### [4] CLEAR_SWD_OUTPUT_OVER_VOLTAGE_STATUS

- Description: Clear Switch Node D Output Over Voltage Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 115, Register 0x0A [4][2] |

### [3] CLEAR_PEC_ERROR_STATUS

- Description: Clear PEC Error Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 115, Register 0x0A [3] |

### [2] CLEAR_PARITY_ERROR_STATUS

- Description: Clear Parity Error Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 115, Register 0x0A [2] |

### [1:0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

**Notes**

- NOTE 1: Table 123, Register 0x12 [7:0] are self-clearing bits.
- NOTE 2: See Table 28 and Table 29 for GSI_n and POWER_GOOD output signal status change.
- NOTE 3: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care.

## R13 (0x13) — CLEAR_SWA_OUTPUT_CURRENT_LIMITER_WARNING_STATUS, CLEAR_SWB_OUTPUT_CURRENT_LIMITER_WARNING_STATUS, CLEAR_SWC_OUTPUT_CURRENT_LIMITER_WARNING_STATUS, CLEAR_SWD_OUTPUT_CURRENT_LIMITER_WARNING_STATUS, CLEAR_SWA_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS, CLEAR_SWB_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS, CLEAR_SWC_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS, CLEAR_SWD_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

Region: Host Region | Source: JESD301-5 Table 124, p.150

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | CLEAR_SWA_OUTPUT_CURRENT_LIMITER_WARNING_STATUS | 1O | 0 |
| 6 | CLEAR_SWB_OUTPUT_CURRENT_LIMITER_WARNING_STATUS | 1O | 0 |
| 5 | CLEAR_SWC_OUTPUT_CURRENT_LIMITER_WARNING_STATUS | 1O | 0 |
| 4 | CLEAR_SWD_OUTPUT_CURRENT_LIMITER_WARNING_STATUS | 1O | 0 |
| 3 | CLEAR_SWA_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS | 1O | 0 |
| 2 | CLEAR_SWB_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS | 1O | 0 |
| 1 | CLEAR_SWC_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS | 1O | 0 |
| 0 | CLEAR_SWD_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS | 1O | 0 |

### [7] CLEAR_SWA_OUTPUT_CURRENT_LIMITER_WARNING_STATUS

- Description: Clear Switch Node A Output Current Limiter Warning Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 116, Register 0x0B [7][2] |

### [6] CLEAR_SWB_OUTPUT_CURRENT_LIMITER_WARNING_STATUS

- Description: Clear Switch Node B Output Current Limiter Warning Status.[3]
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 116, Register 0x0B [6][2] |

### [5] CLEAR_SWC_OUTPUT_CURRENT_LIMITER_WARNING_STATUS

- Description: Clear Switch Node C Output Current Limiter Warning Status.[4]
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 116, Register 0x0B [5][2] |

### [4] CLEAR_SWD_OUTPUT_CURRENT_LIMITER_WARNING_STATUS

- Description: Clear Switch Node D Output Current Limiter Warning Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 116, Register 0x0B [4][2] |

### [3] CLEAR_SWA_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

- Description: Clear Switch Node A Output Under Voltage Lockout Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 116, Register 0x0B [3][2] |

### [2] CLEAR_SWB_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

- Description: Clear Switch Node B Output Under Voltage Lockout Status.[5]
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 116, Register 0x0B [2][2] |

### [1] CLEAR_SWC_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

- Description: Clear Switch Node C Output Under Voltage Lockout Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 116, Register 0x0B [1][2] |

### [0] CLEAR_SWD_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

- Description: Clear Switch Node D Output Under Voltage Lockout Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 116, Register 0x0B [0][2] |

**Notes**

- NOTE 1: Table 124, Register 0x13 [7:0] bits self-clearing.
- NOTE 2: See Table 28 and Table 29 for GSI_n and POWER_GOOD output signal status change.
- NOTE 3: This register is applicable regardless of the setting in Table 247, Register 0x4F [5,0].
- NOTE 4: This register is applicable regardless of the setting in Table 247, Register 0x4F [6].
- NOTE 5: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care.

## R14 (0x14) — CLEAR_VIN_MGMT_POWER_GOOD_STATUS_SWITCHOVER_MODE, CLEAR_VBIAS_OUTPUT_OR_VIN_BULK_UNDER_VOLTAGE_LOCKOUT_STATUS, CLEAR_VOUT_1.0V_OUTPUT_POWER_GOOD_STATUS, GLOBAL_CLEAR_STATUS

Region: Host Region | Source: JESD301-5 Table 125, p.151

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:5 | RESERVED | RV | 0 |
| 4 | CLEAR_VIN_MGMT_POWER_GOOD_STATUS_SWITCHOVER_MODE | 1O | 0 |
| 3 | CLEAR_VBIAS_OUTPUT_OR_VIN_BULK_UNDER_VOLTAGE_LOCKOUT_STATUS | 1O | 0 |
| 2 | CLEAR_VOUT_1.0V_OUTPUT_POWER_GOOD_STATUS | 1O | 0 |
| 1 | RESERVED | RV | 0 |
| 0 | GLOBAL_CLEAR_STATUS | 1O | 0 |

### [7:5] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [4] CLEAR_VIN_MGMT_POWER_GOOD_STATUS_SWITCHOVER_MODE

- Description: Clear Valid VIN_Mgmt Power Good Status in Switchover Mode.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 157, Register 0x33 [4][2] |

### [3] CLEAR_VBIAS_OUTPUT_OR_VIN_BULK_UNDER_VOLTAGE_LOCKOUT_STATUS

- Description: Clear VBias Output or VIN_Bulk Input Under Voltage Lockout Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 157, Register 0x33 [3][2] |

### [2] CLEAR_VOUT_1.0V_OUTPUT_POWER_GOOD_STATUS

- Description: Clear VOUT_1.0V Output Power Good Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 157, Register 0x33 [2][2] |

### [1] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [0] GLOBAL_CLEAR_STATUS

- Description: Clear all[3] status bits.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear all status bits[4] |

**Notes**

- NOTE 1: Table 125, Register 0x14 [4:2, 0] bits are self-clearing.
- NOTE 2: See Table 28 and Table 29 for GSI_n and POWER_GOOD output signal status change.
- NOTE 3: All status bits in register Table 121, Register 0x10 [7,5:0], Table 122, Register 0x11 [7:0], Table 123, Register 0x12 [7:2], Table 124, Register 0x13 [7:0], Table 125, Register 0x14 [4:2], Table 178, Register 0x10E [7:0] and Table 179, Register 0x10F [7:6,0].
- NOTE 4: See Table 28 and Table 29 for GSI_n and POWER_GOOD output signal status change.

## R15 (0x15) — MASK_VIN_BULK_INPUT_POWER_GOOD_STATUS, MASK_SWA_OUTPUT_POWER_GOOD_STATUS, MASK_SWB_OUTPUT_POWER_GOOD_STATUS, MASK_SWC_OUTPUT_POWER_GOOD_STATUS, MASK_SWD_OUTPUT_POWER_GOOD_STATUS, MASK_VIN_MGMT_INPUT_OVER_VOLTAGE_STATUS, MASK_VIN_BULK_INPUT_OVER_VOLTAGE_STATUS

Region: Host Region | Source: JESD301-5 Table 126, p.153

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | MASK_VIN_BULK_INPUT_POWER_GOOD_STATUS | RW | 1 |
| 6 | RESERVED | RV | 0 |
| 5 | MASK_SWA_OUTPUT_POWER_GOOD_STATUS | RW | 1 |
| 4 | MASK_SWB_OUTPUT_POWER_GOOD_STATUS | RW | 1 |
| 3 | MASK_SWC_OUTPUT_POWER_GOOD_STATUS | RW | 1 |
| 2 | MASK_SWD_OUTPUT_POWER_GOOD_STATUS | RW | 1 |
| 1 | MASK_VIN_MGMT_INPUT_OVER_VOLTAGE_STATUS | RW | 0 |
| 0 | MASK_VIN_BULK_INPUT_OVER_VOLTAGE_STATUS | RW | 0 |

### [7] MASK_VIN_BULK_INPUT_POWER_GOOD_STATUS

- Description: Mask VIN_Bulk Input Power Good Status Event.
- Attribute: RW — Read/Write
- Default: 1 → Mask VIN_Bulk Input Power Good Status Event[1]

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask VIN_Bulk Input Power Good Status Event |
| 1 | Mask VIN_Bulk Input Power Good Status Event[1] |

### [6] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [5] MASK_SWA_OUTPUT_POWER_GOOD_STATUS

- Description: Mask SWA Output Power Good Status Event.
- Attribute: RW — Read/Write
- Default: 1 → Mask SWA Output Power Good Status Event1

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWA Output Power Good Status Event |
| 1 | Mask SWA Output Power Good Status Event1 |

### [4] MASK_SWB_OUTPUT_POWER_GOOD_STATUS

- Description: Mask SWB Output Power Good Status Event.[2]
- Attribute: RW — Read/Write
- Default: 1 → Mask SWB Output Power Good Status Event1

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWB Output Power Good Status Event |
| 1 | Mask SWB Output Power Good Status Event1 |

### [3] MASK_SWC_OUTPUT_POWER_GOOD_STATUS

- Description: Mask SWC Output Power Good Status Event.
- Attribute: RW — Read/Write
- Default: 1 → Mask SWC Output Power Good Status Event1

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWC Output Power Good Status Event |
| 1 | Mask SWC Output Power Good Status Event1 |

### [2] MASK_SWD_OUTPUT_POWER_GOOD_STATUS

- Description: Mask SWD Output Power Good Status Event.
- Attribute: RW — Read/Write
- Default: 1 → Mask SWD Output Power Good Status Event1

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWD Output Power Good Status Event |
| 1 | Mask SWD Output Power Good Status Event1 |

### [1] MASK_VIN_MGMT_INPUT_OVER_VOLTAGE_STATUS

- Description: Mask VIN_Mgmt Input Supply Over Voltage Status Event.
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask VIN_Mgmt Input Supply Over Voltage Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask VIN_Mgmt Input Supply Over Voltage Status Event |
| 1 | Mask VIN_Mgmt Input Supply Over Voltage Status Event[3] |

### [0] MASK_VIN_BULK_INPUT_OVER_VOLTAGE_STATUS

- Description: Mask VIN_Bulk Input Supply Over Voltage Status Event.
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask VIN_Bulk Input Supply Over Voltage Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask VIN_Bulk Input Supply Over Voltage Status Event |
| 1 | Mask VIN_Bulk Input Supply Over Voltage Status Event3 |

**Notes**

- NOTE 1: Not assert GSI_n or assert POWER_GOOD output signal.
- NOTE 2: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care.
- NOTE 3: Not assert GSI_n output signal.

## R16 (0x16) — MASK_PMIC_HIGH_TEMP_WARNING_STATUS, MASK_VBIAS_POWER_GOOD_STATUS, MASK_VOUT_1.8V_OUTPUT_POWER_GOOD_STATUS, MASK_VIN_MGMT_TO_VIN_BULK_SWITCHOVER_STATUS, MASK_SWA_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS, MASK_SWB_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS, MASK_SWC_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS, MASK_SWD_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS

Region: Host Region | Source: JESD301-5 Table 127, p.154

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | MASK_PMIC_HIGH_TEMP_WARNING_STATUS | RW | 0 |
| 6 | MASK_VBIAS_POWER_GOOD_STATUS | RW | 0 |
| 5 | MASK_VOUT_1.8V_OUTPUT_POWER_GOOD_STATUS | RW | 1 |
| 4 | MASK_VIN_MGMT_TO_VIN_BULK_SWITCHOVER_STATUS | RW | 0 |
| 3 | MASK_SWA_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS | RW | 0 |
| 2 | MASK_SWB_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS | RW | 0 |
| 1 | MASK_SWC_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS | RW | 0 |
| 0 | MASK_SWD_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS | RW | 0 |

### [7] MASK_PMIC_HIGH_TEMP_WARNING_STATUS

- Description: Mask PMIC High Temperature Warning Status Event.
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask PMIC High Temperature Warning Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask PMIC High Temperature Warning Status Event |
| 1 | Mask PMIC High Temperature Warning Status Event[1] |

### [6] MASK_VBIAS_POWER_GOOD_STATUS

- Description: Mask VBias (applies to both VBias1 and VBias2) Power Good Status Event.
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask VBias Power Good Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask VBias Power Good Status Event |
| 1 | Mask VBias Power Good Status Event[2] |

### [5] MASK_VOUT_1.8V_OUTPUT_POWER_GOOD_STATUS

- Description: Mask VOUT_1.8V Output Power Good Status Event.
- Attribute: RW — Read/Write
- Default: 1 → Mask 1.8V Output Power Good Status Event2

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask 1.8V Output Power Good Status Event |
| 1 | Mask 1.8V Output Power Good Status Event2 |

### [4] MASK_VIN_MGMT_TO_VIN_BULK_SWITCHOVER_STATUS

- Description: Mask VIN_Mgmt to VIN_Bulk Input Supply Switchover Status Event.
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask VIN_Mgmt to VIN_Bulk Input Supply Switchover Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask VIN_Mgmt to VIN_Bulk Input Supply Switchover Status Event |
| 1 | Mask VIN_Mgmt to VIN_Bulk Input Supply Switchover Status Event1 |

### [3] MASK_SWA_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS

- Description: Mask SWA High Output Current Consumption Warning Status Event.
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask SWA Output Current Consumption Warning Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWA Output Current Consumption Warning Status Event |
| 1 | Mask SWA Output Current Consumption Warning Status Event1 |

### [2] MASK_SWB_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS

- Description: Mask SWB High Output Current Consumption Warning Status Event.[3]
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask SWB Output Current Consumption Warning Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWB Output Current Consumption Warning Status Event |
| 1 | Mask SWB Output Current Consumption Warning Status Event1 |

### [1] MASK_SWC_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS

- Description: Mask SWC High Output Current Consumption Warning Status Event.[4]
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask SWC Output Current Consumption Warning Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWC Output Current Consumption Warning Status Event |
| 1 | Mask SWC Output Current Consumption Warning Status Event1 |

### [0] MASK_SWD_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS

- Description: Mask SWD High Output Current Consumption Warning Status Event.
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask SWD Output Current Consumption Warning Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWD Output Current Consumption Warning Status Event |
| 1 | Mask SWD Output Current Consumption Warning Status Event1 |

**Notes**

- NOTE 1: Not assert GSI_n output signal.
- NOTE 2: Not assert GSI_n or assert POWER_GOOD output signal
- NOTE 3: This register is applicable regardless of the setting in Table 247, Register 0x4F [5,0].
- NOTE 4: This register is applicable regardless of the setting in Table 247, Register 0x4F [6].

## R17 (0x17) — MASK_SWA_OUTPUT_OVER_VOLTAGE_STATUS, MASK_SWB_OUTPUT_OVER_VOLTAGE_STATUS, MASK_SWC_OUTPUT_OVER_VOLTAGE_STATUS, MASK_SWD_OUTPUT_OVER_VOLTAGE_STATUS, MASK_PEC_ERROR_STATUS, MASK_PARITY_ERROR_STATUS

Region: Host Region | Source: JESD301-5 Table 128, p.155

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | MASK_SWA_OUTPUT_OVER_VOLTAGE_STATUS | RW | 0 |
| 6 | MASK_SWB_OUTPUT_OVER_VOLTAGE_STATUS | RW | 0 |
| 5 | MASK_SWC_OUTPUT_OVER_VOLTAGE_STATUS | RW | 0 |
| 4 | MASK_SWD_OUTPUT_OVER_VOLTAGE_STATUS | RW | 0 |
| 3 | MASK_PEC_ERROR_STATUS | RW | 0 |
| 2 | MASK_PARITY_ERROR_STATUS | RW | 0 |
| 1:0 | RESERVED | RV | 0 |

### [7] MASK_SWA_OUTPUT_OVER_VOLTAGE_STATUS

- Description: Mask SWA Output Over Voltage Status Event.
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask SWA Output Over Voltage Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWA Output Over Voltage Status Event |
| 1 | Mask SWA Output Over Voltage Status Event[1] |

### [6] MASK_SWB_OUTPUT_OVER_VOLTAGE_STATUS

- Description: Mask SWB Output Over Voltage Status Event.[2]
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask SWB Output Over Voltage Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWB Output Over Voltage Status Event |
| 1 | Mask SWB Output Over Voltage Status Event1 |

### [5] MASK_SWC_OUTPUT_OVER_VOLTAGE_STATUS

- Description: Mask SWC Output Over Voltage Status Event.
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask SWC Output Over Voltage Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWC Output Over Voltage Status Event |
| 1 | Mask SWC Output Over Voltage Status Event1 |

### [4] MASK_SWD_OUTPUT_OVER_VOLTAGE_STATUS

- Description: Mask SWD Output Over Voltage Status Event.
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask SWD Output Over Voltage Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWD Output Over Voltage Status Event |
| 1 | Mask SWD Output Over Voltage Status Event1 |

### [3] MASK_PEC_ERROR_STATUS

- Description: Mask PEC Error Event for GSI_n output Only[3]
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask PEC Error Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask PEC Error Status Event |
| 1 | Mask PEC Error Status |

### [2] MASK_PARITY_ERROR_STATUS

- Description: Mask Parity Error Event for GSI_n output Only3
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask Parity Error Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask Parity Error Status Event |
| 1 | Mask Parity Error Status |

### [1:0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

**Notes**

- NOTE 1: Not assert GSI_n output signal.
- NOTE 2: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care.
- NOTE 3: Only applicable when PMIC is in I3C Basic Mode. This Mask register only masks the GSI_n output. Does not apply to IBI.

## R18 (0x18) — MASK_SWA_OUTPUT_CURRENT_LIMITER_WARNING_STATUS, MASK_SWB_OUTPUT_CURRENT_LIMITER_WARNING_STATUS, MASK_SWC_OUTPUT_CURRENT_LIMITER_WARNING_STATUS, MASK_SWD_OUTPUT_CURRENT_LIMITER_WARNING_STATUS, MASK_SWA_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS, MASK_SWB_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS, MASK_SWC_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS, MASK_SWD_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

Region: Host Region | Source: JESD301-5 Table 129, p.156

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | MASK_SWA_OUTPUT_CURRENT_LIMITER_WARNING_STATUS | RW | 0 |
| 6 | MASK_SWB_OUTPUT_CURRENT_LIMITER_WARNING_STATUS | RW | 0 |
| 5 | MASK_SWC_OUTPUT_CURRENT_LIMITER_WARNING_STATUS | RW | 0 |
| 4 | MASK_SWD_OUTPUT_CURRENT_LIMITER_WARNING_STATUS | RW | 0 |
| 3 | MASK_SWA_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS | RW | 0 |
| 2 | MASK_SWB_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS | RW | 0 |
| 1 | MASK_SWC_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS | RW | 0 |
| 0 | MASK_SWD_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS | RW | 0 |

### [7] MASK_SWA_OUTPUT_CURRENT_LIMITER_WARNING_STATUS

- Description: Mask SWA Output Current Limiter Warning Status Event.
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask SWA Output Current Limiter Warning Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWA Output Current Limiter Warning Status Event |
| 1 | Mask SWA Output Current Limiter Warning Status Event[1] |

### [6] MASK_SWB_OUTPUT_CURRENT_LIMITER_WARNING_STATUS

- Description: Mask SWB Output Current Limiter Warning Status Event.[2]
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask SWB Output Current Limiter Warning Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWB Output Current Limiter Warning Status Event |
| 1 | Mask SWB Output Current Limiter Warning Status Event1 |

### [5] MASK_SWC_OUTPUT_CURRENT_LIMITER_WARNING_STATUS

- Description: Mask SWC Output Current Limiter Warning Status Event.
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask SWC Output Current Limiter Warning Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWC Output Current Limiter Warning Status Event |
| 1 | Mask SWC Output Current Limiter Warning Status Event1 |

### [4] MASK_SWD_OUTPUT_CURRENT_LIMITER_WARNING_STATUS

- Description: Mask SWD Output Current Limiter Warning Status Event.
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask SWD Output Current Limiter Warning Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWD Output Current Limiter Warning Status Event |
| 1 | Mask SWD Output Current Limiter Warning Status Event1 |

### [3] MASK_SWA_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

- Description: Mask SWA Output Under Voltage Lockout Status Event.
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask SWA Output Under Voltage Lockout Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWA Output Under Voltage Lockout Status Event |
| 1 | Mask SWA Output Under Voltage Lockout Status Event1 |

### [2] MASK_SWB_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

- Description: Mask SWB Output Under Voltage Lockout Status Event.[3]
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask SWB Output Under Voltage Lockout Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWB Output Under Voltage Lockout Status Event |
| 1 | Mask SWB Output Under Voltage Lockout Status Event1 |

### [1] MASK_SWC_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

- Description: Mask SWC Output Under Voltage Lockout Status Event.
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask SWC Output Under Voltage Lockout Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWC Output Under Voltage Lockout Status Event |
| 1 | Mask SWC Output Under Voltage Lockout Status Event1 |

### [0] MASK_SWD_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

- Description: Mask SWD Output Under Voltage Lockout Status Event.
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask SWD Output Under Voltage Lockout Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWD Output Under Voltage Lockout Status Event |
| 1 | Mask SWD Output Under Voltage Lockout Status Event1 |

**Notes**

- NOTE 1: Not assert GSI_n output signal.
- NOTE 2: This register is applicable regardless of the setting in Table 247, Register 0x4F [5,0].
- NOTE 3: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care.

## R19 (0x19) — MASK_VIN_MGMT_POWER_GOOD_STATUS_SWITCHOVER_MODE, MASK_VBIAS_OUTPUT_OR_VIN_BULK_UNDER_VOLTAGE_LOCKOUT_STATUS, MASK_VOUT_1.0V_OUTPUT_POWER_GOOD_STATUS

Region: Host Region | Source: JESD301-5 Table 130, p.157

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:5 | RESERVED | RV | 0 |
| 4 | MASK_VIN_MGMT_POWER_GOOD_STATUS_SWITCHOVER_MODE | RW | 0 |
| 3 | MASK_VBIAS_OUTPUT_OR_VIN_BULK_UNDER_VOLTAGE_LOCKOUT_STATUS | RW | 0 |
| 2 | MASK_VOUT_1.0V_OUTPUT_POWER_GOOD_STATUS | RW | 1 |
| 1:0 | RESERVED | RV | 0 |

### [7:5] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [4] MASK_VIN_MGMT_POWER_GOOD_STATUS_SWITCHOVER_MODE

- Description: Mask VIN_Mgmt Input Supply Power Good Status in Switchover Mode Only
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask VIN_Mgmt Input Power Supply Power Good Status Event in Switchover Mode

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask VIN_Mgmt Input Power Supply Power Good Status Event in Switchover Mode |
| 1 | Mask VIN_Mgmt Input Power Supply Power Good Status Event in Switchover Mode[1] |

### [3] MASK_VBIAS_OUTPUT_OR_VIN_BULK_UNDER_VOLTAGE_LOCKOUT_STATUS

- Description: Mask VBias Output or VIN_Bulk Input Under Voltage Lockout Event
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask Vbias Output or VIN_Bulk Input Under Voltage Lockout Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask Vbias Output or VIN_Bulk Input Under Voltage Lockout Event |
| 1 | Mask Vbias Output or VIN_Bulk Input Under Voltage Lockout Event1 |

### [2] MASK_VOUT_1.0V_OUTPUT_POWER_GOOD_STATUS

- Description: Mask VOUT_1.0V Output Power Good Status Event.
- Attribute: RW — Read/Write
- Default: 1 → Mask VOUT_1.0V Output Power Good Status Event[2]

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask VOUT_1.0V Output Power Good Status Event |
| 1 | Mask VOUT_1.0V Output Power Good Status Event[2] |

### [1:0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

**Notes**

- NOTE 1: Not assert GSI_n output signal.
- NOTE 2: Not assert GSI_n or POWER_GOOD output signal.

## R1A (0x1A) — VIN_BULK_POWER_GOOD_THRESHOLD_VOLTAGE, VBIAS_POWER_GOOD_THRESHOLD_VOLTAGE, VOUT_1.8V_POWER_GOOD_THRESHOLD_VOLTAGE, OUTPUT_POWER_SELECT, VOUT_1.0V_POWER_GOOD_THRESHOLD_VOLTAGE

Region: Host Region | Source: JESD301-5 Table 131, p.158

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:5 | VIN_BULK_POWER_GOOD_THRESHOLD_VOLTAGE | RW | 110 |
| 4 | RESERVED | RV | 0 |
| 3 | VBIAS_POWER_GOOD_THRESHOLD_VOLTAGE | RW | 0 |
| 2 | VOUT_1.8V_POWER_GOOD_THRESHOLD_VOLTAGE | RW | 0 |
| 1 | OUTPUT_POWER_SELECT | RW | 0 |
| 0 | VOUT_1.0V_POWER_GOOD_THRESHOLD_VOLTAGE | RW | 0 |

### [7:5] VIN_BULK_POWER_GOOD_THRESHOLD_VOLTAGE

- Description: VIN Bulk Input Threshold Voltage for Input Power Good Status for input supply
- Attribute: RW — Read/Write
- Default: 110 → 4.25 V[1],[2],[3]

| Code (bin) | Meaning |
|---|---|
| 000 | Reserved |
| 001 | 9.5 V |
| 010 | 8.5 V |
| 011 | 7.5 V |
| 100 | 6.5 V |
| 101 | 5.5 V |
| 110 | 4.25 V[1],[2],[3] |
| 111 | Reserved |

### [4] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [3] VBIAS_POWER_GOOD_THRESHOLD_VOLTAGE

- Description: VBias1 or VBias2 LDO Output (depending on PMIC implementation) Threshold Voltage for Power Good Status
- Attribute: RW — Read/Write
- Default: 0 → Vendor Specific

| Code (bin) | Meaning |
|---|---|
| 0 | Vendor Specific |
| 1 | Reserved |

### [2] VOUT_1.8V_POWER_GOOD_THRESHOLD_VOLTAGE

- Description: VOUT 1.8V LDO Output Threshold Voltage for Power Good Status
- Attribute: RW — Read/Write
- Default: 0 → 1.6 V

| Code (bin) | Meaning |
|---|---|
| 0 | 1.6 V |
| 1 | Reserved |

### [1] OUTPUT_POWER_SELECT

- Description: Switch Regulator Output Power Select[4]
- Attribute: RW — Read/Write
- Default: 0 → Report individual power for each rail in R0C, R0D, R0E & R0F or R100, R101, R102, R103, R104, R105, R106, R107 depending on the setting of R32[1:0]

| Code (bin) | Meaning |
|---|---|
| 0 | Report individual power for each rail in R0C, R0D, R0E & R0F or R100, R101, R102, R103, R104, R105, R106, R107 depending on the setting of R32[1:0] |
| 1 | Report total power of each rail in R0C[5] or R101+R102[6] |

### [0] VOUT_1.0V_POWER_GOOD_THRESHOLD_VOLTAGE

- Description: VOUT 1.0V LDO Output Threshold Voltage for Power Good Status
- Attribute: RW — Read/Write
- Default: 0 → -10% from the setting in Table 148, Register 0x2B [2:1]

| Code (bin) | Meaning |
|---|---|
| 0 | -10% from the setting in Table 148, Register 0x2B [2:1] |
| 1 | -15% from the setting in Table 148, Register 0x2B [2:1] |

**Notes**

- NOTE 1: If VIN_Bulk input voltage falls below this threshold, the PMIC may not guarantee the operation.
- NOTE 2: If VIN_Bulk voltage continues to fall below vendor specific UVLO, the PMIC triggers an VR Disable command and executes power down sequence.
- NOTE 3: If VIN_Bulk voltage threshold is higher than default setting of this register, the PMIC continues to operate but updates its PWR_GOOD status register and GSI_n/PWR_GOOD signal is asserted when VIN_Bulk falls below the threshold setting.
- NOTE 4: This register is only applicable if Table 132, Register 0x1B [6] = ‘1’.
- NOTE 5: Host should only read Table 117, Register 0x0C [7:0] for total power if Table 155, Register 0x32 [1:0] = ‘00’. The register contents of Table 118, Register 0x0D, Table 119, Register 0x0E and Table 120, Register 0x0F may not be valid.
- NOTE 6: Host should only read Table 168, Register 0x101 [2:0] and Table 169, Register 0x102 [7:0] for total power if Table 155, Register 0x32 [1:0] = ‘01’. The register contents of Table 170, Register 0x103, Table 171, Register 0x104 and Table 172, Register 0x105, Table 173, Register 0x106, and Table 174, Register 0x107 may not be valid.

## R1B (0x1B) — VIN_BULK_OVER_VOLTAGE_THRESHOLD, CURRENT_OR_POWER_METER_SELECT, VIN_MGMT_OVER_VOLTAGE_THRESHOLD, GLOBAL_PWR_GOOD_PIN_STATUS_MASK, GSI_N_PIN_ENABLE, PMIC_HIGH_TEMPERATURE_WARNING_THRESHOLD

Region: Host Region | Source: JESD301-5 Table 132, p.159

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | VIN_BULK_OVER_VOLTAGE_THRESHOLD | RW | 0 |
| 6 | CURRENT_OR_POWER_METER_SELECT | RW | 0 |
| 5 | VIN_MGMT_OVER_VOLTAGE_THRESHOLD | RW | 0 |
| 4 | GLOBAL_PWR_GOOD_PIN_STATUS_MASK | RW | 0 |
| 3 | GSI_N_PIN_ENABLE | RW | 0 |
| 2:0 | PMIC_HIGH_TEMPERATURE_WARNING_THRESHOLD | RW | 101 |

### [7] VIN_BULK_OVER_VOLTAGE_THRESHOLD

- Description: VIN_Bulk Input Over Voltage Threshold Setting
- Attribute: RW — Read/Write
- Default: 0 → 14.5 V

| Code (bin) | Meaning |
|---|---|
| 0 | 14.5 V |
| 1 | 16.0 V |

### [6] CURRENT_OR_POWER_METER_SELECT

- Description: PMIC Output Regulator Measurement - Current or Power Meter[1]
- Attribute: RW — Read/Write
- Default: 0 → Report Current Measurements in registers

| Code (bin) | Meaning |
|---|---|
| 0 | Report Current Measurements in registers |
| 1 | Report Power Measurements in registers |

### [5] VIN_MGMT_OVER_VOLTAGE_THRESHOLD

- Description: VIN_Mgmt Input Over Voltage Threshold
- Attribute: RW — Read/Write
- Default: 0 → 3.8 V

| Code (bin) | Meaning |
|---|---|
| 0 | 3.8 V |
| 1 | 3.7 V |

### [4] GLOBAL_PWR_GOOD_PIN_STATUS_MASK

- Description: Global Mask PWR_GOOD Output Pin[2]
- Attribute: RW — Read/Write
- Default: 0 → Not Masked

| Code (bin) | Meaning |
|---|---|
| 0 | Not Masked |
| 1 | Masked |

### [3] GSI_N_PIN_ENABLE

- Description: Enable GSI_n Pin[3]
- Attribute: RW — Read/Write
- Default: 0 → Disable GSI_n Pin

| Code (bin) | Meaning |
|---|---|
| 0 | Disable GSI_n Pin |
| 1 | Enable GSI_n Pin |

### [2:0] PMIC_HIGH_TEMPERATURE_WARNING_THRESHOLD

- Description: PMIC High Temperature Warning Threshold[4]
- Attribute: RW — Read/Write
- Default: 101 → PMIC temperature > 125 °C

| Code (bin) | Meaning |
|---|---|
| 000 | Reserved |
| 001 | PMIC temperature > 85 °C |
| 010 | PMIC temperature > 95 °C |
| 011 | PMIC temperature > 105 °C |
| 100 | PMIC temperature > 115 °C |
| 101 | PMIC temperature > 125 °C |
| 110 | PMIC temperature > 135 °C |
| 111 | Reserved |

**Notes**

- NOTE 1: Table 117, Register 0x0C [7:0] to Table 120, Register 0x0F[7:0] if Table 155, Register 0x32 [1:0] = ‘00’ or Table 167, Register 0x100 [7:0] to Table 174, Register 0x107[7:0] if Table 155, Register 0x32 [1:0] = ‘01’.
- NOTE 2: Mask POWER_GOOD output signal for all appropriate register bits in Table 126, Register 0x15 [7,5:0], Table 127, Register 0x16 [7:0], Table 128, Register 0x17 [7:4], Table 129, Register 0x18 [7:0] and Table 130, Register 0x19 [4:2]. Mask Register Control Table 152, Register 0x2F [1:0] still applies when Global PWR_GOOD output Mask register is set to ‘1’.
- NOTE 3: This register can be used as Global Mask Function for GSI_n pin. If disabled, this masks GSI_n output signal for all register bits in Table 126, Register 0x15 [7, 5:0], Table 127, Register 0x16 [7:0], Table 128, Register 0x17 [7:2], Table 129, Register 0x18 [7:0], and Table 130, Register 0x19 [4:2].
- NOTE 4: The tolerance of the temperature warning threshold is + 5 0C from the selected setting.

## R1C (0x1C) — SWA_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD

Region: Host Region | Source: JESD301-5 Table 133, p.160

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SWA_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD | RW | 0011 1100 |

### [7:0] SWA_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD

- Description: SWA Output High Current Consumption Warning Threshold[2]
- Attribute: RW — Read/Write
- Default: 0011 1100 → > 7500 mA (if If Table 155, Register 0x32[1:0] = ‘00’); > 1875 mA (if If Table 155, Register 0x32[1:0] = ‘01’)

**When: If Table 155, Register 0x32[1:0] = ‘00’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | > 125 mA |
| 00000010 | 0x02 | > 250 mA |
| ... | ... | ... |
| 11111111 | 0xFF | > 31.875 A |

**When: If Table 155, Register 0x32[1:0] = ‘01’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | > 31.25 mA |
| 00000010 | 0x02 | > 62.5 mA |
| ... | ... | ... |
| 11111111 | 0xFF | > 7.968 A |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 271, Register 0x67.
- NOTE 2: This register is applicable regardless of the setting in Table 247, Register 0x4F [5,0]. For dual phase operation, registers Table 133, Register 0x1C [7:0] and Table 134, Register 0x1D [7:0] must be configured identical. For three phase operation, registers Table 133, Register 0x1C [7:0], Table 134, Register 0x1D [7:0] and Table 182, Register 0x11A [7:0] must be configured identical.

## R1D (0x1D) — SWB_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD

Region: Host Region | Source: JESD301-5 Table 134, p.161

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SWB_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD | RW | 0011 1100 |

### [7:0] SWB_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD

- Description: SWB Output High Current Consumption Warning Threshold[2]
- Attribute: RW — Read/Write
- Default: 0011 1100 → > 7500 mA (if If Table 155, Register 0x32[1:0] = ‘00’); > 1875 mA (if If Table 155, Register 0x32[1:0] = ‘01’)

**When: If Table 155, Register 0x32[1:0] = ‘00’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | > 125 mA |
| 00000010 | 0x02 | > 250 mA |
| ... | ... | ... |
| 11111111 | 0xFF | > 31.875 A |

**When: If Table 155, Register 0x32[1:0] = ‘01’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | > 31.25 mA |
| 00000010 | 0x02 | > 62.5 mA |
| ... | ... | ... |
| 11111111 | 0xFF | > 7.968 A |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 272, Register 0x68.
- NOTE 2: This register is applicable regardless of the setting in Table 247, Register 0x4F [5,0]. For dual phase operation, registers Table 133, Register 0x1C [7:0] and Table 134, Register 0x1D [7:0] must be configured identical. For three phase operation, registers Table 133, Register 0x1C [7:0], Table 134, Register 0x1D [7:0] and Table 182, Register 0x11A [7:0] must be configured identical.

## R1E (0x1E) — SWC_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD

Region: Host Region | Source: JESD301-5 Table 135, p.162

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SWC_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD | RW | 0011 1100 |

### [7:0] SWC_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD

- Description: SWC Output High Current Consumption Warning Threshold[2]
- Attribute: RW — Read/Write
- Default: 0011 1100 → > 7500 mA (if If Table 155, Register 0x32[1:0] = ‘00’); > 1875 mA (if If Table 155, Register 0x32[1:0] = ‘01’)

**When: If Table 155, Register 0x32[1:0] = ‘00’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | > 125 mA |
| 00000010 | 0x02 | > 250 mA |
| ... | ... | ... |
| 11111111 | 0xFF | > 31.875 A |

**When: If Table 155, Register 0x32[1:0] = ‘01’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | > 31.25 mA |
| 00000010 | 0x02 | > 62.5 mA |
| ... | ... | ... |
| 11111111 | 0xFF | > 7.968 A |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 273, Register 0x69.
- NOTE 2: This register is applicable regardless of the setting in Table 247, Register 0x4F [6]. For dual phase operation, registers Table 135, Register 0x1E [7:0] and Table 183, Register 0x11B [7:0] must be configured identical.

## R1F (0x1F) — SWD_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD

Region: Host Region | Source: JESD301-5 Table 136, p.162

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SWD_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD | RW | 0010 1000 |

### [7:0] SWD_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD

- Description: SWD Output High Current Consumption Warning Threshold
- Attribute: RW — Read/Write
- Default: 0010 1000 → > 5000 mA (if If Table 155, Register 0x32[1:0] = ‘00’); > 1250 mA (if If Table 155, Register 0x32[1:0] = ‘01’)
- Source correction: Spec lists code 000000100 for '> 250 mA'; corrected to 00000010. 9-digit code in source table; 250 mA is code 2 (125 mA/LSB).

**When: If Table 155, Register 0x32[1:0] = ‘00’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | > 125 mA |
| 00000010 | 0x02 | > 250 mA |
| ... | ... | ... |
| 11111111 | 0xFF | > 31.875 A |

**When: If Table 155, Register 0x32[1:0] = ‘01’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | > 31.25 mA |
| 00000010 | 0x02 | > 62.5 mA |
| ... | ... | ... |
| 11111111 | 0xFF | > 7.968 A |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 274, Register 0x6A.

## R20 (0x20) — SWA_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING, SWB_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING, SWC_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING, SWD_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING

Region: Host Region | Source: JESD301-5 Table 137, p.163

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWA_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING | RW | 01 |
| 5:4 | SWB_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING | RW | 01 |
| 3:2 | SWC_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING | RW | 01 |
| 1:0 | SWD_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING | RW | 01 |

### [7:6] SWA_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING

- Description: COT Ivalley_limit
- Attribute: RW — Read/Write
- Default: 01 → 7A

| Code (bin) | Meaning |
|---|---|
| 00 | 6A |
| 01 | 7A |
| 10 | 8A |
| 11 | 9A |

### [5:4] SWB_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING

- Description: COT Ivalley_limit[2]
- Attribute: RW — Read/Write
- Default: 01 → 7A

| Code (bin) | Meaning |
|---|---|
| 00 | 6A |
| 01 | 7A |
| 10 | 8A |
| 11 | 9A |

### [3:2] SWC_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING

- Description: COT Ivalley_limit[3]
- Attribute: RW — Read/Write
- Default: 01 → 7A

| Code (bin) | Meaning |
|---|---|
| 00 | 6A |
| 01 | 7A |
| 10 | 8A |
| 11 | 9A |

### [1:0] SWD_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING

- Description: COT Ivalley_limit
- Attribute: RW — Read/Write
- Default: 01 → 4.5A

| Code (bin) | Meaning |
|---|---|
| 00 | 4A |
| 01 | 4.5A |
| 10 | 5A |
| 11 | 5.5A |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 248, Register 0x50.
- NOTE 2: This register is applicable regardless of the setting in Table 247, Register 0x4F [5,0].
- NOTE 3: This register is applicable regardless of the setting in Table 247, Register 0x4F [6].

## R21 (0x21) — SWA_VOLTAGE_SETTING, SWA_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

Region: Host Region | Source: JESD301-5 Table 138, p.164

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:1 | SWA_VOLTAGE_SETTING | RW | 011 1100 |
| 0 | SWA_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING | RW | 0 |

### [7:1] SWA_VOLTAGE_SETTING

- Description: SWA Output Regulator Voltage Setting[3],[4]
- Attribute: RW — Read/Write
- Default: 011 1100 → 1100 mV or 900 mV

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 0000000 | 0x00 | 800 mV[5] or 600 mV[6] |
| 0000001 | 0x01 | 805 mV or 605 mV |
| 0000010 | 0x02 | 810 mV or 610 mV |
| ... | ... | ... |
| 0111100 | 0x3C | 1100 mV or 900 mV |
| ... | ... | ... |
| 1111101 | 0x7D | 1425 mV or 1225 mV |
| 1111110 | 0x7E | 1430 mV or 1230 mV |
| 1111111 | 0x7F | 1435 mV or 1235 mV |

### [0] SWA_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

- Description: SWA Output Threshold Low Side Voltage For Power Good Status
- Attribute: RW — Read/Write
- Default: 0 → -5% from the setting in Table 138, Register 0x21 [7:1]

| Code (bin) | Meaning |
|---|---|
| 0 | -5% from the setting in Table 138, Register 0x21 [7:1] |
| 1 | -7.5% from the setting in Table 138, Register 0x21 [7:1] |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 237, Register 0x45.
- NOTE 2: If required, the host must update the settings in register Table 138, Register 0x21 [0], Table 139, Register 0x22 [7:2] and Table 137, Register 0x20 [7:6] first prior to updating the settings in the register Table 138, Register 0x21 [7:1].
- NOTE 3: PMIC guarantees efficiency spec within a range of 1050 mV to 1160 mV.
- NOTE 4: After VR is enabled, the host may update this register to any new setting that it may desire. However to prevent false error trigger, the PMIC internally will increment the SWA output voltage setting by 5 mV at a time. The time it takes for PMIC to adjust the output voltage is 5 μs for each 5 mV increment. The host must wait sufficient time for PMIC to adjust to final value. As an example, if host adjusts the output voltage by 50 mV from the original value, the host must wait minimum of 50 μs before PMIC can guarantee the new output voltage. During this time, PMIC masks the PWR_GOOD output signal assertion to prevent any artificial error due to the crossing of the output voltage threshold setting. However, PMIC does assert PWR_GOOD output signal if there are any abnormal issues that triggers VR Disable command as described in Table 27. Further, PMIC does monitor PWR_GOOD input signal and executes power off config sequence registers if it is registered low when Table 155, Register 0x32 [5] = ‘1’.
- NOTE 5: Table 148, Register 0x2B [5] = ‘0’; 5 mV step size.
- NOTE 6: Table 148, Register 0x2B [5] = ‘1’; 5 mV step size

## R22 (0x22) — SWA_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING, SWA_OVER_VOLTAGE_THRESHOLD_SETTING, SWA_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING, SWA_OUTPUT_SOFT_STOP_TIME

Region: Host Region | Source: JESD301-5 Table 139, p.165

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWA_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING | RW | 01 |
| 5:4 | SWA_OVER_VOLTAGE_THRESHOLD_SETTING | RW | 10 |
| 3:2 | SWA_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING | RW | 00 |
| 1:0 | SWA_OUTPUT_SOFT_STOP_TIME | RW | 00 |

### [7:6] SWA_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING

- Description: SWA Output Threshold High Side Voltage For Power Good Status
- Attribute: RW — Read/Write
- Default: 01 → +7.5% from the setting in Table 138, Register 0x21 [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +5% from the setting in Table 138, Register 0x21 [7:1] |
| 01 | +7.5% from the setting in Table 138, Register 0x21 [7:1] |
| 10 | +10% from the setting in Table 138, Register 0x21 [7:1] |
| 11 | Reserved |

### [5:4] SWA_OVER_VOLTAGE_THRESHOLD_SETTING

- Description: SWA Output Regulator Threshold For Over Voltage Status[3]
- Attribute: RW — Read/Write
- Default: 10 → +12.5% from the setting in Table 138, Register 0x21 [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +7.5% from the setting in Table 138, Register 0x21 [7:1] |
| 01 | +10% from the setting in Table 138, Register 0x21 [7:1] |
| 10 | +12.5% from the setting in Table 138, Register 0x21 [7:1] |
| 11 | Reserved |

### [3:2] SWA_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING

- Description: SWA Output Regulator Threshold For Under Voltage Lockout Status
- Attribute: RW — Read/Write
- Default: 00 → -10% from the setting in Table 138, Register 0x21 [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | -10% from the setting in Table 138, Register 0x21 [7:1] |
| 01 | -12.5% from the setting in Table 138, Register 0x21 [7:1] |
| 10 | Reserved |
| 11 | Reserved |

### [1:0] SWA_OUTPUT_SOFT_STOP_TIME

- Description: SWA Output Regulator Soft Stop Time After VR Disable[4]
- Attribute: RW — Read/Write
- Default: 00 → 0.5 ms

| Code (bin) | Meaning |
|---|---|
| 00 | 0.5 ms |
| 01 | 1 ms |
| 10 | 2 ms |
| 11 | 4 ms |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 238, Register 0x46.
- NOTE 2: If required, the host must update the setting in register Table 138, Register 0x21 [0], Table 139, Register 0x22 [7:2] and Table 137, Register 0x20 [7:6] first prior to updating the settings in the register Table 138, Register 0x21 [7:1].
- NOTE 3: The setting for the Over Voltage must be higher than Power Good High Side Voltage threshold in Table 139, Register 0x22[7:6].
- NOTE 4: This is the time it takes for buck regulator to go from steady state voltage to 0 V.

## R23 (0x23) — SWB_VOLTAGE_SETTING, SWB_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

Region: Host Region | Source: JESD301-5 Table 140, p.166

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:1 | SWB_VOLTAGE_SETTING | RW | 011 1100 |
| 0 | SWB_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING | RW | 0 |

### [7:1] SWB_VOLTAGE_SETTING

- Description: SWB Output Regulator Voltage Setting[4],[5]
- Attribute: RW — Read/Write
- Default: 011 1100 → 1100 mV or 900 mV

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 0000000 | 0x00 | 800 mV[6] or 600 mV[7] |
| 0000001 | 0x01 | 805 mV or 605 mV |
| 0000010 | 0x02 | 810 mV or 610 mV |
| ... | ... | ... |
| 0111100 | 0x3C | 1100 mV or 900 mV |
| ... | ... | ... |
| 1111101 | 0x7D | 1425 mV or 1225 mV |
| 1111110 | 0x7E | 1430 mV or 1230 mV |
| 1111111 | 0x7F | 1435 mV or 1235 mV |

### [0] SWB_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

- Description: SWB Output Threshold Low Side Voltage For Power Good Status
- Attribute: RW — Read/Write
- Default: 0 → -5% from the setting in Table 140, Register 0x23 [7:1]

| Code (bin) | Meaning |
|---|---|
| 0 | -5% from the setting in Table 140, Register 0x23 [7:1] |
| 1 | -7.5% from the setting in Table 140, Register 0x23 [7:1] |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 239, Register 0x47.
- NOTE 2: If required, the host must update the settings in register Table 140, Register 0x23 [0], Table 141, Register 0x24 [7:2] and Table 137, Register 0x20 [5:4] first prior to updating the settings in the register Table 140, Register 0x23 [7:1].
- NOTE 3: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care.
- NOTE 4: PMIC guarantees efficiency spec within a range of 1050 mV to 1160 mV.
- NOTE 5: After VR is enabled, the host may update this register to any new setting that it may desire. However to prevent false error trigger, the PMIC internally will increment the SWB output voltage setting by 5 mV at a time. The time it takes for PMIC to adjust the output voltage is 5 μs for each 5 mV increment. The host must wait sufficient time for PMIC to adjust to final value. As an example, if host adjusts the output voltage by 50 mV from the original value, the host must wait minimum of 50 μs before PMIC can guarantee the new output voltage. During this time, PMIC masks the PWR_GOOD output signal assertion to prevent any artificial error due to the crossing of the output voltage threshold setting. However, PMIC does assert PWR_GOOD output signal if there are any abnormal issues that triggers VR Disable command as described in Table 27. Further, PMIC does monitor PWR_GOOD input signal and executes power off config sequence registers if it is registered low when Table 155, Register 0x32 [5] = ‘1’.
- NOTE 6: Table 148, Register 0x2B [4] = ‘0’; 5 mV step size.
- NOTE 7: Table 148, Register 0x2B [4] = ‘1’; 5 mV step size

## R24 (0x24) — SWB_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING, SWB_OVER_VOLTAGE_THRESHOLD_SETTING, SWB_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING, SWB_OUTPUT_SOFT_STOP_TIME

Region: Host Region | Source: JESD301-5 Table 141, p.167

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWB_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING | RW | 01 |
| 5:4 | SWB_OVER_VOLTAGE_THRESHOLD_SETTING | RW | 10 |
| 3:2 | SWB_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING | RW | 00 |
| 1:0 | SWB_OUTPUT_SOFT_STOP_TIME | RW | 00 |

### [7:6] SWB_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING

- Description: SWB Output Threshold High Side Voltage For Power Good Status
- Attribute: RW — Read/Write
- Default: 01 → +7.5% from the setting in Table 140, Register 0x23 [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +5% from the setting in Table 140, Register 0x23 [7:1] |
| 01 | +7.5% from the setting in Table 140, Register 0x23 [7:1] |
| 10 | +10% from the setting in Table 140, Register 0x23 [7:1] |
| 11 | Reserved |

### [5:4] SWB_OVER_VOLTAGE_THRESHOLD_SETTING

- Description: SWB Output Regulator Threshold For Over Voltage Status[4]
- Attribute: RW — Read/Write
- Default: 10 → +12.5% from the setting in Table 140, Register 0x23 [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +7.5% from the setting in Table 140, Register 0x23 [7:1] |
| 01 | +10% from the setting in Table 140, Register 0x23 [7:1] |
| 10 | +12.5% from the setting in Table 140, Register 0x23 [7:1] |
| 11 | Reserved |

### [3:2] SWB_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING

- Description: SWB Output Regulator Threshold For Under Voltage Lockout Status
- Attribute: RW — Read/Write
- Default: 00 → -10% from the setting in Table 140, Register 0x23 [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | -10% from the setting in Table 140, Register 0x23 [7:1] |
| 01 | -12.5% from the setting in Table 140, Register 0x23 [7:1] |
| 10 | Reserved |
| 11 | Reserved |

### [1:0] SWB_OUTPUT_SOFT_STOP_TIME

- Description: SWB Output Regulator Soft Stop Time After VR Disable[5]
- Attribute: RW — Read/Write
- Default: 00 → 0.5 ms

| Code (bin) | Meaning |
|---|---|
| 00 | 0.5 ms |
| 01 | 1 ms |
| 10 | 2 ms |
| 11 | 4 ms |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 240, Register 0x48.
- NOTE 2: If required, the host must update the settings in register Table 140, Register 0x23 [0], Table 141, Register 0x24 [7:2] and Table 137, Register 0x20 [5:4] first prior to updating the settings in the register Table 140, Register 0x23 [7:1].
- NOTE 3: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care.
- NOTE 4: The setting for the Over Voltage must be higher than Power Good High Side Voltage threshold in Table 141, Register 0x24[7:6].
- NOTE 5: This is the time it takes for buck regulator to go from steady state voltage to 0 V.

## R25 (0x25) — SWC_VOLTAGE_SETTING, SWC_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

Region: Host Region | Source: JESD301-5 Table 142, p.168

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:1 | SWC_VOLTAGE_SETTING | RW | 011 1100 |
| 0 | SWC_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING | RW | 0 |

### [7:1] SWC_VOLTAGE_SETTING

- Description: SWC Output Regulator Voltage Setting[3],[4]
- Attribute: RW — Read/Write
- Default: 011 1100 → 1100 mV or 900 mV or 550 mV

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 0000000 | 0x00 | 800 mV[5] or 600 mV[6] or 400 mV[7] |
| 0000001 | 0x01 | 805 mV or 605 mV or 402.5 mV |
| 0000010 | 0x02 | 810 mV or 610 mV or 405 mV |
| ... | ... | ... |
| 0111100 | 0x3C | 1100 mV or 900 mV or 550 mV |
| ... | ... | ... |
| 1111101 | 0x7D | 1425 mV or 1225 mV or 712.5 mV |
| 1111110 | 0x7E | 1430 mV or 1230 mV or 715 mV |
| 1111111 | 0x7F | 1435 mV or 1235 mV or 717.5 mV |

### [0] SWC_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

- Description: SWC Output Threshold Low Side Voltage For Power Good Status
- Attribute: RW — Read/Write
- Default: 0 → -5% from the setting in Table 142, Register 0x25 [7:1]

| Code (bin) | Meaning |
|---|---|
| 0 | -5% from the setting in Table 142, Register 0x25 [7:1] |
| 1 | -7.5% from the setting in Table 142, Register 0x25 [7:1] |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 241, Register 0x49.
- NOTE 2: If required, the host must update the settings in register Table 142, Register 0x25 [0], Table 143, Register 0x26 [7:2] and Table 137, Register 0x20 [3:2] first prior to updating the settings in the register Table 142, Register 0x25 [7:1].
- NOTE 3: PMIC guarantees efficiency spec within a range of 1050 mV to 1160 mV.
- NOTE 4: After VR is enabled, the host may update this register to any new setting that it may desire. However to prevent false error trigger, the PMIC internally will increment the SWC output voltage setting by 5 mV at a time. The time it takes for PMIC to adjust the output voltage is 5 μs for each 5 mV increment. The host must wait sufficient time for PMIC to adjust to final value. As an example, if host adjusts the output voltage by 50 mV from the original value, the host must wait minimum of 50 μs before PMIC can guarantee the new output voltage. During this time, PMIC masks the PWR_GOOD output signal assertion to prevent any artificial error due to the crossing of the output voltage threshold setting. However, PMIC does assert PWR_GOOD output signal if there are any abnormal issues that triggers VR Disable command as described in Table 27. Further, PMIC does monitor PWR_GOOD input signal and executes power off config sequence registers if it is registered low when Table 155, Register 0x32 [5] = ‘1’.
- NOTE 5: Table 184, Register 0x11C [0] = ‘0’ and Table 148, Register 0x2B [3] = ‘0’; 5 mV step size.
- NOTE 6: Table 184, Register 0x11C [0] = ‘0’ and Table 148, Register 0x2B [3] = ‘1’; 5 mV step size
- NOTE 7: Table 184, Register 0x11C [0] = ‘1’ and Table 148, Register 0x2B [3] = ‘0’; 2.5 mV step size.

## R26 (0x26) — SWC_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING, SWC_OVER_VOLTAGE_THRESHOLD_SETTING, SWC_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING, SWC_OUTPUT_SOFT_STOP_TIME

Region: Host Region | Source: JESD301-5 Table 143, p.169

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWC_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING | RW | 01 |
| 5:4 | SWC_OVER_VOLTAGE_THRESHOLD_SETTING | RW | 10 |
| 3:2 | SWC_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING | RW | 00 |
| 1:0 | SWC_OUTPUT_SOFT_STOP_TIME | RW | 00 |

### [7:6] SWC_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING

- Description: SWC Output Threshold High Side Voltage For Power Good Status
- Attribute: RW — Read/Write
- Default: 01 → +7.5% from the setting in Table 142, Register 0x25 [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +5% from the setting in Table 142, Register 0x25 [7:1] |
| 01 | +7.5% from the setting in Table 142, Register 0x25 [7:1] |
| 10 | +10% from the setting in Table 142, Register 0x25 [7:1] |
| 11 | Reserved |

### [5:4] SWC_OVER_VOLTAGE_THRESHOLD_SETTING

- Description: SWC Output Regulator Threshold For Over Voltage Status[3]
- Attribute: RW — Read/Write
- Default: 10 → +12.5% from the setting in Table 142, Register 0x25 [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +7.5% from the setting in Table 142, Register 0x25 [7:1] |
| 01 | +10% from the setting in Table 142, Register 0x25 [7:1] |
| 10 | +12.5% from the setting in Table 142, Register 0x25 [7:1] |
| 11 | Reserved |

### [3:2] SWC_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING

- Description: SWC Output Regulator Threshold For Under Voltage Lockout Status
- Attribute: RW — Read/Write
- Default: 00 → -10% from the setting in Table 142, Register 0x25 [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | -10% from the setting in Table 142, Register 0x25 [7:1] |
| 01 | -12.5% from the setting in Table 142, Register 0x25 [7:1] |
| 10 | Reserved |
| 11 | Reserved |

### [1:0] SWC_OUTPUT_SOFT_STOP_TIME

- Description: SWC Output Regulator Soft Stop Time After VR Disable[4]
- Attribute: RW — Read/Write
- Default: 00 → 0.5 ms

| Code (bin) | Meaning |
|---|---|
| 00 | 0.5 ms |
| 01 | 1 ms |
| 10 | 2 ms |
| 11 | 4 ms |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 242, Register 0x4A.
- NOTE 2: If required, the host must update the settings in register Table 142, Register 0x25 [0], Table 143, Register 0x26 [7:2] and Table 137, Register 0x20 [3:2] first prior to updating the settings in the register Table 142, Register 0x25 [7:1].
- NOTE 3: The setting for the Over Voltage must be higher than Power Good High Side Voltage threshold in Table 143, Register 0x26[7:6].
- NOTE 4: This is the time it takes for buck regulator to go from steady state voltage to 0 V.

## R27 (0x27) — SWD_VOLTAGE_SETTING, SWD_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

Region: Host Region | Source: JESD301-5 Table 144, p.170

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:1 | SWD_VOLTAGE_SETTING | RW | 011 1100 |
| 0 | SWD_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING | RW | 0 |

### [7:1] SWD_VOLTAGE_SETTING

- Description: SWD Output Regulator Voltage Setting[3],[4]
- Attribute: RW — Read/Write
- Default: 011 1100 → 1800 mV or 2500 mV

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 0000000 | 0x00 | 1500 mV[5] or 2200 mV[6] |
| 0000001 | 0x01 | 1505 mV or 2205 mV |
| 0000010 | 0x02 | 1510 mV or 2210 mV |
| ... | ... | ... |
| 0111100 | 0x3C | 1800 mV or 2500 mV |
| ... | ... | ... |
| 1111101 | 0x7D | 2125 mV or 2825 mV |
| 1111110 | 0x7E | 2130 mV or 2830 mV |
| 1111111 | 0x7F | 2135 mV or 2835 mV |

### [0] SWD_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

- Description: SWD Output Threshold Low Side Voltage For Power Good Status
- Attribute: RW — Read/Write
- Default: 0 → -5% from the setting in Table 144, Register 0x27 [7:1]

| Code (bin) | Meaning |
|---|---|
| 0 | -5% from the setting in Table 144, Register 0x27 [7:1] |
| 1 | -7.5% from the setting in Table 144, Register 0x27 [7:1] |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 243, Register 0x4B.
- NOTE 2: If required, the host must update the settings in register Table 144, Register 0x27 [0], Table 145, Register 0x28 [7:2] and Table 137, Register 0x20 [1:0] first prior to updating the settings in the register Table 144, Register 0x27 [7:1].
- NOTE 3: PMIC guarantees efficiency spec within a range of 1750 mV to 1850 mV.
- NOTE 4: After VR is enabled, the host may update this register to any new setting that it may desire. However to prevent false error trigger, the PMIC internally will increment the SWD output voltage setting by 5 mV at a time. The time it takes for PMIC to adjust the output voltage is 5 μs for each 5 mV increment. The host must wait sufficient time for PMIC to adjust to final value. As an example, if host adjusts the output voltage by 50 mV from the original value, the host must wait minimum of 50 μs before PMIC can guarantee the new output voltage. During this time, PMIC masks the PWR_GOOD output signal assertion to prevent any artificial error due to the crossing of the output voltage threshold setting. However, PMIC does assert PWR_GOOD output signal if there are any abnormal issues that triggers VR Disable command as described in Table 27. Further, PMIC does monitor PWR_GOOD input signal and executes power off config sequence registers if it is registered low when Table 155, Register 0x32 [5] = ‘1’.
- NOTE 5: Table 148, Register 0x2B [0] = ‘0’; 5 mV step size.
- NOTE 6: Table 148, Register 0x2B [0] = ‘1’; 5 mV step size.

## R28 (0x28) — SWD_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING, SWD_OVER_VOLTAGE_THRESHOLD_SETTING, SWD_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING, SWD_OUTPUT_SOFT_STOP_TIME

Region: Host Region | Source: JESD301-5 Table 145, p.171

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWD_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING | RW | 01 |
| 5:4 | SWD_OVER_VOLTAGE_THRESHOLD_SETTING | RW | 10 |
| 3:2 | SWD_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING | RW | 00 |
| 1:0 | SWD_OUTPUT_SOFT_STOP_TIME | RW | 00 |

### [7:6] SWD_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING

- Description: SWD Output Threshold High Side Voltage For Power Good Status
- Attribute: RW — Read/Write
- Default: 01 → +7.5% from the setting in Table 144, Register 0x27 [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +5% from the setting in Table 144, Register 0x27 [7:1] |
| 01 | +7.5% from the setting in Table 144, Register 0x27 [7:1] |
| 10 | +10% from the setting in Table 144, Register 0x27 [7:1] |
| 11 | Reserved |

### [5:4] SWD_OVER_VOLTAGE_THRESHOLD_SETTING

- Description: SWD Output Regulator Threshold For Over Voltage Status[3]
- Attribute: RW — Read/Write
- Default: 10 → +12.5% from the setting in Table 144, Register 0x27 [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +7.5% from the setting in Table 144, Register 0x27 [7:1] |
| 01 | +10% from the setting in Table 144, Register 0x27 [7:1] |
| 10 | +12.5% from the setting in Table 144, Register 0x27 [7:1] |
| 11 | Reserved |

### [3:2] SWD_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING

- Description: SWD Output Regulator Threshold For Under Voltage Lockout Status
- Attribute: RW — Read/Write
- Default: 00 → -10% from the setting in Table 144, Register 0x27 [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | -10% from the setting in Table 144, Register 0x27 [7:1] |
| 01 | -12.5% from the setting in Table 144, Register 0x27 [7:1] |
| 10 | Reserved |
| 11 | Reserved |

### [1:0] SWD_OUTPUT_SOFT_STOP_TIME

- Description: SWD Output Regulator Soft Stop Time After VR Disable[4]
- Attribute: RW — Read/Write
- Default: 00 → 1 ms

| Code (bin) | Meaning |
|---|---|
| 00 | 1 ms |
| 01 | 2 ms |
| 10 | 4 ms |
| 11 | 8 ms |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 244, Register 0x4C.
- NOTE 2: If required, the host must update the settings in register Table 144, Register 0x27 [0], Table 145, Register 0x28 [7:2] and Table 137, Register 0x20 [1:0] first prior to updating the settings in the register Table 144, Register 0x27 [7:1].
- NOTE 3: The setting for the Over Voltage must be higher than Power Good High Side Voltage threshold in Table 145, Register 0x28[7:6].
- NOTE 4: This is the time it takes for buck regulator to go from steady state voltage to 0 V.

## R29 (0x29) — SWA_MODE_SELECT, SWA_SWITCHING_FREQ, SWB_MODE_SELECT, SWB_SWITCHING_FREQ

Region: Host Region | Source: JESD301-5 Table 146, p.172

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWA_MODE_SELECT | RW | 10 |
| 5:4 | SWA_SWITCHING_FREQ | RW | 01 |
| 3:2 | SWB_MODE_SELECT | RW | 10 |
| 1:0 | SWB_SWITCHING_FREQ | RW | 01 |

### [7:6] SWA_MODE_SELECT

- Description: SWA Output Regulator Mode Selection
- Attribute: RW — Read/Write
- Default: 10 → COT; DCM (Constant on Time; Discontinuous Current Mode)

| Code (bin) | Meaning |
|---|---|
| 00 | Reserved |
| 01 | Reserved |
| 10 | COT; DCM (Constant on Time; Discontinuous Current Mode) |
| 11 | COT; Forced CCM (Constant on Time; Continuous Current Mode) |

### [5:4] SWA_SWITCHING_FREQ

- Description: SWA Output Regulator Switching Frequency
- Attribute: RW — Read/Write
- Default: 01 → 750 KHz

| Code (bin) | Meaning |
|---|---|
| 00 | 500 KHz |
| 01 | 750 KHz |
| 10 | Reserved |
| 11 | Reserved |

### [3:2] SWB_MODE_SELECT

- Description: SWB Output Regulator Mode Selection[3]
- Attribute: RW — Read/Write
- Default: 10 → COT; DCM (Constant on Time; Discontinuous Current Mode)

| Code (bin) | Meaning |
|---|---|
| 00 | Reserved |
| 01 | Reserved |
| 10 | COT; DCM (Constant on Time; Discontinuous Current Mode) |
| 11 | COT; Forced CCM (Constant on Time; Continuous Current Mode) |

### [1:0] SWB_SWITCHING_FREQ

- Description: SWB Output Regulator Switching Frequency[3]
- Attribute: RW — Read/Write
- Default: 01 → 750 KHz

| Code (bin) | Meaning |
|---|---|
| 00 | 500 KHz |
| 01 | 750 KHz |
| 10 | Reserved |
| 11 | Reserved |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 245, Register 0x4D.
- NOTE 2: If required, the host must adjust this register first before issuing VR Enable command in Table 155, Register 0x32 [7].
- NOTE 3: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care.

## R2A (0x2A) — SWC_MODE_SELECT, SWC_SWITCHING_FREQ, SWD_MODE_SELECT, SWD_SWITCHING_FREQ

Region: Host Region | Source: JESD301-5 Table 147, p.173

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWC_MODE_SELECT | RW | 10 |
| 5:4 | SWC_SWITCHING_FREQ | RW | 01 |
| 3:2 | SWD_MODE_SELECT | RW | 10 |
| 1:0 | SWD_SWITCHING_FREQ | RW | 01 |

### [7:6] SWC_MODE_SELECT

- Description: Switch Node C Output Regulator Mode Selection
- Attribute: RW — Read/Write
- Default: 10 → COT; DCM (Constant on Time; Discontinuous Current Mode)

| Code (bin) | Meaning |
|---|---|
| 00 | Reserved |
| 01 | Reserved |
| 10 | COT; DCM (Constant on Time; Discontinuous Current Mode) |
| 11 | COT; Forced CCM (Constant on Time; Continuous Current Mode) |

### [5:4] SWC_SWITCHING_FREQ

- Description: Switch Node C Output Regulator Switching Frequency[3]
- Attribute: RW — Read/Write
- Default: 01 → 750 KHz

| Code (bin) | Meaning |
|---|---|
| 00 | 500 KHz |
| 01 | 750 KHz |
| 10 | Reserved |
| 11 | Reserved |

### [3:2] SWD_MODE_SELECT

- Description: Switch Node D Output Regulator Mode Selection
- Attribute: RW — Read/Write
- Default: 10 → COT; DCM (Constant on Time; Discontinuous Current Mode)

| Code (bin) | Meaning |
|---|---|
| 00 | Reserved |
| 01 | Reserved |
| 10 | COT; DCM (Constant on Time; Discontinuous Current Mode) |
| 11 | COT; Forced CCM (Constant on Time; Continuous Current Mode) |

### [1:0] SWD_SWITCHING_FREQ

- Description: Switch Node D Output Regulator Switching Frequency
- Attribute: RW — Read/Write
- Default: 01 → 750 KHz

| Code (bin) | Meaning |
|---|---|
| 00 | Reserved |
| 01 | 750 KHz |
| 10 | 1000 KHz |
| 11 | Reserved |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 246, Register 0x4E.
- NOTE 2: If required, the host must adjust this register first before issuing VR Enable command in Table 155, Register 0x32 [7].

## R2B (0x2B) — VOUT_1.8V_VOLTAGE_SETTING, SWA_VOLTAGE_RANGE, SWB_VOLTAGE_RANGE, SWC_VOLTAGE_RANGE, VOUT_1.0V_VOLTAGE_SETTING, SWD_VOLTAGE_RANGE

Region: Host Region | Source: JESD301-5 Table 148, p.174

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | VOUT_1.8V_VOLTAGE_SETTING | RW | 01 |
| 5 | SWA_VOLTAGE_RANGE | RW | 0 |
| 4 | SWB_VOLTAGE_RANGE | RW | 0 |
| 3 | SWC_VOLTAGE_RANGE | RW | 0 |
| 2:1 | VOUT_1.0V_VOLTAGE_SETTING | RW | 01 |
| 0 | SWD_VOLTAGE_RANGE | RW | 0 |

### [7:6] VOUT_1.8V_VOLTAGE_SETTING

- Description: VOUT 1.8 V LDO Output Voltage Setting[3]
- Attribute: RW — Read/Write
- Default: 01 → 1.8 V

| Code (bin) | Meaning |
|---|---|
| 00 | 1.7 V |
| 01 | 1.8 V |
| 10 | 1.9 V |
| 11 | Reserved |

### [5] SWA_VOLTAGE_RANGE

- Description: SWA Output Voltage Range Selection[4]
- Attribute: RW — Read/Write
- Default: 0 → Range: 800 mV to 1435 mV for SWA; 5 mV step size

| Code (bin) | Meaning |
|---|---|
| 0 | Range: 800 mV to 1435 mV for SWA; 5 mV step size |
| 1 | Range: 600 mV to 1235 mV for SWA; 5 mV step size |

### [4] SWB_VOLTAGE_RANGE

- Description: SWB Output Voltage Range Selection[5],[6]
- Attribute: RW — Read/Write
- Default: 0 → Range: 800 mV to 1435 mV for SWB; 5 mV step size

| Code (bin) | Meaning |
|---|---|
| 0 | Range: 800 mV to 1435 mV for SWB; 5 mV step size |
| 1 | Range: 600 mV to 1235 mV for SWB; 5 mV step size |

### [3] SWC_VOLTAGE_RANGE

- Description: SWC Output Voltage Range Selection[7]. The MSB bit Table 184, Register 0x11C [0] plus this LSB bit Table 148, Register 0x2B [3] makes 2 bit encoding as following:
- Attribute: RW — Read/Write
- Default: 0
- Note: the codes below are wider than this 1-bit field; the encoding combines bits from more than one field/register (see Description).

| Code (bin) | Meaning |
|---|---|
| 00 | Range: 800 mV to 1435 mV for SWC; 5 mV step size |
| 01 | Range: 600 mV to 1235 mV for SWC; 5 mV step size |
| 10 | Range: 400 mV to 717.5 mV for SWC; 2.5 mV step size |
| 11 | Reserved |

### [2:1] VOUT_1.0V_VOLTAGE_SETTING

- Description: VOUT 1.0 V LDO Voltage Setting[8]
- Attribute: RW — Read/Write
- Default: 01 → 1.0 V

| Code (bin) | Meaning |
|---|---|
| 00 | 0.9 V |
| 01 | 1.0 V |
| 10 | 1.1 V |
| 11 | 1.2 V |

### [0] SWD_VOLTAGE_RANGE

- Description: SWD Output Voltage Range Selection[9]
- Attribute: RW — Read/Write
- Default: 0 → Range: 1500 mV to 2135 mV for SWD; 5 mV step size

| Code (bin) | Meaning |
|---|---|
| 0 | Range: 1500 mV to 2135 mV for SWD; 5 mV step size |
| 1 | Range: 2200 mV to 2835 mV for SWD; 5 mV step size |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 249, Register 0x51.
- NOTE 2: If required, the host must adjust this register first before issuing VR Enable command in Table 155, Register 0x32 [7]. The host must also wait minimum of 5 μs after the adjustment before issuing VR Enable command.
- NOTE 3: The VOUT_1.8V Power Good threshold in register Table 131, Register 0x1A [2] is always fixed regardless of the setting in this register.
- NOTE 4: Range and resolution selection applies to register Table 138, Register 0x21 [7:1].
- NOTE 5: Range and resolution selection applies to register Table 140, Register 0x23 [7:1].
- NOTE 6: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care.
- NOTE 7: Range selection applies to registers Table 142, Register 0x25 [7:1].
- NOTE 8: If required, the host must adjust this register one step at a time (0.1 V increment or decrement) to prevent false trigger of power good status and PWR_GOOD pin assertion. In other words, host should not increment or decrement 0.2 V or 0.3 V from its current setting.
- NOTE 9: Range and resolution selection applies to register Table 144, Register 0x27 [7:1].

## R2C (0x2C) — SWA_OUTPUT_SOFT_START_TIME, SWB_OUTPUT_SOFT_START_TIME

Region: Host Region | Source: JESD301-5 Table 149, p.175

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:5 | SWA_OUTPUT_SOFT_START_TIME | RW | 001 |
| 4 | RESERVED | RV | 0 |
| 3:1 | SWB_OUTPUT_SOFT_START_TIME | RW | 001 |
| 0 | RESERVED | RV | 0 |

### [7:5] SWA_OUTPUT_SOFT_START_TIME

- Description: SWA Output Regulator Soft Start Time After VR Enable[3]
- Attribute: RW — Read/Write
- Default: 001 → 2 ms

| Code (bin) | Meaning |
|---|---|
| 000 | 1 ms |
| 001 | 2 ms |
| 010 | 4 ms |
| 011 | 6 ms |
| ... | ... |
| 111 | 14 ms |

### [4] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [3:1] SWB_OUTPUT_SOFT_START_TIME

- Description: SWB Output Regulator Soft Start Time After VR Enable[3],[4]
- Attribute: RW — Read/Write
- Default: 001 → 2 ms

| Code (bin) | Meaning |
|---|---|
| 000 | 1 ms |
| 001 | 2 ms |
| 010 | 4 ms |
| 011 | 6 ms |
| ... | ... |
| 111 | 14 ms |

### [0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 261, Register 0x5D.
- NOTE 2: If required, the host must adjust this register first before issuing VR Enable command in Table 155, Register 0x32 [7].
- NOTE 3: This is the time it takes for buck regulator to go from 0 V to steady state voltage (the actual voltage varies based on pre- programmed voltage).
- NOTE 4: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care.

## R2D (0x2D) — SWC_OUTPUT_SOFT_START_TIME, SWD_OUTPUT_SOFT_START_TIME

Region: Host Region | Source: JESD301-5 Table 150, p.176

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:5 | SWC_OUTPUT_SOFT_START_TIME | RW | 001 |
| 4 | RESERVED | RV | 0 |
| 3:1 | SWD_OUTPUT_SOFT_START_TIME | RW | 001 |
| 0 | RESERVED | RV | 0 |

### [7:5] SWC_OUTPUT_SOFT_START_TIME

- Description: SWC Output Regulator Soft Start Time After VR Enable[3]
- Attribute: RW — Read/Write
- Default: 001 → 2 ms

| Code (bin) | Meaning |
|---|---|
| 000 | 1 ms |
| 001 | 2 ms |
| 010 | 4 ms |
| 011 | 6 ms |
| ... | ... |
| 111 | 14 ms |

### [4] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [3:1] SWD_OUTPUT_SOFT_START_TIME

- Description: SWD Output Regulator Soft Start Time After VR Enable3
- Attribute: RW — Read/Write
- Default: 001 → 2 ms

| Code (bin) | Meaning |
|---|---|
| 000 | 1 ms |
| 001 | 2 ms |
| 010 | 4 ms |
| 011 | 6 ms |
| ... | ... |
| 111 | 14 ms |

### [0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 262, Register 0x5E.
- NOTE 2: If required, the host must adjust this register first before issuing VR Enable command in Table 155, Register 0x32 [7].
- NOTE 3: This is the time it takes for buck regulator to go from 0 V to steady state voltage (the actual voltage varies based on pre- programmed voltage)

## R2E (0x2E) — PMIC_SHUTDOWN_TEMPERATURE_THRESHOLD

Region: Host Region | Source: JESD301-5 Table 151, p.176

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:3 | RESERVED | RV | 0 |
| 2:0 | PMIC_SHUTDOWN_TEMPERATURE_THRESHOLD | RW | 100 |

### [7:3] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [2:0] PMIC_SHUTDOWN_TEMPERATURE_THRESHOLD

- Description: PMIC Shutdown Temperature Threshold
- Attribute: RW — Read/Write
- Default: 100 → PMIC Temperature > 145 0C

| Code (bin) | Meaning |
|---|---|
| 000 | PMIC Temperature > 105 0C |
| 001 | PMIC Temperature > 115 0C |
| 010 | PMIC Temperature > 125 0C |
| 011 | PMIC Temperature > 135 0C |
| 100 | PMIC Temperature > 145 0C |
| 101 | Reserved |
| 110 | Reserved |
| 111 | Reserved |

## R2F (0x2F) — VIN_MGMT_INPUT_SUPPLY_SWITCHOVER_THRESHOLD, SWA_REGULATOR_CONTROL, SWB_REGULATOR_CONTROL, SWC_REGULATOR_CONTROL, SWD_REGULATOR_CONTROL, WRITE_PROTECT_FUNCTION_CONTROL, MASK_BITS_REGISTER_CONTROL

Region: Host Region | Source: JESD301-5 Table 152, p.177

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | VIN_MGMT_INPUT_SUPPLY_SWITCHOVER_THRESHOLD | RW | 0 |
| 6 | SWA_REGULATOR_CONTROL | RW | 0 |
| 5 | SWB_REGULATOR_CONTROL | RW | 0 |
| 4 | SWC_REGULATOR_CONTROL | RW | 0 |
| 3 | SWD_REGULATOR_CONTROL | RW | 0 |
| 2 | WRITE_PROTECT_FUNCTION_CONTROL | RW | 0 |
| 1:0 | MASK_BITS_REGISTER_CONTROL | RW | 10 |

### [7] VIN_MGMT_INPUT_SUPPLY_SWITCHOVER_THRESHOLD

- Description: VIN_Mgmt Input Supply Switchover Voltage Threshold to VIN_Bulk Input Supply
- Attribute: RW — Read/Write
- Default: 0 → Vendor Specific[1]

| Code (bin) | Meaning |
|---|---|
| 0 | Vendor Specific[1] |
| 1 | Reserved |

### [6] SWA_REGULATOR_CONTROL

- Description: Disable SWA Regulator Output[2],[3]
- Attribute: RW — Read/Write
- Default: 0 → Disable Switch Node A Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Disable Switch Node A Output Regulator |
| 1 | Enable Switch Node A Output Regulator |

### [5] SWB_REGULATOR_CONTROL

- Description: Disable SWB Regulator Output[2],[3],[4]
- Attribute: RW — Read/Write
- Default: 0 → Disable Switch Node B Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Disable Switch Node B Output Regulator |
| 1 | Enable Switch Node B Output Regulator |

### [4] SWC_REGULATOR_CONTROL

- Description: Disable SWC Regulator Output[2],[3]
- Attribute: RW — Read/Write
- Default: 0 → Disable Switch Node C Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Disable Switch Node C Output Regulator |
| 1 | Enable Switch Node C Output Regulator |

### [3] SWD_REGULATOR_CONTROL

- Description: Disable SWD Regulator Output[2],[3]
- Attribute: RW — Read/Write
- Default: 0 → Disable Switch Node D Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Disable Switch Node D Output Regulator |
| 1 | Enable Switch Node D Output Regulator |

### [2] WRITE_PROTECT_FUNCTION_CONTROL

- Description: PMIC write-protect Function Control[5]
- Attribute: RW — Read/Write
- Default: 0 → CAMP input signal determines the write-protect Function as noted in clause 6.9.1

| Code (bin) | Meaning |
|---|---|
| 0 | CAMP input signal determines the write-protect Function as noted in clause 6.9.1 |
| 1 | Write-protect Function is disabled; All register write access is allowed independent of CAMP input signal as noted in clause 6.9.1. |

### [1:0] MASK_BITS_REGISTER_CONTROL

- Description: Mask Bits Register Control[6]
- Attribute: RW — Read/Write
- Default: 10 → Mask GSI_n and PWR_GOOD Signals (neither PWR_GOOD assert or GSI_n signal will assert)

| Code (bin) | Meaning |
|---|---|
| 00 | Mask GSI_n Signal Only (PWR_GOOD Signal will assert) |
| 01 | Mask PWR_GOOD Signal Only (GSI_n Signal will assert) |
| 10 | Mask GSI_n and PWR_GOOD Signals (neither PWR_GOOD assert or GSI_n signal will assert) |
| 11 | Reserved |

**Notes**

- NOTE 1: The VIN_Mgmt input switchover voltage threshold range is vendor specific and can vary between 2.6 V to 2.9 V max.
- NOTE 2: This bit must be used only after power up sequence (after VR Enable command). At first power up, PMIC automatically updates the status of this register to ‘1’ after VR Enable command. When VR Enable command is registered, the PMIC updates this register based on Power On Sequence Configuration (0 to 5) setting. If enabled in Power On Sequence Configuration 0 to 5 registers, only then, under non write-protect mode of operation, the PMIC’s output regulator can be disabled by clearing this bit and they can be re-enabled again by setting this bit. The PMIC does not alter its Power Good output signal and keeps it asserted High. If any regulator is not enabled in Power on Sequence Configuration 0 to 5, it cannot be enabled using this register. For example, if only SWA is enabled and SWB, SWC,SWD, SWE and SWF are not enabled in Table 232, Register 0x40 [7:0] to Table 236, Register 0x44 [7:0],Table 265, Register 0x61 [7:0] then only SWA can be disabled and then re-enabled again but SWB, SWC,SWD, SWE and SWF cannot be enabled using Table 152, Register 0x2F [6:3], Table 191, Register 0x123 [1:0].
- NOTE 3: In non write-protect mode, after VR enable command, if any output regulators are disabled by clearing Table 152, Register 0x2F [6:3],Table 191, Register 0x123 [1:0] and then if host issues VR Disable command or PMIC internally triggers VR Disable command, the PMIC keeps the disabled output regulator in Table 152, Register 0x2F[6:3],Table 191, Register 0x123 [1:0] off and remaining output regulators are disabled by following the Power Off Sequence Configuration 0 to 5 settings.
- NOTE 4: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care.
- NOTE 5: At first power on, this register is automatically configured identically by the PMIC on its own as Table 263, Register 0x5F [7].
- NOTE 6: Applies to Mask Registers Table 126, Register 0x15 [7,5:0], Table 127, Register 0x16 [7:0], Table 128, Register 0x17 [7:2], Table 129, Register 0x18 [7:0], Table 130, Register 0x19 [4:2],Table 180, Register 0x114 [7:0] and Table 181, Register 0x115 [7:6]. when any one or more Mask registers are set to ‘1’. If all Mask registers are configured as ‘0’, the setting in this register (Table 152, Register 0x2F [1:0]) does not matter.

## R30 (0x30) — ADC_ENABLE, ADC_SELECT, REGISTER_ADDRESSING_MODE, ADC_REGISTER_UPDATE_FREQUENCY

Region: Host Region | Source: JESD301-5 Table 153, p.179

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | ADC_ENABLE | RW | 0 |
| 6:3 | ADC_SELECT | RW | 0 |
| 2 | REGISTER_ADDRESSING_MODE | RW | 0 |
| 1:0 | ADC_REGISTER_UPDATE_FREQUENCY | RW | 0 |

### [7] ADC_ENABLE

- Description: Enable ADC (Analog to Digital Conversion)
- Attribute: RW — Read/Write
- Default: 0 → Disable[1]

| Code (bin) | Meaning |
|---|---|
| 0 | Disable[1] |
| 1 | Enable |

### [6:3] ADC_SELECT

- Description: Input Selection for ADC Readout[2] All other encodings are reserved.
- Attribute: RW — Read/Write
- Default: 0

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 0000 | 0x0 | SWA Output Voltage |
| 0001 | 0x1 | SWB Output Voltage[3] |
| 0010 | 0x2 | SWC Output Voltage |
| 0011 | 0x3 | SWD Output Voltage |
| 0100 | 0x4 | SWE Output Voltage[3] |
| 0101 | 0x5 | VIN_Bulk Input Voltage |
| 0110 | 0x6 | VIN_Mgmt Input Voltage |
| 0111 | 0x7 | VBias1 Output Voltage[4] |
| 1000 | 0x8 | VOUT_1.8V Output Voltage |
| 1001 | 0x9 | VOUT_1.0V Output Voltage |
| 1010 | 0xA | SWF Output Voltage[5] |
| 1011 | 0xB | VBias2 Output Voltage[4] |

### [2] REGISTER_ADDRESSING_MODE

- Description: Register Addressing for I2C and I3C Protocol[6]
- Attribute: RW — Read/Write
- Default: 0 → 1 Byte address; Configuration register space is limited to first 256 Bytes

| Code (bin) | Meaning |
|---|---|
| 0 | 1 Byte address; Configuration register space is limited to first 256 Bytes |
| 1 | 2 Byte address; Configuration register space is up to 64K Bytes |

### [1:0] ADC_REGISTER_UPDATE_FREQUENCY

- Description: ADC Current or Power Measurement Update Frequency[7],[8]
- Attribute: RW — Read/Write
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 00 | 1 ms |
| 01 | 2 ms |
| 10 | 4 ms |
| 11 | 8 ms |

**Notes**

- NOTE 1: Disables the ADC function completely. Applies to voltage readout in Table 154, Register 0x31 [7:0] as well as current or power readout in Table 117, Register 0x0C [7:0], Table 118, Register 0x0D [5:0], Table 119, Register 0x0E [5:0] and Table 120, Register 0x0F [5:0]. Does not apply to thermal sensor temperature readout in Table 157, Register 0x33 [7:5] as well as high temperature warning and critical temperature shutdown.
- NOTE 2: The host shall wait minimum of 9 ms delay after the input selection for ADC readout and the actual readout from Table 154, Register 0x31 to get the latest reading
- NOTE 3: Only applicable if Table 247, Register 0x4F [5,0] = ‘00’. For any other setting in Table 247, Register 0x4F [5,0], this encoding does not apply and it is a don’t care.
- NOTE 4: PMIC may implement only one VBIAS LDO output regulator or two VBIAS LDO output regulators. If only one VBIAS LDO output regulator is used, VBIAS1 code (0111) should be used to read out the output LDO voltage status. If two VBIAS LDO output regulators are used, both VBIAS1 (0111) and VBIAS2 (1011) can be used to read out the output LDO voltage status individually.
- NOTE 5: Only applicable if Table 247, Register 0x4F [6] = ‘0’. For any other setting in Table 247, Register 0x4F [6], this encoding does not apply and it is a don’t care.
- NOTE 6: When there is a change in addressing mode, STOP operation is required on I2C or I3C bus.
- NOTE 7: For average output current or power measurement in registers Table 117, Register 0x0C [7:0] to Table 120, Register 0x0F [7:0] or Table 167, Register 0x100 [7:0] to Table 174, Register 0x107 [7:0].
- NOTE 8: This register represents how often the registers are updated. The internal sampling rate is vendor specific.

## R31 (0x31) — ADC_READ

Region: Host Region | Source: JESD301-5 Table 154, p.180

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | ADC_READ | RO | 0 |

### [7:0] ADC_READ

- Description: ADC Output Voltage Reading[1](Applies to SW[A:F], VOUT_1.8V, VOUT_1.0V, VIN_Mgmt)
- Attribute: RO — Read Only (writes have no effect)
- Default: 0

**When: ADC Output Voltage Reading[1](Applies to SW[A:F], VOUT_1.8V, VOUT_1.0V, VIN_Mgmt)**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | 15 mV |
| 00000010 | 0x02 | 30 mV |
| ... | ... | ... |
| 11111111 | 0xFF | ≥ 3825 mV |

**When: ADC Output Voltage Reading[2] (Applies to VIN_Bulk Input Voltage)**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | 70 mV |
| 00000010 | 0x02 | 140 mV |
| ... | ... | ... |
| 11111111 | 0xFF | ≥ 17850 mV |

**When: ADC Output Voltage Reading[3] (Applies to VBias1 or VBias2 Output Voltage)**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | 25 mV |
| 00000010 | 0x02 | 50 mV |
| ... | ... | ... |
| 11111111 | 0xFF | ≥ 6375 mV |

**Notes**

- NOTE 1: Only valid when Table 153, Register 0x30 [6:3] = ‘0000’ or ‘0001’ or ‘0010’ or ‘0011’ or ‘0100’ or ‘1010’ or ‘0110’ or ‘1000’ or ‘1001’.
- NOTE 2: Only valid when Table 153, Register 0x30 [6:3] = ‘0101’.
- NOTE 3: Only valid when Table 153, Register 0x30 [6:3] = ‘0111’ or ‘1011’.

## R32 (0x32) — VR_ENABLE, MANAGEMENT_INTERFACE_SELECTION, EXECUTE_VR_ENABLE_CONTROL, EXECUTE_CAMP_FAIL_N_FUNCTION_CONTROL, CAMP_PWR_GOOD_OUTPUT_SIGNAL_CONTROL, ADC_ACCURACY_STEP_SIZE

Region: Host Region | Source: JESD301-5 Table 155, p.181

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | VR_ENABLE | RW | 0 |
| 6 | MANAGEMENT_INTERFACE_SELECTION | RO | 0 |
| 5 | EXECUTE_VR_ENABLE_CONTROL | RW | 1 |
| 4 | EXECUTE_CAMP_FAIL_N_FUNCTION_CONTROL | RW | 0 |
| 3 | CAMP_PWR_GOOD_OUTPUT_SIGNAL_CONTROL | RW | 0 |
| 2 | RESERVED | RV | 0 |
| 1:0 | ADC_ACCURACY_STEP_SIZE | RW | 00 |

### [7] VR_ENABLE

- Description: PMIC Enable[1],[2],[3],[4],[5],[6]
- Attribute: RW — Read/Write
- Default: 0 → PMIC Disable

| Code (bin) | Meaning |
|---|---|
| 0 | PMIC Disable |
| 1 | PMIC Enable |

### [6] MANAGEMENT_INTERFACE_SELECTION

- Description: PMIC Management Bus Interface Protocol Selection[7]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → I2C Protocol (Max speed 1 MHz)

| Code (bin) | Meaning |
|---|---|
| 0 | I2C Protocol (Max speed 1 MHz) |
| 1 | I3C Basic Protocol |

### [5] EXECUTE_VR_ENABLE_CONTROL

- Description: PMIC VR Enable Command Execution Control over I2C/I3C Bus or VR_OE or Auto Power On[4],[5],[6]
- Attribute: RW — Read/Write
- Default: 1 → Execute VR Enable Command

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Execute VR Enable Command; i.e., ignore bit [7] = ‘1’ and keep it as ‘0’. |
| 1 | Execute VR Enable Command |

### [4] EXECUTE_CAMP_FAIL_N_FUNCTION_CONTROL

- Description: PMIC CAMP Fail_n function (Transition from High to Low) Control[8]
- Attribute: RW — Read/Write
- Default: 0 → Execute VR Disable Command

| Code (bin) | Meaning |
|---|---|
| 0 | Execute VR Disable Command |
| 1 | Do Not Execute VR Disable Command |

### [3] CAMP_PWR_GOOD_OUTPUT_SIGNAL_CONTROL

- Description: PMIC CAMP PWR_GOOD Output Signal Control
- Attribute: RW — Read/Write
- Default: 0 → PMIC controls PWR_GOOD output on its own based on internal status

| Code (bin) | Meaning |
|---|---|
| 0 | PMIC controls PWR_GOOD output on its own based on internal status |
| 1 | PWR_GOOD Output Float[9] |

### [2] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [1:0] ADC_ACCURACY_STEP_SIZE

- Description: ADC Accuracy Step Size[10] All other encodings are reserved
- Attribute: RW — Read/Write
- Default: 00 → 125 mA or 125 mW[11]

| Code (bin) | Meaning |
|---|---|
| 00 | 125 mA or 125 mW[11] |
| 01 | 31.25 mA or 31.25 mW[12] |

**Notes**

- NOTE 1: The PMIC updates this bit when VR_OE signal transitions to high or when host issues VR Enable command over I2C/I3C Basic Bus; whichever comes first. PMIC also updates this bit when VR_OE signal transitions to low or when host issues VR Disable command over I2C/I3C Basic bus in programmable mode; whichever comes first. Further, PMIC updates this bit when CAMP input is low (if Table 155, Register 0x32 [4] = ‘0’) or when PMIC internally generates VR Disable command due to fault condition regardless of PMIC’s VR_OE signal.
- NOTE 2: Host sets this bit at first power on. After this bit is set, the PMIC executes Power On Sequence configuration 0 (Table 232, Register 0x40) to Power On Sequence configuration 4 (Table 236, Register 0x44) and Power On Sequence configuration 5 (Table 265, Register 0x61) registers.
- NOTE 3: The host shall ensure that prior to issuing VR Enable command, there is no pending IBI interrupt (i.e., Table 115, Register 0x0A [1] = ‘1’) status. After host issues VR Enable command, the PMIC may NACK any I2C or I3C Basic bus transaction by host until tPMIC_PWR_GOOD_OUT timing parameter is satisfied. The host shall not access any device specific registers or issue any CCCs until tPMIC_PWR_GOOD_OUT parameter is satisfied. The PMIC device may request for an IBI during power up sequence (i.e., during tPMIC_PWR_GOOD_OUT time) if there is any event.
- NOTE 4: After host issues VR Enable command, the PMIC may NACK any I2C or I3C Basic bus transactions by host until tPMIC_PWR_GOOD_OUT timing parameter is satisfied.
- NOTE 5: Once Table 155, Register 0x32 [7] is set to ‘1’ via VR Enable command, the subsequent write to register Table 155, Register 0x32 [5] = ‘0’ is ignored by the PMIC. If there is a simultaneous write to register Table 155, Register 0x32 [7,5] = ‘10’, the PMIC prioritizes bit [5] and does not execute VR Enable command.
- NOTE 6: See Table 156.
- NOTE 7: This register is automatically updated when SETAASA CCC or RSTDAA CCC is registered by the PMIC device or when PMIC device goes through bus reset as described in clause 7.8 regardless of whether PMIC is in write-protect mode or non write-protect mode of operation. This register can be read by the Host through normal Read operation but it cannot be written with normal write operation either in I2C mode or I3C Basic mode of operation. When this register is updated, it takes in effect where there is a next START operation (i.e., after STOP operation).
- NOTE 8: At first power on, this register is automatically configured identically by the PMIC on its own as Table 263, Register 0x5F [4].
- NOTE 9: When this encoding is set, the PMIC always floats the PWR_GOOD output signal even when there is an internal VR Disable command due to fault condition.
- NOTE 10: When Host changes ADC accuracy step size, it should also update the threshold setting in Table 133, Register 0x1C to Table 136, Register 0x1F, Table 182, Register 0x11A, Table 183, Register 0x11B.
- NOTE 11: With the coarse ADC accuracy, the register readout is in Table 117, Register 0x0C to Table 120, Register 0x0F and register threshold setting in Table 133, Register 0x1C to Table 136, Register 0x1F is limited to 31.875A.
- NOTE 12: With the granular ADC accuracy, the register readout is in Table 167, Register 0x100 to Table 174, Register 0x107 is limited to 31.968A; the register threshold setting in Table 133, Register 0x1C to Table 136, Register 0x1F and Table 182, Register 0x11A, Table 183, Register 0x11B is limited to 7.968A.

### Related: Table 156 — PMIC Action for Register R32[7,5] Setting (p.182)

```text
                   R32[7,5]        If Output Regulators are On              If Output Regulators are Off
                     00                 Execute VR Disable                              No Action
                     01                 Execute VR Disable                              No Action
                     10         No Action; Regulators remains On                Regulators remains Off
                      11                      No Action                           Execute VR Enable
```

## R33 (0x33) — TEMPERATURE_MEASUREMENT, VIN_MGMT_POWER_GOOD_STATUS_SWITCHOVER_MODE, VBIAS_OR_VIN_BULK_UNDER_VOLTAGE_LOCKOUT_STATUS, VOUT_1.0V_OUTPUT_POWER_GOOD_STATUS

Region: Host Region | Source: JESD301-5 Table 157, p.183

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:5 | TEMPERATURE_MEASUREMENT | RO | 0 |
| 4 | VIN_MGMT_POWER_GOOD_STATUS_SWITCHOVER_MODE | RO | 0 |
| 3 | VBIAS_OR_VIN_BULK_UNDER_VOLTAGE_LOCKOUT_STATUS | RO | 0 |
| 2 | VOUT_1.0V_OUTPUT_POWER_GOOD_STATUS | RO | 0 |
| 1:0 | RESERVED | RV | 0 |

### [7:5] TEMPERATURE_MEASUREMENT

- Description: PMIC Temperature[1]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 000 | < 85 °C |
| 001 | 85 °C |
| 010 | 95 °C |
| 011 | 105 °C |
| 100 | 115 °C |
| 101 | 125 °C |
| 110 | 135 °C |
| 111 | > 140 °C |

### [4] VIN_MGMT_POWER_GOOD_STATUS_SWITCHOVER_MODE

- Description: VIN_Mgmt Input Supply Power Good Status in Switchover Mode Only[2]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → Power Not Good

| Code (bin) | Meaning |
|---|---|
| 0 | Power Not Good |
| 1 | Power Good |

### [3] VBIAS_OR_VIN_BULK_UNDER_VOLTAGE_LOCKOUT_STATUS

- Description: VBias or VIN_Bulk Under Voltage Lockout Status[3]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No Under Voltage Lockout

| Code (bin) | Meaning |
|---|---|
| 0 | No Under Voltage Lockout |
| 1 | Under Voltage Lockout |

### [2] VOUT_1.0V_OUTPUT_POWER_GOOD_STATUS

- Description: VOUT_1.0V LDO Output Power Good Status[4]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → Power Good

| Code (bin) | Meaning |
|---|---|
| 0 | Power Good |
| 1 | Power Not Good |

### [1:0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

**Notes**

- NOTE 1: The accuracy of the temperature readout code is + 5 0C.
- NOTE 2: This register has no meaning when PMIC is NOT in switchover mode. In switchover mode only, when PMIC detects VIN_Mgmt input supply from the platform, this bit is set to indicate that PMIC now recognizes valid VIN_Mgmt input power supply.
- NOTE 3: This register is set when either VBias1 or VBias2 LDO output (depending on PMIC implementation) goes below vendor specific threshold or VIN_Bulk input goes below vendor specific threshold.
- NOTE 4: This register is set when VOUT_1.0V output drops below the threshold setting in register Table 131, Register 0x1A [0].

## R34 (0x34) — PEC_ENABLE, IBI_ENABLE, PARITY_DISABLE, HID_CODE

Region: Host Region | Source: JESD301-5 Table 158, p.184

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | PEC_ENABLE | RO | 0 |
| 6 | IBI_ENABLE | RO | 0 |
| 5 | PARITY_DISABLE | RO | 0 |
| 4 | RESERVED | RV | 0 |
| 3:1 | HID_CODE | RO | 111 |
| 0 | RESERVED | RV | 0 |

### [7] PEC_ENABLE

- Description: Packet Error Code Enable[2] (Applicable Only if R32 [6] = ‘1’)
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → Disable

| Code (bin) | Meaning |
|---|---|
| 0 | Disable |
| 1 | Enable |

### [6] IBI_ENABLE

- Description: In Band Interrupt Enable[3] (Applicable Only if R32 [6] = ‘1’)
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → Disable

| Code (bin) | Meaning |
|---|---|
| 0 | Disable |
| 1 | Enable |

### [5] PARITY_DISABLE

- Description: T Bit Parity Code Disable2 (Applicable Only if R32 [6] = ‘1’.)
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → Enable

| Code (bin) | Meaning |
|---|---|
| 0 | Enable |
| 1 | Disable[4] |

### [4] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [3:1] HID_CODE

- Description: PMIC’s 3-bit HID Code[5]
- Attribute: RO — Read Only (writes have no effect)
- Default: 111 → (code value; no separate meaning listed)

| Code (bin) | Meaning |
|---|---|
| 000 | (code value; no separate meaning listed) |
| 001 | (code value; no separate meaning listed) |
| 010 | (code value; no separate meaning listed) |
| 011 | (code value; no separate meaning listed) |
| 100 | (code value; no separate meaning listed) |
| 101 | (code value; no separate meaning listed) |
| 110 | (code value; no separate meaning listed) |
| 111 | (code value; no separate meaning listed) |

### [0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

**Notes**

- NOTE 1: The write (or update) transaction to this register must be followed by STOP operation to allow the PMIC device to update the setting.
- NOTE 2: This register is automatically updated when RSTDAA CCC is registered by the PMIC device or when PMIC device goes through bus reset as described in clause 7.7. This register cannot be written by the Host through normal write operation either in I2C mode or I3C mode of operation. This register is updated with DEVCTRL CCC with RegMod=’0’ only. This register cannot be written with DEVCTRL CCC with RegMod=’1’.
- NOTE 3: This register is automatically updated when ENEC CCC or DISEC CCC or RSTDAA CCC is registered by the PMIC device or when PMIC device goes through bus reset as described in clause 7.7. This register can be read by the Host through normal Read operation but it cannot be written with normal write operation either in I2C mode or I3C mode of operation. This register cannot be written with DEVCTRL CCC with RegMod=’1’.
- NOTE 4: When Parity function is disabled, the PMIC simply ignores the “T” bit information from the Host. The host may actually choose to compute the parity and send that information in “T” bit or simply drive static low or high in “T” bit.
- NOTE 5: This register is updated when PMIC device receives SETHID CCC or when PMIC device goes through bus reset as described in clause 7.7. This register cannot be written with DEVCTRL CCC with RegMod=’1’.

## R35 (0x35) — ERROR_INJECTION_ENABLE, ERROR_INJECTION_RAIL_SELECTION, OVER_VOLTAGE_UNDER_VOLTAGE_SELECT, MISC_ERROR_INJECTION_TYPE

Region: Host Region | Source: JESD301-5 Table 159, p.185

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | ERROR_INJECTION_ENABLE | RW | 0 |
| 6:4 | ERROR_INJECTION_RAIL_SELECTION | RW | 0 |
| 3 | OVER_VOLTAGE_UNDER_VOLTAGE_SELECT | RW | 0 |
| 2:0 | MISC_ERROR_INJECTION_TYPE | RW | 0 |

### [7] ERROR_INJECTION_ENABLE

- Description: Error Injection Enable[4]
- Attribute: RW — Read/Write
- Default: 0 → Disable

| Code (bin) | Meaning |
|---|---|
| 0 | Disable |
| 1 | Enable |

### [6:4] ERROR_INJECTION_RAIL_SELECTION

- Description: Error Injection - Input Rail and Output Rail Selection[5],[6]
- Attribute: RW — Read/Write
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 000 | Undefined |
| 001 | SWA Output Only |
| 010 | SWB Output Only |
| 011 | SWC Output Only |
| 100 | SWD Output Only |
| 101 | VIN_Bulk Input Only |
| 110 | VIN_Mgmt Input Only |
| 111 | Do Not Use |

### [3] OVER_VOLTAGE_UNDER_VOLTAGE_SELECT

- Description: Over Voltage or Under Voltage Selection for Bits [6:4][7]
- Attribute: RW — Read/Write
- Default: 0 → Over Voltage

| Code (bin) | Meaning |
|---|---|
| 0 | Over Voltage |
| 1 | Under Voltage[8] |

### [2:0] MISC_ERROR_INJECTION_TYPE

- Description: Miscellaneous Error Injection Type[9]
- Attribute: RW — Read/Write
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 000 | Undefined |
| 001 | VIN_Mgmt to VIN_Bulk Switchover |
| 010 | Critical Temperature Shutdown |
| 011 | High Temperature Warning Threshold |
| 100 | VOUT_1.8V LDO Power Good |
| 101 | High Current Consumption Warning[10] |
| 110 | Reserved |
| 111 | Current Limiter Warning[10] |

**Notes**

- NOTE 1: Refer to clause 6.28 for error function usage model. The host can erase the error log registers (Table 109, Register 0x04 to Table 112, Register 0x07) by writing 0x74 to Table 162, Register 0x39.
- NOTE 2: To exit from Error Injection Mode, the PMIC must go through power cycle of both VIN_Bulk and VIN_Mgmt input supply.
- NOTE 3: Error injection function utilizes two registers: Table 159, Register 0x35 and Table 193, Register 0x12F.
- NOTE 4: When error function is invoked by setting bit [7] = ‘1’, the setting of bits Table 159, Register 0x35 [6:4, 2:0] = ‘000 000’ and Table 193, Register 0x12F [5:4, 1:0] = ‘00 00’ is considered an illegal setting.
- NOTE 5: The register Table 159, Register 0x35 [6:4] and Table 193, Register 0x12F [5:4] is only applicable if Table 159, Register 0x35 [2:0] is ‘000’ and Table 193, Register 0x12F [1:0] = ‘00’. Any value other than ‘000’ in Table 159, Register 0x35 [6:4], ‘00’ in Table 193, Register 0x12F [5:4], ‘000’ in Table 159, Register 0x35 [2:0] and ‘00’ in Table 193, Register 0x12F [1:0] is considered an illegal setting and PMIC operation is not guaranteed.
- NOTE 6: If dual or three phase regulator is selected for SWA, SWB and SWE, use SWA encoding to inject the error. If dual phase regulator is selected for SWC and SWF, use SWC encoding to inject the error. Register Table 159, Register 0x35 [3] selects either over voltage or under voltage condition for the setting selected in this register.
- NOTE 7: This register Table 159, Register 0x35 [3] is only applicable if bits Table 159, Register 0x35 [6:4] and Table 193, Register 0x12F [5:4] is anything other than ‘000’ and ‘00’ respectively and Table 193, Register 0x12F [1:0] = ‘00’.
- NOTE 8: The under voltage selection only applies to SWx output rails and VIN_Bulk input. Does not apply to VIN_Mgmt input.
- NOTE 9: This register Table 159, Register 0x35 [2:0] is only applicable if Table 159, Register 0x35 [6:3] is ‘0000’ and Table 193, Register 0x12F [5:4, 1:0] is ‘0000’. Any value other than ‘0000’ in Table 159, Register 0x35 [6:3], ‘00’ in Table 193, Register 0x12F [5:4], ‘000’ in Table 159, Register 0x35 [2:0] and ‘00’ in Table 193, Register 0x12F [1:0] is considered an illegal setting and PMIC operation is not guaranteed.
- NOTE 10: Applies to all enabled SWx output regulators at the same time.

## R37 (0x37) — DIMM_VENDOR_MEMORY_REGION_PASSWORD_LOWER_BYTE

Region: Host Region | Source: JESD301-5 Table 160, p.186

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | DIMM_VENDOR_MEMORY_REGION_PASSWORD_LOWER_BYTE | WO | - |

### [7:0] DIMM_VENDOR_MEMORY_REGION_PASSWORD_LOWER_BYTE

- Description: DIMM Vendor Memory Region (0x40 - 0x6F) Password - Lower Byte [7:0] = Code
- Attribute: WO — Write Only (reads return 0)
- Default: -
- Values: no per-value encoding is listed in the spec for this field.

## R38 (0x38) — DIMM_VENDOR_MEMORY_REGION_PASSWORD_UPPER_BYTE

Region: Host Region | Source: JESD301-5 Table 161, p.186

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | DIMM_VENDOR_MEMORY_REGION_PASSWORD_UPPER_BYTE | WO | - |

### [7:0] DIMM_VENDOR_MEMORY_REGION_PASSWORD_UPPER_BYTE

- Description: DIMM Vendor Memory Region (0x40 - 0x6F) Password - Upper Byte [7:0] = Code
- Attribute: WO — Write Only (reads return 0)
- Default: -
- Values: no per-value encoding is listed in the spec for this field.

## R39 (0x39) — (unnamed)

Region: Host Region | Source: JESD301-5 Table 162, p.186

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | (unnamed) | RW | 0x00 |

### [7:0] (unnamed)

- Attribute: RW — Read/Write
- Default: 0x00
- Note: the codes below are wider than this 8-bit field; the encoding combines bits from more than one field/register (see Description).

**When: Host Region Codes**

| Code (bin) | Meaning |
|---|---|
| 0x74 | Clear Registers R04[7:4], R05 [7:0] to R07[7:0], Erase MTP memory for R04[7:4], R05[7:0] to R07[7:0] |

**When: DIMM Vendor Region (0x40 to 0x6F) Write Codes**

| Code (bin) | Meaning |
|---|---|
| 0x40 | Unlock DIMM Vendor Region. Password needs to be present in R37 & R38 registers. |
| 0x00 | Lock DIMM Vendor Region. |
| 0x80 | Burn DIMM Vendor Region Password. New password needs to be present in R37 & R38. |
| 0x81 | Burn DIMM Vendor Region - 0x40 to 0x4F |
| 0x82 | Burn DIMM Vendor Region - 0x50 to 0x5F |
| 0x85 | Burn DIMM Vendor Region - 0x60 to 0x6F |

**When: DIMM Vendor Region (0x40 to 0x6F) Read Codes**

| Code (bin) | Meaning |
|---|---|
| 0x5A | Burning is complete in DIMM Vendor region. |

## R3A (0x3A) — DEFAULT_READ_ADDRESS_POINTER_ENABLE, DEFAULT_READ_STARTING_ADDRESS, BURST_LENGTH_FOR_READ_DEFAULT_ADDR_POINTER, BYPASS_DIMM_VENDOR_REGION_CRC_ERROR, CHECK_DIMM_VENDOR_REGION_CRC

Region: Host Region | Source: JESD301-5 Table 163, p.187

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | RESERVED | RV | 0 |
| 6 | DEFAULT_READ_ADDRESS_POINTER_ENABLE | RW | 0 |
| 5:4 | DEFAULT_READ_STARTING_ADDRESS | RW | 0 |
| 3:2 | BURST_LENGTH_FOR_READ_DEFAULT_ADDR_POINTER | RW | 0 |
| 1 | BYPASS_DIMM_VENDOR_REGION_CRC_ERROR | RW | 0 |
| 0 | CHECK_DIMM_VENDOR_REGION_CRC | 1O | 0 |

### [7] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [6] DEFAULT_READ_ADDRESS_POINTER_ENABLE

- Description: Enable Default Address Read Pointer when PMIC sees STOP operation
- Attribute: RW — Read/Write
- Default: 0 → Disable Default Address Pointer (address pointer is set by Host)[2]

| Code (bin) | Meaning |
|---|---|
| 0 | Disable Default Address Pointer (address pointer is set by Host)[2] |
| 1 | Enable Default Address Pointer; Address selected by register bits [5:4][3] |

### [5:4] DEFAULT_READ_STARTING_ADDRESS

- Description: Default Read Address Pointer Selection when PMIC sees STOP operation[4]
- Attribute: RW — Read/Write
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 00 | R08 |
| 01 | R0C |
| 10 | R100 |
| 11 | Reserved |

### [3:2] BURST_LENGTH_FOR_READ_DEFAULT_ADDR_POINTER

- Description: Burst Length (# of Bytes) to be transferred for Read Default Address Pointer Mode[5]
- Attribute: RW — Read/Write
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 00 | 2 Bytes |
| 01 | 4 Bytes |
| 10 | 8 Bytes |
| 11 | 16 Bytes |

### [1] BYPASS_DIMM_VENDOR_REGION_CRC_ERROR

- Description: Bypass DIMM Vendor Region CRC Error for VR Enable
- Attribute: RW — Read/Write
- Default: 0 → Disable; PMIC blocks VR Enable command if Table 177, Register 0x10A [6] = ‘1’

| Code (bin) | Meaning |
|---|---|
| 0 | Disable; PMIC blocks VR Enable command if Table 177, Register 0x10A [6] = ‘1’ |
| 1 | Enable; Ignore Table 177, Register 0x10A [6] Error status and turn on output regulators at next VR Enable command |

### [0] CHECK_DIMM_VENDOR_REGION_CRC

- Description: Check DIMM Vendor Region CRC Code[6]
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Check DIMM Vendor Region CRC Code |

**Notes**

- NOTE 1: The write (or update) transaction to this register must be followed by STOP operation to allow the PMIC device to update the setting.
- NOTE 2: The register setting in Table 163, Register 0x3A[5:4] is a don’t care.
- NOTE 3: This mode is only allowed when PEC function is disabled (i.e., register Table 158, Register 0x34[7] = ‘0’).
- NOTE 4: This register is only applicable if Table 163, Register 0x3A[6] = ‘1’.
- NOTE 5: This register is only applicable if Table 163, Register 0x3A[6] = ‘1’ and Table 158, Register 0x34[7] = ‘1’.
- NOTE 6: The PMIC self clears this bit when CRC check is complete.

## R3B (0x3B) — PMIC_PART_CAPABILITY_EXT, REVISION_ID_MAJOR_STEPPING, REVISION_ID_MINOR_STEPPING, PMIC_PART_CAPABILITY

Region: Host Region | Source: JESD301-5 Table 164, p.188

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | PMIC_PART_CAPABILITY_EXT | ROA | 10 |
| 5:4 | REVISION_ID_MAJOR_STEPPING | ROA | - |
| 3:1 | REVISION_ID_MINOR_STEPPING | ROA | - |
| 0 | PMIC_PART_CAPABILITY | ROA | 0 |

### [7:6] PMIC_PART_CAPABILITY_EXT

- Description: PMIC Current Capability Extension. This register bits [7:6] and bit [0] provides 3 bit encoding as following:
- Attribute: ROA — Read Only (writes have no effect); Persistent, set by the PMIC vendor at manufacturing
- Default: 10
- Note: the codes below are wider than this 2-bit field; the encoding combines bits from more than one field/register (see Description).

| Code (bin) | Meaning |
|---|---|
| 000 | PMIC5010 |
| 001 | PMIC5000 |
| 01x | PMIC5020 |
| 10x | PMIC5030 |
| 11x | Reserved |

### [5:4] REVISION_ID_MAJOR_STEPPING

- Description: Major Revision Stepping
- Attribute: ROA — Read Only (writes have no effect); Persistent, set by the PMIC vendor at manufacturing
- Default: -

| Code (bin) | Meaning |
|---|---|
| 00 | Revision 1 |
| 01 | Revision 2 |
| 10 | Revision 3 |
| 11 | Revision 4 |

### [3:1] REVISION_ID_MINOR_STEPPING

- Description: Minor Revision Stepping All other encodings are reserved.
- Attribute: ROA — Read Only (writes have no effect); Persistent, set by the PMIC vendor at manufacturing
- Default: -

| Code (bin) | Meaning |
|---|---|
| 000 | Revision 0 |
| 001 | Revision 1 |
| 010 | Revision 2 |
| 011 | Revision 3 |

### [0] PMIC_PART_CAPABILITY

- Description: PMIC Current Capability. See also bits [7:6] definition.
- Attribute: ROA — Read Only (writes have no effect); Persistent, set by the PMIC vendor at manufacturing
- Default: 0 → PMIC5010

| Code (bin) | Meaning |
|---|---|
| 0 | PMIC5010 |
| 1 | PMIC5000 |

## R3C (0x3C) — VENDOR_ID_BYTE0

Region: Host Region | Source: JESD301-5 Table 165, p.188

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | VENDOR_ID_BYTE0 | ROA | - |

### [7:0] VENDOR_ID_BYTE0

- Description: Vendor Identification Register Byte 0.
- Attribute: ROA — Read Only (writes have no effect); Persistent, set by the PMIC vendor at manufacturing
- Default: -
- Values: no per-value encoding is listed in the spec for this field.

## R3D (0x3D) — VENDOR_ID_BYTE1

Region: Host Region | Source: JESD301-5 Table 166, p.189

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | VENDOR_ID_BYTE1 | ROA | - |

### [7:0] VENDOR_ID_BYTE1

- Description: Vendor Identification Register Byte 1.
- Attribute: ROA — Read Only (writes have no effect); Persistent, set by the PMIC vendor at manufacturing
- Default: -
- Values: no per-value encoding is listed in the spec for this field.

## R40 (0x40) — POWER_ON_SEQUENCE_CONFIG0, POWER_ON_SEQUENCE_CONFIG0_SWA_ENABLE, POWER_ON_SEQUENCE_CONFIG0_SWB_ENABLE, POWER_ON_SEQUENCE_CONFIG0_SWC_ENABLE, POWER_ON_SEQUENCE_CONFIG0_SWD_ENABLE, POWER_ON_SEQUENCE_CONFIG0_IDLE

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-5 Table 232, p.223

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | POWER_ON_SEQUENCE_CONFIG0 | RWPE | 0 |
| 6 | POWER_ON_SEQUENCE_CONFIG0_SWA_ENABLE | RWPE | 0 |
| 5 | POWER_ON_SEQUENCE_CONFIG0_SWB_ENABLE | RWPE | 0 |
| 4 | POWER_ON_SEQUENCE_CONFIG0_SWC_ENABLE | RWPE | 0 |
| 3 | POWER_ON_SEQUENCE_CONFIG0_SWD_ENABLE | RWPE | 0 |
| 2:0 | POWER_ON_SEQUENCE_CONFIG0_IDLE | RWPE | 001 |

### [7] POWER_ON_SEQUENCE_CONFIG0

- Description: PMIC Power On Sequence Config 0[2],[3]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Do Not Execute Config 0

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Execute Config 0 |
| 1 | Execute Config 0 |

### [6] POWER_ON_SEQUENCE_CONFIG0_SWA_ENABLE

- Description: Enable SWA Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No action

| Code (bin) | Meaning |
|---|---|
| 0 | No action |
| 1 | Enable SWA Output Regulator |

### [5] POWER_ON_SEQUENCE_CONFIG0_SWB_ENABLE

- Description: Enable SWB Output Regulator.[4]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No action

| Code (bin) | Meaning |
|---|---|
| 0 | No action |
| 1 | Enable SWB Output Regulator |

### [4] POWER_ON_SEQUENCE_CONFIG0_SWC_ENABLE

- Description: Enable SWC Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No action

| Code (bin) | Meaning |
|---|---|
| 0 | No action |
| 1 | Enable SWC Output Regulator |

### [3] POWER_ON_SEQUENCE_CONFIG0_SWD_ENABLE

- Description: Enable SWD Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No action

| Code (bin) | Meaning |
|---|---|
| 0 | No action |
| 1 | Enable SWD Output Regulator |

### [2:0] POWER_ON_SEQUENCE_CONFIG0_IDLE

- Description: Idle time after Power On Sequence Config 0[5]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 001 → 2 ms

| Code (bin) | Meaning |
|---|---|
| 000 | 0 ms |
| 001 | 2 ms |
| 010 | 4 ms |
| 011 | 6 ms |
| 100 | 8 ms |
| 101 | 10 ms |
| 110 | 12 ms |
| 111 | 24 ms |

**Notes**

- NOTE 1: The PMIC always starts with power on sequence configuration 0 register and executes remaining power on sequence configuration registers (1 to 5) in sequential order.
- NOTE 2: Power on sequence configuration 0 is total of 10 bit register. 8 bits as shown in Table 232, Register 0x40 [7:0] plus 2 bits in Table 267, Register 0x63 [7:6].
- NOTE 3: If bit [7] = ‘0’, bits [6:0] and Table 267, Register 0x63 [7:6] are ignored and PMIC moves to next power on sequence configuration register. If bit [7] = ‘1’, PMIC executes bits [6:0] and Table 267, Register 0x63 [7:6] as configured; if no new rail is turned on, the PMIC simply waits the idle time as configured and then moves to next power sequence configuration register.
- NOTE 4: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care.
- NOTE 5: Idle time is the additional time after soft-start time expires. The PMIC waits sum of Soft Start time and Idle time before it executes the next power on sequence configuration register. If more than one regulators are enabled, the PMIC uses the largest value of the soft start time among the regulators that are enabled in this configuration register.

## R41 (0x41) — POWER_ON_SEQUENCE_CONFIG1, POWER_ON_SEQUENCE_CONFIG1_SWA_ENABLE, POWER_ON_SEQUENCE_CONFIG1_SWB_ENABLE, POWER_ON_SEQUENCE_CONFIG1_SWC_ENABLE, POWER_ON_SEQUENCE_CONFIG1_SWD_ENABLE, POWER_ON_SEQUENCE_CONFIG1_IDLE

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-5 Table 233, p.224

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | POWER_ON_SEQUENCE_CONFIG1 | RWPE | 0 |
| 6 | POWER_ON_SEQUENCE_CONFIG1_SWA_ENABLE | RWPE | 0 |
| 5 | POWER_ON_SEQUENCE_CONFIG1_SWB_ENABLE | RWPE | 0 |
| 4 | POWER_ON_SEQUENCE_CONFIG1_SWC_ENABLE | RWPE | 0 |
| 3 | POWER_ON_SEQUENCE_CONFIG1_SWD_ENABLE | RWPE | 0 |
| 2:0 | POWER_ON_SEQUENCE_CONFIG1_IDLE | RWPE | 001 |

### [7] POWER_ON_SEQUENCE_CONFIG1

- Description: PMIC Power On Sequence Config 1
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Do Not Execute Config[3][1]

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Execute Config[3][1] |
| 1 | Execute Config 1 |

### [6] POWER_ON_SEQUENCE_CONFIG1_SWA_ENABLE

- Description: Enable SWA Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No action

| Code (bin) | Meaning |
|---|---|
| 0 | No action |
| 1 | Enable SWA Output Regulator |

### [5] POWER_ON_SEQUENCE_CONFIG1_SWB_ENABLE

- Description: Enable SWB Output Regulator.[4]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No action

| Code (bin) | Meaning |
|---|---|
| 0 | No action |
| 1 | Enable SWB Output Regulator |

### [4] POWER_ON_SEQUENCE_CONFIG1_SWC_ENABLE

- Description: Enable Switch Node C Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No action

| Code (bin) | Meaning |
|---|---|
| 0 | No action |
| 1 | Enable SWC Output Regulator |

### [3] POWER_ON_SEQUENCE_CONFIG1_SWD_ENABLE

- Description: Enable Switch Node D Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No action

| Code (bin) | Meaning |
|---|---|
| 0 | No action |
| 1 | Enable SWD Output Regulator |

### [2:0] POWER_ON_SEQUENCE_CONFIG1_IDLE

- Description: Idle time after Power On Sequence Config 1[5]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 001 → 2 ms

| Code (bin) | Meaning |
|---|---|
| 000 | 0 ms |
| 001 | 2 ms |
| 010 | 4 ms |
| 011 | 6 ms |
| 100 | 8 ms |
| 101 | 10 ms |
| 110 | 12 ms |
| 111 | 24 ms |

**Notes**

- NOTE 1: The PMIC always starts with power on sequence configuration 0 register and executes remaining power on sequence configuration registers (1 to 5) in sequential order.
- NOTE 2: Power on sequence configuration 1 is total of 10 bit register. 8 bits as shown in Table 233, Register 0x41 [7:0] plus 2 bits in Table 267, Register 0x63 [5:4].
- NOTE 3: If bit [7] = ‘0’, bits [6:0] and Table 267, Register 0x63 [5:4] are ignored and PMIC moves to next power on sequence configuration register. If bit [7] = ‘1’, PMIC executes bits [6:0] and Table 267, Register 0x63 [5:4] as configured; if no new rail is turned on, the PMIC simply waits the idle time as configured and then moves to next power sequence configuration register.
- NOTE 4: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care.
- NOTE 5: Idle time is the additional time after soft-start time expires. The PMIC waits sum of Soft Start time and Idle time before it executes the next power on sequence configuration register. If more than one regulators are enabled, the PMIC uses the largest value of the soft start time among the regulators that are enabled in this configuration register.

## R42 (0x42) — POWER_ON_SEQUENCE_CONFIG2, POWER_ON_SEQUENCE_CONFIG2_SWA_ENABLE, POWER_ON_SEQUENCE_CONFIG2_SWB_ENABLE, POWER_ON_SEQUENCE_CONFIG2_SWC_ENABLE, POWER_ON_SEQUENCE_CONFIG2_SWD_ENABLE, POWER_ON_SEQUENCE_CONFIG2_IDLE

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-5 Table 234, p.225

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | POWER_ON_SEQUENCE_CONFIG2 | RWPE | 0 |
| 6 | POWER_ON_SEQUENCE_CONFIG2_SWA_ENABLE | RWPE | 0 |
| 5 | POWER_ON_SEQUENCE_CONFIG2_SWB_ENABLE | RWPE | 0 |
| 4 | POWER_ON_SEQUENCE_CONFIG2_SWC_ENABLE | RWPE | 0 |
| 3 | POWER_ON_SEQUENCE_CONFIG2_SWD_ENABLE | RWPE | 0 |
| 2:0 | POWER_ON_SEQUENCE_CONFIG2_IDLE | RWPE | 001 |

### [7] POWER_ON_SEQUENCE_CONFIG2

- Description: PMIC Power On Sequence Config 2[3]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Do Not Execute Config 2

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Execute Config 2 |
| 1 | Execute Config 2 |

### [6] POWER_ON_SEQUENCE_CONFIG2_SWA_ENABLE

- Description: Enable Switch Node A Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No action

| Code (bin) | Meaning |
|---|---|
| 0 | No action |
| 1 | Enable Switch Node A Output Regulator |

### [5] POWER_ON_SEQUENCE_CONFIG2_SWB_ENABLE

- Description: Enable Switch Node B Output Regulator.[4]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No action

| Code (bin) | Meaning |
|---|---|
| 0 | No action |
| 1 | Enable Switch Node B Output Regulator |

### [4] POWER_ON_SEQUENCE_CONFIG2_SWC_ENABLE

- Description: Enable Switch Node C Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No action

| Code (bin) | Meaning |
|---|---|
| 0 | No action |
| 1 | Enable Switch Node C Output Regulator |

### [3] POWER_ON_SEQUENCE_CONFIG2_SWD_ENABLE

- Description: Enable Switch Node D Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No action

| Code (bin) | Meaning |
|---|---|
| 0 | No action |
| 1 | Enable Switch Node D Output Regulator |

### [2:0] POWER_ON_SEQUENCE_CONFIG2_IDLE

- Description: Idle time after Power On Sequence Config 2[5]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 001 → 2 ms

| Code (bin) | Meaning |
|---|---|
| 000 | 0 ms |
| 001 | 2 ms |
| 010 | 4 ms |
| 011 | 6 ms |
| 100 | 8 ms |
| 101 | 10 ms |
| 110 | 12 ms |
| 111 | 24 ms |

**Notes**

- NOTE 1: The PMIC always starts with power on sequence configuration 0 register and executes remaining power on sequence configuration registers (1 to 5) in sequential order.
- NOTE 2: Power on sequence configuration 2 is total of 10 bit register. 8 bits as shown in Table 234, Register 0x42 [7:0] plus 2 bits in Table 267, Register 0x63 [3:2].
- NOTE 3: If bit [7] = ‘0’, bits [6:0] and Table 267, Register 0x63 [3:2] are ignored and PMIC moves to next power on sequence configuration register. If bit [7] = ‘1’, PMIC executes bits [6:0] and Table 267, Register 0x63 [3:2] as configured; if no new rail is turned on, the PMIC simply waits the idle time as configured and then moves to next power sequence configuration register.
- NOTE 4: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care.
- NOTE 5: Idle time is the additional time after soft-start time expires. The PMIC waits sum of Soft Start time and Idle time before it executes the next power on sequence configuration register. If more than one regulators are enabled, the PMIC uses the largest value of the soft start time among the regulators that are enabled in this configuration register.

## R43 (0x43) — POWER_ON_SEQUENCE_CONFIG3, POWER_ON_SEQUENCE_CONFIG3_SWA_ENABLE, POWER_ON_SEQUENCE_CONFIG3_SWB_ENABLE, POWER_ON_SEQUENCE_CONFIG3_SWC_ENABLE, POWER_ON_SEQUENCE_CONFIG3_SWD_ENABLE, POWER_ON_SEQUENCE_CONFIG3_IDLE

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-5 Table 235, p.226

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | POWER_ON_SEQUENCE_CONFIG3 | RWPE | 0 |
| 6 | POWER_ON_SEQUENCE_CONFIG3_SWA_ENABLE | RWPE | 0 |
| 5 | POWER_ON_SEQUENCE_CONFIG3_SWB_ENABLE | RWPE | 0 |
| 4 | POWER_ON_SEQUENCE_CONFIG3_SWC_ENABLE | RWPE | 0 |
| 3 | POWER_ON_SEQUENCE_CONFIG3_SWD_ENABLE | RWPE | 0 |
| 2:0 | POWER_ON_SEQUENCE_CONFIG3_IDLE | RWPE | 001 |

### [7] POWER_ON_SEQUENCE_CONFIG3

- Description: PMIC Power On Sequence Config 3
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Do Not Execute Config 3[3]

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Execute Config 3[3] |
| 1 | Execute Config 3 |

### [6] POWER_ON_SEQUENCE_CONFIG3_SWA_ENABLE

- Description: Enable Switch Node A Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Enable Switch Node A Output Regulator |

### [5] POWER_ON_SEQUENCE_CONFIG3_SWB_ENABLE

- Description: Enable Switch Node B Output Regulator.[4]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Enable Switch Node B Output Regulator |

### [4] POWER_ON_SEQUENCE_CONFIG3_SWC_ENABLE

- Description: Enable Switch Node C Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Enable Switch Node C Output Regulator |

### [3] POWER_ON_SEQUENCE_CONFIG3_SWD_ENABLE

- Description: Enable Switch Node D Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Enable Switch Node D Output Regulator |

### [2:0] POWER_ON_SEQUENCE_CONFIG3_IDLE

- Description: Idle time after Power On Sequence Config 3[5]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 001 → 2 ms

| Code (bin) | Meaning |
|---|---|
| 000 | 0 ms |
| 001 | 2 ms |
| 010 | 4 ms |
| 011 | 6 ms |
| 100 | 8 ms |
| 101 | 10 ms |
| 110 | 12 ms |
| 111 | 24 ms |

**Notes**

- NOTE 1: The PMIC always starts with power on sequence configuration 0 register and executes remaining power on sequence configuration registers (1 to 5) in sequential order.
- NOTE 2: Power on sequence configuration 3 is total of 10 bit register. 8 bits as shown in Table 235, Register 0x43 [7:0] plus 2 bits in Table 267, Register 0x63 [1:0].
- NOTE 3: If bit [7] = ‘0’, bits [6:0] and Table 267, Register 0x63 [1:0] are ignored and PMIC moves to next power on sequence configuration register. If bit [7] = ‘1’, PMIC executes bits [6:0] and Table 267, Register 0x63 [1:0] as configured; if no new rail is turned on, the PMIC simply waits the idle time as configured and then moves to next power sequence configuration register.
- NOTE 4: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care.
- NOTE 5: Idle time is the additional time after soft-start time expires. The PMIC waits sum of Soft Start time and Idle time before it executes the next event. If more than one regulators are enabled, the PMIC uses the largest value of the soft start time among the regulators that are enabled in this configuration register.

## R44 (0x44) — POWER_ON_SEQUENCE_CONFIG4, POWER_ON_SEQUENCE_CONFIG4_SWA_ENABLE, POWER_ON_SEQUENCE_CONFIG4_SWB_ENABLE, POWER_ON_SEQUENCE_CONFIG4_SWC_ENABLE, POWER_ON_SEQUENCE_CONFIG4_SWD_ENABLE, POWER_ON_SEQUENCE_CONFIG4_IDLE

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-5 Table 236, p.227

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | POWER_ON_SEQUENCE_CONFIG4 | RWPE | 0 |
| 6 | POWER_ON_SEQUENCE_CONFIG4_SWA_ENABLE | RWPE | 0 |
| 5 | POWER_ON_SEQUENCE_CONFIG4_SWB_ENABLE | RWPE | 0 |
| 4 | POWER_ON_SEQUENCE_CONFIG4_SWC_ENABLE | RWPE | 0 |
| 3 | POWER_ON_SEQUENCE_CONFIG4_SWD_ENABLE | RWPE | 0 |
| 2:0 | POWER_ON_SEQUENCE_CONFIG4_IDLE | RWPE | 001 |

### [7] POWER_ON_SEQUENCE_CONFIG4

- Description: PMIC Power On Sequence Config 4
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Do Not Execute Config 4[3]

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Execute Config 4[3] |
| 1 | Execute Config 4 |

### [6] POWER_ON_SEQUENCE_CONFIG4_SWA_ENABLE

- Description: Enable Switch Node A Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Enable Switch Node A Output Regulator |

### [5] POWER_ON_SEQUENCE_CONFIG4_SWB_ENABLE

- Description: Enable Switch Node B Output Regulator.[4]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Enable Switch Node B Output Regulator |

### [4] POWER_ON_SEQUENCE_CONFIG4_SWC_ENABLE

- Description: Enable Switch Node C Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Enable Switch Node C Output Regulator |

### [3] POWER_ON_SEQUENCE_CONFIG4_SWD_ENABLE

- Description: Enable Switch Node D Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Enable Switch Node D Output Regulator |

### [2:0] POWER_ON_SEQUENCE_CONFIG4_IDLE

- Description: Idle time after Power On Sequence Config 4[5]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 001 → 2 ms

| Code (bin) | Meaning |
|---|---|
| 000 | 0 ms |
| 001 | 2 ms |
| 010 | 4 ms |
| 011 | 6 ms |
| 100 | 8 ms |
| 101 | 10 ms |
| 110 | 12 ms |
| 111 | 24 ms |

**Notes**

- NOTE 1: The PMIC always starts with power on sequence configuration 0 register and executes remaining power on sequence configuration registers (1 to 5) in sequential order.
- NOTE 2: Power on sequence configuration 4 is total of 10 bit register. 8 bits as shown in Table 236, Register 0x44 [7:0] plus 2 bits in Table 268, Register 0x64 [7:6].
- NOTE 3: If bit [7] = ‘0’, bits [6:0] and Table 268, Register 0x64 [7:6] are ignored and PMIC moves to next power on sequence configuration register. If bit [7] = ‘1’, PMIC executes bits [6:0] Table 268, Register 0x64 [7:6] as configured; if no new rail is turned on, the PMIC simply waits the idle time as configured and then moves to next power sequence configuration register.
- NOTE 4: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care.
- NOTE 5: Idle time is the additional time after soft-start time expires. The PMIC waits sum of Soft Start time and Idle time before it executes the next event. If more than one regulators are enabled, the PMIC uses the largest value of the soft start time among the regulators that are enabled in this configuration register.

## R45 (0x45) — SWA_VOLTAGE_SETTING, SWA_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-5 Table 237, p.228

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:1 | SWA_VOLTAGE_SETTING | RWPE | 011 1100 |
| 0 | SWA_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING | RWPE | 0 |

### [7:1] SWA_VOLTAGE_SETTING

- Description: SWA Output Regulator Voltage Setting[1]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 011 1100 → 1100 mV or 900 mV

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 0000000 | 0x00 | 800 mV[2] or 600 mV[3] |
| 0000001 | 0x01 | 805 mV or 605 mV |
| 0000010 | 0x02 | 810 mV or 610 mV |
| ... | ... | ... |
| 0111100 | 0x3C | 1100 mV or 900 mV |
| ... | ... | ... |
| 1111101 | 0x7D | 1425 mV or 1225 mV |
| 1111110 | 0x7E | 1430 mV or 1230 mV |
| 1111111 | 0x7F | 1435 mV or 1235 mV |

### [0] SWA_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

- Description: SWA Output Threshold Low Side Voltage For Power Good Status
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → - 5% from the setting in Table 237, Register 0x45 [7:1]

| Code (bin) | Meaning |
|---|---|
| 0 | - 5% from the setting in Table 237, Register 0x45 [7:1] |
| 1 | - 7.5% from the setting in Table 237, Register 0x45 [7:1] |

**Notes**

- NOTE 1: PMIC guarantees efficiency spec within a range of 1050 mV to 1160 mV.
- NOTE 2: Table 249, Register 0x51 [5] = ‘0’.
- NOTE 3: Table 249, Register 0x51 [5] = ‘1’.

## R46 (0x46) — SWA_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING, SWA_OVER_VOLTAGE_THRESHOLD_SETTING, SWA_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING, SWA_OUTPUT_SOFT_STOP_TIME

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-5 Table 238, p.229

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWA_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING | RWPE | 01 |
| 5:4 | SWA_OVER_VOLTAGE_THRESHOLD_SETTING | RWPE | 10 |
| 3:2 | SWA_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING | RWPE | 00 |
| 1:0 | SWA_OUTPUT_SOFT_STOP_TIME | RWPE | 00 |

### [7:6] SWA_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING

- Description: Switch Node A Output Threshold High Side Voltage For Power Good Status
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 01 → +7.5% from the setting in Table 237, Register 0x45 [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +5% from the setting in Table 237, Register 0x45 [7:1] |
| 01 | +7.5% from the setting in Table 237, Register 0x45 [7:1] |
| 10 | +10% from the setting in Table 237, Register 0x45 [7:1] |
| 11 | Reserved |

### [5:4] SWA_OVER_VOLTAGE_THRESHOLD_SETTING

- Description: Switch Node A Output Regulator Threshold For Over Voltage Status[1]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 10 → +12.5% from the setting in Table 237, Register 0x45 [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +7.5% from the setting in Table 237, Register 0x45 [7:1] |
| 01 | +10% from the setting in Table 237, Register 0x45 [7:1] |
| 10 | +12.5% from the setting in Table 237, Register 0x45 [7:1] |
| 11 | Reserved |

### [3:2] SWA_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING

- Description: Switch Node A Output Regulator Threshold For Under Voltage Lockout Status
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 00 → -10% from the setting in Table 237, Register 0x45 [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | -10% from the setting in Table 237, Register 0x45 [7:1] |
| 01 | -12.5% from the setting in Table 237, Register 0x45 [7:1] |
| 10 | Reserved |
| 11 | Reserved |

### [1:0] SWA_OUTPUT_SOFT_STOP_TIME

- Description: SWA Output Regulator Soft Stop Time After VR Disable[2]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 00 → 0.5 ms

| Code (bin) | Meaning |
|---|---|
| 00 | 0.5 ms |
| 01 | 1 ms |
| 10 | 2 ms |
| 11 | 4 ms |

**Notes**

- NOTE 1: The setting for the Over Voltage must be higher than Power Good High Side Voltage threshold in Table 238, Register 0x46[7:6].
- NOTE 2: This is the time it takes for buck regulator to go from steady state voltage to 0 V.

## R47 (0x47) — SWB_VOLTAGE_SETTING, SWB_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-5 Table 239, p.230

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:1 | SWB_VOLTAGE_SETTING | RWPE | 011 1100 |
| 0 | SWB_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING | RWPE | 0 |

### [7:1] SWB_VOLTAGE_SETTING

- Description: SWB Output Regulator Voltage Setting[2]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 011 1100 → 1100 mV or 900 mV

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 0000000 | 0x00 | 800 mV[3] or 600 mV[4] |
| 0000001 | 0x01 | 805 mV or 605 mV |
| 0000010 | 0x02 | 810 mV or 610 mV |
| ... | ... | ... |
| 0111100 | 0x3C | 1100 mV or 900 mV |
| ... | ... | ... |
| 1111101 | 0x7D | 1425 mV or 1225 mV |
| 1111110 | 0x7E | 1430 mV or 1230 mV |
| 1111111 | 0x7F | 1435 mV or 1235 mV |

### [0] SWB_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

- Description: SWB Output Threshold Low Side Voltage For Power Good Status
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → -5% from the setting in Table 239, Register 0x47 [7:1]

| Code (bin) | Meaning |
|---|---|
| 0 | -5% from the setting in Table 239, Register 0x47 [7:1] |
| 1 | -7.5% from the setting in Table 239, Register 0x47 [7:1] |

**Notes**

- NOTE 1: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care.
- NOTE 2: PMIC guarantees efficiency spec within a range of 1050 mV to 1160 mV.
- NOTE 3: Table 249, Register 0x51 [4] = ‘0’.
- NOTE 4: Table 249, Register 0x51 [4] = ‘1’.

## R48 (0x48) — SWB_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING, SWB_OVER_VOLTAGE_THRESHOLD_SETTING, SWB_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING, SWB_OUTPUT_SOFT_STOP_TIME

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-5 Table 240, p.231

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWB_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING | RWPE | 01 |
| 5:4 | SWB_OVER_VOLTAGE_THRESHOLD_SETTING | RWPE | 10 |
| 3:2 | SWB_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING | RWPE | 00 |
| 1:0 | SWB_OUTPUT_SOFT_STOP_TIME | RWPE | 00 |

### [7:6] SWB_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING

- Description: SWB Output Threshold High Side Voltage For Power Good Status
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 01 → +7.5% from the setting in Table 239, Register 0x47 [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +5% from the setting in Table 239, Register 0x47 [7:1] |
| 01 | +7.5% from the setting in Table 239, Register 0x47 [7:1] |
| 10 | +10% from the setting in Table 239, Register 0x47 [7:1] |
| 11 | Reserved |

### [5:4] SWB_OVER_VOLTAGE_THRESHOLD_SETTING

- Description: SWB Output Regulator Threshold For Over Voltage Status[2]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 10 → +12.5% from the setting in Table 239, Register 0x47 [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +7.5% from the setting in Table 239, Register 0x47 [7:1] |
| 01 | +10% from the setting in Table 239, Register 0x47 [7:1] |
| 10 | +12.5% from the setting in Table 239, Register 0x47 [7:1] |
| 11 | Reserved |

### [3:2] SWB_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING

- Description: SWB Output Regulator Threshold For Under Voltage Lockout Status
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 00 → -10% from the setting in Table 239, Register 0x47 [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | -10% from the setting in Table 239, Register 0x47 [7:1] |
| 01 | -12.5% from the setting in Table 239, Register 0x47 [7:1] |
| 10 | Reserved |
| 11 | Reserved |

### [1:0] SWB_OUTPUT_SOFT_STOP_TIME

- Description: SWB Output Regulator Soft Stop Time After VR Disable[3]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 00 → 0.5 ms

| Code (bin) | Meaning |
|---|---|
| 00 | 0.5 ms |
| 01 | 1 ms |
| 10 | 2 ms |
| 11 | 4 ms |

**Notes**

- NOTE 1: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care.
- NOTE 2: The setting for the Over Voltage must be higher than Power Good High Side Voltage threshold in Table 240, Register 0x48[7:6].
- NOTE 3: This is the time it takes for buck regulator to go from steady state voltage to 0 V.

## R49 (0x49) — SWC_VOLTAGE_SETTING, SWC_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-5 Table 241, p.232

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:1 | SWC_VOLTAGE_SETTING | RWPE | 011 1100 |
| 0 | SWC_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING | RWPE | 0 |

### [7:1] SWC_VOLTAGE_SETTING

- Description: SWC Output Regulator Voltage Setting[1]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 011 1100 → 1100 mV or 900 mV or 550 mV

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 0000000 | 0x00 | 800 mV[2] or 600 mV[3] or 400 mV[4] |
| 0000001 | 0x01 | 805 mV or 605 mV or 402.5 mV |
| 0000010 | 0x02 | 810 mV or 610 mV or 405 mV |
| ... | ... | ... |
| 0111100 | 0x3C | 1100 mV or 900 mV or 550 mV |
| ... | ... | ... |
| 1111101 | 0x7D | 1425 mV or 1225 mV or 712.5 mV |
| 1111110 | 0x7E | 1430 mV or 1230 mV or 715 mV |
| 1111111 | 0x7F | 1435 mV or 1235 mV or 717.5 mV |

### [0] SWC_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

- Description: Switch Node C Output Threshold Low Side Voltage For Power Good Status
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → -5% from the setting in Table 241, Register 0x49 [7:1]

| Code (bin) | Meaning |
|---|---|
| 0 | -5% from the setting in Table 241, Register 0x49 [7:1] |
| 1 | -7.5 from the setting in Table 241, Register 0x49 [7:1] |

**Notes**

- NOTE 1: PMIC guarantees efficiency spec within a range of 1050 mV to 1160 mV.
- NOTE 2: Table 250, Register 0x52 [0] = ‘0’ and Table 249, Register 0x51 [3] = ‘0’; 5 mV step size.
- NOTE 3: Table 250, Register 0x52 [0] = ‘0’ and Table 249, Register 0x51 [3] = ‘1’; 5 mV step size.
- NOTE 4: Table 250, Register 0x52 [0] = ‘1’ and Table 249, Register 0x51 [3] = ‘0’; 2.5 mV step size.

## R4A (0x4A) — SWC_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING, SWC_OVER_VOLTAGE_THRESHOLD_SETTING, SWC_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING, SWC_OUTPUT_SOFT_STOP_TIME

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-5 Table 242, p.233

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWC_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING | RWPE | 01 |
| 5:4 | SWC_OVER_VOLTAGE_THRESHOLD_SETTING | RWPE | 10 |
| 3:2 | SWC_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING | RWPE | 00 |
| 1:0 | SWC_OUTPUT_SOFT_STOP_TIME | RWPE | 00 |

### [7:6] SWC_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING

- Description: SWC Output Threshold High Side Voltage For Power Good Status
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 01 → +7.5% from the setting in Table 241, Register 0x49 [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +5% from the setting in Table 241, Register 0x49 [7:1] |
| 01 | +7.5% from the setting in Table 241, Register 0x49 [7:1] |
| 10 | +10% from the setting in Table 241, Register 0x49 [7:1] |
| 11 | Reserved |

### [5:4] SWC_OVER_VOLTAGE_THRESHOLD_SETTING

- Description: SWC Output Regulator Threshold For Over Voltage Status[1]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 10 → +12.5% from the setting in Table 241, Register 0x49 [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +7.5% from the setting in Table 241, Register 0x49 [7:1] |
| 01 | +10% from the setting in Table 241, Register 0x49 [7:1] |
| 10 | +12.5% from the setting in Table 241, Register 0x49 [7:1] |
| 11 | Reserved |

### [3:2] SWC_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING

- Description: SWC Output Regulator Threshold For Under Voltage Lockout Status
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 00 → -10% from the setting in Table 241, Register 0x49 [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | -10% from the setting in Table 241, Register 0x49 [7:1] |
| 01 | -12.5% from the setting in Table 241, Register 0x49 [7:1] |
| 10 | Reserved |
| 11 | Reserved |

### [1:0] SWC_OUTPUT_SOFT_STOP_TIME

- Description: SWC Output Regulator Soft Stop Time After VR Disable[2]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 00 → 0.5 ms

| Code (bin) | Meaning |
|---|---|
| 00 | 0.5 ms |
| 01 | 1 ms |
| 10 | 2 ms |
| 11 | 4 ms |

**Notes**

- NOTE 1: The setting for the Over Voltage must be higher than Power Good High Side Voltage threshold in Table 242, Register 0x4A[7:6].
- NOTE 2: This is the time it takes for buck regulator to go from steady state voltage to 0 V.

## R4B (0x4B) — SWD_VOLTAGE_SETTING, SWD_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-5 Table 243, p.234

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:1 | SWD_VOLTAGE_SETTING | RWPE | 011 1100 |
| 0 | SWD_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING | RWPE | 0 |

### [7:1] SWD_VOLTAGE_SETTING

- Description: SWD Output Regulator Voltage Setting[1]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 011 1100 → 1800 mV or 2500 mV

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 0000000 | 0x00 | 1500 mV[2] or 2200 mV[3] |
| 0000001 | 0x01 | 1505 mV or 2205 mV |
| 0000010 | 0x02 | 1510 mV or 2210 mV |
| ... | ... | ... |
| 0111100 | 0x3C | 1800 mV or 2500 mV |
| ... | ... | ... |
| 1111101 | 0x7D | 2125 mV or 2825 mV |
| 1111110 | 0x7E | 2130 mV or 2830 mV |
| 1111111 | 0x7F | 2135 mV or 2835 mV |

### [0] SWD_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

- Description: SWD Output Threshold Low Side Voltage For Power Good Status
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → -5% from the setting in Table 243, Register 0x4B [7:1]

| Code (bin) | Meaning |
|---|---|
| 0 | -5% from the setting in Table 243, Register 0x4B [7:1] |
| 1 | -7.5% from the setting in Table 243, Register 0x4B [7:1] |

**Notes**

- NOTE 1: PMIC guarantees efficiency spec within a range of 1750 mV to 1850 mV.
- NOTE 2: Table 249, Register 0x51 [0] = ‘0’.
- NOTE 3: Table 249, Register 0x51 [0] = ‘1’.

## R4C (0x4C) — SWD_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING, SWD_OVER_VOLTAGE_THRESHOLD_SETTING, SWD_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING, SWD_OUTPUT_SOFT_STOP_TIME

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-5 Table 244, p.235

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWD_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING | RWPE | 01 |
| 5:4 | SWD_OVER_VOLTAGE_THRESHOLD_SETTING | RWPE | 10 |
| 3:2 | SWD_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING | RWPE | 00 |
| 1:0 | SWD_OUTPUT_SOFT_STOP_TIME | RWPE | 00 |

### [7:6] SWD_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING

- Description: SWD Output Threshold High Side Voltage For Power Good Status
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 01 → +7.5% from the setting in Table 243, Register 0x4B [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +5% from the setting in Table 243, Register 0x4B [7:1] |
| 01 | +7.5% from the setting in Table 243, Register 0x4B [7:1] |
| 10 | Reserved |
| 11 | Reserved |

### [5:4] SWD_OVER_VOLTAGE_THRESHOLD_SETTING

- Description: SWD Output Regulator Threshold For Over Voltage Status[1]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 10 → +12.5% from the setting in Table 243, Register 0x4B [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +7.5% from the setting in Table 243, Register 0x4B [7:1] |
| 01 | +10% from the setting in Table 243, Register 0x4B [7:1] |
| 10 | +12.5% from the setting in Table 243, Register 0x4B [7:1] |
| 11 | Reserved |

### [3:2] SWD_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING

- Description: SWD Output Regulator Threshold For Under Voltage Lockout Status
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 00 → -10% from the setting in Table 243, Register 0x4B [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | -10% from the setting in Table 243, Register 0x4B [7:1] |
| 01 | -12.5% from the setting in Table 243, Register 0x4B [7:1] |
| 10 | Reserved |
| 11 | Reserved |

### [1:0] SWD_OUTPUT_SOFT_STOP_TIME

- Description: SWD Output Regulator Soft Stop Time After VR Disable[2]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 00 → 1 ms

| Code (bin) | Meaning |
|---|---|
| 00 | 1 ms |
| 01 | 2 ms |
| 10 | 4 ms |
| 11 | 8 ms |

**Notes**

- NOTE 1: The setting for the Over Voltage must be higher than Power Good High Side Voltage threshold in Table 244, Register 0x4C[7:6].
- NOTE 2: This is the time it takes for buck regulator to go from steady state voltage to 0 V.

## R4D (0x4D) — SWA_MODE_SELECT, SWA_SWITCHING_FREQ, SWB_MODE_SELECT, SWB_SWITCHING_FREQ

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-5 Table 245, p.236

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWA_MODE_SELECT | RWPE | 10 |
| 5:4 | SWA_SWITCHING_FREQ | RWPE | 01 |
| 3:2 | SWB_MODE_SELECT | RWPE | 10 |
| 1:0 | SWB_SWITCHING_FREQ | RWPE | 01 |

### [7:6] SWA_MODE_SELECT

- Description: Switch Node A Output Regulator Mode Selection
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 10 → COT; DCM (Constant on Time; Discontinuous Current Mode)

| Code (bin) | Meaning |
|---|---|
| 00 | Reserved |
| 01 | Reserved |
| 10 | COT; DCM (Constant on Time; Discontinuous Current Mode) |
| 11 | COT; CCM (Constant on Time; Continuous Current Mode) |

### [5:4] SWA_SWITCHING_FREQ

- Description: Switch Node A Output Regulator Switching Frequency
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 01 → 750 KHz

| Code (bin) | Meaning |
|---|---|
| 00 | 500 KHz |
| 01 | 750 KHz |
| 10 | Reserved |
| 11 | Reserved |

### [3:2] SWB_MODE_SELECT

- Description: Switch Node B Output Regulator Mode Selection[1]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 10 → COT; DCM (Constant on Time; Discontinuous Current Mode)

| Code (bin) | Meaning |
|---|---|
| 00 | Reserved |
| 01 | Reserved |
| 10 | COT; DCM (Constant on Time; Discontinuous Current Mode) |
| 11 | COT; CCM (Constant on Time; Continuous Current Mode) |

### [1:0] SWB_SWITCHING_FREQ

- Description: Switch Node B Output Regulator Switching Frequency[1]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 01 → 750 KHz

| Code (bin) | Meaning |
|---|---|
| 00 | 500 KHz |
| 01 | 750 KHz |
| 10 | Reserved |
| 11 | Reserved |

**Notes**

- NOTE 1: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care.

## R4E (0x4E) — SWC_MODE_SELECT, SWC_SWITCHING_FREQ, SWD_MODE_SELECT, SWD_SWITCHING_FREQ

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-5 Table 246, p.237

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWC_MODE_SELECT | RWPE | 10 |
| 5:4 | SWC_SWITCHING_FREQ | RWPE | 01 |
| 3:2 | SWD_MODE_SELECT | RWPE | 10 |
| 1:0 | SWD_SWITCHING_FREQ | RWPE | 01 |

### [7:6] SWC_MODE_SELECT

- Description: Switch Node C Output Regulator Mode Selection
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 10 → COT; DCM (Constant on Time; Discontinuous Current Mode)

| Code (bin) | Meaning |
|---|---|
| 00 | Reserved |
| 01 | Reserved |
| 10 | COT; DCM (Constant on Time; Discontinuous Current Mode) |
| 11 | COT; CCM (Constant on Time; Continuous Current Mode) |

### [5:4] SWC_SWITCHING_FREQ

- Description: Switch Node C Output Regulator Switching Frequency
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 01 → 750 KHz

| Code (bin) | Meaning |
|---|---|
| 00 | 500 KHz |
| 01 | 750 KHz |
| 10 | Reserved |
| 11 | Reserved |

### [3:2] SWD_MODE_SELECT

- Description: Switch Node D Output Regulator Mode Selection
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 10 → COT; DCM (Constant on Time; Discontinuous Current Mode)

| Code (bin) | Meaning |
|---|---|
| 00 | Reserved |
| 01 | Reserved |
| 10 | COT; DCM (Constant on Time; Discontinuous Current Mode) |
| 11 | COT; CCM (Constant on Time; Continuous Current Mode) |

### [1:0] SWD_SWITCHING_FREQ

- Description: Switch Node D Output Regulator Switching Frequency
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 01 → 750 KHz

| Code (bin) | Meaning |
|---|---|
| 00 | Reserved |
| 01 | 750 KHz |
| 10 | 1000 KHz |
| 11 | Reserved |

## R4F (0x4F) — SWC_SWF_PHASE_MODE_SELECT, SWA_SWB_SWE_PHASE_MODE_SELECT_MSB, SWA_SWB_PHASE_MODE_SELECT_LSB

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-5 Table 247, p.238

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | RESERVED | RV | 0 |
| 6 | SWC_SWF_PHASE_MODE_SELECT | RWPE | 0 |
| 5 | SWA_SWB_SWE_PHASE_MODE_SELECT_MSB | RWPE | 0 |
| 4:1 | RESERVED | RV | 0 |
| 0 | SWA_SWB_PHASE_MODE_SELECT_LSB | RWPE | 0 |

### [7] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [6] SWC_SWF_PHASE_MODE_SELECT

- Description: SWC and SWF Phase Regulator Mode Selection
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Single Phase Regulator Mode (SWC, SWF)

| Code (bin) | Meaning |
|---|---|
| 0 | Single Phase Regulator Mode (SWC, SWF) |
| 1 | Dual Phase Regulator Mode (SWC+SWF) |

### [5] SWA_SWB_SWE_PHASE_MODE_SELECT_MSB

- Description: SWA, SWB and SWE Phase Regulator Mode Selection. When this bit is set to ‘1’, the setting in bit [0] is a don’t care & PMIC operates in a triple phase regulator mode.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0
- Note: the codes below are wider than this 1-bit field; the encoding combines bits from more than one field/register (see Description).

| Code (bin) | Meaning |
|---|---|
| 00 | Single Phase Regulator Mode (SWA, SWB, SWE) |
| 01 | Dual Phase Regulator Mode (SWA+SWB, SWE is a single phase) |
| 1x | Three Phase Regulator Mode (SWA+SWB+SWE) |

### [4:1] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [0] SWA_SWB_PHASE_MODE_SELECT_LSB

- Description: SWA and SWB Phase Regulator Mode Selection. See the description for bit [5].
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Single Phase Regulator Mode (SWA, SWB)

| Code (bin) | Meaning |
|---|---|
| 0 | Single Phase Regulator Mode (SWA, SWB) |
| 1 | Dual Phase Regulator Mode (SWA+SWB) |

## R50 (0x50) — SWA_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING, SWB_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING, SWC_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING, SWD_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-5 Table 248, p.239

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWA_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING | RWPE | 01 |
| 5:4 | SWB_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING | RWPE | 01 |
| 3:2 | SWC_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING | RWPE | 01 |
| 1:0 | SWD_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING | RWPE | 01 |

### [7:6] SWA_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING

- Description: PMIC5030 COT Mode, Ivalley_limit:
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 01 → 7A

| Code (bin) | Meaning |
|---|---|
| 00 | 6A |
| 01 | 7A |
| 10 | 8A |
| 11 | 9A |

### [5:4] SWB_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING

- Description: PMIC5030 COT Mode, Ivalley_limit[1]:
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 01 → 7A

| Code (bin) | Meaning |
|---|---|
| 00 | 6A |
| 01 | 7A |
| 10 | 8A |
| 11 | 9A |

### [3:2] SWC_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING

- Description: PMIC5030 COT Mode, Ivalley_limit:
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 01 → 7A

| Code (bin) | Meaning |
|---|---|
| 00 | 6A |
| 01 | 7A |
| 10 | 8A |
| 11 | 9A |

### [1:0] SWD_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING

- Description: PMIC5030 COT Mode, Ivalley_limit:
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 01 → 4.5A

| Code (bin) | Meaning |
|---|---|
| 00 | 4A |
| 01 | 4.5A |
| 10 | 5A |
| 11 | 5.5A |

**Notes**

- NOTE 1: This register is applicable regardless of the setting in Table 247, Register 0x4F [5,0].

## R51 (0x51) — VOUT_1.8V_VOLTAGE_SETTING, SWA_VOLTAGE_RANGE, SWB_VOLTAGE_RANGE, SWC_VOLTAGE_RANGE, VOUT_1.0V_VOLTAGE_SETTING, SWD_VOLTAGE_RANGE

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-5 Table 249, p.240

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | VOUT_1.8V_VOLTAGE_SETTING | RWPE | 01 |
| 5 | SWA_VOLTAGE_RANGE | RWPE | 0 |
| 4 | SWB_VOLTAGE_RANGE | RWPE | 0 |
| 3 | SWC_VOLTAGE_RANGE | RWPE | 0 |
| 2:1 | VOUT_1.0V_VOLTAGE_SETTING | RWPE | 01 |
| 0 | SWD_VOLTAGE_RANGE | RWPE | 0 |

### [7:6] VOUT_1.8V_VOLTAGE_SETTING

- Description: VOUT 1.8 V LDO Output Voltage Setting[1]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 01 → 1.8 V

| Code (bin) | Meaning |
|---|---|
| 00 | 1.7 V |
| 01 | 1.8 V |
| 10 | 1.9 V |
| 11 | Reserved |

### [5] SWA_VOLTAGE_RANGE

- Description: SWA Output Voltage Range Selection[2]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Range: 800 mV to 1435 mV for SWA; 5 mV step size.

| Code (bin) | Meaning |
|---|---|
| 0 | Range: 800 mV to 1435 mV for SWA; 5 mV step size. |
| 1 | Range: 600 mV to 1235 mV for SWA; 5 mV step size |

### [4] SWB_VOLTAGE_RANGE

- Description: SWB Output Voltage Range Selection[3],[4]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Range: 800 mV to 1435 mV for SWB; 5 mV step size

| Code (bin) | Meaning |
|---|---|
| 0 | Range: 800 mV to 1435 mV for SWB; 5 mV step size |
| 1 | Range: 600 mV to 1235 mV for SWB; 5 mV step size |

### [3] SWC_VOLTAGE_RANGE

- Description: SWC Output Voltage Range Selection[5]. The MSB bit Table 250, Register 0x52 [0] plus this bit LSB Table 249, Register 0x51 [3] makes 2 bit encoding as following:
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0
- Note: the codes below are wider than this 1-bit field; the encoding combines bits from more than one field/register (see Description).

| Code (bin) | Meaning |
|---|---|
| 00 | Range: 800 mV to 1435 mV for SWC; 5 mV step size |
| 01 | Range: 600 mV to 1235 mV for SWC; 5 mV step size |
| 10 | Range: 400 mV to 717.5 mV for SWC; 2.5 mV step size |
| 11 | Reserved |

### [2:1] VOUT_1.0V_VOLTAGE_SETTING

- Description: VOUT 1.0 V LDO Voltage Setting
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 01 → 1.0 V

| Code (bin) | Meaning |
|---|---|
| 00 | 0.9 V |
| 01 | 1.0 V |
| 10 | 1.1 V |
| 11 | 1.2 V |

### [0] SWD_VOLTAGE_RANGE

- Description: SWD Output Voltage Range Selection[6]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Range: 1500 mV to 2135 mV for SWD; 5 mV step size

| Code (bin) | Meaning |
|---|---|
| 0 | Range: 1500 mV to 2135 mV for SWD; 5 mV step size |
| 1 | Range: 2200 mV to 2835 mV for SWD; 5 mV step size |

**Notes**

- NOTE 1: The VOUT_1.8V Power Good threshold in register Table 131, Register 0x1A [2] is always fixed regardless of the setting in this register.
- NOTE 2: Range selection applies to registers Table 237, Register 0x45 [7:1].
- NOTE 3: Range selection applies to registers Table 239, Register 0x47 [7:1].
- NOTE 4: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care.
- NOTE 5: Range selection applies to registers Table 241, Register 0x49 [7:1].
- NOTE 6: Range selection applies to registers Table 243, Register 0x4B [7:1].

## R52 (0x52) — SWE_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING, SWF_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING, SWE_VOLTAGE_RANGE, SWF_VOLTAGE_RANGE, SWC_VOLTAGE_RANGE_EXT

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-5 Table 250, p.241

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWE_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING | RWPE | 01 |
| 5:4 | SWF_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING | RWPE | 01 |
| 3 | SWE_VOLTAGE_RANGE | RWPE | 0 |
| 2:1 | SWF_VOLTAGE_RANGE | RWPE | 0 |
| 0 | SWC_VOLTAGE_RANGE_EXT | RWPE | 0 |

### [7:6] SWE_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING

- Description: PMIC5030 COT Mode, Ivalley_limit[1]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 01 → 7A

| Code (bin) | Meaning |
|---|---|
| 00 | 6A |
| 01 | 7A |
| 10 | 8A |
| 11 | 9A |

### [5:4] SWF_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING

- Description: PMIC5030 COT Mode, Ivalley_limit[2]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 01 → 7A

| Code (bin) | Meaning |
|---|---|
| 00 | 6A |
| 01 | 7A |
| 10 | 8A |
| 11 | 9A |

### [3] SWE_VOLTAGE_RANGE

- Description: SWE Output Voltage Range Selection[3],[4]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Range: 800 mV to 1435 mV for SWA; 5 mV step size.

| Code (bin) | Meaning |
|---|---|
| 0 | Range: 800 mV to 1435 mV for SWA; 5 mV step size. |
| 1 | Range: 600 mV to 1235 mV for SWA; 5 mV step size |

### [2:1] SWF_VOLTAGE_RANGE

- Description: SWF Output Voltage Range Selection[5],[6]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 00 | Range: 800 mV to 1435 mV for SWF; 5 mV step size |
| 01 | Range: 600 mV to 1235 mV for SWF; 5 mV step size |
| 10 | Range: 400 mV to 717.5 mV for SWF; 2.5 mV step size |
| 11 | Reserved |

### [0] SWC_VOLTAGE_RANGE_EXT

- Description: SWC Output Voltage Range Selection[7]. This bit MSB plus Table 249, Register 0x51 [3] as LSB bit makes 2 bit encoding as following:
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0
- Note: the codes below are wider than this 1-bit field; the encoding combines bits from more than one field/register (see Description).

| Code (bin) | Meaning |
|---|---|
| 00 | Range: 800 mV to 1435 mV for SWC; 5 mV step size |
| 01 | Range: 600 mV to 1235 mV for SWC; 5 mV step size |
| 10 | Range: 400 mV to 717.5 mV for SWC; 2.5 mV step size |
| 11 | Reserved |

**Notes**

- NOTE 1: This register is applicable regardless of the setting in Table 247, Register 0x4F [5,0].
- NOTE 2: This register is applicable regardless of the setting in Table 247, Register 0x4F [6].
- NOTE 3: Range selection applies to registers Table 251, Register 0x53 [7:1].
- NOTE 4: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’ or ‘01’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care.
- NOTE 5: Range selection applies to registers Table 253, Register 0x55 [7:1].
- NOTE 6: This register is only applicable if Table 247, Register 0x4F [6] = ‘0’. For any other setting in Table 247, Register 0x4F [6], this register does not apply and it is a don’t care.
- NOTE 7: Range selection applies to registers Table 241, Register 0x49 [7:1].

## R53 (0x53) — SWE_VOLTAGE_SETTING, SWE_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-5 Table 251, p.242

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:1 | SWE_VOLTAGE_SETTING | RWPE | 011 1100 |
| 0 | SWE_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING | RWPE | 0 |

### [7:1] SWE_VOLTAGE_SETTING

- Description: SWE Output Regulator Voltage Setting[2]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 011 1100 → 1100 mV or 900 mV

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 0000000 | 0x00 | 800 mV[3] or 600 mV[4] |
| 0000001 | 0x01 | 805 mV or 605 mV |
| 0000010 | 0x02 | 810 mV or 610 mV |
| ... | ... | ... |
| 0111100 | 0x3C | 1100 mV or 900 mV |
| ... | ... | ... |
| 1111101 | 0x7D | 1425 mV or 1225 mV |
| 1111110 | 0x7E | 1430 mV or 1230 mV |
| 1111111 | 0x7F | 1435 mV or 1235 mV |

### [0] SWE_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

- Description: SWE Output Threshold Low Side Voltage For Power Good Status
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → - 5% from the setting in Table 251, Register 0x53 [7:1]

| Code (bin) | Meaning |
|---|---|
| 0 | - 5% from the setting in Table 251, Register 0x53 [7:1] |
| 1 | - 7.5% from the setting in Table 251, Register 0x53 [7:1] |

**Notes**

- NOTE 1: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’ or ‘01’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care.
- NOTE 2: PMIC guarantees efficiency spec within a range of 1050 mV to 1160 mV.
- NOTE 3: Table 250, Register 0x52 [3] = ‘0’.
- NOTE 4: Table 250, Register 0x52 [3] = ‘1’.

## R54 (0x54) — SWE_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING, SWE_OVER_VOLTAGE_THRESHOLD_SETTING, SWE_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING, SWE_OUTPUT_SOFT_STOP_TIME

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-5 Table 252, p.243

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWE_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING | RWPE | 01 |
| 5:4 | SWE_OVER_VOLTAGE_THRESHOLD_SETTING | RWPE | 10 |
| 3:2 | SWE_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING | RWPE | 00 |
| 1:0 | SWE_OUTPUT_SOFT_STOP_TIME | RWPE | 00 |

### [7:6] SWE_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING

- Description: Switch Node E Output Threshold High Side Voltage For Power Good Status
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 01 → +7.5% from the setting in Table 251, Register 0x53 [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +5% from the setting in Table 251, Register 0x53 [7:1] |
| 01 | +7.5% from the setting in Table 251, Register 0x53 [7:1] |
| 10 | +10% from the setting in Table 251, Register 0x53 [7:1] |
| 11 | Reserved |

### [5:4] SWE_OVER_VOLTAGE_THRESHOLD_SETTING

- Description: Switch Node E Output Regulator Threshold For Over Voltage Status[2]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 10 → +12.5% from the setting in Table 251, Register 0x53 [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +7.5% from the setting in Table 251, Register 0x53 [7:1] |
| 01 | +10% from the setting in Table 251, Register 0x53 [7:1] |
| 10 | +12.5% from the setting in Table 251, Register 0x53 [7:1] |
| 11 | Reserved |

### [3:2] SWE_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING

- Description: Switch Node E Output Regulator Threshold For Under Voltage Lockout Status
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 00 → -10% from the setting in Table 251, Register 0x53 [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | -10% from the setting in Table 251, Register 0x53 [7:1] |
| 01 | -12.5% from the setting in Table 251, Register 0x53 [7:1] |
| 10 | Reserved |
| 11 | Reserved |

### [1:0] SWE_OUTPUT_SOFT_STOP_TIME

- Description: SWE Output Regulator Soft Stop Time After VR Disable[3]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 00 → 0.5 ms

| Code (bin) | Meaning |
|---|---|
| 00 | 0.5 ms |
| 01 | 1 ms |
| 10 | 2 ms |
| 11 | 4 ms |

**Notes**

- NOTE 1: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’ or ‘01’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care.
- NOTE 2: The setting for the Over Voltage threshold must be higher than Power Good High Side Voltage threshold in Table 252, Register 0x54[7:6].
- NOTE 3: This is the time it takes for buck regulator to go from steady state voltage to 0 V.

## R55 (0x55) — SWF_VOLTAGE_SETTING, SWF_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-5 Table 253, p.244

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:1 | SWF_VOLTAGE_SETTING | RWPE | 011 1100 |
| 0 | SWF_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING | RWPE | 0 |

### [7:1] SWF_VOLTAGE_SETTING

- Description: SWF Output Regulator Voltage Setting[2]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 011 1100 → 1100 mV or 900 mV or 550 mV

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 0000000 | 0x00 | 800 mV[3] or 600 mV[4] or 400 mV[5] |
| 0000001 | 0x01 | 805 mV or 605 mV or 402.5 mV |
| 0000010 | 0x02 | 810 mV or 610 mV or 405 mV |
| ... | ... | ... |
| 0111100 | 0x3C | 1100 mV or 900 mV or 550 mV |
| ... | ... | ... |
| 1111101 | 0x7D | 1425 mV or 1225 mV or 712.5 mV |
| 1111110 | 0x7E | 1430 mV or 1230 mV or 715 mV |
| 1111111 | 0x7F | 1435 mV or 1235 mV or 717.5 mV |

### [0] SWF_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

- Description: SWF Output Threshold Low Side Voltage For Power Good Status
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → -5% from the setting in Table 253, Register 0x55 [7:1]

| Code (bin) | Meaning |
|---|---|
| 0 | -5% from the setting in Table 253, Register 0x55 [7:1] |
| 1 | -7.5% from the setting in Table 253, Register 0x55 [7:1] |

**Notes**

- NOTE 1: This register is only applicable if Table 247, Register 0x4F [6] = ‘0’. For any other setting in Table 247, Register 0x4F [6], this register does not apply and it is a don’t care.
- NOTE 2: PMIC guarantees efficiency spec within a range of 1050 mV to 1160 mV.
- NOTE 3: Table 250, Register 0x52 [2:1] = ‘00’; 5 mV step size.
- NOTE 4: Table 250, Register 0x52 [2:1] = ‘01’; 5 mV step size.
- NOTE 5: Table 250, Register 0x52 [2:1] = ‘10’; 2.5 mV step size.

## R56 (0x56) — SWF_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING, SWF_OVER_VOLTAGE_THRESHOLD_SETTING, SWF_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING, SWF_OUTPUT_SOFT_STOP_TIME

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-5 Table 254, p.245

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWF_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING | RWPE | 01 |
| 5:4 | SWF_OVER_VOLTAGE_THRESHOLD_SETTING | RWPE | 10 |
| 3:2 | SWF_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING | RWPE | 00 |
| 1:0 | SWF_OUTPUT_SOFT_STOP_TIME | RWPE | 00 |

### [7:6] SWF_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING

- Description: SWF Output Threshold High Side Voltage For Power Good Status
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 01 → +7.5% from the setting in Table 253, Register 0x55 [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +5% from the setting in Table 253, Register 0x55 [7:1] |
| 01 | +7.5% from the setting in Table 253, Register 0x55 [7:1] |
| 10 | +10% from the setting in Table 253, Register 0x55 [7:1] |
| 11 | Reserved |

### [5:4] SWF_OVER_VOLTAGE_THRESHOLD_SETTING

- Description: SWF Output Regulator Threshold For Over Voltage Status[2]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 10 → +12.5% from the setting in Table 253, Register 0x55 [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +7.5% from the setting in Table 253, Register 0x55 [7:1] |
| 01 | +10% from the setting in Table 253, Register 0x55 [7:1] |
| 10 | +12.5% from the setting in Table 253, Register 0x55 [7:1] |
| 11 | Reserved |

### [3:2] SWF_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING

- Description: SWF Output Regulator Threshold For Under Voltage Lockout Status
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 00 → -10% from the setting in Table 253, Register 0x55 [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | -10% from the setting in Table 253, Register 0x55 [7:1] |
| 01 | -12.5% from the setting in Table 253, Register 0x55 [7:1] |
| 10 | Reserved |
| 11 | Reserved |

### [1:0] SWF_OUTPUT_SOFT_STOP_TIME

- Description: SWF Output Regulator Soft Stop Time After VR Disable[3]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 00 → 0.5 ms

| Code (bin) | Meaning |
|---|---|
| 00 | 0.5 ms |
| 01 | 1 ms |
| 10 | 2 ms |
| 11 | 4 ms |

**Notes**

- NOTE 1: This register is only applicable if Table 247, Register 0x4F [6] = ‘0’. For any other setting in Table 247, Register 0x4F [6], this register does not apply and it is a don’t care.
- NOTE 2: The setting for the Over Voltage must threshold be higher than Power Good High Side Voltage threshold in Table 254, Register 0x56 [7:6].
- NOTE 3: This is the time it takes for buck regulator to go from steady state voltage to 0 V.

## R57 (0x57) — SWE_MODE_SELECT, SWE_SWITCHING_FREQ, SWF_MODE_SELECT, SWF_SWITCHING_FREQ

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-5 Table 255, p.246

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWE_MODE_SELECT | RWPE | 10 |
| 5:4 | SWE_SWITCHING_FREQ | RWPE | 01 |
| 3:2 | SWF_MODE_SELECT | RWPE | 10 |
| 1:0 | SWF_SWITCHING_FREQ | RWPE | 01 |

### [7:6] SWE_MODE_SELECT

- Description: Switch Node E Output Regulator Mode Selection[1]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 10 → COT; DCM (Constant on Time; Discontinuous Current Mode)

| Code (bin) | Meaning |
|---|---|
| 00 | Reserved |
| 01 | Reserved |
| 10 | COT; DCM (Constant on Time; Discontinuous Current Mode) |
| 11 | COT; CCM (Constant on Time; Continuous Current Mode) |

### [5:4] SWE_SWITCHING_FREQ

- Description: Switch Node E Output Regulator Switching Frequency[1]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 01 → 750 KHz

| Code (bin) | Meaning |
|---|---|
| 00 | 500 KHz |
| 01 | 750 KHz |
| 10 | Reserved |
| 11 | Reserved |

### [3:2] SWF_MODE_SELECT

- Description: Switch Node F Output Regulator Mode Selection[2]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 10 → COT; DCM (Constant on Time; Discontinuous Current Mode)

| Code (bin) | Meaning |
|---|---|
| 00 | Reserved |
| 01 | Reserved |
| 10 | COT; DCM (Constant on Time; Discontinuous Current Mode) |
| 11 | COT; CCM (Constant on Time; Continuous Current Mode) |

### [1:0] SWF_SWITCHING_FREQ

- Description: Switch Node F Output Regulator Switching Frequency[2]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 01 → 750 KHz

| Code (bin) | Meaning |
|---|---|
| 00 | 500 KHz |
| 01 | 750 KHz |
| 10 | Reserved |
| 11 | Reserved |

**Notes**

- NOTE 1: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’ or ‘01’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care.
- NOTE 2: This register is only applicable if Table 247, Register 0x4F [6] = ‘0’. For any other setting in Table 247, Register 0x4F [6], this register does not apply and it is a don’t care.

## R58 (0x58) — POWER_OFF_SEQUENCE_CONFIG0, POWER_OFF_SEQUENCE_CONFIG0_SWA_DISABLE, POWER_OFF_SEQUENCE_CONFIG0_SWB_DISABLE, POWER_OFF_SEQUENCE_CONFIG0_SWC_DISABLE, POWER_OFF_SEQUENCE_CONFIG0_SWD_DISABLE, POWER_OFF_SEQUENCE_CONFIG0_IDLE

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-5 Table 256, p.247

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | POWER_OFF_SEQUENCE_CONFIG0 | RWPE | 0 |
| 6 | POWER_OFF_SEQUENCE_CONFIG0_SWA_DISABLE | RWPE | 0 |
| 5 | POWER_OFF_SEQUENCE_CONFIG0_SWB_DISABLE | RWPE | 0 |
| 4 | POWER_OFF_SEQUENCE_CONFIG0_SWC_DISABLE | RWPE | 0 |
| 3 | POWER_OFF_SEQUENCE_CONFIG0_SWD_DISABLE | RWPE | 0 |
| 2:0 | POWER_OFF_SEQUENCE_CONFIG0_IDLE | RWPE | 0 |

### [7] POWER_OFF_SEQUENCE_CONFIG0

- Description: PMIC Power Off Sequence Config 0[3]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Do Not Execute Config 0

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Execute Config 0 |
| 1 | Execute Config 0 |

### [6] POWER_OFF_SEQUENCE_CONFIG0_SWA_DISABLE

- Description: Disable SWA Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Disable SWA Output Regulator |

### [5] POWER_OFF_SEQUENCE_CONFIG0_SWB_DISABLE

- Description: Disable Switch Node B Output Regulator.[4]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Disable SWB Output Regulator |

### [4] POWER_OFF_SEQUENCE_CONFIG0_SWC_DISABLE

- Description: Disable Switch Node C Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Disable SWC Output Regulator |

### [3] POWER_OFF_SEQUENCE_CONFIG0_SWD_DISABLE

- Description: Disable SWD Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Disable SWD Output Regulator |

### [2:0] POWER_OFF_SEQUENCE_CONFIG0_IDLE

- Description: Idle time after Power Off Sequence Config 0[5]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 000 | 0 ms |
| 001 | 1 ms |
| 010 | 2 ms |
| 011 | 3 ms |
| 100 | 4 ms |
| 101 | 5 ms |
| 110 | 6 ms |
| 111 | 7 ms |

**Notes**

- NOTE 1: The PMIC always starts with power off sequence configuration 0 register and executes remaining power off sequence configuration registers (1 to 5) in sequential order.
- NOTE 2: Power off sequence configuration 0 is total of 10 bit register. 8 bits as shown in Table 256, Register 0x58 [7:0] plus 2 bits in Table 269, Register 0x65 [7:6].
- NOTE 3: If bit [7] = ‘0’, bits [6:0] and Table 269, Register 0x65 [7:6] are ignored and PMIC moves to next power off sequence configuration register. If bit [7] = ‘1’, PMIC executes bits [6:0] and Table 269, Register 0x65 [7:6] as configured; if no new rail is turned off, the PMIC simply waits the idle time as configured and then moves to next power off sequence configuration register.
- NOTE 4: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care.
- NOTE 5: Idle time is the additional time after soft-stop time expires. The PMIC waits sum of soft stop time and idle time before it executes the next power off sequence configuration register. If more than one regulators are disabled, the PMIC uses the largest value of the soft stop time among the regulators that are disabled in this configuration register.

## R59 (0x59) — POWER_OFF_SEQUENCE_CONFIG1, POWER_OFF_SEQUENCE_CONFIG1_SWA_DISABLE, POWER_OFF_SEQUENCE_CONFIG1_SWB_DISABLE, POWER_OFF_SEQUENCE_CONFIG1_SWC_DISABLE, POWER_OFF_SEQUENCE_CONFIG1_SWD_DISABLE, POWER_OFF_SEQUENCE_CONFIG1_IDLE

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-5 Table 257, p.248

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | POWER_OFF_SEQUENCE_CONFIG1 | RWPE | 0 |
| 6 | POWER_OFF_SEQUENCE_CONFIG1_SWA_DISABLE | RWPE | 0 |
| 5 | POWER_OFF_SEQUENCE_CONFIG1_SWB_DISABLE | RWPE | 0 |
| 4 | POWER_OFF_SEQUENCE_CONFIG1_SWC_DISABLE | RWPE | 0 |
| 3 | POWER_OFF_SEQUENCE_CONFIG1_SWD_DISABLE | RWPE | 0 |
| 2:0 | POWER_OFF_SEQUENCE_CONFIG1_IDLE | RWPE | 0 |

### [7] POWER_OFF_SEQUENCE_CONFIG1

- Description: PMIC Power Off Sequence Config1[3]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Do Not Execute Config 1

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Execute Config 1 |
| 1 | Execute Config 1 |

### [6] POWER_OFF_SEQUENCE_CONFIG1_SWA_DISABLE

- Description: Disable SWA Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Disable SWA Output Regulator |

### [5] POWER_OFF_SEQUENCE_CONFIG1_SWB_DISABLE

- Description: Disable Switch Node B Output Regulator.[4]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Disable SWB Output Regulator |

### [4] POWER_OFF_SEQUENCE_CONFIG1_SWC_DISABLE

- Description: Disable Switch Node C Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Disable SWC Output Regulator |

### [3] POWER_OFF_SEQUENCE_CONFIG1_SWD_DISABLE

- Description: Disable Switch Node D Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Disable SWD Output Regulator |

### [2:0] POWER_OFF_SEQUENCE_CONFIG1_IDLE

- Description: Idle time after Power Off Sequence Config 1[5]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 000 | 0 ms |
| 001 | 1 ms |
| 010 | 2 ms |
| 011 | 3 ms |
| 100 | 4 ms |
| 101 | 5 ms |
| 110 | 6 ms |
| 111 | 7 ms |

**Notes**

- NOTE 1: The PMIC always starts with power off sequence configuration 0 register and executes remaining power off sequence configuration registers (1 to 5) in sequential order.
- NOTE 2: Power off sequence configuration 1 is total of 10 bit register. 8 bits as shown in Table 257, Register 0x59 [7:0] plus 2 bits in Table 269, Register 0x65 [5:4].
- NOTE 3: If bit [7] = ‘0’, bits [6:0] and Table 269, Register 0x65 [5:4] are ignored and PMIC moves to next power off sequence configuration register. If bit [7] = ‘1’, PMIC executes bits [6:0] and Table 269, Register 0x65 [5:4] as configured; if no new rail is turned off, the PMIC simply waits the idle time as configured and then moves to next power off sequence configuration register.
- NOTE 4: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care.
- NOTE 5: Idle time is the additional time after soft-stop time expires. The PMIC waits sum of soft stop time and idle time before it executes the next power off sequence configuration register. If more than one regulators are disabled, the PMIC uses the largest value of the soft stop time among the regulators that are disabled in this configuration register.

## R5A (0x5A) — POWER_OFF_SEQUENCE_CONFIG2, POWER_OFF_SEQUENCE_CONFIG2_SWA_DISABLE, POWER_OFF_SEQUENCE_CONFIG2_SWB_DISABLE, POWER_OFF_SEQUENCE_CONFIG2_SWC_DISABLE, POWER_OFF_SEQUENCE_CONFIG2_SWD_DISABLE, POWER_OFF_SEQUENCE_CONFIG2_IDLE

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-5 Table 258, p.249

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | POWER_OFF_SEQUENCE_CONFIG2 | RWPE | 0 |
| 6 | POWER_OFF_SEQUENCE_CONFIG2_SWA_DISABLE | RWPE | 0 |
| 5 | POWER_OFF_SEQUENCE_CONFIG2_SWB_DISABLE | RWPE | 0 |
| 4 | POWER_OFF_SEQUENCE_CONFIG2_SWC_DISABLE | RWPE | 0 |
| 3 | POWER_OFF_SEQUENCE_CONFIG2_SWD_DISABLE | RWPE | 0 |
| 2:0 | POWER_OFF_SEQUENCE_CONFIG2_IDLE | RWPE | 0 |

### [7] POWER_OFF_SEQUENCE_CONFIG2

- Description: PMIC Power Off Sequence Config 2[3]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Do Not Execute Config 2

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Execute Config 2 |
| 1 | Execute Config 2 |

### [6] POWER_OFF_SEQUENCE_CONFIG2_SWA_DISABLE

- Description: Disable SWA Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Disable SWA Output Regulator |

### [5] POWER_OFF_SEQUENCE_CONFIG2_SWB_DISABLE

- Description: Disable Switch Node B Output Regulator.[4]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Disable SWB Output Regulator |

### [4] POWER_OFF_SEQUENCE_CONFIG2_SWC_DISABLE

- Description: Disable Switch Node C Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Disable SWC Output Regulator |

### [3] POWER_OFF_SEQUENCE_CONFIG2_SWD_DISABLE

- Description: Disable Switch Node D Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Disable SWD Output Regulator |

### [2:0] POWER_OFF_SEQUENCE_CONFIG2_IDLE

- Description: Idle time after Power Off Sequence Config 2[5]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 000 | 0 ms |
| 001 | 1 ms |
| 010 | 2 ms |
| 011 | 3 ms |
| 100 | 4 ms |
| 101 | 5 ms |
| 110 | 6 ms |
| 111 | 7 ms |

**Notes**

- NOTE 1: The PMIC always starts with power off sequence configuration 0 register and executes remaining power off sequence configuration registers (1 to 5) in sequential order.
- NOTE 2: Power off sequence configuration 2 is total of 10 bit register. 8 bits as shown in Table 258, Register 0x5A [7:0] plus 2 bits in Table 269, Register 0x65 [3:2].
- NOTE 3: If bit [7] = ‘0’, bits [6:0] and Table 269, Register 0x65 [3:2] are ignored and PMIC moves to next power off sequence configuration register. If bit [7] = ‘1’, PMIC executes bits [6:0] and Table 269, Register 0x65 [3:2] as configured; if no new rail is turned off, the PMIC simply waits the idle time as configured and then moves to next power off sequence configuration register.
- NOTE 4: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care.
- NOTE 5: Idle time is the additional time after soft-stop time expires. The PMIC waits sum of soft stop time and idle time before it executes the next power off sequence configuration register. If more than one regulators are disabled, the PMIC uses the largest value of the soft stop time among the regulators that are disabled in this configuration register.

## R5B (0x5B) — POWER_OFF_SEQUENCE_CONFIG3, POWER_OFF_SEQUENCE_CONFIG3_SWA_DISABLE, POWER_OFF_SEQUENCE_CONFIG3_SWB_DISABLE, POWER_OFF_SEQUENCE_CONFIG3_SWC_DISABLE, POWER_OFF_SEQUENCE_CONFIG3_SWD_DISABLE, POWER_OFF_SEQUENCE_CONFIG3_IDLE

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-5 Table 259, p.250

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | POWER_OFF_SEQUENCE_CONFIG3 | RWPE | 0 |
| 6 | POWER_OFF_SEQUENCE_CONFIG3_SWA_DISABLE | RWPE | 0 |
| 5 | POWER_OFF_SEQUENCE_CONFIG3_SWB_DISABLE | RWPE | 0 |
| 4 | POWER_OFF_SEQUENCE_CONFIG3_SWC_DISABLE | RWPE | 0 |
| 3 | POWER_OFF_SEQUENCE_CONFIG3_SWD_DISABLE | RWPE | 0 |
| 2:0 | POWER_OFF_SEQUENCE_CONFIG3_IDLE | RWPE | 0 |

### [7] POWER_OFF_SEQUENCE_CONFIG3

- Description: PMIC Power Off Sequence Config 3[3]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Do Not Execute Config 3

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Execute Config 3 |
| 1 | Execute Config 3 |

### [6] POWER_OFF_SEQUENCE_CONFIG3_SWA_DISABLE

- Description: Disable SWA Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Disable SWA Output Regulator |

### [5] POWER_OFF_SEQUENCE_CONFIG3_SWB_DISABLE

- Description: Disable SWB Output Regulator.[4]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Disable SWB Output Regulator |

### [4] POWER_OFF_SEQUENCE_CONFIG3_SWC_DISABLE

- Description: Disable Switch Node C Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Disable SWC Output Regulator |

### [3] POWER_OFF_SEQUENCE_CONFIG3_SWD_DISABLE

- Description: Disable Switch Node D Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Disable SWD Output Regulator |

### [2:0] POWER_OFF_SEQUENCE_CONFIG3_IDLE

- Description: Idle time after Power Off Sequence Config 3[5]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 000 | 0 ms |
| 001 | 1 ms |
| 010 | 2 ms |
| 011 | 3 ms |
| 100 | 4 ms |
| 101 | 5 ms |
| 110 | 6 ms |
| 111 | 7 ms |

**Notes**

- NOTE 1: The PMIC always starts with power off sequence configuration 0 register and executes remaining power off sequence configuration registers (1 to 5) in sequential order.
- NOTE 2: Power off sequence configuration 3 is total of 10 bit register. 8 bits as shown in Table 259, Register 0x5B [7:0] plus 2 bits in Table 269, Register 0x65 [1:0].
- NOTE 3: If bit [7] = ‘0’, bits [6:0] and Table 269, Register 0x65 [1:0] are ignored and PMIC moves to next power off sequence configuration register. If bit [7] = ‘1’, PMIC executes bits [6:0] and Table 269, Register 0x65 [1:0] as configured; if no new rail is turned off, the PMIC simply waits the idle time as configured and then moves to next power off sequence configuration register.
- NOTE 4: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care.
- NOTE 5: Idle time is the additional time after soft-stop time expires. The PMIC waits sum of soft stop time and idle time before it executes the next power off sequence configuration register. If more than one regulators are disabled, the PMIC uses the largest value of the soft stop time among the regulators that are disabled in this configuration register.

## R5C (0x5C) — POWER_OFF_SEQUENCE_CONFIG4, POWER_OFF_SEQUENCE_CONFIG4_SWA_DISABLE, POWER_OFF_SEQUENCE_CONFIG4_SWB_DISABLE, POWER_OFF_SEQUENCE_CONFIG4_SWC_DISABLE, POWER_OFF_SEQUENCE_CONFIG4_SWD_DISABLE, POWER_OFF_SEQUENCE_CONFIG4_IDLE

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-5 Table 260, p.251

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | POWER_OFF_SEQUENCE_CONFIG4 | RWPE | 0 |
| 6 | POWER_OFF_SEQUENCE_CONFIG4_SWA_DISABLE | RWPE | 0 |
| 5 | POWER_OFF_SEQUENCE_CONFIG4_SWB_DISABLE | RWPE | 0 |
| 4 | POWER_OFF_SEQUENCE_CONFIG4_SWC_DISABLE | RWPE | 0 |
| 3 | POWER_OFF_SEQUENCE_CONFIG4_SWD_DISABLE | RWPE | 0 |
| 2:0 | POWER_OFF_SEQUENCE_CONFIG4_IDLE | RWPE | 0 |

### [7] POWER_OFF_SEQUENCE_CONFIG4

- Description: PMIC Power Off Sequence Config 4[3]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Do Not Execute Config 4

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Execute Config 4 |
| 1 | Execute Config 4 |

### [6] POWER_OFF_SEQUENCE_CONFIG4_SWA_DISABLE

- Description: Disable SWA Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Disable SWA Output Regulator |

### [5] POWER_OFF_SEQUENCE_CONFIG4_SWB_DISABLE

- Description: Disable SWB Output Regulator.[4]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Disable SWB Output Regulator |

### [4] POWER_OFF_SEQUENCE_CONFIG4_SWC_DISABLE

- Description: Disable Switch Node C Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Disable SWC Output Regulator |

### [3] POWER_OFF_SEQUENCE_CONFIG4_SWD_DISABLE

- Description: Disable Switch Node D Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Disable SWD Output Regulator |

### [2:0] POWER_OFF_SEQUENCE_CONFIG4_IDLE

- Description: Idle time after Power Off Sequence Config 4[5]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 000 | 0 ms |
| 001 | 1 ms |
| 010 | 2 ms |
| 011 | 3 ms |
| 100 | 4 ms |
| 101 | 5 ms |
| 110 | 6 ms |
| 111 | 7 ms |

**Notes**

- NOTE 1: The PMIC always starts with power off sequence configuration 0 register and executes remaining power off sequence configuration registers (1 to 5) in sequential order.
- NOTE 2: Power off sequence configuration 4 is total of 10 bit register. 8 bits as shown in Table 260, Register 0x5C [7:0] plus 2 bits in Table 270, Register 0x66 [7:6].
- NOTE 3: If bit [7] = ‘0’, bits [6:0] and Table 270, Register 0x66 [7:6] are ignored and PMIC moves to next power off sequence configuration register. If bit [7] = ‘1’, PMIC executes bits [6:0] and Table 270, Register 0x66 [7:6] as configured; if no new rail is turned off, the PMIC simply waits the idle time as configured and then moves to next power off sequence configuration register.
- NOTE 4: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care.
- NOTE 5: Idle time is the additional time after soft-stop time expires. The PMIC waits sum of soft stop time and idle time before it executes the next power off sequence configuration register. If more than one regulators are disabled, the PMIC uses the largest value of the soft stop time among the regulators that are disabled in this configuration register.

## R5D (0x5D) — SWA_OUTPUT_SOFT_START_TIME, SWB_OUTPUT_SOFT_START_TIME

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-5 Table 261, p.252

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:5 | SWA_OUTPUT_SOFT_START_TIME | RWPE | 001 |
| 4 | RESERVED | RV | 0 |
| 3:1 | SWB_OUTPUT_SOFT_START_TIME | RWPE | 001 |
| 0 | RESERVED | RV | 0 |

### [7:5] SWA_OUTPUT_SOFT_START_TIME

- Description: SWA Output Regulator Soft Start Time After VR Enable[1]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 001 → 2 ms

| Code (bin) | Meaning |
|---|---|
| 000 | 1 ms |
| 001 | 2 ms |
| 010 | 4 ms |
| 011 | 6 ms |
| ... | ... |
| 111 | 14 ms |

### [4] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [3:1] SWB_OUTPUT_SOFT_START_TIME

- Description: SWB Output Regulator Soft Start Time After VR Enable[1],[2]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 001 → 2 ms

| Code (bin) | Meaning |
|---|---|
| 000 | 1 ms |
| 001 | 2 ms |
| 010 | 4 ms |
| 011 | 6 ms |
| ... | ... |
| 111 | 14 ms |

### [0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

**Notes**

- NOTE 1: This is the time it takes for buck regulator to go from 0 V to steady state voltage (the actual voltage varies based on pre-programmed voltage).
- NOTE 2: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care.

## R5E (0x5E) — SWC_OUTPUT_SOFT_START_TIME, SWD_OUTPUT_SOFT_START_TIME

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-5 Table 262, p.253

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:5 | SWC_OUTPUT_SOFT_START_TIME | RWPE | 001 |
| 4 | RESERVED | RV | 0 |
| 3:1 | SWD_OUTPUT_SOFT_START_TIME | RWPE | 001 |
| 0 | RESERVED | RV | 0 |

### [7:5] SWC_OUTPUT_SOFT_START_TIME

- Description: SWC Output Regulator Soft Start Time After VR Enable[1]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 001 → 2 ms

| Code (bin) | Meaning |
|---|---|
| 000 | 1 ms |
| 001 | 2 ms |
| 010 | 4 ms |
| 011 | 6 ms |
| ... | ... |
| 111 | 14 ms |

### [4] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [3:1] SWD_OUTPUT_SOFT_START_TIME

- Description: SWD Output Regulator Soft Start Time After VR Enable[1]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 001 → 2 ms

| Code (bin) | Meaning |
|---|---|
| 000 | 1 ms |
| 001 | 2 ms |
| 010 | 4 ms |
| 011 | 6 ms |
| ... | ... |
| 111 | 14 ms |

### [0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

**Notes**

- NOTE 1: This is the time it takes for buck regulator to go from 0 V to steady state voltage (the actual voltage varies based on pre-programmed voltage)

## R5F (0x5F) — R2F_2_CONTROL, PMIC_AUTO_POWER_EN, VR_OE_ENABLE, R32_4_CONTROL

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-5 Table 263, p.254

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | R2F_2_CONTROL | RWPE | 0 |
| 6 | PMIC_AUTO_POWER_EN | RWPE | 0 |
| 5 | VR_OE_ENABLE | RWPE | 0 |
| 4 | R32_4_CONTROL | RWPE | 0 |
| 3:0 | RESERVED | RV | 0 |

### [7] R2F_2_CONTROL

- Description: Host Region R2F[2] Register Setting at First Power On
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → R2F[2] = ‘0’

| Code (bin) | Meaning |
|---|---|
| 0 | R2F[2] = ‘0’ |
| 1 | R2F[2] = ‘1’ |

### [6] PMIC_AUTO_POWER_EN

- Description: PMIC Auto Power On Control[1],[2]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → PMIC requires VR Enable command to turn on output rails

| Code (bin) | Meaning |
|---|---|
| 0 | PMIC requires VR Enable command to turn on output rails |
| 1 | PMIC automatically powers on output rails as soon as it detects valid VIN_Bulk and VIN_Mgmt input supplies[3] |

### [5] VR_OE_ENABLE

- Description: VR Output Enable
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → VR OE pin function is disabled[4],[5]

| Code (bin) | Meaning |
|---|---|
| 0 | VR OE pin function is disabled[4],[5] |
| 1 | VR OE pin function is enabled. PMIC turns on SWx when VR_OE pin is asserted High and turns off the SWx when VR_OE pin is de-asserted[6] |

### [4] R32_4_CONTROL

- Description: Host Region R32[4] Register Setting at First Power On
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → R32[4] = ‘0’

| Code (bin) | Meaning |
|---|---|
| 0 | R32[4] = ‘0’ |
| 1 | R32[4] = ‘1’ |

### [3:0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

**Notes**

- NOTE 1: The PMIC considers the setting of bits [6:5] = ‘11’ as illegal.
- NOTE 2: When this feature is enabled, it takes in effect at next power cycle.
- NOTE 3: Once the PMIC output rails are powered up, if there is a subsequent VR Disable command or a fault event, the PMIC output regulators remains off until subsequent VR Enable command.
- NOTE 4: When this feature is enabled, the VR_OE input pin must be held low. The enable function takes in effect at next power cycle.
- NOTE 5: PMIC does not turn on the rail when VR_OE pin is high however the PMIC does turn off the regulator when VR_OE pin is low. The PMIC is prevented from turning on the regulators as long as VR_OE pin is low.
- NOTE 6: At initial power on, the VR_OE pin must be held low while VIN_Bulk and VIN_Mgmt input supplies are ramping up.

## R60 (0x60) — SWE_OUTPUT_SOFT_START_TIME, SWF_OUTPUT_SOFT_START_TIME

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-5 Table 264, p.255

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:5 | SWE_OUTPUT_SOFT_START_TIME | RWPE | 001 |
| 4 | RESERVED | RV | 0 |
| 3:1 | SWF_OUTPUT_SOFT_START_TIME | RWPE | 001 |
| 0 | RESERVED | RV | 0 |

### [7:5] SWE_OUTPUT_SOFT_START_TIME

- Description: SWE Output Regulator Soft Start Time After VR Enable[1],[2]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 001 → 2 ms

| Code (bin) | Meaning |
|---|---|
| 000 | 1 ms |
| 001 | 2 ms |
| 010 | 4 ms |
| 011 | 6 ms |
| ... | ... |
| 111 | 14 ms |

### [4] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [3:1] SWF_OUTPUT_SOFT_START_TIME

- Description: SWF Output Regulator Soft Start Time After VR Enable[1],[3]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 001 → 2 ms

| Code (bin) | Meaning |
|---|---|
| 000 | 1 ms |
| 001 | 2 ms |
| 010 | 4 ms |
| 011 | 6 ms |
| ... | ... |
| 111 | 14 ms |

### [0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

**Notes**

- NOTE 1: This is the time it takes for buck regulator to go from 0 V to steady state voltage (the actual voltage varies based on pre- programmed voltage).
- NOTE 2: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’ or ‘01’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care.
- NOTE 3: This register is only applicable if Table 247, Register 0x4F [6] = ‘0’. For any other setting in Table 247, Register 0x4F [6], this register does not apply and it is a don’t care.

## R61 (0x61) — POWER_ON_SEQUENCE_CONFIG5, POWER_ON_SEQUENCE_CONFIG5_SWA_ENABLE, POWER_ON_SEQUENCE_CONFIG5_SWB_ENABLE, POWER_ON_SEQUENCE_CONFIG5_SWC_ENABLE, POWER_ON_SEQUENCE_CONFIG5_SWD_ENABLE, POWER_ON_SEQUENCE_CONFIG5_IDLE

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-5 Table 265, p.256

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | POWER_ON_SEQUENCE_CONFIG5 | RWPE | 0 |
| 6 | POWER_ON_SEQUENCE_CONFIG5_SWA_ENABLE | RWPE | 0 |
| 5 | POWER_ON_SEQUENCE_CONFIG5_SWB_ENABLE | RWPE | 0 |
| 4 | POWER_ON_SEQUENCE_CONFIG5_SWC_ENABLE | RWPE | 0 |
| 3 | POWER_ON_SEQUENCE_CONFIG5_SWD_ENABLE | RWPE | 0 |
| 2:0 | POWER_ON_SEQUENCE_CONFIG5_IDLE | RWPE | 001 |

### [7] POWER_ON_SEQUENCE_CONFIG5

- Description: PMIC Power On Sequence Config 5
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Do Not Execute Config 5[3]

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Execute Config 5[3] |
| 1 | Execute Config 5 |

### [6] POWER_ON_SEQUENCE_CONFIG5_SWA_ENABLE

- Description: Enable Switch Node A Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Enable Switch Node A Output Regulator |

### [5] POWER_ON_SEQUENCE_CONFIG5_SWB_ENABLE

- Description: Enable Switch Node B Output Regulator.[4]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Enable Switch Node B Output Regulator |

### [4] POWER_ON_SEQUENCE_CONFIG5_SWC_ENABLE

- Description: Enable Switch Node C Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Enable Switch Node C Output Regulator |

### [3] POWER_ON_SEQUENCE_CONFIG5_SWD_ENABLE

- Description: Enable Switch Node D Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Enable Switch Node D Output Regulator |

### [2:0] POWER_ON_SEQUENCE_CONFIG5_IDLE

- Description: Idle time after Power On Sequence Config 5[5]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 001 → 2 ms

| Code (bin) | Meaning |
|---|---|
| 000 | 0 ms |
| 001 | 2 ms |
| 010 | 4 ms |
| 011 | 6 ms |
| 100 | 8 ms |
| 101 | 10 ms |
| 110 | 12 ms |
| 111 | 24 ms |

**Notes**

- NOTE 1: The PMIC always starts with power on sequence configuration 0 register and executes remaining power on sequence configuration registers (1 to 5) in sequential order.
- NOTE 2: Power on sequence configuration 5 is total of 10 bit register. 8 bits as shown in Table 265, Register 0x61 [7:0] plus 2 bits in Table 268, Register 0x64 [5:4].
- NOTE 3: If bit [7] = ‘0’, bits [6:0] Table 268, Register 0x64 [5:4] are ignored and PMIC moves to next power on sequence configuration register. If bit [7] = ‘1’, PMIC executes bits [6:0] Table 268, Register 0x64 [5:4] as configured; if no new rail is turned on, the PMIC simply waits the idle time as configured and then moves to next power sequence configuration register.
- NOTE 4: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care.
- NOTE 5: Idle time is the additional time after soft-start time expires. The PMIC waits sum of Soft Start time and Idle time before it executes the next event. If more than one regulators are enabled, the PMIC uses the largest value of the soft start time among the regulators that are enabled in this configuration register.

## R62 (0x62) — POWER_OFF_SEQUENCE_CONFIG5, POWER_OFF_SEQUENCE_CONFIG5_SWA_DISABLE, POWER_OFF_SEQUENCE_CONFIG5_SWB_DISABLE, POWER_OFF_SEQUENCE_CONFIG5_SWC_DISABLE, POWER_OFF_SEQUENCE_CONFIG5_SWD_DISABLE, POWER_OFF_SEQUENCE_CONFIG5_IDLE

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-5 Table 266, p.257

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | POWER_OFF_SEQUENCE_CONFIG5 | RWPE | 0 |
| 6 | POWER_OFF_SEQUENCE_CONFIG5_SWA_DISABLE | RWPE | 0 |
| 5 | POWER_OFF_SEQUENCE_CONFIG5_SWB_DISABLE | RWPE | 0 |
| 4 | POWER_OFF_SEQUENCE_CONFIG5_SWC_DISABLE | RWPE | 0 |
| 3 | POWER_OFF_SEQUENCE_CONFIG5_SWD_DISABLE | RWPE | 0 |
| 2:0 | POWER_OFF_SEQUENCE_CONFIG5_IDLE | RWPE | 0 |

### [7] POWER_OFF_SEQUENCE_CONFIG5

- Description: PMIC Power Off Sequence Config 5[3]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Do Not Execute Config 5

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Execute Config 5 |
| 1 | Execute Config 5 |

### [6] POWER_OFF_SEQUENCE_CONFIG5_SWA_DISABLE

- Description: Disable SWA Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Disable SWA Output Regulator |

### [5] POWER_OFF_SEQUENCE_CONFIG5_SWB_DISABLE

- Description: Disable SWB Output Regulator.[4]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Disable SWB Output Regulator |

### [4] POWER_OFF_SEQUENCE_CONFIG5_SWC_DISABLE

- Description: Disable Switch Node C Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Disable SWC Output Regulator |

### [3] POWER_OFF_SEQUENCE_CONFIG5_SWD_DISABLE

- Description: Disable Switch Node D Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Disable SWD Output Regulator |

### [2:0] POWER_OFF_SEQUENCE_CONFIG5_IDLE

- Description: Idle time after Power Off Sequence Config 5[5]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 000 | 0 ms |
| 001 | 1 ms |
| 010 | 2 ms |
| 011 | 3 ms |
| 100 | 4 ms |
| 101 | 5 ms |
| 110 | 6 ms |
| 111 | 7 ms |

**Notes**

- NOTE 1: The PMIC always starts with power off sequence configuration 0 register and executes remaining power off sequence configuration registers (1 to 5) in sequential order.
- NOTE 2: Power off sequence configuration 5 is total of 10 bit register. 8 bits as shown in Table 266, Register 0x62 [7:0] plus 2 bits in Table 270, Register 0x66 [5:4].
- NOTE 3: If bit [7] = ‘0’, bits [6:0] and Table 270, Register 0x66 [5:4] are ignored and PMIC moves to next power off sequence configuration register. If bit [7] = ‘1’, PMIC executes bits [6:0] and Table 270, Register 0x66 [5:4] as configured; if no new rail is turned off, the PMIC simply waits the idle time as configured and then moves to next power off sequence configuration register.
- NOTE 4: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care.
- NOTE 5: Idle time is the additional time after soft-stop time expires. The PMIC waits sum of soft stop time and idle time before it executes the next power off sequence configuration register. If more than one regulators are disabled, the PMIC uses the largest value of the soft stop time among the regulators that are disabled in this configuration register.

## R63 (0x63) — POWER_ON_SEQUENCE_CONFIG0_EXT_SWE_ENABLE, POWER_ON_SEQUENCE_CONFIG0_EXT_SWF_ENABLE, POWER_ON_SEQUENCE_CONFIG1_EXT_SWE_ENABLE, POWER_ON_SEQUENCE_CONFIG1_EXT_SWF_ENABLE, POWER_ON_SEQUENCE_CONFIG2_EXT_SWE_ENABLE, POWER_ON_SEQUENCE_CONFIG2_EXT_SWF_ENABLE, POWER_ON_SEQUENCE_CONFIG3_EXT_SWE_ENABLE, POWER_ON_SEQUENCE_CONFIG3_EXT_SWF_ENABLE

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-5 Table 267, p.258

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | POWER_ON_SEQUENCE_CONFIG0_EXT_SWE_ENABLE | RWPE | 0 |
| 6 | POWER_ON_SEQUENCE_CONFIG0_EXT_SWF_ENABLE | RWPE | 0 |
| 5 | POWER_ON_SEQUENCE_CONFIG1_EXT_SWE_ENABLE | RWPE | 0 |
| 4 | POWER_ON_SEQUENCE_CONFIG1_EXT_SWF_ENABLE | RWPE | 0 |
| 3 | POWER_ON_SEQUENCE_CONFIG2_EXT_SWE_ENABLE | RWPE | 0 |
| 2 | POWER_ON_SEQUENCE_CONFIG2_EXT_SWF_ENABLE | RWPE | 0 |
| 1 | POWER_ON_SEQUENCE_CONFIG3_EXT_SWE_ENABLE | RWPE | 0 |
| 0 | POWER_ON_SEQUENCE_CONFIG3_EXT_SWF_ENABLE | RWPE | 0 |

### [7] POWER_ON_SEQUENCE_CONFIG0_EXT_SWE_ENABLE

- Description: PMIC Power On Sequence Config0 Extension[2]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Enable SWE Output Regulator |

### [6] POWER_ON_SEQUENCE_CONFIG0_EXT_SWF_ENABLE

- Description: PMIC Power On Sequence Config0 Extension[3]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Enable SWF Output Regulator |

### [5] POWER_ON_SEQUENCE_CONFIG1_EXT_SWE_ENABLE

- Description: PMIC Power On Sequence Config1 Extension[2]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Enable SWE Output Regulator |

### [4] POWER_ON_SEQUENCE_CONFIG1_EXT_SWF_ENABLE

- Description: PMIC Power On Sequence Config1 Extension[3]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Enable SWF Output Regulator |

### [3] POWER_ON_SEQUENCE_CONFIG2_EXT_SWE_ENABLE

- Description: PMIC Power On Sequence Config2 Extension[2]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Enable SWE Output Regulator |

### [2] POWER_ON_SEQUENCE_CONFIG2_EXT_SWF_ENABLE

- Description: PMIC Power On Sequence Config2 Extension[3]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Enable SWF Output Regulator |

### [1] POWER_ON_SEQUENCE_CONFIG3_EXT_SWE_ENABLE

- Description: PMIC Power On Sequence Config3 Extension[2]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Enable SWE Output Regulator |

### [0] POWER_ON_SEQUENCE_CONFIG3_EXT_SWF_ENABLE

- Description: PMIC Power On Sequence Config3 Extension[3]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Enable SWF Output Regulator |

**Notes**

- NOTE 1: Power on sequence configuration 0 to 3 registers are total of 10 bit register. 8 bits as shown in Table 232, Register 0x40 to Table 235, Register 0x43 plus 2 bits as shown in this register.
- NOTE 2: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’ or ‘01’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care.
- NOTE 3: This register is only applicable if Table 247, Register 0x4F [6] = ‘0. For any other setting in Table 247, Register 0x4F [6], this register does not apply and it is a don’t care.

## R64 (0x64) — POWER_ON_SEQUENCE_CONFIG4_EXT_SWE_ENABLE, POWER_ON_SEQUENCE_CONFIG4_EXT_SWF_ENABLE, POWER_ON_SEQUENCE_CONFIG5_EXT_SWE_ENABLE, POWER_ON_SEQUENCE_CONFIG5_EXT_SWF_ENABLE

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-5 Table 268, p.259

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | POWER_ON_SEQUENCE_CONFIG4_EXT_SWE_ENABLE | RWPE | 0 |
| 6 | POWER_ON_SEQUENCE_CONFIG4_EXT_SWF_ENABLE | RWPE | 0 |
| 5 | POWER_ON_SEQUENCE_CONFIG5_EXT_SWE_ENABLE | RWPE | 0 |
| 4 | POWER_ON_SEQUENCE_CONFIG5_EXT_SWF_ENABLE | RWPE | 0 |
| 3:0 | RESERVED | RV | 0 |

### [7] POWER_ON_SEQUENCE_CONFIG4_EXT_SWE_ENABLE

- Description: PMIC Power On Sequence Config4 Extension[2]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Enable SWE Output Regulator |

### [6] POWER_ON_SEQUENCE_CONFIG4_EXT_SWF_ENABLE

- Description: PMIC Power On Sequence Config4 Extension[3]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Enable SWF Output Regulator |

### [5] POWER_ON_SEQUENCE_CONFIG5_EXT_SWE_ENABLE

- Description: PMIC Power On Sequence Config5 Extension[2]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Enable SWE Output Regulator |

### [4] POWER_ON_SEQUENCE_CONFIG5_EXT_SWF_ENABLE

- Description: PMIC Power On Sequence Config5 Extension[3]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Enable SWF Output Regulator |

### [3:0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

**Notes**

- NOTE 1: Power on sequence configuration 4 to 5 registers are total of 10 bit register. 8 bits as shown in Table 236, Register 0x44, Table 265, Register 0x61 plus 2 bits as shown in this register.
- NOTE 2: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’ or ‘01’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care.
- NOTE 3: This register is only applicable if Table 247, Register 0x4F [6] = ‘0. For any other setting in Table 247, Register 0x4F [6], this register does not apply and it is a don’t care.

## R65 (0x65) — POWER_OFF_SEQUENCE_CONFIG0_EXT_SWE_DISABLE, POWER_OFF_SEQUENCE_CONFIG0_EXT_SWF_DISABLE, POWER_OFF_SEQUENCE_CONFIG1_EXT_SWE_DISABLE, POWER_OFF_SEQUENCE_CONFIG1_EXT_SWF_DISABLE, POWER_OFF_SEQUENCE_CONFIG2_EXT_SWE_DISABLE, POWER_OFF_SEQUENCE_CONFIG2_EXT_SWF_DISABLE, POWER_OFF_SEQUENCE_CONFIG3_EXT_SWE_DISABLE, POWER_OFF_SEQUENCE_CONFIG3_EXT_SWF_DISABLE

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-5 Table 269, p.260

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | POWER_OFF_SEQUENCE_CONFIG0_EXT_SWE_DISABLE | RWPE | 0 |
| 6 | POWER_OFF_SEQUENCE_CONFIG0_EXT_SWF_DISABLE | RWPE | 0 |
| 5 | POWER_OFF_SEQUENCE_CONFIG1_EXT_SWE_DISABLE | RWPE | 0 |
| 4 | POWER_OFF_SEQUENCE_CONFIG1_EXT_SWF_DISABLE | RWPE | 0 |
| 3 | POWER_OFF_SEQUENCE_CONFIG2_EXT_SWE_DISABLE | RWPE | 0 |
| 2 | POWER_OFF_SEQUENCE_CONFIG2_EXT_SWF_DISABLE | RWPE | 0 |
| 1 | POWER_OFF_SEQUENCE_CONFIG3_EXT_SWE_DISABLE | RWPE | 0 |
| 0 | POWER_OFF_SEQUENCE_CONFIG3_EXT_SWF_DISABLE | RWPE | 0 |

### [7] POWER_OFF_SEQUENCE_CONFIG0_EXT_SWE_DISABLE

- Description: PMIC Power Off Sequence Config0 Extension[2]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Disable SWE Output Regulator |

### [6] POWER_OFF_SEQUENCE_CONFIG0_EXT_SWF_DISABLE

- Description: PMIC Power Off Sequence Config0 Extension[3]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Disable SWF Output Regulator |

### [5] POWER_OFF_SEQUENCE_CONFIG1_EXT_SWE_DISABLE

- Description: PMIC Power Off Sequence Config1 Extension[2]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Disable SWE Output Regulator |

### [4] POWER_OFF_SEQUENCE_CONFIG1_EXT_SWF_DISABLE

- Description: PMIC Power Off Sequence Config1 Extension[3]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Disable SWF Output Regulator |

### [3] POWER_OFF_SEQUENCE_CONFIG2_EXT_SWE_DISABLE

- Description: PMIC Power Off Sequence Config2 Extension[2]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Disable SWE Output Regulator |

### [2] POWER_OFF_SEQUENCE_CONFIG2_EXT_SWF_DISABLE

- Description: PMIC Power Off Sequence Config2 Extension[3]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Disable SWF Output Regulator |

### [1] POWER_OFF_SEQUENCE_CONFIG3_EXT_SWE_DISABLE

- Description: PMIC Power Off Sequence Config3 Extension[2]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Disable SWE Output Regulator |

### [0] POWER_OFF_SEQUENCE_CONFIG3_EXT_SWF_DISABLE

- Description: PMIC Power Off Sequence Config3 Extension[3]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Disable SWF Output Regulator |

**Notes**

- NOTE 1: Power off sequence configuration 0 to 3 registers are total of 10 bit register. 8 bits as shown in Table 256, Register 0x58 to Table 259, Register 0x5B plus 2 bits as shown in this register.
- NOTE 2: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’ or ‘01’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care.
- NOTE 3: This register is only applicable if Table 247, Register 0x4F [6] = ‘0. For any other setting in Table 247, Register 0x4F [6], this register does not apply and it is a don’t care.

## R66 (0x66) — POWER_OFF_SEQUENCE_CONFIG4_EXT_SWE_DISABLE, POWER_OFF_SEQUENCE_CONFIG4_EXT_SWF_DISABLE, POWER_OFF_SEQUENCE_CONFIG5_EXT_SWE_DISABLE, POWER_OFF_SEQUENCE_CONFIG5_EXT_SWF_DISABLE

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-5 Table 270, p.261

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | POWER_OFF_SEQUENCE_CONFIG4_EXT_SWE_DISABLE | RWPE | 0 |
| 6 | POWER_OFF_SEQUENCE_CONFIG4_EXT_SWF_DISABLE | RWPE | 0 |
| 5 | POWER_OFF_SEQUENCE_CONFIG5_EXT_SWE_DISABLE | RWPE | 0 |
| 4 | POWER_OFF_SEQUENCE_CONFIG5_EXT_SWF_DISABLE | RWPE | 0 |
| 3:0 | RESERVED | RV | 0 |

### [7] POWER_OFF_SEQUENCE_CONFIG4_EXT_SWE_DISABLE

- Description: PMIC Power Off Sequence Config4 Extension[2]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Disable SWE Output Regulator |

### [6] POWER_OFF_SEQUENCE_CONFIG4_EXT_SWF_DISABLE

- Description: PMIC Power Off Sequence Config4 Extension[3]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Disable SWF Output Regulator |

### [5] POWER_OFF_SEQUENCE_CONFIG5_EXT_SWE_DISABLE

- Description: PMIC Power Off Sequence Config5 Extension[2]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Disable SWE Output Regulator |

### [4] POWER_OFF_SEQUENCE_CONFIG5_EXT_SWF_DISABLE

- Description: PMIC Power Off Sequence Config5 Extension[3]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Action

| Code (bin) | Meaning |
|---|---|
| 0 | No Action |
| 1 | Disable SWF Output Regulator |

### [3:0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

**Notes**

- NOTE 1: Power off sequence configuration 4 to 5 registers are total of 10 bit register. 8 bits as shown in Table 260, Register 0x5C, Table 266, Register 0x62 plus 2 bits as shown in this register.
- NOTE 2: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’ or ‘01’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care.
- NOTE 3: This register is only applicable if Table 247, Register 0x4F [6] = ‘0. For any other setting in Table 247, Register 0x4F [6], this register does not apply and it is a don’t care.

## R67 (0x67) — SWA_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-5 Table 271, p.262

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SWA_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD | RWPE | 0011 1100 |

### [7:0] SWA_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD

- Description: SWA Output High Current Consumption Warning Threshold[1]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0011 1100 → > 7500 mA (if If Table 155, Register 0x32[1:0] = ‘00’); > 1875 mA (if If Table 155, Register 0x32[1:0] = ‘01’)

**When: If Table 155, Register 0x32[1:0] = ‘00’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | > 125 mA |
| 00000010 | 0x02 | > 250 mA |
| ... | ... | ... |
| 11111111 | 0xFF | > 31.875 A |

**When: If Table 155, Register 0x32[1:0] = ‘01’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | > 31.25 mA |
| 00000010 | 0x02 | > 62.5 mA |
| ... | ... | ... |
| 11111111 | 0xFF | > 7.968 A |

**Notes**

- NOTE 1: This register is applicable regardless of the setting in Table 247, Register 0x4F [5,0]. For dual phase operation, registers Table 271, Register 0x67 [7:0] and Table 272, Register 0x68 [7:0] must be configured identical. For three phase operation, registers Table 271, Register 0x67 [7:0], Table 272, Register 0x68 [7:0], and Table 275, Register 0x6B [7:0] must be configured identical.

## R68 (0x68) — SWB_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-5 Table 272, p.263

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SWB_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD | RWPE | 0011 1100 |

### [7:0] SWB_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD

- Description: SWB Output High Current Consumption Warning Threshold[1]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0011 1100 → > 7500 mA (if If Table 155, Register 0x32[1:0] = ‘00’); > 1875 mA (if If Table 155, Register 0x32[1:0] = ‘01’)

**When: If Table 155, Register 0x32[1:0] = ‘00’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | > 125 mA |
| 00000010 | 0x02 | > 250 mA |
| ... | ... | ... |
| 11111111 | 0xFF | > 31.875 A |

**When: If Table 155, Register 0x32[1:0] = ‘01’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | > 31.25 mA |
| 00000010 | 0x02 | > 62.5 mA |
| ... | ... | ... |
| 11111111 | 0xFF | > 7.968 A |

**Notes**

- NOTE 1: This register is applicable regardless of the setting in Table 247, Register 0x4F [5,0]. For dual phase operation, registers Table 271, Register 0x67 [7:0] and Table 272, Register 0x68 [7:0] must be configured identical. For three phase operation, registers Table 271, Register 0x67 [7:0], Table 272, Register 0x68 [7:0], and Table 275, Register 0x6B [7:0] must be configured identical.

## R69 (0x69) — SWC_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-5 Table 273, p.264

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SWC_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD | RWPE | 0011 1100 |

### [7:0] SWC_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD

- Description: SWC Output High Current Consumption Warning Threshold[1]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0011 1100 → > 7500 mA (if If Table 155, Register 0x32[1:0] = ‘00’); > 1875 mA (if If Table 155, Register 0x32[1:0] = ‘01’)

**When: If Table 155, Register 0x32[1:0] = ‘00’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | > 125 mA |
| 00000010 | 0x02 | > 250 mA |
| ... | ... | ... |
| 11111111 | 0xFF | > 31.875 A |

**When: If Table 155, Register 0x32[1:0] = ‘01’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | > 31.25 mA |
| 00000010 | 0x02 | > 62.5 mA |
| ... | ... | ... |
| 11111111 | 0xFF | > 7.968 A |

**Notes**

- NOTE 1: This register is applicable regardless of the setting in Table 247, Register 0x4F [6]. For dual phase operation, registers Table 273, Register 0x69 [7:0] and Table 276, Register 0x6C [7:0] must be configured identical.

## R6A (0x6A) — SWD_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-5 Table 274, p.264

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SWD_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD | RWPE | 0010 1000 |

### [7:0] SWD_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD

- Description: SWD Output High Current Consumption Warning Threshold
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0010 1000 → > 5000 mA (if If Table 155, Register 0x32[1:0] = ‘00’); > 1250 mA (if If Table 155, Register 0x32[1:0] = ‘01’)
- Source correction: Spec lists code 000000100 for '> 250 mA'; corrected to 00000010. 9-digit code in source table; 250 mA is code 2 (125 mA/LSB).

**When: If Table 155, Register 0x32[1:0] = ‘00’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | > 125 mA |
| 00000010 | 0x02 | > 250 mA |
| ... | ... | ... |
| 11111111 | 0xFF | > 31.875 A |

**When: If Table 155, Register 0x32[1:0] = ‘01’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | > 31.25 mA |
| 00000010 | 0x02 | > 62.5 mA |
| ... | ... | ... |
| 11111111 | 0xFF | > 7.968 A |

## R6B (0x6B) — SWE_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-5 Table 275, p.265

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SWE_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD | RWPE | 0011 1100 |

### [7:0] SWE_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD

- Description: SWE Output High Current Consumption Warning Threshold[1]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0011 1100 → > 7500 mA (if If Table 155, Register 0x32[1:0] = ‘00’); > 1875 mA (if If Table 155, Register 0x32[1:0] = ‘01’)

**When: If Table 155, Register 0x32[1:0] = ‘00’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | > 125 mA |
| 00000010 | 0x02 | > 250 mA |
| ... | ... | ... |
| 11111111 | 0xFF | > 31.875 A |

**When: If Table 155, Register 0x32[1:0] = ‘01’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | > 31.25 mA |
| 00000010 | 0x02 | > 62.5 mA |
| ... | ... | ... |
| 11111111 | 0xFF | > 7.968 A |

**Notes**

- NOTE 1: This register is applicable regardless of the setting in Table 247, Register 0x4F [5,0]. For three phase operation, registers Table 271, Register 0x67 [7:0], Table 272, Register 0x68 [7:0], and Table 275, Register 0x6B [7:0] must be configured identical.

## R6C (0x6C) — SWF_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-5 Table 276, p.265

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SWF_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD | RWPE | 0011 1100 |

### [7:0] SWF_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD

- Description: SWF Output High Current Consumption Warning Threshold[1]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0011 1100 → > 7500 mA (if If Table 155, Register 0x32[1:0] = ‘00’); > 1875 mA (if If Table 155, Register 0x32[1:0] = ‘01’)
- Source correction: Spec lists code 000000100 for '> 250 mA'; corrected to 00000010. 9-digit code in source table; 250 mA is code 2 (125 mA/LSB).

**When: If Table 155, Register 0x32[1:0] = ‘00’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | > 125 mA |
| 00000010 | 0x02 | > 250 mA |
| ... | ... | ... |
| 11111111 | 0xFF | > 31.875 A |

**When: If Table 155, Register 0x32[1:0] = ‘01’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | > 31.25 mA |
| 00000010 | 0x02 | > 62.5 mA |
| ... | ... | ... |
| 11111111 | 0xFF | > 7.968 A |

**Notes**

- NOTE 1: This register is applicable regardless of the setting in Table 247, Register 0x4F [6]. For dual phase operation, registers Table 273, Register 0x69 [7:0] and Table 276, Register 0x6C [7:0] must be configured identical.

## R6F (0x6F) — DIMM_VENDOR_REGION_CRC_CODE

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-5 Table 277, p.266

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | DIMM_VENDOR_REGION_CRC_CODE | RWPE | - |

### [7:0] DIMM_VENDOR_REGION_CRC_CODE

- Description: DIMM Vendor Region 8-bit CRC Code[1],[2]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: -
- Values: no per-value encoding is listed in the spec for this field.

**Notes**

- NOTE 1: Programmed by DIMM vendor during DIMM assembly.
- NOTE 2: See Clause 6.30 for CRC code computation procedure.

## R100 (0x100) — SWA_OUTPUT_CURRENT_POWER_MEASUREMENT_MSB, SWB_OUTPUT_CURRENT_POWER_MEASUREMENT_MSB, SWC_OUTPUT_CURRENT_POWER_MEASUREMENT_MSB, SWD_OUTPUT_CURRENT_POWER_MEASUREMENT_MSB

Region: Host Region | Source: JESD301-5 Table 167, p.189

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWA_OUTPUT_CURRENT_POWER_MEASUREMENT_MSB | RO | - |
| 5:4 | SWB_OUTPUT_CURRENT_POWER_MEASUREMENT_MSB | RO | - |
| 3:2 | SWC_OUTPUT_CURRENT_POWER_MEASUREMENT_MSB | RO | - |
| 1:0 | SWD_OUTPUT_CURRENT_POWER_MEASUREMENT_MSB | RO | - |

### [7:6] SWA_OUTPUT_CURRENT_POWER_MEASUREMENT_MSB

- Description: MSB bits - SWA Output Current or Output Power Measurement[3],[4],[5] These two MSB bits plus 8 bit register in Table 169, Register 0x102[7:0] makes 10 bit encoding as shown in Table 169, Register 0x102.
- Attribute: RO — Read Only (writes have no effect)
- Default: -
- Values: no per-value encoding is listed in the spec for this field.

### [5:4] SWB_OUTPUT_CURRENT_POWER_MEASUREMENT_MSB

- Description: MSB bits - SWB Output Current or Output Power Measurement[2],[3],[4] These two MSB bits plus 8 bit register in Table 170, Register 0x103[7:0] makes 10 bit encoding as shown in Table 170, Register 0x103.
- Attribute: RO — Read Only (writes have no effect)
- Default: -
- Values: no per-value encoding is listed in the spec for this field.

### [3:2] SWC_OUTPUT_CURRENT_POWER_MEASUREMENT_MSB

- Description: MSB bits - SWC Output Current or Output Power Measurement[2],[3],[4] These two MSB bits plus 8 bit register in Table 171, Register 0x104[7:0] makes 10 bit encoding as shown in Table 171, Register 0x104.
- Attribute: RO — Read Only (writes have no effect)
- Default: -
- Values: no per-value encoding is listed in the spec for this field.

### [1:0] SWD_OUTPUT_CURRENT_POWER_MEASUREMENT_MSB

- Description: MSB bits - SWD Output Current or Output Power Measurement[2],[3],[4] These two MSB bits plus 8 bit register in Table 172, Register 0x105[7:0] makes 10 bit encoding as shown in Table 172, Register 0x105.
- Attribute: RO — Read Only (writes have no effect)
- Default: -
- Values: no per-value encoding is listed in the spec for this field.

**Notes**

- NOTE 1: This register is only applicable if Table 155, Register 0x32 [1:0] = ‘01’.
- NOTE 2: The Host must read ADC current or power measurement bytes in order from MSB to LSB (i.e., R100 to R107) via I2C/I3C block read commands.
- NOTE 3: This register is only applicable if Table 131, Register 0x1A [1] = ‘0’
- NOTE 4: The PMIC reports current or power measurement as long as there is no output over voltage or output under voltage lockout event that triggers the VR Disable command. If PMIC triggers VR Disable command, PMIC does not report current or power measurement and register content may have stale data. For all other events that causes PMIC’s power good status as Not Good, the PMIC continues to provide current or power measurement.
- NOTE 5: If Table 132, Register 0x1B [6] = ‘0’, the PMIC reports current measurement. If Table 132, Register 0x1B [6] = ‘1’, the PMIC reports power measurement.

## R101 (0x101) — SWE_OUTPUT_CURRENT_POWER_MEASUREMENT_MSB, SWF_OUTPUT_CURRENT_POWER_MEASUREMENT_MSB, TOTAL_SWX_OUTPUT_POWER_MSB

Region: Host Region | Source: JESD301-5 Table 168, p.190

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWE_OUTPUT_CURRENT_POWER_MEASUREMENT_MSB | RO | - |
| 5:4 | SWF_OUTPUT_CURRENT_POWER_MEASUREMENT_MSB | RO | - |
| 3 | RESERVED | RV | - |
| 2:0 | TOTAL_SWX_OUTPUT_POWER_MSB | RO | - |

### [7:6] SWE_OUTPUT_CURRENT_POWER_MEASUREMENT_MSB

- Description: MSB bits - SWE Output Current or Output Power Measurement[3],[4],[5] These two MSB bits plus 8 bit register in Table 173, Register 0x106[7:0] makes 10 bit encoding as shown in Table 173, Register 0x106.
- Attribute: RO — Read Only (writes have no effect)
- Default: -
- Values: no per-value encoding is listed in the spec for this field.

### [5:4] SWF_OUTPUT_CURRENT_POWER_MEASUREMENT_MSB

- Description: MSB bits - SWF Output Current or Output Power Measurement[2],[3],[4] These two MSB bits plus 8 bit register in Table 174, Register 0x107[7:0] makes 10 bit encoding as shown in Table 174, Register 0x107.
- Attribute: RO — Read Only (writes have no effect)
- Default: -
- Values: no per-value encoding is listed in the spec for this field.

### [3] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: -

### [2:0] TOTAL_SWX_OUTPUT_POWER_MSB

- Description: MSB bits - Total SWA+SWB+SWC+SWD+SWE+SWF Output Power Measurement[6],[7] These three MSB bits plus 8 bit register in Table 169, Register 0x102[7:0] makes 11 bit encoding as shown in Table 169, Register 0x102.
- Attribute: RO — Read Only (writes have no effect)
- Default: -
- Values: no per-value encoding is listed in the spec for this field.

**Notes**

- NOTE 1: This register is only applicable if Table 155, Register 0x32 [1:0] = ‘01’.
- NOTE 2: The Host must read ADC current or power measurement bytes in order from MSB to LSB (i.e., R100 to R107) via I2C/I3C block read commands.
- NOTE 3: This register is only applicable if Table 131, Register 0x1A [1] = ‘0’
- NOTE 4: The PMIC reports current or power measurement as long as there is no output over voltage or output under voltage lockout event that triggers the VR Disable command. If PMIC triggers VR Disable command, PMIC does not report current or power measurement and register content may have stale data. For all other events that causes PMIC’s power good status as Not Good, the PMIC continues to provide current or power measurement.
- NOTE 5: If Table 132, Register 0x1B [6] = ‘0’, the PMIC reports current measurement. If Table 132, Register 0x1B [6] = ‘1’, the PMIC reports power measurement.
- NOTE 6: This register is only applicable if Table 131, Register 0x1A [1] = ‘1’
- NOTE 7: The PMIC reports power measurement as long as there is no output over voltage or output under voltage lockout event that triggers the VR Disable command. If PMIC triggers VR Disable command, PMIC does not report power measurement and register content may have stale data. For all other events that cause PMIC’s power good status as Not Good, the PMIC continues to provide power measurement.

## R102 (0x102) — SWA_OUTPUT_CURRENT_POWER_OR_TOTAL_POWER_MEASUREMENT_LSB

Region: Host Region | Source: JESD301-5 Table 169, p.191

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SWA_OUTPUT_CURRENT_POWER_OR_TOTAL_POWER_MEASUREMENT_LSB | RO | - |

### [7:0] SWA_OUTPUT_CURRENT_POWER_OR_TOTAL_POWER_MEASUREMENT_LSB

- Attribute: RO — Read Only (writes have no effect)
- Default: -
- Note: the codes below are wider than this 8-bit field; the encoding combines bits from more than one field/register (see Description).

**When: If Table 131, Register 0x1A[1] = ‘0’ — [3],[4] — LSB bits - SWA Output Current or Output Power. The 2 MSB bits Table 167, Register 0x100 [7:6] — plus this 8 bit register makes 10 bit encoding as shown below.**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 0000000000 | 0x000 | Undefined |
| 0000000001 | 0x001 | 31.25mA or 31.25mW |
| 0000000010 | 0x002 | 62.5mA or 62.5mW |
| ... | ... | ... |
| 1111111111 | 0x3FF | > 31.968A or 31.968W |

**When: If Table 131, Register 0x1A[1] = ‘1’ — [5],[6] — LSB bits - Total SWA+SWB+SWC+SWD+SWE+SWF Output Power. The 3 MSB bits Table 168, — Register 0x101 [2:0] plus this 8 bit register makes 11 bit encoding as shown below.**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000000 | 0x000 | Undefined |
| 00000000001 | 0x001 | 31.25mW |
| 00000000010 | 0x002 | 62.5mW |
| ... | ... | ... |
| 11111111111 | 0x7FF | > 63.968W |

**Notes**

- NOTE 1: This register is only applicable if Table 155, Register 0x32 [1:0] = ‘01’. The Host must read ADC current or power measurement bytes in order from MSB to LSB (i.e., R100 to R107) via I2C/I3C block
- NOTE: 2 read commands.
- NOTE 3: The PMIC reports current or power measurement as long as there is no output over voltage or output under voltage lockout event that triggers the VR Disable command. If PMIC triggers VR Disable command, PMIC does not report current or power measurement and register content may have stale data. For all other events that causes PMIC’s power good status as Not Good, the PMIC continues to provide current or power measurement.
- NOTE 4: If Table 132, Register 0x1B [6] = ‘0’, the PMIC reports current measurement. If Table 132, Register 0x1B [6] = ‘1’, the PMIC reports power measurement.
- NOTE 5: The PMIC reports power measurement as long as there is no output over voltage or output under voltage lockout event that triggers the VR Disable command. If PMIC triggers VR Disable command, PMIC does not report power measurement and register content may have stale data. For all other events that cause PMIC’s power good status as Not Good, the PMIC continues to provide power measurement.
- NOTE 6: The register Table 132, Register 0x1B [6] must be configured as ‘1’.

## R103 (0x103) — SWB_OUTPUT_CURRENT_POWER_MEASUREMENT_LSB

Region: Host Region | Source: JESD301-5 Table 170, p.192

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SWB_OUTPUT_CURRENT_POWER_MEASUREMENT_LSB | RO | - |

### [7:0] SWB_OUTPUT_CURRENT_POWER_MEASUREMENT_LSB

- Description: LSB bits - SWB Output Current or Output Power Measurement[3],[4] The 2 MSB bits Table 167, Register 0x100 [5:4] plus this 8 bit register makes 10 bit encoding as shown below. Table 131, Register 0x1A[1] = ‘0’:
- Attribute: RO — Read Only (writes have no effect)
- Default: -
- Note: the codes below are wider than this 8-bit field; the encoding combines bits from more than one field/register (see Description).

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 0000000000 | 0x000 | Undefined |
| 0000000001 | 0x001 | 31.25mA or 31.25mW |
| 0000000010 | 0x002 | 62.5mA or 62.5mW |
| ... | ... | ... |
| 1111111111 | 0x3FF | > 31.968A or 31.968W |

**Notes**

- NOTE 1: This register is only applicable if Table 155, Register 0x32 [1:0] = ‘01’.
- NOTE 2: The Host must read ADC current or power measurement bytes in order from MSB to LSB (i.e., R100 to R107) via I2C/I3C block read commands.
- NOTE 3: The PMIC reports current or power measurement as long as there is no output over voltage or output under voltage lockout event that triggers the VR Disable command. If PMIC triggers VR Disable command, PMIC does not report current or power measurement and register content may have stale data. For all other events that causes PMIC’s power good status as Not Good, the PMIC continues to provide current or power measurement.
- NOTE 4: If Table 132, Register 0x1B [6] = ‘0’, the PMIC reports current measurement. If Table 132, Register 0x1B [6] = ‘1’, the PMIC reports power measurement.

## R104 (0x104) — SWC_OUTPUT_CURRENT_POWER_MEASUREMENT_LSB

Region: Host Region | Source: JESD301-5 Table 171, p.192

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SWC_OUTPUT_CURRENT_POWER_MEASUREMENT_LSB | RO | - |

### [7:0] SWC_OUTPUT_CURRENT_POWER_MEASUREMENT_LSB

- Description: LSB bits - SWC Output Current or Output Power Measurement[3],[4] The 2 MSB bits Table 167, Register 0x100 [3:2] plus this 8 bit register makes 10 bit encoding as shown below. Table 131, Register 0x1A[1] = ‘0’:
- Attribute: RO — Read Only (writes have no effect)
- Default: -
- Note: the codes below are wider than this 8-bit field; the encoding combines bits from more than one field/register (see Description).

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 0000000000 | 0x000 | Undefined |
| 0000000001 | 0x001 | 31.25mA or 31.25mW |
| 0000000010 | 0x002 | 62.5mA or 62.5mW |
| ... | ... | ... |
| 1111111111 | 0x3FF | > 31.968A or 31.968W |

**Notes**

- NOTE 1: This register is only applicable if Table 155, Register 0x32 [1:0] = ‘01’.
- NOTE 2: The Host must read ADC current or power measurement bytes in order from MSB to LSB (i.e., R100 to R107) via I2C/I3C block read commands.
- NOTE 3: The PMIC reports current or power measurement as long as there is no output over voltage or output under voltage lockout event that triggers the VR Disable command. If PMIC triggers VR Disable command, PMIC does not report current or power measurement and register content may have stale data. For all other events that causes PMIC’s power good status as Not Good, the PMIC continues to provide current or power measurement.
- NOTE 4: If Table 132, Register 0x1B [6] = ‘0’, the PMIC reports current measurement. If Table 132, Register 0x1B [6] = ‘1’, the PMIC reports power measurement.

## R105 (0x105) — SWD_OUTPUT_CURRENT_POWER_MEASUREMENT_LSB

Region: Host Region | Source: JESD301-5 Table 172, p.193

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SWD_OUTPUT_CURRENT_POWER_MEASUREMENT_LSB | RO | - |

### [7:0] SWD_OUTPUT_CURRENT_POWER_MEASUREMENT_LSB

- Description: LSB bits - SWD Output Current or Output Power Measurement[3],[4] The 2 MSB bits Table 167, Register 0x100 [1:0] plus this 8 bit register makes 10 bit encoding as shown below. Table 131, Register 0x1A[1] = ‘0’:
- Attribute: RO — Read Only (writes have no effect)
- Default: -
- Note: the codes below are wider than this 8-bit field; the encoding combines bits from more than one field/register (see Description).

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 0000000000 | 0x000 | Undefined |
| 0000000001 | 0x001 | 31.25mA or 31.25mW |
| 0000000010 | 0x002 | 62.5mA or 62.5mW |
| ... | ... | ... |
| 1111111111 | 0x3FF | > 31.968A or 31.968W |

**Notes**

- NOTE 1: This register is only applicable if Table 155, Register 0x32 [1:0] = ‘01’.
- NOTE 2: The Host must read ADC current or power measurement bytes in order from MSB to LSB (i.e., R100 to R107) via I2C/I3C block read commands.
- NOTE 3: The PMIC reports current or power measurement as long as there is no output over voltage or output under voltage lockout event that triggers the VR Disable command. If PMIC triggers VR Disable command, PMIC does not report current or power measurement and register content may have stale data. For all other events that causes PMIC’s power good status as Not Good, the PMIC continues to provide current or power measurement.
- NOTE 4: If Table 132, Register 0x1B [6] = ‘0’, the PMIC reports current measurement. If Table 132, Register 0x1B [6] = ‘1’, the PMIC reports power measurement.

## R106 (0x106) — SWE_OUTPUT_CURRENT_POWER_MEASUREMENT_LSB

Region: Host Region | Source: JESD301-5 Table 173, p.193

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SWE_OUTPUT_CURRENT_POWER_MEASUREMENT_LSB | RO | - |

### [7:0] SWE_OUTPUT_CURRENT_POWER_MEASUREMENT_LSB

- Description: LSB bits - SWE Output Current or Output Power Measurement[3],[4] The 2 MSB bits Table 168, Register 0x101 [7:6] plus this 8 bit register makes 10 bit encoding as shown below. Table 131, Register 0x1A[1] = ‘0’:
- Attribute: RO — Read Only (writes have no effect)
- Default: -
- Note: the codes below are wider than this 8-bit field; the encoding combines bits from more than one field/register (see Description).

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 0000000000 | 0x000 | Undefined |
| 0000000001 | 0x001 | 31.25mA or 31.25mW |
| 0000000010 | 0x002 | 62.5mA or 62.5mW |
| ... | ... | ... |
| 1111111111 | 0x3FF | > 31.968A or 31.968W |

**Notes**

- NOTE 1: This register is only applicable if Table 155, Register 0x32 [1:0] = ‘01’.
- NOTE 2: The Host must read ADC current or power measurement bytes in order from MSB to LSB (i.e., R100 to R107) via I2C/I3C block read commands.
- NOTE 3: The PMIC reports current or power measurement as long as there is no output over voltage or output under voltage lockout event that triggers the VR Disable command. If PMIC triggers VR Disable command, PMIC does not report current or power measurement and register content may have stale data. For all other events that causes PMIC’s power good status as Not Good, the PMIC continues to provide current or power measurement.
- NOTE 4: If Table 132, Register 0x1B [6] = ‘0’, the PMIC reports current measurement. If Table 132, Register 0x1B [6] = ‘1’, the PMIC reports power measurement.

## R107 (0x107) — SWF_OUTPUT_CURRENT_POWER_MEASUREMENT_LSB

Region: Host Region | Source: JESD301-5 Table 174, p.194

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SWF_OUTPUT_CURRENT_POWER_MEASUREMENT_LSB | RO | - |

### [7:0] SWF_OUTPUT_CURRENT_POWER_MEASUREMENT_LSB

- Description: LSB bits - SWF Output Current or Output Power Measurement[3],[4] The 2 MSB bits Table 168, Register 0x101 [5:4] plus this 8 bit register makes 10 bit encoding as shown below. Table 131, Register 0x1A[1] = ‘0’:
- Attribute: RO — Read Only (writes have no effect)
- Default: -
- Note: the codes below are wider than this 8-bit field; the encoding combines bits from more than one field/register (see Description).

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 0000000000 | 0x000 | Undefined |
| 0000000001 | 0x001 | 31.25mA or 31.25mW |
| 0000000010 | 0x002 | 62.5mA or 62.5mW |
| ... | ... | ... |
| 1111111111 | 0x3FF | > 31.968A or 31.968W |

**Notes**

- NOTE 1: This register is only applicable if Table 155, Register 0x32 [1:0] = ‘01’.
- NOTE 2: The Host must read ADC current or power measurement bytes in order from MSB to LSB (i.e., R100 to R107) via I2C/I3C block read commands.
- NOTE 3: The PMIC reports current or power measurement as long as there is no output over voltage or output under voltage lockout event that triggers the VR Disable command. If PMIC triggers VR Disable command, PMIC does not report current or power measurement and register content may have stale data. For all other events that causes PMIC’s power good status as Not Good, the PMIC continues to provide current or power measurement.
- NOTE 4: If Table 132, Register 0x1B [6] = ‘0’, the PMIC reports current measurement. If Table 132, Register 0x1B [6] = ‘1’, the PMIC reports power measurement.

## R108 (0x108) — SWE_OUTPUT_POWER_GOOD_STATUS, SWF_OUTPUT_POWER_GOOD_STATUS, SWE_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS, SWF_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS, SWE_OUTPUT_OVER_VOLTAGE_STATUS, SWF_OUTPUT_OVER_VOLTAGE_STATUS, SWE_OUTPUT_CURRENT_LIMITER_WARNING_STATUS, SWF_OUTPUT_CURRENT_LIMITER_WARNING_STATUS

Region: Host Region | Source: JESD301-5 Table 175, p.194

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | SWE_OUTPUT_POWER_GOOD_STATUS | RO | 0 |
| 6 | SWF_OUTPUT_POWER_GOOD_STATUS | RO | 0 |
| 5 | SWE_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS | RO | 0 |
| 4 | SWF_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS | RO | 0 |
| 3 | SWE_OUTPUT_OVER_VOLTAGE_STATUS | RO | 0 |
| 2 | SWF_OUTPUT_OVER_VOLTAGE_STATUS | RO | 0 |
| 1 | SWE_OUTPUT_CURRENT_LIMITER_WARNING_STATUS | RO | 0 |
| 0 | SWF_OUTPUT_CURRENT_LIMITER_WARNING_STATUS | RO | 0 |

### [7] SWE_OUTPUT_POWER_GOOD_STATUS

- Description: Switch Node E Output Power Good Status[1],[2]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → Power Good

| Code (bin) | Meaning |
|---|---|
| 0 | Power Good |
| 1 | Power Not Good |

### [6] SWF_OUTPUT_POWER_GOOD_STATUS

- Description: Switch Node F Output Power Good Status[3],[4]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → Power Good

| Code (bin) | Meaning |
|---|---|
| 0 | Power Good |
| 1 | Power Not Good |

### [5] SWE_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS

- Description: Switch Node E High Output Current Consumption Warning Status[5],[6]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No High Current Consumption Warning

| Code (bin) | Meaning |
|---|---|
| 0 | No High Current Consumption Warning |
| 1 | High Current Consumption Warning R108 |

### [4] SWF_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS

- Description: Switch Node F High Output Current Consumption Warning Status[7],[8]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No High Current Consumption Warning

| Code (bin) | Meaning |
|---|---|
| 0 | No High Current Consumption Warning |
| 1 | High Current Consumption Warning |

### [3] SWE_OUTPUT_OVER_VOLTAGE_STATUS

- Description: Switch Node E Output Over Voltage Status[1],[9]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No Over Voltage

| Code (bin) | Meaning |
|---|---|
| 0 | No Over Voltage |
| 1 | Over Voltage |

### [2] SWF_OUTPUT_OVER_VOLTAGE_STATUS

- Description: Switch Node F Output Over Voltage Status[3],[10]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No Over Voltage

| Code (bin) | Meaning |
|---|---|
| 0 | No Over Voltage |
| 1 | Over Voltage |

### [1] SWE_OUTPUT_CURRENT_LIMITER_WARNING_STATUS

- Description: Switch Node E Output Current Limiter Warning Status[5],[11]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No Current Limiter Event

| Code (bin) | Meaning |
|---|---|
| 0 | No Current Limiter Event |
| 1 | Current Limiter Event |

### [0] SWF_OUTPUT_CURRENT_LIMITER_WARNING_STATUS

- Description: Switch Node F Output Current Limiter Warning Status[7],[12]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No Current Limiter Event

| Code (bin) | Meaning |
|---|---|
| 0 | No Current Limiter Event |
| 1 | Current Limiter Event |

**Notes**

- NOTE 1: Only applicable if Table 247, Register 0x4F [5,0] = ‘00’ or ‘01’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care.
- NOTE 2: This register is set when SWE output voltage goes either below the threshold setting in register Table 185, Register 0x11D[1:0] or above the threshold setting in register Table 186, Register 0x11E [7:6].
- NOTE 3: Only applicable if Table 247, Register 0x4F [6] = ‘0’. For any other setting in Table 247, Register 0x4F [6], this register does not apply and it is a don’t care.
- NOTE 4: This register is set when SWF output goes either below the threshold setting in register Table 187, Register 0x11F[1:0] or above the threshold setting in register Table 188, Register 0x120 [7:6].
- NOTE 5: This register is applicable regardless of the setting in Table 247, Register 0x4F [5,0].
- NOTE 6: This register is set when SWE output current consumption goes above the threshold setting in Table 182, Register 0x11A [7:0].
- NOTE 7: This register is applicable regardless of the setting in Table 247, Register 0x4F [6].
- NOTE 8: This register is set when SWF output current consumption goes above the threshold setting in Table 183, Register 0x11B [7:0].
- NOTE 9: This register is set when SWE output voltage goes above the threshold setting in Table 186, Register 0x11E [5:4].
- NOTE 10: This register is set when SWE output voltage goes above the threshold setting in Table 188, Register 0x120 [5:4].
- NOTE 11: This register is set when SWE output current goes above the threshold setting in Table 184, Register 0x11C [7:6]. If Table 247, Register 0x4F [5,0] = ‘1x’, the setting in Table 137, Register 0x20 [5:4], Table 137, Register 0x20 [7:6] and Table 184, Register 0x11C [7:6] must be configured identical.
- NOTE 12: This register is set when SWF output current goes above the threshold setting in Table 184, Register 0x11C [5:4]. If Table 247, Register 0x4F [6] = ‘1’, the setting in Table 137, Register 0x20 [3:2] must be identical as Table 184, Register 0x11C [5:4].

## R109 (0x109) — SWE_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS, SWF_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS, DIMM_VENDOR_REGION_CRC_CHECK_ON_CMD_STATUS

Region: Host Region | Source: JESD301-5 Table 176, p.196

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | SWE_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS | RO | 0 |
| 6 | SWF_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS | RO | 0 |
| 5:1 | RESERVED | RV | 0 |
| 0 | DIMM_VENDOR_REGION_CRC_CHECK_ON_CMD_STATUS | RO | 0 |

### [7] SWE_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

- Description: Switch Node E Output Under Voltage Lockout Status[1],[2]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No Under Voltage Lockout

| Code (bin) | Meaning |
|---|---|
| 0 | No Under Voltage Lockout |
| 1 | Under Voltage Lockout |

### [6] SWF_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

- Description: Switch Node F Output Under Voltage Lockout Status[3],[4]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No Under Voltage Lockout

| Code (bin) | Meaning |
|---|---|
| 0 | No Under Voltage Lockout |
| 1 | Under Voltage Lockout |

### [5:1] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [0] DIMM_VENDOR_REGION_CRC_CHECK_ON_CMD_STATUS

- Description: DIMM Vendor Region CRC Check on CMD; i.e., Table 163, Register 0x3A [0] = ‘1’
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → DIMM Region CRC Error Checked - No Error

| Code (bin) | Meaning |
|---|---|
| 0 | DIMM Region CRC Error Checked - No Error |
| 1 | DIMM Region CRC Error Checked - Error |

**Notes**

- NOTE 1: Only applicable if Table 247, Register 0x4F [5,0] = ‘00’ or ‘01’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care.
- NOTE 2: This register is set when SWE output voltage goes below the threshold setting in Table 186, Register 0x11E [3:2].
- NOTE 3: Only applicable if Table 247, Register 0x4F [6] = ‘1’. For any other setting in Table 247, Register 0x4F [6], this register does not apply and it is a don’t care.
- NOTE 4: This register is set when SWF output voltage goes below the threshold setting in Table 188, Register 0x120 [3:2].

## R10A (0x10A) — DIMM_VENDOR_REGION_MTP_CRC_CHECK_STATUS, DIMM_VENDOR_REGION_MTP_CRC_CHECK_ERROR_STATUS, PMIC_VENDOR_REGION_MTP_CHECK_STATUS, PMIC_VENDOR_REGION_MTP_CHECK_ERROR_STATUS

Region: Host Region | Source: JESD301-5 Table 177, p.197

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | DIMM_VENDOR_REGION_MTP_CRC_CHECK_STATUS | RO | 0 |
| 6 | DIMM_VENDOR_REGION_MTP_CRC_CHECK_ERROR_STATUS | RO | 0 |
| 5 | PMIC_VENDOR_REGION_MTP_CHECK_STATUS | RO | 0 |
| 4 | PMIC_VENDOR_REGION_MTP_CHECK_ERROR_STATUS | RO | 0 |
| 3:0 | RESERVED | RV | 0 |

### [7] DIMM_VENDOR_REGION_MTP_CRC_CHECK_STATUS

- Description: DIMM Vendor Region MTP CRC Check Status at first power on[1]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → DIMM Region MTP CRC Not Checked

| Code (bin) | Meaning |
|---|---|
| 0 | DIMM Region MTP CRC Not Checked |
| 1 | DIMM Region MTP CRC Checked |

### [6] DIMM_VENDOR_REGION_MTP_CRC_CHECK_ERROR_STATUS

- Description: DIMM Vendor Region MTP CRC Check Error Status at first power on[2]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → DIMM Region MTP CRC Error Checked - No Error

| Code (bin) | Meaning |
|---|---|
| 0 | DIMM Region MTP CRC Error Checked - No Error |
| 1 | DIMM Region MTP CRC Error Checked - Error |

### [5] PMIC_VENDOR_REGION_MTP_CHECK_STATUS

- Description: PMIC Vendor Region MTP Check Status at first power on[3]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → PMIC Region MTP Error Not Checked

| Code (bin) | Meaning |
|---|---|
| 0 | PMIC Region MTP Error Not Checked |
| 1 | PMIC Region MTP Error Checked |

### [4] PMIC_VENDOR_REGION_MTP_CHECK_ERROR_STATUS

- Description: PMIC Vendor Region MTP Check Error Status at first power on[4]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → PMIC Region MTP Error Checked - No Error

| Code (bin) | Meaning |
|---|---|
| 0 | PMIC Region MTP Error Checked - No Error |
| 1 | PMIC Region MTP Error Checked - Error |

### [3:0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

**Notes**

- NOTE 1: PMIC must check the DIMM Vendor Region MTP for error as defined in clause 6.30 and sets this bit [7] to ‘1’ after checking. If PMIC does not perform the DIMM vendor region MTP error check at power on, the PMIC keeps this bit to ‘0’.
- NOTE 2: This bit is only applicable if bit [7] is set to ‘1’. After PMIC checks for DIMM region MTP error, the PMIC sets this bit [6] to ‘1’ if there is an error.
- NOTE 3: PMIC must check the PMIC Vendor Region MTP for error as defined in clause 6.30 and set this bit [5] to ‘1’ after checking. If PMIC does not perform the PMIV vendor region MTP error check at power on, the PMIC keeps this bit to ‘0’.
- NOTE 4: This bit is only applicable if bit [5] is set to ‘1’. After PMIC checks for PMIC vendor region MTP error, the PMIC sets this bit [4] to ‘1’ if there is an error.

## R10E (0x10E) — CLEAR_SWE_OUTPUT_POWER_GOOD_STATUS, CLEAR_SWF_OUTPUT_POWER_GOOD_STATUS, CLEAR_SWE_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS, CLEAR_SWF_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS, CLEAR_SWE_OUTPUT_OVER_VOLTAGE_STATUS, CLEAR_SWF_OUTPUT_OVER_VOLTAGE_STATUS, CLEAR_SWE_OUTPUT_CURRENT_LIMITER_WARNING_STATUS, CLEAR_SWF_OUTPUT_CURRENT_LIMITER_WARNING_STATUS

Region: Host Region | Source: JESD301-5 Table 178, p.198

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | CLEAR_SWE_OUTPUT_POWER_GOOD_STATUS | 1O | 0 |
| 6 | CLEAR_SWF_OUTPUT_POWER_GOOD_STATUS | 1O | 0 |
| 5 | CLEAR_SWE_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS | 1O | 0 |
| 4 | CLEAR_SWF_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS | 1O | 0 |
| 3 | CLEAR_SWE_OUTPUT_OVER_VOLTAGE_STATUS | 1O | 0 |
| 2 | CLEAR_SWF_OUTPUT_OVER_VOLTAGE_STATUS | 1O | 0 |
| 1 | CLEAR_SWE_OUTPUT_CURRENT_LIMITER_WARNING_STATUS | 1O | 0 |
| 0 | CLEAR_SWF_OUTPUT_CURRENT_LIMITER_WARNING_STATUS | 1O | 0 |

### [7] CLEAR_SWE_OUTPUT_POWER_GOOD_STATUS

- Description: Clear SWE Output Power Good Status.[2]
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 175, Register 0x108 [7][3] |

### [6] CLEAR_SWF_OUTPUT_POWER_GOOD_STATUS

- Description: Clear SWF Output Power Good Status.[4]
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 175, Register 0x108 [6][3] |

### [5] CLEAR_SWE_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS

- Description: Clear Switch Node E High Output Current Consumption Warning Status.[5]
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 175, Register 0x108 [5][3] |

### [4] CLEAR_SWF_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS

- Description: Clear Switch Node F High Output Current Consumption Warning Status.[6]
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 175, Register 0x108 [4][3] |

### [3] CLEAR_SWE_OUTPUT_OVER_VOLTAGE_STATUS

- Description: Clear Switch Node E Output Over Voltage Status.[2]
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 175, Register 0x108 [3][3] |

### [2] CLEAR_SWF_OUTPUT_OVER_VOLTAGE_STATUS

- Description: Clear Switch Node F Output Over Voltage Status.[4]
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 175, Register 0x108 [2][3] |

### [1] CLEAR_SWE_OUTPUT_CURRENT_LIMITER_WARNING_STATUS

- Description: Clear Switch Node E Output Current Limiter Warning Status.[5]
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 175, Register 0x108 [1][3] |

### [0] CLEAR_SWF_OUTPUT_CURRENT_LIMITER_WARNING_STATUS

- Description: Clear Switch Node F Output Current Limiter Warning Status.[6]
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 175, Register 0x108 [0][3] |

**Notes**

- NOTE 1: Table 178, Register 0x10E [7:0] are self-clearing bits.
- NOTE 2: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’ or ‘01’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care.
- NOTE 3: See Table 28 and Table 29 for GSI_n and POWER_GOOD output signal status change.
- NOTE 4: This register is only applicable if Table 247, Register 0x4F [6] = ‘0’. For any other setting in Table 247, Register 0x4F [6], this register does not apply and it is a don’t care.
- NOTE 5: This register is applicable regardless of the setting in Table 247, Register 0x4F [5,0].
- NOTE 6: This register is applicable regardless of the setting in Table 247, Register 0x4F [6].

## R10F (0x10F) — CLEAR_SWE_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS, CLEAR_SWF_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS, CLEAR_DIMM_REGION_CRC_ERROR_STATUS

Region: Host Region | Source: JESD301-5 Table 179, p.199

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | CLEAR_SWE_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS | 1O | 0 |
| 6 | CLEAR_SWF_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS | 1O | 0 |
| 5:1 | RESERVED | RV | 0 |
| 0 | CLEAR_DIMM_REGION_CRC_ERROR_STATUS | 1O | 0 |

### [7] CLEAR_SWE_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

- Description: Clear Switch Node E Output Under Voltage Lockout Status.[2]
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 176, Register 0x109 [7][3] |

### [6] CLEAR_SWF_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

- Description: Clear Switch Node F Output Under Voltage Lockout Status.[4]
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 176, Register 0x109 [6][3] |

### [5:1] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [0] CLEAR_DIMM_REGION_CRC_ERROR_STATUS

- Description: Clear DIMM Vendor Region CRC Error Status
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 176, Register 0x109 [0] |

**Notes**

- NOTE 1: Table 179, Register 0x10F [7:0] are self-clearing bits.
- NOTE 2: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’ or ‘01’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care.
- NOTE 3: See Table 28 and Table 29 for GSI_n and POWER_GOOD output signal status change.
- NOTE 4: This register is only applicable if Table 247, Register 0x4F [6] = ‘0’. For any other setting in Table 247, Register 0x4F [6], this register does not apply and it is a don’t care.

## R114 (0x114) — MASK_SWE_OUTPUT_POWER_GOOD_STATUS, MASK_SWF_OUTPUT_POWER_GOOD_STATUS, MASK_SWE_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS, MASK_SWF_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS, MASK_SWE_OUTPUT_OVER_VOLTAGE_STATUS, MASK_SWF_OUTPUT_OVER_VOLTAGE_STATUS, MASK_SWE_OUTPUT_CURRENT_LIMITER_WARNING_STATUS, MASK_SWF_OUTPUT_CURRENT_LIMITER_WARNING_STATUS

Region: Host Region | Source: JESD301-5 Table 180, p.200

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | MASK_SWE_OUTPUT_POWER_GOOD_STATUS | RW | 1 |
| 6 | MASK_SWF_OUTPUT_POWER_GOOD_STATUS | RW | 1 |
| 5 | MASK_SWE_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS | RW | 0 |
| 4 | MASK_SWF_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS | RW | 0 |
| 3 | MASK_SWE_OUTPUT_OVER_VOLTAGE_STATUS | RW | 0 |
| 2 | MASK_SWF_OUTPUT_OVER_VOLTAGE_STATUS | RW | 0 |
| 1 | MASK_SWE_OUTPUT_CURRENT_LIMITER_WARNING_STATUS | RW | 0 |
| 0 | MASK_SWF_OUTPUT_CURRENT_LIMITER_WARNING_STATUS | RW | 0 |

### [7] MASK_SWE_OUTPUT_POWER_GOOD_STATUS

- Description: Mask SWE Output Power Good Status Event.[1]
- Attribute: RW — Read/Write
- Default: 1 → Mask SWE Output Power Good Status Event[2]

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWE Output Power Good Status Event |
| 1 | Mask SWE Output Power Good Status Event[2] |

### [6] MASK_SWF_OUTPUT_POWER_GOOD_STATUS

- Description: Mask SWF Output Power Good Status Event.[3]
- Attribute: RW — Read/Write
- Default: 1 → Mask SWF Output Power Good Status Event[2]

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWF Output Power Good Status Event |
| 1 | Mask SWF Output Power Good Status Event[2] |

### [5] MASK_SWE_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS

- Description: Mask SWE High Output Current Consumption Warning Status Event.[1]
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask SWE Output Current Consumption Warning Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWE Output Current Consumption Warning Status Event |
| 1 | Mask SWE Output Current Consumption Warning Status Event[4] |

### [4] MASK_SWF_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS

- Description: Mask SWF High Output Current Consumption Warning Status Event.[3]
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask SWF Output Current Consumption Warning Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWF Output Current Consumption Warning Status Event |
| 1 | Mask SWF Output Current Consumption Warning Status Event[4] |

### [3] MASK_SWE_OUTPUT_OVER_VOLTAGE_STATUS

- Description: Mask SWE Output Over Voltage Status Event.[1]
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask SWE Output Over Voltage Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWE Output Over Voltage Status Event |
| 1 | Mask SWE Output Over Voltage Status Event[4] |

### [2] MASK_SWF_OUTPUT_OVER_VOLTAGE_STATUS

- Description: Mask SWF Output Over Voltage Status Event.[3]
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask SWF Output Over Voltage Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWF Output Over Voltage Status Event |
| 1 | Mask SWF Output Over Voltage Status Event[4] |

### [1] MASK_SWE_OUTPUT_CURRENT_LIMITER_WARNING_STATUS

- Description: Mask SWE Output Current Limiter Warning Status Event.[1]
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask SWE Output Current Limiter Warning Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWE Output Current Limiter Warning Status Event |
| 1 | Mask SWE Output Current Limiter Warning Status Event[4] |

### [0] MASK_SWF_OUTPUT_CURRENT_LIMITER_WARNING_STATUS

- Description: Mask SWF Output Current Limiter Warning Status Event.[3]
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask SWF Output Current Limiter Warning Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWF Output Current Limiter Warning Status Event |
| 1 | Mask SWF Output Current Limiter Warning Status Event[4] |

**Notes**

- NOTE 1: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’ or ‘01’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care.
- NOTE 2: Not assert GSI_n or PWR_GOOD output signal.
- NOTE 3: This register is only applicable if Table 247, Register 0x4F [6] = ‘0’. For any other setting in Table 247, Register 0x4F [6], this register does not apply and it is a don’t care.
- NOTE 4: Not assert GSI_n output signal.

## R115 (0x115) — MASK_SWE_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS, MASK_SWF_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

Region: Host Region | Source: JESD301-5 Table 181, p.201

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | MASK_SWE_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS | RW | 0 |
| 6 | MASK_SWF_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS | RW | 0 |
| 5:0 | RESERVED | RV | 0 |

### [7] MASK_SWE_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

- Description: Mask SWE Output Under Voltage Lockout Status Event.[1]
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask SWE Output Under Voltage Lockout Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWE Output Under Voltage Lockout Status Event |
| 1 | Mask SWE Output Under Voltage Lockout Status Event[2] |

### [6] MASK_SWF_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

- Description: Mask SWF Output Under Voltage Lockout Status Event.[3]
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask SWF Output Under Voltage Lockout Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWF Output Under Voltage Lockout Status Event |
| 1 | Mask SWF Output Under Voltage Lockout Status Event[2] |

### [5:0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

**Notes**

- NOTE 1: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’ or ‘01’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care.
- NOTE 2: Not assert GSI_n output signal.
- NOTE 3: This register is only applicable if Table 247, Register 0x4F [6] = ‘0’. For any other setting in Table 247, Register 0x4F [6], this register does not apply and it is a don’t care.

## R11A (0x11A) — SWE_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD

Region: Host Region | Source: JESD301-5 Table 182, p.201

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SWE_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD | RW | 0011 1100 |

### [7:0] SWE_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD

- Description: SWE Output High Current Consumption Warning Threshold[2]
- Attribute: RW — Read/Write
- Default: 0011 1100 → > 7500 mA (if If Table 155, Register 0x32[1:0] = ‘00’); > 1875 mA (if If Table 155, Register 0x32[1:0] = ‘01’)

**When: If Table 155, Register 0x32[1:0] = ‘00’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | > 125 mA |
| 00000010 | 0x02 | > 250 mA |
| ... | ... | ... |
| 11111111 | 0xFF | > 31.875 A |

**When: If Table 155, Register 0x32[1:0] = ‘01’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | > 31.25 mA |
| 00000010 | 0x02 | > 62.5 mA |
| ... | ... | ... |
| 11111111 | 0xFF | > 7.968 A |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 275, Register 0x6B.
- NOTE 2: This register is applicable regardless of the setting in Table 247, Register 0x4F [5,0]. For three phase operation, registers Table 133, Register 0x1C [7:0], Table 134, Register 0x1D [7:0] and Table 182, Register 0x11A [7:0] must be configured identical.

## R11B (0x11B) — SWF_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD

Region: Host Region | Source: JESD301-5 Table 183, p.202

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SWF_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD | RW | 0011 1100 |

### [7:0] SWF_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD

- Description: SWF Output High Current Consumption Warning Threshold[2]
- Attribute: RW — Read/Write
- Default: 0011 1100 → > 7500 mA (if If Table 155, Register 0x32[1:0] = ‘00’); > 1875 mA (if If Table 155, Register 0x32[1:0] = ‘01’)
- Source correction: Spec lists code 000000100 for '> 250 mA'; corrected to 00000010. 9-digit code in source table; 250 mA is code 2 (125 mA/LSB).

**When: If Table 155, Register 0x32[1:0] = ‘00’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | > 125 mA |
| 00000010 | 0x02 | > 250 mA |
| ... | ... | ... |
| 11111111 | 0xFF | > 31.875 A |

**When: If Table 155, Register 0x32[1:0] = ‘01’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | > 31.25 mA |
| 00000010 | 0x02 | > 62.5 mA |
| ... | ... | ... |
| 11111111 | 0xFF | > 7.968 A |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 276, Register 0x6C.
- NOTE 2: This register is applicable regardless of the setting in Table 247, Register 0x4F [6]. For dual phase operation, registers Table 135, Register 0x1E [7:0] and Table 183, Register 0x11B [7:0] must be configured identical.

## R11C (0x11C) — SWE_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING, SWF_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING, SWE_VOLTAGE_RANGE, SWF_VOLTAGE_RANGE, SWC_VOLTAGE_RANGE_EXT

Region: Host Region | Source: JESD301-5 Table 184, p.203

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWE_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING | RW | 01 |
| 5:4 | SWF_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING | RW | 01 |
| 3 | SWE_VOLTAGE_RANGE | RW | 0 |
| 2:1 | SWF_VOLTAGE_RANGE | RW | 0 |
| 0 | SWC_VOLTAGE_RANGE_EXT | RW | 0 |

### [7:6] SWE_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING

- Description: COT Ivalley_limit[2]
- Attribute: RW — Read/Write
- Default: 01 → 7A

| Code (bin) | Meaning |
|---|---|
| 00 | 6A |
| 01 | 7A |
| 10 | 8A |
| 11 | 9A |

### [5:4] SWF_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING

- Description: COT Ivalley_limit[3]
- Attribute: RW — Read/Write
- Default: 01 → 7A

| Code (bin) | Meaning |
|---|---|
| 00 | 6A |
| 01 | 7A |
| 10 | 8A |
| 11 | 9A |

### [3] SWE_VOLTAGE_RANGE

- Description: SWE Output Voltage Range Selection[4],[5]
- Attribute: RW — Read/Write
- Default: 0 → Range: 800 mV to 1435 mV for SWA; 5 mV step size

| Code (bin) | Meaning |
|---|---|
| 0 | Range: 800 mV to 1435 mV for SWA; 5 mV step size |
| 1 | Range: 600 mV to 1235 mV for SWA; 5 mV step size |

### [2:1] SWF_VOLTAGE_RANGE

- Description: SWF Output Voltage Range Selection[6],[7]
- Attribute: RW — Read/Write
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 00 | Range: 800 mV to 1435 mV for SWF; 5 mV step size |
| 01 | Range: 600 mV to 1235 mV for SWF; 5 mV step size |
| 10 | Range: 400 mV to 717.5 mV for SWF; 2.5 mV step size |
| 11 | Reserved |

### [0] SWC_VOLTAGE_RANGE_EXT

- Description: SWC Output Voltage Range Selection[8]. The MSB bit Table 184, Register 0x11C [0] plus LSB bit Table 148, Register 0x2B [3] makes 2 bit encoding as following:
- Attribute: RW — Read/Write
- Default: 0
- Note: the codes below are wider than this 1-bit field; the encoding combines bits from more than one field/register (see Description).

| Code (bin) | Meaning |
|---|---|
| 00 | Range: 800 mV to 1435 mV for SWC; 5 mV step size |
| 01 | Range: 600 mV to 1235 mV for SWC; 5 mV step size |
| 10 | Range: 400 mV to 717.5 mV for SWC; 2.5 mV step size |
| 11 | Reserved |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 250, Register 0x52.
- NOTE 2: This register is applicable regardless of the setting in Table 247, Register 0x4F [5,0].
- NOTE 3: This register is applicable regardless of the setting in Table 247, Register 0x4F [6].
- NOTE 4: Range and resolution selection applies to register Table 185, Register 0x11D [7:1].
- NOTE 5: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’ or ‘01’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care.
- NOTE 6: Range and resolution selection applies to register Table 187, Register 0x11F [7:1].
- NOTE 7: This register is only applicable if Table 247, Register 0x4F [6] = ‘0’. For any other setting in Table 247, Register 0x4F [6], this register does not apply and it is a don’t care.
- NOTE 8: Range selection applies to registers Table 142, Register 0x25 [7:1].

## R11D (0x11D) — SWE_VOLTAGE_SETTING, SWE_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

Region: Host Region | Source: JESD301-5 Table 185, p.204

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:1 | SWE_VOLTAGE_SETTING | RW | 011 1100 |
| 0 | SWE_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING | RW | 0 |

### [7:1] SWE_VOLTAGE_SETTING

- Description: SWE Output Regulator Voltage Setting[4],[5]
- Attribute: RW — Read/Write
- Default: 011 1100 → 1100 mV or 900 mV

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 0000000 | 0x00 | 800 mV[6] or 600 mV[7] |
| 0000001 | 0x01 | 805 mV or 605 mV |
| 0000010 | 0x02 | 810 mV or 610 mV |
| ... | ... | ... |
| 0111100 | 0x3C | 1100 mV or 900 mV |
| ... | ... | ... |
| 1111101 | 0x7D | 1425 mV or 1225 mV |
| 1111110 | 0x7E | 1430 mV or 1230 mV |
| 1111111 | 0x7F | 1435 mV or 1235 mV |

### [0] SWE_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

- Description: SWE Output Threshold Low Side Voltage For Power Good Status
- Attribute: RW — Read/Write
- Default: 0 → -5% from the setting in Table 185, Register 0x11D [7:1]

| Code (bin) | Meaning |
|---|---|
| 0 | -5% from the setting in Table 185, Register 0x11D [7:1] |
| 1 | -7.5% from the setting in Table 185, Register 0x11D [7:1] |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 251, Register 0x53.
- NOTE 2: If required, the host must update the settings in register Table 185, Register 0x11D [0], Table 185, Register 0x11D [7:2] and Table 184, Register 0x11C [7:6] first prior to updating the settings in the register Table 185, Register 0x11D [7:1].
- NOTE 3: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’ or ‘01’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care.
- NOTE 4: PMIC guarantees efficiency spec within a range of 1050 mV to 1160 mV.
- NOTE 5: After VR is enabled, the host may update this register to any new setting that it may desire. However to prevent false error trigger, the PMIC internally will increment the SWE output voltage setting by 5 mV at a time. The time it takes for PMIC to adjust the output voltage is 5 μs for each 5 mV increment. The host must wait sufficient time for PMIC to adjust to final value. As an example, if host adjusts the output voltage by 50 mV from the original value, the host must wait minimum of 50 μs before PMIC can guarantee the new output voltage. During this time, PMIC masks the PWR_GOOD output signal assertion to prevent any artificial error due to the crossing of the output voltage threshold setting. However, PMIC does assert PWR_GOOD output signal if there are any abnormal issues that triggers VR Disable command as described in Table 27. Further, PMIC does monitor PWR_GOOD input signal and executes power off config sequence registers if it is registered low when Table 155, Register 0x32 [5] = ‘1’.
- NOTE 6: Table 184, Register 0x11C [3] = ‘0’; 5 mV step size.
- NOTE 7: Table 184, Register 0x11C [3] = ‘1’; 5 mV step size

## R11E (0x11E) — SWE_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING, SWE_OVER_VOLTAGE_THRESHOLD_SETTING, SWE_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING, SWE_OUTPUT_SOFT_STOP_TIME

Region: Host Region | Source: JESD301-5 Table 186, p.205

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWE_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING | RW | 01 |
| 5:4 | SWE_OVER_VOLTAGE_THRESHOLD_SETTING | RW | 10 |
| 3:2 | SWE_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING | RW | 00 |
| 1:0 | SWE_OUTPUT_SOFT_STOP_TIME | RW | 00 |

### [7:6] SWE_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING

- Description: SWE Output Threshold High Side Voltage For Power Good Status
- Attribute: RW — Read/Write
- Default: 01 → +7.5% from the setting in Table 185, Register 0x11D [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +5% from the setting in Table 185, Register 0x11D [7:1] |
| 01 | +7.5% from the setting in Table 185, Register 0x11D [7:1] |
| 10 | +10% from the setting in Table 185, Register 0x11D [7:1] |
| 11 | Reserved |

### [5:4] SWE_OVER_VOLTAGE_THRESHOLD_SETTING

- Description: SWE Output Regulator Threshold For Over Voltage Status[4]
- Attribute: RW — Read/Write
- Default: 10 → +12.5% from the setting in Table 185, Register 0x11D [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +7.5% from the setting in Table 185, Register 0x11D [7:1] |
| 01 | +10% from the setting in Table 185, Register 0x11D [7:1] |
| 10 | +12.5% from the setting in Table 185, Register 0x11D [7:1] |
| 11 | Reserved |

### [3:2] SWE_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING

- Description: SWE Output Regulator Threshold For Under Voltage Lockout Status
- Attribute: RW — Read/Write
- Default: 00 → -10% from the setting in Table 185, Register 0x11D [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | -10% from the setting in Table 185, Register 0x11D [7:1] |
| 01 | -12.5% from the setting in Table 185, Register 0x11D [7:1] |
| 10 | Reserved |
| 11 | Reserved |

### [1:0] SWE_OUTPUT_SOFT_STOP_TIME

- Description: SWE Output Regulator Soft Stop Time After VR Disable[5]
- Attribute: RW — Read/Write
- Default: 00 → 0.5 ms

| Code (bin) | Meaning |
|---|---|
| 00 | 0.5 ms |
| 01 | 1 ms |
| 10 | 2 ms |
| 11 | 4 ms |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 252, Register 0x54.
- NOTE 2: If required, the host must update the setting in register Table 185, Register 0x11D [0], Table 186, Register 0x11E [7:2] and Table 184, Register 0x11C [7:6] first prior to updating the settings in the register Table 185, Register 0x11D [7:1].
- NOTE 3: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’ or ‘01’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care.
- NOTE 4: The setting for the Over Voltage must be higher than Power Good High Side Voltage threshold in Table 185, Register 0x11D[7:6].
- NOTE 5: This is the time it takes for buck regulator to go from steady state voltage to 0 V.

## R11F (0x11F) — SWF_VOLTAGE_SETTING, SWF_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

Region: Host Region | Source: JESD301-5 Table 187, p.206

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:1 | SWF_VOLTAGE_SETTING | RW | 011 1100 |
| 0 | SWF_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING | RW | 0 |

### [7:1] SWF_VOLTAGE_SETTING

- Description: SWF Output Regulator Voltage Setting[4],[5]
- Attribute: RW — Read/Write
- Default: 011 1100 → 1100 mV or 900 mV or 550 mV

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 0000000 | 0x00 | 800 mV[6] or 600 mV[7] or 400 mV[8] |
| 0000001 | 0x01 | 805 mV or 605 mV or 402.5 mV |
| 0000010 | 0x02 | 810 mV or 610 mV or 405 mV |
| ... | ... | ... |
| 0111100 | 0x3C | 1100 mV or 900 mV or 550 mV |
| ... | ... | ... |
| 1111101 | 0x7D | 1425 mV or 1225 mV or 712.5 mV |
| 1111110 | 0x7E | 1430 mV or 1230 mV or 715 mV |
| 1111111 | 0x7F | 1435 mV or 1235 mV or 717.5 mV |

### [0] SWF_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

- Description: SWF Output Threshold Low Side Voltage For Power Good Status
- Attribute: RW — Read/Write
- Default: 0 → -5% from the setting in Table 187, Register 0x11F [7:1]

| Code (bin) | Meaning |
|---|---|
| 0 | -5% from the setting in Table 187, Register 0x11F [7:1] |
| 1 | -7.5% from the setting in Table 187, Register 0x11F [7:1] |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 253, Register 0x55.
- NOTE 2: If required, the host must update the settings in register Table 187, Register 0x11F [0], Table 188, Register 0x120 [7:2] and Table 184, Register 0x11C [5:4] first prior to updating the settings in the register Table 187, Register 0x11F [7:1].
- NOTE 3: This register is only applicable if Table 247, Register 0x4F [6] = ‘0’. For any other setting in Table 247, Register 0x4F [6], this register does not apply and it is a don’t care.
- NOTE 4: PMIC guarantees efficiency spec within a range of 1050 mV to 1160 mV.
- NOTE 5: After VR is enabled, the host may update this register to any new setting that it may desire. However to prevent false error trigger, the PMIC internally will increment the SWF output voltage setting by 5 mV at a time. The time it takes for PMIC to adjust the output voltage is 5 μs for each 5 mV increment. The host must wait sufficient time for PMIC to adjust to final value. As an example, if host adjusts the output voltage by 50 mV from the original value, the host must wait minimum of 50 μs before PMIC can guarantee the new output voltage. During this time, PMIC masks the PWR_GOOD output signal assertion to prevent any artificial error due to the crossing of the output voltage threshold setting. However, PMIC does assert PWR_GOOD output signal if there are any abnormal issues that triggers VR Disable command as described in Table 27. Further, PMIC does monitor PWR_GOOD input signal and executes power off config sequence registers if it is registered low when Table 155, Register 0x32 [5] = ‘1’.
- NOTE 6: Table 184, Register 0x11C [2:1] = ‘00’; 5 mV step size.
- NOTE 7: Table 184, Register 0x11C [2:1] = ‘01’; 5 mV step size
- NOTE 8: Table 184, Register 0x11C [2:1] = ‘10’; 2.5 mV step size.

## R120 (0x120) — SWF_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING, SWF_OVER_VOLTAGE_THRESHOLD_SETTING, SWF_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING, SWF_OUTPUT_SOFT_STOP_TIME

Region: Host Region | Source: JESD301-5 Table 188, p.207

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWF_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING | RW | 01 |
| 5:4 | SWF_OVER_VOLTAGE_THRESHOLD_SETTING | RW | 10 |
| 3:2 | SWF_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING | RW | 00 |
| 1:0 | SWF_OUTPUT_SOFT_STOP_TIME | RW | 00 |

### [7:6] SWF_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING

- Description: SWF Output Threshold High Side Voltage For Power Good Status
- Attribute: RW — Read/Write
- Default: 01 → +7.5% from the setting in Table 187, Register 0x11F [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +5% from the setting in Table 187, Register 0x11F [7:1] |
| 01 | +7.5% from the setting in Table 187, Register 0x11F [7:1] |
| 10 | +10% from the setting in Table 187, Register 0x11F [7:1] |
| 11 | Reserved |

### [5:4] SWF_OVER_VOLTAGE_THRESHOLD_SETTING

- Description: SWF Output Regulator Threshold For Over Voltage Status[4]
- Attribute: RW — Read/Write
- Default: 10 → +12.5% from the setting in Table 187, Register 0x11F [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +7.5% from the setting in Table 187, Register 0x11F [7:1] |
| 01 | +10% from the setting in Table 187, Register 0x11F [7:1] |
| 10 | +12.5% from the setting in Table 187, Register 0x11F [7:1] |
| 11 | Reserved |

### [3:2] SWF_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING

- Description: SWF Output Regulator Threshold For Under Voltage Lockout Status
- Attribute: RW — Read/Write
- Default: 00 → -10% from the setting in Table 187, Register 0x11F [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | -10% from the setting in Table 187, Register 0x11F [7:1] |
| 01 | -12.5% from the setting in Table 187, Register 0x11F [7:1] |
| 10 | Reserved |
| 11 | Reserved |

### [1:0] SWF_OUTPUT_SOFT_STOP_TIME

- Description: SWF Output Regulator Soft Stop Time After VR Disable[5]
- Attribute: RW — Read/Write
- Default: 00 → 0.5 ms

| Code (bin) | Meaning |
|---|---|
| 00 | 0.5 ms |
| 01 | 1 ms |
| 10 | 2 ms |
| 11 | 4 ms |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 254, Register 0x56.
- NOTE 2: If required, the host must update the settings in register Table 187, Register 0x11F [0], Table 188, Register 0x120 [7:2] and Table 184, Register 0x11C [5:4] first prior to updating the settings in the register Table 187, Register 0x11F [7:1].
- NOTE 3: This register is only applicable if Table 247, Register 0x4F [6] = ‘0’. For any other setting in Table 247, Register 0x4F [6], this register does not apply and it is a don’t care.
- NOTE 4: The setting for the Over Voltage must be higher than Power Good High Side Voltage threshold in Table 188, Register 0x120[7:6].
- NOTE 5: This is the time it takes for buck regulator to go from steady state voltage to 0 V.

## R121 (0x121) — SWE_MODE_SELECT, SWE_SWITCHING_FREQ, SWF_MODE_SELECT, SWF_SWITCHING_FREQ

Region: Host Region | Source: JESD301-5 Table 189, p.208

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWE_MODE_SELECT | RW | 10 |
| 5:4 | SWE_SWITCHING_FREQ | RW | 01 |
| 3:2 | SWF_MODE_SELECT | RW | 10 |
| 1:0 | SWF_SWITCHING_FREQ | RW | 01 |

### [7:6] SWE_MODE_SELECT

- Description: Switch Node E Output Regulator Mode Selection[3]
- Attribute: RW — Read/Write
- Default: 10 → COT; DCM (Constant on Time; Discontinuous Current Mode)

| Code (bin) | Meaning |
|---|---|
| 00 | Reserved |
| 01 | Reserved |
| 10 | COT; DCM (Constant on Time; Discontinuous Current Mode) |
| 11 | COT; Forced CCM (Constant on Time; Continuous Current Mode) |

### [5:4] SWE_SWITCHING_FREQ

- Description: Switch Node E Output Regulator Switching Frequency[3]
- Attribute: RW — Read/Write
- Default: 01 → 750 KHz

| Code (bin) | Meaning |
|---|---|
| 00 | 500 KHz |
| 01 | 750 KHz |
| 10 | Reserved |
| 11 | Reserved |

### [3:2] SWF_MODE_SELECT

- Description: Switch Node F Output Regulator Mode Selection[4]
- Attribute: RW — Read/Write
- Default: 10 → COT; DCM (Constant on Time; Discontinuous Current Mode)

| Code (bin) | Meaning |
|---|---|
| 00 | Reserved |
| 01 | Reserved |
| 10 | COT; DCM (Constant on Time; Discontinuous Current Mode) |
| 11 | COT; Forced CCM (Constant on Time; Continuous Current Mode) |

### [1:0] SWF_SWITCHING_FREQ

- Description: Switch Node F Output Regulator Switching Frequency[4]
- Attribute: RW — Read/Write
- Default: 01 → 750 KHz

| Code (bin) | Meaning |
|---|---|
| 00 | 500 KHz |
| 01 | 750 KHz |
| 10 | Reserved |
| 11 | Reserved |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 255, Register 0x57.
- NOTE 2: If required, the host must adjust this register first before issuing VR Enable command in Table 155, Register 0x32 [7].
- NOTE 3: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’ or ‘01’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care.
- NOTE 4: This register is only applicable if Table 247, Register 0x4F [6] = ‘0’. For any other setting in Table 247, Register 0x4F [6], this register does not apply and it is a don’t care.

## R122 (0x122) — SWE_OUTPUT_SOFT_START_TIME, SWF_OUTPUT_SOFT_START_TIME

Region: Host Region | Source: JESD301-5 Table 190, p.209

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:5 | SWE_OUTPUT_SOFT_START_TIME | RW | 001 |
| 4 | RESERVED | RV | 0 |
| 3:1 | SWF_OUTPUT_SOFT_START_TIME | RW | 001 |
| 0 | RESERVED | RV | 0 |

### [7:5] SWE_OUTPUT_SOFT_START_TIME

- Description: SWE Output Regulator Soft Start Time After VR Enable[3],[4]
- Attribute: RW — Read/Write
- Default: 001 → 2 ms

| Code (bin) | Meaning |
|---|---|
| 000 | 1 ms |
| 001 | 2 ms |
| 010 | 4 ms |
| 011 | 6 ms |
| ... | ... |
| 111 | 14 ms |

### [4] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [3:1] SWF_OUTPUT_SOFT_START_TIME

- Description: SWF Output Regulator Soft Start Time After VR Enable[4],[5]
- Attribute: RW — Read/Write
- Default: 001 → 2 ms

| Code (bin) | Meaning |
|---|---|
| 000 | 1 ms |
| 001 | 2 ms |
| 010 | 4 ms |
| 011 | 6 ms |
| ... | ... |
| 111 | 14 ms |

### [0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 264, Register 0x60.
- NOTE 2: If required, the host must adjust this register first before issuing VR Enable command in Table 155, Register 0x32 [7].
- NOTE 3: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’ or ‘01’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care.
- NOTE 4: This is the time it takes for buck regulator to go from 0 V to steady state voltage (the actual voltage varies based on pre- programmed voltage).
- NOTE 5: This register is only applicable if Table 247, Register 0x4F [6] = ‘0’. For any other setting in Table 247, Register 0x4F [6], this register does not apply and it is a don’t care.

## R123 (0x123) — SWE_REGULATOR_CONTROL, SWF_REGULATOR_CONTROL

Region: Host Region | Source: JESD301-5 Table 191, p.210

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:2 | RESERVED | RV | 0 |
| 1 | SWE_REGULATOR_CONTROL | RW | 0 |
| 0 | SWF_REGULATOR_CONTROL | RW | 0 |

### [7:2] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [1] SWE_REGULATOR_CONTROL

- Description: Disable SWE Regulator Output[1],[2],[3]
- Attribute: RW — Read/Write
- Default: 0 → Disable Switch Node E Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Disable Switch Node E Output Regulator |
| 1 | Enable Switch Node E Output Regulator |

### [0] SWF_REGULATOR_CONTROL

- Description: Disable SWF Regulator Output[2],[3],[4]
- Attribute: RW — Read/Write
- Default: 0 → Disable Switch Node F Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Disable Switch Node F Output Regulator |
| 1 | Enable Switch Node F Output Regulator |

**Notes**

- NOTE 1: This register is only applicable if Table 247, Register 0x4F [5,0] = ‘00’ or ‘01’. For any other setting in Table 247, Register 0x4F [5,0], this register does not apply and it is a don’t care.
- NOTE 2: This bit must be used only after power up sequence (after VR Enable command). At first power up, PMIC automatically updates the status of this register to ‘1’ after VR Enable command. When VR Enable command is registered, the PMIC updates this register based on Power On Sequence Configuration (0 to 5) setting. If enabled in Power On Sequence Configuration 0 to 5 registers, only then, under non write-protect mode of operation, the PMIC’s output regulator can be disabled by clearing this bit and they can be re-enabled again by setting this bit. The PMIC does not alter its Power Good output signal and keeps it asserted High. If any regulator is not enabled in Power on Sequence Configuration 0 to 5, it cannot be enabled using this register. For example, if only SWA is enabled and SWB, SWC,SWD, SWE, and SWF is not enabled in Table 232, Register 0x40 [7:0] to Table 236, Register 0x44 [7:0],Table 265, Register 0x61 [7:0] then only SWA can be disabled and then re-enabled again but SWB, SWC, SWD, SWE and SWF cannot be enabled using Table 152, Register 0x2F [6:3], Table 191, Register 0x123 [1:0].
- NOTE 3: In non write-protect mode, after VR enable command, if any output regulators are disabled by clearing Table 152, Register 0x2F [6:3],Table 191, Register 0x123 [1:0] and then if host issues VR Disable command or PMIC internally triggers VR Disable command, the PMIC keeps the disabled output regulator in Table 152, Register 0x2F[6:3],Table 191, Register 0x123 [1:0] off and remaining output regulators are disabled by following the Power Off Sequence Configuration 0 to 5 settings.
- NOTE 4: This register is only applicable if Table 247, Register 0x4F [6] = ‘0’. For any other setting in Table 247, Register 0x4F [6], this register does not apply and it is a don’t care.

## R12E (0x12E) — RESET_N_CONTROL

Region: Host Region | Source: JESD301-5 Table 192, p.210

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | RESET_N_CONTROL | RW | 0 |
| 5:0 | RESERVED | RV | 0 |

### [7:6] RESET_N_CONTROL

- Description: Reset_n Input Pin Enable & Configuration Control All other encodings are reserved
- Attribute: RW — Read/Write
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 00 | Disable Reset_n Input Pin |
| 01 | Enable; Reset_n assertion resets only Bus Interface (i.e., I2C and I3C bus)[1] |

### [5:0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

**Notes**

- NOTE 1: The PMIC resets I2C/I3C interface as if it was a power on reset. The PMIC returns to I2C mode (Table 155, Register 0x32 [6] = ‘0’), 1 byte address mode (Table 153, Register 0x30 [2] = ‘0’), clears Table 115, Register 0x0A [3:2] = ‘00’, Table 158, Register 0x34 [7:5] = ‘000’ and Table 158, Register 0x34 [3:1] = ‘111’. The host shall re-issue SETHID followed by SETAASA CCC to ensure all components on the module are aligned to same mode of operation. Further, the host should also update the Table 153, Register 0x30 [2] to ‘1’ for 2 byte address mode.

## R12F (0x12F) — ERROR_INJECTION_RAIL_SELECTION_EXT, ERROR_INJECTION_MTP_SELECTION

Region: Host Region | Source: JESD301-5 Table 193, p.211

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | RESERVED | RV | 0 |
| 5:4 | ERROR_INJECTION_RAIL_SELECTION_EXT | RW | 0 |
| 3:2 | RESERVED | RV | 0 |
| 1:0 | ERROR_INJECTION_MTP_SELECTION | RW | 0 |

### [7:6] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [5:4] ERROR_INJECTION_RAIL_SELECTION_EXT

- Description: Error Injection - Output Rail Selection Extension[4],[5]
- Attribute: RW — Read/Write
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 00 | Undefined |
| 01 | SWE Output Only |
| 10 | SWF Output Only |
| 11 | Reserved |

### [3:2] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [1:0] ERROR_INJECTION_MTP_SELECTION

- Description: Error Injection - MTP Selection[6]
- Attribute: RW — Read/Write
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 00 | Undefined |
| 01 | DIMM Vendor MTP |
| 10 | PMIC Vendor MTP |
| 11 | Reserved |

**Notes**

- NOTE 1: Refer to Clause 6.28 for error function usage model. The host can erase the error log registers (Table 109, Register 0x04 to Table 112, Register 0x07) by writing 0x74 to Table 162, Register 0x39.
- NOTE 2: To exit from Error Injection Mode, the PMIC must go through power cycle of both VIN_Bulk and VIN_Mgmt input supply. Error injection function utilizes two registers: Table 159, Register 0x35 and Table 193, Register 0x12F.
- NOTE: 3
- NOTE 4: The register Table 159, Register 0x35 [6:4] and Table 193, Register 0x12F [5:4] is only applicable if Table 159, Register 0x35 [2:0] is ‘000’ and Table 193, Register 0x12F [1:0] = ‘00’. Any value other than ‘000’ in Table 159, Register 0x35 [6:4], ‘00’ in Table 193, Register 0x12F [5:4], ‘000’ in Table 159, Register 0x35 [2:0] and ‘00’ in Table 193, Register 0x12F [1:0] is considered an illegal setting and PMIC operation is not guaranteed.
- NOTE 5: If dual or three phase regulator is selected for SWA, SWB and SWE, use SWA encoding to inject the error. If dual phase regulator is selected for SWC and SWF, use SWC encoding to inject the error. Register Table 159, Register 0x35 [3] selects either over voltage or under voltage condition for the setting selected in this register.
- NOTE 6: This register Table 193, Register 0x12F [1:0] is only applicable if Table 159, Register 0x35 [6:0] is ‘000 0000’ and Table 193, Register 0x12F [5:4] is ‘00’. Any value other than ‘000 0000’ in Table 159, Register 0x35 [6:0] and ‘00’ in Table 193, Register 0x12F [5:4] is considered an illegal setting and PMIC operation is not guaranteed.

## R130 (0x130) — SERIAL_NUMBER_BYTE_0

Region: Host Region | Source: JESD301-5 Table 194, p.211

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SERIAL_NUMBER_BYTE_0 | ROA | - |

### [7:0] SERIAL_NUMBER_BYTE_0

- Description: Byte 0 of the Unique 56-bit Serial number Serial number is vendor specific
- Attribute: ROA — Read Only (writes have no effect); Persistent, set by the PMIC vendor at manufacturing
- Default: -
- Values: no per-value encoding is listed in the spec for this field.

## R131 (0x131) — SERIAL_NUMBER_BYTE_1

Region: Host Region | Source: JESD301-5 Table 195, p.212

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SERIAL_NUMBER_BYTE_1 | ROA | - |

### [7:0] SERIAL_NUMBER_BYTE_1

- Description: Byte 1 of the Unique 56-bit Serial number Serial number is vendor specific
- Attribute: ROA — Read Only (writes have no effect); Persistent, set by the PMIC vendor at manufacturing
- Default: -
- Values: no per-value encoding is listed in the spec for this field.

## R132 (0x132) — SERIAL_NUMBER_BYTE_2

Region: Host Region | Source: JESD301-5 Table 196, p.212

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SERIAL_NUMBER_BYTE_2 | ROA | - |

### [7:0] SERIAL_NUMBER_BYTE_2

- Description: Byte 2 of the Unique 56-bit Serial number Serial number is vendor specific
- Attribute: ROA — Read Only (writes have no effect); Persistent, set by the PMIC vendor at manufacturing
- Default: -
- Values: no per-value encoding is listed in the spec for this field.

## R133 (0x133) — SERIAL_NUMBER_BYTE_3

Region: Host Region | Source: JESD301-5 Table 197, p.212

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SERIAL_NUMBER_BYTE_3 | ROA | - |

### [7:0] SERIAL_NUMBER_BYTE_3

- Description: Byte 3 of the Unique 56-bit Serial number Serial number is vendor specific
- Attribute: ROA — Read Only (writes have no effect); Persistent, set by the PMIC vendor at manufacturing
- Default: -
- Values: no per-value encoding is listed in the spec for this field.

## R134 (0x134) — SERIAL_NUMBER_BYTE_4

Region: Host Region | Source: JESD301-5 Table 198, p.212

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SERIAL_NUMBER_BYTE_4 | ROA | - |

### [7:0] SERIAL_NUMBER_BYTE_4

- Description: Byte 4 of the Unique 56-bit Serial number Serial number is vendor specific
- Attribute: ROA — Read Only (writes have no effect); Persistent, set by the PMIC vendor at manufacturing
- Default: -
- Values: no per-value encoding is listed in the spec for this field.

## R135 (0x135) — SERIAL_NUMBER_BYTE_5

Region: Host Region | Source: JESD301-5 Table 199, p.212

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SERIAL_NUMBER_BYTE_5 | ROA | - |

### [7:0] SERIAL_NUMBER_BYTE_5

- Description: Byte 5 of the Unique 56-bit Serial number Serial number is vendor specific
- Attribute: ROA — Read Only (writes have no effect); Persistent, set by the PMIC vendor at manufacturing
- Default: -
- Values: no per-value encoding is listed in the spec for this field.

## R136 (0x136) — SERIAL_NUMBER_BYTE_6

Region: Host Region | Source: JESD301-5 Table 200, p.213

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SERIAL_NUMBER_BYTE_6 | ROA | - |

### [7:0] SERIAL_NUMBER_BYTE_6

- Description: Byte 6 of the Unique 56-bit Serial number Serial number is vendor specific
- Attribute: ROA — Read Only (writes have no effect); Persistent, set by the PMIC vendor at manufacturing
- Default: -
- Values: no per-value encoding is listed in the spec for this field.

## R140 (0x140) — SWA_OV_FAULT, SWB_OV_FAULT, SWC_OV_FAULT, SWD_OV_FAULT, SWE_OV_FAULT, SWF_OV_FAULT, VIN_BULK_OV_FAULT

Title: R140 - 1st Fault Error Log | Region: Host Region | Source: JESD301-5 Table 201, p.213

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | SWA_OV_FAULT | RON | 0 |
| 6 | SWB_OV_FAULT | RON | 0 |
| 5 | SWC_OV_FAULT | RON | 0 |
| 4 | SWD_OV_FAULT | RON | 0 |
| 3 | SWE_OV_FAULT | RON | 0 |
| 2 | SWF_OV_FAULT | RON | 0 |
| 1 | VIN_BULK_OV_FAULT | RON | 0 |
| 0 | RESERVED | RV | 0 |

### [7] SWA_OV_FAULT

- Description: SWA Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [6] SWB_OV_FAULT

- Description: SWB Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [5] SWC_OV_FAULT

- Description: SWC Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [4] SWD_OV_FAULT

- Description: SWD Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [3] SWE_OV_FAULT

- Description: SWE Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [2] SWF_OV_FAULT

- Description: SWF Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [1] VIN_BULK_OV_FAULT

- Description: VIN_Bulk OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

## R141 (0x141) — SWA_UV_FAULT, SWB_UV_FAULT, SWC_UV_FAULT, SWD_UV_FAULT, SWE_UV_FAULT, SWF_UV_FAULT, CRITICAL_TEMP_FAULT

Title: R141 - 1st Fault Error Log | Region: Host Region | Source: JESD301-5 Table 202, p.214

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | SWA_UV_FAULT | RON | 0 |
| 6 | SWB_UV_FAULT | RON | 0 |
| 5 | SWC_UV_FAULT | RON | 0 |
| 4 | SWD_UV_FAULT | RON | 0 |
| 3 | SWE_UV_FAULT | RON | 0 |
| 2 | SWF_UV_FAULT | RON | 0 |
| 1 | RESERVED | RV | 0 |
| 0 | CRITICAL_TEMP_FAULT | RON | 0 |

### [7] SWA_UV_FAULT

- Description: SWA Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [6] SWB_UV_FAULT

- Description: SWB Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [5] SWC_UV_FAULT

- Description: SWC Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [4] SWD_UV_FAULT

- Description: SWD Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [3] SWE_UV_FAULT

- Description: SWE Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [2] SWF_UV_FAULT

- Description: SWF Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [1] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [0] CRITICAL_TEMP_FAULT

- Description: Critical Temperature Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

## R142 (0x142) — SWA_OV_FAULT, SWB_OV_FAULT, SWC_OV_FAULT, SWD_OV_FAULT, SWE_OV_FAULT, SWF_OV_FAULT, VIN_BULK_OV_FAULT

Title: R142 - 2nd Fault Error Log | Region: Host Region | Source: JESD301-5 Table 203, p.214 | Encoding: same as 0x140 (spec: 'See encoding definition in 140[7:0]')

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | SWA_OV_FAULT | RON | 0 |
| 6 | SWB_OV_FAULT | RON | 0 |
| 5 | SWC_OV_FAULT | RON | 0 |
| 4 | SWD_OV_FAULT | RON | 0 |
| 3 | SWE_OV_FAULT | RON | 0 |
| 2 | SWF_OV_FAULT | RON | 0 |
| 1 | VIN_BULK_OV_FAULT | RON | 0 |
| 0 | RESERVED | RON | 0 |

### [7] SWA_OV_FAULT

- Description: SWA Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [6] SWB_OV_FAULT

- Description: SWB Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [5] SWC_OV_FAULT

- Description: SWC Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [4] SWD_OV_FAULT

- Description: SWD Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [3] SWE_OV_FAULT

- Description: SWE Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [2] SWF_OV_FAULT

- Description: SWF Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [1] VIN_BULK_OV_FAULT

- Description: VIN_Bulk OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [0] RESERVED

- Description: Reserved
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0

## R143 (0x143) — SWA_UV_FAULT, SWB_UV_FAULT, SWC_UV_FAULT, SWD_UV_FAULT, SWE_UV_FAULT, SWF_UV_FAULT, CRITICAL_TEMP_FAULT

Title: R143 - 2nd Fault Error Log | Region: Host Region | Source: JESD301-5 Table 204, p.215 | Encoding: same as 0x141 (spec: 'See encoding definition in 141[7:0]')

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | SWA_UV_FAULT | RON | 0 |
| 6 | SWB_UV_FAULT | RON | 0 |
| 5 | SWC_UV_FAULT | RON | 0 |
| 4 | SWD_UV_FAULT | RON | 0 |
| 3 | SWE_UV_FAULT | RON | 0 |
| 2 | SWF_UV_FAULT | RON | 0 |
| 1 | RESERVED | RON | 0 |
| 0 | CRITICAL_TEMP_FAULT | RON | 0 |

### [7] SWA_UV_FAULT

- Description: SWA Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [6] SWB_UV_FAULT

- Description: SWB Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [5] SWC_UV_FAULT

- Description: SWC Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [4] SWD_UV_FAULT

- Description: SWD Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [3] SWE_UV_FAULT

- Description: SWE Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [2] SWF_UV_FAULT

- Description: SWF Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [1] RESERVED

- Description: Reserved
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0

### [0] CRITICAL_TEMP_FAULT

- Description: Critical Temperature Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

## R144 (0x144) — SWA_OV_FAULT, SWB_OV_FAULT, SWC_OV_FAULT, SWD_OV_FAULT, SWE_OV_FAULT, SWF_OV_FAULT, VIN_BULK_OV_FAULT

Title: R144 - 3rd Fault Error Log | Region: Host Region | Source: JESD301-5 Table 205, p.215 | Encoding: same as 0x140 (spec: 'See encoding definition in 140[7:0]')

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | SWA_OV_FAULT | RON | 0 |
| 6 | SWB_OV_FAULT | RON | 0 |
| 5 | SWC_OV_FAULT | RON | 0 |
| 4 | SWD_OV_FAULT | RON | 0 |
| 3 | SWE_OV_FAULT | RON | 0 |
| 2 | SWF_OV_FAULT | RON | 0 |
| 1 | VIN_BULK_OV_FAULT | RON | 0 |
| 0 | RESERVED | RON | 0 |

### [7] SWA_OV_FAULT

- Description: SWA Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [6] SWB_OV_FAULT

- Description: SWB Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [5] SWC_OV_FAULT

- Description: SWC Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [4] SWD_OV_FAULT

- Description: SWD Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [3] SWE_OV_FAULT

- Description: SWE Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [2] SWF_OV_FAULT

- Description: SWF Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [1] VIN_BULK_OV_FAULT

- Description: VIN_Bulk OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [0] RESERVED

- Description: Reserved
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0

## R145 (0x145) — SWA_UV_FAULT, SWB_UV_FAULT, SWC_UV_FAULT, SWD_UV_FAULT, SWE_UV_FAULT, SWF_UV_FAULT, CRITICAL_TEMP_FAULT

Title: R145 - 3rd Fault Error Log | Region: Host Region | Source: JESD301-5 Table 206, p.215 | Encoding: same as 0x141 (spec: 'See encoding definition in 141[7:0]')

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | SWA_UV_FAULT | RON | 0 |
| 6 | SWB_UV_FAULT | RON | 0 |
| 5 | SWC_UV_FAULT | RON | 0 |
| 4 | SWD_UV_FAULT | RON | 0 |
| 3 | SWE_UV_FAULT | RON | 0 |
| 2 | SWF_UV_FAULT | RON | 0 |
| 1 | RESERVED | RON | 0 |
| 0 | CRITICAL_TEMP_FAULT | RON | 0 |

### [7] SWA_UV_FAULT

- Description: SWA Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [6] SWB_UV_FAULT

- Description: SWB Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [5] SWC_UV_FAULT

- Description: SWC Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [4] SWD_UV_FAULT

- Description: SWD Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [3] SWE_UV_FAULT

- Description: SWE Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [2] SWF_UV_FAULT

- Description: SWF Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [1] RESERVED

- Description: Reserved
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0

### [0] CRITICAL_TEMP_FAULT

- Description: Critical Temperature Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

## R146 (0x146) — SWA_OV_FAULT, SWB_OV_FAULT, SWC_OV_FAULT, SWD_OV_FAULT, SWE_OV_FAULT, SWF_OV_FAULT, VIN_BULK_OV_FAULT

Title: R146 - 4th Fault Error Log | Region: Host Region | Source: JESD301-5 Table 207, p.215 | Encoding: same as 0x140 (spec: 'See encoding definition in 140[7:0]')

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | SWA_OV_FAULT | RON | 0 |
| 6 | SWB_OV_FAULT | RON | 0 |
| 5 | SWC_OV_FAULT | RON | 0 |
| 4 | SWD_OV_FAULT | RON | 0 |
| 3 | SWE_OV_FAULT | RON | 0 |
| 2 | SWF_OV_FAULT | RON | 0 |
| 1 | VIN_BULK_OV_FAULT | RON | 0 |
| 0 | RESERVED | RON | 0 |

### [7] SWA_OV_FAULT

- Description: SWA Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [6] SWB_OV_FAULT

- Description: SWB Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [5] SWC_OV_FAULT

- Description: SWC Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [4] SWD_OV_FAULT

- Description: SWD Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [3] SWE_OV_FAULT

- Description: SWE Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [2] SWF_OV_FAULT

- Description: SWF Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [1] VIN_BULK_OV_FAULT

- Description: VIN_Bulk OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [0] RESERVED

- Description: Reserved
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0

## R147 (0x147) — SWA_UV_FAULT, SWB_UV_FAULT, SWC_UV_FAULT, SWD_UV_FAULT, SWE_UV_FAULT, SWF_UV_FAULT, CRITICAL_TEMP_FAULT

Title: R147 - 4th Fault Error Log | Region: Host Region | Source: JESD301-5 Table 208, p.215 | Encoding: same as 0x141 (spec: 'See encoding definition in 141[7:0]')

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | SWA_UV_FAULT | RON | 0 |
| 6 | SWB_UV_FAULT | RON | 0 |
| 5 | SWC_UV_FAULT | RON | 0 |
| 4 | SWD_UV_FAULT | RON | 0 |
| 3 | SWE_UV_FAULT | RON | 0 |
| 2 | SWF_UV_FAULT | RON | 0 |
| 1 | RESERVED | RON | 0 |
| 0 | CRITICAL_TEMP_FAULT | RON | 0 |

### [7] SWA_UV_FAULT

- Description: SWA Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [6] SWB_UV_FAULT

- Description: SWB Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [5] SWC_UV_FAULT

- Description: SWC Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [4] SWD_UV_FAULT

- Description: SWD Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [3] SWE_UV_FAULT

- Description: SWE Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [2] SWF_UV_FAULT

- Description: SWF Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [1] RESERVED

- Description: Reserved
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0

### [0] CRITICAL_TEMP_FAULT

- Description: Critical Temperature Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

## R148 (0x148) — SWA_OV_FAULT, SWB_OV_FAULT, SWC_OV_FAULT, SWD_OV_FAULT, SWE_OV_FAULT, SWF_OV_FAULT, VIN_BULK_OV_FAULT

Title: R148 - 5th Fault Error Log | Region: Host Region | Source: JESD301-5 Table 209, p.215 | Encoding: same as 0x140 (spec: 'See encoding definition in 140[7:0]')

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | SWA_OV_FAULT | RON | 0 |
| 6 | SWB_OV_FAULT | RON | 0 |
| 5 | SWC_OV_FAULT | RON | 0 |
| 4 | SWD_OV_FAULT | RON | 0 |
| 3 | SWE_OV_FAULT | RON | 0 |
| 2 | SWF_OV_FAULT | RON | 0 |
| 1 | VIN_BULK_OV_FAULT | RON | 0 |
| 0 | RESERVED | RON | 0 |

### [7] SWA_OV_FAULT

- Description: SWA Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [6] SWB_OV_FAULT

- Description: SWB Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [5] SWC_OV_FAULT

- Description: SWC Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [4] SWD_OV_FAULT

- Description: SWD Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [3] SWE_OV_FAULT

- Description: SWE Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [2] SWF_OV_FAULT

- Description: SWF Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [1] VIN_BULK_OV_FAULT

- Description: VIN_Bulk OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [0] RESERVED

- Description: Reserved
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0

## R149 (0x149) — SWA_UV_FAULT, SWB_UV_FAULT, SWC_UV_FAULT, SWD_UV_FAULT, SWE_UV_FAULT, SWF_UV_FAULT, CRITICAL_TEMP_FAULT

Title: R149 - 5th Fault Error Log | Region: Host Region | Source: JESD301-5 Table 210, p.216 | Encoding: same as 0x141 (spec: 'See encoding definition in 141[7:0]')

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | SWA_UV_FAULT | RON | 0 |
| 6 | SWB_UV_FAULT | RON | 0 |
| 5 | SWC_UV_FAULT | RON | 0 |
| 4 | SWD_UV_FAULT | RON | 0 |
| 3 | SWE_UV_FAULT | RON | 0 |
| 2 | SWF_UV_FAULT | RON | 0 |
| 1 | RESERVED | RON | 0 |
| 0 | CRITICAL_TEMP_FAULT | RON | 0 |

### [7] SWA_UV_FAULT

- Description: SWA Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [6] SWB_UV_FAULT

- Description: SWB Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [5] SWC_UV_FAULT

- Description: SWC Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [4] SWD_UV_FAULT

- Description: SWD Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [3] SWE_UV_FAULT

- Description: SWE Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [2] SWF_UV_FAULT

- Description: SWF Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [1] RESERVED

- Description: Reserved
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0

### [0] CRITICAL_TEMP_FAULT

- Description: Critical Temperature Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

## R14A (0x14A) — SWA_OV_FAULT, SWB_OV_FAULT, SWC_OV_FAULT, SWD_OV_FAULT, SWE_OV_FAULT, SWF_OV_FAULT, VIN_BULK_OV_FAULT

Title: R14A - 6th Fault Error Log | Region: Host Region | Source: JESD301-5 Table 211, p.216 | Encoding: same as 0x140 (spec: 'See encoding definition in 140[7:0]')

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | SWA_OV_FAULT | RON | 0 |
| 6 | SWB_OV_FAULT | RON | 0 |
| 5 | SWC_OV_FAULT | RON | 0 |
| 4 | SWD_OV_FAULT | RON | 0 |
| 3 | SWE_OV_FAULT | RON | 0 |
| 2 | SWF_OV_FAULT | RON | 0 |
| 1 | VIN_BULK_OV_FAULT | RON | 0 |
| 0 | RESERVED | RON | 0 |

### [7] SWA_OV_FAULT

- Description: SWA Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [6] SWB_OV_FAULT

- Description: SWB Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [5] SWC_OV_FAULT

- Description: SWC Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [4] SWD_OV_FAULT

- Description: SWD Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [3] SWE_OV_FAULT

- Description: SWE Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [2] SWF_OV_FAULT

- Description: SWF Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [1] VIN_BULK_OV_FAULT

- Description: VIN_Bulk OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [0] RESERVED

- Description: Reserved
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0

## R14B (0x14B) — SWA_UV_FAULT, SWB_UV_FAULT, SWC_UV_FAULT, SWD_UV_FAULT, SWE_UV_FAULT, SWF_UV_FAULT, CRITICAL_TEMP_FAULT

Title: R14B - 6th Fault Error Log | Region: Host Region | Source: JESD301-5 Table 212, p.216 | Encoding: same as 0x141 (spec: 'See encoding definition in 141[7:0]')

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | SWA_UV_FAULT | RON | 0 |
| 6 | SWB_UV_FAULT | RON | 0 |
| 5 | SWC_UV_FAULT | RON | 0 |
| 4 | SWD_UV_FAULT | RON | 0 |
| 3 | SWE_UV_FAULT | RON | 0 |
| 2 | SWF_UV_FAULT | RON | 0 |
| 1 | RESERVED | RON | 0 |
| 0 | CRITICAL_TEMP_FAULT | RON | 0 |

### [7] SWA_UV_FAULT

- Description: SWA Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [6] SWB_UV_FAULT

- Description: SWB Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [5] SWC_UV_FAULT

- Description: SWC Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [4] SWD_UV_FAULT

- Description: SWD Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [3] SWE_UV_FAULT

- Description: SWE Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [2] SWF_UV_FAULT

- Description: SWF Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [1] RESERVED

- Description: Reserved
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0

### [0] CRITICAL_TEMP_FAULT

- Description: Critical Temperature Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

## R14C (0x14C) — SWA_OV_FAULT, SWB_OV_FAULT, SWC_OV_FAULT, SWD_OV_FAULT, SWE_OV_FAULT, SWF_OV_FAULT, VIN_BULK_OV_FAULT

Title: R14C - 7th Fault Error Log | Region: Host Region | Source: JESD301-5 Table 213, p.216 | Encoding: same as 0x140 (spec: 'See encoding definition in 140[7:0]')

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | SWA_OV_FAULT | RON | 0 |
| 6 | SWB_OV_FAULT | RON | 0 |
| 5 | SWC_OV_FAULT | RON | 0 |
| 4 | SWD_OV_FAULT | RON | 0 |
| 3 | SWE_OV_FAULT | RON | 0 |
| 2 | SWF_OV_FAULT | RON | 0 |
| 1 | VIN_BULK_OV_FAULT | RON | 0 |
| 0 | RESERVED | RON | 0 |

### [7] SWA_OV_FAULT

- Description: SWA Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [6] SWB_OV_FAULT

- Description: SWB Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [5] SWC_OV_FAULT

- Description: SWC Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [4] SWD_OV_FAULT

- Description: SWD Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [3] SWE_OV_FAULT

- Description: SWE Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [2] SWF_OV_FAULT

- Description: SWF Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [1] VIN_BULK_OV_FAULT

- Description: VIN_Bulk OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [0] RESERVED

- Description: Reserved
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0

## R14D (0x14D) — SWA_UV_FAULT, SWB_UV_FAULT, SWC_UV_FAULT, SWD_UV_FAULT, SWE_UV_FAULT, SWF_UV_FAULT, CRITICAL_TEMP_FAULT

Title: R14D - 7th Fault Error Log | Region: Host Region | Source: JESD301-5 Table 214, p.216 | Encoding: same as 0x141 (spec: 'See encoding definition in 141[7:0]')

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | SWA_UV_FAULT | RON | 0 |
| 6 | SWB_UV_FAULT | RON | 0 |
| 5 | SWC_UV_FAULT | RON | 0 |
| 4 | SWD_UV_FAULT | RON | 0 |
| 3 | SWE_UV_FAULT | RON | 0 |
| 2 | SWF_UV_FAULT | RON | 0 |
| 1 | RESERVED | RON | 0 |
| 0 | CRITICAL_TEMP_FAULT | RON | 0 |

### [7] SWA_UV_FAULT

- Description: SWA Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [6] SWB_UV_FAULT

- Description: SWB Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [5] SWC_UV_FAULT

- Description: SWC Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [4] SWD_UV_FAULT

- Description: SWD Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [3] SWE_UV_FAULT

- Description: SWE Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [2] SWF_UV_FAULT

- Description: SWF Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [1] RESERVED

- Description: Reserved
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0

### [0] CRITICAL_TEMP_FAULT

- Description: Critical Temperature Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

## R14E (0x14E) — SWA_OV_FAULT, SWB_OV_FAULT, SWC_OV_FAULT, SWD_OV_FAULT, SWE_OV_FAULT, SWF_OV_FAULT, VIN_BULK_OV_FAULT

Title: R14E - 8th Fault Error Log | Region: Host Region | Source: JESD301-5 Table 215, p.216 | Encoding: same as 0x140 (spec: 'See encoding definition in 140[7:0]')

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | SWA_OV_FAULT | RON | 0 |
| 6 | SWB_OV_FAULT | RON | 0 |
| 5 | SWC_OV_FAULT | RON | 0 |
| 4 | SWD_OV_FAULT | RON | 0 |
| 3 | SWE_OV_FAULT | RON | 0 |
| 2 | SWF_OV_FAULT | RON | 0 |
| 1 | VIN_BULK_OV_FAULT | RON | 0 |
| 0 | RESERVED | RON | 0 |

### [7] SWA_OV_FAULT

- Description: SWA Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [6] SWB_OV_FAULT

- Description: SWB Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [5] SWC_OV_FAULT

- Description: SWC Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [4] SWD_OV_FAULT

- Description: SWD Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [3] SWE_OV_FAULT

- Description: SWE Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [2] SWF_OV_FAULT

- Description: SWF Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [1] VIN_BULK_OV_FAULT

- Description: VIN_Bulk OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [0] RESERVED

- Description: Reserved
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0

## R14F (0x14F) — SWA_UV_FAULT, SWB_UV_FAULT, SWC_UV_FAULT, SWD_UV_FAULT, SWE_UV_FAULT, SWF_UV_FAULT, CRITICAL_TEMP_FAULT

Title: R14F - 8th Fault Error Log | Region: Host Region | Source: JESD301-5 Table 216, p.217 | Encoding: same as 0x141 (spec: 'See encoding definition in 141[7:0]')

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | SWA_UV_FAULT | RON | 0 |
| 6 | SWB_UV_FAULT | RON | 0 |
| 5 | SWC_UV_FAULT | RON | 0 |
| 4 | SWD_UV_FAULT | RON | 0 |
| 3 | SWE_UV_FAULT | RON | 0 |
| 2 | SWF_UV_FAULT | RON | 0 |
| 1 | RESERVED | RON | 0 |
| 0 | CRITICAL_TEMP_FAULT | RON | 0 |

### [7] SWA_UV_FAULT

- Description: SWA Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [6] SWB_UV_FAULT

- Description: SWB Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [5] SWC_UV_FAULT

- Description: SWC Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [4] SWD_UV_FAULT

- Description: SWD Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [3] SWE_UV_FAULT

- Description: SWE Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [2] SWF_UV_FAULT

- Description: SWF Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [1] RESERVED

- Description: Reserved
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0

### [0] CRITICAL_TEMP_FAULT

- Description: Critical Temperature Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

## R150 (0x150) — SWA_OV_FAULT, SWB_OV_FAULT, SWC_OV_FAULT, SWD_OV_FAULT, SWE_OV_FAULT, SWF_OV_FAULT, VIN_BULK_OV_FAULT

Title: R150 - 9th Fault Error Log | Region: Host Region | Source: JESD301-5 Table 217, p.217 | Encoding: same as 0x140 (spec: 'See encoding definition in 140[7:0]')

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | SWA_OV_FAULT | RON | 0 |
| 6 | SWB_OV_FAULT | RON | 0 |
| 5 | SWC_OV_FAULT | RON | 0 |
| 4 | SWD_OV_FAULT | RON | 0 |
| 3 | SWE_OV_FAULT | RON | 0 |
| 2 | SWF_OV_FAULT | RON | 0 |
| 1 | VIN_BULK_OV_FAULT | RON | 0 |
| 0 | RESERVED | RON | 0 |

### [7] SWA_OV_FAULT

- Description: SWA Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [6] SWB_OV_FAULT

- Description: SWB Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [5] SWC_OV_FAULT

- Description: SWC Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [4] SWD_OV_FAULT

- Description: SWD Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [3] SWE_OV_FAULT

- Description: SWE Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [2] SWF_OV_FAULT

- Description: SWF Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [1] VIN_BULK_OV_FAULT

- Description: VIN_Bulk OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [0] RESERVED

- Description: Reserved
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0

## R151 (0x151) — SWA_UV_FAULT, SWB_UV_FAULT, SWC_UV_FAULT, SWD_UV_FAULT, SWE_UV_FAULT, SWF_UV_FAULT, CRITICAL_TEMP_FAULT

Title: R151 - 9th Fault Error Log | Region: Host Region | Source: JESD301-5 Table 218, p.217 | Encoding: same as 0x141 (spec: 'See encoding definition in 141[7:0]')

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | SWA_UV_FAULT | RON | 0 |
| 6 | SWB_UV_FAULT | RON | 0 |
| 5 | SWC_UV_FAULT | RON | 0 |
| 4 | SWD_UV_FAULT | RON | 0 |
| 3 | SWE_UV_FAULT | RON | 0 |
| 2 | SWF_UV_FAULT | RON | 0 |
| 1 | RESERVED | RON | 0 |
| 0 | CRITICAL_TEMP_FAULT | RON | 0 |

### [7] SWA_UV_FAULT

- Description: SWA Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [6] SWB_UV_FAULT

- Description: SWB Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [5] SWC_UV_FAULT

- Description: SWC Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [4] SWD_UV_FAULT

- Description: SWD Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [3] SWE_UV_FAULT

- Description: SWE Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [2] SWF_UV_FAULT

- Description: SWF Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [1] RESERVED

- Description: Reserved
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0

### [0] CRITICAL_TEMP_FAULT

- Description: Critical Temperature Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

## R152 (0x152) — SWA_OV_FAULT, SWB_OV_FAULT, SWC_OV_FAULT, SWD_OV_FAULT, SWE_OV_FAULT, SWF_OV_FAULT, VIN_BULK_OV_FAULT

Title: R152 - 10th Fault Error Log | Region: Host Region | Source: JESD301-5 Table 219, p.217 | Encoding: same as 0x140 (spec: 'See encoding definition in 140[7:0]')

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | SWA_OV_FAULT | RON | 0 |
| 6 | SWB_OV_FAULT | RON | 0 |
| 5 | SWC_OV_FAULT | RON | 0 |
| 4 | SWD_OV_FAULT | RON | 0 |
| 3 | SWE_OV_FAULT | RON | 0 |
| 2 | SWF_OV_FAULT | RON | 0 |
| 1 | VIN_BULK_OV_FAULT | RON | 0 |
| 0 | RESERVED | RON | 0 |

### [7] SWA_OV_FAULT

- Description: SWA Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [6] SWB_OV_FAULT

- Description: SWB Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [5] SWC_OV_FAULT

- Description: SWC Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [4] SWD_OV_FAULT

- Description: SWD Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [3] SWE_OV_FAULT

- Description: SWE Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [2] SWF_OV_FAULT

- Description: SWF Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [1] VIN_BULK_OV_FAULT

- Description: VIN_Bulk OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [0] RESERVED

- Description: Reserved
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0

## R153 (0x153) — SWA_UV_FAULT, SWB_UV_FAULT, SWC_UV_FAULT, SWD_UV_FAULT, SWE_UV_FAULT, SWF_UV_FAULT, CRITICAL_TEMP_FAULT

Title: R153 - 10th Fault Error Log | Region: Host Region | Source: JESD301-5 Table 220, p.217 | Encoding: same as 0x141 (spec: 'See encoding definition in 141[7:0]')

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | SWA_UV_FAULT | RON | 0 |
| 6 | SWB_UV_FAULT | RON | 0 |
| 5 | SWC_UV_FAULT | RON | 0 |
| 4 | SWD_UV_FAULT | RON | 0 |
| 3 | SWE_UV_FAULT | RON | 0 |
| 2 | SWF_UV_FAULT | RON | 0 |
| 1 | RESERVED | RON | 0 |
| 0 | CRITICAL_TEMP_FAULT | RON | 0 |

### [7] SWA_UV_FAULT

- Description: SWA Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [6] SWB_UV_FAULT

- Description: SWB Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [5] SWC_UV_FAULT

- Description: SWC Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [4] SWD_UV_FAULT

- Description: SWD Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [3] SWE_UV_FAULT

- Description: SWE Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [2] SWF_UV_FAULT

- Description: SWF Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [1] RESERVED

- Description: Reserved
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0

### [0] CRITICAL_TEMP_FAULT

- Description: Critical Temperature Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

## R154 (0x154) — SWA_OV_FAULT, SWB_OV_FAULT, SWC_OV_FAULT, SWD_OV_FAULT, SWE_OV_FAULT, SWF_OV_FAULT, VIN_BULK_OV_FAULT

Title: R154 - 11th Fault Error Log | Region: Host Region | Source: JESD301-5 Table 221, p.218 | Encoding: same as 0x140 (spec: 'See encoding definition in 140[7:0]')

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | SWA_OV_FAULT | RON | 0 |
| 6 | SWB_OV_FAULT | RON | 0 |
| 5 | SWC_OV_FAULT | RON | 0 |
| 4 | SWD_OV_FAULT | RON | 0 |
| 3 | SWE_OV_FAULT | RON | 0 |
| 2 | SWF_OV_FAULT | RON | 0 |
| 1 | VIN_BULK_OV_FAULT | RON | 0 |
| 0 | RESERVED | RON | 0 |

### [7] SWA_OV_FAULT

- Description: SWA Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [6] SWB_OV_FAULT

- Description: SWB Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [5] SWC_OV_FAULT

- Description: SWC Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [4] SWD_OV_FAULT

- Description: SWD Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [3] SWE_OV_FAULT

- Description: SWE Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [2] SWF_OV_FAULT

- Description: SWF Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [1] VIN_BULK_OV_FAULT

- Description: VIN_Bulk OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [0] RESERVED

- Description: Reserved
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0

## R155 (0x155) — SWA_UV_FAULT, SWB_UV_FAULT, SWC_UV_FAULT, SWD_UV_FAULT, SWE_UV_FAULT, SWF_UV_FAULT, CRITICAL_TEMP_FAULT

Title: R155 - 11th Fault Error Log | Region: Host Region | Source: JESD301-5 Table 222, p.218 | Encoding: same as 0x141 (spec: 'See encoding definition in 141[7:0]')

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | SWA_UV_FAULT | RON | 0 |
| 6 | SWB_UV_FAULT | RON | 0 |
| 5 | SWC_UV_FAULT | RON | 0 |
| 4 | SWD_UV_FAULT | RON | 0 |
| 3 | SWE_UV_FAULT | RON | 0 |
| 2 | SWF_UV_FAULT | RON | 0 |
| 1 | RESERVED | RON | 0 |
| 0 | CRITICAL_TEMP_FAULT | RON | 0 |

### [7] SWA_UV_FAULT

- Description: SWA Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [6] SWB_UV_FAULT

- Description: SWB Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [5] SWC_UV_FAULT

- Description: SWC Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [4] SWD_UV_FAULT

- Description: SWD Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [3] SWE_UV_FAULT

- Description: SWE Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [2] SWF_UV_FAULT

- Description: SWF Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [1] RESERVED

- Description: Reserved
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0

### [0] CRITICAL_TEMP_FAULT

- Description: Critical Temperature Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

## R156 (0x156) — SWA_OV_FAULT, SWB_OV_FAULT, SWC_OV_FAULT, SWD_OV_FAULT, SWE_OV_FAULT, SWF_OV_FAULT, VIN_BULK_OV_FAULT

Title: R156 - 12th Fault Error Log | Region: Host Region | Source: JESD301-5 Table 223, p.218 | Encoding: same as 0x140 (spec: 'See encoding definition in 140[7:0]')

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | SWA_OV_FAULT | RON | 0 |
| 6 | SWB_OV_FAULT | RON | 0 |
| 5 | SWC_OV_FAULT | RON | 0 |
| 4 | SWD_OV_FAULT | RON | 0 |
| 3 | SWE_OV_FAULT | RON | 0 |
| 2 | SWF_OV_FAULT | RON | 0 |
| 1 | VIN_BULK_OV_FAULT | RON | 0 |
| 0 | RESERVED | RON | 0 |

### [7] SWA_OV_FAULT

- Description: SWA Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [6] SWB_OV_FAULT

- Description: SWB Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [5] SWC_OV_FAULT

- Description: SWC Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [4] SWD_OV_FAULT

- Description: SWD Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [3] SWE_OV_FAULT

- Description: SWE Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [2] SWF_OV_FAULT

- Description: SWF Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [1] VIN_BULK_OV_FAULT

- Description: VIN_Bulk OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [0] RESERVED

- Description: Reserved
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0

## R157 (0x157) — SWA_UV_FAULT, SWB_UV_FAULT, SWC_UV_FAULT, SWD_UV_FAULT, SWE_UV_FAULT, SWF_UV_FAULT, CRITICAL_TEMP_FAULT

Title: R157 - 12th Fault Error Log | Region: Host Region | Source: JESD301-5 Table 224, p.218 | Encoding: same as 0x141 (spec: 'See encoding definition in 141[7:0]')

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | SWA_UV_FAULT | RON | 0 |
| 6 | SWB_UV_FAULT | RON | 0 |
| 5 | SWC_UV_FAULT | RON | 0 |
| 4 | SWD_UV_FAULT | RON | 0 |
| 3 | SWE_UV_FAULT | RON | 0 |
| 2 | SWF_UV_FAULT | RON | 0 |
| 1 | RESERVED | RON | 0 |
| 0 | CRITICAL_TEMP_FAULT | RON | 0 |

### [7] SWA_UV_FAULT

- Description: SWA Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [6] SWB_UV_FAULT

- Description: SWB Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [5] SWC_UV_FAULT

- Description: SWC Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [4] SWD_UV_FAULT

- Description: SWD Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [3] SWE_UV_FAULT

- Description: SWE Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [2] SWF_UV_FAULT

- Description: SWF Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [1] RESERVED

- Description: Reserved
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0

### [0] CRITICAL_TEMP_FAULT

- Description: Critical Temperature Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

## R158 (0x158) — SWA_OV_FAULT, SWB_OV_FAULT, SWC_OV_FAULT, SWD_OV_FAULT, SWE_OV_FAULT, SWF_OV_FAULT, VIN_BULK_OV_FAULT

Title: R158 - 13th Fault Error Log | Region: Host Region | Source: JESD301-5 Table 225, p.218 | Encoding: same as 0x140 (spec: 'See encoding definition in 140[7:0]')

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | SWA_OV_FAULT | RON | 0 |
| 6 | SWB_OV_FAULT | RON | 0 |
| 5 | SWC_OV_FAULT | RON | 0 |
| 4 | SWD_OV_FAULT | RON | 0 |
| 3 | SWE_OV_FAULT | RON | 0 |
| 2 | SWF_OV_FAULT | RON | 0 |
| 1 | VIN_BULK_OV_FAULT | RON | 0 |
| 0 | RESERVED | RON | 0 |

### [7] SWA_OV_FAULT

- Description: SWA Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [6] SWB_OV_FAULT

- Description: SWB Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [5] SWC_OV_FAULT

- Description: SWC Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [4] SWD_OV_FAULT

- Description: SWD Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [3] SWE_OV_FAULT

- Description: SWE Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [2] SWF_OV_FAULT

- Description: SWF Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [1] VIN_BULK_OV_FAULT

- Description: VIN_Bulk OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [0] RESERVED

- Description: Reserved
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0

## R159 (0x159) — SWA_UV_FAULT, SWB_UV_FAULT, SWC_UV_FAULT, SWD_UV_FAULT, SWE_UV_FAULT, SWF_UV_FAULT, CRITICAL_TEMP_FAULT

Title: R159 - 13th Fault Error Log | Region: Host Region | Source: JESD301-5 Table 226, p.218 | Encoding: same as 0x141 (spec: 'See encoding definition in 141[7:0]')

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | SWA_UV_FAULT | RON | 0 |
| 6 | SWB_UV_FAULT | RON | 0 |
| 5 | SWC_UV_FAULT | RON | 0 |
| 4 | SWD_UV_FAULT | RON | 0 |
| 3 | SWE_UV_FAULT | RON | 0 |
| 2 | SWF_UV_FAULT | RON | 0 |
| 1 | RESERVED | RON | 0 |
| 0 | CRITICAL_TEMP_FAULT | RON | 0 |

### [7] SWA_UV_FAULT

- Description: SWA Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [6] SWB_UV_FAULT

- Description: SWB Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [5] SWC_UV_FAULT

- Description: SWC Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [4] SWD_UV_FAULT

- Description: SWD Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [3] SWE_UV_FAULT

- Description: SWE Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [2] SWF_UV_FAULT

- Description: SWF Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [1] RESERVED

- Description: Reserved
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0

### [0] CRITICAL_TEMP_FAULT

- Description: Critical Temperature Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

## R15A (0x15A) — SWA_OV_FAULT, SWB_OV_FAULT, SWC_OV_FAULT, SWD_OV_FAULT, SWE_OV_FAULT, SWF_OV_FAULT, VIN_BULK_OV_FAULT

Title: R15A - 14th Fault Error Log | Region: Host Region | Source: JESD301-5 Table 227, p.219 | Encoding: same as 0x140 (spec: 'See encoding definition in 140[7:0]')

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | SWA_OV_FAULT | RON | 0 |
| 6 | SWB_OV_FAULT | RON | 0 |
| 5 | SWC_OV_FAULT | RON | 0 |
| 4 | SWD_OV_FAULT | RON | 0 |
| 3 | SWE_OV_FAULT | RON | 0 |
| 2 | SWF_OV_FAULT | RON | 0 |
| 1 | VIN_BULK_OV_FAULT | RON | 0 |
| 0 | RESERVED | RON | 0 |

### [7] SWA_OV_FAULT

- Description: SWA Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [6] SWB_OV_FAULT

- Description: SWB Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [5] SWC_OV_FAULT

- Description: SWC Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [4] SWD_OV_FAULT

- Description: SWD Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [3] SWE_OV_FAULT

- Description: SWE Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [2] SWF_OV_FAULT

- Description: SWF Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [1] VIN_BULK_OV_FAULT

- Description: VIN_Bulk OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [0] RESERVED

- Description: Reserved
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0

## R15B (0x15B) — SWA_UV_FAULT, SWB_UV_FAULT, SWC_UV_FAULT, SWD_UV_FAULT, SWE_UV_FAULT, SWF_UV_FAULT, CRITICAL_TEMP_FAULT

Title: R15B - 14th Fault Error Log | Region: Host Region | Source: JESD301-5 Table 228, p.219 | Encoding: same as 0x141 (spec: 'See encoding definition in 141[7:0]')

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | SWA_UV_FAULT | RON | 0 |
| 6 | SWB_UV_FAULT | RON | 0 |
| 5 | SWC_UV_FAULT | RON | 0 |
| 4 | SWD_UV_FAULT | RON | 0 |
| 3 | SWE_UV_FAULT | RON | 0 |
| 2 | SWF_UV_FAULT | RON | 0 |
| 1 | RESERVED | RON | 0 |
| 0 | CRITICAL_TEMP_FAULT | RON | 0 |

### [7] SWA_UV_FAULT

- Description: SWA Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [6] SWB_UV_FAULT

- Description: SWB Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [5] SWC_UV_FAULT

- Description: SWC Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [4] SWD_UV_FAULT

- Description: SWD Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [3] SWE_UV_FAULT

- Description: SWE Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [2] SWF_UV_FAULT

- Description: SWF Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [1] RESERVED

- Description: Reserved
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0

### [0] CRITICAL_TEMP_FAULT

- Description: Critical Temperature Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

## R15C (0x15C) — SWA_OV_FAULT, SWB_OV_FAULT, SWC_OV_FAULT, SWD_OV_FAULT, SWE_OV_FAULT, SWF_OV_FAULT, VIN_BULK_OV_FAULT

Title: R15C - 15th Fault Error Log | Region: Host Region | Source: JESD301-5 Table 229, p.219 | Encoding: same as 0x140 (spec: 'See encoding definition in 140[7:0]')

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | SWA_OV_FAULT | RON | 0 |
| 6 | SWB_OV_FAULT | RON | 0 |
| 5 | SWC_OV_FAULT | RON | 0 |
| 4 | SWD_OV_FAULT | RON | 0 |
| 3 | SWE_OV_FAULT | RON | 0 |
| 2 | SWF_OV_FAULT | RON | 0 |
| 1 | VIN_BULK_OV_FAULT | RON | 0 |
| 0 | RESERVED | RON | 0 |

### [7] SWA_OV_FAULT

- Description: SWA Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [6] SWB_OV_FAULT

- Description: SWB Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [5] SWC_OV_FAULT

- Description: SWC Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [4] SWD_OV_FAULT

- Description: SWD Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [3] SWE_OV_FAULT

- Description: SWE Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [2] SWF_OV_FAULT

- Description: SWF Buck Regulator OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [1] VIN_BULK_OV_FAULT

- Description: VIN_Bulk OV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [0] RESERVED

- Description: Reserved
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0

## R15D (0x15D) — SWA_UV_FAULT, SWB_UV_FAULT, SWC_UV_FAULT, SWD_UV_FAULT, SWE_UV_FAULT, SWF_UV_FAULT, CRITICAL_TEMP_FAULT

Title: R15D - 15th Fault Error Log | Region: Host Region | Source: JESD301-5 Table 230, p.219 | Encoding: same as 0x141 (spec: 'See encoding definition in 141[7:0]')

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | SWA_UV_FAULT | RON | 0 |
| 6 | SWB_UV_FAULT | RON | 0 |
| 5 | SWC_UV_FAULT | RON | 0 |
| 4 | SWD_UV_FAULT | RON | 0 |
| 3 | SWE_UV_FAULT | RON | 0 |
| 2 | SWF_UV_FAULT | RON | 0 |
| 1 | RESERVED | RON | 0 |
| 0 | CRITICAL_TEMP_FAULT | RON | 0 |

### [7] SWA_UV_FAULT

- Description: SWA Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [6] SWB_UV_FAULT

- Description: SWB Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [5] SWC_UV_FAULT

- Description: SWC Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [4] SWD_UV_FAULT

- Description: SWD Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [3] SWE_UV_FAULT

- Description: SWE Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [2] SWF_UV_FAULT

- Description: SWF Buck Regulator UV Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |

### [1] RESERVED

- Description: Reserved
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0

### [0] CRITICAL_TEMP_FAULT

- Description: Critical Temperature Fault
- Attribute: RON — Read Only (writes have no effect); Persistent across power cycle, not erasable by command
- Default: 0 → No Fault

| Code (bin) | Meaning |
|---|---|
| 0 | No Fault |
| 1 | Fault |
