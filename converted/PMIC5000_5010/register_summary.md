# PMIC5000/PMIC5010 Register Map Summary

Source: JESD301-1A.03 — PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5 (February 2025). Application: server (DDR5 RDIMM, DDR5 LRDIMM).

Elided ranges ('...') follow the linear pattern of the neighbouring codes; see registers/<addr>.md for every value spelled out.

## R04 (0x04) — GLOBAL_ERROR_COUNT, GLOBAL_ERROR_LOG_BUCK_OV_OR_UV, GLOBAL_ERROR_LOG_VIN_BULK_OVER_VOLTAGE, GLOBAL_ERROR_LOG_CRITICAL_TEMPERATURE

Region: Host Region | Source: JESD301-1A.03 Table 94, p.112

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | GLOBAL_ERROR_COUNT | ROE | 0 |
| 6 | GLOBAL_ERROR_LOG_BUCK_OV_OR_UV | ROE | 0 |
| 5 | GLOBAL_ERROR_LOG_VIN_BULK_OVER_VOLTAGE | ROE | 0 |
| 4 | GLOBAL_ERROR_LOG_CRITICAL_TEMPERATURE | ROE | 0 |
| 3:0 | RESERVED | RV | 0 |

### [7] GLOBAL_ERROR_COUNT

- Description: Global Error Count Since Last Erase Operation[3]
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0 → No Error or Only 1 Error since last Erase operation

| Code (bin) | Meaning |
|---|---|
| 0 | No Error or Only 1 Error since last Erase operation |
| 1 | > 1 Error Count since last Erase operation |

### [6] GLOBAL_ERROR_LOG_BUCK_OV_OR_UV

- Description: Global Error Log History for Buck Regulator Output Over or Under Voltage[4]
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0 → No Error Occurred

| Code (bin) | Meaning |
|---|---|
| 0 | No Error Occurred |
| 1 | Error Occurred |

### [5] GLOBAL_ERROR_LOG_VIN_BULK_OVER_VOLTAGE

- Description: Global Error Log History for VIN_Bulk Over Voltage[4]
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0 → No Error Occurred

| Code (bin) | Meaning |
|---|---|
| 0 | No Error Occurred |
| 1 | Error Occurred |

### [4] GLOBAL_ERROR_LOG_CRITICAL_TEMPERATURE

- Description: Global Error Log History for Critical Temperature[4]
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0 → No Error Occurred

| Code (bin) | Meaning |
|---|---|
| 0 | No Error Occurred |
| 1 | Error Occurred |

### [3:0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

**Notes**

- NOTE 1: The PMIC always attempts to write this register into its non-volatile memory. However, it may not be guaranteed depending on how fast the host may shut off the input power to the PMIC. The PMIC needs minimum of 5.0 V for VIN_Bulk voltage and 200 ms duration from PWR_GOOD signal assertion to guarantee the write operation into non-volatile memory.
- NOTE 2: Host must explicitly perform Erase operation to erase this entire register Table 94, “Register 0x04” [7:0] via Table 146, “Register 0x39”. The PMIC needs minimum of 200 ms for Erase operation.
- NOTE 3: PMIC counts the error since last erase operation and if more than one error occurs, it sets this bit to ‘1’. Host must explicitly perform Erase operation to erase this entire register Table 94, “Register 0x04” [7:0].
- NOTE 4: PMIC sets the bit when error occurs.

## R05 (0x05) — SWA_POWER_GOOD, SWB_POWER_GOOD, SWC_POWER_GOOD, SWD_POWER_GOOD, PMIC_ERROR_LOG

Region: Host Region | Source: JESD301-1A.03 Table 95, p.113

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

- Description: PMIC Power On - SWA Power Not Good[3]
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0 → Normal Power On

| Code (bin) | Meaning |
|---|---|
| 0 | Normal Power On |
| 1 | SWA Power Not Good |

### [5] SWB_POWER_GOOD

- Description: PMIC Power On - SWB Power Not Good[3],[4]
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
| 010 | Buck Regulator Output Over or Under Voltage[5] |
| 011 | Critical Temperature |
| 100 | VIN_Bulk Input Over Voltage |
| 101 | Reserved |
| 110 | Reserved |
| 111 | Reserved |

**Notes**

- NOTE 1: The PMIC always attempts to write this register into its non-volatile memory. However, it may not be guaranteed depending on how fast the host may shut off the input power to the PMIC. The PMIC needs minimum of 5.0 V for VIN_Bulk voltage and 200 ms duration from PWR_GOOD signal assertion to guarantee the write operation into non-volatile memory.
- NOTE 2: This entire register status reflects previous power down cycle of the PMIC and is updated by the PMIC on its own at each power cycle, if update is needed. Because this register is updated only if there is an update needed, there is no NVM life time impact. This register is cleared when host issues the erase command via Table 146, “Register 0x39”. The PMIC needs minimum of 200 ms for Erase operation.
- NOTE 3: This register is set only if PMIC generates internal VR Disable command due to fault condition.
- NOTE 4: Only applicable if Table 166, “Register 0x4F” [0] = ‘0’.
- NOTE 5: This code is a logical OR function of Table 96, “Register 0x06” [7:0] register bits.

## R06 (0x06) — SWA_UNDER_VOLTAGE_LOCKOUT, SWB_UNDER_VOLTAGE_LOCKOUT, SWC_UNDER_VOLTAGE_LOCKOUT, SWD_UNDER_VOLTAGE_LOCKOUT, SWA_OVER_VOLTAGE, SWB_OVER_VOLTAGE, SWC_OVER_VOLTAGE, SWD_OVER_VOLTAGE

Region: Host Region | Source: JESD301-1A.03 Table 96, p.114

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

- Description: PMIC Power On - SWB Under Voltage Lockout[3]
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

- NOTE 1: The PMIC always attempts to write this register into its non-volatile memory. However, it may not be guaranteed depending on how fast the host may shut off the input power to the PMIC. The PMIC needs minimum of 5.0 V for VIN_Bulk voltage and 200 ms duration from PWR_GOOD signal assertion to guarantee the write operation into non-volatile memory.
- NOTE 2: This entire register status reflects previous power down cycle of the PMIC and is updated by the PMIC on its own at each power cycle, if update is needed. Because this register is updated only if there is an update needed, there is no NVM life time impact. This register is cleared when host issues the erase command via Table 146, “Register 0x39”. The PMIC needs minimum of 200 ms for Erase operation.
- NOTE 3: Only applicable if Table 166, “Register 0x4F” [0] = ‘0’.

## R07 (0x07) — Reserved

Region: Host Region | Source: JESD301-1A.03 Table 97, p.115

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | RESERVED | ROE | 0 |

### [7:0] RESERVED

- Description: Reserved
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0

**Notes**

- NOTE 1: The PMIC always attempts to write this register into its non-volatile memory. However, it may not be guaranteed depending on how fast the host may shut off the input power to the PMIC. The PMIC needs minimum of 5.0V for VIN_Bulk voltage and 200 ms duration from PWR_GOOD signal assertion to guarantee the write operation into non-volatile memory.
- NOTE 2: This entire register status reflects previous power down cycle of the PMIC and is updated by the PMIC on its own at each power cycle, if update is needed. Because this register is updated only if there is an update needed, there is no NVM life time impact. This register is cleared when host issues the erase command via Table 146, “Register 0x39”. The PMIC needs minimum of 200 ms for Erase operation.

## R08 (0x08) — VIN_BULK_INPUT_POWER_GOOD_STATUS, CRITICAL_TEMP_SHUTDOWN_STATUS, SWA_OUTPUT_POWER_GOOD_STATUS, SWB_OUTPUT_POWER_GOOD_STATUS, SWC_OUTPUT_POWER_GOOD_STATUS, SWD_OUTPUT_POWER_GOOD_STATUS, VIN_MGMT_INPUT_OVER_VOLTAGE_STATUS, VIN_BULK_INPUT_OVER_VOLTAGE_STATUS

Region: Host Region | Source: JESD301-1A.03 Table 98, p.116

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

- NOTE 1: This register is set when VIN_Bulk input goes below the threshold setting in register Table 116, “Register 0x1A” [7:5].
- NOTE 2: This register is set when PMIC temperature goes above the threshold setting in register Table 136, “Register 0x2E” [2:0].
- NOTE 3: This register is set when SWA output voltage goes either below the threshold setting in register Table 123, “Register 0x21”[1:0] or above the threshold setting in register Table 124, “Register 0x22” [7:6].
- NOTE 4: Only applicable if Table 166, “Register 0x4F” [0] = ‘0’. This register is set when SWB output goes either below the threshold setting in register Table 125, “Register 0x23”[1:0] or above the threshold setting in register Table 126, “Register 0x24” [7:6].
- NOTE 5: This register is set when SWC output goes either below the threshold setting in register Table 127, “Register 0x25”[1:0] or above the threshold setting in register Table 128, “Register 0x26” [7:6].
- NOTE 6: This register is set when SWD output goes either below the threshold setting in register Table 129, “Register 0x27”[1:0] or above the threshold setting in register Table 130, “Register 0x28” [7:6].
- NOTE 7: This register is set when VIN_Mgmt input voltage goes above the threshold setting in register Table 117, “Register 0x1B” [5].
- NOTE 8: This register is set when VIN_Bulk input voltage goes above the threshold setting in register Table 117, “Register 0x1B” [7].

## R09 (0x09) — PMIC_HIGH_TEMP_WARNING_STATUS, VBIAS_POWER_GOOD_STATUS, VOUT_1.8V_OUTPUT_POWER_GOOD_STATUS, VIN_MGMT_TO_VIN_BULK_INPUT_SUPPLY_SWITCHOVER_STATUS, SWA_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS, SWB_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS, SWC_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS, SWD_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS

Region: Host Region | Source: JESD301-1A.03 Table 99, p.117

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

- Description: VBias Power Good Status[2]
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

- NOTE 1: This register is set when PMIC temperature goes above the threshold setting in Table 117, “Register 0x1B” [2:0].
- NOTE 2: This register is set when VBias voltage goes below the threshold setting in register Table 116, “Register 0x1A” [3].
- NOTE 3: This register is set when VOUT_1.8V output goes below the threshold setting in register Table 116, “Register 0x1A” [2].
- NOTE 4: This register is set when VIN_Mgmt input supply goes below the threshold setting in register Table 137, “Register 0x2F” [7].
- NOTE 5: This register is set when SWA output current consumption goes above the threshold setting in Table 118, “Register 0x1C” [7:2].
- NOTE 6: This register is set when SWB output current consumption goes above the threshold setting in Table 119, “Register 0x1D” [7:2]. If Table 166, “Register 0x4F” [0] = ‘1’, the setting in Table 119, “Register 0x1D” [7:2] must be identical as Table 118, “Register 0x1C” [7:2].
- NOTE 7: This register is applicable regardless of the setting in Table 166, “Register 0x4F” [0]
- NOTE 8: This register is set when SWC output current consumption goes above the threshold setting in Table 120, “Register 0x1E” [7:2].
- NOTE 9: This register is set when SWD output current consumption goes above the threshold setting in Table 121, “Register 0x1F” [7:2].

## R0A (0x0A) — SWA_OUTPUT_OVER_VOLTAGE_STATUS, SWB_OUTPUT_OVER_VOLTAGE_STATUS, SWC_OUTPUT_OVER_VOLTAGE_STATUS, SWD_OUTPUT_OVER_VOLTAGE_STATUS, PEC_ERROR_STATUS, PARITY_ERROR_STATUS, IBI_AND_GLOBAL_STATUS

Region: Host Region | Source: JESD301-1A.03 Table 100, p.118

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

- Description: T Bit Parity Error Status[6],[7]
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

- NOTE 1: This register is set when SWA output voltage goes above the threshold setting in Table 124, “Register 0x22” [5:4].
- NOTE 2: Only applicable if Table 166, “Register 0x4F” [0] = ‘0’. This register is set when SWB output voltage goes above the threshold setting in Table 126, “Register 0x24” [5:4]. If Table 166, “Register 0x4F” [0] = ‘1’, the setting in Table 126, “Register 0x24” [5:4] must be identical to Table 124, “Register 0x22” [5:4].
- NOTE 3: This register is set when SWC output voltage goes above the threshold setting in Table 128, “Register 0x26” [5:4]
- NOTE 4: This register is set when SWD output voltage goes above the threshold setting in Table 130, “Register 0x28” [5:4]
- NOTE 5: Applicable in I3C Basic Mode Only and if enabled in register Table 142, “Register 0x34” [7].
- NOTE 6: This register is updated when PMIC device goes through bus reset as described in clause 2.10.15.
- NOTE 7: Applicable in I3C Basic Mode and if enabled in register Table 142, “Register 0x34” [5]. Also applicable in I2C mode for supported CCC.
- NOTE 8: This register can be used as Global Status in addition to IBI status. When IBI function is enabled, this register is automatically cleared when PMIC transmits IBI payload; however individual status registers still require an explicit clear command from host.

## R0B (0x0B) — SWA_OUTPUT_CURRENT_LIMITER_WARNING_STATUS, SWB_OUTPUT_CURRENT_LIMITER_WARNING_STATUS, SWC_OUTPUT_CURRENT_LIMITER_WARNING_STATUS, SWD_OUTPUT_CURRENT_LIMITER_WARNING_STATUS, SWA_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS, SWB_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS, SWC_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS, SWD_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

Region: Host Region | Source: JESD301-1A.03 Table 101, p.119

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

- Description: Switch Node C Output Current Limiter Warning Status[3]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No Current Limiter Event

| Code (bin) | Meaning |
|---|---|
| 0 | No Current Limiter Event |
| 1 | Current Limiter Event |

### [4] SWD_OUTPUT_CURRENT_LIMITER_WARNING_STATUS

- Description: Switch Node D Output Current Limiter Warning Status[4]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No Current Limiter Event

| Code (bin) | Meaning |
|---|---|
| 0 | No Current Limiter Event |
| 1 | Current Limiter Event |

### [3] SWA_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

- Description: Switch Node A Output Under Voltage Lockout Status[5]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No Under Voltage Lockout

| Code (bin) | Meaning |
|---|---|
| 0 | No Under Voltage Lockout |
| 1 | Under Voltage Lockout |

### [2] SWB_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

- Description: Switch Node B Output Under Voltage Lockout Status[6]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No Under Voltage Lockout

| Code (bin) | Meaning |
|---|---|
| 0 | No Under Voltage Lockout |
| 1 | Under Voltage Lockout |

### [1] SWC_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

- Description: Switch Node C Output Under Voltage Lockout Status[7]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No Under Voltage Lockout

| Code (bin) | Meaning |
|---|---|
| 0 | No Under Voltage Lockout |
| 1 | Under Voltage Lockout |

### [0] SWD_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

- Description: Switch Node D Output Under Voltage Lockout Status[8]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No Under Voltage Lockout

| Code (bin) | Meaning |
|---|---|
| 0 | No Under Voltage Lockout |
| 1 | Under Voltage Lockout |

**Notes**

- NOTE 1: This register is set when SWA output current goes above the threshold setting in Table 122, “Register 0x20” [7:6].
- NOTE 2: This register is applicable regardless of the setting in Table 166, “Register 0x4F” [0]. This register is set when SWB output current goes above the threshold setting in Table 123, “Register 0x21” [5:4]. If Table 166, “Register 0x4F” [0] = ‘1’, the setting in Table 122, “Register 0x20” [5:4] must be identical as Table 122, “Register 0x20” [7:6].
- NOTE 3: This register is set when SWC output current goes above the threshold setting in Table 122, “Register 0x20” [3:2].
- NOTE 4: This register is set when SWD output current goes above the threshold setting in Table 122, “Register 0x20” [1:0].
- NOTE 5: This register is set when SWA output voltage goes below the threshold setting in Table 122, “Register 0x20” [3:2].
- NOTE 6: Only applicable if Table 166, “Register 0x4F” [0] = ‘0’. This register is set when SWB output voltage goes below the threshold setting in Table 126, “Register 0x24” [3:2]. If Table 166, “Register 0x4F” [0] = ‘1’, the setting in Table 126, “Register 0x24” [3:2] must be identical as Table 124, “Register 0x22” [3:2].
- NOTE 7: This register is set when SWC output voltage goes below the threshold setting in Table 128, “Register 0x26” [3:2].
- NOTE 8: This register is set when SWD output voltage goes below the threshold setting in Table 130, “Register 0x28” [3:2].

## R0C (0x0C) — SWA_OUTPUT_CURRENT_POWER_MEASUREMENT

Region: Host Region | Source: JESD301-1A.03 Table 102, p.120

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SWA_OUTPUT_CURRENT_POWER_MEASUREMENT | RO | 0 |

### [7:0] SWA_OUTPUT_CURRENT_POWER_MEASUREMENT

- Description: All other encodings are reserved
- Attribute: RO — Read Only (writes have no effect)
- Default: 0

**When: If Table 116, “Register 0x1A”[1] = ‘0’ — Switch Node A Output Current or — Output Power[2] Measurement[3]**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | 0.125 A or 125 mW |
| 00000010 | 0x02 | 0.25 A or 250 mW |
| 00000011 | 0x03 | 0.375 A or 375 mW |
| 00000100 | 0x04 | 0.5 A or 500 mW |
| 00000101 | 0x05 | 0.625 A or 625 mW |
| 00000110 | 0x06 | 0.75 A or 750 mW |
| 00000111 | 0x07 | 0.875 A or 875 mW |
| 00001000 | 0x08 | 1.0 A or 1000 mW |
| 00001001 | 0x09 | 1.125 A or 1125 mW |
| ... | ... | ... |
| 00110111 | 0x37 | 6.875 A or 6875 mW |
| 00111000 | 0x38 | 7.0 A or 7000 mW |
| 00111001 | 0x39 | 7.125 A or 7125 mW |
| 00111010 | 0x3A | 7.25 A or 7250 mW |
| 00111011 | 0x3B | 7.375 A or 7375 mW |
| 00111100 | 0x3C | 7.5 A or 7500 mW |
| 00111101 | 0x3D | 7.625 A or 7625 mW |
| 00111110 | 0x3E | 7.75 A or 7750 mW |
| 00111111 | 0x3F | ≥ 7.875 A or 7875 mW |

**When: If Table 116, “Register 0x1A”[1] = ‘1’ — Sum of SWA, SWB, SWC and SWD — Output Power[4]**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | 125 mW |
| 00000010 | 0x02 | 250 mW |
| 00000011 | 0x03 | 375 mW |
| 00000100 | 0x04 | 500 mW |
| ... | ... | ... |
| 11111100 | 0xFC | 31500 mW |
| 11111101 | 0xFD | 31625 mW |
| 11111110 | 0xFE | 31750 mW |
| 11111111 | 0xFF | ≥ 31875 mW |

**Notes**

- NOTE 1: The PMIC reports current or power measurement as long as there is no output over voltage or output under voltage lockout event that triggers the VR Disable command. If PMIC triggers VR Disable command, PMIC does not report current or power measurement and register content may have stale data. For all other events that causes PMIC’s power good status as Not Good, the PMIC continues to provide current or power measurement.
- NOTE 2: If Table 117, “Register 0x1B” [6] = ‘0’, the PMIC reports current measurement. If Table 117, “Register 0x1B” [6] = ‘1’, the PMIC reports power measurement.
- NOTE 3: If Table 166, “Register 0x4F” [0] = ‘1’, host adds the current or power reported in Table 102, “Register 0x0C” [7:0] and Table 103, “Register 0x0D” [5:0] for total current or power consumption.
- NOTE 4: Register Table 117, “Register 0x1B” [6] must be configured as ‘1’.

## R0D (0x0D) — SWB_OUTPUT_CURRENT_POWER_MEASUREMENT

Region: Host Region | Source: JESD301-1A.03 Table 103, p.121

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | RESERVED | RV | 0 |
| 5:0 | SWB_OUTPUT_CURRENT_POWER_MEASUREMENT | RO | 0 |

### [7:6] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [5:0] SWB_OUTPUT_CURRENT_POWER_MEASUREMENT

- Description: Switch Node B Output Current or Output Power[2] Measurement[3]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 000000 | 0x00 | Un-defined |
| 000001 | 0x01 | 0.125 A or 125 mW |
| 000010 | 0x02 | 0.25 A or 250 mW |
| 000011 | 0x03 | 0.375 A or 375 mW |
| 000100 | 0x04 | 0.5 A or 500 mW |
| 000101 | 0x05 | 0.625 A or 625 mW |
| 000110 | 0x06 | 0.75 A or 750 mW |
| 000111 | 0x07 | 0.875 A or 875 mW |
| 001000 | 0x08 | 1.0 A or 1000 mW |
| 001001 | 0x09 | 1.125 A or 1125 mW |
| ... | ... | ... |
| 110111 | 0x37 | 6.875 A or 6875 mW |
| 111000 | 0x38 | 7.0 A or 7000 mW |
| 111001 | 0x39 | 7.125 A or 7125 mW |
| 111010 | 0x3A | 7.25 A or 7250 mW |
| 111011 | 0x3B | 7.375 A or 7375 mW |
| 111100 | 0x3C | 7.5 A or 7500 mW |
| 111101 | 0x3D | 7.625 A or 7625 mW |
| 111110 | 0x3E | 7.75 A or 7750 mW |
| 111111 | 0x3F | ≥ 7.875 A or 7875 mW |

**Notes**

- NOTE 1: The PMIC reports current or power measurement as long as there is no output over voltage or output under voltage lockout event that triggers the VR Disable command. If PMIC triggers VR Disable command, PMIC does not report current or power measurement and register content may have stale data. For all other events that causes PMIC’s power good status as Not Good, the PMIC continues to provide current or power measurement.
- NOTE 2: If Table 117, “Register 0x1B” [6] = ‘0’, the PMIC reports current measurement. If Table 117, “Register 0x1B” [6] = ‘1’, the PMIC reports power measurement.
- NOTE 3: If Table 166, “Register 0x4F” [0] = ‘1’, host adds the current or power reported in Table 102, “Register 0x0C” [7:0] and Table 103, “Register 0x0D” [5:0] for total current or power consumption.

## R0E (0x0E) — SWC_OUTPUT_CURRENT_POWER_MEASUREMENT

Region: Host Region | Source: JESD301-1A.03 Table 104, p.122

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | RESERVED | RV | 0 |
| 5:0 | SWC_OUTPUT_CURRENT_POWER_MEASUREMENT | RO | 0 |

### [7:6] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [5:0] SWC_OUTPUT_CURRENT_POWER_MEASUREMENT

- Description: Switch Node C Output Current or Output Power[2] Measurement
- Attribute: RO — Read Only (writes have no effect)
- Default: 0

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 000000 | 0x00 | Un-defined |
| 000001 | 0x01 | 0.125 A or 125 mW |
| 000010 | 0x02 | 0.25 A or 250 mW |
| 000011 | 0x03 | 0.375 A or 375 mW |
| 000100 | 0x04 | 0.5 A or 500 mW |
| 000101 | 0x05 | 0.625 A or 625 mW |
| 000110 | 0x06 | 0.75 A or 750 mW |
| 000111 | 0x07 | 0.875 A or 875 mW |
| 001000 | 0x08 | 1.0 A or 1000 mW |
| 001001 | 0x09 | 1.125 A or 1125 mW |
| 001010 | 0x0A | 1.25 A or 1250 mW |
| ... | ... | ... |
| 110111 | 0x37 | 6.875 A or 6875 mW |
| 111000 | 0x38 | 7.0 A or 7000 mW |
| 111001 | 0x39 | 7.125 A or 7125 mW |
| 111010 | 0x3A | 7.25 A or 7250 mW |
| 111011 | 0x3B | 7.375 A or 7375 mW |
| 111100 | 0x3C | 7.5 A or 7500 mW |
| 111101 | 0x3D | 7.625 A or 7625 mW |
| 111110 | 0x3E | 7.75 A or 7750 mW |
| 111111 | 0x3F | ≥ 7.875 A or 7875 mW |

**Notes**

- NOTE 1: The PMIC reports current or power measurement as long as there is no output over voltage or output under voltage lockout event that triggers the VR Disable command. If PMIC triggers VR Disable command, PMIC does not report current or power measurement and register content may have stale data. For all other events that causes PMIC’s power good status as Not Good, the PMIC continues to provide current or power measurement.
- NOTE 2: If Table 117, “Register 0x1B” [6] = ‘0’, the PMIC reports current measurement. If Table 117, “Register 0x1B” [6] = ‘1’, the PMIC reports power measurement.

## R0F (0x0F) — SWD_OUTPUT_CURRENT_POWER_MEASUREMENT

Region: Host Region | Source: JESD301-1A.03 Table 105, p.123

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | RESERVED | RV | 0 |
| 5:0 | SWD_OUTPUT_CURRENT_POWER_MEASUREMENT | RO | 0 |

### [7:6] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [5:0] SWD_OUTPUT_CURRENT_POWER_MEASUREMENT

- Description: Switch Node D Output Current or Output Power[2] Measurement
- Attribute: RO — Read Only (writes have no effect)
- Default: 0

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 000000 | 0x00 | Un-defined |
| 000001 | 0x01 | 0.125 A or 125 mW |
| 000010 | 0x02 | 0.25 A or 250 mW |
| 000011 | 0x03 | 0.375 A or 375 mW |
| 000100 | 0x04 | 0.5 A or 500 mW |
| 000101 | 0x05 | 0.625 A or 625 mW |
| 000110 | 0x06 | 0.75 A or 750 mW |
| 000111 | 0x07 | 0.875 A or 875 mW |
| 001000 | 0x08 | 1.0 A or 1000 mW |
| 001001 | 0x09 | 1.125 A or 1125 mW |
| ... | ... | ... |
| 110111 | 0x37 | 6.875 A or 6875 mW |
| 111000 | 0x38 | 7.0 A or 7000 mW |
| 111001 | 0x39 | 7.125 A or 7125 mW |
| 111010 | 0x3A | 7.25 A or 7250 mW |
| 111011 | 0x3B | 7.375 A or 7375 mW |
| 111100 | 0x3C | 7.5 A or 7500 mW |
| 111101 | 0x3D | 7.625 A or 7625 mW |
| 111110 | 0x3E | 7.75 A or 7750 mW |
| 111111 | 0x3F | ≥ 7.875 A or 7875 mW |

**Notes**

- NOTE 1: The PMIC reports current or power measurement as long as there is no output over voltage or output under voltage lockout event that triggers the VR Disable command. If PMIC triggers VR Disable command, PMIC does not report current or power measurement and register content may have stale data. For all other events that causes PMIC’s power good status as Not Good, the PMIC continues to provide current or power measurement.
- NOTE 2: If Table 117, “Register 0x1B” [6] = ‘0’, the PMIC reports current measurement. If Table 117, “Register 0x1B” [6] = ‘1’, the PMIC reports power measurement. For each Real Time Status Registers (Table 98, “Register 0x08” [7:0], Table 99, “Register 0x09” [7:0], Table 100, “Register 0x0A” [7:1], Table 101, “Register 0x0B” [7:0] and Table 141, “Register 0x33” [4:2]), the PMIC offers a way to clear the status of each event. The clear registers are Table 106, “Register 0x10” [7,5:0], Table 107, “Register 0x11” [7:0], Table 108, “Register 0x12” [7:2], Table 109, “Register 0x13” [7:0] and to Table 110, “Register 0x14” [4:2,0], respectively. All clear registers are Write ‘1’ only registers. When ‘1’ is written to any of the clear registers, the PMIC updates the status registers to default state and removes the interrupt condition on GSI_n and PWR_GOOD output signal assuming that event is no longer present. If the failing condition is still present, the status register will still remain at ‘1’. Note that GSI_n and PWR_GOOD interrupt is only applicable if that event is not masked. GSI_n output signal can be disabled. When ‘1’ is written to any of the clear registers, there are three categories of response by the PMIC. 1.  PMIC removes GSI_n interrupt (PWR_GOOD interrupt is not applicable. Related status registers are: Table 106, “Register 0x10” [1], Table 107, “Register 0x11” [7,4:0], Table 109, “Register 0x13” [7:4], Table 110, “Register 0x14” [4]. 2. PMIC removes GSI_n and PWR_GOOD interrupt. Related status registers are: Table 106, “Register 0x10” [7,5:2], Table 107, “Register 0x11” [6:5], Table 110, “Register 0x14” [2]. 3. PMIC only removes GSI_n interrupt and does not remove PWR_GOOD interrupt. Related status registers are: Table 106, “Register 0x10” [0], Table 108, “Register 0x12” [7:4], Table 109, “Register 0x13” [3:0], Table 110, “Register 0x14” [3]. The host is expected to either power cycle the PMIC or re-issue the VR Enable command if PMIC is in non write protect mode. The PMIC offers a Global Clear command by writing ‘1’ to registers Table 110, “Register 0x14” [0]. This command works same way as individual clear command. This command can alternatively be used by the host if more than one clear command is required to different registers.

## R10 (0x10) — CLEAR_VIN_BULK_INPUT_POWER_GOOD_STATUS, CLEAR_SWA_OUTPUT_POWER_GOOD_STATUS, CLEAR_SWB_OUTPUT_POWER_GOOD_STATUS, CLEAR_SWC_OUTPUT_POWER_GOOD_STATUS, CLEAR_SWD_OUTPUT_POWER_GOOD_STATUS, CLEAR_VIN_MGMT_INPUT_OVER_VOLTAGE_STATUS, CLEAR_VIN_BULK_INPUT_OVER_VOLTAGE_STATUS

Region: Host Region | Source: JESD301-1A.03 Table 106, p.124

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
| 1 | Clear Register Table 98, “Register 0x08” [7][2] |

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
| 1 | Clear Register Table 98, “Register 0x08” [5][2] |

### [4] CLEAR_SWB_OUTPUT_POWER_GOOD_STATUS

- Description: Clear SWB Output Power Good Status.[3]
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 98, “Register 0x08” [4][2] |

### [3] CLEAR_SWC_OUTPUT_POWER_GOOD_STATUS

- Description: Clear SWC Output Power Good Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 98, “Register 0x08” [3][2] |

### [2] CLEAR_SWD_OUTPUT_POWER_GOOD_STATUS

- Description: Clear SWD Output Power Good Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 98, “Register 0x08” [2][2] |

### [1] CLEAR_VIN_MGMT_INPUT_OVER_VOLTAGE_STATUS

- Description: Clear VIN_Mgmt Input Supply Over Voltage Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 98, “Register 0x08” [1][2] |

### [0] CLEAR_VIN_BULK_INPUT_OVER_VOLTAGE_STATUS

- Description: Clear VIN_Bulk Input Supply Over Voltage Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 98, “Register 0x08” [0][2] |

**Notes**

- NOTE 1: Table 106, “Register 0x10” [7:0] are self clearing bits.
- NOTE 2: See Table 28 and Table 29 for GSI_n and POWER_GOOD output signal status change.
- NOTE 3: Only applicable if Table 166, “Register 0x4F” [0] = ‘0’.

## R11 (0x11) — CLEAR_PMIC_HIGH_TEMP_WARNING_STATUS, CLEAR_VBIAS_POWER_GOOD_STATUS, CLEAR_VOUT_1.8V_OUTPUT_POWER_GOOD_STATUS, CLEAR_VIN_MGMT_TO_VIN_BULK_INPUT_SWITCHOVER_STATUS, CLEAR_SWA_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS, CLEAR_SWB_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS, CLEAR_SWC_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS, CLEAR_SWD_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS

Region: Host Region | Source: JESD301-1A.03 Table 107, p.125

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
| 1 | Clear Register Table 99, “Register 0x09” [7][2] |

### [6] CLEAR_VBIAS_POWER_GOOD_STATUS

- Description: Clear VBias Power Good Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 99, “Register 0x09” [6][2] |

### [5] CLEAR_VOUT_1.8V_OUTPUT_POWER_GOOD_STATUS

- Description: Clear VOUT_1.8V Output Power Good Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 99, “Register 0x09” [5][2] |

### [4] CLEAR_VIN_MGMT_TO_VIN_BULK_INPUT_SWITCHOVER_STATUS

- Description: Clear VIN_Mgmt to VIN_Bulk Input Supply Switchover Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 99, “Register 0x09” [4][2] |

### [3] CLEAR_SWA_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS

- Description: Clear Switch Node A High Output Current Consumption Warning Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 99, “Register 0x09” [3][2] |

### [2] CLEAR_SWB_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS

- Description: Clear Switch Node B High Output Current Consumption Warning Status.[3]
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0
- Source correction: Table 107 prints 'Clear Register Table 99, “Register 0x09” [2]' without the leading '1 =' used by every other bit of R11; treated as the value for code 1.

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 99, “Register 0x09” [2][2] |

### [1] CLEAR_SWC_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS

- Description: Clear Switch Node C High Output Current Consumption Warning Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 99, “Register 0x09” [1][2] |

### [0] CLEAR_SWD_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS

- Description: Clear Switch Node D High Output Current Consumption Warning Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 99, “Register 0x09” [0][2] |

**Notes**

- NOTE 1: Table 107, “Register 0x11” [7:0] are self clearing bits.
- NOTE 2: See Table 28 and Table 29 for GSI_n and POWER_GOOD output signal status change.
- NOTE 3: This register is applicable regardless of the setting in Table 166, “Register 0x4F” [0].

## R12 (0x12) — CLEAR_SWA_OUTPUT_OVER_VOLTAGE_STATUS, CLEAR_SWB_OUTPUT_OVER_VOLTAGE_STATUS, CLEAR_SWC_OUTPUT_OVER_VOLTAGE_STATUS, CLEAR_SWD_OUTPUT_OVER_VOLTAGE_STATUS, CLEAR_PER_ERROR_STATUS, CLEAR_PARITY_ERROR_STATUS

Region: Host Region | Source: JESD301-1A.03 Table 108, p.126

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | CLEAR_SWA_OUTPUT_OVER_VOLTAGE_STATUS | 1O | 0 |
| 6 | CLEAR_SWB_OUTPUT_OVER_VOLTAGE_STATUS | 1O | 0 |
| 5 | CLEAR_SWC_OUTPUT_OVER_VOLTAGE_STATUS | 1O | 0 |
| 4 | CLEAR_SWD_OUTPUT_OVER_VOLTAGE_STATUS | 1O | 0 |
| 3 | CLEAR_PER_ERROR_STATUS | 1O | 0 |
| 2 | CLEAR_PARITY_ERROR_STATUS | 1O | 0 |
| 1:0 | RESERVED | RV | 0 |

### [7] CLEAR_SWA_OUTPUT_OVER_VOLTAGE_STATUS

- Description: Clear Switch Node A Output Over Voltage Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 100, “Register 0x0A” [7][2] |

### [6] CLEAR_SWB_OUTPUT_OVER_VOLTAGE_STATUS

- Description: Clear Switch Node B Output Over Voltage Status.[3]
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 100, “Register 0x0A” [6][2] |

### [5] CLEAR_SWC_OUTPUT_OVER_VOLTAGE_STATUS

- Description: Clear Switch Node C Output Over Voltage Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 100, “Register 0x0A” [5][2] |

### [4] CLEAR_SWD_OUTPUT_OVER_VOLTAGE_STATUS

- Description: Clear Switch Node D Output Over Voltage Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 100, “Register 0x0A” [4][2] |

### [3] CLEAR_PER_ERROR_STATUS

- Description: Clear PEC Error Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 100, “Register 0x0A” [3] |

### [2] CLEAR_PARITY_ERROR_STATUS

- Description: Clear Parity Error Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 100, “Register 0x0A” [2] |

### [1:0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

**Notes**

- NOTE 1: Table 108, “Register 0x12” [7:0] are self clearing bits.
- NOTE 2: See Table 28 and Table 29 for GSI_n and POWER_GOOD output signal status change.
- NOTE 3: Only applicable if Table 166, “Register 0x4F” [0] = ‘0’.

## R13 (0x13) — CLEAR_SWA_OUTPUT_CURRENT_LIMITER_WARNING_STATUS, CLEAR_SWB_OUTPUT_CURRENT_LIMITER_WARNING_STATUS, CLEAR_SWC_OUTPUT_CURRENT_LIMITER_WARNING_STATUS, CLEAR_SWD_OUTPUT_CURRENT_LIMITER_WARNING_STATUS, CLEAR_SWA_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS, CLEAR_SWB_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS, CLEAR_SWC_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS, CLEAR_SWD_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

Region: Host Region | Source: JESD301-1A.03 Table 109, p.127

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
| 1 | Clear Register Table 101, “Register 0x0B” [7][2] |

### [6] CLEAR_SWB_OUTPUT_CURRENT_LIMITER_WARNING_STATUS

- Description: Clear Switch Node B Output Current Limiter Warning Status.[3]
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 101, “Register 0x0B” [6][2] |

### [5] CLEAR_SWC_OUTPUT_CURRENT_LIMITER_WARNING_STATUS

- Description: Clear Switch Node C Output Current Limiter Warning Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 101, “Register 0x0B” [5][2] |

### [4] CLEAR_SWD_OUTPUT_CURRENT_LIMITER_WARNING_STATUS

- Description: Clear Switch Node D Output Current Limiter Warning Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 101, “Register 0x0B” [4][2] |

### [3] CLEAR_SWA_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

- Description: Clear Switch Node A Output Under Voltage Lockout Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 101, “Register 0x0B” [3][2] |

### [2] CLEAR_SWB_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

- Description: Clear Switch Node B Output Under Voltage Lockout Status.[4]
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 101, “Register 0x0B” [2][2] |

### [1] CLEAR_SWC_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

- Description: Clear Switch Node C Output Under Voltage Lockout Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 101, “Register 0x0B” [1][2] |

### [0] CLEAR_SWD_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

- Description: Clear Switch Node D Output Under Voltage Lockout Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 101, “Register 0x0B” [0][2] |

**Notes**

- NOTE 1: Table 109, “Register 0x13” [7:0] are self clearing bits.
- NOTE 2: See Table 28 and Table 29 for GSI_n and POWER_GOOD output signal status change.
- NOTE 3: This register is applicable regardless of the setting in Table 166, “Register 0x4F” [0]
- NOTE 4: Only applicable if Table 166, “Register 0x4F” [0] = ‘0’.

## R14 (0x14) — CLEAR_VIN_MGMT_POWER_GOOD_STATUS_SWITCHOVER_MODE, CLEAR_VBIAS_OUTPUT_OR_VIN_BULK_UNDER_VOLTAGE_LOCKOUT_STATUS, CLEAR_VOUT_1.0V_OUTPUT_POWER_GOOD_STATUS, GLOBAL_CLEAR_STATUS

Region: Host Region | Source: JESD301-1A.03 Table 110, p.128

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
| 1 | Clear Register Table 141, “Register 0x33” [4][2] |

### [3] CLEAR_VBIAS_OUTPUT_OR_VIN_BULK_UNDER_VOLTAGE_LOCKOUT_STATUS

- Description: Clear VBias Output or VIN_Bulk Input Under Voltage Lockout Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 141, “Register 0x33” [3][2] |

### [2] CLEAR_VOUT_1.0V_OUTPUT_POWER_GOOD_STATUS

- Description: Clear VOUT_1.0V Output Power Good Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 141, “Register 0x33” [2][2] |

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

- NOTE 1: Table 110, “Register 0x14” [4:2, 0] are self clearing bits.
- NOTE 2: See Table 28 and Table 29 for GSI_n and POWER_GOOD output signal status change.
- NOTE 3: All status bits in register Table 106, “Register 0x10” [7,5:0], Table 107, “Register 0x11” [7:0], Table 108, “Register 0x12” [7:2], Table 109, “Register 0x13” [7:0] and Table 110, “Register 0x14” [4:2].
- NOTE 4: See Table 28 and Table 29 for GSI_n and POWER_GOOD output signal status change. For each Real Time Status Registers (Table 98, “Register 0x08” [7:0], Table 99, “Register 0x09” [7:0], Table 100, “Register 0x0A” [7:1], Table 101, “Register 0x0B” [7:0], Table 141, “Register 0x33” [4:2]), the PMIC offers a way to mask the status of each event interrupt. The mask registers are Table 111, “Register 0x15” [7,5:0], Table 112, “Register 0x16” [7:0], Table 113, “Register 0x17” [7:2], Table 114, “Register 0x18” [7:0], and Table 115, “Register 0x19” [4:2] respectively. The mask registers only masks the event interrupt on GSI_n and PWR_GOOD signal. There is also a global mask bits register control Table 137, “Register 0x2F” [1:0] to control the GSI_n and PWR_GOOD output signal. When all mask registers are Table 111, “Register 0x15” [7,5:0], Table 112, “Register 0x16” [7:0], Table 113, “Register 0x17” [7:2], Table 114, “Register 0x18” [7:0], and Table 115, “Register 0x19” [4:2] configured as ‘0’, the setting in Table 137, “Register 0x2F” [1:0] does not matter. The setting in Table 137, “Register 0x2F” [1:0] only matters when one or more mask registers Table 111, “Register 0x15” [7,5:0], Table 112, “Register 0x16” [7:0], Table 113, “Register 0x17” [7:2], Table 114, “Register 0x18” [7:0], and Table 115, “Register 0x19” [4:2] are configured to ‘1’. For any failure events that causes the PMIC to generate VR Disable command on its own, the mask register bits (Table 111, “Register 0x15” [0], Table 113, “Register 0x17” [7:4], Table 114, “Register 0x18” [3:0], Table 115, “Register 0x19” [3], Table 137, “Register 0x2F” [1:0]) do not apply and PMIC will assert PWR_GOOD output signal regardless of the setting in mask registers. The PMIC still updates the status registers appropriately when any event occurs. When masked, the host is expected to read the status registers periodically to learn if any of the event has occurred or not. The host can mask or unmask each event individually. The host can mask or un-mask at any time in non write protect mode. In write protect mode of operation, the mask registers are locked.

## R15 (0x15) — MASK_VIN_BULK_INPUT_POWER_GOOD_STATUS, MASK_SWA_OUTPUT_POWER_GOOD_STATUS, MASK_SWB_OUTPUT_POWER_GOOD_STATUS, MASK_SWC_OUTPUT_POWER_GOOD_STATUS, MASK_SWD_OUTPUT_POWER_GOOD_STATUS, MASK_VIN_MGMT_INPUT_OVER_VOLTAGE_STATUS, MASK_VIN_BULK_INPUT_OVER_VOLTAGE_STATUS

Region: Host Region | Source: JESD301-1A.03 Table 111, p.129

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
- Default: 1 → Mask SWA Output Power Good Status Event[1]

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWA Output Power Good Status Event |
| 1 | Mask SWA Output Power Good Status Event[1] |

### [4] MASK_SWB_OUTPUT_POWER_GOOD_STATUS

- Description: Mask SWB Output Power Good Status Event.[2]
- Attribute: RW — Read/Write
- Default: 1 → Mask SWB Output Power Good Status Event[1]

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWB Output Power Good Status Event |
| 1 | Mask SWB Output Power Good Status Event[1] |

### [3] MASK_SWC_OUTPUT_POWER_GOOD_STATUS

- Description: Mask SWC Output Power Good Status Event.
- Attribute: RW — Read/Write
- Default: 1 → Mask SWC Output Power Good Status Event[1]

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWC Output Power Good Status Event |
| 1 | Mask SWC Output Power Good Status Event[1] |

### [2] MASK_SWD_OUTPUT_POWER_GOOD_STATUS

- Description: Mask SWD Output Power Good Status Event.
- Attribute: RW — Read/Write
- Default: 1 → Mask SWD Output Power Good Status Event[1]

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWD Output Power Good Status Event |
| 1 | Mask SWD Output Power Good Status Event[1] |

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
| 1 | Mask VIN_Bulk Input Supply Over Voltage Status Event[3] |

**Notes**

- NOTE 1: Not assert GSI_n or assert POWER_GOOD output signal.
- NOTE 2: Only applicable if Table 166, “Register 0x4F” [0] = ‘0’.
- NOTE 3: Not assert GSI_n output signal.

## R16 (0x16) — MASK_PMIC_HIGH_TEMP_WARNING_STATUS, MASK_VBIAS_POWER_GOOD_STATUS, MASK_VOUT_1.8V_OUTPUT_POWER_GOOD_STATUS, MASK_VIN_MGMT_TO_VIN_BULK_SWITCHOVER_STATUS, MASK_SWA_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_S, MASK_SWB_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_S, MASK_SWC_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_S, MASK_SWD_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_S

Region: Host Region | Source: JESD301-1A.03 Table 112, p.130

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | MASK_PMIC_HIGH_TEMP_WARNING_STATUS | RW | 0 |
| 6 | MASK_VBIAS_POWER_GOOD_STATUS | RW | 0 |
| 5 | MASK_VOUT_1.8V_OUTPUT_POWER_GOOD_STATUS | RW | 1 |
| 4 | MASK_VIN_MGMT_TO_VIN_BULK_SWITCHOVER_STATUS | RW | 0 |
| 3 | MASK_SWA_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_S | RW | 0 |
| 2 | MASK_SWB_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_S | RW | 0 |
| 1 | MASK_SWC_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_S | RW | 0 |
| 0 | MASK_SWD_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_S | RW | 0 |

### [7] MASK_PMIC_HIGH_TEMP_WARNING_STATUS

- Description: Mask PMIC High Temperature Warning Status Event.
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask PMIC High Temperature Warning Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask PMIC High Temperature Warning Status Event |
| 1 | Mask PMIC High Temperature Warning Status Event[1] |

### [6] MASK_VBIAS_POWER_GOOD_STATUS

- Description: Mask VBias Power Good Status Event.
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask VBias Power Good Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask VBias Power Good Status Event |
| 1 | Mask VBias Power Good Status Event[2] |

### [5] MASK_VOUT_1.8V_OUTPUT_POWER_GOOD_STATUS

- Description: Mask VOUT_1.8V Output Power Good Status Event.
- Attribute: RW — Read/Write
- Default: 1 → Mask 1.8V Output Power Good Status Event[2]

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask 1.8V Output Power Good Status Event |
| 1 | Mask 1.8V Output Power Good Status Event[2] |

### [4] MASK_VIN_MGMT_TO_VIN_BULK_SWITCHOVER_STATUS

- Description: Mask VIN_Mgmt to VIN_Bulk Input Supply Switchover Status Event.
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask VIN_Mgmt to VIN_Bulk Input Supply Switchover Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask VIN_Mgmt to VIN_Bulk Input Supply Switchover Status Event |
| 1 | Mask VIN_Mgmt to VIN_Bulk Input Supply Switchover Status Event[1] |

### [3] MASK_SWA_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_S

- Description: TATUS Mask SWA High Output Current Consumption Warning Status Event.
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask SWA Output Current Consumption Warning Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWA Output Current Consumption Warning Status Event |
| 1 | Mask SWA Output Current Consumption Warning Status Event[1] |

### [2] MASK_SWB_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_S

- Description: TATUS Mask SWB High Output Current Consumption Warning Status Event.[3]
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask SWB Output Current Consumption Warning Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWB Output Current Consumption Warning Status Event |
| 1 | Mask SWB Output Current Consumption Warning Status Event[1] |

### [1] MASK_SWC_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_S

- Description: TATUS Mask SWC High Output Current Consumption Warning Status Event.
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask SWC Output Current Consumption Warning Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWC Output Current Consumption Warning Status Event |
| 1 | Mask SWC Output Current Consumption Warning Status Event[1] |

### [0] MASK_SWD_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_S

- Description: TATUS Mask SWD High Output Current Consumption Warning Status Event.
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask SWD Output Current Consumption Warning Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWD Output Current Consumption Warning Status Event |
| 1 | Mask SWD Output Current Consumption Warning Status Event[1] |

**Notes**

- NOTE 1: Not assert GSI_n output signal.
- NOTE 2: Not assert GSI_n or assert POWER_GOOD output signal
- NOTE 3: This register is applicable regardless of the setting in Table 166, “Register 0x4F” [0].

## R17 (0x17) — MASK_SWA_OUTPUT_OVER_VOLTAGE_STATUS, MASK_SWB_OUTPUT_OVER_VOLTAGE_STATUS, MASK_SWC_OUTPUT_OVER_VOLTAGE_STATUS, MASK_SWD_OUTPUT_OVER_VOLTAGE_STATUS, MASK_PEC_ERROR_STATUS, MASK_PARITY_ERROR_STATUS

Region: Host Region | Source: JESD301-1A.03 Table 113, p.131

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
| 1 | Mask SWB Output Over Voltage Status Event[1] |

### [5] MASK_SWC_OUTPUT_OVER_VOLTAGE_STATUS

- Description: Mask SWC Output Over Voltage Status Event.
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask SWC Output Over Voltage Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWC Output Over Voltage Status Event |
| 1 | Mask SWC Output Over Voltage Status Event[1] |

### [4] MASK_SWD_OUTPUT_OVER_VOLTAGE_STATUS

- Description: Mask SWD Output Over Voltage Status Event.
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask SWD Output Over Voltage Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWD Output Over Voltage Status Event |
| 1 | Mask SWD Output Over Voltage Status Event[1] |

### [3] MASK_PEC_ERROR_STATUS

- Description: Mask PEC Error Event for GSI_n output Only[3]
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask PEC Error Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask PEC Error Status Event |
| 1 | Mask PEC Error Status |

### [2] MASK_PARITY_ERROR_STATUS

- Description: Mask Parity Error Event for GSI_n output Only[3]
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
- NOTE 2: Only applicable if Table 166, “Register 0x4F” [0] = ‘0’.
- NOTE 3: Only applicable when PMIC is in I3C Basic Mode. This Mask register only masks the GSI_n output. Does not apply to IBI.

## R18 (0x18) — MASK_SWA_OUTPUT_CURRENT_LIMITER_WARNING_STATUS, MASK_SWB_OUTPUT_CURRENT_LIMITER_WARNING_STATUS, MASK_SWC_OUTPUT_CURRENT_LIMITER_WARNING_STATUS, MASK_SWD_OUTPUT_CURRENT_LIMITER_WARNING_STATUS, MASK_SWA_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS, MASK_SWB_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS, MASK_SWC_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS, MASK_SWD_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

Region: Host Region | Source: JESD301-1A.03 Table 114, p.132

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
| 1 | Mask SWB Output Current Limiter Warning Status Event[1] |

### [5] MASK_SWC_OUTPUT_CURRENT_LIMITER_WARNING_STATUS

- Description: Mask SWC Output Current Limiter Warning Status Event.
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask SWC Output Current Limiter Warning Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWC Output Current Limiter Warning Status Event |
| 1 | Mask SWC Output Current Limiter Warning Status Event[1] |

### [4] MASK_SWD_OUTPUT_CURRENT_LIMITER_WARNING_STATUS

- Description: Mask SWD Output Current Limiter Warning Status Event.
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask SWD Output Current Limiter Warning Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWD Output Current Limiter Warning Status Event |
| 1 | Mask SWD Output Current Limiter Warning Status Event[1] |

### [3] MASK_SWA_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

- Description: Mask SWA Output Under Voltage Lockout Status Event.
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask SWA Output Under Voltage Lockout Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWA Output Under Voltage Lockout Status Event |
| 1 | Mask SWA Output Under Voltage Lockout Status Event[1] |

### [2] MASK_SWB_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

- Description: Mask SWB Output Under Voltage Lockout Status Event.[3]
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask SWB Output Under Voltage Lockout Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWB Output Under Voltage Lockout Status Event |
| 1 | Mask SWB Output Under Voltage Lockout Status Event[1] |

### [1] MASK_SWC_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

- Description: Mask SWC Output Under Voltage Lockout Status Event.
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask SWC Output Under Voltage Lockout Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWC Output Under Voltage Lockout Status Event |
| 1 | Mask SWC Output Under Voltage Lockout Status Event[1] |

### [0] MASK_SWD_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

- Description: Mask SWD Output Under Voltage Lockout Status Event.
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask SWD Output Under Voltage Lockout Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWD Output Under Voltage Lockout Status Event |
| 1 | Mask SWD Output Under Voltage Lockout Status Event[1] |

**Notes**

- NOTE 1: Not assert GSI_n output signal.
- NOTE 2: This register is applicable regardless of the setting in Table 166, “Register 0x4F” [0]
- NOTE 3: Only applicable if Table 166, “Register 0x4F” [0] = ‘0’.

## R19 (0x19) — MASK_VIN_MGMT_POWER_GOOD_STATUS_SWITCHOVER_MODE, MASK_VBIAS_OUTPUT_OR_VIN_BULK_UNDER_VOLTAGE_LOCK, MASK_VOUT_1.0V_OUTPUT_POWER_GOOD_STATUS

Region: Host Region | Source: JESD301-1A.03 Table 115, p.133

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:5 | RESERVED | RV | 0 |
| 4 | MASK_VIN_MGMT_POWER_GOOD_STATUS_SWITCHOVER_MODE | RW | 0 |
| 3 | MASK_VBIAS_OUTPUT_OR_VIN_BULK_UNDER_VOLTAGE_LOCK | RW | 0 |
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

### [3] MASK_VBIAS_OUTPUT_OR_VIN_BULK_UNDER_VOLTAGE_LOCK

- Description: OUT_STATUS Mask VBias Output or VIN_Bulk Input Under Voltage Lockout Event
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask Vbias Output or VIN_Bulk Input Under Voltage Lockout Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask Vbias Output or VIN_Bulk Input Under Voltage Lockout Event |
| 1 | Mask Vbias Output or VIN_Bulk InputUnder Voltage Lockout Event[1] |

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

Region: Host Region | Source: JESD301-1A.03 Table 116, p.134

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

- Description: VBias LDO Output Threshold Voltage for Power Good Status
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
- Default: 0 → Report individual power for each rail in R0C, R0D, R0E, and R0F

| Code (bin) | Meaning |
|---|---|
| 0 | Report individual power for each rail in R0C, R0D, R0E, and R0F |
| 1 | Report total power of each rail in R0C5 |

### [0] VOUT_1.0V_POWER_GOOD_THRESHOLD_VOLTAGE

- Description: VOUT 1.0V LDO Output Threshold Voltage for Power Good Status
- Attribute: RW — Read/Write
- Default: 0 → -10% from the setting in Table 133, “Register 0x2B” [2:1]

| Code (bin) | Meaning |
|---|---|
| 0 | -10% from the setting in Table 133, “Register 0x2B” [2:1] |
| 1 | -15% from the setting in Table 133, “Register 0x2B” [2:1] |

**Notes**

- NOTE 1: If VIN_Bulk input voltage falls below this threshold, the PMIC may not guarantee the operation.
- NOTE 2: If VIN_Bulk voltage continues to fall below vendor specific UVLO, the PMIC triggers a VR Disable command and executes power down sequence.
- NOTE 3: If VIN_Bulk voltage threshold is higher than default setting of this register, the PMIC continues to operate but updates its PWR_GOOD status register and GSI_n/PWR_GOOD signal is asserted when VIN_Bulk falls below the threshold setting.
- NOTE 4: This register is only applicable if Table 117, “Register 0x1B” [6] = ‘1’.
- NOTE 5: Host should only read Table 102, “Register 0x0C” [7:0] for total power. The register contents of Table 103, “Register 0x0D”, Table 104, “Register 0x0E”, and Table 105, “Register 0x0F” may not be valid.

## R1B (0x1B) — VIN_BULK_OVER_VOLTAGE_THRESHOLD, CURRENT_OR_POWER_METER_SELECT, VIN_MGMT_OVER_VOLTAGE_THRESHOLD, GLOBAL_PWR_GOOD_PIN_STATUS_MASK, GSI_N_PIN_ENABLE, PMIC_HIGH_TEMPERATURE_WARNING_THRESHOLD

Region: Host Region | Source: JESD301-1A.03 Table 117, p.135

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

- Description: PMIC Output Regulator Measurement - Current or Power Meter
- Attribute: RW — Read/Write
- Default: 0 → Report Current Measurements in registers:[1]

| Code (bin) | Meaning |
|---|---|
| 0 | Report Current Measurements in registers:[1] |
| 1 | Report Power Measurements in registers[1] |

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

- NOTE 1: Table 102, “Register 0x0C” [7:0], Table 103, “Register 0x0D” [5:0], Table 104, “Register 0x0E” [5:0], Table 105, “Register 0x0F”[5:0].
- NOTE 2: Mask POWER_GOOD output signal for all appropriate register bits in Table 111, “Register 0x15” [7,5:0], Table 112, “Register 0x16” [7:0], Table 113, “Register 0x17” [7:4], Table 114, “Register 0x18” [7:0] and Table 115, “Register 0x19” [4:2]. Mask Register Control Table 137, “Register 0x2F” [1:0] still applies when Global PWR_GOOD output Mask register is set to ‘1’.
- NOTE 3: This register can be used as Global Mask Function for GSI_n pin. If disabled, this masks GSI_n output signal for all register bits in Table 111, “Register 0x15” [7, 5:0], Table 112, “Register 0x16” [7:0], Table 113, “Register 0x17” [7:2], Table 114, “Register 0x18” [7:0], and Table 115, “Register 0x19” [4:2].
- NOTE 4: The tolerance of the temperature warning threshold is + 5 0C from the selected setting.

## R1C (0x1C) — SWA_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRE

Region: Host Region | Source: JESD301-1A.03 Table 118, p.136

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:2 | SWA_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRE | RW | 011000 |
| 1:0 | RESERVED | RV | 0 |

### [7:2] SWA_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRE

- Description: SHOLD SWA Output High Current Consumption Warning Threshold
- Attribute: RW — Read/Write
- Default: 011000 → > 3.0 A

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 000000 | 0x00 | Un-defined |
| 000001 | 0x01 | > 0.125 A |
| 000010 | 0x02 | > 0.25 A |
| 000011 | 0x03 | > 0.375 A |
| 000100 | 0x04 | > 0.5 A or |
| 000101 | 0x05 | > 0.625 A |
| 000110 | 0x06 | > 0.75 A |
| 000111 | 0x07 | > 0.875 A |
| 001000 | 0x08 | > 1.0 A |
| 001001 | 0x09 | > 1.125 A |
| ... | ... | ... |
| 010111 | 0x17 | > 2.875 A |
| 011000 | 0x18 | > 3.0 A |
| 011001 | 0x19 | > 3.125 A |
| ... | ... | ... |
| 110111 | 0x37 | > 6.875 A |
| 111000 | 0x38 | > 7.0 A |
| 111001 | 0x39 | > 7.125 A |
| 111010 | 0x3A | > 7.25 A |
| 111011 | 0x3B | > 7.375 A |
| 111100 | 0x3C | > 7.5 A |
| 111101 | 0x3D | > 7.625 A |
| 111110 | 0x3E | > 7.75 A |
| 111111 | 0x3F | > 7.875 A |

### [1:0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

## R1D (0x1D) — SWB_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRE

Region: Host Region | Source: JESD301-1A.03 Table 119, p.137

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:2 | SWB_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRE | RW | 011000 |
| 1:0 | RESERVED | RV | 0 |

### [7:2] SWB_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRE

- Description: SHOLD SWB Output High Current Consumption Warning Threshold[1]
- Attribute: RW — Read/Write
- Default: 011000 → > 3.0 A

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 000000 | 0x00 | Un-defined |
| 000001 | 0x01 | > 0.125 A |
| 000010 | 0x02 | > 0.25 A |
| 000011 | 0x03 | > 0.375 A |
| 000100 | 0x04 | > 0.5 A or |
| 000101 | 0x05 | > 0.625 A |
| 000110 | 0x06 | > 0.75 A |
| 000111 | 0x07 | > 0.875 A |
| 001000 | 0x08 | > 1.0 A |
| 001001 | 0x09 | > 1.125 A |
| ... | ... | ... |
| 010111 | 0x17 | > 2.875 A |
| 011000 | 0x18 | > 3.0 A |
| ... | ... | ... |
| 110111 | 0x37 | > 6.875 A |
| 111000 | 0x38 | > 7.0 A |
| 111001 | 0x39 | > 7.125 A |
| 111010 | 0x3A | > 7.25 A |
| 111011 | 0x3B | > 7.375 A |
| 111100 | 0x3C | > 7.5 A |
| 111101 | 0x3D | > 7.625 A |
| 111110 | 0x3E | > 7.75 A |
| 111111 | 0x3F | > 7.875 A |

### [1:0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

**Notes**

- NOTE 1: This register is applicable regardless of the setting in Table 166, “Register 0x4F” [0]. For dual phase operation, this register should be configured identically as Table 118, “Register 0x1C” [7:2].

## R1E (0x1E) — SWC_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRE

Region: Host Region | Source: JESD301-1A.03 Table 120, p.138

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:2 | SWC_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRE | RW | 011000 |
| 1:0 | RESERVED | RV | 0 |

### [7:2] SWC_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRE

- Description: SHOLD SWC Output High Current Consumption Warning Threshold
- Attribute: RW — Read/Write
- Default: 011000 → > 3.0 A

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 000000 | 0x00 | Un-defined |
| 000001 | 0x01 | > 0.125 A |
| 000010 | 0x02 | > 0.25 A |
| 000011 | 0x03 | > 0.375 A |
| 000100 | 0x04 | > 0.5 A or |
| 000101 | 0x05 | > 0.625 A |
| 000110 | 0x06 | > 0.75 A |
| 000111 | 0x07 | > 0.875 A |
| 001000 | 0x08 | > 1.0 A |
| 001001 | 0x09 | > 1.125 A |
| ... | ... | ... |
| 010111 | 0x17 | > 2.875 A |
| 011000 | 0x18 | > 3.0 A |
| 011001 | 0x19 | > 3.125 A |
| ... | ... | ... |
| 110111 | 0x37 | > 6.875 A |
| 111000 | 0x38 | > 7.0 A |
| 111001 | 0x39 | > 7.125 A |
| 111010 | 0x3A | > 7.25 A |
| 111011 | 0x3B | > 7.375 A |
| 111100 | 0x3C | > 7.5 A |
| 111101 | 0x3D | > 7.625 A |
| 111110 | 0x3E | > 7.75 A |
| 111111 | 0x3F | > 7.875 A |

### [1:0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

## R1F (0x1F) — SWD_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD

Region: Host Region | Source: JESD301-1A.03 Table 121, p.139

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:2 | SWD_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD | RW | 011000 |
| 1:0 | RESERVED | RV | 0 |

### [7:2] SWD_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD

- Description: SWD Output High Current Consumption Warning Threshold
- Attribute: RW — Read/Write
- Default: 011000 → > 3.0 A

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 000000 | 0x00 | Un-defined |
| 000001 | 0x01 | > 0.125 A |
| 000010 | 0x02 | > 0.25 A |
| 000011 | 0x03 | > 0.375 A |
| 000100 | 0x04 | > 0.5 A or |
| 000101 | 0x05 | > 0.625 A |
| 000110 | 0x06 | > 0.75 A |
| 000111 | 0x07 | > 0.875 A |
| 001000 | 0x08 | > 1.0 A |
| 001001 | 0x09 | > 1.125 A |
| ... | ... | ... |
| 010111 | 0x17 | > 2.875 A |
| 011000 | 0x18 | > 3.0 A |
| 011001 | 0x19 | > 3.125 A |
| ... | ... | ... |
| 110111 | 0x37 | > 6.875 A |
| 111000 | 0x38 | > 7.0 A |
| 111001 | 0x39 | > 7.125 A |
| 111010 | 0x3A | > 7.25 A |
| 111011 | 0x3B | > 7.375 A |
| 111100 | 0x3C | > 7.5 A |
| 111101 | 0x3D | > 7.625 A |
| 111110 | 0x3E | > 7.75 A |
| 111111 | 0x3F | > 7.875 A |

### [1:0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

## R20 (0x20) — SWA_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING, SWB_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING, SWC_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING, SWD_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING

Region: Host Region | Source: JESD301-1A.03 Table 122, p.140

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWA_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING | RW | 0 |
| 5:4 | SWB_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING | RW | 0 |
| 3:2 | SWC_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING | RW | 0 |
| 1:0 | SWD_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING | RW | 0 |

### [7:6] SWA_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING

- Description: PMIC5000, COT Ivalley_limit
- Attribute: RW — Read/Write
- Default: 0

**When: PMIC5000, COT Ivalley_limit**

| Code (bin) | Meaning |
|---|---|
| 00 | 4.0 A |
| 01 | 4.5 A |
| 10 | 5.0 A |
| 11 | 5.5 A |

**When: PMIC5010, COT Ivalley_limit**

| Code (bin) | Meaning |
|---|---|
| 00 | 2.0 A |
| 01 | 2.5 A |
| 10 | 3.0 A |
| 11 | 3.5 A |

### [5:4] SWB_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING

- Description: PMIC5000, COT Ivalley_limit:[2]
- Attribute: RW — Read/Write
- Default: 0

**When: PMIC5000, COT Ivalley_limit:[2]**

| Code (bin) | Meaning |
|---|---|
| 00 | 4.0 A |
| 01 | 4.5 A |
| 10 | 5.0 A |
| 11 | 5.5 A |

**When: PMIC5010, COT Ivalley_limit**

| Code (bin) | Meaning |
|---|---|
| 00 | 2.0 A |
| 01 | 2.5 A |
| 10 | 3.0 A |
| 11 | 3.5 A |

### [3:2] SWC_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING

- Description: PMIC5000, COT Ivalley_limit:
- Attribute: RW — Read/Write
- Default: 0

**When: PMIC5000, COT Ivalley_limit:**

| Code (bin) | Meaning |
|---|---|
| 00 | 4.0 A |
| 01 | 4.5 A |
| 10 | 5.0 A |
| 11 | 5.5 A |

**When: PMIC5010, COT Ivalley_limit**

| Code (bin) | Meaning |
|---|---|
| 00 | 2.0 A |
| 01 | 2.5 A |
| 10 | 3.0 A |
| 11 | 3.5 A |

### [1:0] SWD_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING

- Description: PMIC5000, COT Ivalley_limit:
- Attribute: RW — Read/Write
- Default: 0

**When: PMIC5000, COT Ivalley_limit:**

| Code (bin) | Meaning |
|---|---|
| 00 | 4.0 A |
| 01 | 4.5 A |
| 10 | 5.0 A |
| 11 | 5.5 A |

**When: PMIC5010, COT Ivalley_limit**

| Code (bin) | Meaning |
|---|---|
| 00 | 2.0 A |
| 01 | 2.5 A |
| 10 | 3.0 A |
| 11 | 3.5 A |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 167, “Register 0x50””.
- NOTE 2: This register is applicable regardless of the setting in Table 166, “Register 0x4F” [0]. If Table 166, “Register 0x4F” [0] = ‘1’, this register must be configured identically as bits [7:6].

## R21 (0x21) — SWA_VOLTAGE_SETTING, SWA_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

Region: Host Region | Source: JESD301-1A.03 Table 123, p.142

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
- Default: 0 → -5% from the setting in Table 123, “Register 0x21” [7:1]

| Code (bin) | Meaning |
|---|---|
| 0 | -5% from the setting in Table 123, “Register 0x21” [7:1] |
| 1 | -7.5% from the setting in Table 123, “Register 0x21” [7:1] |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 156, “Register 0x45”.
- NOTE 2: If required, the host must update the settings in register Table 123, “Register 0x21” [0], Table 124, “Register 0x22” [7:2] and Table 122, “Register 0x20” [7:6] first prior to updating the settings in the register Table 123, “Register 0x21” [7:1].
- NOTE 3: PMIC guarantees efficiency spec and all electrical characteristics spec within a range of 1050 mV to 1160 mV.
- NOTE 4: After VR is enabled, the host may update this register to any new setting that it may desire. However to prevent false error trigger, the PMIC internally will increment the SWA output voltage setting by 5 mV at a time. The time it takes for PMIC to adjust the output voltage is 5 μs for each 5 mV increment. The host must wait sufficient time for PMIC to adjust to final value. As an example, if host adjusts the output voltage by 50 mV from the original value, the host must wait minimum of 50 μs before PMIC can guarantee the new output voltage. During this time, PMIC masks the PWR_GOOD output signal assertion to prevent any artificial error due to the crossing of the output voltage threshold setting. However, PMIC does assert PWR_GOOD output signal if there is any abnormal issues that triggers VR Disable command as described in Table 27, “Events Interrupt Summary”. Further, PMIC does monitor PWR_GOOD input signal and executes power off config sequence registers if it is registered low when Table 140, “Register 0x32” [5] = ‘1’.
- NOTE 5: Table 133, “Register 0x2B” [5] = ‘0’; 5 mV step size.
- NOTE 6: Table 133, “Register 0x2B” [5] = ‘1’; 5 mV step size

## R22 (0x22) — SWA_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING, SWA_OVER_VOLTAGE_THRESHOLD_SETTING, SWA_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING, SWA_OUTPUT_SOFT_STOP_TIME

Region: Host Region | Source: JESD301-1A.03 Table 124, p.143

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWA_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING | RW | 01 |
| 5:4 | SWA_OVER_VOLTAGE_THRESHOLD_SETTING | RW | 10 |
| 3:2 | SWA_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING | RW | 00 |
| 1:0 | SWA_OUTPUT_SOFT_STOP_TIME | RW | 00 |

### [7:6] SWA_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING

- Description: SWA Output Threshold High Side Voltage For Power Good Status
- Attribute: RW — Read/Write
- Default: 01 → +7.5% from the setting in Table 123, “Register 0x21” [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +5% from the setting in Table 123, “Register 0x21” [7:1] |
| 01 | +7.5% from the setting in Table 123, “Register 0x21” [7:1] |
| 10 | +10% from the setting in Table 123, “Register 0x21” [7:1] |
| 11 | Reserved |

### [5:4] SWA_OVER_VOLTAGE_THRESHOLD_SETTING

- Description: SWA Output Regulator Threshold For Over Voltage Status[3]
- Attribute: RW — Read/Write
- Default: 10 → +12.5% from the setting in Table 123, “Register 0x21” [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +7.5% from the setting in Table 123, “Register 0x21” [7:1] |
| 01 | +10% from the setting in Table 123, “Register 0x21” [7:1] |
| 10 | +12.5% from the setting in Table 123, “Register 0x21” [7:1] |
| 11 | Reserved |

### [3:2] SWA_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING

- Description: SWA Output Regulator Threshold For Under Voltage Lockout Status
- Attribute: RW — Read/Write
- Default: 00 → -10% from the setting in Table 123, “Register 0x21” [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | -10% from the setting in Table 123, “Register 0x21” [7:1] |
| 01 | -12.5% from the setting in Table 123, “Register 0x21” [7:1] |
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

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 157, “Register 0x46”.
- NOTE 2: If required, the host must update the setting in register Table 123, “Register 0x21” [0], Table 124, “Register 0x22” [7:2] and Table 122, “Register 0x20” [7:6] first prior to updating the settings in the register Table 123, “Register 0x21” [7:1].
- NOTE 3: The setting for the Over Voltage must be higher than Power Good High Side Voltage threshold in Table 124, “Register 0x22”[7:6].
- NOTE 4: This is the time it takes for buck regulator to go from steady state voltage to 0 V.

## R23 (0x23) — SWB_VOLTAGE_SETTING, SWB_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

Region: Host Region | Source: JESD301-1A.03 Table 125, p.144

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
- Default: 0 → -5% from the setting in Table 125, “Register 0x23” [7:1]

| Code (bin) | Meaning |
|---|---|
| 0 | -5% from the setting in Table 125, “Register 0x23” [7:1] |
| 1 | -7.5% from the setting in Table 125, “Register 0x23” [7:1] |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 158, “Register 0x47”.
- NOTE 2: If required, the host must update the settings in register Table 125, “Register 0x23” [0], Table 126, “Register 0x24” [7:2], and Table 122, “Register 0x20” [5:4] first prior to updating the settings in the register Table 125, “Register 0x23” [7:1].
- NOTE 3: Only applicable if Table 166, “Register 0x4F” [0] = ‘0’.
- NOTE 4: PMIC guarantees efficiency spec and all electrical characteristics spec within a range of 1050 mV to 1160 mV.
- NOTE 5: After VR is enabled, the host may update this register to any new setting that it may desire. However to prevent false error trigger, the PMIC internally will increment the SWB output voltage setting by 5 mV at a time. The time it takes for PMIC to adjust the output voltage is 5 μs for each 5 mV increment. The host must wait sufficient time for PMIC to adjust to final value. As an example, if host adjusts the output voltage by 50 mV from the original value, the host must wait minimum of 50 μs before PMIC can guarantee the new output voltage. During this time, PMIC masks the PWR_GOOD output signal assertion to prevent any artificial error due to the crossing of the output voltage threshold setting. However, PMIC does assert PWR_GOOD output signal if there is any abnormal issues that triggers VR Disable command as described in Table 27. Further, PMIC does monitor PWR_GOOD input signal and executes power off config sequence registers if it is registered low when Table 140, “Register 0x32” [5] = ‘1’.
- NOTE 6: Table 133, “Register 0x2B” [4] = ‘0’; 5 mV step size.
- NOTE 7: Table 133, “Register 0x2B” [4] = ‘1’; 5 mV step size

## R24 (0x24) — SWB_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING, SWB_OVER_VOLTAGE_THRESHOLD_SETTING, SWB_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING, SWB_OUTPUT_SOFT_STOP_TIME

Region: Host Region | Source: JESD301-1A.03 Table 126, p.145

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWB_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING | RW | 01 |
| 5:4 | SWB_OVER_VOLTAGE_THRESHOLD_SETTING | RW | 10 |
| 3:2 | SWB_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING | RW | 00 |
| 1:0 | SWB_OUTPUT_SOFT_STOP_TIME | RW | 00 |

### [7:6] SWB_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING

- Description: SWB Output Threshold High Side Voltage For Power Good Status
- Attribute: RW — Read/Write
- Default: 01 → +7.5% from the setting in Table 125, “Register 0x23” [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +5% from the setting in Table 125, “Register 0x23” [7:1] |
| 01 | +7.5% from the setting in Table 125, “Register 0x23” [7:1] |
| 10 | +10% from the setting in Table 125, “Register 0x23” [7:1] |
| 11 | Reserved |

### [5:4] SWB_OVER_VOLTAGE_THRESHOLD_SETTING

- Description: SWB Output Regulator Threshold For Over Voltage Status[4]
- Attribute: RW — Read/Write
- Default: 10 → +12.5% from the setting in Table 125, “Register 0x23” [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +7.5% from the setting in Table 125, “Register 0x23” [7:1] |
| 01 | +10% from the setting in Table 125, “Register 0x23” [7:1] |
| 10 | +12.5% from the setting in Table 125, “Register 0x23” [7:1] |
| 11 | Reserved |

### [3:2] SWB_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING

- Description: SWB Output Regulator Threshold For Under Voltage Lockout Status
- Attribute: RW — Read/Write
- Default: 00 → -10% from the setting in Table 125, “Register 0x23” [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | -10% from the setting in Table 125, “Register 0x23” [7:1] |
| 01 | -12.5% from the setting in Table 125, “Register 0x23” [7:1] |
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

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 159, “Register 0x48”.
- NOTE 2: If required, the host must update the settings in register Table 125, “Register 0x23” [0], Table 126, “Register 0x24” [7:2] and Table 122, “Register 0x20” [5:4] first prior to updating the settings in the register Table 125, “Register 0x23” [7:1].
- NOTE 3: Only applicable if Table 166, “Register 0x4F” [0] = ‘0’.
- NOTE 4: The setting for the Over Voltage must be higher than Power Good High Side Voltage threshold in Table 126, “Register 0x24”[7:6].
- NOTE 5: This is the time it takes for buck regulator to go from steady state voltage to 0 V.

## R25 (0x25) — SWC_VOLTAGE_SETTING, SWC_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

Region: Host Region | Source: JESD301-1A.03 Table 127, p.146

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:1 | SWC_VOLTAGE_SETTING | RW | 011 1100 |
| 0 | SWC_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING | RW | 0 |

### [7:1] SWC_VOLTAGE_SETTING

- Description: SWC Output Regulator Voltage Setting[3],[4]
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

### [0] SWC_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

- Description: SWC Output Threshold Low Side Voltage For Power Good Status
- Attribute: RW — Read/Write
- Default: 0 → -5% from the setting in Table 127, “Register 0x25” [7:1]

| Code (bin) | Meaning |
|---|---|
| 0 | -5% from the setting in Table 127, “Register 0x25” [7:1] |
| 1 | -7.5% from the setting in Table 127, “Register 0x25” [7:1] |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 160, “Register 0x49”.
- NOTE 2: If required, the host must update the settings in register Table 127, “Register 0x25” [0], Table 128, “Register 0x26” [7:2] and Table 122, “Register 0x20” [3:2] first prior to updating the settings in the register Table 127, “Register 0x25” [7:1].
- NOTE 3: PMIC guarantees efficiency spec and all electrical characteristics spec within a range of 1050 mV to 1160 mV.
- NOTE 4: After VR is enabled, the host may update this register to any new setting that it may desire. However to prevent false error trigger, the PMIC internally will increment the SWC output voltage setting by 5 mV at a time. The time it takes for PMIC to adjust the output voltage is 5 μs for each 5 mV increment. The host must wait sufficient time for PMIC to adjust to final value. As an example, if host adjusts the output voltage by 50 mV from the original value, the host must wait minimum of 50 μs before PMIC can guarantee the new output voltage. During this time, PMIC masks the PWR_GOOD output signal assertion to prevent any artificial error due to the crossing of the output voltage threshold setting. However, PMIC does assert PWR_GOOD output signal if there is any abnormal issues that triggers VR Disable command as described in Table 27, “Events Interrupt Summary”. Further, PMIC does monitor PWR_GOOD input signal and executes power off config sequence registers if it is registered low when Table 140, “Register 0x32” [5] = ‘1’.
- NOTE 5: Table 133, “Register 0x2B” [3] = ‘0’; 5 mV step size.
- NOTE 6: Table 133, “Register 0x2B” [3] = ‘1’; 5 mV step size

## R26 (0x26) — SWC_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING, SWC_OVER_VOLTAGE_THRESHOLD_SETTING, SWC_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING, SWC_OUTPUT_SOFT_STOP_TIME

Region: Host Region | Source: JESD301-1A.03 Table 128, p.147

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWC_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING | RW | 01 |
| 5:4 | SWC_OVER_VOLTAGE_THRESHOLD_SETTING | RW | 10 |
| 3:2 | SWC_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING | RW | 00 |
| 1:0 | SWC_OUTPUT_SOFT_STOP_TIME | RW | 00 |

### [7:6] SWC_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING

- Description: SWC Output Threshold High Side Voltage For Power Good Status
- Attribute: RW — Read/Write
- Default: 01 → +7.5% from the setting in Table 127, “Register 0x25” [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +5% from the setting in Table 127, “Register 0x25” [7:1] |
| 01 | +7.5% from the setting in Table 127, “Register 0x25” [7:1] |
| 10 | +10% from the setting in Table 127, “Register 0x25” [7:1] |
| 11 | Reserved |

### [5:4] SWC_OVER_VOLTAGE_THRESHOLD_SETTING

- Description: SWC Output Regulator Threshold For Over Voltage Status[3]
- Attribute: RW — Read/Write
- Default: 10 → +12.5% from the setting in Table 127, “Register 0x25” [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +7.5% from the setting in Table 127, “Register 0x25” [7:1] |
| 01 | +10% from the setting in Table 127, “Register 0x25” [7:1] |
| 10 | +12.5% from the setting in Table 127, “Register 0x25” [7:1] |
| 11 | Reserved |

### [3:2] SWC_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING

- Description: SWC Output Regulator Threshold For Under Voltage Lockout Status
- Attribute: RW — Read/Write
- Default: 00 → -10% from the setting in Table 127, “Register 0x25” [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | -10% from the setting in Table 127, “Register 0x25” [7:1] |
| 01 | -12.5% from the setting in Table 127, “Register 0x25” [7:1] |
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

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 161, “Register 0x4A”.
- NOTE 2: If required, the host must update the settings in register Table 127, “Register 0x25” [0], Table 128, “Register 0x26” [7:2], and Table 122, “Register 0x20” [3:2] first prior to updating the settings in the register Table 127, “Register 0x25” [7:1].
- NOTE 3: The setting for the Over Voltage must be higher than Power Good High Side Voltage threshold in Table 128, “Register 0x26”[7:6].
- NOTE 4: This is the time it takes for buck regulator to go from steady state voltage to 0 V.

## R27 (0x27) — SWD_VOLTAGE_SETTING, SWD_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

Region: Host Region | Source: JESD301-1A.03 Table 129, p.148

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
- Default: 0 → -5% from the setting in Table 129, “Register 0x27” [7:1]

| Code (bin) | Meaning |
|---|---|
| 0 | -5% from the setting in Table 129, “Register 0x27” [7:1] |
| 1 | -7.5% from the setting in Table 129, “Register 0x27” [7:1] |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 162, “Register 0x4B”.
- NOTE 2: If required, the host must update the settings in register Table 129, “Register 0x27” [0], Table 130, “Register 0x28” [7:2], and Table 122, “Register 0x20” [1:0] first prior to updating the settings in the register Table 129, “Register 0x27” [7:1].
- NOTE 3: PMIC guarantees efficiency spec and all electrical characteristics spec within a range of 1750 mV to 1850 mV.
- NOTE 4: After VR is enabled, the host may update this register to any new setting that it may desire. However to prevent false error trigger, the PMIC internally will increment the SWD output voltage setting by 5 mV at a time. The time it takes for PMIC to adjust the output voltage is 5 μs for each 5 mV increment. The host must wait sufficient time for PMIC to adjust to final value. As an example, if host adjusts the output voltage by 50 mV from the original value, the host must wait minimum of 50 μs before PMIC can guarantee the new output voltage. During this time, PMIC masks the PWR_GOOD output signal assertion to prevent any artificial error due to the crossing of the output voltage threshold setting. However, PMIC does assert PWR_GOOD output signal if there is any abnormal issues that triggers VR Disable command as described in Table 27, “Events Interrupt Summary”. Further, PMIC does monitor PWR_GOOD input signal and executes power off config sequence registers if it is registered low when Table 140, “Register 0x32” [5] = ‘1’.
- NOTE 5: Table 133, “Register 0x2B” [0] = ‘0’; 5 mV step size.
- NOTE 6: Table 133, “Register 0x2B” [0] = ‘1’; 5 mV step size.

## R28 (0x28) — SWD_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING, SWD_OVER_VOLTAGE_THRESHOLD_SETTING, SWD_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING, SWD_OUTPUT_SOFT_STOP_TIME

Region: Host Region | Source: JESD301-1A.03 Table 130, p.149

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWD_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING | RW | 01 |
| 5:4 | SWD_OVER_VOLTAGE_THRESHOLD_SETTING | RW | 10 |
| 3:2 | SWD_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING | RW | 00 |
| 1:0 | SWD_OUTPUT_SOFT_STOP_TIME | RW | 00 |

### [7:6] SWD_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING

- Description: SWD Output Threshold High Side Voltage For Power Good Status
- Attribute: RW — Read/Write
- Default: 01 → +7.5% from the setting in Table 129, “Register 0x27” [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +5% from the setting in Table 129, “Register 0x27” [7:1] |
| 01 | +7.5% from the setting in Table 129, “Register 0x27” [7:1] |
| 10 | +10% from the setting in Table 129, “Register 0x27” [7:1] |
| 11 | Reserved |

### [5:4] SWD_OVER_VOLTAGE_THRESHOLD_SETTING

- Description: SWD Output Regulator Threshold For Over Voltage Status[3]
- Attribute: RW — Read/Write
- Default: 10 → +12.5% from the setting in Table 129, “Register 0x27” [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +7.5% from the setting in Table 129, “Register 0x27” [7:1] |
| 01 | +10% from the setting in Table 129, “Register 0x27” [7:1] |
| 10 | +12.5% from the setting in Table 129, “Register 0x27” [7:1] |
| 11 | Reserved |

### [3:2] SWD_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING

- Description: SWD Output Regulator Threshold For Under Voltage Lockout Status
- Attribute: RW — Read/Write
- Default: 00 → -10% from the setting in Table 129, “Register 0x27” [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | -10% from the setting in Table 129, “Register 0x27” [7:1] |
| 01 | -12.5% from the setting in Table 129, “Register 0x27” [7:1] |
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

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 163, “Register 0x4C”.
- NOTE 2: If required, the host must update the settings in register Table 129, “Register 0x27” [0], Table 130, “Register 0x28” [7:2] and Table 122, “Register 0x20” [1:0] first prior to updating the settings in the register Table 129, “Register 0x27” [7:1].
- NOTE 3: The setting for the Over Voltage must be higher than Power Good High Side Voltage threshold in Table 130, “Register 0x28”[7:6].
- NOTE 4: This is the time it takes for buck regulator to go from steady state voltage to 0 V.

## R29 (0x29) — SWA_MODE_SELECT, SWA_SWITCHING_FREQ, SWB_MODE_SELECT, SWB_SWITCHING_FREQ

Region: Host Region | Source: JESD301-1A.03 Table 131, p.150

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
| 10 | 1000 KHz |
| 11 | 1250 KHz |

### [3:2] SWB_MODE_SELECT

- Description: SWB Output Regulator Mode Selection[3]
- Attribute: RW — Read/Write
- Default: 10 → COT; DCM (Constant on Time; Discontinuous Current Mode)
- Source correction: Field header says [1:0] but the Bits column shows [3:2]; the Bits column is used.

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
| 10 | 1000 KHz |
| 11 | 1250 KHz |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 164, “Register 0x4D”.
- NOTE 2: If required, the host must adjust this register first before issuing VR Enable command in Table 140, “Register 0x32” [7].
- NOTE 3: Only applicable if Table 166, “Register 0x4F” [0] = ‘0’.

## R2A (0x2A) — SWC_MODE_SELECT, SWC_SWITCHING_FREQ, SWD_MODE_SELECT, SWD_SWITCHING_FREQ

Region: Host Region | Source: JESD301-1A.03 Table 132, p.151

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

- Description: Switch Node C Output Regulator Switching Frequency
- Attribute: RW — Read/Write
- Default: 01 → 750 KHz

| Code (bin) | Meaning |
|---|---|
| 00 | 500 KHz |
| 01 | 750 KHz |
| 10 | 1000 KHz |
| 11 | 1250 KHz |

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
| 00 | 500 KHz |
| 01 | 750 KHz |
| 10 | 1000 KHz |
| 11 | 1250 KHz |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 165, “Register 0x4E”.
- NOTE 2: If required, the host must adjust this register first before issuing VR Enable command in Table 140, “Register 0x32” [7].

## R2B (0x2B) — VOUT_1.8V_VOLTAGE_SETTING, SWA_VOLTAGE_RANGE, SWB_VOLTAGE_RANGE, SWC_VOLTAGE_RANGE, VOUT_1.0V_VOLTAGE_SETTING, SWD_VOLTAGE_RANGE

Region: Host Region | Source: JESD301-1A.03 Table 133, p.152

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

- Description: SWC Output Voltage Range Selection[7]
- Attribute: RW — Read/Write
- Default: 0 → Range: 800 mV to 1435 mV for SWC; 5 mV step size

| Code (bin) | Meaning |
|---|---|
| 0 | Range: 800 mV to 1435 mV for SWC; 5 mV step size |
| 1 | Range: 600 mV to 1235 mV for SWC; 5 mV step size |

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

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 168, “Register 0x51”.
- NOTE 2: If required, the host must adjust this register first before issuing VR Enable command in Table 140, “Register 0x32” [7]. The host must also wait minimum of 5 μs after the adjustment before issuing VR Enable command.
- NOTE 3: The VOUT_1.8V Power Good threshold in register Table 116, “Register 0x1A” [2] is always fixed regardless of the setting in this register.
- NOTE 4: Range and resolution selection applies to register Table 123, “Register 0x21” [7:1].
- NOTE 5: Range and resolution selection applies to register Table 125, “Register 0x23” [7:1].
- NOTE 6: Only applicable if Table 166, “Register 0x4F” [0] = ‘0’.
- NOTE 7: Range and resolution selection applies to register Table 127, “Register 0x25” [7:1].
- NOTE 8: If required, the host must adjust this register one step at a time (0.1 V increment or decrement) to prevent false trigger of power good status and PWR_GOOD pin assertion. In other words, host should not increment or decrement 0.2 V or 0.3 V from its current setting.
- NOTE 9: Range and resolution selection applies to register Table 129, “Register 0x27” [7:1].

## R2C (0x2C) — SWA_OUTPUT_SOFT_START_TIME, SWB_OUTPUT_SOFT_START_TIME

Region: Host Region | Source: JESD301-1A.03 Table 134, p.153

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

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 173, “Register 0x5D”.
- NOTE 2: If required, the host must adjust this register first before issuing VR Enable command in Table 140, “Register 0x32” [7].
- NOTE 3: This is the time it takes for buck regulator to go from 0 V to steady state voltage (the actual voltage varies based on pre-programmed voltage).
- NOTE 4: Only applicable if Table 166, “Register 0x4F” [0] = ‘0’.

## R2D (0x2D) — SWC_OUTPUT_SOFT_START_TIME, SWD_OUTPUT_SOFT_START_TIME

Region: Host Region | Source: JESD301-1A.03 Table 135, p.154

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

- Description: SWD Output Regulator Soft Start Time After VR Enable[3]
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

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 174, “Register 0x5E”.
- NOTE 2: If required, the host must adjust this register first before issuing VR Enable command in Table 140, “Register 0x32” [7].
- NOTE 3: This is the time it takes for buck regulator to go from 0 V to steady state voltage (the actual voltage varies based on pre- programmed voltage)

## R2E (0x2E) — PMIC_SHUTDOWN_TEMPERATURE_THRESHOLD

Region: Host Region | Source: JESD301-1A.03 Table 136, p.154

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
- Default: 100 → PMIC Temperature > 145 °C

| Code (bin) | Meaning |
|---|---|
| 000 | PMIC Temperature > 105 °C |
| 001 | PMIC Temperature > 115 °C |
| 010 | PMIC Temperature > 125 °C |
| 011 | PMIC Temperature > 135 °C |
| 100 | PMIC Temperature > 145 °C |
| 101 | Reserved |
| 110 | Reserved |
| 111 | Reserved |

## R2F (0x2F) — VIN_MGMT_INPUT_SUPPLY_SWITCHOVER_THRESHOLD, SWA_REGULATOR_CONTROL, SWB_REGULATOR_CONTROL, SWC_REGULATOR_CONTROL, SWD_REGULATOR_CONTROL, WRITE_PROTECT_FUNCTION_CONTROL, MASK_BITS_REGISTER_CONTROL

Region: Host Region | Source: JESD301-1A.03 Table 137, p.155

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

- Description: PMIC Write Protect Function Control
- Attribute: RW — Read/Write
- Default: 0 → CAMP input signal determines the Write Protect Function as noted in clause 2.7.7.1

| Code (bin) | Meaning |
|---|---|
| 0 | CAMP input signal determines the Write Protect Function as noted in clause 2.7.7.1 |
| 1 | Write Protect Function is disabled; All register write access is allowed independent of CAMP input signal as noted in clause 2.7.7.1. |

### [1:0] MASK_BITS_REGISTER_CONTROL

- Description: Mask Bits Register Control[5]
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
- NOTE 2: This bit must be used only after power up sequence (after VR Enable command). At first power up, PMIC automatically updates the status of this register to ‘1’ after VR Enable command. When VR Enable command is registered, the PMIC updates this register based on Power On Sequence Configuration (0 to 3) setting. If enabled in Power On Sequence Configuration 0 to 3 registers, only then, under non write protect mode of operation, the PMIC’s output regulator can be disabled by clearing this bit and they can be re-enabled again by setting this bit. The PMIC does not alter its Power Good output signal and keeps it asserted High. If any regulator is not enabled in Power on Sequence Configuration 0 to 3, it cannot be enabled using this register. For example, if only SWA is enabled and SWB, SWC and SWD is not enabled in Table 152, “Register 0x40” [7:0] to Table 155, “Register 0x43” [7:0] then only SWA can be disabled and then re-enabled again but SWB, SWC and SWD cannot be enabled using Table 137, “Register 0x2F” [6:3].
- NOTE 3: In non write protect mode, after VR enable command, if any output regulators are disabled by clearing Table 137, “Register 0x2F” [6:3] and then if host issues VR Disable command or PMIC internally triggers VR Disable command, the PMIC keeps the disabled output regulator in Table 137, “Register 0x2F”[6:3] off and remaining output regulators are disabled by following the Power Off Sequence Configuration 0 to 3 settings.
- NOTE 4: Only applicable if Table 166, “Register 0x4F” [0] = ‘0’.
- NOTE 5: Applies to Mask Registers Table 111, “Register 0x15” [7,5:0], Table 112, “Register 0x16” [7:0], Table 113, “Register 0x17” [7:2], Table 114, “Register 0x18” [7:0], Table 115, “Register 0x19” [4:2] when any one or more Mask registers are set to ‘1’. If all Mask registers are configured as ‘0’, the setting in this register (Table 137, “Register 0x2F” [1:0]) does not matter.

## R30 (0x30) — ADC_ENABLE, ADC_SELECT, ADC_REGISTER_UPDATE_FREQUENCY

Region: Host Region | Source: JESD301-1A.03 Table 138, p.157

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | ADC_ENABLE | RW | 0 |
| 6:3 | ADC_SELECT | RW | 0 |
| 2 | RESERVED | RV | 0 |
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
| 0100 | 0x4 | Reserved |
| 0101 | 0x5 | VIN_Bulk Input Voltage |
| 0110 | 0x6 | VIN_Mgmt Input Voltage |
| 0111 | 0x7 | VBias Output Voltage |
| 1000 | 0x8 | VOUT_1.8V Output Voltage |
| 1001 | 0x9 | VOUT_1.0V Output Voltage |

### [2] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [1:0] ADC_REGISTER_UPDATE_FREQUENCY

- Description: ADC Current or Power Measurement Update Frequency[4],[5]
- Attribute: RW — Read/Write
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 00 | 1 ms |
| 01 | 2 ms |
| 10 | 4 ms |
| 11 | 8 ms |

**Notes**

- NOTE 1: Disables the ADC function completely. Applies to voltage readout in Table 139, “Register 0x31” [7:0] as well as current or power readout in Table 102, “Register 0x0C” [7:0], Table 103, “Register 0x0D” [5:0], Table 104, “Register 0x0E” [5:0] and Table 105, “Register 0x0F” [5:0]. Does not apply to thermal sensor temperature readout in Table 141, “Register 0x33” [7:5] as well as high temperature warning and critical temperature shutdown.
- NOTE 2: The host shall wait minimum of 9 ms delay after the input selection for ADC readout and the actual readout from Table 139, “Register 0x31” to get the latest reading
- NOTE 3: Only applicable if Table 166, “Register 0x4F” [0] = ‘0’
- NOTE 4: For average output current or power measurement in registers Table 102, “Register 0x0C” [7:0], Table 103, “Register 0x0D” [5:0], Table 104, “Register 0x0E” [5:0] and Table 105, “Register 0x0F” [5:0].
- NOTE 5: This register represents how often the registers are updated. The internal sampling rate is vendor specific.

## R31 (0x31) — ADC_READ

Region: Host Region | Source: JESD301-1A.03 Table 139, p.158

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | ADC_READ | RO | 0 |

### [7:0] ADC_READ

- Description: ADC Output Voltage Reading[1](Applies to SW[A:D], VOUT_1.8V, VOUT_1.0V, VIN_Mgmt)
- Attribute: RO — Read Only (writes have no effect)
- Default: 0

**When: ADC Output Voltage Reading[1](Applies to SW[A:D], VOUT_1.8V, VOUT_1.0V, VIN_Mgmt)**

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

**When: ADC Output Voltage Reading[3] (Applies to VBias Output Voltage)**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | 25 mV |
| 00000010 | 0x02 | 50 mV |
| ... | ... | ... |
| 11111111 | 0xFF | ≥ 6375 mV |

**Notes**

- NOTE 1: Only valid when Table 138, “Register 0x30” [6:3] = ‘0000’ or ‘0001’ or ‘0010’ or ‘0011’ or ‘0110’ or ‘1000’ or ‘1001’.
- NOTE 2: Only valid when Table 138, “Register 0x30” [6:3] = ‘0101’.
- NOTE 3: Only valid when Table 138, “Register 0x30” [6:3] = ‘0111’.

## R32 (0x32) — VR_ENABLE, MANAGEMENT_INTERFACE_SELECTION, EXECUTE_VR_ENABLE_CONTROL_, EXECUTE_CAMP_FAIL_N_FUNCTION_CONTROL, CAMP_PWR_GOOD_OUTPUT_SIGNAL_CONTROL

Region: Host Region | Source: JESD301-1A.03 Table 140, p.159

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | VR_ENABLE | RW | 0 |
| 6 | MANAGEMENT_INTERFACE_SELECTION | RO | 0 |
| 5 | EXECUTE_VR_ENABLE_CONTROL_ | RW | 1 |
| 4 | EXECUTE_CAMP_FAIL_N_FUNCTION_CONTROL | RW | 0 |
| 3 | CAMP_PWR_GOOD_OUTPUT_SIGNAL_CONTROL | RW | 0 |
| 2:0 | RESERVED | RV | 00 |

### [7] VR_ENABLE

- Description: PMIC Enable[1],[2],[3],[4]
- Attribute: RW — Read/Write
- Default: 0 → PMIC Disable

| Code (bin) | Meaning |
|---|---|
| 0 | PMIC Disable |
| 1 | PMIC Enable |

### [6] MANAGEMENT_INTERFACE_SELECTION

- Description: PMIC Management Bus Interface Protocol Selection[5]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → I2C Protocol (Max speed 1 MHz)

| Code (bin) | Meaning |
|---|---|
| 0 | I2C Protocol (Max speed 1 MHz) |
| 1 | I3C Basic Protocol |

### [5] EXECUTE_VR_ENABLE_CONTROL_

- Description: PMIC VR Enable Command Execution Control over I2C/I3C Bus[4]
- Attribute: RW — Read/Write
- Default: 1 → Execute VR Enable Command

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Execute VR Enable Command; i.e., ignore bit [7] = ‘1’ and keep it as ‘0’. |
| 1 | Execute VR Enable Command |

### [4] EXECUTE_CAMP_FAIL_N_FUNCTION_CONTROL

- Description: PMIC CAMP Fail_n function (Transition from High to Low) Control
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
| 1 | PWR_GOOD Output Float[6] |

### [2:0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 00

**Notes**

- NOTE 1: Host sets this bit at first power on. After this bit is set, the PMIC executes Power On Sequence configuration 0 (Table 152, “Register 0x40”) to Power On Sequence configuration 3 (Table 155, “Register 0x43”) registers. At least one bit in Table 152, “Register 0x40” [6:3] must be set to ‘1’ to issue VR Enable command.
- NOTE 2: The host shall ensure that prior to issuing VR Enable command, there is no pending IBI interrupt (i.e., Table 100, “Register 0x0A” [1] = ‘1’) status. After host issues VR Enable command, the PMIC may NACK any I2C or I3C Basic bus transaction by host until tPMIC_PWR_GOOD_OUT timing parameter is satisfied. The host shall not access any device specific registers or issue any CCCs until tPMIC_PWR_GOOD_OUT parameter is satisfied. The PMIC device may request for an IBI during power up sequence (i.e., during tPMIC_PWR_GOOD_OUT time) if there is any event.
- NOTE 3: After host issues VR Enable command, the PMIC may NACK any I2C or I3C Basic bus transactions by host until tPMIC_PWR_GOOD_OUT timing parameter is satisfied.
- NOTE 4: Once Table 140, “Register 0x32” [7] is set to ‘1’ via VR Enable command, the subsequent write to register Table 140, “Register 0x32” [5] = ‘0’ is ignored by the PMIC. If there is a simultaneous write to register Table 140, “Register 0x32” [7,5] = ‘10’, the PMIC prioritizes bit [5] and does not execute VR Enable command.
- NOTE 5: This register is automatically updated when SETAASA CCC or RSTDAA CCC is registered by the PMIC device or when PMIC device goes through bus reset as described in clause 2.10.15 regardless of whether PMIC is in write protect mode or non write protect mode of operation. This register can be read by the Host through normal Read operation but it cannot be written with normal write operation either in I2C mode or I3C Basic mode of operation. When this register is updated, it takes in effect where there is a next START operation (i.e., after STOP operation).
- NOTE 6: When this encoding is set, the PMIC always floats the PWR_GOOD output signal even when there is an internal VR Disable command due to fault condition.

## R33 (0x33) — TEMPERATURE_MEASUREMENT, VIN_MGMT_POWER_GOOD_STATUS_SWITCHOVER_MODE, VBIAS_OR_VIN_BULK_UNDER_VOLTAGE_LOCKOUT_STATUS, VOUT_1.0V_OUTPUT_POWER_GOOD_STATUS

Region: Host Region | Source: JESD301-1A.03 Table 141, p.160

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

- NOTE 1: The accuracy of the temperature readout code is + 5 °C.
- NOTE 2: This register has no meaning when PMIC is NOT in switchover mode. In switchover mode only, when PMIC detects VIN_Mgmt input supply from the platform, this bit is set to indicate that PMIC now recognizes valid VIN_Mgmt input power supply.
- NOTE 3: This register is set when VBias LDO output goes below vendor specific threshold or VIN_Bulk input goes below vendor-specific threshold.
- NOTE 4: This register is set when VOUT_1.0V output drops below the threshold setting in register Table 116, “Register 0x1A” [0].

## R34 (0x34) — PEC_ENABLE, IBI_ENABLE, PARITY_DISABLE, HID_CODE

Region: Host Region | Source: JESD301-1A.03 Table 142, p.161

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

- Description: T Bit Parity Code Disable[2] (Applicable Only if R32 [6] = ‘1’.)
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
- NOTE 2: This register is automatically updated when RSTDAA CCC is registered by the PMIC device or when PMIC device goes through bus reset as described in clause 2.10.15. This register cannot be written by the Host through normal write operation either in I2C mode or I3C mode of operation. This register is updated with DEVCTRL CCC with RegMod=’0’ only. This register cannot be written with DEVCTRL CCC with RegMod=’1’.
- NOTE 3: This register is automatically updated when ENEC CCC or DISEC CCC or RSTDAA CCC is registered by the PMIC device or when PMIC device goes through bus reset as described in clause 2.10.15. This register can be read by the Host through normal Read operation but it cannot be written with normal write operation either in I2C mode or I3C mode of operation. This register cannot be written with DEVCTRL CCC with RegMod=’1’.
- NOTE 4: When Parity function is disabled, the PMIC simply ignores the “T” bit information from the Host. The host may actually choose to compute the parity and send that information in “T” bit or simply drive static low or high in “T” bit.
- NOTE 5: This register is updated when PMIC device receives SETHID CCC or when PMIC device goes through bus reset as described in clause 2.10.15. This register cannot be written with DEVCTRL CCC with RegMod=’1’.

## R35 (0x35) — ERROR_INJECTION_ENABLE, ERROR_INJECTION_RAIL_SELECTION, OVER_VOLTAGE_UNDER_VOLTAGE_SELECT, MISC_ERROR_INJECTION_TYPE

Region: Host Region | Source: JESD301-1A.03 Table 143, p.162

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | ERROR_INJECTION_ENABLE | RW | 0 |
| 6:4 | ERROR_INJECTION_RAIL_SELECTION | RW | 0 |
| 3 | OVER_VOLTAGE_UNDER_VOLTAGE_SELECT | RW | 0 |
| 2:0 | MISC_ERROR_INJECTION_TYPE | RW | 0 |

### [7] ERROR_INJECTION_ENABLE

- Description: Error Injection Enable[3]
- Attribute: RW — Read/Write
- Default: 0 → Disable

| Code (bin) | Meaning |
|---|---|
| 0 | Disable |
| 1 | Enable |

### [6:4] ERROR_INJECTION_RAIL_SELECTION

- Description: Error Injection - Input Rail and Output Rail Selection[4],[5]
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

- Description: Over Voltage or Under Voltage Selection for Bits [6:4][6]
- Attribute: RW — Read/Write
- Default: 0 → Over Voltage

| Code (bin) | Meaning |
|---|---|
| 0 | Over Voltage |
| 1 | Under Voltage[7] |

### [2:0] MISC_ERROR_INJECTION_TYPE

- Description: Miscellaneous Error Injection Type[8]
- Attribute: RW — Read/Write
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 000 | Undefined |
| 001 | VIN_Mgmt to VIN_Bulk Switchover |
| 010 | Critical Temperature Shutdown |
| 011 | High Temperature Warning Threshold |
| 100 | VOUT_1.8V LDO Power Good |
| 101 | High Current Consumption Warning[9] |
| 110 | Reserved |
| 111 | Current Limiter Warning[9] |

**Notes**

- NOTE 1: Refer to clause 2.8.2 for error function usage model. The host can erase the error log registers (Table 94, “Register 0x04” to Table 94, “Register 0x04”) by writing 0x74 to Table 146, “Register 0x39”.
- NOTE 2: To exit from Error Injection Mode, the PMIC must go through power cycle of both VIN_Bulk and VIN_Mgmt input supply.
- NOTE 3: When error function is invoked by setting bit [7] = ‘1’, the setting of bits [6:4, 2:0] = ‘000 000’ is considered an illegal setting.
- NOTE 4: This register Table 143, “Register 0x35” [6:4] is only applicable if Table 143, “Register 0x35” [2:0] is ‘000’. Any value other than ‘000’ in both Table 143, “Register 0x35” [6:4] and Table 143, “Register 0x35” [2:0] is considered an illegal setting and PMIC operation is not guaranteed.
- NOTE 5: If dual phase regulator is selected, use SWA encoding to inject the error. Register bit [3] selects either over voltage or under voltage condition for the setting selected in this register.
- NOTE 6: This register Table 143, “Register 0x35” [3] is only applicable if bits [6:4] is anything other than ‘000’.
- NOTE 7: The under voltage selection only applies to SWx output rails and VIN_Bulk input. Does not apply to VIN_Mgmt input.
- NOTE 8: This register Table 143, “Register 0x35” [2:0] is only applicable if Table 143, “Register 0x35” [6:3] is ‘0000’. Any value other than ‘000’ in both Table 143, “Register 0x35” [6:4] and Table 143, “Register 0x35” [2:0] is considered an illegal setting and PMIC operation is not guaranteed.
- NOTE 9: Applies to all enabled SWx output regulators at the same time.

## R37 (0x37) — DIMM_VENDOR_MEMORY_REGION_PASSWORD_LOWER_BYTE

Region: Host Region | Source: JESD301-1A.03 Table 144, p.163

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | DIMM_VENDOR_MEMORY_REGION_PASSWORD_LOWER_BYTE | WO | - |

### [7:0] DIMM_VENDOR_MEMORY_REGION_PASSWORD_LOWER_BYTE

- Description: DIMM Vendor Memory Region (0x40 - 0x6F) Password - Lower Byte [7:0] = Code
- Attribute: WO — Write Only (reads return 0)
- Default: -
- Values: no per-value encoding is listed in the spec for this field.

## R38 (0x38) — DIMM_VENDOR_MEMORY_REGION_PASSWORD_UPPER_BYTE

Region: Host Region | Source: JESD301-1A.03 Table 145, p.163

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | DIMM_VENDOR_MEMORY_REGION_PASSWORD_UPPER_BYTE | WO | - |

### [7:0] DIMM_VENDOR_MEMORY_REGION_PASSWORD_UPPER_BYTE

- Description: DIMM Vendor Memory Region (0x40 - 0x6F) Password - Upper Byte [7:0] = Code
- Attribute: WO — Write Only (reads return 0)
- Default: -
- Values: no per-value encoding is listed in the spec for this field.

## R39 (0x39) — (unnamed)

Region: Host Region | Source: JESD301-1A.03 Table 146, p.163

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
| 0x74 | Clear Registers R04 to R07, Erase MTP memory for R04 Register. |

**When: DIMM Vendor Region (0x40 to 0x6F) Write Codes**

| Code (bin) | Meaning |
|---|---|
| 0x40 | Unlock DIMM Vendor Region. Password needs to be present in R37 and R38 registers. |
| 0x00 | Lock DIMM Vendor Region. |
| 0x80 | Burn DIMM Vendor Region Password. New password needs to be present in R37 and R38. |
| 0x81 | Burn DIMM Vendor Region - 0x40 to 0x4F |
| 0x82 | Burn DIMM Vendor Region - 0x50 to 0x5F |
| 0x85 | Burn DIMM Vendor Region - 0x60 to 0x6F |

**When: DIMM Vendor Region (0x40 to 0x6F) Read Codes**

| Code (bin) | Meaning |
|---|---|
| 0x5A | Burning is complete in DIMM Vendor region. |

## R3A (0x3A) — DEFAULT_READ_ADDRESS_POINTER_ENABLE, DEFAULT_READ_STARTING_ADDRESS, BURST_LENGTH_FOR_READ_DEFAULT_ADDR_POINTER

Region: Host Region | Source: JESD301-1A.03 Table 147, p.164

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | RESERVED | RV | 0 |
| 6 | DEFAULT_READ_ADDRESS_POINTER_ENABLE | RW | 0 |
| 5:4 | DEFAULT_READ_STARTING_ADDRESS | RW | 0 |
| 3:2 | BURST_LENGTH_FOR_READ_DEFAULT_ADDR_POINTER | RW | 0 |
| 1:0 | RESERVED | RV | 0 |

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
| 10 | Reserved |
| 11 | Reserved |

### [3:2] BURST_LENGTH_FOR_READ_DEFAULT_ADDR_POINTER

- Description: Burst Length (# of Bytes) to be transferred for Read Default Address Pointer Mode[5]
- Attribute: RW — Read/Write
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 00 | 2 Bytes |
| 01 | 4 Bytes |
| 10 | Reserved |
| 11 | 16 Bytes |

### [1:0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

**Notes**

- NOTE 1: The write (or update) transaction to this register must be followed by STOP operation to allow the PMIC device to update the setting.
- NOTE 2: The register setting in R3A [5:4] is a don’t care.
- NOTE 3: This mode is only allowed when PEC function is disabled (i.e., register R34 [7] = ‘0’).
- NOTE 4: This register is only applicable if R3A [6] = ‘1’.
- NOTE 5: This register is only applicable if R3A [6] = ‘1’ and R34 [7] = ‘1’.

## R3B (0x3B) — PMIC_PART_CAPABILITY_EXT, REVISION_ID_MAJOR_STEPPING, REVISION_ID_MINOR_STEPPING, PMIC_PART_CAPABILITY

Region: Host Region | Source: JESD301-1A.03 Table 148, p.165

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | PMIC_PART_CAPABILITY_EXT | ROE | 0 |
| 5:4 | REVISION_ID_MAJOR_STEPPING | ROE | - |
| 3:1 | REVISION_ID_MINOR_STEPPING | ROE | - |
| 0 | PMIC_PART_CAPABILITY | ROE | - |

### [7:6] PMIC_PART_CAPABILITY_EXT

- Description: PMIC Current Capability Extension. This register bits [7:6] and bit [0] provides 3 bit encoding as following: All other encodings are reserved.
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0
- Note: the codes below are wider than this 2-bit field; the encoding combines bits from more than one field/register (see Description).

| Code (bin) | Meaning |
|---|---|
| 000 | Small PMIC (Low Current) |
| 001 | Big PMIC (High Current) |
| 01x | Extreme PMIC (Highest Current) |

### [5:4] REVISION_ID_MAJOR_STEPPING

- Description: Major Revision Stepping
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: -

| Code (bin) | Meaning |
|---|---|
| 00 | Revision 1 |
| 01 | Revision 2 |
| 10 | Revision 3 |
| 11 | Revision 4 |

### [3:1] REVISION_ID_MINOR_STEPPING

- Description: Minor Revision Stepping All other encodings are reserved.
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: -

| Code (bin) | Meaning |
|---|---|
| 000 | Revision 0 |
| 001 | Revision 1 |
| 010 | Revision 2 |
| 011 | Revision 3 |

### [0] PMIC_PART_CAPABILITY

- Description: PMIC Current Capability. See also bits [7:6] definition.
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: -

| Code (bin) | Meaning |
|---|---|
| 0 | Small PMIC (Low Current) |
| 1 | Big PMIC (High Current) |

## R3C (0x3C) — VENDOR_ID_BYTE0

Region: Host Region | Source: JESD301-1A.03 Table 149, p.165

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | VENDOR_ID_BYTE0 | ROE | - |

### [7:0] VENDOR_ID_BYTE0

- Description: Vendor Identification Register Byte 0.
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: -
- Values: no per-value encoding is listed in the spec for this field.

## R3D (0x3D) — VENDOR_ID_BYTE1

Region: Host Region | Source: JESD301-1A.03 Table 150, p.165

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | VENDOR_ID_BYTE1 | ROE | - |

### [7:0] VENDOR_ID_BYTE1

- Description: Vendor Identification Register Byte 1. Registers
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: -
- Values: no per-value encoding is listed in the spec for this field.

## R40 (0x40) — POWER_ON_SEQUENCE_CONFIG0, POWER_ON_SEQUENCE_CONFIG0_SWA_ENABLE, POWER_ON_SEQUENCE_CONFIG0_SWB_ENABLE, POWER_ON_SEQUENCE_CONFIG0_SWC_ENABLE, POWER_ON_SEQUENCE_CONFIG0_SWD_ENABLE, POWER_ON_SEQUENCE_CONFIG0_IDLE

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-1A.03 Table 152, p.168

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | POWER_ON_SEQUENCE_CONFIG0 | RWPE | 0 |
| 6 | POWER_ON_SEQUENCE_CONFIG0_SWA_ENABLE | RWPE | 0 |
| 5 | POWER_ON_SEQUENCE_CONFIG0_SWB_ENABLE | RWPE | 0 |
| 4 | POWER_ON_SEQUENCE_CONFIG0_SWC_ENABLE | RWPE | 0 |
| 3 | POWER_ON_SEQUENCE_CONFIG0_SWD_ENABLE | RWPE | 0 |
| 2:0 | POWER_ON_SEQUENCE_CONFIG0_IDLE | RWPE | 001 |

### [7] POWER_ON_SEQUENCE_CONFIG0

- Description: PMIC Power On Sequence Config 02
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Do Not Execute Config 0

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Execute Config 0 |
| 1 | Execute Config 0 |

### [6] POWER_ON_SEQUENCE_CONFIG0_SWA_ENABLE

- Description: Enable SWA Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Disable SWA Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Disable SWA Output Regulator |
| 1 | Enable SWA Output Regulator |

### [5] POWER_ON_SEQUENCE_CONFIG0_SWB_ENABLE

- Description: Enable SWB Output Regulator.[3]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Disable SWB Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Disable SWB Output Regulator |
| 1 | Enable SWB Output Regulator |

### [4] POWER_ON_SEQUENCE_CONFIG0_SWC_ENABLE

- Description: Enable SWC Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Disable SWC Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Disable SWC Output Regulator |
| 1 | Enable SWC Output Regulator |

### [3] POWER_ON_SEQUENCE_CONFIG0_SWD_ENABLE

- Description: Enable SWD Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Disable SWD Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Disable SWD Output Regulator |
| 1 | Enable SWD Output Regulator |

### [2:0] POWER_ON_SEQUENCE_CONFIG0_IDLE

- Description: Idle time after Power On Sequence Config 04
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

- NOTE 1: If more than one configuration register is used for power on sequence, first register must start at Table 152, “Register 0x40” and it must go in sequential order to Table 155, “Register 0x43” to turn on all desired regulators. In other words, there must not be any gap of the register that is used for power on sequence.
- NOTE 2: If bit [7] = ‘0’, bits [6:3] must be programmed as ‘0000’. If bit [7] = ‘1’, at least one of the bits [6:3] must be programmed as ‘1’.
- NOTE 3: Only applicable if Table 166, “Register 0x4F” [0] = ‘0’. This bit is a don’t care when Table 166, “Register 0x4F” [0] = ‘1’.
- NOTE 4: Idle time is the additional time after soft-start time expires. The PMIC waits sum of Soft Start time and Idle time before it executes the next power on sequence configuration register. If more than one regulators are enabled, the PMIC uses the largest value of the soft start time among the regulators that are enabled in this configuration register.

## R41 (0x41) — POWER_ON_SEQUENCE_CONFIG1, POWER_ON_SEQUENCE_CONFIG1_SWA_ENABLE, POWER_ON_SEQUENCE_CONFIG1_SWB_ENABLE, POWER_ON_SEQUENCE_CONFIG1_SWC_ENABLE, POWER_ON_SEQUENCE_CONFIG1_SWD_ENABLE, POWER_ON_SEQUENCE_CONFIG1_IDLE

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-1A.03 Table 153, p.169

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
- Default: 0 → Do Not Execute Config1[3]

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Execute Config1[3] |
| 1 | Execute Config 1 |

### [6] POWER_ON_SEQUENCE_CONFIG1_SWA_ENABLE

- Description: Enable SWA Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Disable SWA Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Disable SWA Output Regulator |
| 1 | Enable SWA Output Regulator |

### [5] POWER_ON_SEQUENCE_CONFIG1_SWB_ENABLE

- Description: Enable SWB Output Regulator.[4]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Disable SWB Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Disable SWB Output Regulator |
| 1 | Enable SWB Output Regulator |

### [4] POWER_ON_SEQUENCE_CONFIG1_SWC_ENABLE

- Description: Enable Switch Node C Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Disable SWC Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Disable SWC Output Regulator |
| 1 | Enable SWC Output Regulator |

### [3] POWER_ON_SEQUENCE_CONFIG1_SWD_ENABLE

- Description: Enable Switch Node D Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Disable SWD Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Disable SWD Output Regulator |
| 1 | Enable SWD Output Regulator |

### [2:0] POWER_ON_SEQUENCE_CONFIG1_IDLE

- Description: Idle time after Power On Sequence Config 15
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

- NOTE 1: If any regulators are enabled in Table 152, “Register 0x40” [6:3], those regulators must be configured as ‘1’ in this sequence.
- NOTE 2: If more than one configuration register is used for power on sequence, first register must start at Table 152, “Register 0x40” and it must go in sequential order to Table 155, “Register 0x43” to turn on all desired regulators. In other words, there must not be any gap of the register that is used for power on sequence.
- NOTE 3: If bit [7] = ‘0’, bits [6:3] must be programmed as ‘0000’. If bit [7] = ‘1’, at least one of the bits [6:3] must be programmed as ‘1’.
- NOTE 4: Only applicable if Table 166, “Register 0x4F” [0] = ‘0’. This bit is a don’t care when Table 166, “Register 0x4F” [0] = ‘1’
- NOTE 5: Idle time is the additional time after soft-start time expires. The PMIC waits sum of Soft Start time and Idle time before it executes the next power on sequence configuration register. If more than one regulators are enabled, the PMIC uses the largest value of the soft start time among the regulators that are enabled in this configuration register.

## R42 (0x42) — POWER_ON_SEQUENCE_CONFIG2, POWER_ON_SEQUENCE_CONFIG2_SWA_ENABLE, POWER_ON_SEQUENCE_CONFIG2_SWB_ENABLE, POWER_ON_SEQUENCE_CONFIG2_SWC_ENABLE, POWER_ON_SEQUENCE_CONFIG2_SWD_ENABLE, POWER_ON_SEQUENCE_CONFIG2_IDLE

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-1A.03 Table 154, p.170

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | POWER_ON_SEQUENCE_CONFIG2 | RWPE | 0 |
| 6 | POWER_ON_SEQUENCE_CONFIG2_SWA_ENABLE | RWPE | 0 |
| 5 | POWER_ON_SEQUENCE_CONFIG2_SWB_ENABLE | RWPE | 0 |
| 4 | POWER_ON_SEQUENCE_CONFIG2_SWC_ENABLE | RWPE | 0 |
| 3 | POWER_ON_SEQUENCE_CONFIG2_SWD_ENABLE | RWPE | 0 |
| 2:0 | POWER_ON_SEQUENCE_CONFIG2_IDLE | RWPE | 001 |

### [7] POWER_ON_SEQUENCE_CONFIG2

- Description: PMIC Power On Sequence Config 23
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Do Not Execute Config 2

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Execute Config 2 |
| 1 | Execute Config 2 |

### [6] POWER_ON_SEQUENCE_CONFIG2_SWA_ENABLE

- Description: Enable Switch Node A Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Disable Switch Node A Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Disable Switch Node A Output Regulator |
| 1 | Enable Switch Node A Output Regulator |

### [5] POWER_ON_SEQUENCE_CONFIG2_SWB_ENABLE

- Description: Enable Switch Node B Output Regulator.[4]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Disable Switch Node B Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Disable Switch Node B Output Regulator |
| 1 | Enable Switch Node B Output Regulator |

### [4] POWER_ON_SEQUENCE_CONFIG2_SWC_ENABLE

- Description: Enable Switch Node C Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Disable Switch Node C Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Disable Switch Node C Output Regulator |
| 1 | Enable Switch Node C Output Regulator |

### [3] POWER_ON_SEQUENCE_CONFIG2_SWD_ENABLE

- Description: Enable Switch Node D Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Disable Switch Node D Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Disable Switch Node D Output Regulator |
| 1 | Enable Switch Node D Output Regulator |

### [2:0] POWER_ON_SEQUENCE_CONFIG2_IDLE

- Description: Idle time after Power On Sequence Config 25
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

- NOTE 1: If any regulators are enabled in Table 152, “Register 0x40” [6:3] and Table 153, “Register 0x41” [6:3], those regulators must be configured as ‘1’ in this sequence.
- NOTE 2: If more than one configuration register is used for power on sequence, first register must start at Table 152, “Register 0x40” and it must go in sequential order to Table 155, “Register 0x43” to turn on all desired regulators. In other words, there must not be any gap of the register that is used for power on sequence.
- NOTE 3: If bit [7] = ‘0’, bits [6:3] must be programmed as ‘0000’. If bit [7] = ‘1’, at least one of the bits [6:3] must be programmed as ‘1’.
- NOTE 4: Only applicable if Table 166, “Register 0x4F” [0] = ‘0’. This bit is a don’t care when Table 166, “Register 0x4F” [0] = ‘1’
- NOTE 5: Idle time is the additional time after soft-start time expires. The PMIC waits sum of Soft Start time and Idle time before it executes the next power on sequence configuration register. If more than one regulators are enabled, the PMIC uses the largest value of the soft start time among the regulators that are enabled in this configuration register.

## R43 (0x43) — POWER_ON_SEQUENCE_CONFIG3, POWER_ON_SEQUENCE_CONFIG3_SWA_ENABLE, POWER_ON_SEQUENCE_CONFIG3_SWB_ENABLE, POWER_ON_SEQUENCE_CONFIG3_SWC_ENABLE, POWER_ON_SEQUENCE_CONFIG3_SWD_ENABLE, POWER_ON_SEQUENCE_CONFIG3_IDLE

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-1A.03 Table 155, p.171

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
- Default: 0 → Do Not Execute Config 33

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Execute Config 33 |
| 1 | Execute Config 3 |

### [6] POWER_ON_SEQUENCE_CONFIG3_SWA_ENABLE

- Description: Enable Switch Node A Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Disable Switch Node A Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Disable Switch Node A Output Regulator |
| 1 | Enable Switch Node A Output Regulator |

### [5] POWER_ON_SEQUENCE_CONFIG3_SWB_ENABLE

- Description: Enable Switch Node B Output Regulator.[4]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Disable Switch Node B Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Disable Switch Node B Output Regulator |
| 1 | Enable Switch Node B Output Regulator |

### [4] POWER_ON_SEQUENCE_CONFIG3_SWC_ENABLE

- Description: Enable Switch Node C Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Disable Switch Node C Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Disable Switch Node C Output Regulator |
| 1 | Enable Switch Node C Output Regulator |

### [3] POWER_ON_SEQUENCE_CONFIG3_SWD_ENABLE

- Description: Enable Switch Node D Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Disable Switch Node D Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Disable Switch Node D Output Regulator |
| 1 | Enable Switch Node D Output Regulator |

### [2:0] POWER_ON_SEQUENCE_CONFIG3_IDLE

- Description: Idle time after Power On Sequence Config 35
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

- NOTE 1: If any regulators are enabled in Table 152, “Register 0x40” [6:3], Table 153, “Register 0x41” [6:3] and Table 154, “Register 0x42” [6:3], those regulators must be configured as ‘1’ in this sequence.
- NOTE 2: If more than one configuration register is used for power on sequence, first register must start at Table 152, “Register 0x40” and it must go in sequential order to Table 155, “Register 0x43” to turn on all desired regulators. In other words, there must not be any gap of the register that is used for power on sequence.
- NOTE 3: If bit [7] = ‘0’, bits [6:3] must be programmed as ‘0000’. If bit [7] = ‘1’, at least one of the bits [6:3] must be programmed as ‘1’.
- NOTE 4: Only applicable if Table 166, “Register 0x4F” [0] = ‘0’. This bit is a don’t care when Table 166, “Register 0x4F” [0] = ‘1’
- NOTE 5: Idle time is the additional time after soft-start time expires. The PMIC waits sum of Soft Start time and Idle time before it executes the next event. If more than one regulators are enabled, the PMIC uses the largest value of the soft start time among the regulators that are enabled in this configuration register.

## R45 (0x45) — SWA_VOLTAGE_SETTING, SWA_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-1A.03 Table 156, p.172

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
- Default: 0 → - 5% from the setting in Table 156, “Register 0x45” [7:1]
- Source correction: Field header says [1:0] but the Bits column shows [0]; the Bits column is used.

| Code (bin) | Meaning |
|---|---|
| 0 | - 5% from the setting in Table 156, “Register 0x45” [7:1] |
| 1 | - 7.5% from the setting in Table 156, “Register 0x45” [7:1] |

**Notes**

- NOTE 1: PMIC guarantees efficiency spec and all electrical characteristics spec within a range of 1050 mV to 1160 mV.
- NOTE 2: Table 168, “Register 0x51” [5] = ‘0’; 5 mV step size.
- NOTE 3: Table 168, “Register 0x51” [5] = ‘1’; 5 mV step size.

## R46 (0x46) — SWA_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING, SWA_OVER_VOLTAGE_THRESHOLD_SETTING, SWA_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING, SWA_OUTPUT_SOFT_STOP_TIME

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-1A.03 Table 157, p.173

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWA_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING | RWPE | 01 |
| 5:4 | SWA_OVER_VOLTAGE_THRESHOLD_SETTING | RWPE | 10 |
| 3:2 | SWA_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING | RWPE | 00 |
| 1:0 | SWA_OUTPUT_SOFT_STOP_TIME | RWPE | 00 |

### [7:6] SWA_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING

- Description: Switch Node A Output Threshold High Side Voltage For Power Good Status
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 01 → +7.5% from the setting in Table 156, “Register 0x45” [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +5% from the setting in Table 156, “Register 0x45” [7:1] |
| 01 | +7.5% from the setting in Table 156, “Register 0x45” [7:1] |
| 10 | +10% from the setting in Table 156, “Register 0x45” [7:1] |
| 11 | Reserved |

### [5:4] SWA_OVER_VOLTAGE_THRESHOLD_SETTING

- Description: Switch Node A Output Regulator Threshold For Over Voltage Status[1]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 10 → +12.5% from the setting in Table 156, “Register 0x45” [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +7.5% from the setting in Table 156, “Register 0x45” [7:1] |
| 01 | +10% from the setting in Table 156, “Register 0x45” [7:1] |
| 10 | +12.5% from the setting in Table 156, “Register 0x45” [7:1] |
| 11 | Reserved |

### [3:2] SWA_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING

- Description: Switch Node A Output Regulator Threshold For Under Voltage Lockout Status
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 00 → -10% from the setting in Table 156, “Register 0x45” [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | -10% from the setting in Table 156, “Register 0x45” [7:1] |
| 01 | -12.5% from the setting in Table 156, “Register 0x45” [7:1] |
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

- NOTE 1: The setting for the Over Voltage must be higher than Power Good High Side Voltage threshold in Table 157, “Register 0x46”[7:6].
- NOTE 2: This is the time it takes for buck regulator to go from steady state voltage to 0 V.

## R47 (0x47) — SWB_VOLTAGE_SETTING, SWB_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-1A.03 Table 158, p.174

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
- Default: 0 → -5% from the setting in Table 158, “Register 0x47” [7:1]
- Source correction: Field header says [1] but the Bits column shows [0]; the Bits column is used.

| Code (bin) | Meaning |
|---|---|
| 0 | -5% from the setting in Table 158, “Register 0x47” [7:1] |
| 1 | -7.5% from the setting in Table 158, “Register 0x47” [7:1] |

**Notes**

- NOTE 1: Only applicable if Table 166, “Register 0x4F” [0] = ‘0’.
- NOTE 2: PMIC guarantees efficiency spec and all electrical characteristics spec within a range of 1050 mV to 1160 mV.
- NOTE 3: Table 168, “Register 0x51” [4] = ‘0’; 5 mV step size.
- NOTE 4: Table 168, “Register 0x51” [4] = ‘1’; 5 mV step size.

## R48 (0x48) — SWB_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING, SWB_OVER_VOLTAGE_THRESHOLD_SETTING, SWB_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING, SWB_OUTPUT_SOFT_STOP_TIME

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-1A.03 Table 159, p.175

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWB_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING | RWPE | 01 |
| 5:4 | SWB_OVER_VOLTAGE_THRESHOLD_SETTING | RWPE | 10 |
| 3:2 | SWB_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING | RWPE | 00 |
| 1:0 | SWB_OUTPUT_SOFT_STOP_TIME | RWPE | 00 |

### [7:6] SWB_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING

- Description: SWB Output Threshold High Side Voltage For Power Good Status
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 01 → +7.5% from the setting in Table 158, “Register 0x47” [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +5% from the setting in Table 158, “Register 0x47” [7:1] |
| 01 | +7.5% from the setting in Table 158, “Register 0x47” [7:1] |
| 10 | +10% from the setting in Table 158, “Register 0x47” [7:1] |
| 11 | Reserved |

### [5:4] SWB_OVER_VOLTAGE_THRESHOLD_SETTING

- Description: SWB Output Regulator Threshold For Over Voltage Status[2]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 10 → +12.5% from the setting in Table 158, “Register 0x47” [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +7.5% from the setting in Table 158, “Register 0x47” [7:1] |
| 01 | +10% from the setting in Table 158, “Register 0x47” [7:1] |
| 10 | +12.5% from the setting in Table 158, “Register 0x47” [7:1] |
| 11 | Reserved |

### [3:2] SWB_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING

- Description: SWB Output Regulator Threshold For Under Voltage Lockout Status
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 00 → -10% from the setting in Table 158, “Register 0x47” [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | -10% from the setting in Table 158, “Register 0x47” [7:1] |
| 01 | -12.5% from the setting in Table 158, “Register 0x47” [7:1] |
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

- NOTE 1: Only applicable if Table 166, “Register 0x4F” [0] = ‘0’.
- NOTE 2: The setting for the Over Voltage must be higher than Power Good High Side Voltage threshold in Table 159, “Register 0x48”[7:6].
- NOTE 3: This is the time it takes for buck regulator to go from steady state voltage to 0 V.

## R49 (0x49) — SWC_VOLTAGE_SETTING, SWC_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-1A.03 Table 160, p.176

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:1 | SWC_VOLTAGE_SETTING | RWPE | 011 1100 |
| 0 | SWC_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING | RWPE | 0 |

### [7:1] SWC_VOLTAGE_SETTING

- Description: SWC Output Regulator Voltage Setting[1]
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

### [0] SWC_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

- Description: Switch Node C Output Threshold Low Side Voltage For Power Good Status
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → -5% from the setting in Table 160, “Register 0x49” [7:1]

| Code (bin) | Meaning |
|---|---|
| 0 | -5% from the setting in Table 160, “Register 0x49” [7:1] |
| 1 | -7.5 from the setting in Table 160, “Register 0x49” [7:1] |

**Notes**

- NOTE 1: PMIC guarantees efficiency spec and all electrical characteristics spec within a range of 1050 mV to 1160 mV.
- NOTE 2: Table 168, “Register 0x51” [3] = ‘0’; 5 mV step size.
- NOTE 3: Table 168, “Register 0x51” [3] = ‘1’; 5 mV step size.

## R4A (0x4A) — SWC_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING, SWC_OVER_VOLTAGE_THRESHOLD_SETTING, SWC_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING, SWC_OUTPUT_SOFT_STOP_TIME

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-1A.03 Table 161, p.177

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWC_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING | RWPE | 01 |
| 5:4 | SWC_OVER_VOLTAGE_THRESHOLD_SETTING | RWPE | 10 |
| 3:2 | SWC_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING | RWPE | 00 |
| 1:0 | SWC_OUTPUT_SOFT_STOP_TIME | RWPE | 00 |

### [7:6] SWC_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING

- Description: SWC Output Threshold High Side Voltage For Power Good Status
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 01 → +7.5% from the setting in Table 160, “Register 0x49” [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +5% from the setting in Table 160, “Register 0x49” [7:1] |
| 01 | +7.5% from the setting in Table 160, “Register 0x49” [7:1] |
| 10 | +10% from the setting in Table 160, “Register 0x49” [7:1] |
| 11 | Reserved |

### [5:4] SWC_OVER_VOLTAGE_THRESHOLD_SETTING

- Description: SWC Output Regulator Threshold For Over Voltage Status[1]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 10 → +12.5% from the setting in Table 160, “Register 0x49” [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +7.5% from the setting in Table 160, “Register 0x49” [7:1] |
| 01 | +10% from the setting in Table 160, “Register 0x49” [7:1] |
| 10 | +12.5% from the setting in Table 160, “Register 0x49” [7:1] |
| 11 | Reserved |

### [3:2] SWC_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING

- Description: SWC Output Regulator Threshold For Under Voltage Lockout Status
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 00 → -10% from the setting in Table 160, “Register 0x49” [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | -10% from the setting in Table 160, “Register 0x49” [7:1] |
| 01 | -12.5% from the setting in Table 160, “Register 0x49” [7:1] |
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

- NOTE 1: The setting for the Over Voltage must be higher than Power Good High Side Voltage threshold in Table 161, “Register 0x4A”[7:6].
- NOTE 2: This is the time it takes for buck regulator to go from steady state voltage to 0 V.

## R4B (0x4B) — SWD_VOLTAGE_SETTING, SWD_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-1A.03 Table 162, p.178

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
- Default: 0 → -5% from the setting in Table 162, “Register 0x4B” [7:1]

| Code (bin) | Meaning |
|---|---|
| 0 | -5% from the setting in Table 162, “Register 0x4B” [7:1] |
| 1 | -7.5% from the setting in Table 162, “Register 0x4B” [7:1] |

**Notes**

- NOTE 1: PMIC guarantees efficiency spec and all electrical characteristics spec within a range of 1750 mV to 1850 mV.
- NOTE 2: Table 168, “Register 0x51” [0] = ‘0’; 5 mV step size.
- NOTE 3: Table 168, “Register 0x51” [0] = ‘1’; 5 mV step size.

## R4C (0x4C) — SWD_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING, SWD_OVER_VOLTAGE_THRESHOLD_SETTING, SWD_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING, SWD_OUTPUT_SOFT_STOP_TIME

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-1A.03 Table 163, p.179

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWD_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING | RWPE | 01 |
| 5:4 | SWD_OVER_VOLTAGE_THRESHOLD_SETTING | RWPE | 10 |
| 3:2 | SWD_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING | RWPE | 00 |
| 1:0 | SWD_OUTPUT_SOFT_STOP_TIME | RWPE | 00 |

### [7:6] SWD_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING

- Description: SWD Output Threshold High Side Voltage For Power Good Status
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 01 → +7.5% from the setting in Table 162, “Register 0x4B” [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +5% from the setting in Table 162, “Register 0x4B” [7:1] |
| 01 | +7.5% from the setting in Table 162, “Register 0x4B” [7:1] |
| 10 | Reserved |
| 11 | Reserved |

### [5:4] SWD_OVER_VOLTAGE_THRESHOLD_SETTING

- Description: SWD Output Regulator Threshold For Over Voltage Status[1]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 10 → +12.5% from the setting in Table 162, “Register 0x4B” [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +7.5% from the setting in Table 162, “Register 0x4B” [7:1] |
| 01 | +10% from the setting in Table 162, “Register 0x4B” [7:1] |
| 10 | +12.5% from the setting in Table 162, “Register 0x4B” [7:1] |
| 11 | Reserved |

### [3:2] SWD_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING

- Description: SWD Output Regulator Threshold For Under Voltage Lockout Status
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 00 → -10% from the setting in Table 162, “Register 0x4B” [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | -10% from the setting in Table 162, “Register 0x4B” [7:1] |
| 01 | -12.5% from the setting in Table 162, “Register 0x4B” [7:1] |
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

- NOTE 1: The setting for the Over Voltage must be higher than Power Good High Side Voltage threshold in Table 163, “Register 0x4C”[7:6].
- NOTE 2: This is the time it takes for buck regulator to go from steady state voltage to 0 V.

## R4D (0x4D) — SWA_MODE_SELECT, SWA_SWITCHING_FREQ, SWB_MODE_SELECT, SWB_SWITCHING_FREQ

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-1A.03 Table 164, p.180

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
| 10 | 1000 KHz |
| 11 | 1250 KHz |

### [3:2] SWB_MODE_SELECT

- Description: Switch Node B Output Regulator Mode Selection[1]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 10 → COT; DCM (Constant on Time; Discontinuous Current Mode)
- Source correction: Field header says [1:0] but the Bits column shows [3:2]; the Bits column is used.

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
| 10 | 1000 KHz |
| 11 | 1250 KHz |

**Notes**

- NOTE 1: Only applicable if Table 166, “Register 0x4F” [0] = ‘0’.

## R4E (0x4E) — SWC_MODE_SELECT, SWC_SWITCHING_FREQ, SWD_MODE_SELECT, SWD_SWITCHING_FREQ

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-1A.03 Table 165, p.181

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
| 10 | 1000 KHz |
| 11 | 1250 KHz |

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
| 00 | 500 KHz |
| 01 | 750 KHz |
| 10 | 1000 KHz |
| 11 | 1250 KHz |

## R4F (0x4F) — OUTPUT_REGULAOTRS_DISABLE_CONTROL1, SWA_OUTPUT_REGULATOR_REMOTE_SENSING, SWC_OUTPUT_REGULATOR_REMOTE_SENSING, SWD_OUTPUT_REGULATOR_REMOTE_SENSING, SWA_SWB_PHASE_MODE_SELECT

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-1A.03 Table 166, p.182

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | OUTPUT_REGULAOTRS_DISABLE_CONTROL1 | RWPE | 0 |
| 6:5 | RESERVED | RWPE | 0 |
| 4 | SWA_OUTPUT_REGULATOR_REMOTE_SENSING | RWPE | 0 |
| 3 | RESERVED | RV | 0 |
| 2 | SWC_OUTPUT_REGULATOR_REMOTE_SENSING | RWPE | 0 |
| 1 | SWD_OUTPUT_REGULATOR_REMOTE_SENSING | RWPE | 0 |
| 0 | SWA_SWB_PHASE_MODE_SELECT | RWPE | 0 |

### [7] OUTPUT_REGULAOTRS_DISABLE_CONTROL1

- Description: Output Regulator SWA, SWB, SWC and SWD Disable Control for OV and UV.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Disable all switching regulators of PMIC2

| Code (bin) | Meaning |
|---|---|
| 0 | Disable all switching regulators of PMIC2 |
| 1 | Disable only the affected switching output regulator; Rest of the PMIC’s switching regulators remains operations[3] |

### [6:5] RESERVED

- Description: Reserved
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0

### [4] SWA_OUTPUT_REGULATOR_REMOTE_SENSING

- Description: SWA Output Regulator Remote Sensing Scheme on DIMM
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Single Ended Remote Sensing on DIMM.1 = Differential Remote Sensing on DIMM

| Code (bin) | Meaning |
|---|---|
| 0 | Single Ended Remote Sensing on DIMM.1 = Differential Remote Sensing on DIMM |

### [3] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [2] SWC_OUTPUT_REGULATOR_REMOTE_SENSING

- Description: SWC Output Regulator Remote Sensing Scheme on DIMM
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Single Ended Remote Sensing on DIMM.

| Code (bin) | Meaning |
|---|---|
| 0 | Single Ended Remote Sensing on DIMM. |
| 1 | Differential Remote Sensing on DIMM |

### [1] SWD_OUTPUT_REGULATOR_REMOTE_SENSING

- Description: SWD Output Regulator Remote Sensing Scheme on DIMM
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Single Ended Remote Sensing on DIMM; Use SWD_FB_N pin as PID input pin to determine the PMIC’s ID4

| Code (bin) | Meaning |
|---|---|
| 0 | Single Ended Remote Sensing on DIMM; Use SWD_FB_N pin as PID input pin to determine the PMIC’s ID4 |
| 1 | Differential Remote Sensing on DIMM5 |

### [0] SWA_SWB_PHASE_MODE_SELECT

- Description: Switch Node A and Switch Node B Phase Regulator Mode Selection.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Single Phase Regulator Mode

| Code (bin) | Meaning |
|---|---|
| 0 | Single Phase Regulator Mode |
| 1 | Dual Phase Regulator Mode |

**Notes**

- NOTE 1: Applicable to Output Over Voltage and Output Under Voltage. For VIN_Bulk input over voltage or VBIAS under voltage or VIN_Bulk Input under voltage, this bit does not apply and the PMIC always disables all switching regulators.
- NOTE 2: For standard DDR5 RDIMM and DDR5 LRDIMM, this bit must be always configured to ‘0’.
- NOTE 3: For DDR5 NVDIMM or any other custom DIMM, this bit can be configured to either ‘0’ or ‘1’ as desired. This is applicable only after VR_ENABLE bit is set to ‘1’. Prior to VR_ENABLE bit is set to ‘1’, PMIC keeps all buck regulator off.
- NOTE 4: Up to three different PMIC can be placed on DIMM module.
- NOTE 5: Only one PMIC can be placed on DIMM module.

## R50 (0x50) — SWA_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING, SWB_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING, SWC_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING, SWD_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-1A.03 Table 167, p.183

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWA_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING | RWPE | 0 |
| 5:4 | SWB_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING | RWPE | 0 |
| 3:2 | SWC_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING | RWPE | 0 |
| 1:0 | SWD_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING | RWPE | 0 |

### [7:6] SWA_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING

- Description: PMIC5000 COT Mode, Ivalley_limit:
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0

**When: PMIC5000 COT Mode, Ivalley_limit:**

| Code (bin) | Meaning |
|---|---|
| 00 | 4.0 A |
| 01 | 4.5 A |
| 10 | 5.0 A |
| 11 | 5.5 A |

**When: PMIC5010 COT Mode, Ivalley_limit:**

| Code (bin) | Meaning |
|---|---|
| 00 | 2.0 A |
| 01 | 2.5 A |
| 10 | 3.0 A |
| 11 | 3.5 A |

### [5:4] SWB_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING

- Description: PMIC5000 COT Mode, Ivalley_limit[1]:
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0

**When: PMIC5000 COT Mode, Ivalley_limit[1]:**

| Code (bin) | Meaning |
|---|---|
| 00 | 4.0 A |
| 01 | 4.5 A |
| 10 | 5.0 A |
| 11 | 5.5 A |

**When: PMIC5010 COT Mode, Ivalley_limit:**

| Code (bin) | Meaning |
|---|---|
| 00 | 2.0 A |
| 01 | 2.5 A |
| 10 | 3.0 A |
| 11 | 3.5 A |

### [3:2] SWC_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING

- Description: PMIC5000 COT Mode, Ivalley_limit:
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0

**When: PMIC5000 COT Mode, Ivalley_limit:**

| Code (bin) | Meaning |
|---|---|
| 00 | 4.0 A |
| 01 | 4.5 A |
| 10 | 5.0 A |
| 11 | 5.5 A |

**When: PMIC5010 COT Mode, Ivalley_limit:**

| Code (bin) | Meaning |
|---|---|
| 00 | 2.0 A |
| 01 | 2.5 A |
| 10 | 3.0 A |
| 11 | 3.5 A |

### [1:0] SWD_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING

- Description: PMIC5000 COT Mode, Ivalley_limit:
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0

**When: PMIC5000 COT Mode, Ivalley_limit:**

| Code (bin) | Meaning |
|---|---|
| 00 | 4.0 A |
| 01 | 4.5 A |
| 10 | 5.0 A |
| 11 | 5.5 A |

**When: PMIC5010 COT Mode, Ivalley_limit:**

| Code (bin) | Meaning |
|---|---|
| 00 | 2.0 A |
| 01 | 2.5 A |
| 10 | 3.0 A |
| 11 | 3.5 A |

**Notes**

- NOTE 1: This register is applicable regardless of the setting in Table 166, “Register 0x4F” [0].

## R51 (0x51) — VOUT_1.8V_VOLTAGE_SETTING, SWA_VOLTAGE_RANGE, SWB_VOLTAGE_RANGE, SWC_VOLTAGE_RANGE, VOUT_1.0V_VOLTAGE_SETTING, SWD_VOLTAGE_RANGE

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-1A.03 Table 168, p.185

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

- Description: SWC Output Voltage Range Selection[5]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Range: 800 mV to 1435 mV for SWC; 5 mV step size

| Code (bin) | Meaning |
|---|---|
| 0 | Range: 800 mV to 1435 mV for SWC; 5 mV step size |
| 1 | Range: 600 mV to 1235 mV for SWC; 5 mV step size |

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

- NOTE 1: The VOUT_1.8V Power Good threshold in register Table 116, “Register 0x1A” [2] is always fixed regardless of the setting in this register.
- NOTE 2: Range and resolution selection applies to registers Table 156, “Register 0x45” [7:1].
- NOTE 3: Range and resolution selection applies to registers Table 158, “Register 0x47” [7:1].
- NOTE 4: Only applicable if Table 166, “Register 0x4F” [0] = ‘0’.
- NOTE 5: Range and resolution selection applies to registers Table 160, “Register 0x49” [7:1].
- NOTE 6: Range and resolution selection applies to registers Table 162, “Register 0x4B” [7:1].

## R58 (0x58) — POWER_OFF_SEQUENCE_CONFIG0, POWER_OFF_SEQUENCE_CONFIG0_SWA_DISABLE, POWER_OFF_SEQUENCE_CONFIG0_SWB_DISABLE, POWER_OFF_SEQUENCE_CONFIG0_SWC_DISABLE, POWER_OFF_SEQUENCE_CONFIG0_SWD_DISABLE, POWER_OFF_SEQUENCE_CONFIG0_IDLE

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-1A.03 Table 169, p.186

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | POWER_OFF_SEQUENCE_CONFIG0 | RWPE | 0 |
| 6 | POWER_OFF_SEQUENCE_CONFIG0_SWA_DISABLE | RWPE | 0 |
| 5 | POWER_OFF_SEQUENCE_CONFIG0_SWB_DISABLE | RWPE | 0 |
| 4 | POWER_OFF_SEQUENCE_CONFIG0_SWC_DISABLE | RWPE | 0 |
| 3 | POWER_OFF_SEQUENCE_CONFIG0_SWD_DISABLE | RWPE | 0 |
| 2:0 | POWER_OFF_SEQUENCE_CONFIG0_IDLE | RWPE | 0 |

### [7] POWER_OFF_SEQUENCE_CONFIG0

- Description: PMIC Power Off Sequence Config 0
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Do Not Execute Config 02

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Execute Config 02 |
| 1 | Execute Config 0 |

### [6] POWER_OFF_SEQUENCE_CONFIG0_SWA_DISABLE

- Description: Disable SWA Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Do Not Disable SWA Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Disable SWA Output Regulator |
| 1 | Disable SWA Output Regulator |

### [5] POWER_OFF_SEQUENCE_CONFIG0_SWB_DISABLE

- Description: Disable Switch Node B Output Regulator.[3]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Do Not Disable SWB Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Disable SWB Output Regulator |
| 1 | Disable SWB Output Regulator |

### [4] POWER_OFF_SEQUENCE_CONFIG0_SWC_DISABLE

- Description: Disable Switch Node C Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Do Not Disable SWC Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Disable SWC Output Regulator |
| 1 | Disable SWC Output Regulator |

### [3] POWER_OFF_SEQUENCE_CONFIG0_SWD_DISABLE

- Description: Disable SWD Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Do Not Disable SWD Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Disable SWD Output Regulator |
| 1 | Disable SWD Output Regulator |

### [2:0] POWER_OFF_SEQUENCE_CONFIG0_IDLE

- Description: Idle time after Power Off Sequence Config 04
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

- NOTE 1: If more than one configuration register is used for power off sequence, first register must start at Table 169, “Register 0x58” and it must go in sequential order to Table 172, “Register 0x5B” to turn off all regulators. In other words, there must not be any gap of the register that is used for power off sequence.
- NOTE 2: If bit [7] = ‘0’, bits [6:3] must be programmed as ‘0000’.If bit [7] = ‘1’, at least one of the bits [6:3] must be programmed as ‘1’.
- NOTE 3: Only applicable if Table 166, “Register 0x4F” [0] = ‘0’.
- NOTE 4: Idle time is the additional time after soft-stop time expires. The PMIC waits sum of soft stop time and idle time before it executes the next power off sequence configuration register. If more than one regulators are disabled, the PMIC uses the largest value of the soft stop time among the regulators that are disabled in this configuration register.

## R59 (0x59) — POWER_OFF_SEQUENCE_CONFIG1, POWER_OFF_SEQUENCE_CONFIG1_SWA_DISABLE, POWER_OFF_SEQUENCE_CONFIG1_SWB_DISABLE, POWER_OFF_SEQUENCE_CONFIG1_SWC_DISABLE, POWER_OFF_SEQUENCE_CONFIG1_SWD_DISABLE, POWER_OFF_SEQUENCE_CONFIG1_IDLE

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-1A.03 Table 170, p.187

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
- Default: 0 → Do Not Disable SWA Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Disable SWA Output Regulator |
| 1 | Disable SWA Output Regulator |

### [5] POWER_OFF_SEQUENCE_CONFIG1_SWB_DISABLE

- Description: Disable Switch Node B Output Regulator.[4]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Do Not Disable SWB Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Disable SWB Output Regulator |
| 1 | Disable SWB Output Regulator |

### [4] POWER_OFF_SEQUENCE_CONFIG1_SWC_DISABLE

- Description: Disable Switch Node C Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Do Not Disable SWC Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Disable SWC Output Regulator |
| 1 | Disable SWC Output Regulator |

### [3] POWER_OFF_SEQUENCE_CONFIG1_SWD_DISABLE

- Description: Disable Switch Node D Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Do Not Disable SWD Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Disable SWD Output Regulator |
| 1 | Disable SWD Output Regulator |

### [2:0] POWER_OFF_SEQUENCE_CONFIG1_IDLE

- Description: Idle time after Power Off Sequence Config 15
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

- NOTE 1: If any regulators are disabled in Table 169, “Register 0x58” [6:3], those regulators must be configured as ‘1’ in this sequence.
- NOTE 2: If more than one configuration register is used for power off sequence, first register must start at Table 169, “Register 0x58” and it must go in sequential order to Table 172, “Register 0x5B” to turn off all regulators. In other words, there must not be any gap of the register that is used for power off sequence.
- NOTE 3: If bit [7] = ‘0’, bits [6:3] must be programmed as ‘0000’.If bit [7] = ‘1’, at least one of the bits [6:3] must be programmed as ‘1’.
- NOTE 4: Only applicable if Table 166, “Register 0x4F” [0] = ‘0’.
- NOTE 5: Idle time is the additional time after soft-stop time expires. The PMIC waits sum of soft stop time and idle time before it executes the next power off sequence configuration register. If more than one regulators are disabled, the PMIC uses the largest value of the soft stop time among the regulators that are disabled in this configuration register.

## R5A (0x5A) — POWER_OFF_SEQUENCE_CONFIG2, POWER_OFF_SEQUENCE_CONFIG2_SWA_DISABLE, POWER_OFF_SEQUENCE_CONFIG2_SWB_DISABLE, POWER_OFF_SEQUENCE_CONFIG2_SWC_DISABLE, POWER_OFF_SEQUENCE_CONFIG2_SWD_DISABLE, POWER_OFF_SEQUENCE_CONFIG2_IDLE

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-1A.03 Table 171, p.188

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | POWER_OFF_SEQUENCE_CONFIG2 | RWPE | 0 |
| 6 | POWER_OFF_SEQUENCE_CONFIG2_SWA_DISABLE | RWPE | 0 |
| 5 | POWER_OFF_SEQUENCE_CONFIG2_SWB_DISABLE | RWPE | 0 |
| 4 | POWER_OFF_SEQUENCE_CONFIG2_SWC_DISABLE | RWPE | 0 |
| 3 | POWER_OFF_SEQUENCE_CONFIG2_SWD_DISABLE | RWPE | 0 |
| 2:0 | POWER_OFF_SEQUENCE_CONFIG2_IDLE | RWPE | 0 |

### [7] POWER_OFF_SEQUENCE_CONFIG2

- Description: PMIC Power Off Sequence Config 23
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Do Not Execute Config 2

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Execute Config 2 |
| 1 | Execute Config 2 |

### [6] POWER_OFF_SEQUENCE_CONFIG2_SWA_DISABLE

- Description: Disable SWA Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Do Not Disable SWA Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Disable SWA Output Regulator |
| 1 | Disable SWA Output Regulator |

### [5] POWER_OFF_SEQUENCE_CONFIG2_SWB_DISABLE

- Description: Disable Switch Node B Output Regulator.[4]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Do Not Disable SWB Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Disable SWB Output Regulator |
| 1 | Disable SWB Output Regulator |

### [4] POWER_OFF_SEQUENCE_CONFIG2_SWC_DISABLE

- Description: Disable Switch Node C Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Do Not Disable SWC Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Disable SWC Output Regulator |
| 1 | Disable SWC Output Regulator |

### [3] POWER_OFF_SEQUENCE_CONFIG2_SWD_DISABLE

- Description: Disable Switch Node D Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Do Not Disable SWD Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Disable SWD Output Regulator |
| 1 | Disable SWD Output Regulator |

### [2:0] POWER_OFF_SEQUENCE_CONFIG2_IDLE

- Description: Idle time after Power Off Sequence Config 25
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

- NOTE 1: If any regulators are disabled in Table 169, “Register 0x58” [6:3], and Table 170, “Register 0x59” [6:3] those regulators must be configured as ‘1’ in this sequence.
- NOTE 2: If more than one configuration register is used for power off sequence, first register must start at Table 169, “Register 0x58” and it must go in sequential order to Table 172, “Register 0x5B” to turn off all regulators. In other words, there must not be any gap of the register that is used for power off sequence.
- NOTE 3: If bit [7] = ‘0’, bits [6:3] must be programmed as ‘0000’.If bit [7] = ‘1’, at least one of the bits [6:3] must be programmed as ‘1’.
- NOTE 4: Only applicable if Table 166, “Register 0x4F” [0] = ‘0’.
- NOTE 5: Idle time is the additional time after soft-stop time expires. The PMIC waits sum of soft stop time and idle time before it executes the next power off sequence configuration register. If more than one regulators are disabled, the PMIC uses the largest value of the soft stop time among the regulators that are disabled in this configuration register.

## R5B (0x5B) — POWER_OFF_SEQUENCE_CONFIG3, POWER_OFF_SEQUENCE_CONFIG3_SWA_DISABLE, POWER_OFF_SEQUENCE_CONFIG3_SWB_DISABLE, POWER_OFF_SEQUENCE_CONFIG3_SWC_DISABLE, POWER_OFF_SEQUENCE_CONFIG3_SWD_DISABLE

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-1A.03 Table 172, p.189

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | POWER_OFF_SEQUENCE_CONFIG3 | RWPE | 0 |
| 6 | POWER_OFF_SEQUENCE_CONFIG3_SWA_DISABLE | RWPE | 0 |
| 5 | POWER_OFF_SEQUENCE_CONFIG3_SWB_DISABLE | RWPE | 0 |
| 4 | POWER_OFF_SEQUENCE_CONFIG3_SWC_DISABLE | RWPE | 0 |
| 3 | POWER_OFF_SEQUENCE_CONFIG3_SWD_DISABLE | RWPE | 0 |
| 2:0 | RESERVED | RV | 0 |

### [7] POWER_OFF_SEQUENCE_CONFIG3

- Description: PMIC Power Off Sequence Config 33
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Do Not Execute Config 3

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Execute Config 3 |
| 1 | Execute Config 3 |

### [6] POWER_OFF_SEQUENCE_CONFIG3_SWA_DISABLE

- Description: Disable SWA Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Do Not Disable SWA Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Disable SWA Output Regulator |
| 1 | Disable SWA Output Regulator |

### [5] POWER_OFF_SEQUENCE_CONFIG3_SWB_DISABLE

- Description: Disable SWB Output Regulator.[4]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Do Not Disable SWB Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Disable SWB Output Regulator |
| 1 | Disable SWB Output Regulator |

### [4] POWER_OFF_SEQUENCE_CONFIG3_SWC_DISABLE

- Description: Disable Switch Node C Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Do Not Disable SWC Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Disable SWC Output Regulator |
| 1 | Disable SWC Output Regulator |

### [3] POWER_OFF_SEQUENCE_CONFIG3_SWD_DISABLE

- Description: Disable Switch Node D Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Do Not Disable SWD Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Disable SWD Output Regulator |
| 1 | Disable SWD Output Regulator |

### [2:0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

**Notes**

- NOTE 1: If any regulators are disabled in Table 169, “Register 0x58” [6:3], Table 170, “Register 0x59” [6:3] and Table 171, “Register 0x5A” [6:3], those regulators must be configured as ‘1’ in this sequence.
- NOTE 2: If more than one configuration register is used for power off sequence, first register must start at Table 169, “Register 0x58” and it must go in sequential order to Table 172, “Register 0x5B” to turn off all regulators. In other words, there must not be any gap of the register that is used for power off sequence.
- NOTE 3: If bit [7] = ‘0’, bits [6:3] must be programmed as ‘0000’.If bit [7] = ‘1’, at least one of the bits [6:3] must be programmed as ‘1’.
- NOTE 4: Only applicable if Table 166, “Register 0x4F” [0] = ‘0’.

## R5D (0x5D) — SWA_OUTPUT_SOFT_START_TIME, SWB_OUTPUT_SOFT_START_TIME

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-1A.03 Table 173, p.190

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
- NOTE 2: Only applicable if Table 166, “Register 0x4F” [0] = ‘0’.

## R5E (0x5E) — SWC_OUTPUT_SOFT_START_TIME, SWD_OUTPUT_SOFT_START_TIME

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-1A.03 Table 174, p.190

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

- NOTE 1: This is the time it takes for buck regulator to go from 0 V to steady state voltage (the actual voltage varies based on pre-programmed voltage) Annex A (Informative) - Differences between Revisions A.1 Differences between JESD301-1A and JESD301-1 (June 2020) Release Version                                                         Changes Date Rev 1.3   August 20   Clause 1.9.2: Wording clarification. 2020      Table 94 to Table 97: Updated program and erase time values. Table 143: Deleted first statement in footnote 5 for clarification. Table 18: Updated Ron min value. Clause B.3.5.1: Added clarification. Table 100, Table 70: Added clarification. clause 1.8.8: Added description. Clause 1.8.5, 1.8.9, 1.8.10, 1.8.12, 1.8.14, 1.8.15: Updated with new definition. Table 22: Added note 1. Rev 1.4   October 1   Table 54. Table 72, Table 73: Deleted RSTDAA direct CCC. 2020      Table 21: Updated temperature spec to be compliant with JESD402-1. Table 15: Separated output slew rate value. Table 137: Updated bit [2] definition and associated footnote. Table 140: Updated bit [5:3] definition and associated footnotes. Table 93: Updated functional description. Clause 1.8.5: Deleted entire clause. Clause 1.8.7: Updated definition. Clause 1.8.9: Updated definition. Clause 1.8.1: Added clarification. Table 86: Updated CAMP pin description. Figure 11, Figure 12: Updated drawing for clarification. Clause 1.14.1: Updated definition. Global update: Re-labeled PWR_GOOD pin w/ CAMP; secure mode with write protect mode; programmable mode with non write protect mode Rev 1.5   October 3   Corrected typo. 2020      Clause : Corrected typo. Added clarification. Added cross reference. Added Hi-Z clarification. Clause: Editorial cleanup. Added missing transition A.1   Differences between JESD301-1A and JESD301-1 (June 2020) (cont’d) Version    Release Date                                      Changes Section Corrected typo Section Updated label Section Added cross reference; added cautionary statement. Added clarification Updated pin numbers to align with Rev 1.6   Oct. 15, 2020 Updated figure Section Added clarification Marked write protect register Section Added section about defective LDO failure behavior Added filter parameter for LDO outputs Added R32[5] definition. Updated mapping from R32[5] to R32[3] Section Rev 1.7   Oct. 17, 2020   Fixed typo Section Added clarification statement. Table 65, Table 66: Deleted Repeat Start condition. Table 100: Added additional clarification. Table 138: Added footnote 2 for clarification. Section 1.2.2: Editorial correction. Table 13: Editorial correction. Table 14: Editorial correction; deleted row Table 15: Editorial correction Section 1.8.1: Editorial correction. Rev 1.7a   Dec. 10, 2020   Section 1.8.2: Editorial correction. Section 1.8.10: Editorial correction. Section 1.8.7.3: Editorial correction. Section 1.8.11: Editorial correction. Table 166: Editorial correction. Table 26: Editorial correction in footnote. Table 117: Editorial correction. Table 142: Changed the register attribute definition and added notes. Figure 17: Added clarification. A.1        Differences between JESD301-1A and JESD301-1 (June 2020) (cont’d) Version        Release Date                                          Changes Rev 1.8        Dec. 18, 2020     Table 138: Updated footnote 2 delay value to 9 ms. Inclusive terminology updated throughout the document. Figure 18: Added inclusive terminology. Figure 19: Added inclusive terminology. Figure 20: Added inclusive terminology. Rev 1.8a        Feb. 2, 2021 Figure 21: Added inclusive terminology. Figure 22: Added inclusive terminology. Table 19 and notes 7,9,10: Added inclusive terminology. Clause 1.11.9: Added inclusive terminology. A.2 Differences between JESD301-1A.01 and JESD301-1A (August 2021) 1. Table 2: Updated Footnote 2 2. Table 86: Added NC pin definition A.3 Differences between JESD301-1A.02 and JESD301-1A.01 (October 2022) Editorial corrections as outlined in the following summary. Page                                                       Description 3       Table 2: Updated VIN_Bulk Ramp Down minimum value 12       Table 15: Corrected IOL/IOH minimum and maximum values, respectively 32       Clause 2.7.7.1: Added clarification 33/34       Clause 2.7.9: Added clarification 35       Table 27: Corrected typographical error 105      Table 92: Added missing register to the list 110      Clause 3.3.5: Added editorial explanation 111      Figure 33: Added 117      Table 99: Editorial re-wording of Footnote #3 128      Clause 3.3.5.3: Added missing register reference 134      Table 116: Editorial correction of the cross reference pointer 135      Table 117: Corrected typographical error in Footnote #3 A.4 Differences between JESD301-1A.03 and JESD301-1A.02 (March 2023) Editorial correction of the document title fromPMIC50x0 Power Management IC Standard to PMIC5000/PMIC5010 Power Management IC Standard. Standard Improvement Form                                            JEDEC Standard JESD301-1A.03 The purpose of this form is to provide the Technical Committees of JEDEC with input from the industry regarding usage of the subject standard. Individuals or companies are invited to submit comments to JEDEC. All comments will be collected and dispersed to the appropriate committee(s). If you can provide input, please complete this form and return to: JEDEC                                                 Email: angies@jedec.org Attn: Publications Department 3103 10th Street North Suite 240S Arlington, VA 22201 1. I recommend changes to the following: Requirement, clause number Test method number                       Clause number The referenced clause number has proven to be: Unclear          Too Rigid         In Error Other 2. Recommendations for correction: 3. Other suggestions for document improvement: Submitted by Name:                                                          Phone: Company:                                                       E-mail: Address: City/State/Zip:                                                Date:
