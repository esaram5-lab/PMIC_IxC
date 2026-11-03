# PMIC5200 Register Map Summary

Source: JESD301-3 — PMIC5200 Power Management IC Standard, Version 1.0 (October 2025). Application: client (LPDDR5 CAMM2).

Elided ranges ('...') follow the linear pattern of the neighbouring codes; see registers/<addr>.md for every value spelled out.

## R04 (0x04) — GLOBAL_ERROR_COUNT, GLOBAL_ERROR_LOG_BUCK_OV_OR_UV, GLOBAL_ERROR_LOG_VIN_BULK_OVER_VOLTAGE, GLOBAL_ERROR_LOG_CRITICAL_TEMPERATURE

Region: Host Region | Source: JESD301-3 Table 108, p.135

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | GLOBAL_ERROR_COUNT | ROE | 0 |
| 6 | GLOBAL_ERROR_LOG_BUCK_OV_OR_UV | ROE | 0 |
| 5 | GLOBAL_ERROR_LOG_VIN_BULK_OVER_VOLTAGE | ROE | 0 |
| 4 | GLOBAL_ERROR_LOG_CRITICAL_TEMPERATURE | ROE | 0 |
| 3:0 | RESERVED | RV | 0 |

### [7] GLOBAL_ERROR_COUNT

- Description: Global Error Count Since Last Erase Operation[4]
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0 → No Error or Only 1 Error since last Erase operation

| Code (bin) | Meaning |
|---|---|
| 0 | No Error or Only 1 Error since last Erase operation |
| 1 | > 1 Error Count since last Erase operation |

### [6] GLOBAL_ERROR_LOG_BUCK_OV_OR_UV

- Description: Global Error Log History for Buck Regulator Output Over or Under Voltage[5]
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0 → No Error Occurred

| Code (bin) | Meaning |
|---|---|
| 0 | No Error Occurred |
| 1 | Error Occurred |

### [5] GLOBAL_ERROR_LOG_VIN_BULK_OVER_VOLTAGE

- Description: Global Error Log History for VIN_Bulk Over Voltage4
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0 → No Error Occurred

| Code (bin) | Meaning |
|---|---|
| 0 | No Error Occurred |
| 1 | Error Occurred |

### [4] GLOBAL_ERROR_LOG_CRITICAL_TEMPERATURE

- Description: Global Error Log History for Critical Temperature4
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

- NOTE 1: The PMIC always attempts to write this register into its non-volatile memory. However, it may not be guaranteed depending on how fast the host may shut off the input power to the PMIC. The PMIC needs a minimum of 3.0 V for VIN_Bulk voltage and 200 ms duration from PWR_GOOD signal assertion to guarantee the write operation into non- volatile memory.
- NOTE 2: Host must explicitly perform Erase operation to erase this entire register via command in Table 161, Register 0x39. The PMIC needs minimum of 200 ms for Erase operation.
- NOTE 3: The error log registers are only updated when there is a VR Disable fault when the buck regulators are under regulation.
- NOTE 4: PMIC counts the error since last erase operation and if more than one error occurs, it sets this bit to ‘1’. Host must explicitly perform Erase operation to erase this entire register Table 108, Register 0x04 [7:0].
- NOTE 5: PMIC sets the bit when error occurs.

## R05 (0x05) — SWA_POWER_GOOD, (unnamed), SWB_POWER_GOOD, SWC_POWER_GOOD, PMIC_ERROR_LOG

Region: Host Region | Source: JESD301-3 Table 109, p.136

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | RESERVED | ROE | 0 |
| 6 | SWA_POWER_GOOD | ROE | 0 |
| 5 | (unnamed) | ROE | 0 |
| 4 | SWB_POWER_GOOD | ROE | 0 |
| 3 | SWC_POWER_GOOD | ROE | 0 |
| 2:0 | PMIC_ERROR_LOG | ROE | 0 |

### [7] RESERVED

- Description: R0 5 [7]: Reserved
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0

### [6] SWA_POWER_GOOD

- Description: PMIC Power On - SWA Power Not Good[4]
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0 → Normal Power On

| Code (bin) | Meaning |
|---|---|
| 0 | Normal Power On |
| 1 | Power On - SWA Power Not Good |

### [5] (unnamed)

- Description: PMIC Power On - SWD Power Not Good3
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0 → Normal Power On

| Code (bin) | Meaning |
|---|---|
| 0 | Normal Power On |
| 1 | Power On - SWD Power Not Good |

### [4] SWB_POWER_GOOD

- Description: PMIC Power On - SWB Power Not Good3
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0 → Normal Power On

| Code (bin) | Meaning |
|---|---|
| 0 | Normal Power On |
| 1 | Power On - SWB Power Not Good |

### [3] SWC_POWER_GOOD

- Description: PMIC Power On - SWC Power Not Good3
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0 → Normal Power On

| Code (bin) | Meaning |
|---|---|
| 0 | Normal Power On |
| 1 | Power On - SWC Power Not Good |

### [2:0] PMIC_ERROR_LOG

- Description: PMIC Power On - High Level Status Bit to Indicate Last Known Power Cycle or System Reset
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
| 111 | VIN_Bulk Input Under Voltage |

**Notes**

- NOTE 1: The PMIC always attempts to write this register into its non-volatile memory. However, it may not be guaranteed depending on how fast the host may shut off the input power to the PMIC. The PMIC needs minimum of 3.0 V for VIN_Bulk voltage and 200 ms duration from PWR_GOOD signal assertion to guarantee the write operation into non- volatile memory.
- NOTE 2: This entire register status reflects previous power down cycle of the PMIC and is updated by the PMIC on its own at each power cycle, if update is needed. Because this register is updated only if there is an update needed, there is no NVM life time impact. This register is cleared when host issues the erase command via Table 161, Register 0x39. The PMIC needs a minimum of 200 ms for Erase operation.
- NOTE 3: The error log registers are only updated when there is a VR Disable fault when the buck regulators are under regulation.
- NOTE 4: This register is set only if PMIC generates internal VR Disable command due to fault condition.
- NOTE 5: This code is a logical OR function of Table 110, Register 0x06 [7:0] register bits.

## R06 (0x06) — SWA_UNDER_VOLTAGE_LOCKOUT, SWD_UNDER_VOLTAGE_LOCKOUT, SWB_UNDER_VOLTAGE_LOCKOUT, SWC_UNDER_VOLTAGE_LOCKOUT, SWA_OVER_VOLTAGE, SWD_OVER_VOLTAGE, SWB_OVER_VOLTAGE, SWC_OVER_VOLTAGE

Region: Host Region | Source: JESD301-3 Table 110, p.137

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | SWA_UNDER_VOLTAGE_LOCKOUT | ROE | 0 |
| 6 | SWD_UNDER_VOLTAGE_LOCKOUT | ROE | 0 |
| 5 | SWB_UNDER_VOLTAGE_LOCKOUT | ROE | 0 |
| 4 | SWC_UNDER_VOLTAGE_LOCKOUT | ROE | 0 |
| 3 | SWA_OVER_VOLTAGE | ROE | 0 |
| 2 | SWD_OVER_VOLTAGE | ROE | 0 |
| 1 | SWB_OVER_VOLTAGE | ROE | 0 |
| 0 | SWC_OVER_VOLTAGE | ROE | 0 |

### [7] SWA_UNDER_VOLTAGE_LOCKOUT

- Description: PMIC Power On - SWA Under Voltage Lockout
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0 → Normal Power On

| Code (bin) | Meaning |
|---|---|
| 0 | Normal Power On |
| 1 | Power On - SWA Under Voltage Lockout |

### [6] SWD_UNDER_VOLTAGE_LOCKOUT

- Description: PMIC Power On - SWD Under Voltage Lockout
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0 → Normal Power On

| Code (bin) | Meaning |
|---|---|
| 0 | Normal Power On |
| 1 | Power On - SWD Under Voltage Lockout |

### [5] SWB_UNDER_VOLTAGE_LOCKOUT

- Description: PMIC Power On - SWB Under Voltage Lockout
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0 → Normal Power On

| Code (bin) | Meaning |
|---|---|
| 0 | Normal Power On |
| 1 | Power On - SWB Under Voltage Lockout |

### [4] SWC_UNDER_VOLTAGE_LOCKOUT

- Description: PMIC Power On - SWC Under Voltage Lockout
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0 → Normal Power On

| Code (bin) | Meaning |
|---|---|
| 0 | Normal Power On |
| 1 | Power On - SWC Under Voltage Lockout |

### [3] SWA_OVER_VOLTAGE

- Description: PMIC Power On - SWA Over Voltage
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0 → Normal Power On

| Code (bin) | Meaning |
|---|---|
| 0 | Normal Power On |
| 1 | Power On - SWA Over Voltage |

### [2] SWD_OVER_VOLTAGE

- Description: PMIC Power On - SWD Over Voltage
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0 → Normal Power On

| Code (bin) | Meaning |
|---|---|
| 0 | Normal Power On |
| 1 | Power On - SWD Over Voltage |

### [1] SWB_OVER_VOLTAGE

- Description: PMIC Power On - SWB Over Voltage
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0 → Normal Power On

| Code (bin) | Meaning |
|---|---|
| 0 | Normal Power On |
| 1 | Power On - SWB Over Voltage |

### [0] SWC_OVER_VOLTAGE

- Description: PMIC Power On - SWC Over Voltage
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0 → Normal Power On

| Code (bin) | Meaning |
|---|---|
| 0 | Normal Power On |
| 1 | Power On - SWC Over Voltage |

**Notes**

- NOTE 1: The PMIC always attempts to write this register into its non-volatile memory. However, it may not be guaranteed depending on how fast the host may shut off the input power to the PMIC. The PMIC needs minimum of 3.0 V for VIN_Bulk voltage and 200 ms duration from PWR_GOOD signal assertion to guarantee the write operation into non- volatile memory.
- NOTE 2: This entire register status reflects previous power down cycle of the PMIC and is updated by the PMIC on its own at each power cycle, if update is needed. Because this register is updated only if there is an update needed, there is no NVM life time impact. This register is cleared when host issues the erase command via Table 161, Register 0x39. The PMIC needs a minimum of 200 ms for Erase operation.
- NOTE 3: The error log registers are only updated when there is a VR Disable fault when the buck regulators are under regulation.

## R07 (0x07) — Reserved

Region: Host Region | Source: JESD301-3 Table 111, p.138

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | RESERVED | ROE | 0 |

### [7:0] RESERVED

- Description: Reserved
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0

**Notes**

- NOTE 1: The PMIC always attempts to write this register into its non-volatile memory. However, it may not be guaranteed depending on how fast the host may shut off the input power to the PMIC. The PMIC needs minimum of 3.0 V for VIN_Bulk voltage and 200 ms duration from PWR_GOOD signal assertion to guarantee the write operation into non- volatile memory.
- NOTE 2: This entire register status reflects previous power down cycle of the PMIC and is updated by the PMIC on its own at each power cycle, if update is needed. Because this register is updated only if there is an update needed, there is no NVM life time impact. This register is cleared when host issues the erase command via Table 161, Register 0x39. The PMIC needs a minimum of 200 ms for Erase operation.

## R08 (0x08) — VIN_BULK_INPUT_POWER_GOOD_STATUS, CRITICAL_TEMP_SHUTDOWN_STATUS, SWA_OUTPUT_POWER_GOOD_STATUS, SWD_OUTPUT_POWER_GOOD_STATUS, SWB_OUTPUT_POWER_GOOD_STATUS, SWC_OUTPUT_POWER_GOOD_STATUS, VIN_BULK_INPUT_OVER_VOLTAGE_STATUS

Region: Host Region | Source: JESD301-3 Table 112, p.139

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | VIN_BULK_INPUT_POWER_GOOD_STATUS | RO | 0 |
| 6 | CRITICAL_TEMP_SHUTDOWN_STATUS | RO | 0 |
| 5 | SWA_OUTPUT_POWER_GOOD_STATUS | RO | 0 |
| 4 | SWD_OUTPUT_POWER_GOOD_STATUS | RO | 0 |
| 3 | SWB_OUTPUT_POWER_GOOD_STATUS | RO | 0 |
| 2 | SWC_OUTPUT_POWER_GOOD_STATUS | RO | 0 |
| 1 | RESERVED | RV | 0 |
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

### [4] SWD_OUTPUT_POWER_GOOD_STATUS

- Description: Switch Node D Output Power Good Status[4]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → Power Good

| Code (bin) | Meaning |
|---|---|
| 0 | Power Good |
| 1 | Power Not Good |

### [3] SWB_OUTPUT_POWER_GOOD_STATUS

- Description: Switch Node B Output Power Good Status[5]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → Power Good

| Code (bin) | Meaning |
|---|---|
| 0 | Power Good |
| 1 | Power Not Good |

### [2] SWC_OUTPUT_POWER_GOOD_STATUS

- Description: Switch Node C Output Power Good Status[6]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → Power Good

| Code (bin) | Meaning |
|---|---|
| 0 | Power Good |
| 1 | Power Not Good |

### [1] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [0] VIN_BULK_INPUT_OVER_VOLTAGE_STATUS

- Description: VIN_Bulk Input Supply Over Voltage Status[7]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No Over Voltage

| Code (bin) | Meaning |
|---|---|
| 0 | No Over Voltage |
| 1 | Over Voltage |

**Notes**

- NOTE 1: This register is set when VIN_Bulk input goes below the threshold setting in register Table 130, Register 0x1A [7:6].
- NOTE 2: This register is set when PMIC temperature goes above the threshold setting in register Table 150, Register 0x2E [2:0].
- NOTE 3: This register is set when SWA output voltage goes either below the threshold setting in register Table 137, Register 0x21,[0] or above the threshold setting in register Table 138, Register 0x22, [7:6].
- NOTE 4: This register is set when SWD output goes either below the threshold setting in register Table 139, Register 0x23, [0] or above the threshold setting in register Table 140, Register 0x24 [7:6].
- NOTE 5: This register is set when SWB output goes either below the threshold setting in register Table 141, Register 0x25,[0] or above the threshold setting in register Table 142, Register 0x26, [7:6].
- NOTE 6: This register is set when SWC output goes either below the threshold setting in register Table 143, Register 0x27,[0] or above the threshold setting in register Table 144, Register 0x28, [7:6].
- NOTE 7: This register is set when VIN_Bulk input voltage goes above the threshold setting in register Table 131, Register 0x1B [7].

## R09 (0x09) — PMIC_HIGH_TEMP_WARNING_STATUS, VOUT_1.8V_OUTPUT_POWER_GOOD_STATUS, SWA_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS, SWD_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS, SWB_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS, SWC_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS

Region: Host Region | Source: JESD301-3 Table 113, p.140

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | PMIC_HIGH_TEMP_WARNING_STATUS | RO | 0 |
| 6 | RESERVED | RV | 0 |
| 5 | VOUT_1.8V_OUTPUT_POWER_GOOD_STATUS | RO | 0 |
| 4 | RESERVED | RV | 0 |
| 3 | SWA_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS | RO | 0 |
| 2 | SWD_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS | RO | 0 |
| 1 | SWB_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS | RO | 0 |
| 0 | SWC_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS | RO | 0 |

### [7] PMIC_HIGH_TEMP_WARNING_STATUS

- Description: PMIC High Temperature Warning Status[1]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → Temperature Below the Warning Threshold

| Code (bin) | Meaning |
|---|---|
| 0 | Temperature Below the Warning Threshold |
| 1 | Temperature Exceeded the Warning Threshold |

### [6] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [5] VOUT_1.8V_OUTPUT_POWER_GOOD_STATUS

- Description: VOUT_1.8V LDO Output Power Good Status[2]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → Power Good

| Code (bin) | Meaning |
|---|---|
| 0 | Power Good |
| 1 | Power Not Good |

### [4] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [3] SWA_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS

- Description: Switch Node A High Output Current Consumption Warning Status[3]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No High Current Consumption Warning

| Code (bin) | Meaning |
|---|---|
| 0 | No High Current Consumption Warning |
| 1 | High Current Consumption Warning |

### [2] SWD_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS

- Description: Switch Node D High Output Current Consumption Warning Status[4]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No High Current Consumption Warning

| Code (bin) | Meaning |
|---|---|
| 0 | No High Current Consumption Warning |
| 1 | High Current Consumption Warning |

### [1] SWB_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS

- Description: Switch Node B High Output Current Consumption Warning Status[5]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No High Current Consumption Warning

| Code (bin) | Meaning |
|---|---|
| 0 | No High Current Consumption Warning |
| 1 | High Current Consumption Warning |

### [0] SWC_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS

- Description: Switch Node C High Output Current Consumption Warning Status[6]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No High Current Consumption Warning

| Code (bin) | Meaning |
|---|---|
| 0 | No High Current Consumption Warning |
| 1 | High Current Consumption Warning |

**Notes**

- NOTE 1: This register is set when PMIC temperature goes above the threshold setting in Table 131, Register 0x1B [2:0].
- NOTE 2: This register is set when VOUT_1.8V output exceeds the threshold setting in register Table 130, Register 0x1A [2].
- NOTE 3: This register is set when SWA output current consumption goes above the threshold setting in Table 132, Register 0x1C [7:0].
- NOTE 4: This register is set when SWD output current consumption goes above the threshold setting in Table 133, Register 0x1D [7:0].
- NOTE 5: This register is set when SWB output current consumption goes above the threshold setting in Table 134, Register 0x1E [7:0].
- NOTE 6: This register is set when SWC output current consumption goes above the threshold setting in Table 135, Register 0x1F [7:0].

## R0A (0x0A) — SWA_OUTPUT_OVER_VOLTAGE_STATUS, SWD_OUTPUT_OVER_VOLTAGE_STATUS, SWB_OUTPUT_OVER_VOLTAGE_STATUS, SWC_OUTPUT_OVER_VOLTAGE_STATUS, PEC_ERROR_STATUS, PARITY_ERROR_STATUS, IBI_AND_GLOBAL_STATUS, DVFSQ_POWER_STATE_STATUS

Region: Host Region | Source: JESD301-3 Table 114, p.141

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | SWA_OUTPUT_OVER_VOLTAGE_STATUS | RO | 0 |
| 6 | SWD_OUTPUT_OVER_VOLTAGE_STATUS | RO | 0 |
| 5 | SWB_OUTPUT_OVER_VOLTAGE_STATUS | RO | 0 |
| 4 | SWC_OUTPUT_OVER_VOLTAGE_STATUS | RO | 0 |
| 3 | PEC_ERROR_STATUS | RO | 0 |
| 2 | PARITY_ERROR_STATUS | RO | 0 |
| 1 | IBI_AND_GLOBAL_STATUS | RO | 0 |
| 0 | DVFSQ_POWER_STATE_STATUS | RO | 0 |

### [7] SWA_OUTPUT_OVER_VOLTAGE_STATUS

- Description: Switch Node A Output Over Voltage Status[1]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No Over Voltage

| Code (bin) | Meaning |
|---|---|
| 0 | No Over Voltage |
| 1 | Over Voltage |

### [6] SWD_OUTPUT_OVER_VOLTAGE_STATUS

- Description: Switch Node D Output Over Voltage Status[2]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No Over Voltage

| Code (bin) | Meaning |
|---|---|
| 0 | No Over Voltage |
| 1 | Over Voltage |

### [5] SWB_OUTPUT_OVER_VOLTAGE_STATUS

- Description: Switch Node B Output Over Voltage Status[3]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No Over Voltage

| Code (bin) | Meaning |
|---|---|
| 0 | No Over Voltage |
| 1 | Over Voltage |

### [4] SWC_OUTPUT_OVER_VOLTAGE_STATUS

- Description: Switch Node C Output Over Voltage Status[4]
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

- Description: T Bit Parity Error Status6,[7]
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

### [0] DVFSQ_POWER_STATE_STATUS

- Description: PMIC DVFSQ Power State Status[9].[10],[11]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → PMIC is not operating in the DVFSQ Power State

| Code (bin) | Meaning |
|---|---|
| 0 | PMIC is not operating in the DVFSQ Power State |
| 1 | PMIC is operating in the DVFSQ Power State |

**Notes**

- NOTE 1: This register is set when SWA output voltage goes above the threshold setting in Table 138, Register 0x22, [5:4].
- NOTE 2: This register is set when SWD output voltage goes above the threshold setting in Table 140, Register 0x24 [5:4]
- NOTE 3: This register is set when SWB output voltage goes above the threshold setting in Table 142, Register 0x26, [5:4]
- NOTE 4: This register is set when SWC output voltage goes above the threshold setting in Table 144, Register 0x28, [5:4]
- NOTE 5: Applicable in I3C Mode Only and if enabled in register Table 156, Register 0x34 [7].
- NOTE 6: This register is updated when PMIC device goes through bus reset as described in clause 5.4.13.
- NOTE 7: Applicable in I3C Mode and if enabled in register Table 156, Register 0x34 [5]. It is also applicable in I2C mode for supported CCCs.
- NOTE 8: This register can be used as Global Status in addition to IBI status. When IBI function is enabled, this register is automatically cleared when PMIC transmits IBI payload; however, individual status registers still require an explicit clear command from host.
- NOTE 9: If Table 150, Register 0x2E [4] = ‘1’, this register is set when PMIC detects DVFSQ_n input transitions from high to low and is cleared when PMIC detects DVFSQ_n input transitions from low to high. The PMIC also clears this register when VR Disable command is registered (either with VR_EN pin de-assertion or via I2C/I3C bus command).
- NOTE 10: The controller cannot clear this register via any I2C/I3C bus command.
- NOTE 11: This status register is not applicable and it is a don’t care when Table 150, Register 0x2E [5] = ‘1’.

## R0B (0x0B) — SWA_OUTPUT_CURRENT_LIMITER_WARNING_STATUS, SWD_OUTPUT_CURRENT_LIMITER_WARNING_STATUS, SWB_OUTPUT_CURRENT_LIMITER_WARNING_STATUS, SWC_OUTPUT_CURRENT_LIMITER_WARNING_STATUS, SWA_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS, SWD_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS, SWB_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS, SWC_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

Region: Host Region | Source: JESD301-3 Table 115, p.142

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | SWA_OUTPUT_CURRENT_LIMITER_WARNING_STATUS | RO | 0 |
| 6 | SWD_OUTPUT_CURRENT_LIMITER_WARNING_STATUS | RO | 0 |
| 5 | SWB_OUTPUT_CURRENT_LIMITER_WARNING_STATUS | RO | 0 |
| 4 | SWC_OUTPUT_CURRENT_LIMITER_WARNING_STATUS | RO | 0 |
| 3 | SWA_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS | RO | 0 |
| 2 | SWD_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS | RO | 0 |
| 1 | SWB_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS | RO | 0 |
| 0 | SWC_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS | RO | 0 |

### [7] SWA_OUTPUT_CURRENT_LIMITER_WARNING_STATUS

- Description: Switch Node A Output Current Limiter Warning Status[1]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No Current Limiter Event

| Code (bin) | Meaning |
|---|---|
| 0 | No Current Limiter Event |
| 1 | Current Limiter Event |

### [6] SWD_OUTPUT_CURRENT_LIMITER_WARNING_STATUS

- Description: Switch Node D Output Current Limiter Warning Status[2]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No Current Limiter Event

| Code (bin) | Meaning |
|---|---|
| 0 | No Current Limiter Event |
| 1 | Current Limiter Event |

### [5] SWB_OUTPUT_CURRENT_LIMITER_WARNING_STATUS

- Description: Switch Node B Output Current Limiter Warning Status[3]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No Current Limiter Event

| Code (bin) | Meaning |
|---|---|
| 0 | No Current Limiter Event |
| 1 | Current Limiter Event |

### [4] SWC_OUTPUT_CURRENT_LIMITER_WARNING_STATUS

- Description: Switch Node C Output Current Limiter Warning Status[4]
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

### [2] SWD_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

- Description: Switch Node D Output Under Voltage Lockout Status[6]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No Under Voltage Lockout

| Code (bin) | Meaning |
|---|---|
| 0 | No Under Voltage Lockout |
| 1 | Under Voltage Lockout |

### [1] SWB_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

- Description: Switch Node B Output Under Voltage Lockout Status[7]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No Under Voltage Lockout

| Code (bin) | Meaning |
|---|---|
| 0 | No Under Voltage Lockout |
| 1 | Under Voltage Lockout |

### [0] SWC_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

- Description: Switch Node C Output Under Voltage Lockout Status[8]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No Under Voltage Lockout

| Code (bin) | Meaning |
|---|---|
| 0 | No Under Voltage Lockout |
| 1 | Under Voltage Lockout |

**Notes**

- NOTE 1: This register is set when SWA output valley current goes above the threshold setting in Table 136, Register 0x20 [7:6].
- NOTE 2: This register is set when SWC output valley current goes above the threshold setting in Table 136, Register 0x20 [5:4].
- NOTE 3: This register is set when SWB output valley current goes above the threshold setting in Table 136, Register 0x20 [3:2].
- NOTE 4: This register is set when SWC output valley current goes above the threshold setting in Table 136, Register 0x20 [1:0].
- NOTE 5: This register is set when SWA output voltage goes below the threshold setting in Table 138, Register 0x22, [3:2].
- NOTE 6: This register is set when SWC output voltage goes below the threshold setting in Table 140, Register 0x24 [3:2].
- NOTE 7: This register is set when SWB output voltage goes below the threshold setting in Table 142, Register 0x26, [3:2].
- NOTE 8: This register is set when SWC output voltage goes below the threshold setting in Table 144, Register 0x28, [3:2].

## R0C (0x0C) — SWA_OUTPUT_CURRENT_POWER_MEASUREMENT

Region: Host Region | Source: JESD301-3 Table 116, p.143

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SWA_OUTPUT_CURRENT_POWER_MEASUREMENT | RO | - |

### [7:0] SWA_OUTPUT_CURRENT_POWER_MEASUREMENT

- Description: Switch Node A Output Current or Output Power[2] Measurement[3]
- Attribute: RO — Read Only (writes have no effect)
- Default: -

**When: If Table 130, Register 0x1A[1] = ‘0’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | 125 mA or 125 mW |
| 00000010 | 0x02 | 250 mA or 250 mW |
| 00000011 | 0x03 | 375 mA or 375 mW |
| 00000100 | 0x04 | 500 mA or 500 mW |
| ... | ... | ... |
| 11111111 | 0xFF | > 31.875A or 31.875 W |

**When: If Table 130, Register 0x1A[1] = ‘1’ — Sum of SWA, SWD, SWB and SWC Output Power[4]**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | 125 mW |
| 00000010 | 0x02 | 250 mW |
| 00000011 | 0x03 | 375 mW |
| 00000100 | 0x04 | 500 mW |
| ... | ... | ... |
| 11111111 | 0xFF | > 31.875 W |

**Notes**

- NOTE 1: The PMIC reports current or power measurement as long as there is no output over voltage or output under voltage lockout event that triggers the VR Disable command. If PMIC triggers VR Disable command, PMIC does not report current or power measurement and register content may have stale data. For all other events that causes PMIC’s power good status as Not Good, the PMIC continues to provide current or power measurement.
- NOTE 2: If Table 131, Register 0x1B [6] = ‘0’, the PMIC reports current measurement. If Table 131, Register 0x1B [6] = ‘1’, the PMIC reports power measurement.
- NOTE 3: This register is only applicable if Table 154, Register 0x32 [1:0] = ‘00’.
- NOTE 4: Register Table 131, Register 0x1B [6] must be configured as ‘1’.

## R0D (0x0D) — SWD_OUTPUT_CURRENT_POWER_MEASUREMENT

Region: Host Region | Source: JESD301-3 Table 117, p.144

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SWD_OUTPUT_CURRENT_POWER_MEASUREMENT | RO | - |

### [7:0] SWD_OUTPUT_CURRENT_POWER_MEASUREMENT

- Description: Switch Node D Output Current or Output Power[2] Measurement[3]
- Attribute: RO — Read Only (writes have no effect)
- Default: -

**When: If Table 130, Register 0x1A[1] = ‘0’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | 125 mA or 125 mW |
| 00000010 | 0x02 | 250 mA or 250 mW |
| 00000011 | 0x03 | 375 mA or 375 mW |
| 00000100 | 0x04 | 500 mA or 500 mW |
| ... | ... | ... |
| 00111111 | 0x3F | > 7.875A or 7.875 W |

**Notes**

- NOTE 1: The PMIC reports current or power measurement as long as there is no output over voltage or output under voltage lockout event that triggers the VR Disable command. If PMIC triggers VR Disable command, PMIC does not report current or power measurement and register content may have stale data. For all other events that causes PMIC’s power good status as Not Good, the PMIC continues to provide current or power measurement.
- NOTE 2: If Table 131, Register 0x1B [6] = ‘0’, the PMIC reports current measurement. If Table 131, Register 0x1B [6] = ‘1’, the PMIC reports power measurement.
- NOTE 3: This register is only applicable if Table 154, Register 0x32 [1:0] = ‘00’.

## R0E (0x0E) — SWB_OUTPUT_CURRENT_POWER_MEASUREMENT

Region: Host Region | Source: JESD301-3 Table 118, p.144

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SWB_OUTPUT_CURRENT_POWER_MEASUREMENT | RO | - |

### [7:0] SWB_OUTPUT_CURRENT_POWER_MEASUREMENT

- Description: Switch Node B Output Current or Output Power[2] Measurement[3]
- Attribute: RO — Read Only (writes have no effect)
- Default: -

**When: If Table 130, Register 0x1A[1] = ‘0’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | 125 mA or 125 mW |
| 00000010 | 0x02 | 250 mA or 250 mW |
| 00000011 | 0x03 | 375 mA or 375 mW |
| 00000100 | 0x04 | 500 mA or 500 mW |
| ... | ... | ... |
| 00111111 | 0x3F | > 7.875A or 7.875 W |

**Notes**

- NOTE 1: The PMIC reports current or power measurement as long as there is no output over voltage or output under voltage lockout event that triggers the VR Disable command. If PMIC triggers VR Disable command, PMIC does not report current or power measurement and register content may have stale data. For all other events that causes PMIC’s power good status as Not Good, the PMIC continues to provide current or power measurement.
- NOTE 2: If Table 131, Register 0x1B [6] = ‘0’, the PMIC reports current measurement. If Table 131, Register 0x1B [6] = ‘1’, the PMIC reports power measurement.
- NOTE 3: This register is only applicable if Table 154, Register 0x32 [1:0] = ‘00’.

## R0F (0x0F) — SWC_OUTPUT_CURRENT_POWER_MEASUREMENT

Region: Host Region | Source: JESD301-3 Table 119, p.145

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SWC_OUTPUT_CURRENT_POWER_MEASUREMENT | RO | - |

### [7:0] SWC_OUTPUT_CURRENT_POWER_MEASUREMENT

- Description: Switch Node C Output Current or Output Power[2] Measurement[3]
- Attribute: RO — Read Only (writes have no effect)
- Default: -

**When: If Table 130, Register 0x1A[1] = ‘0’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | 125 mA or 125 mW |
| 00000010 | 0x02 | 250 mA or 250 mW |
| 00000011 | 0x03 | 375 mA or 375 mW |
| 00000100 | 0x04 | 500 mA or 500 mW |
| ... | ... | ... |
| xx111111 |  | > 7.875A or 7.875 W |

**Notes**

- NOTE 1: The PMIC reports current or power measurement as long as there is no output over voltage or output under voltage lockout event that triggers the VR Disable command. If PMIC triggers VR Disable command, PMIC does not report current or power measurement and register content may have stale data. For all other events that causes PMIC’s power good status as Not Good, the PMIC continues to provide current or power measurement.
- NOTE 2: If Table 131, Register 0x1B [6] = ‘0’, the PMIC reports current measurement. If Table 131, Register 0x1B [6] = ‘1’, the PMIC reports power measurement.
- NOTE 3: This register is only applicable if Table 154, Register 0x32 [1:0] = ‘00’.

## R10 (0x10) — CLEAR_VIN_BULK_INPUT_POWER_GOOD_STATUS, CLEAR_SWA_OUTPUT_POWER_GOOD_STATUS, CLEAR_SWD_OUTPUT_POWER_GOOD_STATUS, CLEAR_SWB_OUTPUT_POWER_GOOD_STATUS, CLEAR_SWC_OUTPUT_POWER_GOOD_STATUS, CLEAR_VIN_BULK_INPUT_OVER_VOLTAGE_STATUS

Region: Host Region | Source: JESD301-3 Table 120, p.146

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | CLEAR_VIN_BULK_INPUT_POWER_GOOD_STATUS | 1O | 0 |
| 6 | RESERVED | RV | 0 |
| 5 | CLEAR_SWA_OUTPUT_POWER_GOOD_STATUS | 1O | 0 |
| 4 | CLEAR_SWD_OUTPUT_POWER_GOOD_STATUS | 1O | 0 |
| 3 | CLEAR_SWB_OUTPUT_POWER_GOOD_STATUS | 1O | 0 |
| 2 | CLEAR_SWC_OUTPUT_POWER_GOOD_STATUS | 1O | 0 |
| 1 | RESERVED | RV | 0 |
| 0 | CLEAR_VIN_BULK_INPUT_OVER_VOLTAGE_STATUS | 1O | 0 |

### [7] CLEAR_VIN_BULK_INPUT_POWER_GOOD_STATUS

- Description: Clear VIN_Bulk Input Power Good Status
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 112, Register 0x08 [7][2] |

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
| 1 | Clear Register Table 112, Register 0x08 [5][2] |

### [4] CLEAR_SWD_OUTPUT_POWER_GOOD_STATUS

- Description: Clear SWD Output Power Good Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 112, Register 0x08 [4][2] |

### [3] CLEAR_SWB_OUTPUT_POWER_GOOD_STATUS

- Description: Clear SWB Output Power Good Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 112, Register 0x08 [3][2] |

### [2] CLEAR_SWC_OUTPUT_POWER_GOOD_STATUS

- Description: Clear SWC Output Power Good Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 112, Register 0x08 [2][2] |

### [1] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [0] CLEAR_VIN_BULK_INPUT_OVER_VOLTAGE_STATUS

- Description: Clear VIN_Bulk Input Supply Over Voltage Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 112, Register 0x08 [0][2] |

**Notes**

- NOTE 1: Table 120, Register 0x10 [5:2,0] are self clearing bits.
- NOTE 2: See Table 28 and Table 29 for POWER_GOOD output signal status change.

## R11 (0x11) — CLEAR_PMIC_HIGH_TEMP_WARNING_STATUS, CLEAR_VOUT_1.8V_OUTPUT_POWER_GOOD_STATUS, CLEAR_SWA_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS, CLEAR_SWD_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS, CLEAR_SWB_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS, CLEAR_SWC_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS

Region: Host Region | Source: JESD301-3 Table 121, p.147

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | CLEAR_PMIC_HIGH_TEMP_WARNING_STATUS | 1O | 0 |
| 6 | RESERVED | RV | 0 |
| 5 | CLEAR_VOUT_1.8V_OUTPUT_POWER_GOOD_STATUS | 1O | 0 |
| 4 | RESERVED | RV | 0 |
| 3 | CLEAR_SWA_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS | 1O | 0 |
| 2 | CLEAR_SWD_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS | 1O | 0 |
| 1 | CLEAR_SWB_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS | 1O | 0 |
| 0 | CLEAR_SWC_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS | 1O | 0 |

### [7] CLEAR_PMIC_HIGH_TEMP_WARNING_STATUS

- Description: Clear PMIC High Temperature Warning Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 113, Register 0x09 [7][2] |

### [6] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [5] CLEAR_VOUT_1.8V_OUTPUT_POWER_GOOD_STATUS

- Description: Clear VOUT_1.8V Output Power Good Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 113, Register 0x09 [5][2] |

### [4] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [3] CLEAR_SWA_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS

- Description: Clear Switch Node A High Output Current Consumption Warning Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 113, Register 0x09 [3][2] |

### [2] CLEAR_SWD_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS

- Description: Clear Switch Node D High Output Current Consumption Warning Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 113, Register 0x09 [2][2] |

### [1] CLEAR_SWB_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS

- Description: Clear Switch Node B High Output Current Consumption Warning Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 113, Register 0x09 [1][2] |

### [0] CLEAR_SWC_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS

- Description: Clear Switch Node C High Output Current Consumption Warning Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 113, Register 0x09 [0][2] |

**Notes**

- NOTE 1: Table 121, Register 0x11 [7,5,3:0] are self clearing bits.
- NOTE 2: See Table 28 and Table 29 for POWER_GOOD output signal status change.

## R12 (0x12) — CLEAR_SWA_OUTPUT_OVER_VOLTAGE_STATUS, CLEAR_SWD_OUTPUT_OVER_VOLTAGE_STATUS, CLEAR_SWB_OUTPUT_OVER_VOLTAGE_STATUS, CLEAR_SWC_OUTPUT_OVER_VOLTAGE_STATUS, CLEAR_PEC_ERROR_STATUS, CLEAR_PARITY_ERROR_STATUS

Region: Host Region | Source: JESD301-3 Table 122, p.147

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | CLEAR_SWA_OUTPUT_OVER_VOLTAGE_STATUS | 1O | 0 |
| 6 | CLEAR_SWD_OUTPUT_OVER_VOLTAGE_STATUS | 1O | 0 |
| 5 | CLEAR_SWB_OUTPUT_OVER_VOLTAGE_STATUS | 1O | 0 |
| 4 | CLEAR_SWC_OUTPUT_OVER_VOLTAGE_STATUS | 1O | 0 |
| 3 | CLEAR_PEC_ERROR_STATUS | 1O | 0 |
| 2 | CLEAR_PARITY_ERROR_STATUS | 1O | 0 |
| 1:0 | RESERVED | RV | 0 |

### [7] CLEAR_SWA_OUTPUT_OVER_VOLTAGE_STATUS

- Description: Clear Switch Node A Output Over Voltage Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 114, Register 0x0A [7][2] |

### [6] CLEAR_SWD_OUTPUT_OVER_VOLTAGE_STATUS

- Description: Clear Switch Node D Output Over Voltage Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 114, Register 0x0A [6][2] |

### [5] CLEAR_SWB_OUTPUT_OVER_VOLTAGE_STATUS

- Description: Clear Switch Node B Output Over Voltage Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 114, Register 0x0A [5][2] |

### [4] CLEAR_SWC_OUTPUT_OVER_VOLTAGE_STATUS

- Description: Clear Switch Node C Output Over Voltage Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 114, Register 0x0A [4][2] |

### [3] CLEAR_PEC_ERROR_STATUS

- Description: Clear PEC Error Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 114, Register 0x0A [3] |

### [2] CLEAR_PARITY_ERROR_STATUS

- Description: Clear Parity Error Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 114, Register 0x0A [2] |

### [1:0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

**Notes**

- NOTE 1: Table 122, Register 0x12 [7:1] are self clearing bits.
- NOTE 2: See Table 28 and Table 29 for POWER_GOOD output signal status change.

## R13 (0x13) — CLEAR_SWA_OUTPUT_CURRENT_LIMITER_WARNING_STATUS, CLEAR_SWD_OUTPUT_CURRENT_LIMITER_WARNING_STATUS, CLEAR_SWB_OUTPUT_CURRENT_LIMITER_WARNING_STATUS, CLEAR_SWC_OUTPUT_CURRENT_LIMITER_WARNING_STATUS, CLEAR_SWA_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS, CLEAR_SWD_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS, CLEAR_SWB_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS, CLEAR_SWC_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

Region: Host Region | Source: JESD301-3 Table 123, p.148

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | CLEAR_SWA_OUTPUT_CURRENT_LIMITER_WARNING_STATUS | 1O | 0 |
| 6 | CLEAR_SWD_OUTPUT_CURRENT_LIMITER_WARNING_STATUS | 1O | 0 |
| 5 | CLEAR_SWB_OUTPUT_CURRENT_LIMITER_WARNING_STATUS | 1O | 0 |
| 4 | CLEAR_SWC_OUTPUT_CURRENT_LIMITER_WARNING_STATUS | 1O | 0 |
| 3 | CLEAR_SWA_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS | 1O | 0 |
| 2 | CLEAR_SWD_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS | 1O | 0 |
| 1 | CLEAR_SWB_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS | 1O | 0 |
| 0 | CLEAR_SWC_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS | 1O | 0 |

### [7] CLEAR_SWA_OUTPUT_CURRENT_LIMITER_WARNING_STATUS

- Description: Clear Switch Node A Output Current Limiter Warning Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 115, Register 0x0B [7][2] |

### [6] CLEAR_SWD_OUTPUT_CURRENT_LIMITER_WARNING_STATUS

- Description: Clear Switch Node D Output Current Limiter Warning Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 115, Register 0x0B [6][2] |

### [5] CLEAR_SWB_OUTPUT_CURRENT_LIMITER_WARNING_STATUS

- Description: Clear Switch Node B Output Current Limiter Warning Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 115, Register 0x0B [5][2] |

### [4] CLEAR_SWC_OUTPUT_CURRENT_LIMITER_WARNING_STATUS

- Description: Clear Switch Node C Output Current Limiter Warning Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 115, Register 0x0B [4][2] |

### [3] CLEAR_SWA_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

- Description: Clear Switch Node A Output Under Voltage Lockout Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 115, Register 0x0B [3][2] |

### [2] CLEAR_SWD_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

- Description: Clear Switch Node D Output Under Voltage Lockout Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 115, Register 0x0B [2][2] |

### [1] CLEAR_SWB_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

- Description: Clear Switch Node B Output Under Voltage Lockout Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 115, Register 0x0B [1][2] |

### [0] CLEAR_SWC_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

- Description: Clear Switch Node C Output Under Voltage Lockout Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 115, Register 0x0B [0][2] |

**Notes**

- NOTE 1: Table 123, Register 0x13 [7:0] are self clearing bits.
- NOTE 2: See Table 28 and Table 29 for POWER_GOOD output signal status change.

## R14 (0x14) — CLEAR_VIN_BULK_UNDER_VOLTAGE_LOCKOUT_STATUS, CLEAR_VOUT_1.0V_OUTPUT_POWER_GOOD_STATUS, GLOBAL_CLEAR_STATUS

Region: Host Region | Source: JESD301-3 Table 124, p.148

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:4 | RESERVED | RV | 0 |
| 3 | CLEAR_VIN_BULK_UNDER_VOLTAGE_LOCKOUT_STATUS | 1O | 0 |
| 2 | CLEAR_VOUT_1.0V_OUTPUT_POWER_GOOD_STATUS | 1O | 0 |
| 1 | RESERVED | RV | 0 |
| 0 | GLOBAL_CLEAR_STATUS | 1O | 0 |

### [7:4] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [3] CLEAR_VIN_BULK_UNDER_VOLTAGE_LOCKOUT_STATUS

- Description: Clear VIN_Bulk Input Under Voltage Lockout Status
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 155, Register 0x33 [3] |

### [2] CLEAR_VOUT_1.0V_OUTPUT_POWER_GOOD_STATUS

- Description: Clear VOUT_1.0V Output Power Good Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 155, Register 0x33 [2][3] |

### [1] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [0] GLOBAL_CLEAR_STATUS

- Description: Clear all[2] status bits.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear all status bits[3] |

**Notes**

- NOTE 1: Table 124, Register 0x14 [3:2,0] are self clearing bits.
- NOTE 2: All status bits in register Table 120, Register 0x10 [5:2,0], Table 121, Register 0x11 [7,5,3:0], Table 122, Register 0x12 [7:2], Table 123, Register 0x13 [7:0], and Table 124, Register 0x14 [3:2].
- NOTE 3: See Table 28 and Table 29 for POWER_GOOD output signal status change.

## R15 (0x15) — MASK_VIN_BULK_INPUT_POWER_GOOD_STATUS, MASK_SWA_OUTPUT_POWER_GOOD_STATUS, MASK_SWD_OUTPUT_POWER_GOOD_STATUS, MASK_SWB_OUTPUT_POWER_GOOD_STATUS, MASK_SWC_OUTPUT_POWER_GOOD_STATUS, MASK_VIN_BULK_INPUT_OVER_VOLTAGE_STATUS

Region: Host Region | Source: JESD301-3 Table 125, p.149

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | MASK_VIN_BULK_INPUT_POWER_GOOD_STATUS | RW | 0 |
| 6 | RESERVED | RV | 0 |
| 5 | MASK_SWA_OUTPUT_POWER_GOOD_STATUS | RW | 1 |
| 4 | MASK_SWD_OUTPUT_POWER_GOOD_STATUS | RW | 1 |
| 3 | MASK_SWB_OUTPUT_POWER_GOOD_STATUS | RW | 1 |
| 2 | MASK_SWC_OUTPUT_POWER_GOOD_STATUS | RW | 1 |
| 1 | RESERVED | RV | 0 |
| 0 | MASK_VIN_BULK_INPUT_OVER_VOLTAGE_STATUS | RW | 0 |

### [7] MASK_VIN_BULK_INPUT_POWER_GOOD_STATUS

- Description: Mask VIN_Bulk Input Power Good Status Event[1]
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask VIN_Bulk Input Power Good Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask VIN_Bulk Input Power Good Status Event |
| 1 | Mask VIN_Bulk Input Power Good Status Event |

### [6] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [5] MASK_SWA_OUTPUT_POWER_GOOD_STATUS

- Description: Mask SWA Output Power Good Status Event1
- Attribute: RW — Read/Write
- Default: 1 → Mask SWA Output Power Good Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWA Output Power Good Status Event |
| 1 | Mask SWA Output Power Good Status Event |

### [4] MASK_SWD_OUTPUT_POWER_GOOD_STATUS

- Description: Mask SWD Output Power Good Status Event1
- Attribute: RW — Read/Write
- Default: 1 → Mask SWD Output Power Good Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWD Output Power Good Status Event |
| 1 | Mask SWD Output Power Good Status Event |

### [3] MASK_SWB_OUTPUT_POWER_GOOD_STATUS

- Description: Mask SWB Output Power Good Status Event1
- Attribute: RW — Read/Write
- Default: 1 → Mask SWB Output Power Good Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWB Output Power Good Status Event |
| 1 | Mask SWB Output Power Good Status Event |

### [2] MASK_SWC_OUTPUT_POWER_GOOD_STATUS

- Description: Mask SWC Output Power Good Status Event1
- Attribute: RW — Read/Write
- Default: 1 → Mask SWC Output Power Good Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWC Output Power Good Status Event |
| 1 | Mask SWC Output Power Good Status Event |

### [1] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [0] MASK_VIN_BULK_INPUT_OVER_VOLTAGE_STATUS

- Description: Mask VIN_Bulk Input Supply Over Voltage Status Event[2]
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask VIN_Bulk Input Supply Over Voltage Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask VIN_Bulk Input Supply Over Voltage Status Event |
| 1 | Mask VIN_Bulk Input Supply Over Voltage Status Event |

**Notes**

- NOTE 1: Not assert GSI_n or assert PWR_GOOD output signal.
- NOTE 2: Not assert GSI_n output signal.

## R16 (0x16) — MASK_PMIC_HIGH_TEMP_WARNING_STATUS, MASK_VOUT_1.8V_OUTPUT_POWER_GOOD_STATUS, MASK_SWA_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS, MASK_SWD_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS, MASK_SWB_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS, MASK_SWC_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS

Region: Host Region | Source: JESD301-3 Table 126, p.150

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | MASK_PMIC_HIGH_TEMP_WARNING_STATUS | RW | 0 |
| 6 | RESERVED | RV | 0 |
| 5 | MASK_VOUT_1.8V_OUTPUT_POWER_GOOD_STATUS | RW | 1 |
| 4 | RESERVED | RV | 0 |
| 3 | MASK_SWA_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS | RW | 0 |
| 2 | MASK_SWD_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS | RW | 0 |
| 1 | MASK_SWB_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS | RW | 0 |
| 0 | MASK_SWC_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS | RW | 0 |

### [7] MASK_PMIC_HIGH_TEMP_WARNING_STATUS

- Description: Mask PMIC High Temperature Warning Status Event
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask PMIC High Temperature Warning Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask PMIC High Temperature Warning Status Event |
| 1 | Mask PMIC High Temperature Warning Status Event[1] |

### [6] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [5] MASK_VOUT_1.8V_OUTPUT_POWER_GOOD_STATUS

- Description: Mask VOUT_1.8V Output Power Good Status Event.
- Attribute: RW — Read/Write
- Default: 1 → Mask 1.8V Output Power Good Status Event[2]

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask 1.8V Output Power Good Status Event |
| 1 | Mask 1.8V Output Power Good Status Event[2] |

### [4] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [3] MASK_SWA_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS

- Description: Mask SWA High Output Current Consumption Warning Status Event
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask SWA High Output Current Consumption Warning Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWA High Output Current Consumption Warning Status Event |
| 1 | Mask SWA High Output Current Consumption Warning Status Event[1] |

### [2] MASK_SWD_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS

- Description: Mask SWD High Output Current Consumption Warning Status Event
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask SWD High Output Current Consumption Warning Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWD High Output Current Consumption Warning Status Event |
| 1 | Mask SWD High Output Current Consumption Warning Status Event[1] |

### [1] MASK_SWB_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS

- Description: Mask SWB High Output Current Consumption Warning Status Event
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask SWB High Output Current Consumption Warning Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWB High Output Current Consumption Warning Status Event |
| 1 | Mask SWB High Output Current Consumption Warning Status Event[1] |

### [0] MASK_SWC_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS

- Description: Mask SWC High Output Current Consumption Warning Status Event
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask SWC High Output Current Consumption Warning Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWC High Output Current Consumption Warning Status Event |
| 1 | Mask SWC High Output Current Consumption Warning Status Event[1] |

**Notes**

- NOTE 1: Not assert GSI_n output signal.
- NOTE 2: Not assert GSI_n or assert PWR_GOOD output signal.

## R17 (0x17) — MASK_SWA_OUTPUT_OVER_VOLTAGE_STATUS, MASK_SWD_OUTPUT_OVER_VOLTAGE_STATUS, MASK_SWB_OUTPUT_OVER_VOLTAGE_STATUS, MASK_SWC_OUTPUT_OVER_VOLTAGE_STATUS, MASK_PEC_ERROR_STATUS, MASK_PARITY_ERROR_STATUS

Region: Host Region | Source: JESD301-3 Table 127, p.151

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | MASK_SWA_OUTPUT_OVER_VOLTAGE_STATUS | RW | 0 |
| 6 | MASK_SWD_OUTPUT_OVER_VOLTAGE_STATUS | RW | 0 |
| 5 | MASK_SWB_OUTPUT_OVER_VOLTAGE_STATUS | RW | 0 |
| 4 | MASK_SWC_OUTPUT_OVER_VOLTAGE_STATUS | RW | 0 |
| 3 | MASK_PEC_ERROR_STATUS | RW | 0 |
| 2 | MASK_PARITY_ERROR_STATUS | RW | 0 |
| 1:0 | RESERVED | RV | 0 |

### [7] MASK_SWA_OUTPUT_OVER_VOLTAGE_STATUS

- Description: Mask SWA Output Over Voltage Status Event
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask SWA Output Over Voltage Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWA Output Over Voltage Status Event |
| 1 | Mask SWA Output Over Voltage Status Event[1] |

### [6] MASK_SWD_OUTPUT_OVER_VOLTAGE_STATUS

- Description: Mask SWD Output Over Voltage Status Event
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask SWD Output Over Voltage Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWD Output Over Voltage Status Event |
| 1 | Mask SWD Output Over Voltage Status Event[1] |

### [5] MASK_SWB_OUTPUT_OVER_VOLTAGE_STATUS

- Description: Mask SWB Output Over Voltage Status Event
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask SWB Output Over Voltage Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWB Output Over Voltage Status Event |
| 1 | Mask SWB Output Over Voltage Status Event[1] |

### [4] MASK_SWC_OUTPUT_OVER_VOLTAGE_STATUS

- Description: Mask SWC Output Over Voltage Status Event
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask SWC Output Over Voltage Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWC Output Over Voltage Status Event |
| 1 | Mask SWC Output Over Voltage Status Event[1] |

### [3] MASK_PEC_ERROR_STATUS

- Description: Mask PEC Error Event for GSI_n Output Only[2]
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask PEC Error Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask PEC Error Status Event |
| 1 | Mask PEC Error Status |

### [2] MASK_PARITY_ERROR_STATUS

- Description: Mask Parity Error Event for GSI_n Output Only[3]
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
- NOTE 2: Only applicable when PMIC is in I3C Basic Mode. This mask register only masks the GSI_n output signal. Does not apply to IBI.
- NOTE 3: Only applicable when PMIC is in I3C Basic Mode or for supported CCC in I2C mode. This mask register only masks the GSI_n output signal. Does not apply to IBI.

## R18 (0x18) — MASK_SWA_OUTPUT_CURRENT_LIMITER_WARNING_STATUS, MASK_SWD_OUTPUT_CURRENT_LIMITER_WARNING_STATUS, MASK_SWB_OUTPUT_CURRENT_LIMITER_WARNING_STATUS, MASK_SWC_OUTPUT_CURRENT_LIMITER_WARNING_STATUS, MASK_SWA_OUTPUT_UNDER_VOLTAGE_STATUS, MASK_SWD_OUTPUT_UNDER_VOLTAGE_STATUS, MASK_SWB_OUTPUT_UNDER_VOLTAGE_STATUS, MASK_SWC_OUTPUT_UNDER_VOLTAGE_STATUS

Region: Host Region | Source: JESD301-3 Table 128, p.152

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | MASK_SWA_OUTPUT_CURRENT_LIMITER_WARNING_STATUS | RW | 0 |
| 6 | MASK_SWD_OUTPUT_CURRENT_LIMITER_WARNING_STATUS | RW | 0 |
| 5 | MASK_SWB_OUTPUT_CURRENT_LIMITER_WARNING_STATUS | RW | 0 |
| 4 | MASK_SWC_OUTPUT_CURRENT_LIMITER_WARNING_STATUS | RW | 0 |
| 3 | MASK_SWA_OUTPUT_UNDER_VOLTAGE_STATUS | RW | 0 |
| 2 | MASK_SWD_OUTPUT_UNDER_VOLTAGE_STATUS | RW | 0 |
| 1 | MASK_SWB_OUTPUT_UNDER_VOLTAGE_STATUS | RW | 0 |
| 0 | MASK_SWC_OUTPUT_UNDER_VOLTAGE_STATUS | RW | 0 |

### [7] MASK_SWA_OUTPUT_CURRENT_LIMITER_WARNING_STATUS

- Description: Mask SWA Output Current Limiter Warning Status Event
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask SWA Output Current Limiter Warning Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWA Output Current Limiter Warning Status Event |
| 1 | Mask SWA Output Current Limiter Warning Status Event[1] |

### [6] MASK_SWD_OUTPUT_CURRENT_LIMITER_WARNING_STATUS

- Description: Mask SWD Output Current Limiter Warning Status Event
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask SWD Output Current Limiter Warning Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWD Output Current Limiter Warning Status Event |
| 1 | Mask SWD Output Current Limiter Warning Status Event[1] |

### [5] MASK_SWB_OUTPUT_CURRENT_LIMITER_WARNING_STATUS

- Description: Mask SWB Output Current Limiter Warning Status Event
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask SWB Output Current Limiter Warning Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWB Output Current Limiter Warning Status Event |
| 1 | Mask SWB Output Current Limiter Warning Status Event[1] |

### [4] MASK_SWC_OUTPUT_CURRENT_LIMITER_WARNING_STATUS

- Description: Mask SWC Output Current Limiter Warning Status Event
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask SWC Output Current Limiter Warning Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWC Output Current Limiter Warning Status Event |
| 1 | Mask SWC Output Current Limiter Warning Status Event[1] |

### [3] MASK_SWA_OUTPUT_UNDER_VOLTAGE_STATUS

- Description: Mask SWA Output Under Voltage Status Event
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask SWA Output Under Voltage Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWA Output Under Voltage Status Event |
| 1 | Mask SWA Output Under Voltage Status Event[1] |

### [2] MASK_SWD_OUTPUT_UNDER_VOLTAGE_STATUS

- Description: Mask SWD Output Under Voltage Status Event
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask SWD Output Under Voltage Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWD Output Under Voltage Status Event |
| 1 | Mask SWD Output Under Voltage Status Event[1] |

### [1] MASK_SWB_OUTPUT_UNDER_VOLTAGE_STATUS

- Description: Mask SWB Output Under Voltage Status Event
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask SWB Output Under Voltage Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWB Output Under Voltage Status Event |
| 1 | Mask SWB Output Under Voltage Status Event[1] |

### [0] MASK_SWC_OUTPUT_UNDER_VOLTAGE_STATUS

- Description: Mask SWC Output Under Voltage Status Event
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask SWC Output Under Voltage Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWC Output Under Voltage Status Event |
| 1 | Mask SWC Output Under Voltage Status Event[1] |

**Notes**

- NOTE 1: Not assert GSI_n output signal.

## R19 (0x19) — MASK_VIN_BULK_UNDER_VOLTAGE_LOCKOUT_STATUS, MASK_VOUT_1.0V_OUTPUT_POWER_GOOD_STATUS

Region: Host Region | Source: JESD301-3 Table 129, p.153

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:4 | RESERVED | RV | 0 |
| 3 | MASK_VIN_BULK_UNDER_VOLTAGE_LOCKOUT_STATUS | RW | 0 |
| 2 | MASK_VOUT_1.0V_OUTPUT_POWER_GOOD_STATUS | RW | 1 |
| 1:0 | RESERVED | RV | 0 |

### [7:4] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [3] MASK_VIN_BULK_UNDER_VOLTAGE_LOCKOUT_STATUS

- Description: Mask VIN_Bulk Input Under Voltage Lockout Event
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask VIN_Bulk Input Under Voltage Lockout

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask VIN_Bulk Input Under Voltage Lockout |
| 1 | Mask VIN_Bulk Input Under Voltage Lockout[1] |

### [2] MASK_VOUT_1.0V_OUTPUT_POWER_GOOD_STATUS

- Description: Mask VOUT_1.0V Output Power Good Status Event.[2]
- Attribute: RW — Read/Write
- Default: 1 → Mask 1.0V Output Power Good Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask 1.0V Output Power Good Status Event |
| 1 | Mask 1.0V Output Power Good Status Event |

### [1:0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

**Notes**

- NOTE 1: Not assert GSI_n output signal.
- NOTE 2: Not assert GSI_n or PWR_GOOD output signal.

## R1A (0x1A) — VIN_BULK_POWER_GOOD_THRESHOLD_VOLTAGE, QUIESCENT_STATE_EN, VOUT_1.8V_POWER_GOOD_THRESHOLD_VOLTAGE, OUTPUT_POWER_SELECT, VOUT_1.0V_POWER_GOOD_THRESHOLD_VOLTAGE

Region: Host Region | Source: JESD301-3 Table 130, p.154

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | VIN_BULK_POWER_GOOD_THRESHOLD_VOLTAGE | RW | 10 |
| 5 | RESERVED | RV | 0 |
| 4 | QUIESCENT_STATE_EN | RW | 1 |
| 3 | RESERVED | RV | 0 |
| 2 | VOUT_1.8V_POWER_GOOD_THRESHOLD_VOLTAGE | RW | 0 |
| 1 | OUTPUT_POWER_SELECT | RW | 0 |
| 0 | VOUT_1.0V_POWER_GOOD_THRESHOLD_VOLTAGE | RW | 0 |

### [7:6] VIN_BULK_POWER_GOOD_THRESHOLD_VOLTAGE

- Description: VIN_Bulk Input Threshold Voltage for Input Power Good Status for Input supply Voltage[1]
- Attribute: RW — Read/Write
- Default: 10 → 3.0V[2],[3]

| Code (bin) | Meaning |
|---|---|
| 00 | Reserved |
| 01 | 4.25V |
| 10 | 3.0V[2],[3] |
| 11 | Reserved |

### [5] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [4] QUIESCENT_STATE_EN

- Description: PMIC Quiescent State Entry Enable[4]
- Attribute: RW — Read/Write
- Default: 1 → Enable[5],[6]

| Code (bin) | Meaning |
|---|---|
| 0 | Disable |
| 1 | Enable[5],[6] |

### [3] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [2] VOUT_1.8V_POWER_GOOD_THRESHOLD_VOLTAGE

- Description: VOUT 1.8V LDO Output Threshold Voltage for Power Good Status
- Attribute: RW — Read/Write
- Default: 0 → 1.6 V

| Code (bin) | Meaning |
|---|---|
| 0 | 1.6 V |
| 1 | Reserved |

### [1] OUTPUT_POWER_SELECT

- Description: Switch Regulator Output Power Select[7]
- Attribute: RW — Read/Write
- Default: 0 → Report individual power for each rail in R0C, R0D, R0E and R0F

| Code (bin) | Meaning |
|---|---|
| 0 | Report individual power for each rail in R0C, R0D, R0E and R0F |
| 1 | Report total power of each rail in R0C[8] |

### [0] VOUT_1.0V_POWER_GOOD_THRESHOLD_VOLTAGE

- Description: VOUT 1.0V LDO Output Threshold Voltage for Power Good Status
- Attribute: RW — Read/Write
- Default: 0 → -10% from the setting in Table 199, Register 0x51 [2:1]

| Code (bin) | Meaning |
|---|---|
| 0 | -10% from the setting in Table 199, Register 0x51 [2:1] |
| 1 | -15% from the setting in Table 199, Register 0x51 [2:1] |

**Notes**

- NOTE 1: If VIN_Bulk input voltage is higher than threshold setting, the PMIC continues to operate as normal. If VIN_Bulk input voltage falls below the threshold setting, the PMIC may continue to operate but updates its PWR_GOOD status register and asserts GSI_n, PWR_GOOD output signal appropriately.
- NOTE 2: If VIN_Bulk input voltage falls below this threshold setting, the PMIC may not guarantee operation.
- NOTE 3: If VIN_Bulk input voltage continues to fall below vendor specific UVLO, the PMIC triggers VR Disable command and executes power down sequence.
- NOTE 4: This bit must be configured before issuing VR Enable command unless Unlock_n pin is intended to be used to unlock the registers.
- NOTE 5: VR Disable command (VR_EN pin transition to low or Table 154, Register 0x32 [7] = ‘0’ (in programmable mode only)) puts PMIC in Quiescent state.
- NOTE 6: Simultaneous usage of programmable mode (i.e., Table 151, Register 0x2F [2] = ‘1’), PWR_GOOD as IO (i.e., Table 154, Register 0x32 [5] = ‘1’) and P1 State Enable (i.e., Table 130, Register 0x1A [4] = ‘1’) is considered an illegal configuration when VR_EN pin is intended to be used; otherwise it is a valid configuration if VR_EN command is used on I2C/I3C Basic bus.
- NOTE 7: This register is only applicable if Table 131, Register 0x1B [6] = ‘1’.
- NOTE 8: Host should only read Table 116, Register 0x0C [7:0] for total power. The register contents of Table 117, Register 0x0D, Table 118, Register 0x0E, and Table 119, Register 0x0F may not be valid.

## R1B (0x1B) — VIN_BULK_OVER_VOLTAGE_THRESHOLD, CURRENT_OR_POWER_METER_SELECT, GLOBAL_PWR_GOOD_PIN_STATUS_MASK, GSI_N_PIN_ENABLE, PMIC_HIGH_TEMPERATURE_WARNING_THRESHOLD

Region: Host Region | Source: JESD301-3 Table 131, p.155

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | VIN_BULK_OVER_VOLTAGE_THRESHOLD | RW | 0 |
| 6 | CURRENT_OR_POWER_METER_SELECT | RW | 0 |
| 5 | RESERVED | RV | 0 |
| 4 | GLOBAL_PWR_GOOD_PIN_STATUS_MASK | RW | 0 |
| 3 | GSI_N_PIN_ENABLE | RW | 0 |
| 2:0 | PMIC_HIGH_TEMPERATURE_WARNING_THRESHOLD | RW | 101 |

### [7] VIN_BULK_OVER_VOLTAGE_THRESHOLD

- Description: VIN_Bulk Input Over Voltage Threshold Setting
- Attribute: RW — Read/Write
- Default: 0 → 5.8 V to 6 V (Varies across vendors)

| Code (bin) | Meaning |
|---|---|
| 0 | 5.8 V to 6 V (Varies across vendors) |
| 1 | Reserved |

### [6] CURRENT_OR_POWER_METER_SELECT

- Description: PMIC Output Regulator Measurement - Current or Power Meter
- Attribute: RW — Read/Write
- Default: 0 → Report Current Measurements in registers:[1]

| Code (bin) | Meaning |
|---|---|
| 0 | Report Current Measurements in registers:[1] |
| 1 | Report Power Measurements in registers1 |

### [5] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

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
- Default: 101 → PMIC temperature > 125 0C

| Code (bin) | Meaning |
|---|---|
| 000 | Reserved |
| 001 | PMIC temperature > 85 0C |
| 010 | PMIC temperature > 95 0C |
| 011 | PMIC temperature > 105 0C |
| 100 | PMIC temperature > 115 0C |
| 101 | PMIC temperature > 125 0C |
| 110 | PMIC temperature > 135 0C |
| 111 | Reserved |

**Notes**

- NOTE 1: Table 116, Register 0x0C, Table 117, Register 0x0D, Table 118, Register 0x0E, and Table 119, Register 0x0F.
- NOTE 2: Mask POWER_GOOD output signal for register bits in Table 125, Register 0x15 [7,5:0], Table 126, Register 0x16 [7,5,3:0], Table 127, Register 0x17 [7:4], Table 128, Register 0x18 [7:0], and Table 129, Register 0x19 [3:2]. Mask Register Control Table 151, Register 0x2F [1:0] still applies when Global PWR_GOOD output Mask register is set to ‘1’.
- NOTE 3: This register can be used as Global Mask Function for GSI_n pin. If disabled, this masks the GSI_n output signal for all register bits in Table 125, Register 0x15 [7,5:0], Table 126, Register 0x16 [7,5,3:0], Table 127, Register 0x17 [7:4] Table 128, Register 0x18[7:0], and Table 129, Register 0x19 [3:2].
- NOTE 4: The tolerance of the temperature warning threshold is + 5 0C from the selected setting.

## R1C (0x1C) — SWA_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD

Region: Host Region | Source: JESD301-3 Table 132, p.156

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SWA_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD | RW | 1111 0000 |

### [7:0] SWA_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD

- Description: Switch Node A Output High Current Consumption Warning Threshold[2]
- Attribute: RW — Read/Write
- Default: 1111 0000 → > 30000 mA (if If Table 154, Register 0x32 [1:0] = ‘00’); > 7500 mA (if If Table 154, Register 0x32 [1:0] = ‘01’)

**When: If Table 154, Register 0x32 [1:0] = ‘00’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | > 125 mA |
| 00000010 | 0x02 | > 250 mA |
| ... | ... | ... |
| 11111111 | 0xFF | > 31.875A |

**When: If Table 154, Register 0x32 [1:0] = ‘01’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | > 31.25 mA |
| 00000010 | 0x02 | > 62.5 mA |
| 00000011 | 0x03 | > 93.75 mA |
| 00000100 | 0x04 | > 125 mA |
| ... | ... | ... |
| 11111111 | 0xFF | > 7.968 A |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 207, Register 0x67.
- NOTE 2: The default value is set based on Table 154, Register 0x32 [1:0] = ‘01’

## R1D (0x1D) — SWD_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD

Region: Host Region | Source: JESD301-3 Table 133, p.156

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SWD_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD | RW | 0010 0111 |

### [7:0] SWD_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD

- Description: Switch Node D Output High Current Consumption Warning Threshold[2]
- Attribute: RW — Read/Write
- Default: 0010 0111 → > 4875 mA (if If Table 154, Register 0x32 [1:0] = ‘00’); > 1218.75 mA (if If Table 154, Register 0x32 [1:0] = ‘01’)

**When: If Table 154, Register 0x32 [1:0] = ‘00’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | > 125 mA |
| 00000010 | 0x02 | > 250 mA |
| ... | ... | ... |
| 11111111 | 0xFF | > 31.875A |

**When: If Table 154, Register 0x32 [1:0] = ‘01’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | > 31.25 mA |
| 00000010 | 0x02 | > 62.5 mA |
| 00000011 | 0x03 | > 93.75 mA |
| 00000100 | 0x04 | > 125 mA |
| ... | ... | ... |
| 11111111 | 0xFF | > 7.968 A |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 208, Register 0x68.
- NOTE 2: The default value is set based on Table 154, Register 0x32 [1:0] = ‘01’

## R1E (0x1E) — SWB_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD

Region: Host Region | Source: JESD301-3 Table 134, p.157

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SWB_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD | RW | 0010 0111 |

### [7:0] SWB_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD

- Description: Switch Node B Output High Current Consumption Warning Threshold[2]
- Attribute: RW — Read/Write
- Default: 0010 0111 → > 4875 mA (if If Table 154, Register 0x32 [1:0] = ‘00’); > 1218.75 mA (if If Table 154, Register 0x32 [1:0] = ‘01’)

**When: If Table 154, Register 0x32 [1:0] = ‘00’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | > 125 mA |
| 00000010 | 0x02 | > 250 mA |
| ... | ... | ... |
| 11111111 | 0xFF | > 31.875A |

**When: If Table 154, Register 0x32 [1:0] = ‘01’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | > 31.25 mA |
| 00000010 | 0x02 | > 62.5 mA |
| 00000011 | 0x03 | > 93.75 mA |
| 00000100 | 0x04 | > 125 mA |
| ... | ... | ... |
| 11111111 | 0xFF | > 7.968 A |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 209, Register 0x69.
- NOTE 2: The default value is set based on Table 154, Register 0x32 [1:0] = ‘01’

## R1F (0x1F) — SWC_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD

Region: Host Region | Source: JESD301-3 Table 135, p.157

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SWC_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD | RW | 0010 0000 |

### [7:0] SWC_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD

- Description: Switch Node C Output High Current Consumption Warning Threshold[2]
- Attribute: RW — Read/Write
- Default: 0010 0000 → > 4000 mA (if If Table 154, Register 0x32 [1:0] = ‘00’); > 1000 mA (if If Table 154, Register 0x32 [1:0] = ‘01’)

**When: If Table 154, Register 0x32 [1:0] = ‘00’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | > 125 mA |
| 00000010 | 0x02 | > 250 mA |
| ... | ... | ... |
| 11111111 | 0xFF | > 31.875A |

**When: If Table 154, Register 0x32 [1:0] = ‘01’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | > 31.25 mA |
| 00000010 | 0x02 | > 62.5 mA |
| 00000011 | 0x03 | > 93.75 mA |
| 00000100 | 0x04 | > 125 mA |
| ... | ... | ... |
| 11111111 | 0xFF | > 7.968 A |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 210, Register 0x6A.
- NOTE 2: The default value is set based on Table 154, Register 0x32 [1:0] = ‘01’

## R20 (0x20) — SWA_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING, SWD_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING, SWB_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING, SWC_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING

Region: Host Region | Source: JESD301-3 Table 136, p.158

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWA_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING | RW | 0 |
| 5:4 | SWD_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING | RW | 0 |
| 3:2 | SWB_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING | RW | 0 |
| 1:0 | SWC_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING | RW | 0 |

### [7:6] SWA_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING

- Description: For COT Mode, Ivalley_limit:
- Attribute: RW — Read/Write
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 00 | 7.5. A |
| 01 | 8.5 A |
| 10 | 9.5 A |
| 11 | Vendor specific |

### [5:4] SWD_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING

- Description: For COT Mode, Ivalley_limit:
- Attribute: RW — Read/Write
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 00 | 0.5 A |
| 01 | 1.0 A |
| 10 | 1.5A |
| 11 | Vendor specific |

### [3:2] SWB_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING

- Description: For COT Mode, Ivalley_limit:
- Attribute: RW — Read/Write
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 00 | 0.5 A |
| 01 | 1.0 A |
| 10 | 1.5A |
| 11 | Vendor specific |

### [1:0] SWC_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING

- Description: For COT Mode, Ivalley_limit:
- Attribute: RW — Read/Write
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 00 | 0.5 A |
| 01 | 1.0 A |
| 10 | Reserved |
| 11 | Vendor specific |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 198, Register 0x50.

## R21 (0x21) — SWA_VOLTAGE_SETTING, SWA_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

Region: Host Region | Source: JESD301-3 Table 137, p.159

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:1 | SWA_VOLTAGE_SETTING | RW | 011 0010 |
| 0 | SWA_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING | RW | 0 |

### [7:1] SWA_VOLTAGE_SETTING

- Description: Switch Node A Output Regulator Voltage Setting[3],[4]
- Attribute: RW — Read/Write
- Default: 011 0010 → 1050 mV or 1300 mV

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 0000000 | 0x00 | 800[5] mV or 800[6] mV |
| 0000001 | 0x01 | 805 mV or 810 mV |
| 0000010 | 0x02 | 810 mV or 820 mV |
| ... | ... | ... |
| 0110010 | 0x32 | 1050 mV or 1300 mV |
| ... | ... | ... |
| 1111101 | 0x7D | 1425 mV or 2050 mV |
| 1111110 | 0x7E | 1430 mV or 2060 mV |
| 1111111 | 0x7F | 1435 mV or 2070 mV |

### [0] SWA_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

- Description: Switch Node A Output Threshold Low Side Voltage For Power Good Status
- Attribute: RW — Read/Write
- Default: 0 → -5% from the setting in Table 137, Register 0x21, [7:1]

| Code (bin) | Meaning |
|---|---|
| 0 | -5% from the setting in Table 137, Register 0x21, [7:1] |
| 1 | -7.5% from the setting in Table 137, Register 0x21, [7:1] |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 187, Register 0x45.
- NOTE 2: If required, the host must update the settings in register Table 137, Register 0x21, [0], Table 138, Register 0x22, [7:2], and Table 136, Register 0x20 [7:6] first prior to updating the settings in the register Table 137, Register 0x21, [7:1].
- NOTE 3: PMIC guarantees efficiency spec and all electrical characteristics spec within a range of 1000 mV to 1100 mV.
- NOTE 4: After VR is enabled, the host may update this register to any new setting that it may desire. However, to prevent false error trigger, the PMIC internally will increment the SWA output voltage setting by 5 or 10 mV at a time. The time it takes for PMIC to adjust the output voltage is 5 μs for each 5 mV increment. The host must wait sufficient time for PMIC to adjust to final value. As an example, if host adjusts the output voltage by 50 mV from the original value, the host must wait minimum of 50 μs before PMIC can guarantee the new output voltage. During this time, PMIC masks the PWR_GOOD output signal assertion to prevent any artificial error due to the crossing of the output voltage threshold setting. However, PMIC does assert PWR_GOOD output signal if there are any abnormal issues that triggers VR Disable command as described in Table 27. Further, PMIC does monitor PWR_GOOD input signal and executes power off config sequence registers if it is registered low when Table 154, Register 0x32 [5] = ‘1’.
- NOTE 5: Table 147, Register 0x2B, [5] = ‘0’; 5 mV step size.
- NOTE 6: Table 147, Register 0x2B, [5] = ‘1’; 10 mV step size.

## R22 (0x22) — SWA_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING, SWA_OVER_VOLTAGE_THRESHOLD_SETTING, SWA_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING, SWA_OUTPUT_SOFT_STOP_TIME

Region: Host Region | Source: JESD301-3 Table 138, p.160

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWA_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING | RW | 01 |
| 5:4 | SWA_OVER_VOLTAGE_THRESHOLD_SETTING | RW | 10 |
| 3:2 | SWA_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING | RW | 00 |
| 1:0 | SWA_OUTPUT_SOFT_STOP_TIME | RW | 00 |

### [7:6] SWA_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING

- Description: Switch Node A Output Threshold High Side Voltage For Power Good Status
- Attribute: RW — Read/Write
- Default: 01 → +7.5% from the setting in Table 137, Register 0x21, [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +5% from the setting in Table 137, Register 0x21, [7:1] |
| 01 | +7.5% from the setting in Table 137, Register 0x21, [7:1] |
| 10 | +10% from the setting in Table 137, Register 0x21, [7:1] |
| 11 | Reserved |

### [5:4] SWA_OVER_VOLTAGE_THRESHOLD_SETTING

- Description: Switch Node A Output Regulator Threshold For Over Voltage Status[3]
- Attribute: RW — Read/Write
- Default: 10 → +12.5% from the setting in Table 137, Register 0x21, [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +7.5% from the setting in Table 137, Register 0x21, [7:1] |
| 01 | +10% from the setting in Table 137, Register 0x21, [7:1] |
| 10 | +12.5% from the setting in Table 137, Register 0x21, [7:1] |
| 11 | Reserved |

### [3:2] SWA_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING

- Description: Switch Node A Output Regulator Threshold For Under Voltage Lockout Status
- Attribute: RW — Read/Write
- Default: 00 → -10% from the setting in Table 137, Register 0x21, [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | -10% from the setting in Table 137, Register 0x21, [7:1] |
| 01 | -12.5% from the setting in Table 137, Register 0x21, [7:1] |
| 10 | Reserved |
| 11 | Reserved |

### [1:0] SWA_OUTPUT_SOFT_STOP_TIME

- Description: SWA Output Regulator Soft Stop Time After VR Disable[4]. The register Table 158, Register 0x36 [7] (MSB) plus this two bit register makes the 3 bit encoding.
- Attribute: RW — Read/Write
- Default: 00
- Note: the codes below are wider than this 2-bit field; the encoding combines bits from more than one field/register (see Description).

| Code (bin) | Meaning |
|---|---|
| 000 | 0.5 ms |
| 001 | 1 ms |
| 010 | 2 ms |
| 011 | 4 ms |
| 100 | 8 ms |
| 101 | 16 ms |
| 110 | 32 ms |
| 111 | 64 ms |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 188, Register 0x46.
- NOTE 2: If required, the host must update the setting in register Table 137, Register 0x21, [0], Table 138, Register 0x22, [7:2], and Table 136, Register 0x20 [7:6] first prior to updating the settings in the register Table 137, Register 0x21, [7:1].
- NOTE 3: The setting for the Over Voltage must be higher than Power Good High Side Voltage threshold in Table 138, Register 0x22,[7:6].
- NOTE 4: This is the time it takes for buck regulator to go from steady state voltage to 0 V.

## R23 (0x23) — SWD_VOLTAGE_SETTING, SWD_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

Region: Host Region | Source: JESD301-3 Table 139, p.161

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:1 | SWD_VOLTAGE_SETTING | RW | 001 0100 |
| 0 | SWD_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING | RW | 0 |

### [7:1] SWD_VOLTAGE_SETTING

- Description: Switch Node D Output Regulator Voltage Setting[3],[4]
- Attribute: RW — Read/Write
- Default: 001 0100 → 900 mV or 1000 mV

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 0000000 | 0x00 | 800[5] mV or 800[6] mV |
| 0000001 | 0x01 | 805 mV or 810 mV |
| 0000010 | 0x02 | 810 mV or 820 mV |
| ... | ... | ... |
| 0010100 | 0x14 | 900 mV or 1000 mV |
| ... | ... | ... |
| 1111101 | 0x7D | 1425 mV or 2050 mV |
| 1111110 | 0x7E | 1430 mV or 2060 mV |
| 1111111 | 0x7F | 1435 mV or 2070 mV |

### [0] SWD_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

- Description: Switch Node D Output Threshold Low Side Voltage For Power Good Status
- Attribute: RW — Read/Write
- Default: 0 → -5% from the setting in Table 139, Register 0x23, [7:1]

| Code (bin) | Meaning |
|---|---|
| 0 | -5% from the setting in Table 139, Register 0x23, [7:1] |
| 1 | -7.5% from the setting in Table 139, Register 0x23, [7:1] |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 189, Register 0x47.
- NOTE 2: If required, the host must update the settings in register Table 139, Register 0x23, [0], Table 140, Register 0x24 [7:2], and Table 136, Register 0x20 [5:4] first prior to updating the settings in the register Table 139, Register 0x23, [7:1].
- NOTE 3: PMIC guarantees efficiency spec and all electrical characteristics spec within a range of 850 mV to 950 mV.
- NOTE 4: After VR is enabled, the host may update this register to any new setting that it may desire. However, to prevent false error trigger, the PMIC internally will increment the SWA output voltage setting by 5 or 10 mV at a time. The time it takes for PMIC to adjust the output voltage is 5 μs for each 5 mV increment. The host must wait sufficient time for PMIC to adjust to final value. As an example, if host adjusts the output voltage by 50 mV from the original value, the host must wait minimum of 50 μs before PMIC can guarantee the new output voltage. During this time, PMIC masks the PWR_GOOD output signal assertion to prevent any artificial error due to the crossing of the output voltage threshold setting. However, PMIC does assert PWR_GOOD output signal if there are any abnormal issues that triggers VR Disable command as described in Table 27. Further, PMIC does monitor PWR_GOOD input signal and executes power off config sequence registers if it is registered low when Table 154, Register 0x32 [5] = ‘1’.
- NOTE 5: Table 147, Register 0x2B, [4] = ‘0’; 5 mV step size.
- NOTE 6: Table 147, Register 0x2B, [4] = ‘1’; 10 mV step size.

## R24 (0x24) — SWD_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING, SWD_OVER_VOLTAGE_THRESHOLD_SETTING, SWD_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING, SWD_OUTPUT_SOFT_STOP_TIME

Region: Host Region | Source: JESD301-3 Table 140, p.162

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWD_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING | RW | 01 |
| 5:4 | SWD_OVER_VOLTAGE_THRESHOLD_SETTING | RW | 10 |
| 3:2 | SWD_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING | RW | 00 |
| 1:0 | SWD_OUTPUT_SOFT_STOP_TIME | RW | 00 |

### [7:6] SWD_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING

- Description: Switch Node D Output Threshold High Side Voltage For Power Good Status
- Attribute: RW — Read/Write
- Default: 01 → +7.5% from the setting in Table 139, Register 0x23, [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +5% from the setting in Table 139, Register 0x23, [7:1] |
| 01 | +7.5% from the setting in Table 139, Register 0x23, [7:1] |
| 10 | +10% from the setting in Table 139, Register 0x23, [7:1] |
| 11 | Reserved |

### [5:4] SWD_OVER_VOLTAGE_THRESHOLD_SETTING

- Description: Switch Node D Output Regulator Threshold For Over Voltage Status[2]
- Attribute: RW — Read/Write
- Default: 10 → +12.5% from the setting in Table 139, Register 0x23, [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +7.5% from the setting in Table 139, Register 0x23, [7:1] |
| 01 | +10% from the setting in Table 139, Register 0x23, [7:1] |
| 10 | +12.5% from the setting in Table 139, Register 0x23, [7:1] |
| 11 | Reserved |

### [3:2] SWD_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING

- Description: Switch Node D Output Regulator Threshold For Under Voltage Lockout Status
- Attribute: RW — Read/Write
- Default: 00 → -10% from the setting in Table 139, Register 0x23, [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | -10% from the setting in Table 139, Register 0x23, [7:1] |
| 01 | -12.5% from the setting in Table 139, Register 0x23, [7:1] |
| 10 | Reserved |
| 11 | Reserved |

### [1:0] SWD_OUTPUT_SOFT_STOP_TIME

- Description: SWD Output Regulator Soft Stop Time After VR Disable[3]. The register Table 158, Register 0x36 [6] (MSB) plus this two bit register makes the 3 bit encoding.
- Attribute: RW — Read/Write
- Default: 00
- Note: the codes below are wider than this 2-bit field; the encoding combines bits from more than one field/register (see Description).

| Code (bin) | Meaning |
|---|---|
| 000 | 0.5 ms |
| 001 | 1 ms |
| 010 | 2 ms |
| 011 | 4 ms |
| 100 | 8 ms |
| 101 | 16 ms |
| 110 | 32 ms |
| 111 | 64 ms |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 190, Register 0x48.
- NOTE 2: The setting for the Over Voltage must be higher than Power Good High Side Voltage threshold in Table 138, Register 0x22,[7:6].
- NOTE 3: This is the time it takes for buck regulator to go from steady state voltage to 0 V.

## R25 (0x25) — SWB_VOLTAGE_SETTING, SWB_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

Region: Host Region | Source: JESD301-3 Table 141, p.163

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:1 | SWB_VOLTAGE_SETTING | RW | 011 1100 |
| 0 | SWB_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING | RW | 0 |

### [7:1] SWB_VOLTAGE_SETTING

- Description: Switch Node B Output Regulator Voltage Setting[3],[4]
- Attribute: RW — Read/Write
- Default: 011 1100 → 500 mV or 350 mV

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 0000000 | 0x00 | 200[5] mV or 200[6] mV |
| 0000001 | 0x01 | 205 mV or 202.5 mV |
| 0000010 | 0x02 | 210 mV or 205 mV |
| ... | ... | ... |
| 0111100 | 0x3C | 500 mV or 350 mV |
| ... | ... | ... |
| 1111101 | 0x7D | 825 mV or 512.5 mV |
| 1111110 | 0x7E | 830 mV or 515 mV |
| 1111111 | 0x7F | 835 mV or 517.5 mV |

### [0] SWB_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

- Description: Switch Node B Output Threshold Low Side Voltage For Power Good Status
- Attribute: RW — Read/Write
- Default: 0 → -5% from the setting in Table 141, Register 0x25, [7:1]

| Code (bin) | Meaning |
|---|---|
| 0 | -5% from the setting in Table 141, Register 0x25, [7:1] |
| 1 | -7.5% from the setting in Table 141, Register 0x25, [7:1] |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 191, Register 0x49.
- NOTE 2: If required, the host must update the settings in register Table 141, Register 0x25, [0], Table 142, Register 0x26, [7:2], and Table 136, Register 0x20 [3:2] first prior to updating the settings in the register Table 141, Register 0x25, [7:1].
- NOTE 3: PMIC guarantees efficiency spec and all electrical characteristics spec within a range of 450 mV to 550 mV or from 300 mV to 400 mV depending on the range selection.
- NOTE 4: After VR is enabled, the host may update this register to any new setting that it may desire. However to prevent false error trigger, the PMIC internally will increment the SWB output voltage setting by 5 or 2.5 mV at a time. The time it takes for PMIC to adjust the output voltage is 5 μs for each 5 mV increment. The host must wait sufficient time for PMIC to adjust to final value. As an example, if host adjusts the output voltage by 50 mV from the original value, the host must wait minimum of 50 μs before PMIC can guarantee the new output voltage. During this time, PMIC masks the PWR_GOOD output signal assertion to prevent any artificial error due to the crossing of the output voltage threshold setting. However, PMIC does assert PWR_GOOD output signal if there are any abnormal issues that triggers VR Disable command as described in Table 27. Further, PMIC does monitor PWR_GOOD input signal and executes power off config sequence registers if it is registered low when Table 154, Register 0x32 [5] = ‘1’.
- NOTE 5: Table 147, Register 0x2B, [3] = ‘0’; 5 mV step size.
- NOTE 6: Table 147, Register 0x2B, [3] = ‘1’; 2.5 mV step size.

## R26 (0x26) — SWB_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING, SWB_OVER_VOLTAGE_THRESHOLD_SETTING, SWB_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING, SWB_OUTPUT_SOFT_STOP_TIME

Region: Host Region | Source: JESD301-3 Table 142, p.164

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWB_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING | RW | 01 |
| 5:4 | SWB_OVER_VOLTAGE_THRESHOLD_SETTING | RW | 10 |
| 3:2 | SWB_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING | RW | 00 |
| 1:0 | SWB_OUTPUT_SOFT_STOP_TIME | RW | 00 |

### [7:6] SWB_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING

- Description: Switch Node B Output Threshold High Side Voltage For Power Good Status
- Attribute: RW — Read/Write
- Default: 01 → +7.5% from the setting in Table 141, Register 0x25, [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +5% from the setting in Table 141, Register 0x25, [7:1] |
| 01 | +7.5% from the setting in Table 141, Register 0x25, [7:1] |
| 10 | +10% from the setting in Table 141, Register 0x25, [7:1] |
| 11 | Reserved |

### [5:4] SWB_OVER_VOLTAGE_THRESHOLD_SETTING

- Description: Switch Node B Output Regulator Threshold For Over Voltage Status[3]
- Attribute: RW — Read/Write
- Default: 10 → +12.5% from the setting in Table 141, Register 0x25, [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +7.5% from the setting in Table 141, Register 0x25, [7:1] |
| 01 | +10% from the setting in Table 141, Register 0x25, [7:1] |
| 10 | +12.5% from the setting in Table 141, Register 0x25, [7:1] |
| 11 | Reserved |

### [3:2] SWB_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING

- Description: Switch Node B Output Regulator Threshold For Under Voltage Lockout Status
- Attribute: RW — Read/Write
- Default: 00 → -10% from the setting in Table 141, Register 0x25, [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | -10% from the setting in Table 141, Register 0x25, [7:1] |
| 01 | -12.5% from the setting in Table 141, Register 0x25, [7:1] |
| 10 | Reserved |
| 11 | Reserved |

### [1:0] SWB_OUTPUT_SOFT_STOP_TIME

- Description: SWB Output Regulator Soft Stop Time After VR Disable[4]. The register Table 158, Register 0x36 [5] (MSB) plus this two bit register makes the 3 bit encoding.
- Attribute: RW — Read/Write
- Default: 00
- Note: the codes below are wider than this 2-bit field; the encoding combines bits from more than one field/register (see Description).

| Code (bin) | Meaning |
|---|---|
| 000 | 0.5 ms |
| 001 | 1 ms |
| 010 | 2 ms |
| 011 | 4 ms |
| 100 | 8 ms |
| 101 | 16 ms |
| 110 | 32 ms |
| 111 | 64 ms |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 192, Register 0x4A.
- NOTE 2: If required, the host must update the settings in register Table 141, Register 0x25, [0], Table 142, Register 0x26, [7:2], and Table 136, Register 0x20 [3:2] first prior to updating the settings in the register Table 141, Register 0x25, [7:1].
- NOTE 3: The setting for the Over Voltage must be higher than Power Good High Side Voltage threshold in Table 142, Register 0x26,[7:6].
- NOTE 4: This is the time it takes for buck regulator to go from steady state voltage to 0 V.

## R27 (0x27) — SWC_VOLTAGE_SETTING, SWC_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

Region: Host Region | Source: JESD301-3 Table 143, p.165

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:1 | SWC_VOLTAGE_SETTING | RW | 011 1100 |
| 0 | SWC_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING | RW | 0 |

### [7:1] SWC_VOLTAGE_SETTING

- Description: Switch Node C Output Regulator Voltage Setting[3],[4]
- Attribute: RW — Read/Write
- Default: 011 1100 → 1800 mV or 2100 mV

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 0000000 | 0x00 | 1500[5] mV or 1500[6] mV |
| 0000001 | 0x01 | 1505 mV or 1510 mV |
| 0000010 | 0x02 | 1510 mV or 1520 mV |
| ... | ... | ... |
| 0111100 | 0x3C | 1800 mV or 2100 mV |
| ... | ... | ... |
| 1111101 | 0x7D | 2125 mV or 2750 mV |
| 1111110 | 0x7E | 2130 mV or 2760 mV |
| 1111111 | 0x7F | 2135 mV or 2770 mV |

### [0] SWC_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

- Description: Switch Node C Output Threshold Low Side Voltage For Power Good Status
- Attribute: RW — Read/Write
- Default: 0 → -5% from the setting in Table 143, Register 0x27, [7:1]

| Code (bin) | Meaning |
|---|---|
| 0 | -5% from the setting in Table 143, Register 0x27, [7:1] |
| 1 | -7.5% from the setting in Table 143, Register 0x27, [7:1] |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 193, Register 0x4B.
- NOTE 2: If required, the host must update the settings in register Table 143, Register 0x27, [0], Table 144, Register 0x28, [7:2], and Table 136, Register 0x20 [1:0] first prior to updating the settings in the register Table 143, Register 0x27, [7:1].
- NOTE 3: PMIC guarantees efficiency spec and all electrical characteristics spec within a range of 1750 mV to 1850 mV.
- NOTE 4: After VR is enabled, the host may update this register to any new setting that it may desire. However, to prevent false error triggers, the PMIC internally will increment the SWC output voltage setting by 5 or 10 mV at a time. The time it takes for PMIC to adjust the output voltage is 5 μs for each 5 mV increment. The host must wait sufficient time for PMIC to adjust to final value. As an example, if host adjusts the output voltage by 50 mV from the original value, the host must wait minimum of 50 μs before PMIC can guarantee the new output voltage. During this time, PMIC masks the PWR_GOOD output signal assertion to prevent any artificial error due to the crossing of the output voltage threshold setting. However, PMIC does assert PWR_GOOD output signal if there are any abnormal issues that triggers VR Disable command as described in Table 27. Further, PMIC does monitor PWR_GOOD input signal and executes power off config sequence registers if it is registered low when Table 154, Register 0x32 [5] = ‘1’.
- NOTE 5: Table 147, Register 0x2B, [0] = ‘0’; 5 mV step size.
- NOTE 6: Table 147, Register 0x2B, [0] = ‘1’; 10 mV step size.

## R28 (0x28) — SWC_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING, SWC_OVER_VOLTAGE_THRESHOLD_SETTING, SWC_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING, SWC_OUTPUT_SOFT_STOP_TIME

Region: Host Region | Source: JESD301-3 Table 144, p.166

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWC_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING | RW | 01 |
| 5:4 | SWC_OVER_VOLTAGE_THRESHOLD_SETTING | RW | 10 |
| 3:2 | SWC_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING | RW | 00 |
| 1:0 | SWC_OUTPUT_SOFT_STOP_TIME | RW | 00 |

### [7:6] SWC_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING

- Description: Switch Node C Output Threshold High Side Voltage For Power Good Status
- Attribute: RW — Read/Write
- Default: 01 → +7.5% from the setting in Table 143, Register 0x27, [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +5% from the setting in Table 143, Register 0x27, [7:1] |
| 01 | +7.5% from the setting in Table 143, Register 0x27, [7:1] |
| 10 | +10% from the setting in Table 143, Register 0x27, [7:1] |
| 11 | Reserved |

### [5:4] SWC_OVER_VOLTAGE_THRESHOLD_SETTING

- Description: Switch Node C Output Regulator Threshold For Over Voltage Status[3]
- Attribute: RW — Read/Write
- Default: 10 → +12.5% from the setting in Table 143, Register 0x27, [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +7.5% from the setting in Table 143, Register 0x27, [7:1] |
| 01 | +10% from the setting in Table 143, Register 0x27, [7:1] |
| 10 | +12.5% from the setting in Table 143, Register 0x27, [7:1] |
| 11 | Reserved |

### [3:2] SWC_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING

- Description: Switch Node C Output Regulator Threshold For Under Voltage Lockout Status
- Attribute: RW — Read/Write
- Default: 00 → -10% from the setting in Table 143, Register 0x27, [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | -10% from the setting in Table 143, Register 0x27, [7:1] |
| 01 | -12.5% from the setting in Table 143, Register 0x27, [7:1] |
| 10 | Reserved |
| 11 | Reserved |

### [1:0] SWC_OUTPUT_SOFT_STOP_TIME

- Description: SWC Output Regulator Soft Stop Time After VR Disable[4]. The register Table 158, Register 0x36 [4] (MSB) plus this two bit register makes the 3 bit encoding.
- Attribute: RW — Read/Write
- Default: 00
- Note: the codes below are wider than this 2-bit field; the encoding combines bits from more than one field/register (see Description).

| Code (bin) | Meaning |
|---|---|
| 000 | 1 ms |
| 001 | 2 ms |
| 010 | 4 ms |
| 011 | 8 ms |
| 100 | 16 ms |
| 101 | 32 ms |
| 110 | 64 ms |
| 111 | Vendor defined |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 194, Register 0x4C.
- NOTE 2: If required, the host must update the settings in register Table 143, Register 0x27, [0], Table 144, Register 0x28, [7:2], and Table 136, Register 0x20 [1:0] first prior to updating the settings in the register Table 143, Register 0x27, [7:1].
- NOTE 3: The setting for the Over Voltage must be higher than Power Good High Side Voltage threshold in Table 144, Register 0x28,[7:6].
- NOTE 4: This is the time it takes for buck regulator to go from steady state voltage to 0 V.

## R29 (0x29) — SWA_MODE_SELECT, SWA_SWITCHING_FREQ, SWD_MODE_SELECT, SWD_SWITCHING_FREQ

Region: Host Region | Source: JESD301-3 Table 145, p.167

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWA_MODE_SELECT | RW | 10 |
| 5:4 | SWA_SWITCHING_FREQ | RW | 00 |
| 3:2 | SWD_MODE_SELECT | RW | 10 |
| 1:0 | SWD_SWITCHING_FREQ | RW | 00 |

### [7:6] SWA_MODE_SELECT

- Description: Switch Node A Output Regulator Mode Selection
- Attribute: RW — Read/Write
- Default: 10 → COT; DCM (Constant on Time; Discontinuous Current Mode)

| Code (bin) | Meaning |
|---|---|
| 00 | Reserved |
| 01 | Reserved |
| 10 | COT; DCM (Constant on Time; Discontinuous Current Mode) |
| 11 | COT; Forced CCM (Constant on Time; Continuous Current Mode) |

### [5:4] SWA_SWITCHING_FREQ

- Description: Switch Node A Output Regulator Switching Frequency
- Attribute: RW — Read/Write
- Default: 00 → 750 KHz

| Code (bin) | Meaning |
|---|---|
| 00 | 750 KHz |
| 01 | Vendor Specific |
| 10 | Vendor Specific |
| 11 | Vendor Specific |

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
- Default: 00 → 750 KHz

| Code (bin) | Meaning |
|---|---|
| 00 | 750 KHz |
| 01 | Vendor Specific |
| 10 | Vendor Specific |
| 11 | Vendor Specific |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 195, Register 0x4D.
- NOTE 2: If required, the host must adjust this register first before issuing VR Enable command in Table 154, Register 0x32 [7].

## R2A (0x2A) — SWB_MODE_SELECT, SWB_SWITCHING_FREQ, SWC_MODE_SELECT, SWC_SWITCHING_FREQ

Region: Host Region | Source: JESD301-3 Table 146, p.168

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWB_MODE_SELECT | RW | 10 |
| 5:4 | SWB_SWITCHING_FREQ | RW | 00 |
| 3:2 | SWC_MODE_SELECT | RW | 10 |
| 1:0 | SWC_SWITCHING_FREQ | RW | 00 |

### [7:6] SWB_MODE_SELECT

- Description: Switch Node B Output Regulator Mode Selection
- Attribute: RW — Read/Write
- Default: 10 → COT; DCM (Constant on Time; Discontinuous Current Mode)

| Code (bin) | Meaning |
|---|---|
| 00 | Reserved |
| 01 | Reserved |
| 10 | COT; DCM (Constant on Time; Discontinuous Current Mode) |
| 11 | COT; Forced CCM (Constant on Time; Continuous Current Mode) |

### [5:4] SWB_SWITCHING_FREQ

- Description: Switch Node B Output Regulator Switching Frequency
- Attribute: RW — Read/Write
- Default: 00 → 750 KHz

| Code (bin) | Meaning |
|---|---|
| 00 | 750 KHz |
| 01 | Vendor Specific |
| 10 | Vendor Specific |
| 11 | Vendor Specific |

### [3:2] SWC_MODE_SELECT

- Description: Switch Node C Output Regulator Mode Selection
- Attribute: RW — Read/Write
- Default: 10 → COT; DCM (Constant on Time; Discontinuous Current Mode)

| Code (bin) | Meaning |
|---|---|
| 00 | Reserved |
| 01 | Reserved |
| 10 | COT; DCM (Constant on Time; Discontinuous Current Mode) |
| 11 | COT; Forced CCM (Constant on Time; Continuous Current Mode) |

### [1:0] SWC_SWITCHING_FREQ

- Description: Switch Node C Output Regulator Switching Frequency
- Attribute: RW — Read/Write
- Default: 00 → 750 KHz

| Code (bin) | Meaning |
|---|---|
| 00 | 750 KHz |
| 01 | Vendor Specific |
| 10 | Vendor Specific |
| 11 | Vendor Specific |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 196, Register 0x4E.
- NOTE 2: If required, the host must adjust this register first before issuing VR Enable command in Table 154, Register 0x32 [7].

## R2B (0x2B) — VOUT_1.8V_VOLTAGE_SETTING, SWA_VOLTAGE_STEP_SIZE, SWD_VOLTAGE_STEP_SIZE, SWB_VOLTAGE_STEP_SIZE, VOUT_1.0V_VOLTAGE_SETTING, SWC_VOLTAGE_STEP_SIZE

Region: Host Region | Source: JESD301-3 Table 147, p.169

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | VOUT_1.8V_VOLTAGE_SETTING | RW | 01 |
| 5 | SWA_VOLTAGE_STEP_SIZE | RW | 0 |
| 4 | SWD_VOLTAGE_STEP_SIZE | RW | 0 |
| 3 | SWB_VOLTAGE_STEP_SIZE | RW | 0 |
| 2:1 | VOUT_1.0V_VOLTAGE_SETTING | RW | 01 |
| 0 | SWC_VOLTAGE_STEP_SIZE | RW | 0 |

### [7:6] VOUT_1.8V_VOLTAGE_SETTING

- Description: VOUT 1.8 V LDO Output Voltage Setting[3]
- Attribute: RW — Read/Write
- Default: 01 → 1.8 V

| Code (bin) | Meaning |
|---|---|
| 00 | 1.7 V |
| 01 | 1.8 V |
| 10 | 1.9 V |
| 11 | 2.0 V |

### [5] SWA_VOLTAGE_STEP_SIZE

- Description: SWA Voltage Step Size
- Attribute: RW — Read/Write
- Default: 0 → 5 mV

| Code (bin) | Meaning |
|---|---|
| 0 | 5 mV |
| 1 | 10 mV |

### [4] SWD_VOLTAGE_STEP_SIZE

- Description: SWD Voltage Step Size
- Attribute: RW — Read/Write
- Default: 0 → 5 mV

| Code (bin) | Meaning |
|---|---|
| 0 | 5 mV |
| 1 | 10 mV |

### [3] SWB_VOLTAGE_STEP_SIZE

- Description: SWB Voltage Step Size
- Attribute: RW — Read/Write
- Default: 0 → 5 mV

| Code (bin) | Meaning |
|---|---|
| 0 | 5 mV |
| 1 | 2.5 mV |

### [2:1] VOUT_1.0V_VOLTAGE_SETTING

- Description: VOUT 1.0 V LDO Voltage Setting[4]
- Attribute: RW — Read/Write
- Default: 01 → 1.0 V

| Code (bin) | Meaning |
|---|---|
| 00 | 0.9 V |
| 01 | 1.0 V |
| 10 | 1.1 V |
| 11 | 1.2 V |

### [0] SWC_VOLTAGE_STEP_SIZE

- Description: SWC Voltage Step Size
- Attribute: RW — Read/Write
- Default: 0 → 5 mV

| Code (bin) | Meaning |
|---|---|
| 0 | 5 mV |
| 1 | 10 mV |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 199, Register 0x51.
- NOTE 2: If required, the host must adjust this register first before issuing VR Enable command in Table 154, Register 0x32 [7]. The host must also wait minimum of 5 μs after the adjustment before issuing VR Enable command.
- NOTE 3: The VOUT_1.8V Power Good threshold in register Table 130, Register 0x1A [2] is always fixed regardless of the setting in this register.
- NOTE 4: If required, the host must adjust this register one step at a time (0.1 V increment or decrement) to prevent false trigger of power good status and PWR_GOOD pin assertion. In other words, host should not increment or decrement 0.2 V or 0.3 V from its current setting.

## R2C (0x2C) — SWA_OUTPUT_SOFT_START_TIME, SWD_OUTPUT_SOFT_START_TIME

Region: Host Region | Source: JESD301-3 Table 148, p.170

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:5 | SWA_OUTPUT_SOFT_START_TIME | RW | 001 |
| 4 | RESERVED | RV | 0 |
| 3:1 | SWD_OUTPUT_SOFT_START_TIME | RW | 001 |
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

### [3:1] SWD_OUTPUT_SOFT_START_TIME

- Description: SWD Output Regulator Soft Start Time After VR Enable[4]
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

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 204, Register 0x5D.
- NOTE 2: If required, the host must adjust this register first before issuing VR Enable command in Table 154, Register 0x32 [7].
- NOTE 3: This is the time it takes for buck regulator to go from 0 V to steady state voltage (the actual voltage varies based on pre-programmed voltage).
- NOTE 4: This is the time it takes for buck regulator to go from 0 V to steady state voltage (the actual voltage varies based on pre-programmed voltage).

## R2D (0x2D) — SWB_OUTPUT_SOFT_START_TIME, SWC_OUTPUT_SOFT_START_TIME

Region: Host Region | Source: JESD301-3 Table 149, p.171

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:5 | SWB_OUTPUT_SOFT_START_TIME | RW | 001 |
| 4 | RESERVED | RV | 0 |
| 3:1 | SWC_OUTPUT_SOFT_START_TIME | RW | 001 |
| 0 | RESERVED | RW | 0 |

### [7:5] SWB_OUTPUT_SOFT_START_TIME

- Description: SWB Output Regulator Soft Start Time After VR Enable[3]
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

### [3:1] SWC_OUTPUT_SOFT_START_TIME

- Description: SWC Output Regulator Soft Start Time After VR Enable3
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
- Attribute: RW — Read/Write
- Default: 0

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 205, Register 0x5E.
- NOTE 2: If required, the host must adjust this register first before issuing VR Enable command in Table 154, Register 0x32 [7].
- NOTE 3: This is the time it takes for buck regulator to go from 0 V to steady state voltage (the actual voltage varies based on pre-programmed voltage)

## R2E (0x2E) — SWB_DVFSQ_VOLTAGE_SLEW_RATE, SWB_DISABLE_INPUT_PIN_ENABLE, DVFSQ_N_PIN_ENABLE, UNLOCK_PIN_ENABLE, PMIC_SHUTDOWN_TEMPERATURE_THRESHOLD

Region: Host Region | Source: JESD301-3 Table 150, p.172

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWB_DVFSQ_VOLTAGE_SLEW_RATE | RW | 11 |
| 5 | SWB_DISABLE_INPUT_PIN_ENABLE | RW | 1 |
| 4 | DVFSQ_N_PIN_ENABLE | RW | 0 |
| 3 | UNLOCK_PIN_ENABLE | RW | 1 |
| 2:0 | PMIC_SHUTDOWN_TEMPERATURE_THRESHOLD | RW | 100 |

### [7:6] SWB_DVFSQ_VOLTAGE_SLEW_RATE

- Description: SWB Output Voltage Slew Rate when transitioning from P3 to DVFSQ and DVFSQ to P3 state[1],[2]
- Attribute: RW — Read/Write
- Default: 11 → 1 mV/μs

| Code (bin) | Meaning |
|---|---|
| 00 | 15 mV/μs |
| 01 | 10 mV/μs |
| 10 | 5 mV/μs |
| 11 | 1 mV/μs |

### [5] SWB_DISABLE_INPUT_PIN_ENABLE

- Description: SWB_Disable Input Pin Enable[3]
- Attribute: RW — Read/Write
- Default: 1 → Enable; Input pin receiver is enabled

| Code (bin) | Meaning |
|---|---|
| 0 | Disable; Input pin receiver is disabled |
| 1 | Enable; Input pin receiver is enabled |

### [4] DVFSQ_N_PIN_ENABLE

- Description: DVFSQ_n Input Pin Enable[4]
- Attribute: RW — Read/Write
- Default: 0 → Disable; SWB output voltage setting is as configured in register Table 141, Register 0x25,[7:1], Table 147, Register 0x2B,[3].

| Code (bin) | Meaning |
|---|---|
| 0 | Disable; SWB output voltage setting is as configured in register Table 141, Register 0x25,[7:1], Table 147, Register 0x2B,[3]. |
| 1 | Enable[2]; SWB output voltage setting toggles between register Table 141, Register 0x25,[7:1],Table 147, Register 0x2B,[3] and register Table 166, Register 0x3E[7:1], Table 147, Register 0x2B,[3] depending on DVFSQ_n input pin transition. |

### [3] UNLOCK_PIN_ENABLE

- Description: Unlock Input Pin Enable[5],[6]
- Attribute: RW — Read/Write
- Default: 1 → Enable; When Unlock pin is high, the PMIC is in programmable mode (Table 151, Register 0x2F [2] = ‘1’); when Unlock pin is low, the PMIC is in secure mode (Table 151, Register 0x2F [2] = ‘0’).

| Code (bin) | Meaning |
|---|---|
| 0 | Disable; the input receiver is off and pin has no effect. |
| 1 | Enable; When Unlock pin is high, the PMIC is in programmable mode (Table 151, Register 0x2F [2] = ‘1’); when Unlock pin is low, the PMIC is in secure mode (Table 151, Register 0x2F [2] = ‘0’). |

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

**Notes**

- NOTE 1: At first power on, this bit is automatically configured identically by PMIC on its own as Table 206, Register 0x5F [2:1].
- NOTE 2: During the SWB output voltage transition, the PMIC masks the PWR_GOOD output signal assertion to prevent any artificial error due to the crossing of the output voltage threshold setting and keeps the PWR_GOOD signal Hi-Z. However, PMIC does assert PWR_GOOD output signal if there are any abnormal issues that triggers VR Disable command as described in Table 27. Further, PMIC does monitor PWR_GOOD input signal and executes power off config sequence registers if it is registered low when Table 154, Register 0x32 [5] = ‘1’.
- NOTE 3: At first power on, this bit is automatically configured identically by PMIC on its own as Table 186, Register 0x44 [0].
- NOTE 4: This register cannot be cleared by the controller when Table 114, Register 0x0A [0] = ‘1’.
- NOTE 5: At first power on, this bit is automatically configured identically by PMIC on its own as Table 206, Register 0x5F [3].
- NOTE 6: This register is automatically cleared to ‘0’ by PMIC when it enters the Locked security state.

## R2F (0x2F) — SWA_REGULATOR_CONTROL, SWD_REGULATOR_CONTROL, SWB_REGULATOR_CONTROL, SWC_REGULATOR_CONTROL, SECURE_MODE, MASK_BITS_REGISTER_CONTROL

Region: Host Region | Source: JESD301-3 Table 151, p.173

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | RESERVED | RV | 0 |
| 6 | SWA_REGULATOR_CONTROL | RW | 0 |
| 5 | SWD_REGULATOR_CONTROL | RW | 0 |
| 4 | SWB_REGULATOR_CONTROL | RW | 0 |
| 3 | SWC_REGULATOR_CONTROL | RW | 0 |
| 2 | SECURE_MODE | RW | 0 |
| 1:0 | MASK_BITS_REGISTER_CONTROL | RW | 10 |

### [7] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [6] SWA_REGULATOR_CONTROL

- Description: Disable SWA Regulator Output[1],[2]
- Attribute: RW — Read/Write
- Default: 0 → Disable Switch Node A Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Disable Switch Node A Output Regulator |
| 1 | Enable Switch Node A Output Regulator |

### [5] SWD_REGULATOR_CONTROL

- Description: Disable SWD Regulator Output,[1],[2]
- Attribute: RW — Read/Write
- Default: 0 → Disable Switch Node D Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Disable Switch Node D Output Regulator |
| 1 | Enable Switch Node D Output Regulator |

### [4] SWB_REGULATOR_CONTROL

- Description: Disable SWB Regulator Output,[1],[2]
- Attribute: RW — Read/Write
- Default: 0 → Disable Switch Node B Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Disable Switch Node B Output Regulator |
| 1 | Enable Switch Node B Output Regulator |

### [3] SWC_REGULATOR_CONTROL

- Description: Disable SWC Regulator Output,,[1],[2]
- Attribute: RW — Read/Write
- Default: 0 → Disable Switch Node C Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Disable Switch Node C Output Regulator |
| 1 | Enable Switch Node C Output Regulator |

### [2] SECURE_MODE

- Description: PMIC Mode Operation[3]
- Attribute: RW — Read/Write
- Default: 0 → Secure Mode Operation[4],[5],[6]

| Code (bin) | Meaning |
|---|---|
| 0 | Secure Mode Operation[4],[5],[6] |
| 1 | Programmable Mode Operation |

### [1:0] MASK_BITS_REGISTER_CONTROL

- Description: Mask Bits Register Control[7]
- Attribute: RW — Read/Write
- Default: 10 → Mask GSI_n and PWR_GOOD Signals (neither PWR_GOOD asserts nor GSI_n asserts)

| Code (bin) | Meaning |
|---|---|
| 00 | Mask GSI_n Signal Only (PWR_GOOD Signal asserts) |
| 01 | Mask PWR_GOOD Signal Only (GSI_n Signal asserts) |
| 10 | Mask GSI_n and PWR_GOOD Signals (neither PWR_GOOD asserts nor GSI_n asserts) |
| 11 | Reserved |

**Notes**

- NOTE 1: This bit must be used only after power up sequence (after VR Enable command). At first power up, PMIC automatically updates the status of this register to ‘1’ after VR Enable command. When VR Enable command is registered, the PMIC updates this register based on Power On Sequence Configuration (0 to 3) setting. If enabled in Power On Sequence Configuration 0 to 3 registers, only then, under programmable mode of operation, the PMIC’s output regulator can be disabled by clearing this bit and they can be re-enabled again by setting this bit. The PMIC does not alter its Power Good output signal and keeps it asserted High. If any regulator is not enabled in Power on Sequence Configuration 0 to 3, it cannot be enabled using this register. For example, if only SWA is enabled and SWB and SWC are not enabled in Table 182, Register 0x40 [7:0] to Table 185, Register 0x43 [7:0], then only SWA can be disabled and then re-enabled again but SWB and SWC cannot be enabled using Table 151, Register 0x2F [6:3].
- NOTE 2: In programmable mode, after VR enable command, if any output regulators are disabled by clearing Table 151, Register 0x2F [6:3] and then if host issues VR Disable command or PMIC internally triggers VR Disable command, the PMIC keeps the disabled output regulator in Table 151, Register 0x2F[6:3] off and remaining output regulators are disabled by following the Power Off Sequence Configuration 0 to 3 settings.
- NOTE 3: At first power on, this register is automatically configured identically by PMIC on its own as Table 206, Register 0x5F [7].
- NOTE 4: This bit must be configured before issuing VR Enable command. If this bit is configured to ‘0’, when PMIC registers VR Enable command, all registers bits starting Table 125, Register 0x15 to Table 151, Register 0x2F, Table 154, Register 0x32 [7,5:0] in host region as well as Table 182, Register 0x40 to Register 0x6F in the CAMM2 vendor region are secured and host cannot change unless the PMIC goes through power cycle.
- NOTE 5: Simultaneous usage of programmable mode (i.e., Table 151, Register 0x2F [2] = ‘1’), PWR_GOOD as IO (i.e., Table 154, Register 0x32 [5] = ‘1’), and P1 State Enable (i.e., Table 130, Register 0x1A [4] = ‘1’) is considered an illegal configuration when VR_EN pin is intended to be used; otherwise it is a valid configuration if VR_EN command is used on I2C/I3C Basic bus.
- NOTE 6: When Unlock pin is enabled, the PMIC sets this register to ‘1’ when the Unlock input is high and ‘0’ when the Unlock input is low.
- NOTE 7: Applies to Mask Registers Table 125, Register 0x15 [5:2,0], Table 126, Register 0x16 [7,5,3:0], Table 127, Register 0x17 [7:2], Table 128, Register 0x18 [7:0], and Table 129, Register 0x19 [2] when any one or more Mask registers are set to ‘1’. If all Mask registers are configured as ‘0’, the setting in this register (Table 151, Register 0x2F [1:0]) does not apply.

## R30 (0x30) — ADC_ENABLE, ADC_SELECT, REGISTER_ADDRESSING_MODE, ADC_REGISTER_UPDATE_FREQUENCY

Region: Host Region | Source: JESD301-3 Table 152, p.175

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
| 0001 | 0x1 | SWD Output Voltage |
| 0010 | 0x2 | SWB Output Voltage |
| 0011 | 0x3 | SWC Output Voltage |
| 0100 | 0x4 | Reserved |
| 0101 | 0x5 | VIN_Bulk Input Voltage |
| 0110 | 0x6 | Reserved |
| 0111 | 0x7 | Reserved |
| 1000 | 0x8 | VOUT_1.8V Output Voltage |
| 1001 | 0x9 | VOUT_1.0V Output Voltage |
| 1111 | 0xF | VBIAS Output Voltage |

### [2] REGISTER_ADDRESSING_MODE

- Description: Register Addressing for I2C and I3C Protocol[3]
- Attribute: RW — Read/Write
- Default: 0 → 1 Byte address; Configuration register space limited to 256 Bytes

| Code (bin) | Meaning |
|---|---|
| 0 | 1 Byte address; Configuration register space limited to 256 Bytes |
| 1 | 2 Byte address; Configuration register space up to 64K Bytes |

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

- NOTE 1: Disables the ADC function completely. Applies to voltage readout in Table 153, Register 0x31 [7:0], as well as current or power readout in Table 116, Register 0x0C [7:0], Table 117, Register 0x0D [7:0], Table 118, Register 0x0E [7:0], Table 119, Register 0x0F [7:0], Table 168, Register 0x100 [7:0], Table 169, Register 0x102 [7:0], Table 170, Register 0x103 [7:0], Table 171, Register 0x104 [7:0], and Table 172, Register 0x105 [7:0]. When ADC is disabled, the PMIC does not report warning status in Table 113, Register 0x09 [3:0] as Table 132, Register 0x1C [7:0] to Table 135, Register 0x1F [7:0] does not apply. The ADC disable function does not apply to thermal sensor temperature readout in Table 155, Register 0x33 [7:5] as well as high temperature warning and critical temperature shutdown.
- NOTE 2: The host shall wait minimum of 9 ms delay after the input selection for ADC readout and the actual readout from Table 153, Register 0x31 to get the latest reading.
- NOTE 3: When there is a change in addressing mode, STOP operation is required on I2C or I3C bus.
- NOTE 4: For average output current or power measurement in registers Table 116, Register 0x0C [7:0],Table 117, Register 0x0D [7:0], Table 118, Register 0x0E [7:0], and Table 119, Register 0x0F [7:0].
- NOTE 5: This register represents how often the registers are updated. The internal sampling rate is vendor specific.

## R31 (0x31) — ADC_READ

Region: Host Region | Source: JESD301-3 Table 153, p.176

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | ADC_READ | RO | 0 |

### [7:0] ADC_READ

- Description: ADC Output Voltage Reading[1](Applies to SW[A:D], VOUT_1.8V, VOUT_1.0V)
- Attribute: RO — Read Only (writes have no effect)
- Default: 0

**When: ADC Output Voltage Reading[1](Applies to SW[A:D], VOUT_1.8V, VOUT_1.0V)**

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

**When: ADC Output Voltage Reading[3] (Applies to VBias output Voltage)**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | 25 mV |
| 00000010 | 0x02 | 50 mV |
| ... | ... | ... |
| 11111111 | 0xFF | ≥ 6375 mV |

**Notes**

- NOTE 1: Only valid when Table 152, Register 0x30 [6:3] = ‘0000’ or ‘0001’ or ‘0010’ or ‘0011’ or ‘1000’ or ‘1001’.
- NOTE 2: Only valid when Table 152, Register 0x30 [6:3] = ‘0101’.
- NOTE 3: Only valid when Table 152, Register 0x30 [6:3] = ‘1111’.

## R32 (0x32) — VR_ENABLE, MANAGEMENT_INTERFACE_SELECTION, PWR_GOOD_IO_TYPE, PWR_GOOD_OUTPUT_SIGNAL_CONTROL, ADC_ACCURACY_STEP_SIZE

Region: Host Region | Source: JESD301-3 Table 154, p.177

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | VR_ENABLE | RW | 0 |
| 6 | MANAGEMENT_INTERFACE_SELECTION | RO | 0 |
| 5 | PWR_GOOD_IO_TYPE | RW | 0 |
| 4:3 | PWR_GOOD_OUTPUT_SIGNAL_CONTROL | RW | 0 |
| 2 | RESERVED | RV | 0 |
| 1:0 | ADC_ACCURACY_STEP_SIZE | RW | 01 |

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

### [5] PWR_GOOD_IO_TYPE

- Description: PMIC PWR_GOOD Output Signal Type[6]
- Attribute: RW — Read/Write
- Default: 0 → Output Only

| Code (bin) | Meaning |
|---|---|
| 0 | Output Only |
| 1 | Input and Output[7] |

### [4:3] PWR_GOOD_OUTPUT_SIGNAL_CONTROL

- Description: PMIC PWR_GOOD Output Signal Control
- Attribute: RW — Read/Write
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 0x | PMIC controls PWR_GOOD on its own based on internal status |
| 10 | PWR_GOOD Output Low |
| 11 | PWR_GOOD Output Floats[8] |

### [2] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [1:0] ADC_ACCURACY_STEP_SIZE

- Description: ADC Accuracy Step Size All other encodings are reserved
- Attribute: RW — Read/Write
- Default: 01 → 31.25 mA or 31.25 mW[10]

| Code (bin) | Meaning |
|---|---|
| 00 | 125 mA or 125 mW[9] |
| 01 | 31.25 mA or 31.25 mW[10] |

**Notes**

- NOTE 1: The PMIC updates this bit when VR_EN signal transition to high or when host issues VR Enable command over I2C/I3C Basic bus; whichever comes first. PMIC also updates this bit when VR_EN signal transitions to low or when host issues VR Disable command over I2C/I3C Basic bus in programmable mode; whichever comes first. Further, PMIC updates this bit when PWR_GOOD input is low (if Table 154, Register 0x32 [5] = ‘1’) or when PMIC internally generates VR Disable command due to fault condition regardless of PMIC’s VR_EN signal input status.
- NOTE 2: After this bit is set to ‘1’, the PMIC executes Power On Sequence configuration 0 (Table 182, Register 0x40) to Power On Sequence configuration 3 (Table 185, Register 0x43) registers. At least one bit in Table 182, Register 0x40 [6:3] must be set to ‘1’ to issue VR Enable (either with VR_EN pin or over I2C/I3C Basic bus) command.
- NOTE 3: The host shall ensure that prior to issuing VR Enable command, there is no pending IBI interrupt (i.e., Table 114, Register 0x0A [1] = ‘1’). After host issues VR Enable command (either with VR_EN pin or over I2C/I3C Basic bus), the PMIC may NACK any I2C or I3C Basic bus transactions by host until tPMIC_PWR_GOOD_OUT timing parameter is satisfied. The host shall not access any device specific registers or issue CCCs until tPMIC_PWR_GOOD_Out parameter is satisfied. The PMIC device may request for an IBI during power up sequence (i.e., during tPMIC_PWR_GOOD_Out time) if there is any event.
- NOTE 4: An exception to this register is applied. When PMIC is operating in secure mode of operation and PWR_GOOD input is low (if Table 154, Register 0x32 [5] = ‘1’), the PMIC unlocks this register. The PMIC allows host to issue VR Enable command. After host issues VR Enable command, the PMIC re-locks this register.
- NOTE 5: This register is automatically updated when SETAASA CCC or RSTDAA CCC is registered by the PMIC device or when PMIC device goes through bus reset as described in clause 5.4.13 regardless of whether PMIC is in secure mode or programmable mode of operation. This register can be read by the Host through normal Read operation but it cannot be written with normal write operation either in I2C mode or I3C Basic mode of operation. When this register is updated, it takes effect when there is a next START operation (i.e., after STOP operation).
- NOTE 6: This bit must be configured before issuing VR Enable command.
- NOTE 7: Simultaneous usage of programmable mode (i.e., Table 151, Register 0x2F [2] = ‘1’), PWR_GOOD as IO (i.e., Table 154, Register 0x32 [5] = ‘1’), and P1 State Enable (i.e., Table 130, Register 0x1A [4] = ‘1’) is considered an illegal configuration when VR_EN pin is intended to be used; otherwise it is a valid configuration if VR_EN command is used on I2C/I3C Basic bus.
- NOTE 8: When this encoding is set, the PMIC always floats the PWR_GOOD output signal even when there is an internal VR Disable command due to fault condition.
- NOTE 9: See registers Table 116, Register 0x0C to Table 119, Register 0x0F for current or power measurement.
- NOTE 10: See registers Table 168, Register 0x100 to Table 172, Register 0x105 for current or power measurement.

## R33 (0x33) — TEMPERATURE_MEASUREMENT, VIN_BULK_UNDER_VOLTAGE_LOCKOUT_STATUS, VOUT_1.0V_OUTPUT_POWER_GOOD_STATUS, DVFSQ_N_PIN_INPUT_LEVEL_STATUS, UNLOCK_PIN_INPUT_LEVEL_STATUS

Region: Host Region | Source: JESD301-3 Table 155, p.179

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:5 | TEMPERATURE_MEASUREMENT | RO | 0 |
| 4 | RESERVED | RV | 0 |
| 3 | VIN_BULK_UNDER_VOLTAGE_LOCKOUT_STATUS | RO | 0 |
| 2 | VOUT_1.0V_OUTPUT_POWER_GOOD_STATUS | RO | 0 |
| 1 | DVFSQ_N_PIN_INPUT_LEVEL_STATUS | RO | - |
| 0 | UNLOCK_PIN_INPUT_LEVEL_STATUS | RO | - |

### [7:5] TEMPERATURE_MEASUREMENT

- Description: PMIC Temperature[1]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 000 | < 85 0C |
| 001 | 85 0C |
| 010 | 95 0C |
| 011 | 105 0C |
| 100 | 115 0C |
| 101 | 125 0C |
| 110 | 135 0C |
| 111 | > 140 0C |

### [4] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [3] VIN_BULK_UNDER_VOLTAGE_LOCKOUT_STATUS

- Description: VIN_Bulk Under Voltage Lockout Status[2]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No Under Voltage Lockout

| Code (bin) | Meaning |
|---|---|
| 0 | No Under Voltage Lockout |
| 1 | Under Voltage Lockout |

### [2] VOUT_1.0V_OUTPUT_POWER_GOOD_STATUS

- Description: VOUT_1.0V LDO Output Power Good Status[3]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → Power Good

| Code (bin) | Meaning |
|---|---|
| 0 | Power Good |
| 1 | Power Not Good |

### [1] DVFSQ_N_PIN_INPUT_LEVEL_STATUS

- Description: DVFSQ_n Input Pin Level Status[4],[5],[6]
- Attribute: RO — Read Only (writes have no effect)
- Default: -

| Code (bin) | Meaning |
|---|---|
| 0 | Low |
| 1 | High |

### [0] UNLOCK_PIN_INPUT_LEVEL_STATUS

- Description: Unlock Pin Input Level Status[6],[7]
- Attribute: RO — Read Only (writes have no effect)
- Default: -

| Code (bin) | Meaning |
|---|---|
| 0 | Low |
| 1 | High |

**Notes**

- NOTE 1: The accuracy of the temperature readout code is + 5 0C.
- NOTE 2: This register is set when VIN_Bulk input voltage goes below 3.0 V (the exact voltage threshold is vendor specific).
- NOTE 3: This register is set when VOUT_1.0V output drops below the threshold setting in register Table 130, Register 0x1A [0].
- NOTE 4: This register status is only applicable if Table 150, Register 0x2E [4] = ‘1’. This register bit reflects the voltage level status on the DVFSQ_n input pin. In the rare event where there is a simultaneous operation of reading this register and DVFSQ_n pin transition, the PMIC may not reflect the latest status. It is recommended that host performs more than one register read operation to get the latest input pin status.
- NOTE 5: This register (Table 155, Register 0x33 [1]) status does not indicate the PMIC DVFSQ Power State Status (Table 114, Register 0x0A [0]). DVFSQ power state entry is determined by the detection of high to low or low to high voltage edge transition or by VR Disable command (either with VR_EN pin de-assertion or via I2C/I3C bus command).
- NOTE 6: The controller cannot clear this register via any I2C/I3C bus command.
- NOTE 7: This register status is only applicable if Table 150, Register 0x2E [3] = ‘1’. This register bit reflects the voltage level status on the Unlock input pin. In the rare event where there is a simultaneous operation of reading this register and Unlock pin transition, the PMIC may not reflect the latest status. It is recommended that host performs more than one register read operation to get the latest input pin status. If Table 150, Register 0x2E [3] = ‘0’, this register is always ‘0’.

## R34 (0x34) — PEC_ENABLE, IBI_ENABLE, PARITY_DISABLE, HID_CODE

Region: Host Region | Source: JESD301-3 Table 156, p.180

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | PEC_ENABLE | RO | 0 |
| 6 | IBI_ENABLE | RO | 0 |
| 5 | PARITY_DISABLE | RO | 0 |
| 4 | RESERVED | RV | 0 |
| 3:1 | HID_CODE | RO | 111 |
| 0 | RESERVED | RV | 0 |

### [7] PEC_ENABLE

- Description: Packet Error Code Enable[2] (Applicable Only if Table 154, Register 0x32 [6] = ‘1’)
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → Disable

| Code (bin) | Meaning |
|---|---|
| 0 | Disable |
| 1 | Enable |

### [6] IBI_ENABLE

- Description: In Band Interrupt Enable[3] (Applicable Only if Table 154, Register 0x32 [6] = ‘1’)
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → Disable

| Code (bin) | Meaning |
|---|---|
| 0 | Disable |
| 1 | Enable |

### [5] PARITY_DISABLE

- Description: T Bit Parity Code Disable2 (Applicable Only if Table 154, Register 0x32 [6] = ‘1’.)
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

- NOTE 1: The write (or update) transaction to this register must be followed by STOP operation to allow PMIC device to update the setting.
- NOTE 2: This register is automatically updated when RSTDAA CCC is registered by the PMIC device or when PMIC device goes through bus reset as described in clause 5.4.13. This register cannot be written by the Host through normal write operation either in I2C mode or I3C mode of operation. This register is updated with DEVCTRL CCC with RegMod=’0’ only. This register cannot be written with DEVCTRL CCC with RegMod = ‘1’.
- NOTE 3: This register is automatically updated when ENEC CCC or DISEC CCC or RSTDAA CCC is registered by the PMIC device or when PMIC device goes through bus reset as described in clause 5.4.13. This register can be read by the Host through normal Read operation but it cannot be written with normal write operation either in I2C mode or I3C mode of operation. This register cannot be written with DEVCTRL CCC with RegMod = ‘1’.
- NOTE 4: When Parity function is disabled, the PMIC simply ignores the “T” bit information from the Host. The host may actually choose to compute the parity and send that information in “T” bit or simply drive static low or high in “T” bit.
- NOTE 5: This register is updated when PMIC device receives SETHID CCC or when PMIC device goes through bus reset as described in clause 5.4.13. This register cannot be written with DEVCTRL CCC with RegMod = ‘1’.

## R35 (0x35) — ERROR_INJECTION_ENABLE, ERROR_INJECTION_RAIL_SELECTION, OVER_VOLTAGE_UNDER_VOLTAGE_SELECT, MISC_ERROR_INJECTION_TYPE

Region: Host Region | Source: JESD301-3 Table 157, p.181

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

- Description: Error Injection - Input Rail and Output Rail Selection[4]
- Attribute: RW — Read/Write
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 000 | Undefined |
| 001 | SWA Output Only |
| 010 | SWD Output Only |
| 011 | SWB Output Only |
| 100 | SWC Output Only |
| 101 | VIN_Bulk Input Only |
| 110 | Reserved |
| 111 | Do Not Use |

### [3] OVER_VOLTAGE_UNDER_VOLTAGE_SELECT

- Description: Over Voltage or Under Voltage Selection for Bits [6:4][5]
- Attribute: RW — Read/Write
- Default: 0 → Over Voltage

| Code (bin) | Meaning |
|---|---|
| 0 | Over Voltage |
| 1 | Under Voltage[6] |

### [2:0] MISC_ERROR_INJECTION_TYPE

- Description: Miscellaneous Error Injection Type[7]
- Attribute: RW — Read/Write
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 000 | Undefined |
| 001 | Reserved |
| 010 | Critical Temperature Shutdown |
| 011 | High Temperature Warning Threshold |
| 100 | VOUT_1.8V LDO Power Good |
| 101 | High Current Consumption Warning[8] |
| 110 | Reserved |
| 111 | Current Limiter Warning9 |

**Notes**

- NOTE 1: Refer to clause 4.18 for error function usage model. The host can erase the error log registers (Table 108, Register 0x04 to Table 111, Register 0x07) by writing 0x74 to Table 161, Register 0x39.
- NOTE 2: To exit from Error Injection Mode, the PMIC must go through power cycle of VIN_Bulk input supply.
- NOTE 3: When error function is invoked by setting bit [7] = ‘1’, the setting of bits [6:4, 2:0] = ‘000 000’ is considered an illegal setting.
- NOTE 4: This register Table 157, Register 0x35 [6:4] is only applicable if Table 157, Register 0x35 [2:0] is ‘000’. Any value other than ‘000’ in both Table 157, Register 0x35 [6:4] and Table 157, Register 0x35 [2:0] is considered an illegal setting and PMIC operation is not guaranteed.
- NOTE 5: This register Table 157, Register 0x35 [3] is only applicable if bits [6:4] is anything other than ‘000’.
- NOTE 6: The under voltage selection only applies to SWx output rails and VIN_Bulk input.
- NOTE 7: This register Table 157, Register 0x35 [2:0] is only applicable if Table 157, Register 0x35 [6:3] is ‘0000’. Any value other than ‘000’ in both Table 157, Register 0x35 [6:4] and Table 157, Register 0x35 [2:0] is considered an illegal setting and PMIC operation is not guaranteed.
- NOTE 8: Applies to all enabled SWx output regulators at the same time.

## R36 (0x36) — SWA_OUTPUT_SOFT_STOP_TIME_EXTENSION, SWD_OUTPUT_SOFT_STOP_TIME_EXTENSION, SWB_OUTPUT_SOFT_STOP_TIME_EXTENSION, SWC_OUTPUT_SOFT_STOP_TIME_EXTENSION, ACOUSTIC_NOISE_PREVENTION_CONTROL

Region: Host Region | Source: JESD301-3 Table 158, p.182

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | SWA_OUTPUT_SOFT_STOP_TIME_EXTENSION | RW | 0 |
| 6 | SWD_OUTPUT_SOFT_STOP_TIME_EXTENSION | RW | 0 |
| 5 | SWB_OUTPUT_SOFT_STOP_TIME_EXTENSION | RW | 0 |
| 4 | SWC_OUTPUT_SOFT_STOP_TIME_EXTENSION | RW | 0 |
| 3:1 | ACOUSTIC_NOISE_PREVENTION_CONTROL | RW | 001 |
| 0 | RESERVED | RV | 0 |

### [7] SWA_OUTPUT_SOFT_STOP_TIME_EXTENSION

- Description: SWA Output Regulator Soft Stop Time After VR Disable. This register bit (MSB) plus 2 bit register Table 138, Register 0x22, [1:0] makes 3 bit register encoding.[1]
- Attribute: RW — Read/Write
- Default: 0
- Values: no per-value encoding is listed in the spec for this field.

### [6] SWD_OUTPUT_SOFT_STOP_TIME_EXTENSION

- Description: SWD Output Regulator Soft Stop Time After VR Disable. This register bit (MSB) plus 2 bit register Table 140, Register 0x24 [1:0] makes 3 bit register encoding.[2]
- Attribute: RW — Read/Write
- Default: 0
- Values: no per-value encoding is listed in the spec for this field.

### [5] SWB_OUTPUT_SOFT_STOP_TIME_EXTENSION

- Description: SWB Output Regulator Soft Stop Time After VR Disable. This register bit (MSB) plus 2 bit register Table 142, Register 0x26, [1:0] makes 3 bit register encoding.[3]
- Attribute: RW — Read/Write
- Default: 0
- Values: no per-value encoding is listed in the spec for this field.

### [4] SWC_OUTPUT_SOFT_STOP_TIME_EXTENSION

- Description: SWC Output Regulator Soft Stop Time After VR Disable. This register bit (MSB) plus 2 bit registerTable 144, Register 0x28,[1:0] makes 3 bit register encoding.[4]
- Attribute: RW — Read/Write
- Default: 0
- Values: no per-value encoding is listed in the spec for this field.

### [3:1] ACOUSTIC_NOISE_PREVENTION_CONTROL

- Description: Acoustic Noise Prevention Control Feature
- Attribute: RW — Read/Write
- Default: 001 → Enable; Switching frequency threshold = 50 KHz

| Code (bin) | Meaning |
|---|---|
| 000 | Feature is disabled |
| 001 | Enable; Switching frequency threshold = 50 KHz |
| 010 | Enable; Switching frequency threshold = 40 KHz |
| 011 | Enable; Switching frequency threshold = 30 KHz |
| 100 | Enable; Switching frequency threshold = 20 KHz |

### [0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 186, Register 0x44 [7].
- NOTE 2: At first power on, this register is automatically configured identically by PMIC on its own as Table 186, Register 0x44 [6].
- NOTE 3: At first power on, this register is automatically configured identically by PMIC on its own as Table 186, Register 0x44 [5].
- NOTE 4: At first power on, this register is automatically configured identically by PMIC on its own as Table 186, Register 0x44 [4].

## R37 (0x37) — CAMM2_VENDOR_MEMORY_REGION_PASSWORD_LOWER_BYTE

Region: Host Region | Source: JESD301-3 Table 159, p.182

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | CAMM2_VENDOR_MEMORY_REGION_PASSWORD_LOWER_BYTE | WO | - |

### [7:0] CAMM2_VENDOR_MEMORY_REGION_PASSWORD_LOWER_BYTE

- Description: CAMM2 Vendor Memory Region (0x40 - 0x6F) Password - Lower Byte [7:0] = Code
- Attribute: WO — Write Only (reads return 0)
- Default: -
- Values: no per-value encoding is listed in the spec for this field.

## R38 (0x38) — CAMM2_VENDOR_MEMORY_REGION_PASSWORD_UPPER_BYTE

Region: Host Region | Source: JESD301-3 Table 160, p.182

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | CAMM2_VENDOR_MEMORY_REGION_PASSWORD_UPPER_BYTE | WO | - |

### [7:0] CAMM2_VENDOR_MEMORY_REGION_PASSWORD_UPPER_BYTE

- Description: CAMM2 Vendor Memory Region (0x40 - 0x6F) Password - Upper Byte [7:0] = Code
- Attribute: WO — Write Only (reads return 0)
- Default: -
- Values: no per-value encoding is listed in the spec for this field.

## R39 (0x39) — (unnamed)

Region: Host Region | Source: JESD301-3 Table 161, p.183

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | (unnamed) | RW | 0x00 R39 |

### [7:0] (unnamed)

- Attribute: RW — Read/Write
- Default: 0x00 R39
- Note: the codes below are wider than this 8-bit field; the encoding combines bits from more than one field/register (see Description).

**When: Host Region Codes**

| Code (bin) | Meaning |
|---|---|
| 0x74 | Clear Registers R04 to R07, Erase MTP memory for R04 Register to R07. |

**When: CAMM2 Vendor Region (0x40 to 0x6F) Write Codes**

| Code (bin) | Meaning |
|---|---|
| 0x40 | Unlock CAMM2 Vendor Region. Password needs to be present in R37 & R38 registers. |
| 0x00 | Lock CAMM2 Vendor Region. |
| 0x80 | Burn CAMM2 Vendor Region Password. New password needs to be present in R37 & R38. |
| 0x81 | Burn CAMM2 Vendor Region - 0x40 to 0x4F |
| 0x82 | Burn CAMM2 Vendor Region - 0x50 to 0x5F |
| 0x85 | Burn CAMM2 Vendor Region - 0x60 to 0x6F (except for R6D[4,0], R6E[4,0]) |
| 0x86 | Clear CAMM2 Vendor Region Registers: R6D[4,0], R6E[4,0] |

**When: CAMM2 Vendor Region (0x40 to 0x6F) Read Codes**

| Code (bin) | Meaning |
|---|---|
| 0x5A | Burning is complete in CAMM2 Vendor region. |

## R3A (0x3A) — DEFAULT_READ_ADDRESS_POINTER_ENABLE, DEFAULT_READ_STARTING_ADDRESS, BURST_LENGTH_FOR_READ_DEFAULT_ADDR_POINTER

Region: Host Region | Source: JESD301-3 Table 162, p.183

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
| 1 | Enable Default Address Pointer; Address selected by register bits [5:4] |

### [5:4] DEFAULT_READ_STARTING_ADDRESS

- Description: Default Read Address Pointer Selection when PMIC sees STOP operation[3]
- Attribute: RW — Read/Write
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 00 | R08 |
| 01 | R0C |
| 10 | R100 |
| 11 | Reserved |

### [3:2] BURST_LENGTH_FOR_READ_DEFAULT_ADDR_POINTER

- Description: Burst Length (# of Bytes) to be transferred for Read Default Address Pointer Mode[4]
- Attribute: RW — Read/Write
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 00 | 2 Bytes |
| 01 | 4 Bytes |
| 10 | 8 Bytes |
| 11 | 16 Bytes |

### [1:0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

**Notes**

- NOTE 1: The write (or update) transaction to this register must be followed by STOP operation to allow the PMIC device to update the setting.
- NOTE 2: The register setting in R3A [5:4] is a don’t care.
- NOTE 3: This register is only applicable if R3A [6] = ‘1’.
- NOTE 4: This register is only applicable if R3A [6] = ‘1’ and R34 [7] = ‘1’.

## R3B (0x3B) — REVISION_ID_MAJOR_STEPPING, REVISION_ID_MINOR_STEPPING, PMIC_PART_ID

Region: Host Region | Source: JESD301-3 Table 163, p.184

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | RESERVED | RV | 0 |
| 5:4 | REVISION_ID_MAJOR_STEPPING | ROA | - |
| 3:1 | REVISION_ID_MINOR_STEPPING | ROA | - |
| 0 | PMIC_PART_ID | ROA | 1 |

### [7:6] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

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

### [0] PMIC_PART_ID

- Description: Client PMIC Part ID Identification
- Attribute: ROA — Read Only (writes have no effect); Persistent, set by the PMIC vendor at manufacturing
- Default: 1 → PMIC5200

| Code (bin) | Meaning |
|---|---|
| 0 | PMIC5100 |
| 1 | PMIC5200 |

## R3C (0x3C) — VENDOR_ID_BYTE0

Region: Host Region | Source: JESD301-3 Table 164, p.184

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | VENDOR_ID_BYTE0 | ROA | - |

### [7:0] VENDOR_ID_BYTE0

- Description: Vendor Identification Register Byte 0.
- Attribute: ROA — Read Only (writes have no effect); Persistent, set by the PMIC vendor at manufacturing
- Default: -
- Values: no per-value encoding is listed in the spec for this field.

## R3D (0x3D) — VENDOR_ID_BYTE1

Region: Host Region | Source: JESD301-3 Table 165, p.184

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | VENDOR_ID_BYTE1 | ROA | - |

### [7:0] VENDOR_ID_BYTE1

- Description: Vendor Identification Register Byte 1.
- Attribute: ROA — Read Only (writes have no effect); Persistent, set by the PMIC vendor at manufacturing
- Default: -
- Values: no per-value encoding is listed in the spec for this field.

## R3E (0x3E) — SWB_DVFSQ_VOLTAGE_SETTING, OUTPUT_VOLTAGE_RESET

Region: Host Region | Source: JESD301-3 Table 166, p.185

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:1 | SWB_DVFSQ_VOLTAGE_SETTING | RW | 001 0100 |
| 0 | OUTPUT_VOLTAGE_RESET | 1O | 0 |

### [7:1] SWB_DVFSQ_VOLTAGE_SETTING

- Description: Switch Node B Output Regulator Voltage Setting for DVFSQ[1],[2],[3],[4],[5],[6]
- Attribute: RW — Read/Write
- Default: 001 0100 → 300 mV or 250 mV

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 0000000 | 0x00 | 200[7] mV or 200[8] mV |
| 0000001 | 0x01 | 205 mV or 202.5 mV |
| 0000010 | 0x02 | 210 mV or 205 mV |
| ... | ... | ... |
| 0010100 | 0x14 | 300 mV or 250 mV |
| ... | ... | ... |
| 1111101 | 0x7D | 825 mV or 512.5 mV |
| 1111110 | 0x7E | 830 mV or 515 mV |
| 1111111 | 0x7F | 835 mV or 517.5 mV |

### [0] OUTPUT_VOLTAGE_RESET

- Description: SWx Output Voltage, Resolution and Offset Reset to Default[9]
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0 → No action

| Code (bin) | Meaning |
|---|---|
| 0 | No action |
| 1 | Reset registers to default[10],[11] |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 197, Register 0x4F [7:1].
- NOTE 2: If required, the host must update the settings in register Table 141, Register 0x25, [0], Table 142, Register 0x26, [7:2], and Table 136, Register 0x20 [3:2] first prior to updating the settings in the register Table 166, Register 0x3E [7:1]. Note that SWB DVFSQ threshold settings (Power Good Low Threshold, Power Good High Threshold, Over Voltage Threshold, Under Voltage Threshold) are same regardless of whether PMIC is in P3 or DVFSQ operating state.
- NOTE 3: This register is only applicable if Table 150, Register 0x2E[4] = ‘1’.
- NOTE 4: PMIC guarantees efficiency spec and all electrical characteristics spec within a range of 450 mV to 550 mV or from 300 mV to 400 mV depending on the range selection.
- NOTE 5: After VR is enabled, the host may update this register to any new setting that it may desire. However, to prevent false error trigger, the PMIC internally will increment the SWB output voltage setting by 5 or 2.5 mV at a time. The time it takes for PMIC to adjust the output voltage is 5 μs for each 5 mV increment. The host must wait sufficient time for PMIC to adjust to final value. As an example, if host adjusts the output voltage by 50 mV from the original value, the host must wait minimum of 50 μs before PMIC can guarantee the new output voltage. During this time, PMIC masks the PWR_GOOD output signal assertion to prevent any artificial error due to the crossing of the output voltage threshold setting. However, PMIC does assert PWR_GOOD output signal if there are any abnormal issues that triggers VR Disable command as described in Table 27. Further, PMIC does monitor PWR_GOOD input signal and executes power off config sequence registers if it is registered low when Table 154, Register 0x32 [5] = ‘1’.
- NOTE 6: The setting in this register must be less than or equal to value programmed in Table 141, Register 0x25, [7:1].
- NOTE 7: Table 147, Register 0x2B, [3] = ‘0’; 5 mV step size.
- NOTE 8: Table 147, Register 0x2B, [3] = ‘1’; 2.5 mV step size.
- NOTE 9: This register bit is a self clearing bit.
- NOTE 10: The PMIC resets registers Table 147, Register 0x2B, [5:3,0], Table 137, Register 0x21, [7:1], Table 139, Register 0x23, [7:1], Table 141, Register 0x25, [7:1], Table 143, Register 0x27, [7:1], Table 166, Register 0x3E [7:1], and Table 167, Register 0x3F [2] to default value.0
- NOTE 11: Once this register is written to ‘1’, the PMIC requires time before all registers are reset. During this time, the PMIC masks PWR_GOOD output signal assertion to prevent any artificial error due to the crossing of the output voltage threshold setting. However, PMIC does assert PWR_GOOD output signal if there are any abnormal issues that triggers VR Disable command as described in Table 27. Further, PMIC does monitor PWR_GOOD input signal and executes power off config sequence registers if it is registered low when Table 154, Register 0x32 [5] = ‘1’.

## R3F (0x3F) — SWB_VOLTAGE_OFFSET

Region: Host Region | Source: JESD301-3 Table 167, p.186

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:3 | RESERVED | RV | 0 |
| 2 | SWB_VOLTAGE_OFFSET | RW | 0 |
| 1:0 | RESERVED | RV | 0 |

### [7:3] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [2] SWB_VOLTAGE_OFFSET

- Description: SWB Voltage Offset to the setting configured in Table 141, Register 0x25, [7:1][1] All other encodings are reserved
- Attribute: RW — Read/Write
- Default: 0 → No Offset

| Code (bin) | Meaning |
|---|---|
| 0 | No Offset |
| 1 | 600 mV[2],[3],[4],[5],[6] |

### [1:0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 206, Register 0x5F [0].
- NOTE 2: The DVFSQ_n pin function must be disabled and PMIC cannot be in DVFSQ security state.
- NOTE 3: The efficiency spec for SWB does not apply. The DC+AC voltage tolerance for SWB is relaxed to +8% & -5%.
- NOTE 4: The SWB output voltage transitions to 600 mV above the value set in Table 141, Register 0x25, [7:1] at a slew rate of 1mV/μs. The 600 mV offset is removed from the value set in Table 141, Register 0x25, [7:1] when this register is cleared to ‘0’ at a slew rate of 1mV/μs.
- NOTE 5: It is permitted to change the SWB output voltage.
- NOTE 6: The setting in Table 147, Register 0x2B, [3] can be either ‘0’ or ‘1’.

## R40 (0x40) — POWER_ON_SEQUENCE_CONFIG0, POWER_ON_SEQUENCE_CONFIG0_SWA_ENABLE, POWER_ON_SEQUENCE_CONFIG0_SWD_ENABLE, POWER_ON_SEQUENCE_CONFIG0_SWB_ENABLE, POWER_ON_SEQUENCE_CONFIG0_SWC_ENABLE, POWER_ON_SEQUENCE_CONFIG0_IDLE

Region: CAMM2 Vendor Region (NVM, password protected) | Source: JESD301-3 Table 182, p.193

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | POWER_ON_SEQUENCE_CONFIG0 | RWPE | 0 |
| 6 | POWER_ON_SEQUENCE_CONFIG0_SWA_ENABLE | RWPE | 0 |
| 5 | POWER_ON_SEQUENCE_CONFIG0_SWD_ENABLE | RWPE | 0 |
| 4 | POWER_ON_SEQUENCE_CONFIG0_SWB_ENABLE | RWPE | 0 |
| 3 | POWER_ON_SEQUENCE_CONFIG0_SWC_ENABLE | RWPE | 0 |
| 2:0 | POWER_ON_SEQUENCE_CONFIG0_IDLE | RWPE | 001 |

### [7] POWER_ON_SEQUENCE_CONFIG0

- Description: PMIC Power On Sequence Config 0[2]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Do Not Execute Config 0

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Execute Config 0 |
| 1 | Execute Config 0 |

### [6] POWER_ON_SEQUENCE_CONFIG0_SWA_ENABLE

- Description: Enable Switch Node A Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No action

| Code (bin) | Meaning |
|---|---|
| 0 | No action |
| 1 | Enable Switch Node A Output Regulator |

### [5] POWER_ON_SEQUENCE_CONFIG0_SWD_ENABLE

- Description: Enable Switch Node D Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No action

| Code (bin) | Meaning |
|---|---|
| 0 | No action |
| 1 | Enable Switch Node D Output Regulator |

### [4] POWER_ON_SEQUENCE_CONFIG0_SWB_ENABLE

- Description: Enable Switch Node B Output Regulator[3]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No action

| Code (bin) | Meaning |
|---|---|
| 0 | No action |
| 1 | Enable Switch Node B Output Regulator |

### [3] POWER_ON_SEQUENCE_CONFIG0_SWC_ENABLE

- Description: Enable Switch Node C Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No action

| Code (bin) | Meaning |
|---|---|
| 0 | No action |
| 1 | Enable Switch Node C Output Regulator |

### [2:0] POWER_ON_SEQUENCE_CONFIG0_IDLE

- Description: Idle time after Power On Sequence Config 0[4]
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

- NOTE 1: The PMIC always starts with power on sequence config0 and executes remaining power on sequence config registers (1 to 3) in sequential order.
- NOTE 2: If bit [7] = ‘0’, bits [6:0] are ignored and PMIC moves to next power on sequence configuration register. If bits [7] = ‘1’, the PMIC executes bits [6:0] as configured; if no new rail is turned on, the PMIC simply waits the idle time as configured and then moves to next power sequence configuration register.
- NOTE 3: The SWB output regulator is conditionally enabled as defined in clause 4.13. The SWB output rail remains disabled even if this is bit set to ‘1’, if SWB_Disable input pin is enabled, and its input level is either high at the time of VR Enable command (either from VR_EN pin or I2C/I3C bus command or auto power on) from P2_B state.
- NOTE 4: Idle time is the additional time after soft-start time expires. The PMIC waits sum of Soft Start time and Idle time before it executes the next power on sequence configuration register. If more than one regulators are enabled, the PMIC uses the largest value of the soft start time among the regulators that are enabled in this configuration register.

## R41 (0x41) — POWER_ON_SEQUENCE_CONFIG1, POWER_ON_SEQUENCE_CONFIG1_SWA_ENABLE, POWER_ON_SEQUENCE_CONFIG1_SWD_ENABLE, POWER_ON_SEQUENCE_CONFIG1_SWB_ENABLE, POWER_ON_SEQUENCE_CONFIG1_SWC_ENABLE, POWER_ON_SEQUENCE_CONFIG1_IDLE

Region: CAMM2 Vendor Region (NVM, password protected) | Source: JESD301-3 Table 183, p.194

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | POWER_ON_SEQUENCE_CONFIG1 | RWPE | 0 |
| 6 | POWER_ON_SEQUENCE_CONFIG1_SWA_ENABLE | RWPE | 0 |
| 5 | POWER_ON_SEQUENCE_CONFIG1_SWD_ENABLE | RWPE | 0 |
| 4 | POWER_ON_SEQUENCE_CONFIG1_SWB_ENABLE | RWPE | 0 |
| 3 | POWER_ON_SEQUENCE_CONFIG1_SWC_ENABLE | RWPE | 0 |
| 2:0 | POWER_ON_SEQUENCE_CONFIG1_IDLE | RWPE | 001 |

### [7] POWER_ON_SEQUENCE_CONFIG1

- Description: PMIC Power On Sequence Config 1
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Do Not Execute Config 1[2]

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Execute Config 1[2] |
| 1 | Execute Config 1 |

### [6] POWER_ON_SEQUENCE_CONFIG1_SWA_ENABLE

- Description: Enable Switch Node A Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No action

| Code (bin) | Meaning |
|---|---|
| 0 | No action |
| 1 | Enable Switch Node A Output Regulator |

### [5] POWER_ON_SEQUENCE_CONFIG1_SWD_ENABLE

- Description: Enable Switch Node D Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No action

| Code (bin) | Meaning |
|---|---|
| 0 | No action |
| 1 | Enable Switch Node D Output Regulator |

### [4] POWER_ON_SEQUENCE_CONFIG1_SWB_ENABLE

- Description: Enable Switch Node B Output Regulator[3]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No action

| Code (bin) | Meaning |
|---|---|
| 0 | No action |
| 1 | Enable Switch Node B Output Regulator |

### [3] POWER_ON_SEQUENCE_CONFIG1_SWC_ENABLE

- Description: Enable Switch Node C Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No action

| Code (bin) | Meaning |
|---|---|
| 0 | No action |
| 1 | Enable Switch Node C Output Regulator |

### [2:0] POWER_ON_SEQUENCE_CONFIG1_IDLE

- Description: Idle time after Power On Sequence Config 1[4]
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

- NOTE 1: The PMIC always starts with power on sequence config0 and executes remaining power on sequence config registers (1 to 3) in sequential order.
- NOTE 2: If bit [7] = ‘0’, bits [6:0] are ignored and PMIC moves to next power on sequence configuration register. If bits [7] = ‘1’, the PMIC executes bits [6:0] as configured; if no new rail is turned on, the PMIC simply waits the idle time as configured and then moves to next power sequence configuration register.
- NOTE 3: The SWB output regulator is conditionally enabled as defined in clause 4.13. The SWB output rail remains disabled even if this is bit set to ‘1’, if SWB_Disable input pin is enabled, and its input level is either high at the time of VR Enable command (either from VR_EN pin or I2C/I3C bus command or auto power on) from P2_B state.
- NOTE 4: Idle time is the additional time after soft-start time expires. The PMIC waits sum of Soft Start time and Idle time before it executes the next power on sequence configuration register. If more than one regulators are enabled, the PMIC uses the largest value of the soft start time among the regulators that are enabled in this configuration register.

## R42 (0x42) — POWER_ON_SEQUENCE_CONFIG2, POWER_ON_SEQUENCE_CONFIG2_SWA_ENABLE, POWER_ON_SEQUENCE_CONFIG2_SWD_ENABLE, POWER_ON_SEQUENCE_CONFIG2_SWB_ENABLE, POWER_ON_SEQUENCE_CONFIG2_SWC_ENABLE, POWER_ON_SEQUENCE_CONFIG2_IDLE

Region: CAMM2 Vendor Region (NVM, password protected) | Source: JESD301-3 Table 184, p.195

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | POWER_ON_SEQUENCE_CONFIG2 | RWPE | 0 |
| 6 | POWER_ON_SEQUENCE_CONFIG2_SWA_ENABLE | RWPE | 0 |
| 5 | POWER_ON_SEQUENCE_CONFIG2_SWD_ENABLE | RWPE | 0 |
| 4 | POWER_ON_SEQUENCE_CONFIG2_SWB_ENABLE | RWPE | 0 |
| 3 | POWER_ON_SEQUENCE_CONFIG2_SWC_ENABLE | RWPE | 0 |
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

### [5] POWER_ON_SEQUENCE_CONFIG2_SWD_ENABLE

- Description: Enable Switch Node D Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No action

| Code (bin) | Meaning |
|---|---|
| 0 | No action |
| 1 | Enable Switch Node D Output Regulator |

### [4] POWER_ON_SEQUENCE_CONFIG2_SWB_ENABLE

- Description: Enable Switch Node B Output Regulator[4]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No action

| Code (bin) | Meaning |
|---|---|
| 0 | No action |
| 1 | Enable Switch Node B Output Regulator |

### [3] POWER_ON_SEQUENCE_CONFIG2_SWC_ENABLE

- Description: Enable Switch Node C Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No action

| Code (bin) | Meaning |
|---|---|
| 0 | No action |
| 1 | Enable Switch Node C Output Regulator |

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

- NOTE 1: The PMIC always starts with power on sequence config0 and executes remaining power on sequence config registers (1 to 3) in sequential order
- NOTE 2: If more than one configuration register is used for power on sequence, first register must start at Table 182, Register 0x40 and it must go in sequential order to Table 185, Register 0x43 to turn on all desired regulators. In other words, there must not be any gap of the register that is used for power on sequence.
- NOTE 3: If bit [7] = ‘0’, bits [6:0] are ignored and PMIC moves to next power on sequence configuration register. If bits [7] = ‘1’, the PMIC executes bits [6:0] as configured; if no new rail is turned on, the PMIC simply waits the idle time as configured and then moves to next power sequence configuration register.
- NOTE 4: The SWB output regulator is conditionally enabled as defined in clause 4.13. The SWB output rail remains disabled even if this is bit set to ‘1’, if SWB_Disable input pin is enabled, and its input level is either high at the time of VR Enable command (either from VR_EN pin or I2C/I3C bus command or auto power on) from P2_B state.
- NOTE 5: Idle time is the additional time after soft-start time expires. The PMIC waits sum of Soft Start time and Idle time before it executes the next power on sequence configuration register. If more than one regulators are enabled, the PMIC uses the largest value of the soft start time among the regulators that are enabled in this configuration register.

## R43 (0x43) — POWER_ON_SEQUENCE_CONFIG3, POWER_ON_SEQUENCE_CONFIG3_SWA_ENABLE, POWER_ON_SEQUENCE_CONFIG3_SWD_ENABLE, POWER_ON_SEQUENCE_CONFIG3_SWB_ENABLE, POWER_ON_SEQUENCE_CONFIG3_SWC_ENABLE

Region: CAMM2 Vendor Region (NVM, password protected) | Source: JESD301-3 Table 185, p.196

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | POWER_ON_SEQUENCE_CONFIG3 | RWPE | 0 |
| 6 | POWER_ON_SEQUENCE_CONFIG3_SWA_ENABLE | RWPE | 0 |
| 5 | POWER_ON_SEQUENCE_CONFIG3_SWD_ENABLE | RWPE | 0 |
| 4 | POWER_ON_SEQUENCE_CONFIG3_SWB_ENABLE | RWPE | 0 |
| 3 | POWER_ON_SEQUENCE_CONFIG3_SWC_ENABLE | RWPE | 0 |
| 2:0 | RESERVED | RV | 0 |

### [7] POWER_ON_SEQUENCE_CONFIG3

- Description: PMIC Power On Sequence Config 3[2]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Do Not Execute Config 3

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Execute Config 3 |
| 1 | Execute Config 3 |

### [6] POWER_ON_SEQUENCE_CONFIG3_SWA_ENABLE

- Description: Enable Switch Node A Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No action

| Code (bin) | Meaning |
|---|---|
| 0 | No action |
| 1 | Enable Switch Node A Output Regulator |

### [5] POWER_ON_SEQUENCE_CONFIG3_SWD_ENABLE

- Description: Enable Switch Node D Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No action

| Code (bin) | Meaning |
|---|---|
| 0 | No action |
| 1 | Enable Switch Node D Output Regulator |

### [4] POWER_ON_SEQUENCE_CONFIG3_SWB_ENABLE

- Description: Enable Switch Node B Output Regulator.[3]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No action

| Code (bin) | Meaning |
|---|---|
| 0 | No action |
| 1 | Enable Switch Node B Output Regulator |

### [3] POWER_ON_SEQUENCE_CONFIG3_SWC_ENABLE

- Description: Enable Switch Node C Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No action

| Code (bin) | Meaning |
|---|---|
| 0 | No action |
| 1 | Enable Switch Node C Output Regulator |

### [2:0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

**Notes**

- NOTE 1: The PMIC always starts with power on sequence config0 and executes remaining power on sequence config registers (1 to 3) in sequential order.
- NOTE 2: If bit [7] = ‘0’, bits [6:0] are ignored and PMIC moves to next power on sequence configuration register. If bits [7] = ‘1’, the PMIC executes bits [6:0] as configured; if no new rail is turned on, the PMIC simply waits the idle time as configured and then moves to next power sequence configuration register.
- NOTE 3: The SWB output regulator is conditionally enabled as defined in clause 4.13. The SWB output rail remains disabled even if this is bit set to ‘1’, if SWB_Disable input pin is enabled, and its input level is either high at the time of VR Enable command (either from VR_EN pin or I2C/I3C bus command or auto power on) from P2_B state.

## R44 (0x44) — SWA_OUTPUT_SOFT_STOP_TIME_EXTENSION, SWD_OUTPUT_SOFT_STOP_TIME_EXTENSION, SWB_OUTPUT_SOFT_STOP_TIME_EXTENSION, SWC_OUTPUT_SOFT_STOP_TIME_EXTENSION, SWB_DISABLE_INPUT_PIN_ENABLE

Region: CAMM2 Vendor Region (NVM, password protected) | Source: JESD301-3 Table 186, p.197

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | SWA_OUTPUT_SOFT_STOP_TIME_EXTENSION | RWPE | 0 |
| 6 | SWD_OUTPUT_SOFT_STOP_TIME_EXTENSION | RWPE | 0 |
| 5 | SWB_OUTPUT_SOFT_STOP_TIME_EXTENSION | RWPE | 0 |
| 4 | SWC_OUTPUT_SOFT_STOP_TIME_EXTENSION | RWPE | 0 |
| 3:1 | RESERVED | RV | 0 |
| 0 | SWB_DISABLE_INPUT_PIN_ENABLE | RWPE | 1 |

### [7] SWA_OUTPUT_SOFT_STOP_TIME_EXTENSION

- Description: SWA Output Regulator Soft Stop Time After VR Disable. This register bit (MSB) plus 2 bit register Table 188, Register 0x46 [1:0] makes 3 bit register encoding. See encoding in Table 188, Register 0x46.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0
- Values: no per-value encoding is listed in the spec for this field.

### [6] SWD_OUTPUT_SOFT_STOP_TIME_EXTENSION

- Description: SWD Output Regulator Soft Stop Time After VR Disable. This register bit (MSB) plus 2 bit register Table 190, Register 0x48 [1:0] makes 3 bit register encoding. See encoding in Table 190, Register 0x48.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0
- Values: no per-value encoding is listed in the spec for this field.

### [5] SWB_OUTPUT_SOFT_STOP_TIME_EXTENSION

- Description: SWB Output Regulator Soft Stop Time After VR Disable. This register bit (MSB) plus 2 bit register Table 192, Register 0x4A [1:0] makes 3 bit register encoding. See encoding in Table 192, Register 0x4A.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0
- Values: no per-value encoding is listed in the spec for this field.

### [4] SWC_OUTPUT_SOFT_STOP_TIME_EXTENSION

- Description: SWC Output Regulator Soft Stop Time After VR Disable. This register bit (MSB) plus 2 bit register Table 194, Register 0x4C [1:0] makes 3 bit register encoding. See encoding in Table 194, Register 0x4C.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0
- Values: no per-value encoding is listed in the spec for this field.

### [3:1] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [0] SWB_DISABLE_INPUT_PIN_ENABLE

- Description: SWB_Disable Input Pin Enable
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 1 → Enable; Input pin receiver is enabled

| Code (bin) | Meaning |
|---|---|
| 0 | Disable; Input pin receiver is disabled |
| 1 | Enable; Input pin receiver is enabled |

## R45 (0x45) — SWA_VOLTAGE_SETTING, SWA_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

Region: CAMM2 Vendor Region (NVM, password protected) | Source: JESD301-3 Table 187, p.197

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:1 | SWA_VOLTAGE_SETTING | RWPE | 011 0010 |
| 0 | SWA_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING | RWPE | 0 |

### [7:1] SWA_VOLTAGE_SETTING

- Description: Switch Node A Output Regulator Voltage Setting[1]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 011 0010 → 1050 mV or 1300 mV

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 0000000 | 0x00 | 800[2] mV or 800[3] mV |
| 0000001 | 0x01 | 805 mV or 810 mV |
| 0000010 | 0x02 | 810 mV or 820 mV |
| ... | ... | ... |
| 0111100 | 0x3C | 1100 mV or 1400 mV |
| ... | ... | ... |
| 1111101 | 0x7D | 1425 mV or 2050 mV |
| 1111110 | 0x7E | 1430 mV or 2060 mV |
| 1111111 | 0x7F | 1435 mV or 2070 mV |

### [0] SWA_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

- Description: Switch Node A Output Threshold Low Side Voltage For Power Good Status
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → - 5% from the setting in Table 187, Register 0x45 [7:1]
- Source correction: Field header says [1:0] but the Bits column shows [0]; the Bits column is used.

| Code (bin) | Meaning |
|---|---|
| 0 | - 5% from the setting in Table 187, Register 0x45 [7:1] |
| 1 | - 7.5% from the setting in Table 187, Register 0x45 [7:1] |

**Notes**

- NOTE 1: PMIC guarantees efficiency spec and all electrical characteristics spec within a range of 1000 mV to 1100 mV.
- NOTE 2: Table 199, Register 0x51 [5] = ‘0’; 5 mV step size.
- NOTE 3: Table 199, Register 0x51 [5] = ‘1’; 10 mV step size.

## R46 (0x46) — SWA_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING, SWA_OVER_VOLTAGE_THRESHOLD_SETTING, SWA_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING, SWA_OUTPUT_SOFT_STOP_TIME

Region: CAMM2 Vendor Region (NVM, password protected) | Source: JESD301-3 Table 188, p.198

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWA_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING | RWPE | 01 |
| 5:4 | SWA_OVER_VOLTAGE_THRESHOLD_SETTING | RWPE | 10 |
| 3:2 | SWA_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING | RWPE | 00 |
| 1:0 | SWA_OUTPUT_SOFT_STOP_TIME | RWPE | 00 |

### [7:6] SWA_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING

- Description: Switch Node A Output Threshold High Side Voltage For Power Good Status
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 01 → +7.5% from the setting in Table 187, Register 0x45 [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +5% from the setting in Table 187, Register 0x45 [7:1] |
| 01 | +7.5% from the setting in Table 187, Register 0x45 [7:1] |
| 10 | +10% from the setting in Table 187, Register 0x45 [7:1] |
| 11 | Reserved |

### [5:4] SWA_OVER_VOLTAGE_THRESHOLD_SETTING

- Description: Switch Node A Output Regulator Threshold For Over Voltage Status[1]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 10 → +12.5% from the setting in Table 187, Register 0x45 [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +7.5% from the setting in Table 187, Register 0x45 [7:1] |
| 01 | +10% from the setting in Table 187, Register 0x45 [7:1] |
| 10 | +12.5% from the setting in Table 187, Register 0x45 [7:1] |
| 11 | Reserved |

### [3:2] SWA_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING

- Description: Switch Node A Output Regulator Threshold For Under Voltage Lockout Status
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 00 → -10% from the setting in Table 187, Register 0x45 [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | -10% from the setting in Table 187, Register 0x45 [7:1] |
| 01 | -12.5% from the setting in Table 187, Register 0x45 [7:1] |
| 10 | Reserved |
| 11 | Reserved |

### [1:0] SWA_OUTPUT_SOFT_STOP_TIME

- Description: SWA Output Regulator Soft Stop Time After VR Disable[2]. The register Table 186, Register 0x44 [7] (MSB) plus this two bit register makes the 3 bit encoding.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 00
- Note: the codes below are wider than this 2-bit field; the encoding combines bits from more than one field/register (see Description).

| Code (bin) | Meaning |
|---|---|
| 000 | 0.5 ms |
| 001 | 1 ms |
| 010 | 2 ms |
| 011 | 4 ms |
| 100 | 8 ms |
| 101 | 16 ms |
| 110 | 32 ms |
| 111 | 64 ms |

**Notes**

- NOTE 1: The setting for the Over Voltage must be higher than Power Good High Side Voltage threshold in Table 188, Register 0x46[7:6].
- NOTE 2: This is the time it takes for buck regulator to go from steady state voltage to 0 V.

## R47 (0x47) — SWD_VOLTAGE_SETTING, SWD_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

Region: CAMM2 Vendor Region (NVM, password protected) | Source: JESD301-3 Table 189, p.199

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:1 | SWD_VOLTAGE_SETTING | RWPE | 001 0100 |
| 0 | SWD_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING | RWPE | 0 |

### [7:1] SWD_VOLTAGE_SETTING

- Description: Switch Node D Output Regulator Voltage Setting[1]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 001 0100 → 900 mV or 1000 mV

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 0000000 | 0x00 | 800[2] mV or 800[3] mV |
| 0000001 | 0x01 | 805 mV or 810 mV |
| 0000010 | 0x02 | 810 mV or 820 mV |
| ... | ... | ... |
| 0111100 | 0x3C | 1100 mV or 1400 mV |
| ... | ... | ... |
| 1111101 | 0x7D | 1425 mV or 2050 mV |
| 1111110 | 0x7E | 1430 mV or 2060 mV |
| 1111111 | 0x7F | 1435 mV or 2070 mV |

### [0] SWD_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

- Description: Switch Node D Output Threshold Low Side Voltage For Power Good Status
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → - 5% from the setting in Table 189, Register 0x47 [7:1]
- Source correction: Field header says [1:0] but the Bits column shows [0]; the Bits column is used.

| Code (bin) | Meaning |
|---|---|
| 0 | - 5% from the setting in Table 189, Register 0x47 [7:1] |
| 1 | - 7.5% from the setting in Table 189, Register 0x47 [7:1] |

**Notes**

- NOTE 1: PMIC guarantees efficiency spec and all electrical characteristics spec within a range of 850 mV to 950 mV.
- NOTE 2: Table 199, Register 0x51 [4] = ‘0’; 5 mV step size.
- NOTE 3: Table 199, Register 0x51 [4] = ‘1’; 10 mV step size.

## R48 (0x48) — SWD_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING, SWD_OVER_VOLTAGE_THRESHOLD_SETTING, SWD_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING, SWD_OUTPUT_SOFT_STOP_TIME

Region: CAMM2 Vendor Region (NVM, password protected) | Source: JESD301-3 Table 190, p.200

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWD_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING | RWPE | 01 |
| 5:4 | SWD_OVER_VOLTAGE_THRESHOLD_SETTING | RWPE | 10 |
| 3:2 | SWD_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING | RWPE | 00 |
| 1:0 | SWD_OUTPUT_SOFT_STOP_TIME | RWPE | 00 |

### [7:6] SWD_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING

- Description: Switch Node D Output Threshold High Side Voltage For Power Good Status
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 01 → +7.5% from the setting in Table 189, Register 0x47 [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +5% from the setting in Table 189, Register 0x47 [7:1] |
| 01 | +7.5% from the setting in Table 189, Register 0x47 [7:1] |
| 10 | +10% from the setting in Table 189, Register 0x47 [7:1] |
| 11 | Reserved |

### [5:4] SWD_OVER_VOLTAGE_THRESHOLD_SETTING

- Description: Switch Node D Output Regulator Threshold For Over Voltage Status[1]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 10 → +12.5% from the setting in Table 189, Register 0x47 [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +7.5% from the setting in Table 189, Register 0x47 [7:1] |
| 01 | +10% from the setting in Table 189, Register 0x47 [7:1] |
| 10 | +12.5% from the setting in Table 189, Register 0x47 [7:1] |
| 11 | Reserved |

### [3:2] SWD_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING

- Description: Switch Node D Output Regulator Threshold For Under Voltage Lockout Status
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 00 → -10% from the setting in Table 189, Register 0x47 [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | -10% from the setting in Table 189, Register 0x47 [7:1] |
| 01 | -12.5% from the setting in Table 189, Register 0x47 [7:1] |
| 10 | Reserved |
| 11 | Reserved |

### [1:0] SWD_OUTPUT_SOFT_STOP_TIME

- Description: SWD Output Regulator Soft Stop Time After VR Disable[2]. The register Table 186, Register 0x44 [6] (MSB) plus this two bit register makes the 3 bit encoding.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 00
- Note: the codes below are wider than this 2-bit field; the encoding combines bits from more than one field/register (see Description).

| Code (bin) | Meaning |
|---|---|
| 000 | 0.5 ms |
| 001 | 1 ms |
| 010 | 2 ms |
| 011 | 4 ms |
| 100 | 8 ms |
| 101 | 16 ms |
| 110 | 32 ms |
| 111 | 64 ms |

**Notes**

- NOTE 1: The setting for the Over Voltage must be higher than Power Good High Side Voltage threshold in Table 190, Register 0x48 [7:6].
- NOTE 2: This is the time it takes for buck regulator to go from steady state voltage to 0 V.

## R49 (0x49) — SWB_VOLTAGE_SETTING, SWB_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

Region: CAMM2 Vendor Region (NVM, password protected) | Source: JESD301-3 Table 191, p.201

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:1 | SWB_VOLTAGE_SETTING | RWPE | 011 1100 |
| 0 | SWB_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING | RWPE | 0 |

### [7:1] SWB_VOLTAGE_SETTING

- Description: Switch Node B Output Regulator Voltage Setting[1]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 011 1100 → 500 mV or 350 mV

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 0000000 | 0x00 | 200[2] mV or 200[3] mV |
| 0000001 | 0x01 | 205 mV or 202.5 mV |
| 0000010 | 0x02 | 210 mV or 205 mV |
| ... | ... | ... |
| 0111100 | 0x3C | 500 mV or 350 mV |
| ... | ... | ... |
| 1111101 | 0x7D | 825 mV or 512.5 mV |
| 1111110 | 0x7E | 830 mV or 515 mV |
| 1111111 | 0x7F | 835 mV or 517.5 mV |

### [0] SWB_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

- Description: Switch Node B Output Threshold Low Side Voltage For Power Good Status
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → -5% from the setting in Table 191, Register 0x49 [7:1]

| Code (bin) | Meaning |
|---|---|
| 0 | -5% from the setting in Table 191, Register 0x49 [7:1] |
| 1 | -7.5 from the setting in Table 191, Register 0x49 [7:1] |

**Notes**

- NOTE 1: PMIC guarantees efficiency spec and all electrical characteristics spec within a range of 450 mV to 550 mV or from 300 mV to 400 mV depending on the range selection.
- NOTE 2: Table 199, Register 0x51 [3] = ‘0’; 5 mV step size.
- NOTE 3: Table 199, Register 0x51 [3] = ‘1’; 2.5 mV step size.

## R4A (0x4A) — SWB_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING, SWB_OVER_VOLTAGE_THRESHOLD_SETTING, SWB_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING, SWB_OUTPUT_SOFT_STOP_TIME

Region: CAMM2 Vendor Region (NVM, password protected) | Source: JESD301-3 Table 192, p.202

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWB_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING | RWPE | 01 |
| 5:4 | SWB_OVER_VOLTAGE_THRESHOLD_SETTING | RWPE | 10 |
| 3:2 | SWB_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING | RWPE | 00 |
| 1:0 | SWB_OUTPUT_SOFT_STOP_TIME | RWPE | 00 |

### [7:6] SWB_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING

- Description: Switch Node B Output Threshold High Side Voltage For Power Good Status
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 01 → +7.5% from the setting in Table 191, Register 0x49 [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +5% from the setting in Table 191, Register 0x49 [7:1] |
| 01 | +7.5% from the setting in Table 191, Register 0x49 [7:1] |
| 10 | +10% from the setting in Table 191, Register 0x49 [7:1] |
| 11 | Reserved |

### [5:4] SWB_OVER_VOLTAGE_THRESHOLD_SETTING

- Description: Switch Node B Output Regulator Threshold For Over Voltage Status[1]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 10 → +12.5% from the setting in Table 191, Register 0x49 [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +7.5% from the setting in Table 191, Register 0x49 [7:1] |
| 01 | +10% from the setting in Table 191, Register 0x49 [7:1] |
| 10 | +12.5% from the setting in Table 191, Register 0x49 [7:1] |
| 11 | Reserved |

### [3:2] SWB_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING

- Description: Switch Node B Output Regulator Threshold For Under Voltage Lockout Status
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 00 → -10% from the setting in Table 191, Register 0x49 [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | -10% from the setting in Table 191, Register 0x49 [7:1] |
| 01 | -12.5% from the setting in Table 191, Register 0x49 [7:1] |
| 10 | Reserved |
| 11 | Reserved |

### [1:0] SWB_OUTPUT_SOFT_STOP_TIME

- Description: SWB Output Regulator Soft Stop Time After VR Disable[2]. The register Table 186, Register 0x44 [5] (MSB) plus this two bit register makes the 3 bit encoding.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 00
- Note: the codes below are wider than this 2-bit field; the encoding combines bits from more than one field/register (see Description).

| Code (bin) | Meaning |
|---|---|
| 000 | 0.5 ms |
| 001 | 1 ms |
| 010 | 2 ms |
| 011 | 4 ms |
| 100 | 8 ms |
| 101 | 16 ms |
| 110 | 32 ms |
| 111 | 64 ms |

**Notes**

- NOTE 1: The setting for the Over Voltage must be higher than Power Good High Side Voltage threshold in Table 192, Register 0x4A[7:6].
- NOTE 2: This is the time it takes for buck regulator to go from steady state voltage to 0 V.

## R4B (0x4B) — SWC_VOLTAGE_SETTING, SWC_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

Region: CAMM2 Vendor Region (NVM, password protected) | Source: JESD301-3 Table 193, p.203

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:1 | SWC_VOLTAGE_SETTING | RWPE | 011 1100 |
| 0 | SWC_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING | RWPE | 0 |

### [7:1] SWC_VOLTAGE_SETTING

- Description: Switch Node C Output Regulator Voltage Setting[1]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 011 1100 → 1800 mV or 2100 mV

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 0000000 | 0x00 | 1500[2] mV or 1500[3] mV |
| 0000001 | 0x01 | 1505 mV or 1510 mV |
| 0000010 | 0x02 | 1510 mV or 1520 mV |
| ... | ... | ... |
| 0111100 | 0x3C | 1800 mV or 2100 mV |
| ... | ... | ... |
| 1111101 | 0x7D | 2125 mV or 2750 mV |
| 1111110 | 0x7E | 2130 mV or 2760 mV |
| 1111111 | 0x7F | 2135 mV or 2770 mV |

### [0] SWC_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

- Description: Switch Node C Output Threshold Low Side Voltage For Power Good Status
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → -5% from the setting in Table 193, Register 0x4B [7:1]

| Code (bin) | Meaning |
|---|---|
| 0 | -5% from the setting in Table 193, Register 0x4B [7:1] |
| 1 | -7.5% from the setting in Table 193, Register 0x4B [7:1] |

**Notes**

- NOTE 1: PMIC guarantees efficiency spec and all electrical characteristics spec within a range of 1750 mV to 1850 mV.
- NOTE 2: Table 199, Register 0x51 [0] = ‘0’; 5 mV step size.
- NOTE 3: Table 199, Register 0x51 [0] = ‘0’; 10 mV step size.

## R4C (0x4C) — SWC_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING, SWC_OVER_VOLTAGE_THRESHOLD_SETTING, SWC_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING, SWC_OUTPUT_SOFT_STOP_TIME

Region: CAMM2 Vendor Region (NVM, password protected) | Source: JESD301-3 Table 194, p.204

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWC_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING | RWPE | 01 |
| 5:4 | SWC_OVER_VOLTAGE_THRESHOLD_SETTING | RWPE | 10 |
| 3:2 | SWC_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING | RWPE | 00 |
| 1:0 | SWC_OUTPUT_SOFT_STOP_TIME | RWPE | 00 |

### [7:6] SWC_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING

- Description: Switch Node C Output Threshold High Side Voltage For Power Good Status
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 01 → +7.5% from the setting in Table 193, Register 0x4B [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +5% from the setting in Table 193, Register 0x4B [7:1] |
| 01 | +7.5% from the setting in Table 193, Register 0x4B [7:1] |
| 10 | +10% from the setting in Table 193, Register 0x4B [7:1] |
| 11 | Reserved |

### [5:4] SWC_OVER_VOLTAGE_THRESHOLD_SETTING

- Description: Switch Node C Output Regulator Threshold For Over Voltage Status[1]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 10 → +12.5% from the setting in Table 193, Register 0x4B [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +7.5% from the setting in Table 193, Register 0x4B [7:1] |
| 01 | +10% from the setting in Table 193, Register 0x4B [7:1] |
| 10 | +12.5% from the setting in Table 193, Register 0x4B [7:1] |
| 11 | Reserved |

### [3:2] SWC_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING

- Description: Switch Node C Output Regulator Threshold For Under Voltage Lockout Status
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 00 → -10% from the setting in Table 193, Register 0x4B [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | -10% from the setting in Table 193, Register 0x4B [7:1] |
| 01 | -12.5% from the setting in Table 193, Register 0x4B [7:1] |
| 10 | Reserved |
| 11 | Reserved |

### [1:0] SWC_OUTPUT_SOFT_STOP_TIME

- Description: SWC Output Regulator Soft Stop Time After VR Disable[2]. The register Table 186, Register 0x44 [4] (MSB) plus this two bit register makes the 3 bit encoding.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 00
- Note: the codes below are wider than this 2-bit field; the encoding combines bits from more than one field/register (see Description).

| Code (bin) | Meaning |
|---|---|
| 000 | 1 ms |
| 001 | 2 ms |
| 010 | 4 ms |
| 011 | 8 ms |
| 100 | 16 ms |
| 101 | 32 ms |
| 110 | 64 ms |
| 111 | Vendor defined |

**Notes**

- NOTE 1: The setting for the Over Voltage must be higher than Power Good High Side Voltage threshold in Table 194, Register 0x4C[7:6].
- NOTE 2: This is the time it takes for buck regulator to go from steady state voltage to 0 V.

## R4D (0x4D) — SWA_MODE_SELECT, SWA_SWITCHING_FREQ, SWD_MODE_SELECT, SWD_SWITCHING_FREQ

Region: CAMM2 Vendor Region (NVM, password protected) | Source: JESD301-3 Table 195, p.205

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWA_MODE_SELECT | RWPE | 10 |
| 5:4 | SWA_SWITCHING_FREQ | RWPE | 00 |
| 3:2 | SWD_MODE_SELECT | RWPE | 10 |
| 1:0 | SWD_SWITCHING_FREQ | RWPE | 00 |

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
- Default: 00 → 750 KHz

| Code (bin) | Meaning |
|---|---|
| 00 | 750 KHz |
| 01 | Vendor specific |
| 10 | Vendor specific |
| 11 | 500 KHz |

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
- Default: 00 → 750 KHz

| Code (bin) | Meaning |
|---|---|
| 00 | 750 KHz |
| 01 | Vendor specific |
| 10 | Vendor specific |
| 11 | Vendor specific |

## R4E (0x4E) — SWB_MODE_SELECT, SWB_SWITCHING_FREQ, SWC_MODE_SELECT, SWC_SWITCHING_FREQ

Region: CAMM2 Vendor Region (NVM, password protected) | Source: JESD301-3 Table 196, p.206

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWB_MODE_SELECT | RWPE | 10 |
| 5:4 | SWB_SWITCHING_FREQ | RWPE | 00 |
| 3:2 | SWC_MODE_SELECT | RWPE | 10 |
| 1:0 | SWC_SWITCHING_FREQ | RWPE | 00 |

### [7:6] SWB_MODE_SELECT

- Description: Switch Node B Output Regulator Mode Selection
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 10 → COT; DCM (Constant on Time; Discontinuous Current Mode)

| Code (bin) | Meaning |
|---|---|
| 00 | Reserved |
| 01 | Reserved |
| 10 | COT; DCM (Constant on Time; Discontinuous Current Mode) |
| 11 | COT; CCM (Constant on Time; Continuous Current Mode) |

### [5:4] SWB_SWITCHING_FREQ

- Description: Switch Node B Output Regulator Switching Frequency
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 00 → 750 KHz

| Code (bin) | Meaning |
|---|---|
| 00 | 750 KHz |
| 01 | Vendor specific |
| 10 | Vendor specific |
| 11 | Vendor specific |

### [3:2] SWC_MODE_SELECT

- Description: Switch Node C Output Regulator Mode Selection
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 10 → COT; DCM (Constant on Time; Discontinuous Current Mode)

| Code (bin) | Meaning |
|---|---|
| 00 | Reserved |
| 01 | Reserved |
| 10 | COT; DCM (Constant on Time; Discontinuous Current Mode) |
| 11 | COT; CCM (Constant on Time; Continuous Current Mode) |

### [1:0] SWC_SWITCHING_FREQ

- Description: Switch Node C Output Regulator Switching Frequency
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 00 → 750 KHz

| Code (bin) | Meaning |
|---|---|
| 00 | 750 KHz |
| 01 | Vendor specific |
| 10 | Vendor specific |
| 11 | Vendor specific |

## R4F (0x4F) — SWB_DVFSQ_VOLTAGE_SETTING

Region: CAMM2 Vendor Region (NVM, password protected) | Source: JESD301-3 Table 197, p.207

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:1 | SWB_DVFSQ_VOLTAGE_SETTING | RWPE | 001 0100 |
| 0 | RESERVED | RV | 0 |

### [7:1] SWB_DVFSQ_VOLTAGE_SETTING

- Description: Switch Node B Output Regulator Voltage Setting for DVFSQ[1],[2]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 001 0100 → 300 mV or 250 mV

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 0000000 | 0x00 | 200[3] mV or 200[4] mV |
| 0000001 | 0x01 | 205 mV or 202.5 mV |
| 0000010 | 0x02 | 210 mV or 205 mV |
| ... | ... | ... |
| 0010100 | 0x14 | 300 mV or 250 mV |
| ... | ... | ... |
| 1111101 | 0x7D | 825 mV or 512.5 mV |
| 1111110 | 0x7E | 830 mV or 515 mV |
| 1111111 | 0x7F | 835 mV or 517.5 mV |

### [0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

**Notes**

- NOTE 1: PMIC guarantees efficiency spec and all electrical characteristics spec within a range of 450 mV to 550 mV or from 300 mV to 400 mV, depending on the range selection.
- NOTE 2: The setting in this register must be less than or equal to value programmed in Table 191, Register 0x49 [7:1].
- NOTE 3: Table 199, Register 0x51 [3] = ‘0’; 5 mV step size.
- NOTE 4: Table 199, Register 0x51 [3] = ‘1’; 2.5 mV step size.

## R50 (0x50) — SWA_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING, SWD_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING, SWB_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING, SWC_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING

Region: CAMM2 Vendor Region (NVM, password protected) | Source: JESD301-3 Table 198, p.208

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWA_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING | RWPE | 0 |
| 5:4 | SWD_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING | RWPE | 0 |
| 3:2 | SWB_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING | RWPE | 0 |
| 1:0 | SWC_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING | RWPE | 0 |

### [7:6] SWA_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING

- Description: Switch Node A Output Current Limiter Warning Threshold Setting For COT Mode, Ivalley_limit:
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 00 | 7.5. A |
| 01 | 8.5 A |
| 10 | 9.5. A |
| 11 | Vendor specific |

### [5:4] SWD_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING

- Description: Switch Node D Output Current Limiter Warning Threshold Setting For COT Mode, Ivalley_limit:
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 00 | 0.5 A |
| 01 | 1.0 A |
| 10 | 1.5 A |
| 11 | Vendor specific |

### [3:2] SWB_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING

- Description: Switch Node B Output Current Limiter Warning Threshold Setting For COT Mode, Ivalley_limit:
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 00 | 0.5 A |
| 01 | 1.0 A |
| 10 | 1.5 A |
| 11 | Vendor specific |

### [1:0] SWC_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING

- Description: Switch Node C Output Current Limiter Warning Threshold Setting For COT Mode, Ivalley_limit:
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 00 | 0.5 A |
| 01 | 1.0 A |
| 10 | Reserved |
| 11 | Vendor specific |

## R51 (0x51) — VOUT_1.8V_VOLTAGE_SETTING, SWA_VOLTAGE_STEP_SIZE, SWD_VOLTAGE_STEP_SIZE, SWB_VOLTAGE_STEP_SIZE, VOUT_1.0V_VOLTAGE_SETTING, SWC_VOLTAGE_STEP_SIZE

Region: CAMM2 Vendor Region (NVM, password protected) | Source: JESD301-3 Table 199, p.209

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | VOUT_1.8V_VOLTAGE_SETTING | RWPE | 01 |
| 5 | SWA_VOLTAGE_STEP_SIZE | RWPE | 0 |
| 4 | SWD_VOLTAGE_STEP_SIZE | RWPE | 0 |
| 3 | SWB_VOLTAGE_STEP_SIZE | RWPE | 0 |
| 2:1 | VOUT_1.0V_VOLTAGE_SETTING | RWPE | 01 |
| 0 | SWC_VOLTAGE_STEP_SIZE | RWPE | 0 |

### [7:6] VOUT_1.8V_VOLTAGE_SETTING

- Description: VOUT 1.8 V LDO Output Voltage Setting[1]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 01 → 1.8 V

| Code (bin) | Meaning |
|---|---|
| 00 | 1.7 V |
| 01 | 1.8 V |
| 10 | 1.9 V |
| 11 | 2.0 V |

### [5] SWA_VOLTAGE_STEP_SIZE

- Description: SWA Voltage Step Size
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → 5 mV

| Code (bin) | Meaning |
|---|---|
| 0 | 5 mV |
| 1 | 10 mV |

### [4] SWD_VOLTAGE_STEP_SIZE

- Description: SWD Voltage Step Size
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → 5 mV

| Code (bin) | Meaning |
|---|---|
| 0 | 5 mV |
| 1 | 10 mV |

### [3] SWB_VOLTAGE_STEP_SIZE

- Description: SWB Output Voltage Range Selection
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → 5 mV

| Code (bin) | Meaning |
|---|---|
| 0 | 5 mV |
| 1 | 2.5 mV |

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

### [0] SWC_VOLTAGE_STEP_SIZE

- Description: SWC Voltage Step Size
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → 5 mV

| Code (bin) | Meaning |
|---|---|
| 0 | 5 mV |
| 1 | 10 mV |

**Notes**

- NOTE 1: The VOUT_1.8V Power Good threshold in register Table 130, Register 0x1A [2] is always fixed, regardless of the setting in this register.

## R58 (0x58) — POWER_OFF_SEQUENCE_CONFIG0, POWER_OFF_SEQUENCE_CONFIG0_SWA_DISABLE, POWER_OFF_SEQUENCE_CONFIG0_SWD_DISABLE, POWER_OFF_SEQUENCE_CONFIG0_SWB_DISABLE, POWER_OFF_SEQUENCE_CONFIG0_SWC_DISABLE, POWER_OFF_SEQUENCE_CONFIG0_IDLE

Region: CAMM2 Vendor Region (NVM, password protected) | Source: JESD301-3 Table 200, p.210

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | POWER_OFF_SEQUENCE_CONFIG0 | RWPE | 0 |
| 6 | POWER_OFF_SEQUENCE_CONFIG0_SWA_DISABLE | RWPE | 0 |
| 5 | POWER_OFF_SEQUENCE_CONFIG0_SWD_DISABLE | RWPE | 0 |
| 4 | POWER_OFF_SEQUENCE_CONFIG0_SWB_DISABLE | RWPE | 0 |
| 3 | POWER_OFF_SEQUENCE_CONFIG0_SWC_DISABLE | RWPE | 0 |
| 2:0 | POWER_OFF_SEQUENCE_CONFIG0_IDLE | RWPE | 0 |

### [7] POWER_OFF_SEQUENCE_CONFIG0

- Description: PMIC Power Off Sequence Config 0
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Do Not Execute Config 0[2]

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Execute Config 0[2] |
| 1 | Execute Config 0 |

### [6] POWER_OFF_SEQUENCE_CONFIG0_SWA_DISABLE

- Description: Disable Switch Node A Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No action

| Code (bin) | Meaning |
|---|---|
| 0 | No action |
| 1 | Disable Switch Node A Output Regulator |

### [5] POWER_OFF_SEQUENCE_CONFIG0_SWD_DISABLE

- Description: Disable Switch Node D Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No action

| Code (bin) | Meaning |
|---|---|
| 0 | No action |
| 1 | Disable Switch Node D Output Regulator |

### [4] POWER_OFF_SEQUENCE_CONFIG0_SWB_DISABLE

- Description: Disable Switch Node B Output Regulator
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No action

| Code (bin) | Meaning |
|---|---|
| 0 | No action |
| 1 | Disable Switch Node B Output Regulator |

### [3] POWER_OFF_SEQUENCE_CONFIG0_SWC_DISABLE

- Description: Disable Switch Node C Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No action

| Code (bin) | Meaning |
|---|---|
| 0 | No action |
| 1 | Disable Switch Node C Output Regulator |

### [2:0] POWER_OFF_SEQUENCE_CONFIG0_IDLE

- Description: Idle time after Power Off Sequence Config 0[3]
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

- NOTE 1: If more than one configuration register is used for power off sequence, first register must start at Table 200, Register 0x58 and it must go in sequential order to Table 203, Register 0x5B to turn off all regulators. In other words, there must not be any gap of the register that is used for power off sequence.
- NOTE 2: If bit [7] = ‘0’, bits [6:3] must be programmed as ‘000’. If bit [7] = ‘1’, at least one of the bits [6:3] must be programmed as ‘1’.
- NOTE 3: Idle time is the additional time after soft-stop time expires. The PMIC waits sum of soft stop time and idle time before it executes the next power off sequence configuration register. If more than one regulators are disabled, the PMIC uses the largest value of the soft stop time among the regulators that are disabled in this configuration register.

## R59 (0x59) — POWER_OFF_SEQUENCE_CONFIG1, POWER_OFF_SEQUENCE_CONFIG1_SWA_DISABLE, POWER_OFF_SEQUENCE_CONFIG1_SWD_DISABLE, POWER_OFF_SEQUENCE_CONFIG1_SWB_DISABLE, POWER_OFF_SEQUENCE_CONFIG1_SWC_DISABLE, POWER_OFF_SEQUENCE_CONFIG1_IDLE

Region: CAMM2 Vendor Region (NVM, password protected) | Source: JESD301-3 Table 201, p.211

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | POWER_OFF_SEQUENCE_CONFIG1 | RWPE | 0 |
| 6 | POWER_OFF_SEQUENCE_CONFIG1_SWA_DISABLE | RWPE | 0 |
| 5 | POWER_OFF_SEQUENCE_CONFIG1_SWD_DISABLE | RWPE | 0 |
| 4 | POWER_OFF_SEQUENCE_CONFIG1_SWB_DISABLE | RWPE | 0 |
| 3 | POWER_OFF_SEQUENCE_CONFIG1_SWC_DISABLE | RWPE | 0 |
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

- Description: Disable Switch Node A Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No action

| Code (bin) | Meaning |
|---|---|
| 0 | No action |
| 1 | Disable Switch Node A Output Regulator |

### [5] POWER_OFF_SEQUENCE_CONFIG1_SWD_DISABLE

- Description: Disable Switch Node D Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No action

| Code (bin) | Meaning |
|---|---|
| 0 | No action |
| 1 | Disable Switch Node D Output Regulator |

### [4] POWER_OFF_SEQUENCE_CONFIG1_SWB_DISABLE

- Description: Disable Switch Node B Output Regulator
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No action

| Code (bin) | Meaning |
|---|---|
| 0 | No action |
| 1 | Disable Switch Node B Output Regulator |

### [3] POWER_OFF_SEQUENCE_CONFIG1_SWC_DISABLE

- Description: Disable Switch Node C Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No action

| Code (bin) | Meaning |
|---|---|
| 0 | No action |
| 1 | Disable Switch Node C Output Regulator |

### [2:0] POWER_OFF_SEQUENCE_CONFIG1_IDLE

- Description: Idle time after Power Off Sequence Config 1[4]
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

- NOTE 1: If any regulators are disabled in Table 200, Register 0x58 [6:3], those regulators must be configured as ‘1’ in this sequence.
- NOTE 2: If more than one configuration register is used for power off sequence, first register must start at Table 200, Register 0x58 and it must go in sequential order to Table 203, Register 0x5B to turn off all regulators. In other words, there must not be any gap of the register that is used for power off sequence.
- NOTE 3: If bit [7] = ‘0’, bits [6:3] must be programmed as ‘000’. If bit [7] = ‘1’, at least one of the bits [6:3] must be programmed as ‘1’.
- NOTE 4: Idle time is the additional time after soft-stop time expires. The PMIC waits sum of soft stop time and idle time before it executes the next power off sequence configuration register. If more than one regulators are disabled, the PMIC uses the largest value of the soft stop time among the regulators that are disabled in this configuration register.

## R5A (0x5A) — POWER_OFF_SEQUENCE_CONFIG2, POWER_OFF_SEQUENCE_CONFIG2_SWA_DISABLE, POWER_OFF_SEQUENCE_CONFIG2_SWD_DISABLE, POWER_OFF_SEQUENCE_CONFIG2_SWB_DISABLE, POWER_OFF_SEQUENCE_CONFIG2_SWC_DISABLE, POWER_OFF_SEQUENCE_CONFIG2_IDLE

Region: CAMM2 Vendor Region (NVM, password protected) | Source: JESD301-3 Table 202, p.212

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | POWER_OFF_SEQUENCE_CONFIG2 | RWPE | 0 |
| 6 | POWER_OFF_SEQUENCE_CONFIG2_SWA_DISABLE | RWPE | 0 |
| 5 | POWER_OFF_SEQUENCE_CONFIG2_SWD_DISABLE | RWPE | 0 |
| 4 | POWER_OFF_SEQUENCE_CONFIG2_SWB_DISABLE | RWPE | 0 |
| 3 | POWER_OFF_SEQUENCE_CONFIG2_SWC_DISABLE | RWPE | 0 |
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

- Description: Disable Switch Node A Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No action

| Code (bin) | Meaning |
|---|---|
| 0 | No action |
| 1 | Disable Switch Node A Output Regulator |

### [5] POWER_OFF_SEQUENCE_CONFIG2_SWD_DISABLE

- Description: Disable Switch Node D Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No action

| Code (bin) | Meaning |
|---|---|
| 0 | No action |
| 1 | Disable Switch Node D Output Regulator |

### [4] POWER_OFF_SEQUENCE_CONFIG2_SWB_DISABLE

- Description: Disable Switch Node B Output Regulator
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No action

| Code (bin) | Meaning |
|---|---|
| 0 | No action |
| 1 | Disable Switch Node B Output Regulator |

### [3] POWER_OFF_SEQUENCE_CONFIG2_SWC_DISABLE

- Description: Disable Switch Node C Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No action

| Code (bin) | Meaning |
|---|---|
| 0 | No action |
| 1 | Disable Switch Node C Output Regulator |

### [2:0] POWER_OFF_SEQUENCE_CONFIG2_IDLE

- Description: Idle time after Power Off Sequence Config 2[4]
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

- NOTE 1: If any regulators are disabled in Table 200, Register 0x58 [6:3] and Table 201, Register 0x59, [6:3], those regulators must be configured as ‘1’ in this sequence.
- NOTE 2: If more than one configuration register is used for power off sequence, first register must start at Table 200, Register 0x58 and it must go in sequential order to Table 203, Register 0x5B to turn off all regulators. In other words, there must not be any gap of the register that is used for power off sequence.
- NOTE 3: If bit [7] = ‘0’, bits [6:3] must be programmed as ‘000’. If bit [7] = ‘1’, at least one of the bits [6:3] must be programmed as ‘1’.
- NOTE 4: Idle time is the additional time after soft-stop time expires. The PMIC waits sum of soft stop time and idle time before it executes the next power off sequence configuration register. If more than one regulators are disabled, the PMIC uses the largest value of the soft stop time among the regulators that are disabled in this configuration register.

## R5B (0x5B) — POWER_OFF_SEQUENCE_CONFIG3, POWER_OFF_SEQUENCE_CONFIG3_SWA_DISABLE, POWER_OFF_SEQUENCE_CONFIG3_SWD_DISABLE, POWER_OFF_SEQUENCE_CONFIG3_SWB_DISABLE, POWER_OFF_SEQUENCE_CONFIG3_SWC_DISABLE

Region: CAMM2 Vendor Region (NVM, password protected) | Source: JESD301-3 Table 203, p.213

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | POWER_OFF_SEQUENCE_CONFIG3 | RWPE | 0 |
| 6 | POWER_OFF_SEQUENCE_CONFIG3_SWA_DISABLE | RWPE | 0 |
| 5 | POWER_OFF_SEQUENCE_CONFIG3_SWD_DISABLE | RWPE | 0 |
| 4 | POWER_OFF_SEQUENCE_CONFIG3_SWB_DISABLE | RWPE | 0 |
| 3 | POWER_OFF_SEQUENCE_CONFIG3_SWC_DISABLE | RWPE | 0 |
| 2:0 | RESERVED | RV | 0 |

### [7] POWER_OFF_SEQUENCE_CONFIG3

- Description: PMIC Power Off Sequence Config 3[2]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Do Not Execute Config 3

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Execute Config 3 |
| 1 | Execute Config 3 |

### [6] POWER_OFF_SEQUENCE_CONFIG3_SWA_DISABLE

- Description: Disable Switch Node A Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No action

| Code (bin) | Meaning |
|---|---|
| 0 | No action |
| 1 | Disable Switch Node A Output Regulator |

### [5] POWER_OFF_SEQUENCE_CONFIG3_SWD_DISABLE

- Description: Disable Switch Node D Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No action

| Code (bin) | Meaning |
|---|---|
| 0 | No action |
| 1 | Disable Switch Node D Output Regulator |

### [4] POWER_OFF_SEQUENCE_CONFIG3_SWB_DISABLE

- Description: Disable Switch Node B Output Regulator
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No action

| Code (bin) | Meaning |
|---|---|
| 0 | No action |
| 1 | Disable Switch Node B Output Regulator |

### [3] POWER_OFF_SEQUENCE_CONFIG3_SWC_DISABLE

- Description: Disable Switch Node C Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No action

| Code (bin) | Meaning |
|---|---|
| 0 | No action |
| 1 | Disable Switch Node C Output Regulator |

### [2:0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

**Notes**

- NOTE 1: If any regulators are disabled in Table 200, Register 0x58 [6:3], Table 201, Register 0x59, [6:3], and Table 202, Register 0x5A, [6:3], those regulators must be configured as ‘1’ in this sequence.
- NOTE 2: If bit [7] = ‘0’, bits [6:3] must be programmed as ‘000’. If bit [7] = ‘1’, at least one of the bits [6:3] must be programmed as ‘1’.

## R5D (0x5D) — SWA_OUTPUT_SOFT_START_TIME, SWD_OUTPUT_SOFT_START_TIME

Region: CAMM2 Vendor Region (NVM, password protected) | Source: JESD301-3 Table 204, p.214

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:5 | SWA_OUTPUT_SOFT_START_TIME | RWPE | 001 |
| 4 | RESERVED | RV | 0 |
| 3:1 | SWD_OUTPUT_SOFT_START_TIME | RWPE | 001 |
| 0 | RESERVED | RWPE | 0 |

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

### [3:1] SWD_OUTPUT_SOFT_START_TIME

- Description: SWD Output Regulator Soft Start Time After VR Enable[2]
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
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0

**Notes**

- NOTE 1: This is the time it takes for buck regulator to go from 0 V to steady state voltage (the actual voltage varies based on pre-programmed voltage).
- NOTE 2: This is the time it takes for buck regulator to go from 0 V to steady state voltage (the actual voltage varies based on pre-programmed voltage).

## R5E (0x5E) — SWB_OUTPUT_SOFT_START_TIME, SWC_OUTPUT_SOFT_START_TIME

Region: CAMM2 Vendor Region (NVM, password protected) | Source: JESD301-3 Table 205, p.215

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:5 | SWB_OUTPUT_SOFT_START_TIME | RWPE | 001 |
| 4 | RESERVED | RV | 0 |
| 3:1 | SWC_OUTPUT_SOFT_START_TIME | RWPE | 001 |
| 0 | RESERVED | RV | 0 |

### [7:5] SWB_OUTPUT_SOFT_START_TIME

- Description: SWB Output Regulator Soft Start Time After VR Enable[1]
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

### [3:1] SWC_OUTPUT_SOFT_START_TIME

- Description: SWC Output Regulator Soft Start Time After VR Enable1
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

## R5F (0x5F) — R2F_CONTROL, PMIC_AUTO_POWER_ON, UNLOCK_INPUT_PIN_ENABLE, SWB_DVFSQ_VOLTAGE_SLEW_RATE, SWB_VOLTAGE_OFFSET

Region: CAMM2 Vendor Region (NVM, password protected) | Source: JESD301-3 Table 206, p.216

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | R2F_CONTROL | RWPE | 0 |
| 6 | PMIC_AUTO_POWER_ON | RWPE | 0 |
| 5:4 | RESERVED | RV | 0 |
| 3 | UNLOCK_INPUT_PIN_ENABLE | RWPE | 1 |
| 2:1 | SWB_DVFSQ_VOLTAGE_SLEW_RATE | RWPE | 11 |
| 0 | SWB_VOLTAGE_OFFSET | RWPE | 0 |

### [7] R2F_CONTROL

- Description: Host Region R2F[2] Register Setting at First Power On
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → R2F [2] = 0

| Code (bin) | Meaning |
|---|---|
| 0 | R2F [2] = 0 |
| 1 | R2F [2] = 1 |

### [6] PMIC_AUTO_POWER_ON

- Description: PMIC Auto Power On Control
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → PMIC requires VR_EN pin assertion or VR_EN command (i.e., R32 [7] = 1) to turn on output rails

| Code (bin) | Meaning |
|---|---|
| 0 | PMIC requires VR_EN pin assertion or VR_EN command (i.e., R32 [7] = 1) to turn on output rails |
| 1 | PMIC automatically executes R32 [7] = 1 as soon as it detects valid VIN_Bulk and turns on output rails. |

### [5:4] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [3] UNLOCK_INPUT_PIN_ENABLE

- Description: Unlock Input Pin Enable
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 1 → Enable; Unlock input pin receiver is enabled

| Code (bin) | Meaning |
|---|---|
| 0 | Disable; Unlock input pin receiver is disabled |
| 1 | Enable; Unlock input pin receiver is enabled |

### [2:1] SWB_DVFSQ_VOLTAGE_SLEW_RATE

- Description: SWB Output Voltage Slew Rate when transitioning from P3 to DVFSQ and DVFSQ to P3 state[1]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 11 → 1 mV/μs

| Code (bin) | Meaning |
|---|---|
| 00 | 15 mV/μs |
| 01 | 10 mV/μs |
| 10 | 5 mV/μs |
| 11 | 1 mV/μs |

### [0] SWB_VOLTAGE_OFFSET

- Description: SWB Voltage Offset to the setting configured in Table 191, Register 0x49 [7:1]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → No Offset

| Code (bin) | Meaning |
|---|---|
| 0 | No Offset |
| 1 | 600 mV Offset |

**Notes**

- NOTE 1: During the SWB output voltage transition, the PMIC masks the PWR_GOOD output signal assertion to prevent any artificial error due to the crossing of the output voltage threshold setting and keeps the PWR_GOOD signal Hi-Z. However, PMIC does assert PWR_GOOD output signal if there are any abnormal issues that triggers VR Disable command as described in Table 27. Further, PMIC does monitor PWR_GOOD input signal and executes power off config sequence registers if it is registered low when Table 154, Register 0x32 [5] = ‘1’.

## R67 (0x67) — SWA_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD

Region: CAMM2 Vendor Region (NVM, password protected) | Source: JESD301-3 Table 207, p.217

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SWA_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD | RW | 1111 0000 |

### [7:0] SWA_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD

- Description: Switch Node A Output High Current Consumption Warning Threshold
- Attribute: RW — Read/Write
- Default: 1111 0000 → > 30000 mA (if If Table 154, Register 0x32 [1:0] = ‘00’); > 7500 mA (if If Table 154, Register 0x32 [1:0] = ‘01’)

**When: If Table 154, Register 0x32 [1:0] = ‘00’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | > 125 mA |
| 00000010 | 0x02 | > 250 mA |
| ... | ... | ... |
| 11111111 | 0xFF | > 31.875A |

**When: If Table 154, Register 0x32 [1:0] = ‘01’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | > 31.25 mA |
| 00000010 | 0x02 | > 62.5 mA |
| 00000011 | 0x03 | > 93.75 mA |
| 00000100 | 0x04 | > 125 mA |
| ... | ... | ... |
| 11111111 | 0xFF | > 7.968 A |

## R68 (0x68) — SWD_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD

Region: CAMM2 Vendor Region (NVM, password protected) | Source: JESD301-3 Table 208, p.217

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SWD_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD | RW | 0010 0111 |

### [7:0] SWD_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD

- Description: Switch Node D Output High Current Consumption Warning Threshold
- Attribute: RW — Read/Write
- Default: 0010 0111 → > 4875 mA (if If Table 154, Register 0x32 [1:0] = ‘00’); > 1218.75 mA (if If Table 154, Register 0x32 [1:0] = ‘01’)

**When: If Table 154, Register 0x32 [1:0] = ‘00’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | > 125 mA |
| 00000010 | 0x02 | > 250 mA |
| ... | ... | ... |
| 11111111 | 0xFF | > 31.875A |

**When: If Table 154, Register 0x32 [1:0] = ‘01’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | > 31.25 mA |
| 00000010 | 0x02 | > 62.5 mA |
| 00000011 | 0x03 | > 93.75 mA |
| 00000100 | 0x04 | > 125 mA |
| ... | ... | ... |
| 11111111 | 0xFF | > 7.968 A |

## R69 (0x69) — SWB_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD

Region: CAMM2 Vendor Region (NVM, password protected) | Source: JESD301-3 Table 209, p.218

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SWB_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD | RW | 0010 0111 |

### [7:0] SWB_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD

- Description: Switch Node B Output High Current Consumption Warning Threshold
- Attribute: RW — Read/Write
- Default: 0010 0111 → > 4875 mA (if If Table 154, Register 0x32 [1:0] = ‘00’); > 1218.75 mA (if If Table 154, Register 0x32 [1:0] = ‘01’)

**When: If Table 154, Register 0x32 [1:0] = ‘00’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | > 125 mA |
| 00000010 | 0x02 | > 250 mA |
| ... | ... | ... |
| 11111111 | 0xFF | > 31.875A |

**When: If Table 154, Register 0x32 [1:0] = ‘01’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | > 31.25 mA |
| 00000010 | 0x02 | > 62.5 mA |
| 00000011 | 0x03 | > 93.75 mA |
| 00000100 | 0x04 | > 125 mA |
| ... | ... | ... |
| 11111111 | 0xFF | > 7.968 A |

## R6A (0x6A) — SWC_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD

Region: CAMM2 Vendor Region (NVM, password protected) | Source: JESD301-3 Table 210, p.218

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SWC_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD | RW | 0010 0000 |

### [7:0] SWC_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD

- Description: Switch Node C Output High Current Consumption Warning Threshold
- Attribute: RW — Read/Write
- Default: 0010 0000 → > 4000 mA (if If Table 154, Register 0x32 [1:0] = ‘00’); > 1000 mA (if If Table 154, Register 0x32 [1:0] = ‘01’)

**When: If Table 154, Register 0x32 [1:0] = ‘00’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | > 125 mA |
| 00000010 | 0x02 | > 250 mA |
| ... | ... | ... |
| 11111111 | 0xFF | > 31.875A |

**When: If Table 154, Register 0x32 [1:0] = ‘01’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | > 31.25 mA |
| 00000010 | 0x02 | > 62.5 mA |
| 00000011 | 0x03 | > 93.75 mA |
| 00000100 | 0x04 | > 125 mA |
| ... | ... | ... |
| 11111111 | 0xFF | > 7.968 A |

## R6D (0x6D) — SWA_MAX_VOUT_DETECTION, SWA_UNSUPPORTED_VOLTAGE_DETECTION_STATUS, SWD_MAX_VOUT_DETECTION, SWD_UNSUPPORTED_VOLTAGE_DETECTION_STATUS

Region: CAMM2 Vendor Region (NVM, password protected) | Source: JESD301-3 Table 211, p.219

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:5 | SWA_MAX_VOUT_DETECTION | RWPE | 101 |
| 4 | SWA_UNSUPPORTED_VOLTAGE_DETECTION_STATUS | ROE | 0 |
| 3:1 | SWD_MAX_VOUT_DETECTION | RWPE | 101 |
| 0 | SWD_UNSUPPORTED_VOLTAGE_DETECTION_STATUS | ROE | 0 |

### [7:5] SWA_MAX_VOUT_DETECTION

- Description: SWA Max Output Voltage Detection Threshold[1]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 101 → 1200 mV

| Code (bin) | Meaning |
|---|---|
| 000 | 700 mV |
| 001 | 800 mV |
| ... | ... |
| 111 | 1400 mV |

### [4] SWA_UNSUPPORTED_VOLTAGE_DETECTION_STATUS

- Description: SWA Output Voltage Programmed Value Exceed the Threshold Setting Status[2],[3]
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0 → SWA is programmed less than threshold

| Code (bin) | Meaning |
|---|---|
| 0 | SWA is programmed less than threshold |
| 1 | SWA is programmed greater than threshold |

### [3:1] SWD_MAX_VOUT_DETECTION

- Description: SWD Max Output Voltage Detection Threshold[1]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 101 → 1200 mV

| Code (bin) | Meaning |
|---|---|
| 000 | 700 mV |
| 001 | 800 mV |
| ... | ... |
| 111 | 1400 mV |

### [0] SWD_UNSUPPORTED_VOLTAGE_DETECTION_STATUS

- Description: SWD Output Voltage Programmed Value Exceed the Threshold Setting Status[3],[4]
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0 → SWD is programmed less than threshold

| Code (bin) | Meaning |
|---|---|
| 0 | SWD is programmed less than threshold |
| 1 | SWD is programmed greater than threshold |

**Notes**

- NOTE 1: The DIMM vendor sets this threshold during the assembly.
- NOTE 2: The PMIC checks the SWA output programmed value in Table 137, Register 0x21, [7:1] and Table 147, Register 0x2B, [5] and compares it against the threshold set in Table 211, Register 0x6D [7:5] after PMIC receives VR Enable command (either via VR_EN pin or I2C/I3C bus command or auto power on). If SWA output programmed value exceeds the threshold, it sets this register to ‘1’.
- NOTE 3: This register can only be cleared after CAMM2 vendor region password is provided and with a command code: R39 = 0x86 only.
- NOTE 4: The PMIC checks the SWD output programmed value in Table 139, Register 0x23, [7:1] and Table 147, Register 0x2B, [4] and compares it against the threshold set in Table 211, Register 0x6D [3:1] after PMIC receives VR Enable command (either via VR_EN pin or I2C/I3C bus command or auto power on). If SWD output programmed value exceeds the threshold, it sets this register to ‘1’.

## R6E (0x6E) — SWB_MAX_VOUT_DETECTION, SWB_UNSUPPORTED_VOLTAGE_DETECTION_STATUS, SWC_MAX_VOUT_DETECTION, SWC_UNSUPPORTED_VOLTAGE_DETECTION_STATUS

Region: CAMM2 Vendor Region (NVM, password protected) | Source: JESD301-3 Table 212, p.220

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:5 | SWB_MAX_VOUT_DETECTION | RWPE | 001 |
| 4 | SWB_UNSUPPORTED_VOLTAGE_DETECTION_STATUS | ROE | 0 |
| 3 | RESERVED | RV | 0 |
| 2:1 | SWC_MAX_VOUT_DETECTION | RWPE | 11 |
| 0 | SWC_UNSUPPORTED_VOLTAGE_DETECTION_STATUS | ROE | 0 |

### [7:5] SWB_MAX_VOUT_DETECTION

- Description: SWB Max Output Voltage Detection Threshold[1]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 001 → 800 mV

| Code (bin) | Meaning |
|---|---|
| 000 | 700 mV |
| 001 | 800 mV |
| ... | ... |
| 111 | 1400 mV |

### [4] SWB_UNSUPPORTED_VOLTAGE_DETECTION_STATUS

- Description: SWB Output Voltage Programmed Value Exceed the Threshold Setting Status[2],[3]
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0 → SWB is programmed less than threshold

| Code (bin) | Meaning |
|---|---|
| 0 | SWB is programmed less than threshold |
| 1 | SWB is programmed greater than threshold |

### [3] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [2:1] SWC_MAX_VOUT_DETECTION

- Description: SWC Max Output Voltage Detection Threshold[1]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 11 → 2200 mV

| Code (bin) | Meaning |
|---|---|
| 00 | 1900 mV |
| 01 | 2000 mV |
| 10 | 2100 mV |
| 11 | 2200 mV |

### [0] SWC_UNSUPPORTED_VOLTAGE_DETECTION_STATUS

- Description: SWC Output Voltage Programmed Value Exceed the Threshold Setting Status[3],[4]
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0 → SWC is programmed less than threshold

| Code (bin) | Meaning |
|---|---|
| 0 | SWC is programmed less than threshold |
| 1 | SWC is programmed greater than threshold |

**Notes**

- NOTE 1: The DIMM vendor sets this threshold during the assembly.
- NOTE 2: The PMIC checks the SWB output programmed value in Table 141, Register 0x25, [7:1] and Table 147, Register 0x2B, [3] and compares it against the threshold set in Table 212, Register 0x6E [7:5] after PMIC receives VR Enable command (either via VR_EN pin or I2C/I3C bus command or auto power on). If SWB output programmed value exceeds the threshold, it sets this register to ‘1’.
- NOTE 3: This register can only be cleared after CAMM2 vendor region password is provided and with a command code: R39 = 0x86 only.
- NOTE 4: The PMIC checks the SWC output programmed value in Table 143, Register 0x27, [7:1] and Table 147, Register 0x2B, [0] and compares it against the threshold set in Table 212, Register 0x6E [2:1] after PMIC receives VR Enable command (either via VR_EN pin or I2C/I3C bus command or auto power on). If SWC output programmed value exceeds the threshold, it sets this register to ‘1’.

## R100 (0x100) — SWA_OUTPUT_CURRENT_POWER_MEASUREMENT_MSB, SWD_OUTPUT_CURRENT_POWER_MEASUREMENT_MSB, SWB_OUTPUT_CURRENT_POWER_MEASUREMENT_MSB, SWC_OUTPUT_CURRENT_POWER_MEASUREMENT_MSB

Region: Host Region | Source: JESD301-3 Table 168, p.186

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWA_OUTPUT_CURRENT_POWER_MEASUREMENT_MSB | RO | - |
| 5:4 | SWD_OUTPUT_CURRENT_POWER_MEASUREMENT_MSB | RO | - |
| 3:2 | SWB_OUTPUT_CURRENT_POWER_MEASUREMENT_MSB | RO | - |
| 1:0 | SWC_OUTPUT_CURRENT_POWER_MEASUREMENT_MSB | RO | - |

### [7:6] SWA_OUTPUT_CURRENT_POWER_MEASUREMENT_MSB

- Description: MSB bits - SWA Output Current or Output Power or Total SWA+SWB+SWC+SWD Output Power Measurement[5]. This two MSB bits plus 8 bit register in Table 169, Register 0x102[7:0] makes 10 bit encoding as shown in Table 169, Register 0x102.
- Attribute: RO — Read Only (writes have no effect)
- Default: -
- Values: no per-value encoding is listed in the spec for this field.

### [5:4] SWD_OUTPUT_CURRENT_POWER_MEASUREMENT_MSB

- Description: MSB bits - SWD Output Current or Output Power Measurement. This two MSB bits plus 8 bit register in Table 170, Register 0x103[7:0] makes 10 bit encoding as shown in Table 170, Register 0x103.
- Attribute: RO — Read Only (writes have no effect)
- Default: -
- Values: no per-value encoding is listed in the spec for this field.

### [3:2] SWB_OUTPUT_CURRENT_POWER_MEASUREMENT_MSB

- Description: MSB bits - SWB Output Current or Output Power Measurement This two MSB bits plus 8 bit register in Table 171, Register 0x104[7:0] makes 10 bit encoding as shown in Table 171, Register 0x104.
- Attribute: RO — Read Only (writes have no effect)
- Default: -
- Values: no per-value encoding is listed in the spec for this field.

### [1:0] SWC_OUTPUT_CURRENT_POWER_MEASUREMENT_MSB

- Description: MSB bits - SWC Output Current or Output Power Measurement This two MSB bits plus 8 bit register in Table 172, Register 0x105[7:0] makes 10 bit encoding as shown in Table 172, Register 0x105.
- Attribute: RO — Read Only (writes have no effect)
- Default: -
- Values: no per-value encoding is listed in the spec for this field.

**Notes**

- NOTE 1: The PMIC reports current or power measurement as long as there is no output over voltage or output under voltage lockout event that triggers the VR Disable command. If PMIC triggers VR Disable command, PMIC does not report current or power measurement and register content may have stale data. For all other events that causes PMIC’s power good status as Not Good, the PMIC continues to provide current or power measurement.
- NOTE 2: This register is only applicable if Table 154, Register 0x32 = ‘01’.
- NOTE 3: If Table 131, Register 0x1B [6] = ‘0’, the PMIC reports current measurement. If Table 131, Register 0x1B [6] = ‘1’, the PMIC reports power measurement.
- NOTE 4: The Host must read ADC current or power measurement bytes in order from MSB to LSB (i.e., R100 to R105) via I2C/I3C block read commands.
- NOTE 5: The register Table 131, Register 0x1B [6] must be configured as ‘1’.

## R102 (0x102) — SWA_OUTPUT_CURRENT_POWER_MEASUREMENT_LSB

Region: Host Region | Source: JESD301-3 Table 169, p.187

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SWA_OUTPUT_CURRENT_POWER_MEASUREMENT_LSB | RO | - |

### [7:0] SWA_OUTPUT_CURRENT_POWER_MEASUREMENT_LSB

- Description: LSB bits - SWA Output Current or Output Power or Total SWA+SWB+SWC+SWD Output Power Measurement The 2 MSB bits Table 168, Register 0x100 [7:6] plus this 8 bit register makes 10 bit encoding as shown below.
- Attribute: RO — Read Only (writes have no effect)
- Default: -
- Note: the codes below are wider than this 8-bit field; the encoding combines bits from more than one field/register (see Description).

**When: If Table 130, Register 0x1A[1] = ‘0’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 0000000000 | 0x000 | Undefined |
| 0000000001 | 0x001 | 31.25mA or 31.25mW |
| 0000000010 | 0x002 | 62.5mA or 62.5mW |
| ... |  | ... |
| 1111111111 | 0x3FF | > 15.936A or 15.936W |

**When: If Table 130, Register 0x1A[1] = ‘1’ — Sum of SWA, SWD, SWB and SWC Output Power[5]**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 0000000000 | 0x000 | Undefined |
| 0000000001 | 0x001 | 31.25mW |
| 0000000010 | 0x002 | 62.5mW |
| ... |  | ... |
| 1111111111 | 0x3FF | > 15.936W |

**Notes**

- NOTE 1: The PMIC reports current or power measurement as long as there is no output over voltage or output under voltage lockout event that triggers the VR Disable command. If PMIC triggers VR Disable command, PMIC does not report current or power measurement and register content may have stale data. For all other events that causes PMIC’s power good status as Not Good, the PMIC continues to provide current or power measurement.
- NOTE 2: This register is only applicable if Table 154, Register 0x32 = ‘01’.
- NOTE 3: If Table 131, Register 0x1B [6] = ‘0’, the PMIC reports current measurement. If Table 131, Register 0x1B [6] = ‘1’, the PMIC reports power measurement.
- NOTE 4: The Host must read ADC current or power measurement bytes in order from MSB to LSB (i.e., R100 to R105) via I2C/I3C block read commands.
- NOTE 5: The register Table 131, Register 0x1B [6] must be configured as ‘1’.

## R103 (0x103) — SWD_OUTPUT_CURRENT_POWER_MEASUREMENT_LSB

Region: Host Region | Source: JESD301-3 Table 170, p.188

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SWD_OUTPUT_CURRENT_POWER_MEASUREMENT_LSB | RO | - |

### [7:0] SWD_OUTPUT_CURRENT_POWER_MEASUREMENT_LSB

- Description: LSB bits - SWD Output Current or Output Power Measurement The 2 MSB bits Table 168, Register 0x100 [5:4] plus this 8 bit register makes 10 bit encoding as shown below.
- Attribute: RO — Read Only (writes have no effect)
- Default: -
- Note: the codes below are wider than this 8-bit field; the encoding combines bits from more than one field/register (see Description).

**When: If Table 130, Register 0x1A[1] = ‘0’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 0000000000 | 0x000 | Undefined |
| 0000000001 | 0x001 | 31.25 mA or 31.25 mW |
| 0000000010 | 0x002 | 62.5 mA or 62.5 mW |
| ... |  | ... |
| 1111111111 | 0x3FF | > 15.936 A or 15.936 W |

**Notes**

- NOTE 1: The PMIC reports current or power measurement as long as there is no output over voltage or output under voltage lockout event that triggers the VR Disable command. If PMIC triggers VR Disable command, PMIC does not report current or power measurement and register content may have stale data. For all other events that causes PMIC’s power good status as Not Good, the PMIC continues to provide current or power measurement.
- NOTE 2: This register is only applicable if Table 154, Register 0x32 = ‘01’.
- NOTE 3: If Table 131, Register 0x1B [6] = ‘0’, the PMIC reports current measurement. If Table 131, Register 0x1B [6] = ‘1’, the PMIC reports power measurement.
- NOTE 4: The Host must read ADC current or power measurement bytes in order from MSB to LSB (i.e., R100 to R105) via I2C/I3C block read commands.

## R104 (0x104) — SWB_OUTPUT_CURRENT_POWER_MEASUREMENT_LSB

Region: Host Region | Source: JESD301-3 Table 171, p.188

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SWB_OUTPUT_CURRENT_POWER_MEASUREMENT_LSB | RO | - |

### [7:0] SWB_OUTPUT_CURRENT_POWER_MEASUREMENT_LSB

- Description: LSB bits - SWB Output Current or Output Power Measurement The 2 MSB bits Table 168, Register 0x100 [3:2] plus this 8 bit register makes 10 bit encoding as shown below.
- Attribute: RO — Read Only (writes have no effect)
- Default: -
- Note: the codes below are wider than this 8-bit field; the encoding combines bits from more than one field/register (see Description).

**When: If Table 130, Register 0x1A[1] = ‘0’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 0000000000 | 0x000 | Undefined |
| 0000000001 | 0x001 | 31.25 mA or 31.25 mW |
| 0000000010 | 0x002 | 62.5 mA or 62.5 mW |
| ... |  | ... |
| 1111111111 | 0x3FF | > 15.936 A or 15.936 W |

**Notes**

- NOTE 1: The PMIC reports current or power measurement as long as there is no output over voltage or output under voltage lockout event that triggers the VR Disable command. If PMIC triggers VR Disable command, PMIC does not report current or power measurement and register content may have stale data. For all other events that causes PMIC’s power good status as Not Good, the PMIC continues to provide current or power measurement.
- NOTE 2: This register is only applicable if Table 154, Register 0x32 = ‘01’.
- NOTE 3: If Table 131, Register 0x1B [6] = ‘0’, the PMIC reports current measurement. If Table 131, Register 0x1B [6] = ‘1’, the PMIC reports power measurement.
- NOTE 4: The Host must read ADC current or power measurement bytes in order from MSB to LSB (i.e., R100 to R105) via I2C/I3C block read commands.

## R105 (0x105) — SWC_OUTPUT_CURRENT_POWER_MEASUREMENT_LSB

Region: Host Region | Source: JESD301-3 Table 172, p.189

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SWC_OUTPUT_CURRENT_POWER_MEASUREMENT_LSB | RO | - |

### [7:0] SWC_OUTPUT_CURRENT_POWER_MEASUREMENT_LSB

- Description: LSB bits - SWC Output Current or Output Power Measurement The 2 MSB bits Table 168, Register 0x100 [1:0] plus this 8 bit register makes 10 bit encoding as shown below.
- Attribute: RO — Read Only (writes have no effect)
- Default: -
- Note: the codes below are wider than this 8-bit field; the encoding combines bits from more than one field/register (see Description).

**When: If Table 130, Register 0x1A[1] = ‘0’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 0000000000 | 0x000 | Undefined |
| 0000000001 | 0x001 | 31.25 mA or 31.25 mW |
| 0000000010 | 0x002 | 62.5 mA or 62.5 mW |
| ... |  | ... |
| 1111111111 | 0x3FF | > 15.936 A or 15.936 W |

**Notes**

- NOTE 1: The PMIC reports current or power measurement as long as there is no output over voltage or output under voltage lockout event that triggers the VR Disable command. If PMIC triggers VR Disable command, PMIC does not report current or power measurement and register content may have stale data. For all other events that causes PMIC’s power good status as Not Good, the PMIC continues to provide current or power measurement.
- NOTE 2: This register is only applicable if Table 154, Register 0x32 = ‘01’.
- NOTE 3: If Table 131, Register 0x1B [6] = ‘0’, the PMIC reports current measurement. If Table 131, Register 0x1B [6] = ‘1’, the PMIC reports power measurement.
- NOTE 4: The Host must read ADC current or power measurement bytes in order from MSB to LSB (i.e., R100 to R105) via I2C/I3C block read commands.

## R109 (0x109) — SWB_DISABLE_PIN_INPUT_STATUS_AT_VR_EN

Region: Host Region | Source: JESD301-3 Table 173, p.189

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:1 | RESERVED | RV | - |
| 0 | SWB_DISABLE_PIN_INPUT_STATUS_AT_VR_EN | RO | - |

### [7:1] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: -

### [0] SWB_DISABLE_PIN_INPUT_STATUS_AT_VR_EN

- Description: SWB_Disable Input Pin Level Status at VR_EN Command[1],[2],[3]
- Attribute: RO — Read Only (writes have no effect)
- Default: -

| Code (bin) | Meaning |
|---|---|
| 0 | Low |
| 1 | High |

**Notes**

- NOTE 1: The controller cannot clear this register via any I2C/I3C bus command.
- NOTE 2: The PMIC clears this register when PMIC executes VR Disable command (either via VR_EN pin or I2C/I3C bus command or PWR_GOOD input or fault event)
- NOTE 3: At first power on, prior to first VR Enable command, the default register value is a don’t care.

## R130 (0x130) — SERIAL_NUMBER_BYTE_0

Region: Host Region | Source: JESD301-3 Table 174, p.189

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SERIAL_NUMBER_BYTE_0 | ROA | - |

### [7:0] SERIAL_NUMBER_BYTE_0

- Description: Byte 0 of the unique 40-bit serial number Serial number is vendor specific
- Attribute: ROA — Read Only (writes have no effect); Persistent, set by the PMIC vendor at manufacturing
- Default: -
- Values: no per-value encoding is listed in the spec for this field.

## R131 (0x131) — SERIAL_NUMBER_BYTE_1

Region: Host Region | Source: JESD301-3 Table 175, p.190

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SERIAL_NUMBER_BYTE_1 | ROA | - |

### [7:0] SERIAL_NUMBER_BYTE_1

- Description: Byte 1 of the unique 40-bit serial number Serial number is vendor specific
- Attribute: ROA — Read Only (writes have no effect); Persistent, set by the PMIC vendor at manufacturing
- Default: -
- Values: no per-value encoding is listed in the spec for this field.

## R132 (0x132) — SERIAL_NUMBER_BYTE_2

Region: Host Region | Source: JESD301-3 Table 176, p.190

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SERIAL_NUMBER_BYTE_2 | ROA | - |

### [7:0] SERIAL_NUMBER_BYTE_2

- Description: Byte 2 of the unique 40-bit serial number Serial number is vendor specific
- Attribute: ROA — Read Only (writes have no effect); Persistent, set by the PMIC vendor at manufacturing
- Default: -
- Values: no per-value encoding is listed in the spec for this field.

## R133 (0x133) — SERIAL_NUMBER_BYTE_3

Region: Host Region | Source: JESD301-3 Table 177, p.190

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SERIAL_NUMBER_BYTE_3 | ROA | - |

### [7:0] SERIAL_NUMBER_BYTE_3

- Description: Byte 3 of the unique 40-bit serial number Serial number is vendor specific
- Attribute: ROA — Read Only (writes have no effect); Persistent, set by the PMIC vendor at manufacturing
- Default: -
- Values: no per-value encoding is listed in the spec for this field.

## R134 (0x134) — SERIAL_NUMBER_BYTE_4

Region: Host Region | Source: JESD301-3 Table 178, p.190

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SERIAL_NUMBER_BYTE_4 | ROA | - |

### [7:0] SERIAL_NUMBER_BYTE_4

- Description: Byte 4 of the unique 40-bit serial number Serial number is vendor specific
- Attribute: ROA — Read Only (writes have no effect); Persistent, set by the PMIC vendor at manufacturing
- Default: -
- Values: no per-value encoding is listed in the spec for this field.

## R135 (0x135) — SERIAL_NUMBER_BYTE_5

Region: Host Region | Source: JESD301-3 Table 179, p.190

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SERIAL_NUMBER_BYTE_5 | ROA | - |

### [7:0] SERIAL_NUMBER_BYTE_5

- Description: Byte 5 of the unique 40-bit serial number Serial number is vendor specific
- Attribute: ROA — Read Only (writes have no effect); Persistent, set by the PMIC vendor at manufacturing
- Default: -
- Values: no per-value encoding is listed in the spec for this field.

## R136 (0x136) — SERIAL_NUMBER_BYTE_6

Region: Host Region | Source: JESD301-3 Table 180, p.190

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SERIAL_NUMBER_BYTE_6 | ROA | - |

### [7:0] SERIAL_NUMBER_BYTE_6

- Description: Byte 6 of the unique 40-bit serial number Serial number is vendor specific CAMM2 Vendor Region Register Definition
- Attribute: ROA — Read Only (writes have no effect); Persistent, set by the PMIC vendor at manufacturing
- Default: -
- Values: no per-value encoding is listed in the spec for this field.
