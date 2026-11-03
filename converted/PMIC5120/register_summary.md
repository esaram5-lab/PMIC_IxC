# PMIC5120 Register Map Summary

Source: JESD301-6 — PMIC5120 Power Management IC Standard, Version 1.0 (February 2025). Application: client (DDR5 SODIMM, DDR5 UDIMM, DDR5 CSODIMM, DDR5 CUDIMM).

Elided ranges ('...') follow the linear pattern of the neighbouring codes; see registers/<addr>.md for every value spelled out.

## R00 (0x00) — SERIAL_NUMBER_BYTE_0

Region: Host Region | Source: JESD301-6 Table 96, p.123

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SERIAL_NUMBER_BYTE_0 | ROE | 0 |

### [7:0] SERIAL_NUMBER_BYTE_0

- Description: Byte 0 of the unique 40-bit serial number stored in {[R00:R03],R0D} Serial Number is vendor-specific
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0
- Values: no per-value encoding is listed in the spec for this field.

## R01 (0x01) — SERIAL_NUMBER_BYTE_1

Region: Host Region | Source: JESD301-6 Table 97, p.123

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SERIAL_NUMBER_BYTE_1 | ROE | 0 |

### [7:0] SERIAL_NUMBER_BYTE_1

- Description: Byte 1 of the unique 40-bit serial number stored in {[R00:R03],R0D} Serial Number is vendor-specific
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0
- Values: no per-value encoding is listed in the spec for this field.

## R02 (0x02) — SERIAL_NUMBER_BYTE_2

Region: Host Region | Source: JESD301-6 Table 98, p.123

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SERIAL_NUMBER_BYTE_2 | ROE | 0 |

### [7:0] SERIAL_NUMBER_BYTE_2

- Description: Byte 2 of the unique 40-bit serial number stored in {[R00:R03],R0D} Serial Number is vendor-specific
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0
- Values: no per-value encoding is listed in the spec for this field.

## R03 (0x03) — SERIAL_NUMBER_BYTE_3

Region: Host Region | Source: JESD301-6 Table 99, p.123

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SERIAL_NUMBER_BYTE_3 | ROE | 0 |

### [7:0] SERIAL_NUMBER_BYTE_3

- Description: Byte 3 of the unique 40-bit serial number stored in {[R00:R03],R0D} Serial Number is vendor-specific
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0
- Values: no per-value encoding is listed in the spec for this field.

## R04 (0x04) — GLOBAL_ERROR_COUNT, GLOBAL_ERROR_LOG_BUCK_OV_OR_UV, GLOBAL_ERROR_LOG_VIN_BULK_OVER_VOLTAGE, GLOBAL_ERROR_LOG_CRITICAL_TEMPERATURE

Region: Host Region | Source: JESD301-6 Table 100, p.124

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

- NOTE 1: The PMIC always attempts to write this register into its non-volatile memory. However, it may not be guaranteed depending on how fast the host may shut off the input power to the PMIC. The PMIC needs minimum of 4.0 V for VIN_Bulk voltage and 200 ms duration from PWR_GOOD signal assertion to guarantee the write operation into non-volatile memory.
- NOTE 2: Host must explicitly perform Erase operation to erase this entire register via command in Table 153, Register 0x39. The PMIC needs minimum of 200 ms for Erase operation.
- NOTE 3: PMIC counts the error since last erase operation and if more than one error occurs, it sets this bit to ‘1’. Host must explicitly perform Erase operation to erase this entire register Table 100, Register 0x04 [7:0].
- NOTE 4: PMIC sets the bit when error occurs.

## R05 (0x05) — SWA_POWER_GOOD, SWB_POWER_GOOD, SWC_POWER_GOOD, PMIC_ERROR_LOG

Region: Host Region | Source: JESD301-6 Table 101, p.125

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | RESERVED | RV | 0 |
| 6 | SWA_POWER_GOOD | ROE | 0 |
| 5 | RESERVED | RV | 0 |
| 4 | SWB_POWER_GOOD | ROE | 0 |
| 3 | SWC_POWER_GOOD | ROE | 0 |
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
| 1 | Power On - SWA Power Not Good |

### [5] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [4] SWB_POWER_GOOD

- Description: PMIC Power On - SWB Power Not Good[3]
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0 → Normal Power On

| Code (bin) | Meaning |
|---|---|
| 0 | Normal Power On |
| 1 | Power On - SWB Power Not Good |

### [3] SWC_POWER_GOOD

- Description: PMIC Power On - SWC Power Not Good[3]
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
| 010 | Buck Regulator Output Over or Under Voltage[4] |
| 011 | Critical Temperature |
| 100 | VIN_Bulk Input Over Voltage |
| 101 | Reserved |
| 110 | Reserved |
| 111 | VIN_Bulk Under Voltage |

**Notes**

- NOTE 1: The PMIC always attempts to write this register into its non-volatile memory. However, it may not be guaranteed depending on how fast the host may shut off the input power to the PMIC. The PMIC needs minimum of 4.0 V for VIN_Bulk voltage and 200 ms duration from PWR_GOOD signal assertion to guarantee the write operation into non-volatile memory.
- NOTE 2: This entire register status reflects previous power down cycle of the PMIC and is updated by the PMIC on its own at each power cycle, if update is needed. Because this register is updated only if there is an update needed, there is no NVM life time impact. This register is cleared when host issues the erase command via Table 153, Register 0x39. The PMIC needs minimum of 200 ms for Erase operation.
- NOTE 3: This register is set only if PMIC generates internal VR Disable command due to fault condition.
- NOTE 4: This code is a logical OR function of Table 102, Register 0x06 [7:0] register bits.

## R06 (0x06) — SWA_UNDER_VOLTAGE_LOCKOUT, SWB_UNDER_VOLTAGE_LOCKOUT, SWC_UNDER_VOLTAGE_LOCKOUT, SWA_OVER_VOLTAGE, SWB_OVER_VOLTAGE, SWC_OVER_VOLTAGE

Region: Host Region | Source: JESD301-6 Table 102, p.126

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | SWA_UNDER_VOLTAGE_LOCKOUT | ROE | 0 |
| 6 | RESERVED | RV | 0 |
| 5 | SWB_UNDER_VOLTAGE_LOCKOUT | ROE | 0 |
| 4 | SWC_UNDER_VOLTAGE_LOCKOUT | ROE | 0 |
| 3 | SWA_OVER_VOLTAGE | ROE | 0 |
| 2 | RESERVED | RV | 0 |
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

### [6] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [5] SWB_UNDER_VOLTAGE_LOCKOUT

- Description: PMIC Power On - SWB Under Voltage Lockout[3]
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

### [2] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [1] SWB_OVER_VOLTAGE

- Description: PMIC Power On - SWB Over Voltage[3]
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

- NOTE 1: The PMIC always attempts to write this register into its non-volatile memory. However, it may not be guaranteed depending on how fast the host may shut off the input power to the PMIC. The PMIC needs minimum of 4.0 V for VIN_Bulk voltage and 200 ms duration from PWR_GOOD signal assertion to guarantee the write operation into non-volatile memory.
- NOTE 2: This entire register status reflects previous power down cycle of the PMIC and is updated by the PMIC on its own at each power cycle, if update is needed. Because this register is updated only if there is an update needed, there is no NVM life time impact. This register is cleared when host issues the erase command via Table 153, Register 0x39. The PMIC needs minimum of 200 ms for Erase operation.
- NOTE 3: Only applicable if Table 173, Register 0x4F [0] = ‘0’.

## R07 (0x07) — Reserved

Region: Host Region | Source: JESD301-6 Table 103, p.127

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | RESERVED | ROE | 0 |

### [7:0] RESERVED

- Description: Reserved
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0

**Notes**

- NOTE 1: The PMIC always attempts to write this register into its non-volatile memory. However, it may not be guaranteed depending on how fast the host may shut off the input power to the PMIC. The PMIC needs minimum of 4.0 V for VIN_Bulk voltage and 200 ms duration from PWR_GOOD signal assertion to guarantee the write operation into non-volatile memory.
- NOTE 2: This entire register status reflects previous power down cycle of the PMIC and is updated by the PMIC on its own at each power cycle, if update is needed. Because this register is updated only if there is an update needed, there is no NVM life time impact. This register is cleared when host issues the erase command via Table 153, Register 0x39. The PMIC needs minimum of 200 ms for Erase operation.

## R08 (0x08) — CRITICAL_TEMP_SHUTDOWN_STATUS, SWA_OUTPUT_POWER_GOOD_STATUS, SWB_OUTPUT_POWER_GOOD_STATUS, SWC_OUTPUT_POWER_GOOD_STATUS, VIN_BULK_INPUT_OVER_VOLTAGE_STATUS

Region: Host Region | Source: JESD301-6 Table 104, p.127

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | RESERVED | RV | 0 |
| 6 | CRITICAL_TEMP_SHUTDOWN_STATUS | RO | 0 |
| 5 | SWA_OUTPUT_POWER_GOOD_STATUS | RO | 0 |
| 4 | RESERVED | RV | 0 |
| 3 | SWB_OUTPUT_POWER_GOOD_STATUS | RO | 0 |
| 2 | SWC_OUTPUT_POWER_GOOD_STATUS | RO | 0 |
| 1 | RESERVED | RV | 0 |
| 0 | VIN_BULK_INPUT_OVER_VOLTAGE_STATUS | RO | 0 |

### [7] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [6] CRITICAL_TEMP_SHUTDOWN_STATUS

- Description: Critical Temperature Shutdown Status[1]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No Critical Temperature Shutdown

| Code (bin) | Meaning |
|---|---|
| 0 | No Critical Temperature Shutdown |
| 1 | Critical Temperature Shutdown |

### [5] SWA_OUTPUT_POWER_GOOD_STATUS

- Description: Switch Node A Output Power Good Status[2]
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

### [3] SWB_OUTPUT_POWER_GOOD_STATUS

- Description: Switch Node B Output Power Good Status[3],[4]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → Power Good

| Code (bin) | Meaning |
|---|---|
| 0 | Power Good |
| 1 | Power Not Good |

### [2] SWC_OUTPUT_POWER_GOOD_STATUS

- Description: Switch Node C Output Power Good Status[5]
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

- Description: VIN_Bulk Input Supply Over Voltage Status[6]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → No Over Voltage

| Code (bin) | Meaning |
|---|---|
| 0 | No Over Voltage |
| 1 | Over Voltage |

**Notes**

- NOTE 1: This register is set when PMIC temperature goes above the threshold setting in register Table 142, Register 0x2E [2:0].
- NOTE 2: This register is set when SWA output voltage goes either below the threshold setting in register Table 129, Register 0x21,[0] or above the threshold setting in register Table 130, Register 0x22, [7:6].
- NOTE 3: This register is set when SWB output goes either below the threshold setting in register Table 133, Register 0x25,[0] or above the threshold setting in register Table 134, Register 0x26, [7:6].
- NOTE 4: Only applicable if Table 173, Register 0x4F [0] = ‘0’.
- NOTE 5: This register is set when SWC output goes either below the threshold setting in register Table 135, Register 0x27,[0] or above the threshold setting in register Table 136, Register 0x28, [7:6].
- NOTE 6: This register is set when VIN_Bulk input voltage goes above the threshold setting in register Table 123, Register 0x1B [7].

## R09 (0x09) — PMIC_HIGH_TEMP_WARNING_STATUS, VOUT_1.8V_OUTPUT_POWER_GOOD_STATUS, SWA_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS, SWB_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS, SWC_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS

Region: Host Region | Source: JESD301-6 Table 105, p.128

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | PMIC_HIGH_TEMP_WARNING_STATUS | RO | 0 |
| 6 | RESERVED | RV | 0 |
| 5 | VOUT_1.8V_OUTPUT_POWER_GOOD_STATUS | RO | 0 |
| 4 | RESERVED | RV | 0 |
| 3 | SWA_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS | RO | 0 |
| 2 | RESERVED | RV | 0 |
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

### [2] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [1] SWB_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS

- Description: Switch Node B High Output Current Consumption Warning Status[4],[5]
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

- NOTE 1: This register is set when PMIC temperature goes above the threshold setting in Table 123, Register 0x1B [2:0].
- NOTE 2: This register is set when VOUT_1.8V output exceeds the threshold setting in register Table 122, Register 0x1A [2].
- NOTE 3: This register is set when SWA output current consumption goes above the threshold setting in Table 124, Register 0x1C [7:0].
- NOTE 4: This register is set when SWB output current consumption goes above the threshold setting in Table 126, Register 0x1E [7:0].
- NOTE 5: This register is applicable regardless of the setting in Table 173, Register 0x4F [0].
- NOTE 6: This register is set when SWC output current consumption goes above the threshold setting in Table 127, Register 0x1F [7:0].

## R0A (0x0A) — SWA_OUTPUT_OVER_VOLTAGE_STATUS, SWB_OUTPUT_OVER_VOLTAGE_STATUS, SWC_OUTPUT_OVER_VOLTAGE_STATUS, PEC_ERROR_STATUS, PARITY_ERROR_STATUS, IBI_AND_GLOBAL_STATUS

Region: Host Region | Source: JESD301-6 Table 106, p.129

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | SWA_OUTPUT_OVER_VOLTAGE_STATUS | RO | 0 |
| 6 | RESERVED | RV | 0 |
| 5 | SWB_OUTPUT_OVER_VOLTAGE_STATUS | RO | 0 |
| 4 | SWC_OUTPUT_OVER_VOLTAGE_STATUS | RO | 0 |
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

### [6] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [5] SWB_OUTPUT_OVER_VOLTAGE_STATUS

- Description: Switch Node B Output Over Voltage Status[2],[3]
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

- NOTE 1: This register is set when SWA output voltage goes above the threshold setting in Table 130, Register 0x22, [5:4].
- NOTE 2: This register is set when SWB output voltage goes above the threshold setting in Table 134, Register 0x26, [5:4].
- NOTE 3: Only applicable if Table 173, Register 0x4F [0] = ‘0’.
- NOTE 4: This register is set when SWC output voltage goes above the threshold setting in Table 136, Register 0x28, [5:4]
- NOTE 5: Applicable in I3C Basic Mode Only and if enabled in register Table 148, Register 0x34 [7].
- NOTE 6: This register is updated when PMIC device goes through bus reset as described in Section 6.18.13.
- NOTE 7: Applicable in I3C Basic Mode and if enabled in register Table 148, Register 0x34 [5]. It is also applicable in I2C mode for supported CCCs.
- NOTE 8: This register can be used as Global Status in addition to IBI status. When IBI function is enabled, this register is automatically cleared when PMIC transmits IBI payload; however individual status registers still requires an explicit clear command from host.

## R0B (0x0B) — SWA_OUTPUT_CURRENT_LIMITER_WARNING_STATUS, SWB_OUTPUT_CURRENT_LIMITER_WARNING_STATUS, SWC_OUTPUT_CURRENT_LIMITER_WARNING_STATUS, SWA_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS, SWB_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS, SWC_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

Region: Host Region | Source: JESD301-6 Table 107, p.130

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | SWA_OUTPUT_CURRENT_LIMITER_WARNING_STATUS | RO | 0 |
| 6 | RESERVED | RV | 0 |
| 5 | SWB_OUTPUT_CURRENT_LIMITER_WARNING_STATUS | RO | 0 |
| 4 | SWC_OUTPUT_CURRENT_LIMITER_WARNING_STATUS | RO | 0 |
| 3 | SWA_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS | RO | 0 |
| 2 | RESERVED | RV | 0 |
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

### [6] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [5] SWB_OUTPUT_CURRENT_LIMITER_WARNING_STATUS

- Description: Switch Node B Output Current Limiter Warning Status[2],[3]
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

### [2] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [1] SWB_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

- Description: Switch Node B Output Under Voltage Lockout Status[6],[7]
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

- NOTE 1: This register is set when SWA output valley current goes above the threshold setting in Table 128, Register 0x20 [7:6].
- NOTE 2: This register is set when SWB output valley current goes above the threshold setting in Table 128, Register 0x20 [3:2].
- NOTE 3: This register is applicable regardless of the setting in Table 173, Register 0x4F [0].
- NOTE 4: This register is set when SWC output valley current goes above the threshold setting in Table 128, Register 0x20 [1:0].
- NOTE 5: This register is set when SWA output voltage goes below the threshold setting in Table 130, Register 0x22, [3:2].
- NOTE 6: This register is set when SWB output voltage goes below the threshold setting in Table 134, Register 0x26, [3:2].
- NOTE 7: Only applicable if Table 173, Register 0x4F [0] = ‘0’.
- NOTE 8: This register is set when SWC output voltage goes below the threshold setting in Table 136, Register 0x28, [3:2].

## R0C (0x0C) — SWA_OUTPUT_CURRENT_POWER_MEASUREMENT

Region: Host Region | Source: JESD301-6 Table 108, p.131

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SWA_OUTPUT_CURRENT_POWER_MEASUREMENT | RO | 0 |

### [7:0] SWA_OUTPUT_CURRENT_POWER_MEASUREMENT

- Attribute: RO — Read Only (writes have no effect)
- Default: 0
- Source correction: Values print as 'X or Y' with footnotes naming the R32[1:0] setting for each alternative; split into one value table per R32[1:0] setting.

**When: If Table 122, Register 0x1A[1] = ‘0’ — Switch Node A Output Current or — Output Power[2] Measurement[3] and If Table 146, Register 0x32 [1:0] = ‘00’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Un-defined |
| 00000001 | 0x01 | 125 mA/mW |
| 00000010 | 0x02 | 250 mA/mW |
| 00000011 | 0x03 | 375 mA/mW |
| 00000100 | 0x04 | 500 mA/mW |
| ... | ... | ... |
| 11111111 | 0xFF | ≥ 31.875 A/W |

**When: If Table 122, Register 0x1A[1] = ‘0’ — Switch Node A Output Current or — Output Power[2] Measurement[3] and If Table 146, Register 0x32 [1:0] = ‘01’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Un-defined |
| 00000001 | 0x01 | 31.25 mA/mW |
| 00000010 | 0x02 | 62.5 mA/mW |
| 00000011 | 0x03 | 93.75 mA/mW |
| 00000100 | 0x04 | 125 mA/mW |
| ... | ... | ... |
| 11111111 | 0xFF | 7.968 A/W |

**When: If Table 122, Register 0x1A[1] = ‘1’ — Sum of SWA, SWB and SWC Output Power[6]**

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
- NOTE 2: If Table 123, Register 0x1B [6] = ‘0’, the PMIC reports current measurement. If Table 123, Register 0x1B [6] = ‘1’, the PMIC reports power measurement.
- NOTE 3: If Table 173, Register 0x4F [0] = ‘1’, host adds the current or power reported in Table 108, Register 0x0C [7:0] and Table 110, Register 0x0E [7:0] for total current or power consumption.
- NOTE 4: If Table 146, Register 0x32 [1:0] = ‘00’.
- NOTE 5: If Table 146, Register 0x32 [1:0] = ‘01’.
- NOTE 6: Register Table 123, Register 0x1B [6] must be configured as ‘1’ and Table 146, Register 0x32 [1:0] must be configured as ‘00’.

## R0D (0x0D) — SERIAL_NUMBER_BYTE_4

Region: Host Region | Source: JESD301-6 Table 109, p.131

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SERIAL_NUMBER_BYTE_4 | ROE | 0 |

### [7:0] SERIAL_NUMBER_BYTE_4

- Description: Byte 4 of the unique 40-bit serial number stored in {[R00:R03],R0D} Serial Number is vendor-specific
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: 0
- Values: no per-value encoding is listed in the spec for this field.

## R0E (0x0E) — SWB_OUTPUT_CURRENT_POWER_MEASUREMENT

Region: Host Region | Source: JESD301-6 Table 110, p.132

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SWB_OUTPUT_CURRENT_POWER_MEASUREMENT | RO | 0 |

### [7:0] SWB_OUTPUT_CURRENT_POWER_MEASUREMENT

- Description: Switch Node B Output Current or Output Power[2] Measurement[3]
- Attribute: RO — Read Only (writes have no effect)
- Default: 0
- Source correction: Spec lists code 000000 for 'Un-defined'; corrected to 00000000. 6-digit code in the source table for an 8-bit field; same entry is 0000 0000 in R0C/R0D.
- Source correction: Values print as 'X or Y' with footnotes naming the R32[1:0] setting for each alternative; split into one value table per R32[1:0] setting.

**When: If Table 146, Register 0x32 [1:0] = ‘00’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Un-defined |
| 00000001 | 0x01 | 125 mA/mW |
| 00000010 | 0x02 | 250 mA/mW |
| 00000011 | 0x03 | 375 mA/mW |
| 00000100 | 0x04 | 500 mA/mW |
| ... | ... | ... |
| 11111111 | 0xFF | ≥ 31.875 A/W |

**When: If Table 146, Register 0x32 [1:0] = ‘01’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Un-defined |
| 00000001 | 0x01 | 31.25 mA/mW |
| 00000010 | 0x02 | 62.5 mA/mW |
| 00000011 | 0x03 | 93.75 mA/mW |
| 00000100 | 0x04 | 125 mA/mW |
| ... | ... | ... |
| 11111111 | 0xFF | 7.968 A/W |

**Notes**

- NOTE 1: The PMIC reports current or power measurement as long as there is no output over voltage or output under voltage lockout event that triggers the VR Disable command. If PMIC triggers VR Disable command, PMIC does not report current or power measurement and register content may have stale data. For all other events that causes PMIC’s power good status as Not Good, the PMIC continues to provide current or power measurement.
- NOTE 2: If Table 123, Register 0x1B [6] = ‘0’, the PMIC reports current measurement. If Table 123, Register 0x1B [6] = ‘1’, the PMIC reports power measurement.
- NOTE 3: If Table 173, Register 0x4F [0] = ‘1’, host adds the current or power reported in Table 108, Register 0x0C [7:0] and Table 110, Register 0x0E [7:0] for total current or power consumption.
- NOTE 4: If Table 146, Register 0x32 [1:0] = ‘00’.
- NOTE 5: If Table 146, Register 0x32 [1:0] = ‘01’.

## R0F (0x0F) — SWC_OUTPUT_CURRENT_POWER_MEASUREMENT

Region: Host Region | Source: JESD301-6 Table 111, p.132

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SWC_OUTPUT_CURRENT_POWER_MEASUREMENT | RO | 0 |

### [7:0] SWC_OUTPUT_CURRENT_POWER_MEASUREMENT

- Description: Switch Node C Output Current or Output Power[2] Measurement
- Attribute: RO — Read Only (writes have no effect)
- Default: 0
- Source correction: Values print as 'X or Y' with footnotes naming the R32[1:0] setting for each alternative; split into one value table per R32[1:0] setting.

**When: If Table 146, Register 0x32 [1:0] = ‘00’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000001 | 0x01 | 125 mA/mW |
| 00000010 | 0x02 | 250 mA/mW |
| 00000011 | 0x03 | 375 mA/mW |
| 00000100 | 0x04 | 500 mA/mW |
| ... | ... | ... |
| 11111111 | 0xFF | ≥ 31.875 A/W |

**When: If Table 146, Register 0x32 [1:0] = ‘01’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000001 | 0x01 | 31.25 mA/mW |
| 00000010 | 0x02 | 62.5 mA/mW |
| 00000011 | 0x03 | 93.75 mA/mW |
| 00000100 | 0x04 | 125 mA/mW |
| ... | ... | ... |
| 11111111 | 0xFF | 7.968 A/W |

**Notes**

- NOTE 1: The PMIC reports current or power measurement as long as there is no output over voltage or output under voltage lockout event that triggers the VR Disable command. If PMIC triggers VR Disable command, PMIC does not report current or power measurement and register content may have stale data. For all other events that causes PMIC’s power good status as Not Good, the PMIC continues to provide current or power measurement.
- NOTE 2: If Table 123, Register 0x1B [6] = ‘0’, the PMIC reports current measurement. If Table 123, Register 0x1B [6] = ‘1’, the PMIC reports power measurement.
- NOTE 3: If Table 146, Register 0x32 [1:0] = ‘00’.
- NOTE 4: If Table 146, Register 0x32 [1:0] = ‘01’.

## R10 (0x10) — CLEAR_SWA_OUTPUT_POWER_GOOD_STATUS, CLEAR_SWB_OUTPUT_POWER_GOOD_STATUS, CLEAR_SWC_OUTPUT_POWER_GOOD_STATUS, CLEAR_VIN_BULK_INPUT_OVER_VOLTAGE_STATUS

Region: Host Region | Source: JESD301-6 Table 112, p.133

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | RESERVED | RV | 0 |
| 5 | CLEAR_SWA_OUTPUT_POWER_GOOD_STATUS | 1O | 0 |
| 4 | RESERVED | RV | 0 |
| 3 | CLEAR_SWB_OUTPUT_POWER_GOOD_STATUS | 1O | 0 |
| 2 | CLEAR_SWC_OUTPUT_POWER_GOOD_STATUS | 1O | 0 |
| 1 | RESERVED | RV | 0 |
| 0 | CLEAR_VIN_BULK_INPUT_OVER_VOLTAGE_STATUS | 1O | 0 |

### [7:6] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [5] CLEAR_SWA_OUTPUT_POWER_GOOD_STATUS

- Description: Clear SWA Output Power Good Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 104, Register 0x08 [5][2] |

### [4] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [3] CLEAR_SWB_OUTPUT_POWER_GOOD_STATUS

- Description: Clear SWB Output Power Good Status.[3]
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 104, Register 0x08 [3][2] |

### [2] CLEAR_SWC_OUTPUT_POWER_GOOD_STATUS

- Description: Clear SWC Output Power Good Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 104, Register 0x08 [2][2] |

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
| 1 | Clear Register Table 104, Register 0x08 [0][2] |

**Notes**

- NOTE 1: Table 112, Register 0x10 [5,3:2,0] are self clearing bits.
- NOTE 2: See Table 31 and Table 32 for GSI_n and POWER_GOOD output signal status change.
- NOTE 3: Only applicable if Table 173, Register 0x4F [0] = ‘0’.

## R11 (0x11) — CLEAR_PMIC_HIGH_TEMP_WARNING_STATUS, CLEAR_VOUT_1.8V_OUTPUT_POWER_GOOD_STATUS, CLEAR_SWA_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS, CLEAR_SWB_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS, CLEAR_SWC_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS

Region: Host Region | Source: JESD301-6 Table 113, p.134

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | CLEAR_PMIC_HIGH_TEMP_WARNING_STATUS | 1O | 0 |
| 6 | RESERVED | RV | 0 |
| 5 | CLEAR_VOUT_1.8V_OUTPUT_POWER_GOOD_STATUS | 1O | 0 |
| 4 | RESERVED | RV | 0 |
| 3 | CLEAR_SWA_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS | 1O | 0 |
| 2 | RESERVED | RV | 0 |
| 1 | CLEAR_SWB_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS | 1O | 0 |
| 0 | CLEAR_SWC_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS | 1O | 0 |

### [7] CLEAR_PMIC_HIGH_TEMP_WARNING_STATUS

- Description: Clear PMIC High Temperature Warning Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 105, Register 0x09 [7][2] |

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
| 1 | Clear Register Table 105, Register 0x09 [5][2] |

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
| 1 | Clear Register Table 105, Register 0x09 [3][2] |

### [2] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [1] CLEAR_SWB_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS

- Description: Clear Switch Node B High Output Current Consumption Warning Status.[3]
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 105, Register 0x09 [1][2] |

### [0] CLEAR_SWC_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS

- Description: Clear Switch Node C High Output Current Consumption Warning Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 105, Register 0x09 [0][2] |

**Notes**

- NOTE 1: Table 113, Register 0x11 [7,5,3,1:0] are self clearing bits.
- NOTE 2: See Table 31 and Table 32 for GSI_n and POWER_GOOD output signal status change.
- NOTE 3: This register is applicable regardless of the setting in Table 173, Register 0x4F [0].

## R12 (0x12) — CLEAR_SWA_OUTPUT_OVER_VOLTAGE_STATUS, CLEAR_SWB_OUTPUT_OVER_VOLTAGE_STATUS, CLEAR_SWC_OUTPUT_OVER_VOLTAGE_STATUS, CLEAR_PER_ERROR_STATUS, CLEAR_PARITY_ERROR_STATUS

Region: Host Region | Source: JESD301-6 Table 114, p.135

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | CLEAR_SWA_OUTPUT_OVER_VOLTAGE_STATUS | 1O | 0 |
| 6 | RESERVED | RV | 0 |
| 5 | CLEAR_SWB_OUTPUT_OVER_VOLTAGE_STATUS | 1O | 0 |
| 4 | CLEAR_SWC_OUTPUT_OVER_VOLTAGE_STATUS | 1O | 0 |
| 3 | CLEAR_PER_ERROR_STATUS | 1O | 0 |
| 2 | CLEAR_PARITY_ERROR_STATUS | 1O | 0 |
| 1:0 | RESERVED | RV | 0 |

### [7] CLEAR_SWA_OUTPUT_OVER_VOLTAGE_STATUS

- Description: Clear Switch Node A Output Over Voltage Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 106, Register 0x0A [7][2] |

### [6] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [5] CLEAR_SWB_OUTPUT_OVER_VOLTAGE_STATUS

- Description: Clear Switch Node B Output Over Voltage Status.[3]
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 106, Register 0x0A [5][2] |

### [4] CLEAR_SWC_OUTPUT_OVER_VOLTAGE_STATUS

- Description: Clear Switch Node C Output Over Voltage Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 106, Register 0x0A [4][2] |

### [3] CLEAR_PER_ERROR_STATUS

- Description: Clear PEC Error Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 106, Register 0x0A [3] |

### [2] CLEAR_PARITY_ERROR_STATUS

- Description: Clear Parity Error Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 106, Register 0x0A [2] |

### [1:0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

**Notes**

- NOTE 1: Table 114, Register 0x12 [7,5:2] are self clearing bits.
- NOTE 2: See Table 31 and Table 32 for GSI_n and POWER_GOOD output signal status change.
- NOTE 3: Only applicable if Table 173, Register 0x4F [0] = ‘0’.

## R13 (0x13) — CLEAR_SWA_OUTPUT_CURRENT_LIMITER_WARNING_STATUS, CLEAR_SWB_OUTPUT_CURRENT_LIMITER_WARNING_STATUS, CLEAR_SWC_OUTPUT_CURRENT_LIMITER_WARNING_STATUS, CLEAR_SWA_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS, CLEAR_SWB_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS, CLEAR_SWC_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

Region: Host Region | Source: JESD301-6 Table 115, p.136

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | CLEAR_SWA_OUTPUT_CURRENT_LIMITER_WARNING_STATUS | 1O | 0 |
| 6 | RESERVED | RV | 0 |
| 5 | CLEAR_SWB_OUTPUT_CURRENT_LIMITER_WARNING_STATUS | 1O | 0 |
| 4 | CLEAR_SWC_OUTPUT_CURRENT_LIMITER_WARNING_STATUS | 1O | 0 |
| 3 | CLEAR_SWA_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS | 1O | 0 |
| 2 | RESERVED | RV | 0 |
| 1 | CLEAR_SWB_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS | 1O | 0 |
| 0 | CLEAR_SWC_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS | 1O | 0 |

### [7] CLEAR_SWA_OUTPUT_CURRENT_LIMITER_WARNING_STATUS

- Description: Clear Switch Node A Output Current Limiter Warning Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 107, Register 0x0B [7][2] |

### [6] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [5] CLEAR_SWB_OUTPUT_CURRENT_LIMITER_WARNING_STATUS

- Description: Clear Switch Node B Output Current Limiter Warning Status.[3]
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 107, Register 0x0B [5][2] |

### [4] CLEAR_SWC_OUTPUT_CURRENT_LIMITER_WARNING_STATUS

- Description: Clear Switch Node C Output Current Limiter Warning Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 107, Register 0x0B [4][2] |

### [3] CLEAR_SWA_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

- Description: Clear Switch Node A Output Under Voltage Lockout Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 107, Register 0x0B [3][2] |

### [2] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [1] CLEAR_SWB_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

- Description: Clear Switch Node B Output Under Voltage Lockout Status.[4]
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 107, Register 0x0B [1][2] |

### [0] CLEAR_SWC_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

- Description: Clear Switch Node C Output Under Voltage Lockout Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 107, Register 0x0B [0][2] |

**Notes**

- NOTE 1: Table 115, Register 0x13 [7,5:3,1:0] are self clearing bits.
- NOTE 2: See Table 31 and Table 32 for GSI_n and POWER_GOOD output signal status change.
- NOTE 3: This register is applicable regardless of the setting in Table 173, Register 0x4F [0].
- NOTE 4: Only applicable if Table 173, Register 0x4F [0] = ‘0’.

## R14 (0x14) — CLEAR_VIN_BULK_UNDER_VOLTAGE_LOCKOUT_STATUS, CLEAR_VOUT_1.0V_OUTPUT_POWER_GOOD_STATUS, GLOBAL_CLEAR_STATUS

Region: Host Region | Source: JESD301-6 Table 116, p.137

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
| 1 | Clear Register Table 147, Register 0x33 [3] |

### [2] CLEAR_VOUT_1.0V_OUTPUT_POWER_GOOD_STATUS

- Description: Clear VOUT_1.0V Output Power Good Status.
- Attribute: 1O — Write '1' Only (write 1 to set/clear; writing 0 has no effect)
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 1 | Clear Register Table 147, Register 0x33 [2][2] |

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

- NOTE 1: Table 116, Register 0x14 [2, 0] are self clearing bits.
- NOTE 2: All status bits in register Table 112, Register 0x10 [5,3:2,0], Table 113, Register 0x11 [7,5,3,1:0], Table 114, Reg- ister 0x12 [7,5:2], Table 115, Register 0x13 [7,5:3,1:0], and Table 116, Register 0x14 [2].
- NOTE 3: See Table 31 and Table 32 for GSI_n and POWER_GOOD output signal status change.

## R15 (0x15) — MASK_SWA_OUTPUT_POWER_GOOD_STATUS, MASK_SWB_OUTPUT_POWER_GOOD_STATUS, MASK_SWC_OUTPUT_POWER_GOOD_STATUS, MASK_VIN_BULK_INPUT_OVER_VOLTAGE_STATUS

Region: Host Region | Source: JESD301-6 Table 117, p.137

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | RESERVED | RV | 0 |
| 5 | MASK_SWA_OUTPUT_POWER_GOOD_STATUS | RW | 1 |
| 4 | RESERVED | RV | 0 |
| 3 | MASK_SWB_OUTPUT_POWER_GOOD_STATUS | RW | 1 |
| 2 | MASK_SWC_OUTPUT_POWER_GOOD_STATUS | RW | 1 |
| 1 | RESERVED | RV | 0 |
| 0 | MASK_VIN_BULK_INPUT_OVER_VOLTAGE_STATUS | RW | 0 |

### [7:6] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [5] MASK_SWA_OUTPUT_POWER_GOOD_STATUS

- Description: Mask SWA Output Power Good Status Event. 1
- Attribute: RW — Read/Write
- Default: 1 → Mask SWA Output Power Good Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWA Output Power Good Status Event |
| 1 | Mask SWA Output Power Good Status Event |

### [4] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [3] MASK_SWB_OUTPUT_POWER_GOOD_STATUS

- Description: Mask SWB Output Power Good Status Event.[1],[2]
- Attribute: RW — Read/Write
- Default: 1 → Mask SWB Output Power Good Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask SWB Output Power Good Status Event |
| 1 | Mask SWB Output Power Good Status Event |

### [2] MASK_SWC_OUTPUT_POWER_GOOD_STATUS

- Description: Mask SWC Output Power Good Status Event.[1]
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

- Description: Mask VIN_Bulk Input Supply Over Voltage Status Event.[3]
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask VIN_Bulk Input Supply Over Voltage Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask VIN_Bulk Input Supply Over Voltage Status Event |
| 1 | Mask VIN_Bulk Input Supply Over Voltage Status Event |

**Notes**

- NOTE 1: Not assert GSI_n or assert PWR_GOOD output signal.
- NOTE 2: Only applicable if Table 173, Register 0x4F [0] = ‘0’.
- NOTE 3: Not assert GSI_n output signal.

## R16 (0x16) — MASK_PMIC_HIGH_TEMP_WARNING_STATUS, MASK_VOUT_1.8V_OUTPUT_POWER_GOOD_STATUS, MASK_SWA_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS, MASK_SWB_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS, MASK_SWC_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS

Region: Host Region | Source: JESD301-6 Table 118, p.138

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | MASK_PMIC_HIGH_TEMP_WARNING_STATUS | RW | 0 |
| 6 | RESERVED | RV | 0 |
| 5 | MASK_VOUT_1.8V_OUTPUT_POWER_GOOD_STATUS | RW | 1 |
| 4 | RESERVED | RV | 0 |
| 3 | MASK_SWA_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS | RW | 0 |
| 2 | RESERVED | RV | 0 |
| 1 | MASK_SWB_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS | RW | 0 |
| 0 | MASK_SWC_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS | RW | 0 |

### [7] MASK_PMIC_HIGH_TEMP_WARNING_STATUS

- Description: Mask PMIC High Temperature Warning Status Event.
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

- Description: Mask Switch Node A High Output Current Consumption Warning Status Event.
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask Switch Node A Output Current Consumption Warning Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask Switch Node A Output Current Consumption Warning Status Event |
| 1 | Mask Switch Node A Output Current Consumption Warning Status Event[1] |

### [2] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [1] MASK_SWB_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS

- Description: Mask Switch Node B High Output Current Consumption Warning Status Event. 3
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask Switch Node B Output Current Consumption Warning Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask Switch Node B Output Current Consumption Warning Status Event |
| 1 | Mask Switch Node B Output Current Consumption Warning Status Event[1] |

### [0] MASK_SWC_HIGH_OUTPUT_CURRENT_CONSUMPTION_WARNING_STATUS

- Description: Mask Switch Node C High Output Current Consumption Warning Status Event.
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask Switch Node C Output Current Consumption Warning Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask Switch Node C Output Current Consumption Warning Status Event |
| 1 | Mask Switch Node C Output Current Consumption Warning Status Event[1] |

**Notes**

- NOTE 1: Not assert GSI_n output signal.
- NOTE 2: Not assert GSI_n or assert PWR_GOOD output signal.
- NOTE 3: This register is applicable regardless of the setting in Table 173, Register 0x4F [0].

## R17 (0x17) — MASK_SWA_OUTPUT_OVER_VOLTAGE_STATUS, MASK_SWB_OUTPUT_OVER_VOLTAGE_STATUS, MASK_SWC_OUTPUT_OVER_VOLTAGE_STATUS, MASK_PEC_ERROR_STATUS, MASK_PARITY_ERROR_STATUS

Region: Host Region | Source: JESD301-6 Table 119, p.139

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | MASK_SWA_OUTPUT_OVER_VOLTAGE_STATUS | RW | 0 |
| 6 | RESERVED | RV | 0 |
| 5 | MASK_SWB_OUTPUT_OVER_VOLTAGE_STATUS | RW | 0 |
| 4 | MASK_SWC_OUTPUT_OVER_VOLTAGE_STATUS | RW | 0 |
| 3 | MASK_PEC_ERROR_STATUS | RW | 0 |
| 2 | MASK_PARITY_ERROR_STATUS | RW | 0 |
| 1:0 | RESERVED | RV | 0 |

### [7] MASK_SWA_OUTPUT_OVER_VOLTAGE_STATUS

- Description: Mask Switch Node A Output Over Voltage Status Event.
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask Switch Node A Output Over Voltage Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask Switch Node A Output Over Voltage Status Event |
| 1 | Mask Switch Node A Output Over Voltage Status Event[1] |

### [6] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [5] MASK_SWB_OUTPUT_OVER_VOLTAGE_STATUS

- Description: Mask Switch Node B Output Over Voltage Status Event.[2]
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask Switch Node B Output Over Voltage Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask Switch Node B Output Over Voltage Status Event |
| 1 | Mask Switch Node B Output Over Voltage Status Event[1] |

### [4] MASK_SWC_OUTPUT_OVER_VOLTAGE_STATUS

- Description: Mask Switch Node C Output Over Voltage Status Event.
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask Switch Node C Output Over Voltage Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask Switch Node C Output Over Voltage Status Event |
| 1 | Mask Switch Node C Output Over Voltage Status Event[1] |

### [3] MASK_PEC_ERROR_STATUS

- Description: Mask PEC Error Event for GSI_n output Only[3]
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask PEC Error Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask PEC Error Status Event |
| 1 | Mask PEC Error Status |

### [2] MASK_PARITY_ERROR_STATUS

- Description: Mask Parity Error Event for GSI_n output Only[4]
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
- NOTE 2: Only applicable if Table 173, Register 0x4F [0] = ‘0’.
- NOTE 3: Only applicable when PMIC is in I3C Basic Mode. This Mask register only masks the GSI_n output. Does not apply to IBI.
- NOTE 4: Applicable when PMIC is in I3C Basic Mode or for supported CCC in I2C mode. This Mask register only masks the GSI_n output. Does not apply to IBI.

## R18 (0x18) — MASK_SWA_OUTPUT_CURRENT_LIMITER_WARNING_STATUS, MASK_SWB_OUTPUT_CURRENT_LIMITER_WARNING_STATUS, MASK_SWC_OUTPUT_CURRENT_LIMITER_WARNING_STATUS, MASK_SWA_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS, MASK_SWB_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS, MASK_SWC_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

Region: Host Region | Source: JESD301-6 Table 120, p.140

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | MASK_SWA_OUTPUT_CURRENT_LIMITER_WARNING_STATUS | RW | 0 |
| 6 | RESERVED | RV | 0 |
| 5 | MASK_SWB_OUTPUT_CURRENT_LIMITER_WARNING_STATUS | RW | 0 |
| 4 | MASK_SWC_OUTPUT_CURRENT_LIMITER_WARNING_STATUS | RW | 0 |
| 3 | MASK_SWA_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS | RW | 0 |
| 2 | RESERVED | RV | 0 |
| 1 | MASK_SWB_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS | RW | 0 |
| 0 | MASK_SWC_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS | RW | 0 |

### [7] MASK_SWA_OUTPUT_CURRENT_LIMITER_WARNING_STATUS

- Description: Mask Switch Node A Output Current Limiter Warning Status Event.
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask Switch Node A Output Current Limiter Warning Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask Switch Node A Output Current Limiter Warning Status Event |
| 1 | Mask Switch Node A Output Current Limiter Warning Status Event[1] |

### [6] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [5] MASK_SWB_OUTPUT_CURRENT_LIMITER_WARNING_STATUS

- Description: Mask Switch Node B Output Current Limiter Warning Status Event.[2]
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask Switch Node B Output Current Limiter Warning Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask Switch Node B Output Current Limiter Warning Status Event |
| 1 | Mask Switch Node B Output Current Limiter Warning Status Event[1] |

### [4] MASK_SWC_OUTPUT_CURRENT_LIMITER_WARNING_STATUS

- Description: Mask Switch Node C Output Current Limiter Warning Status Event.
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask Switch Node C Output Current Limiter Warning Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask Switch Node C Output Current Limiter Warning Status Event |
| 1 | Mask Switch Node C Output Current Limiter Warning Status Event[1] |

### [3] MASK_SWA_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

- Description: Mask Switch Node A Output Under Voltage Lockout Status Event.
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask Switch Node A Output Under Voltage Lockout Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask Switch Node A Output Under Voltage Lockout Status Event |
| 1 | Mask Switch Node A Output Under Voltage Lockout Status Event[1] |

### [2] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [1] MASK_SWB_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

- Description: Mask Switch Node B Output Under Voltage Lockout Status Event.[3]
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask Switch Node B Output Under Voltage Lockout Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask Switch Node B Output Under Voltage Lockout Status Event |
| 1 | Mask Switch Node B Output Under Voltage Lockout Status Event[1] |

### [0] MASK_SWC_OUTPUT_UNDER_VOLTAGE_LOCKOUT_STATUS

- Description: Mask Switch Node C Output Under Voltage Lockout Status Event.
- Attribute: RW — Read/Write
- Default: 0 → Do Not Mask Switch Node C Output Under Voltage Lockout Status Event

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask Switch Node C Output Under Voltage Lockout Status Event |
| 1 | Mask Switch Node C Output Under Voltage Lockout Status Event[1] |

**Notes**

- NOTE 1: Not assert GSI_n output signal.
- NOTE 2: This register is applicable regardless of the setting in Table 173, Register 0x4F [0].
- NOTE 3: Only applicable if Table 173, Register 0x4F [0] = ‘0’.

## R19 (0x19) — MASK_VIN_BULK_UNDER_VOLTAGE_LOCKOUT_STATUS, MASK_VOUT_1.0V_OUTPUT_POWER_GOOD_STATUS

Region: Host Region | Source: JESD301-6 Table 121, p.141

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

- Description: Mask VOUT_1.0V Output Power Good Status Event.
- Attribute: RW — Read/Write
- Default: 1 → Mask 1.0V Output Power Good Status Event[2]

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Mask 1.0V Output Power Good Status Event |
| 1 | Mask 1.0V Output Power Good Status Event[2] |

### [1:0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

**Notes**

- NOTE 1: Not assert GSI_n output signal.
- NOTE 2: Not assert GSI_n or POWER_GOOD output signal.

## R1A (0x1A) — QUIESCENT_STATE_EN, VOUT_1.8V_POWER_GOOD_THRESHOLD_VOLTAGE, OUTPUT_POWER_SELECT, VOUT_1.0V_POWER_GOOD_THRESHOLD_VOLTAGE

Region: Host Region | Source: JESD301-6 Table 122, p.142

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:5 | RESERVED | RV | 0 |
| 4 | QUIESCENT_STATE_EN | RW | 0 |
| 3 | RESERVED | RW | 0 |
| 2 | VOUT_1.8V_POWER_GOOD_THRESHOLD_VOLTAGE | RW | 0 |
| 1 | OUTPUT_POWER_SELECT | RW | 0 |
| 0 | VOUT_1.0V_POWER_GOOD_THRESHOLD_VOLTAGE | RW | 0 |

### [7:5] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [4] QUIESCENT_STATE_EN

- Description: PMIC Quiescent State Entry Enable[1]
- Attribute: RW — Read/Write
- Default: 0 → Disable

| Code (bin) | Meaning |
|---|---|
| 0 | Disable |
| 1 | Enable[2],[3] |

### [3] RESERVED

- Description: Reserved
- Attribute: RW — Read/Write
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

- Description: Switch Regulator Output Power Select[4]
- Attribute: RW — Read/Write
- Default: 0 → Report individual power for each rail in R0C, R0E and R0F

| Code (bin) | Meaning |
|---|---|
| 0 | Report individual power for each rail in R0C, R0E and R0F |
| 1 | Report total power of each rail in R0C5 |

### [0] VOUT_1.0V_POWER_GOOD_THRESHOLD_VOLTAGE

- Description: VOUT 1.0V LDO Output Threshold Voltage for Power Good Status
- Attribute: RW — Read/Write
- Default: 0 → -10% from the setting in Table 139, Register 0x2B, [2:1]

| Code (bin) | Meaning |
|---|---|
| 0 | -10% from the setting in Table 139, Register 0x2B, [2:1] |
| 1 | -15% from the setting in Table 139, Register 0x2B, [2:1] |

**Notes**

- NOTE 1: This bit must be configured before issuing VR Enable command.
- NOTE 2: VR Disable command (VR_EN pin transition to low or Table 146, Register 0x32 [7] = ‘0’ (in programmable mode only)) puts PMIC in Quiescent state.
- NOTE 3: Simultaneous usage of programmable mode (i.e., Table 143, Register 0x2F [2] = ‘1’), PWR_GOOD as IO (i.e., Table 146, Register 0x32 [5] = ‘1’) and P1 State Enable (i.e., Table 122, Register 0x1A [4] = ‘1’) is considered an illegal configuration when VR_EN pin is intended to be used; otherwise it is a valid configuration if VR_EN command is used on I2C/I3C Basic bus.
- NOTE 4: This register is only applicable if Table 123, Register 0x1B [6] = ‘1’.
- NOTE 5: Host should only read Table 108, Register 0x0C [7:0] for total power. The register contents of Table 110, Register 0x0E and Table 111, Register 0x0F may not be valid.

## R1B (0x1B) — VIN_BULK_OVER_VOLTAGE_THRESHOLD, CURRENT_OR_POWER_METER_SELECT, GLOBAL_PWR_GOOD_PIN_STATUS_MASK, GSI_N_PIN_ENABLE, PMIC_HIGH_TEMPERATURE_WARNING_THRESHOLD

Region: Host Region | Source: JESD301-6 Table 123, p.143

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | VIN_BULK_OVER_VOLTAGE_THRESHOLD | RW | 0 |
| 6 | CURRENT_OR_POWER_METER_SELECT | RW | 0 |
| 5 | RESERVED | RV | 0 |
| 4 | GLOBAL_PWR_GOOD_PIN_STATUS_MASK | RW | 0 |
| 3 | GSI_N_PIN_ENABLE | RW | 0 |
| 2:0 | PMIC_HIGH_TEMPERATURE_WARNING_THRESHOLD | RW | 101 |

### [7] VIN_BULK_OVER_VOLTAGE_THRESHOLD

- Description: VIN_Bulk Input Over Voltage Threshold Setting For GSI_n Assertion
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
| 1 | Report Power Measurements in registers[1] |

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

- NOTE 1: Table 108, Register 0x0C [7:0], Table 110, Register 0x0E [7:0], Table 111, Register 0x0F[7:0].
- NOTE 2: Mask POWER_GOOD output signal for all appropriate register bits in Table 117, Register 0x15 [5,3:2,0], Table 118, Register 0x16 [7,5,3,1:0], Table 119, Register 0x17 [7,5:4], Table 120, Register 0x18 [7,5:3,1:0] and Table 121, Register 0x19 [3:2]. Mask Register Control Table 143, Register 0x2F [1:0] still applies when Global PWR_GOOD output Mask register is set to ‘1’.
- NOTE 3: This register can be used as Global Mask Function for GSI_n pin. If disabled, this masks GSI_n output signal for all register bits in Table 117, Register 0x15 [5,3,2:0], Table 118, Register 0x16 [7,5,3,1:0], Table 119, Register 0x17 [7,5:4], Table 120, Register 0x18 [7,5:3,1:0] and Table 121, Register 0x19 [3:2].
- NOTE 4: The tolerance of the temperature warning threshold is + 5 °C from the selected setting.

## R1C (0x1C) — SWA_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRE

Region: Host Region | Source: JESD301-6 Table 124, p.144

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SWA_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRE | RW | 00110000 |

### [7:0] SWA_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRE

- Description: SHOLD Switch Node A Output High Current Consumption Warning Threshold[1]
- Attribute: RW — Read/Write
- Default: 00110000 → 1500 mA (if If Table 146, Register 0x32 [1:0] = ‘01’); 6.0 A (Default) (if If Table 146, Register 0x32 [1:0] = ‘00’)

**When: If Table 146, Register 0x32 [1:0] = ‘01’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | 31.25 mA |
| 00000010 | 0x02 | 62.5 mA |
| 00000011 | 0x03 | 93.75 mA |
| 00000100 | 0x04 | 125 mA |
| ... | ... | ... |
| 11000000 | 0xC0 | 6.0 A |
| ... | ... | ... |
| 11111111 | 0xFF | 7.968 A |

**When: If Table 146, Register 0x32 [1:0] = ‘00’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | 0.125 A |
| 00000010 | 0x02 | 0.250 A |
| ... | ... | ... |
| 00110000 | 0x30 | 6.0 A (Default) |
| ... | ... | ... |
| 11111111 | 0xFF | 31.875 A |

**Notes**

- NOTE 1: The default value is set based on Table 146, Register 0x32 [1:0] = ‘00’

## R1D (0x1D) — Reserved

Region: Host Region | Source: JESD301-6 Table 125, p.144

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | RESERVED | RV | 0 |

### [7:0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

## R1E (0x1E) — SWB_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD

Region: Host Region | Source: JESD301-6 Table 126, p.145

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SWB_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD | RW | 00110000 |

### [7:0] SWB_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD

- Description: Switch Node B Output High Current Consumption Warning Threshold[12]
- Attribute: RW — Read/Write
- Default: 00110000 → 1500 mA (if If Table 146, Register 0x32 [1:0] = ‘01’); 6.0 A (Default) (if If Table 146, Register 0x32 [1:0] = ‘00’)

**When: If Table 146, Register 0x32 [1:0] = ‘01’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | 31.25 mA |
| 00000010 | 0x02 | 62.5 mA |
| 00000011 | 0x03 | 93.75 mA |
| 00000100 | 0x04 | 125 mA |
| ... | ... | ... |
| 11000000 | 0xC0 | 6.0 A |
| ... | ... | ... |
| 11111111 | 0xFF | 7.968 A |

**When: If Table 146, Register 0x32 [1:0] = ‘00’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | 0.125 A |
| 00000010 | 0x02 | 0.250 A |
| ... | ... | ... |
| 00110000 | 0x30 | 6.0 A (Default) |
| ... | ... | ... |
| 11111111 | 0xFF | 31.875 A |

**Notes**

- NOTE 1: This register is applicable regardless of the setting in Table 173, Register 0x4F [0]. For dual phase operation, this register should be configured identically as Table 124, Register 0x1C [7:0].
- NOTE 2: The default value is set based on Table 146, Register 0x32 [1:0] = ‘00’

## R1F (0x1F) — SWC_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD

Region: Host Region | Source: JESD301-6 Table 127, p.146

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | SWC_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD | RW | 00010000 |

### [7:0] SWC_OUTPUT_HIGH_CURRENT_CONSUMPTION_WARNING_THRESHOLD

- Description: Switch Node C Output High Current Consumption Warning Threshold[1]
- Attribute: RW — Read/Write
- Default: 00010000 → 500 mA (if If Table 146, Register 0x32 [1:0] = ‘01’); 2.0 A (Default) (if If Table 146, Register 0x32 [1:0] = ‘00’)

**When: If Table 146, Register 0x32 [1:0] = ‘01’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | 31.25 mA |
| 00000010 | 0x02 | 62.5 mA |
| 00000011 | 0x03 | 93.75 mA |
| 00000100 | 0x04 | 125 mA |
| ... | ... | ... |
| 01000000 | 0x40 | 2.0 A |
| ... | ... | ... |
| 11111111 | 0xFF | 7.968 A |

**When: If Table 146, Register 0x32 [1:0] = ‘00’**

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 00000000 | 0x00 | Undefined |
| 00000001 | 0x01 | 0.125 A |
| 00000010 | 0x02 | 0.250 A |
| ... | ... | ... |
| 00010000 | 0x10 | 2.0 A (Default) |
| ... | ... | ... |
| 11111111 | 0xFF | 31.875 A |

**Notes**

- NOTE 1: The default value is set based on Table 146, Register 0x32 [1:0] = ‘00’

## R20 (0x20) — SWA_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING, SWB_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING, SWC_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING

Title: Attrib | Region: Host Region | Source: JESD301-6 Table 128, p.147

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWA_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING | RW | 01 |
| 5:4 | RESERVED | RV | 0 |
| 3:2 | SWB_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING | RW | 01 |
| 1:0 | SWC_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING | RW | 0 |

### [7:6] SWA_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING

- Description: For COT Mode, Ivalley_limit:
- Attribute: RW — Read/Write
- Default: 01 → 5.5 A

| Code (bin) | Meaning |
|---|---|
| 00 | 4.5 A |
| 01 | 5.5 A |
| 10 | 6.5 A |
| 11 | Vendor-Specific |

### [5:4] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [3:2] SWB_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING

- Description: For COT Mode, Ivalley_limit[2]
- Attribute: RW — Read/Write
- Default: 01 → 5.5 A

| Code (bin) | Meaning |
|---|---|
| 00 | 4.5 A |
| 01 | 5.5 A |
| 10 | 6.5 A |
| 11 | Vendor-Specific |

### [1:0] SWC_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING

- Description: For COT Mode, Ivalley_limit:
- Attribute: RW — Read/Write
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 00 | 1.5 A |
| 01 | 2.0 A |
| 10 | Reserved |
| 11 | Vendor-Specific |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 174, Register 0x50.
- NOTE 2: This register is applicable regardless of the setting in Table 173, Register 0x4F[0]. For dual phase operation, this register should be configured identically as Table 128, Register 0x20 [7:6].

## R21 (0x21) — SWA_VOLTAGE_SETTING, SWA_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

Region: Host Region | Source: JESD301-6 Table 129, p.148

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:1 | SWA_VOLTAGE_SETTING | RW | 011 1100 |
| 0 | SWA_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING | RW | 0 |

### [7:1] SWA_VOLTAGE_SETTING

- Description: Switch Node A Output Regulator Voltage Setting[3],[4]
- Attribute: RW — Read/Write
- Default: 011 1100 → 1100 mV

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 0000000 | 0x00 | 800 mV |
| 0000001 | 0x01 | 805 mV |
| 0000010 | 0x02 | 810 mV |
| ... | ... | ... |
| 0111100 | 0x3C | 1100 mV |
| ... | ... | ... |
| 1111101 | 0x7D | 1425 mV |
| 1111110 | 0x7E | 1430 mV |
| 1111111 | 0x7F | 1435 mV |

### [0] SWA_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

- Description: Switch Node A Output Threshold Low Side Voltage For Power Good Status
- Attribute: RW — Read/Write
- Default: 0 → -5% from the setting in Table 129, Register 0x21, [7:1]

| Code (bin) | Meaning |
|---|---|
| 0 | -5% from the setting in Table 129, Register 0x21, [7:1] |
| 1 | -7.5% from the setting in Table 129, Register 0x21, [7:1] |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 163, Register 0x45.
- NOTE 2: If required, the host must update the settings in register Table 129, Register 0x21, [0], Table 130, Register 0x22, [7:2] and Table 128, Register 0x20 [7:6] first prior to updating the settings in the register Table 129, Register 0x21, [7:1].
- NOTE 3: PMIC guarantees efficiency spec and all electrical characteristics spec within a range of 1050 mV to 1160 mV.
- NOTE 4: After VR is enabled, the host may update this register to any new setting that it may desire. However to prevent false error trigger, the PMIC internally will increment the SWA output voltage setting by 5 mV at a time. The time it takes for PMIC to adjust the output voltage is 5 μs for each 5 mV increment. The host must wait sufficient time for PMIC to adjust to final value. As an example, if host adjusts the output voltage by 50 mV from the original value, the host must wait minimum of 50 μs before PMIC can guarantee the new output voltage. During this time, PMIC masks the PWR_GOOD output signal assertion to prevent any artificial error due to the crossing of the output voltage threshold setting. However, PMIC does assert PWR_GOOD output signal if there is any abnormal issues that triggers VR Disable command as described in Table 30. Further, PMIC does monitor PWR_GOOD input signal and executes power off config sequence registers if it is registered low when Table 146, Register 0x32 [5] = ‘1’.

## R22 (0x22) — SWA_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING, SWA_OVER_VOLTAGE_THRESHOLD_SETTING, SWA_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING, SWA_OUTPUT_SOFT_STOP_TIME

Region: Host Region | Source: JESD301-6 Table 130, p.149

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWA_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING | RW | 01 |
| 5:4 | SWA_OVER_VOLTAGE_THRESHOLD_SETTING | RW | 10 |
| 3:2 | SWA_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING | RW | 00 |
| 1:0 | SWA_OUTPUT_SOFT_STOP_TIME | RW | 11 |

### [7:6] SWA_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING

- Description: Switch Node A Output Threshold High Side Voltage For Power Good Status
- Attribute: RW — Read/Write
- Default: 01 → +7.5% from the setting in Table 129, Register 0x21, [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +5% from the setting in Table 129, Register 0x21, [7:1] |
| 01 | +7.5% from the setting in Table 129, Register 0x21, [7:1] |
| 10 | +10% from the setting in Table 129, Register 0x21, [7:1] |
| 11 | Reserved |

### [5:4] SWA_OVER_VOLTAGE_THRESHOLD_SETTING

- Description: Switch Node A Output Regulator Threshold For Over Voltage Status[3]
- Attribute: RW — Read/Write
- Default: 10 → +12.5% from the setting in Table 129, Register 0x21, [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +7.5% from the setting in Table 129, Register 0x21, [7:1] |
| 01 | +10% from the setting in Table 129, Register 0x21, [7:1] |
| 10 | +12.5% from the setting in Table 129, Register 0x21, [7:1] |
| 11 | Reserved |

### [3:2] SWA_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING

- Description: Switch Node A Output Regulator Threshold For Under Voltage Lockout Status
- Attribute: RW — Read/Write
- Default: 00 → -10% from the setting in Table 129, Register 0x21, [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | -10% from the setting in Table 129, Register 0x21, [7:1] |
| 01 | -12.5% from the setting in Table 129, Register 0x21, [7:1] |
| 10 | Reserved |
| 11 | Reserved |

### [1:0] SWA_OUTPUT_SOFT_STOP_TIME

- Description: SWA Output Regulator Soft Stop Time After VR Disable[4] 5
- Attribute: RW — Read/Write
- Default: 11 → 4 ms (Default)

| Code (bin) | Meaning |
|---|---|
| 00 | 0.5 ms |
| 01 | 1 ms |
| 10 | 2 ms |
| 11 | 4 ms (Default) |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 164, Register 0x46.
- NOTE 2: If required, the host must update the setting in register Table 129, Register 0x21, [0], Table 130, Register 0x22, [7:2] and Table 128, Register 0x20 [7:6] first prior to updating the settings in the register Table 129, Register 0x21, [7:1].
- NOTE 3: The setting for the Over Voltage must be higher than Power Good High Side Voltage threshold in Table 130, Register 0x22,[7:6].
- NOTE 4: This is the time it takes for buck regulator to go from steady state voltage to 0 V.
- NOTE 5: There is an extension to the SWA Soft Stop time in Table 150, Register 0x36 [7].

## R23 (0x23) — Reserved

Region: Host Region | Source: JESD301-6 Table 131, p.149

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | RESERVED | RV | 0 |

### [7:0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

## R24 (0x24) — Reserved

Region: Host Region | Source: JESD301-6 Table 132, p.150

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | RESERVED | RV | 0 |

### [7:0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

**Notes**

- NOTE 1: Only applicable if Table 173, Register 0x4F [0] = ‘0’.

## R25 (0x25) — SWB_VOLTAGE_SETTING, SWB_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

Region: Host Region | Source: JESD301-6 Table 133, p.150

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:1 | SWB_VOLTAGE_SETTING | RW | 011 1100 |
| 0 | SWB_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING | RW | 0 |

### [7:1] SWB_VOLTAGE_SETTING

- Description: Switch Node B Output Regulator Voltage Setting[3],[4] 5
- Attribute: RW — Read/Write
- Default: 011 1100 → 1100 mV

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 0000000 | 0x00 | 800 mV |
| 0000001 | 0x01 | 805 mV |
| 0000010 | 0x02 | 810 mV |
| ... | ... | ... |
| 0111100 | 0x3C | 1100 mV |
| ... | ... | ... |
| 1111101 | 0x7D | 1425 mV |
| 1111110 | 0x7E | 1430 mV |
| 1111111 | 0x7F | 1435 mV |

### [0] SWB_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

- Description: Switch Node B Output Threshold Low Side Voltage For Power Good Status
- Attribute: RW — Read/Write
- Default: 0 → -5% from the setting in Table 133, Register 0x25, [7:1]

| Code (bin) | Meaning |
|---|---|
| 0 | -5% from the setting in Table 133, Register 0x25, [7:1] |
| 1 | -7.5% from the setting in Table 133, Register 0x25, [7:1] |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 167, Register 0x49.
- NOTE 2: If required, the host must update the settings in register Table 133, Register 0x25, [0], Table 134, Register 0x26, [7:2] and Table 128, Register 0x20 [3:2] first prior to updating the settings in the register Table 133, Register 0x25, [7:1].
- NOTE 3: PMIC guarantees efficiency spec and all electrical characteristics spec within a range of 1050 mV to 1160 mV.
- NOTE 4: After VR is enabled, the host may update this register to any new setting that it may desire. However to prevent false error trigger, the PMIC internally will increment the SWB output voltage setting by 5 mV at a time. The time it takes for PMIC to adjust the output voltage is 5 μs for each 5 mV increment. The host must wait sufficient time for PMIC to adjust to final value. As an example, if host adjusts the output voltage by 50 mV from the original value, the host must wait minimum of 50 μs before PMIC can guarantee the new output voltage. During this time, PMIC masks the PWR_GOOD output signal assertion to prevent any artificial error due to the crossing of the output voltage threshold setting. However, PMIC does assert PWR_GOOD output signal if there is any abnormal issues that triggers VR Disable command as described in Table 30. Further, PMIC does monitor PWR_GOOD input signal and executes power off config sequence registers if it is registered low when Table 146, Register 0x32 [5] = ‘1’.
- NOTE 5: Only applicable if Table 173, Register 0x4F [0] = ‘0’.

## R26 (0x26) — SWB_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING, SWB_OVER_VOLTAGE_THRESHOLD_SETTING, SWB_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING, SWB_OUTPUT_SOFT_STOP_TIME

Region: Host Region | Source: JESD301-6 Table 134, p.151

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWB_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING | RW | 01 |
| 5:4 | SWB_OVER_VOLTAGE_THRESHOLD_SETTING | RW | 10 |
| 3:2 | SWB_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING | RW | 00 |
| 1:0 | SWB_OUTPUT_SOFT_STOP_TIME | RW | 11 |

### [7:6] SWB_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING

- Description: Switch Node B Output Threshold High Side Voltage For Power Good Status
- Attribute: RW — Read/Write
- Default: 01 → +7.5% from the setting in Table 133, Register 0x25, [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +5% from the setting in Table 133, Register 0x25, [7:1] |
| 01 | +7.5% from the setting in Table 133, Register 0x25, [7:1] |
| 10 | +10% from the setting in Table 133, Register 0x25, [7:1] |
| 11 | Reserved |

### [5:4] SWB_OVER_VOLTAGE_THRESHOLD_SETTING

- Description: Switch Node B Output Regulator Threshold For Over Voltage Status[3]
- Attribute: RW — Read/Write
- Default: 10 → +12.5% from the setting in Table 133, Register 0x25, [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +7.5% from the setting in Table 133, Register 0x25, [7:1] |
| 01 | +10% from the setting in Table 133, Register 0x25, [7:1] |
| 10 | +12.5% from the setting in Table 133, Register 0x25, [7:1] |
| 11 | Reserved |

### [3:2] SWB_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING

- Description: Switch Node B Output Regulator Threshold For Under Voltage Lockout Status
- Attribute: RW — Read/Write
- Default: 00 → -10% from the setting in Table 133, Register 0x25, [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | -10% from the setting in Table 133, Register 0x25, [7:1] |
| 01 | -12.5% from the setting in Table 133, Register 0x25, [7:1] |
| 10 | Reserved |
| 11 | Reserved |

### [1:0] SWB_OUTPUT_SOFT_STOP_TIME

- Description: SWB Output Regulator Soft Stop Time After VR Disable[4] 5
- Attribute: RW — Read/Write
- Default: 11 → 4 ms (Default)

| Code (bin) | Meaning |
|---|---|
| 00 | 0.5 ms |
| 01 | 1 ms |
| 10 | 2 ms |
| 11 | 4 ms (Default) |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 168, Register 0x4A.
- NOTE 2: If required, the host must update the settings in register Table 133, Register 0x25, [0], Table 134, Register 0x26, [7:2] and Table 128, Register 0x20 [3:2] first prior to updating the settings in the register Table 133, Register 0x25, [7:1].
- NOTE 3: The setting for the Over Voltage must be higher than Power Good High Side Voltage threshold in Table 134, Reg- ister 0x26,[7:6].
- NOTE 4: This is the time it takes for buck regulator to go from steady state voltage to 0 V.
- NOTE 5: There is an extension to the SWB Soft Stop time in Table 150, Register 0x36 [5].

## R27 (0x27) — SWC_VOLTAGE_SETTING, SWC_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

Region: Host Region | Source: JESD301-6 Table 135, p.152

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:1 | SWC_VOLTAGE_SETTING | RW | 011 1100 |
| 0 | SWC_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING | RW | 0 |

### [7:1] SWC_VOLTAGE_SETTING

- Description: Switch Node C Output Regulator Voltage Setting[3],[4]
- Attribute: RW — Read/Write
- Default: 011 1100 → 1800 mV

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 0000000 | 0x00 | 1500 mV |
| 0000001 | 0x01 | 1505 mV |
| 0000010 | 0x02 | 1510 mV |
| ... | ... | ... |
| 0111100 | 0x3C | 1800 mV |
| ... | ... | ... |
| 1111101 | 0x7D | 2125 mV |
| 1111110 | 0x7E | 2130 mV |
| 1111111 | 0x7F | 2135 mV |

### [0] SWC_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

- Description: Switch Node C Output Threshold Low Side Voltage For Power Good Status
- Attribute: RW — Read/Write
- Default: 0 → -5% from the setting in Table 135, Register 0x27, [7:1]

| Code (bin) | Meaning |
|---|---|
| 0 | -5% from the setting in Table 135, Register 0x27, [7:1] |
| 1 | -7.5% from the setting in Table 135, Register 0x27, [7:1] |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 169, Register 0x4B.
- NOTE 2: If required, the host must update the settings in register Table 135, Register 0x27, [0], Table 136, Register 0x28, [7:2] and Table 128, Register 0x20 [1:0] first prior to updating the settings in the register Table 135, Register 0x27, [7:1].
- NOTE 3: PMIC guarantees efficiency spec and all electrical characteristics spec within a range of 1750 mV to 1850 mV.
- NOTE 4: After VR is enabled, the host may update this register to any new setting that it may desire. However to prevent false error trigger, the PMIC internally will increment the SWC output voltage setting by 5 mV at a time. The time it takes for PMIC to adjust the output voltage is 5 μs for each 5 mV increment. The host must wait sufficient time for PMIC to adjust to final value. As an example, if host adjusts the output voltage by 50 mV from the original value, the host must wait minimum of 50 μs before PMIC can guarantee the new output voltage. During this time, PMIC masks the PWR_GOOD output signal assertion to prevent any artificial error due to the crossing of the output voltage threshold setting. However, PMIC does assert PWR_GOOD output signal if there is any abnormal issues that triggers VR Disable command as described in Table 30. Further, PMIC does monitor PWR_GOOD input signal and executes power off config sequence registers if it is registered low when Table 146, Register 0x32 [5] = ‘1’.

## R28 (0x28) — SWC_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING, SWC_OVER_VOLTAGE_THRESHOLD_SETTING, SWC_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING, SWC_OUTPUT_SOFT_STOP_TIME

Region: Host Region | Source: JESD301-6 Table 136, p.153

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWC_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING | RW | 01 |
| 5:4 | SWC_OVER_VOLTAGE_THRESHOLD_SETTING | RW | 10 |
| 3:2 | SWC_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING | RW | 00 |
| 1:0 | SWC_OUTPUT_SOFT_STOP_TIME | RW | 11 |

### [7:6] SWC_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING

- Description: Switch Node C Output Threshold High Side Voltage For Power Good Status
- Attribute: RW — Read/Write
- Default: 01 → +7.5% from the setting in Table 135, Register 0x27, [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +5% from the setting in Table 135, Register 0x27, [7:1] |
| 01 | +7.5% from the setting in Table 135, Register 0x27, [7:1] |
| 10 | +10% from the setting in Table 135, Register 0x27, [7:1] |
| 11 | Reserved |

### [5:4] SWC_OVER_VOLTAGE_THRESHOLD_SETTING

- Description: Switch Node C Output Regulator Threshold For Over Voltage Status[3]
- Attribute: RW — Read/Write
- Default: 10 → +12.5% from the setting in Table 135, Register 0x27, [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +7.5% from the setting in Table 135, Register 0x27, [7:1] |
| 01 | +10% from the setting in Table 135, Register 0x27, [7:1] |
| 10 | +12.5% from the setting in Table 135, Register 0x27, [7:1] |
| 11 | Reserved |

### [3:2] SWC_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING

- Description: Switch Node C Output Regulator Threshold For Under Voltage Lockout Status
- Attribute: RW — Read/Write
- Default: 00 → -10% from the setting in Table 135, Register 0x27, [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | -10% from the setting in Table 135, Register 0x27, [7:1] |
| 01 | -12.5% from the setting in Table 135, Register 0x27, [7:1] |
| 10 | Reserved |
| 11 | Reserved |

### [1:0] SWC_OUTPUT_SOFT_STOP_TIME

- Description: SWC Output Regulator Soft Stop Time After VR Disable[4] 5
- Attribute: RW — Read/Write
- Default: 11 → 8 ms (Default)
- Source correction: Spec lists code 000 for '1 ms'; corrected to 00. Table for this 2-bit field lists 3-digit codes (000-011); the leading 0 is dropped to match the field width (same values as R4C[1:0]).
- Source correction: Spec lists code 001 for '2 ms'; corrected to 01. Table for this 2-bit field lists 3-digit codes (000-011); the leading 0 is dropped to match the field width (same values as R4C[1:0]).
- Source correction: Spec lists code 010 for '4 ms'; corrected to 10. Table for this 2-bit field lists 3-digit codes (000-011); the leading 0 is dropped to match the field width (same values as R4C[1:0]).
- Source correction: Spec lists code 011 for '8 ms (Default)'; corrected to 11. Table for this 2-bit field lists 3-digit codes (000-011); the leading 0 is dropped to match the field width (same values as R4C[1:0]).

| Code (bin) | Meaning |
|---|---|
| 00 | 1 ms |
| 01 | 2 ms |
| 10 | 4 ms |
| 11 | 8 ms (Default) |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 170, Register 0x4C.
- NOTE 2: If required, the host must update the settings in register Table 135, Register 0x27, [0], Table 136, Register 0x28, [7:2] and Table 128, Register 0x20 [1:0] first prior to updating the settings in the register Table 135, Register 0x27, [7:1].
- NOTE 3: The setting for the Over Voltage must be higher than Power Good High Side Voltage threshold in Table 136, Reg- ister 0x28,[7:6].
- NOTE 4: This is the time it takes for buck regulator to go from steady state voltage to 0 V.
- NOTE 5: There is an extension to the SWC Soft Stop time in Table 150, Register 0x36 [4].

## R29 (0x29) — SWA_MODE_SELECT, SWA_SWITCHING_FREQ

Region: Host Region | Source: JESD301-6 Table 137, p.154

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWA_MODE_SELECT | RW | 10 |
| 5:4 | SWA_SWITCHING_FREQ | RW | 00 |
| 3:0 | RESERVED | RV | 0 |

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

### [3:0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 171, Register 0x4D.
- NOTE 2: If required, the host must adjust this register first before issuing VR Enable command in Table 146, Register 0x32 [7].

## R2A (0x2A) — SWB_MODE_SELECT, SWB_SWITCHING_FREQ, SWC_MODE_SELECT, SWC_SWITCHING_FREQ

Region: Host Region | Source: JESD301-6 Table 138, p.155

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWB_MODE_SELECT | RW | 10 |
| 5:4 | SWB_SWITCHING_FREQ | RW | 00 |
| 3:2 | SWC_MODE_SELECT | RW | 10 |
| 1:0 | SWC_SWITCHING_FREQ | RW | 01 |

### [7:6] SWB_MODE_SELECT

- Description: Switch Node B Output Regulator Mode Selection[3]
- Attribute: RW — Read/Write
- Default: 10 → COT; DCM (Constant on Time; Discontinuous Current Mode)

| Code (bin) | Meaning |
|---|---|
| 00 | Reserved |
| 01 | Reserved |
| 10 | COT; DCM (Constant on Time; Discontinuous Current Mode) |
| 11 | COT; Forced CCM (Constant on Time; Continuous Current Mode) |

### [5:4] SWB_SWITCHING_FREQ

- Description: Switch Node B Output Regulator Switching Frequency[3]
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
- Default: 01 → Vendor Specific

| Code (bin) | Meaning |
|---|---|
| 00 | 750 KHz |
| 01 | Vendor Specific |
| 10 | Vendor Specific |
| 11 | Vendor Specific |

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 172, Register 0x4E.
- NOTE 2: If required, the host must adjust this register first before issuing VR Enable command in Table 146, Register 0x32 [7].
- NOTE 3: Only applicable if Table 173, Register 0x4F [0] = ‘0’.

## R2B (0x2B) — VOUT_1.8V_VOLTAGE_SETTING, VOUT_1.0V_VOLTAGE_SETTING

Region: Host Region | Source: JESD301-6 Table 139, p.156

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | VOUT_1.8V_VOLTAGE_SETTING | RW | 01 |
| 5:3 | RESERVED | RV | 0 |
| 2:1 | VOUT_1.0V_VOLTAGE_SETTING | RW | 01 |
| 0 | RESERVED | RV | 0 |

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

### [5:3] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

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

### [0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 175, Register 0x51.
- NOTE 2: If required, the host must adjust this register first before issuing VR Enable command in Table 146, Register 0x32 [7]. The host must also wait minimum of 5 μs after the adjustment before issuing VR Enable command.
- NOTE 3: The VOUT_1.8V Power Good threshold in register Table 122, Register 0x1A [2] is always fixed regardless of the setting in this register.
- NOTE 4: If required, the host must adjust this register one step at a time (0.1 V increment or decrement) to prevent false trigger of power good status and PWR_GOOD pin assertion. In other words, host should not increment or decrement 0.2 V or 0.3 V from its current setting.

## R2C (0x2C) — SWA_OUTPUT_SOFT_START_TIME

Region: Host Region | Source: JESD301-6 Table 140, p.156

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:5 | SWA_OUTPUT_SOFT_START_TIME | RW | 001 |
| 4:0 | RESERVED | RV | 0 |

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

### [4:0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 180, Register 0x5D.
- NOTE 2: If required, the host must adjust this register first before issuing VR Enable command in Table 146, Register 0x32 [7].
- NOTE 3: This is the time it takes for buck regulator to go from 0 V to steady state voltage (the actual voltage varies based on pre-programmed voltage).

## R2D (0x2D) — SWB_OUTPUT_SOFT_START_TIME, SWC_OUTPUT_SOFT_START_TIME

Region: Host Region | Source: JESD301-6 Table 141, p.157

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:5 | SWB_OUTPUT_SOFT_START_TIME | RW | 001 |
| 4 | RESERVED | RV | 0 |
| 3:1 | SWC_OUTPUT_SOFT_START_TIME | RW | 001 |
| 0 | RESERVED | RV | 0 |

### [7:5] SWB_OUTPUT_SOFT_START_TIME

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

### [4] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [3:1] SWC_OUTPUT_SOFT_START_TIME

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

### [0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

**Notes**

- NOTE 1: At first power on, this register is automatically configured identically by PMIC on its own as Table 181, Register 0x5E.
- NOTE 2: If required, the host must adjust this register first before issuing VR Enable command in Table 146, Register 0x32 [7].
- NOTE 3: This is the time it takes for buck regulator to go from 0 V to steady state voltage (the actual voltage varies based on pre-programmed voltage)
- NOTE 4: Only applicable if Table 173, Register 0x4F [0] = ‘0’.

## R2E (0x2E) — PMIC_SHUTDOWN_TEMPERATURE_THRESHOLD

Region: Host Region | Source: JESD301-6 Table 142, p.157

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

## R2F (0x2F) — SWA_REGULATOR_CONTROL, SWB_REGULATOR_CONTROL, SWC_REGULATOR_CONTROL, SECURE_MODE, MASK_BITS_REGISTER_CONTROL

Region: Host Region | Source: JESD301-6 Table 143, p.158

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | RESERVED | RV | 0 |
| 6 | SWA_REGULATOR_CONTROL | RW | 0 |
| 5 | RESERVED | RV | 0 |
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

### [5] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [4] SWB_REGULATOR_CONTROL

- Description: Disable SWB Regulator Output[1],[2],[3]
- Attribute: RW — Read/Write
- Default: 0 → Disable Switch Node B Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Disable Switch Node B Output Regulator |
| 1 | Enable Switch Node B Output Regulator |

### [3] SWC_REGULATOR_CONTROL

- Description: Disable SWC Regulator Output[1],[2]
- Attribute: RW — Read/Write
- Default: 0 → Disable Switch Node C Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Disable Switch Node C Output Regulator |
| 1 | Enable Switch Node C Output Regulator |

### [2] SECURE_MODE

- Description: PMIC Mode Operation
- Attribute: RW — Read/Write
- Default: 0 → Secure Mode Operation[4],[5]

| Code (bin) | Meaning |
|---|---|
| 0 | Secure Mode Operation[4],[5] |
| 1 | Programmable Mode Operation |

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

- NOTE 1: This bit must be used only after power up sequence (after VR Enable command). At first power up, PMIC automatically updates the status of this register to ‘1’ after VR Enable command. When VR Enable command is registered, the PMIC updates this register based on Power On Sequence Configuration (0 to 2) setting. If enabled in Power On Sequence Configuration 0 to 2 registers, only then, under programmable mode of operation, the PMIC’s output regulator can be disabled by clearing this bit and they can be reenabled again by setting this bit. The PMIC does not alter its Power Good output signal and keeps it asserted High. If any regulator is not enabled in Power on Sequence Configuration 0 to 2, it cannot be enabled using this register. For example, if only SWA is enabled and SWB and SWC is not enabled in Table 158, Register 0x40 [7:0] to Table 160, Register 0x42, [7:0] then only SWA can be disabled and then re-enabled again but SWB and SWC cannot be enabled using Table 143, Register 0x2F [6,4:3].
- NOTE 2: In programmable mode, after VR enable command, if any output regulators are disabled by clearing Table 143, Reg- ister 0x2F [6,4:3] and then if host issues VR Disable command or PMIC internally triggers VR Disable command, the PMIC keeps the disabled output regulator in Table 143, Register 0x2F [6,4:3] off and remaining output regulators are disabled by following the Power Off Sequence Configuration 0 to 2 settings.
- NOTE 3: Only applicable if Table 173, Register 0x4F [0] = ‘0’.
- NOTE 4: This bit must be configured before issuing VR Enable command. If this bit is configured to ‘0’, when PMIC registers VR Enable command, all registers bits starting Table 117, Register 0x15 to Table 143, Register 0x2F, Table 146, Register 0x32 [7,5:0], Table 149, Register 0x35, and Table 150, Register 0x36 in the host region as well as Table 158, Register 0x40 to Register 0x6F in the DIMM vendor region and Register 0x70 to Register 0xFF in the PMIC vendor region are secured and the host cannot change unless the PMIC goes through power cycle.
- NOTE 5: Simultaneous usage of programmable mode (i.e., Table 143, Register 0x2F [2] = ‘1’), PWR_GOOD as IO (i.e., Table 146, Register 0x32 [5] = ‘1’) and P1 State Enable (i.e., Table 122, Register 0x1A [4] = ‘1’) is considered an illegal configuration when VR_EN pin is intended to be used; otherwise it is a valid configuration if VR_EN com- mand is used on I2C/I3C Basic bus.
- NOTE 6: Applies to Mask Registers Table 117, Register 0x15 [5,3:2,0], Table 118, Register 0x16 [7,5,3,1:0], Table 119, Reg- ister 0x17 [7,5:2], Table 120, Register 0x18 [7,5:3,1:0], Table 121, Register 0x19 [2] when any one or more Mask registers are set to ‘1’. If all Mask registers are configured as ‘0’, the setting in this register (Table 143, Register 0x2F [1:0]) does not matter.

## R30 (0x30) — ADC_ENABLE, ADC_SELECT, ADC_REGISTER_UPDATE_FREQUENCY

Region: Host Region | Source: JESD301-6 Table 144, p.159

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
| 0001 | 0x1 | Reserved |
| 0010 | 0x2 | SWB Output Voltage[3] |
| 0011 | 0x3 | SWC Output Voltage |
| 0100 | 0x4 | Reserved |
| 0101 | 0x5 | VIN_Bulk Input Voltage |
| 0110 | 0x6 | Reserved |
| 0111 | 0x7 | Reserved |
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

- NOTE 1: Disables the ADC function completely. Applies to voltage readout in Table 145, Register 0x31 [7:0] as well as current or power readout in Table 108, Register 0x0C [7:0], Table 110, Register 0x0E [7:0] and Table 111, Regis- ter 0x0F [7:0]. Does not apply to thermal sensor temperature readout in Table 147, Register 0x33 [7:5] as well as high temperature warning and critical temperature shutdown.
- NOTE 2: The host shall wait minimum of 9 ms delay after the input selection for ADC readout and the actual readout from Table 145, Register 0x31 to get the latest reading.
- NOTE 3: Only applicable if Table 173, Register 0x4F [0] = ‘0’.
- NOTE 4: For average output current or power measurement in registers Table 108, Register 0x0C [7:0], Table 110, Register 0x0E [7:0] and Table 111, Register 0x0F [7:0].
- NOTE 5: This register represents how often the registers are updated. The internal sampling rate is vendor specific.

## R31 (0x31) — ADC_READ

Region: Host Region | Source: JESD301-6 Table 145, p.160

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | ADC_READ | RO | 0 |

### [7:0] ADC_READ

- Description: ADC Output Voltage Reading[1](Applies to SW[A:C], VOUT_1.8V, VOUT_1.0V)
- Attribute: RO — Read Only (writes have no effect)
- Default: 0

**When: ADC Output Voltage Reading[1](Applies to SW[A:C], VOUT_1.8V, VOUT_1.0V)**

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

**Notes**

- NOTE 1: Only valid when Table 144, Register 0x30 [6:3] = ‘0000’ or ‘0010’ or ‘0011’ or ‘0110’ or ‘1000’ or ‘1001’.
- NOTE 2: Only valid when Table 144, Register 0x30 [6:3] = ‘0101’.

## R32 (0x32) — VR_ENABLE, MANAGEMENT_INTERFACE_SELECTION, PWR_GOOD_IO_TYPE, PWR_GOOD_OUTPUT_SIGNAL_CONTROL, ADC_ACCURACY_STEP_SIZE

Region: Host Region | Source: JESD301-6 Table 146, p.161

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | VR_ENABLE | RW | 0 |
| 6 | MANAGEMENT_INTERFACE_SELECTION | RO | 0 |
| 5 | PWR_GOOD_IO_TYPE | RW | 0 |
| 4:3 | PWR_GOOD_OUTPUT_SIGNAL_CONTROL | RW | 0 |
| 2 | RESERVED | RV | 0 |
| 1:0 | ADC_ACCURACY_STEP_SIZE | RW | 00 |

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
- Default: 00 → 125 mA or 125 mW

| Code (bin) | Meaning |
|---|---|
| 00 | 125 mA or 125 mW |
| 01 | 31.25 mA or 31.25 mW |

**Notes**

- NOTE 1: The PMIC updates this bit when VR_EN signal transition to high or when host issues VR Enable command over I2C/I3C Basic bus; whichever comes first. PMIC also updates this bit when VR_EN signal transitions to low or when host issues VR Disable command over I2C/I3C Basic bus in programmable mode; whichever comes first. Further, PMIC updates this bit when PWR_GOOD input is low (if Table 146, Register 0x32 [5] = ‘1’) or when PMIC internally generates VR Disable command due to fault condition regardless of PMIC’s VR_EN signal input status.
- NOTE 2: After this bit is set to ‘1’, the PMIC executes Power On Sequence configuration 0 (Table 158, Register 0x40) to Power On Sequence configuration 2 (Table 160, Register 0x42,) registers. At least one bit in Table 158, Register 0x40 [6,4:3] must be set to ‘1’ to issue VR Enable (either with VR_EN pin or over I2C/I3C Basic bus) command.
- NOTE 3: The host shall ensure that prior to issuing VR Enable command, there is no pending IBI interrupt (i.e., Table 106, Register 0x0A [1] = ‘1’). After host issues VR Enable command (either with VR_EN pin or over I2C/I3C Basic bus), the PMIC may NACK any I2C or I3C Basic bus transactions by host until tPMIC_PWR_GOOD_OUT timing parameter is satisfied. The host shall not access any device specific registers or issue CCCs until tPMIC_PWR_- GOOD_Out parameter is satisfied. The PMIC device may request for an IBI during power up sequence (i.e., during tPMIC_PWR_GOOD_Out time) if there is any event.
- NOTE 4: An exception to this register is applied. When PMIC is operating in secure mode of operation and PWR_GOOD input is low (if Table 146, Register 0x32 [5] = ‘1’), the PMIC unlocks this register. The PMIC allows host to issue VR Enable command. After host issues VR Enable command, the PMIC re-locks this register.
- NOTE 5: This register is automatically updated when SETAASA CCC or RSTDAA CCC is registered by the PMIC device or when PMIC device goes through bus reset as described in Section 6.18.13 regardless of whether PMIC is in secure mode or programmable mode of operation. This register can be read by the Host through normal Read operation but it cannot be written with normal write operation either in I2C mode or I3C Basic mode of operation. When this register is updated, it takes in effect when there is a next START operation (i.e., after STOP operation).
- NOTE 6: This bit must be configured before issuing VR Enable command.
- NOTE 7: Simultaneous usage of programmable mode (i.e., Table 143, Register 0x2F [2] = ‘1’), PWR_GOOD as IO (i.e., Table 146, Register 0x32 [5] = ‘1’) and P1 State Enable (i.e., Table 122, Register 0x1A [4] = ‘1’) is considered an illegal configuration when VR_EN pin is intended to be used; otherwise it is a valid configuration if VR_EN command is used on I2C/I3C Basic bus.
- NOTE 8: When this encoding is set, the PMIC always floats the PWR_GOOD output signal even when there is an internal VR Disable command due to fault condition.

## R33 (0x33) — TEMPERATURE_MEASUREMENT, VIN_BULK_UNDER_VOLTAGE_LOCKOUT_STATUS, VOUT_1.0V_OUTPUT_POWER_GOOD_STATUS

Region: Host Region | Source: JESD301-6 Table 147, p.162

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:5 | TEMPERATURE_MEASUREMENT | RO | 0 |
| 4 | RESERVED | RV | 0 |
| 3 | VIN_BULK_UNDER_VOLTAGE_LOCKOUT_STATUS | RO | 0 |
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
| 111 | ≥ 140 °C |

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

### [1:0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

**Notes**

- NOTE 1: The accuracy of the temperature readout code is + 5 °C.
- NOTE 2: This register is set when VIN_Bulk input voltage goes below a vendor specific threshold.
- NOTE 3: This register is set when VOUT_1.0V output drops below the threshold setting in register Table 122, Register 0x1A [0].

## R34 (0x34) — PEC_ENABLE, IBI_ENABLE, PARITY_DISABLE, HID_CODE

Region: Host Region | Source: JESD301-6 Table 148, p.163

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | PEC_ENABLE | RO | 0 |
| 6 | IBI_ENABLE | RO | 0 |
| 5 | PARITY_DISABLE | RO | 0 |
| 4 | RESERVED | RV | 0 |
| 3:1 | HID_CODE | RO | 111 |
| 0 | RESERVED | RV | 0 |

### [7] PEC_ENABLE

- Description: Packet Error Code Enable[2] (Applicable Only if Table 146, Register 0x32 [6] = ‘1’)
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → Disable

| Code (bin) | Meaning |
|---|---|
| 0 | Disable |
| 1 | Enable |

### [6] IBI_ENABLE

- Description: In Band Interrupt Enable[3] (Applicable Only if Table 146, Register 0x32 [6] = ‘1’)
- Attribute: RO — Read Only (writes have no effect)
- Default: 0 → Disable

| Code (bin) | Meaning |
|---|---|
| 0 | Disable |
| 1 | Enable |

### [5] PARITY_DISABLE

- Description: T Bit Parity Code Disable[2] (Applicable Only if Table 146, Register 0x32[6] = ‘1’.)
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
- NOTE 2: This register is automatically updated when RSTDAA CCC is registered by the PMIC device or when PMIC device goes through bus reset as described in Section 6.18.13. This register cannot be written by the Host through normal write operation either in I2C mode or I3C mode of operation. This register is updated with DEVCTRL CCC with RegMod=’0’ only. This register cannot be written with DEVCTRL CCC with RegMod = ‘1’.
- NOTE 3: This register is automatically updated when ENEC CCC or DISEC CCC or RSTDAA CCC is registered by the PMIC device or when PMIC device goes through bus reset as described in Section 6.18.13. This register can be read by the Host through normal Read operation but it cannot be written with normal write operation either in I2C mode or I3C mode of operation. This register cannot be written with DEVCTRL CCC with RegMod = ‘1’.
- NOTE 4: When Parity function is disabled, the PMIC simply ignores the “T” bit information from the Host. The host may actually choose to compute the parity and send that information in “T” bit or simply drive static low or high in “T” bit.
- NOTE 5: This register is updated when PMIC device receives SETHID CCC or when PMIC device goes through bus reset as described in Section 6.18.13. This register cannot be written with DEVCTRL CCC with RegMod = ‘1’.

## R35 (0x35) — ERROR_INJECTION_ENABLE, ERROR_INJECTION_RAIL_SELECTION, OVER_VOLTAGE_UNDER_VOLTAGE_SELECT, MISC_ERROR_INJECTION_TYPE

Region: Host Region | Source: JESD301-6 Table 149, p.164

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
| 010 | Reserved |
| 011 | SWB Output Only |
| 100 | SWC Output Only |
| 101 | VIN_Bulk Input Only |
| 110 | Reserved |
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
| 001 | Reserved |
| 010 | Critical Temperature Shutdown |
| 011 | High Temperature Warning Threshold |
| 100 | VOUT_1.8V LDO Power Good |
| 101 | High Current Consumption Warning[9] |
| 110 | Reserved |
| 111 | Current Limiter Warning[9] |

**Notes**

- NOTE 1: Refer to Section 6.13 for error function usage model. The host can erase the error log registers (Table 100, Register 0x04 to Table 103, Register 0x07) by writing 0x74 to Table 153, Register 0x39.
- NOTE 2: To exit from Error Injection Mode, the PMIC must go through power cycle of both VIN_Bulk input supply.
- NOTE 3: When error injection function is invoked by setting bit [7] = ‘1’, the setting of bits [6:4, 2:0] = ‘000 000’ is considered an illegal setting.
- NOTE 4: This register Table 149, Register 0x35 [6:4] is only applicable if Table 149, Register 0x35 [2:0] is ‘000’. Any value other than ‘000’ in both Table 149, Register 0x35 [6:4] and Table 149, Register 0x35 [2:0] is considered an illegal setting and PMIC operation is not guaranteed.
- NOTE 5: If dual phase regulator is selected, use SWA encoding to inject the error. Register bit [3] selects either over voltage or under voltage condition for the setting selected in this register.
- NOTE 6: This register Table 149, Register 0x35 [3] is only applicable if bits [6:4] is anything other than ‘000’.
- NOTE 7: The under voltage selection only applies to SWx output rails and VIN_Bulk input.
- NOTE 8: This register Table 149, Register 0x35 [2:0] is only applicable if Table 149, Register 0x35 [6:3] is ‘0000’. Any value other than ‘000’ in both Table 149, Register 0x35 [6:4] and Table 149, Register 0x35 [2:0] is considered an illegal setting and PMIC operation is not guaranteed.
- NOTE 9: Applies to all enabled SWx output regulators at the same time.

## R36 (0x36) — SWA_OUTPUT_SOFT_STOP_TIME_EXTENSION, SWB_OUTPUT_SOFT_STOP_TIME_EXTENSION, SWC_OUTPUT_SOFT_STOP_TIME_EXTENSION, ACOUSTIC_NOISE_PREVENTION_CONTROL

Region: Host Region | Source: JESD301-6 Table 150, p.165

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | SWA_OUTPUT_SOFT_STOP_TIME_EXTENSION | RW | 0 |
| 6 | RESERVED | RV | 0 |
| 5 | SWB_OUTPUT_SOFT_STOP_TIME_EXTENSION | RW | 0 |
| 4 | SWC_OUTPUT_SOFT_STOP_TIME_EXTENSION | RW | 0 |
| 3:1 | ACOUSTIC_NOISE_PREVENTION_CONTROL | RW | 001 |
| 0 | RESERVED | RV | 0 |

### [7] SWA_OUTPUT_SOFT_STOP_TIME_EXTENSION

- Description: SWA Output Regulator Soft Stop Time After VR Disable[1] 2 3-bit encoding with {R36[7],R22[1:0]}:
- Attribute: RW — Read/Write
- Default: 0
- Note: the codes below are wider than this 1-bit field; the encoding combines bits from more than one field/register (see Description).

| Code (bin) | Meaning |
|---|---|
| 0xx | Encoding determined by R22[1:0] (Default) |
| 100 | 8 ms |
| 101 | 16 ms |
| 110 | 32 ms |
| 111 | 64 ms |

### [6] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [5] SWB_OUTPUT_SOFT_STOP_TIME_EXTENSION

- Description: SWB Output Regulator Soft Stop Time After VR Disable[1] 2 3-bit encoding with {R36[5],R26[1:0]}:
- Attribute: RW — Read/Write
- Default: 0
- Note: the codes below are wider than this 1-bit field; the encoding combines bits from more than one field/register (see Description).

| Code (bin) | Meaning |
|---|---|
| 0xx | Encoding determined by R26[1:0] (Default) |
| 100 | 8 ms |
| 101 | 16 ms |
| 110 | 32 ms |
| 111 | 64 ms |

### [4] SWC_OUTPUT_SOFT_STOP_TIME_EXTENSION

- Description: SWC Output Regulator Soft Stop Time After VR Disable[1] 2 3-bit encoding with {R36[4],R28[1:0]}:
- Attribute: RW — Read/Write
- Default: 0
- Note: the codes below are wider than this 1-bit field; the encoding combines bits from more than one field/register (see Description).

| Code (bin) | Meaning |
|---|---|
| 0xx | Encoding determined by R28[1:0] (Default) |
| 100 | 16 ms |
| 101 | 32 ms |
| 110 | 64 ms |
| 111 | Vendor-defined |

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

- NOTE 1: This is the time it takes for buck regulator to go from steady state voltage to 0 V.
- NOTE 2: At first power on, this register is automatically configured identically by PMIC on its own as Table 162, Register 0x44

## R37 (0x37) — DIMM_VENDOR_MEMORY_REGION_PASSWORD_LOWER_BYTE

Region: Host Region | Source: JESD301-6 Table 151, p.166

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | DIMM_VENDOR_MEMORY_REGION_PASSWORD_LOWER_BYTE | WO | - |

### [7:0] DIMM_VENDOR_MEMORY_REGION_PASSWORD_LOWER_BYTE

- Description: DIMM Vendor Memory Region (0x40 - 0x6F) Password - Lower Byte [7:0] = Code
- Attribute: WO — Write Only (reads return 0)
- Default: -
- Values: no per-value encoding is listed in the spec for this field.

## R38 (0x38) — DIMM_VENDOR_MEMORY_REGION_PASSWORD_UPPER_BYTE

Region: Host Region | Source: JESD301-6 Table 152, p.166

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | DIMM_VENDOR_MEMORY_REGION_PASSWORD_UPPER_BYTE | WO | - |

### [7:0] DIMM_VENDOR_MEMORY_REGION_PASSWORD_UPPER_BYTE

- Description: DIMM Vendor Memory Region (0x40 - 0x6F) Password - Upper Byte [7:0] = Code
- Attribute: WO — Write Only (reads return 0)
- Default: -
- Values: no per-value encoding is listed in the spec for this field.

## R39 (0x39) — (unnamed)

Region: Host Region | Source: JESD301-6 Table 153, p.166

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
| 0x74 | Clear Registers R04 to R07, Erase MTP memory for R04 to R07 Registers. |

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

Region: Host Region | Source: JESD301-6 Table 154, p.167

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
- NOTE 2: The register setting in Table 154, Register 0x3A [5:4] is a don’t care.
- NOTE 3: This mode is only allowed when PEC function is disabled (i.e., Table 148, Register 0x34 [7] = ‘0’).
- NOTE 4: This register is only applicable if Table 154, Register 0x3A [6] = ‘1’.
- NOTE 5: This register is only applicable if Table 154, Register 0x3A [6] = ‘1’ and Table 148, Register 0x34 [7] = ‘1’.

## R3B (0x3B) — PMIC_PART_CAPABILITY, REVISION_ID_MAJOR_STEPPING, REVISION_ID_MINOR_STEPPING

Region: Host Region | Source: JESD301-6 Table 155, p.168

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | RESERVED | RV | 0 |
| 6 | PMIC_PART_CAPABILITY | ROE | - |
| 5:4 | REVISION_ID_MAJOR_STEPPING | ROE | - |
| 3:1 | REVISION_ID_MINOR_STEPPING | ROE | - |
| 0 | RESERVED | RV | - |

### [7] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [6] PMIC_PART_CAPABILITY

- Description: PMIC Current Capability.
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: -

| Code (bin) | Meaning |
|---|---|
| 0 | PMIC5100 (Low Current) |
| 1 | PMIC5120 (High Current) |

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

### [0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: -

## R3C (0x3C) — VENDOR_ID_BYTE0

Region: Host Region | Source: JESD301-6 Table 156, p.168

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | VENDOR_ID_BYTE0 | ROE | - |

### [7:0] VENDOR_ID_BYTE0

- Description: Vendor Identification Register Byte 0.
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: -
- Values: no per-value encoding is listed in the spec for this field.

## R3D (0x3D) — VENDOR_ID_BYTE1

Region: Host Region | Source: JESD301-6 Table 157, p.168

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | VENDOR_ID_BYTE1 | ROE | - |

### [7:0] VENDOR_ID_BYTE1

- Description: Vendor Identification Register Byte 1.
- Attribute: ROE — Read Only (writes have no effect); Persistent across power cycle, erasable by command
- Default: -
- Values: no per-value encoding is listed in the spec for this field.

## R40 (0x40) — POWER_ON_SEQUENCE_CONFIG0, POWER_ON_SEQUENCE_CONFIG0_SWA_ENABLE, POWER_ON_SEQUENCE_CONFIG0_SWB_ENABLE, POWER_ON_SEQUENCE_CONFIG0_SWC_ENABLE, POWER_ON_SEQUENCE_CONFIG0_IDLE

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-6 Table 158, p.169

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | POWER_ON_SEQUENCE_CONFIG0 | RWPE | 0 |
| 6 | POWER_ON_SEQUENCE_CONFIG0_SWA_ENABLE | RWPE | 0 |
| 5 | RESERVED | RV | 0 |
| 4 | POWER_ON_SEQUENCE_CONFIG0_SWB_ENABLE | RWPE | 0 |
| 3 | POWER_ON_SEQUENCE_CONFIG0_SWC_ENABLE | RWPE | 0 |
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

- Description: Enable Switch Node A Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Disable Switch Node A Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Disable Switch Node A Output Regulator |
| 1 | Enable Switch Node A Output Regulator |

### [5] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [4] POWER_ON_SEQUENCE_CONFIG0_SWB_ENABLE

- Description: Enable Switch Node B Output Regulator.[3]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Disable Switch Node B Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Disable Switch Node B Output Regulator |
| 1 | Enable Switch Node B Output Regulator |

### [3] POWER_ON_SEQUENCE_CONFIG0_SWC_ENABLE

- Description: Enable Switch Node C Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Disable Switch Node C Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Disable Switch Node C Output Regulator |
| 1 | Enable Switch Node C Output Regulator |

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

- NOTE 1: If more than one configuration register is used for power on sequence, first register must start at Table 158, Register 0x40 and it must go in sequential order to Table 160, Register 0x42, to turn on all desired regulators. In other words, there must not be any gap of the register that is used for power on sequence.
- NOTE 2: If bit [7] = ‘0’, bits [6,4:3] must be programmed as ‘000’. If bit [7] = ‘1’, at least one of the bits [6,4:3] must be programmed as ‘1’.
- NOTE 3: Only applicable if Table 173, Register 0x4F [0] = ‘0’. This bit is a don’t care when Table 173, Register 0x4F [0] = ‘1’.
- NOTE 4: Idle time is the additional time after soft-start time expires. The PMIC waits sum of Soft Start time and Idle time before it executes the next power on sequence configuration register. If more than one regulators are enabled, the PMIC uses the largest value of the soft start time among the regulators that are enabled in this configuration register.

## R41 (0x41) — POWER_ON_SEQUENCE_CONFIG1, POWER_ON_SEQUENCE_CONFIG1_SWA_ENABLE, POWER_ON_SEQUENCE_CONFIG1_SWB_ENABLE, POWER_ON_SEQUENCE_CONFIG1_SWC_ENABLE, POWER_ON_SEQUENCE_CONFIG1_IDLE

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-6 Table 159, p.170

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | POWER_ON_SEQUENCE_CONFIG1 | RWPE | 0 |
| 6 | POWER_ON_SEQUENCE_CONFIG1_SWA_ENABLE | RWPE | 0 |
| 5 | RESERVED | RV | 0 |
| 4 | POWER_ON_SEQUENCE_CONFIG1_SWB_ENABLE | RWPE | 0 |
| 3 | POWER_ON_SEQUENCE_CONFIG1_SWC_ENABLE | RWPE | 0 |
| 2:0 | POWER_ON_SEQUENCE_CONFIG1_IDLE | RWPE | 001 |

### [7] POWER_ON_SEQUENCE_CONFIG1

- Description: PMIC Power On Sequence Config 1
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Do Not Execute Config3[1]

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Execute Config3[1] |
| 1 | Execute Command 1 |

### [6] POWER_ON_SEQUENCE_CONFIG1_SWA_ENABLE

- Description: Enable Switch Node A Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Disable Switch Node A Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Disable Switch Node A Output Regulator |
| 1 | Enable Switch Node A Output Regulator |

### [5] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [4] POWER_ON_SEQUENCE_CONFIG1_SWB_ENABLE

- Description: Enable Switch Node B Output Regulator.[4]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Disable Switch Node B Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Disable Switch Node B Output Regulator |
| 1 | Enable Switch Node B Output Regulator |

### [3] POWER_ON_SEQUENCE_CONFIG1_SWC_ENABLE

- Description: Enable Switch Node C Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Disable Switch Node C Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Disable Switch Node C Output Regulator |
| 1 | Enable Switch Node C Output Regulator |

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

- NOTE 1: If any regulators are enabled in Table 158, Register 0x40 [6:3], those regulators must be configured as ‘1’ in this sequence.
- NOTE 2: If more than one configuration register is used for power on sequence, first register must start at Table 158, Register 0x40 and it must go in sequential order to Table 160, Register 0x42, to turn on all desired regulators. In other words, there must not be any gap of the register that is used for power on sequence.
- NOTE 3: If bit [7] = ‘0’, bits [6,4:3] must be programmed as ‘000’. If bit [7] = ‘1’, at least one of the bits [6,4:3] must be programmed as ‘1’.
- NOTE 4: Only applicable if Table 173, Register 0x4F [0] = ‘0’. This bit is a don’t care when Table 173, Register 0x4F [0] = ‘1’.
- NOTE 5: Idle time is the additional time after soft-start time expires. The PMIC waits sum of Soft Start time and Idle time before it executes the next power on sequence configuration register. If more than one regulators are enabled, the PMIC uses the largest value of the soft start time among the regulators that are enabled in this configuration register.

## R42 (0x42) — POWER_ON_SEQUENCE_CONFIG2, POWER_ON_SEQUENCE_CONFIG2_SWA_ENABLE, POWER_ON_SEQUENCE_CONFIG2_SWB_ENABLE, POWER_ON_SEQUENCE_CONFIG2_SWC_ENABLE, POWER_ON_SEQUENCE_CONFIG2_IDLE

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-6 Table 160, p.171

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | POWER_ON_SEQUENCE_CONFIG2 | RWPE | 0 |
| 6 | POWER_ON_SEQUENCE_CONFIG2_SWA_ENABLE | RWPE | 0 |
| 5 | RESERVED | RV | 0 |
| 4 | POWER_ON_SEQUENCE_CONFIG2_SWB_ENABLE | RWPE | 0 |
| 3 | POWER_ON_SEQUENCE_CONFIG2_SWC_ENABLE | RWPE | 0 |
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

### [5] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [4] POWER_ON_SEQUENCE_CONFIG2_SWB_ENABLE

- Description: Enable Switch Node B Output Regulator.[4]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Disable Switch Node B Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Disable Switch Node B Output Regulator |
| 1 | Enable Switch Node B Output Regulator |

### [3] POWER_ON_SEQUENCE_CONFIG2_SWC_ENABLE

- Description: Enable Switch Node C Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Disable Switch Node C Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Disable Switch Node C Output Regulator |
| 1 | Enable Switch Node C Output Regulator |

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

- NOTE 1: If any regulators are enabled in Table 158, Register 0x40 [6,4:3] and Table 159, Register 0x41, [6,4:3], those regulators must be configured as ‘1’ in this sequence.
- NOTE 2: If more than one configuration register is used for power on sequence, first register must start at Table 158, Register 0x40 and it must go in sequential order to Table 160, Register 0x42, to turn on all desired regulators. In other words, there must not be any gap of the register that is used for power on sequence.
- NOTE 3: If bit [7] = ‘0’, bits [6,4:3] must be programmed as ‘000’. If bit [7] = ‘1’, at least one of the bits [6,4:3] must be programmed as ‘1’.
- NOTE 4: Only applicable if Table 173, Register 0x4F [0] = ‘0’. This bit is a don’t care when Table 173, Register 0x4F [0] = ‘1’.
- NOTE 5: Idle time is the additional time after soft-start time expires. The PMIC waits sum of Soft Start time and Idle time before it executes the next power on sequence configuration register. If more than one regulators are enabled, the PMIC uses the largest value of the soft start time among the regulators that are enabled in this configuration register.

## R43 (0x43) — Reserved

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-6 Table 161, p.171

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | RESERVED | RV | 0 |

### [7:0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

## R44 (0x44) — SWA_OUTPUT_SOFT_STOP_TIME_EXTENSION, SWB_OUTPUT_SOFT_STOP_TIME_EXTENSION, SWC_OUTPUT_SOFT_STOP_TIME_EXTENSION

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-6 Table 162, p.172

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | SWA_OUTPUT_SOFT_STOP_TIME_EXTENSION | RW | 0 |
| 6 | RESERVED | RV | 0 |
| 5 | SWB_OUTPUT_SOFT_STOP_TIME_EXTENSION | RW | 0 |
| 4 | SWC_OUTPUT_SOFT_STOP_TIME_EXTENSION | RW | 0 |
| 3:0 | RESERVED | RV | 0 |

### [7] SWA_OUTPUT_SOFT_STOP_TIME_EXTENSION

- Description: SWA Output Regulator Soft Stop Time After VR Disable[1] 3-bit encoding with {R44[7],R46[1:0]}:
- Attribute: RW — Read/Write
- Default: 0
- Note: the codes below are wider than this 1-bit field; the encoding combines bits from more than one field/register (see Description).

| Code (bin) | Meaning |
|---|---|
| 0xx | Encoding determined by R46[1:0] (Default) |
| 100 | 8 ms |
| 101 | 16 ms |
| 110 | 32 ms |
| 111 | 64 ms |

### [6] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [5] SWB_OUTPUT_SOFT_STOP_TIME_EXTENSION

- Description: SWB Output Regulator Soft Stop Time After VR Disable[1] 3-bit encoding with {R44[5],R4A[1:0]}:
- Attribute: RW — Read/Write
- Default: 0
- Note: the codes below are wider than this 1-bit field; the encoding combines bits from more than one field/register (see Description).

| Code (bin) | Meaning |
|---|---|
| 0xx | Encoding determined by R4A[1:0] (Default) |
| 100 | 8 ms |
| 101 | 16 ms |
| 110 | 32 ms |
| 111 | 64 ms |

### [4] SWC_OUTPUT_SOFT_STOP_TIME_EXTENSION

- Description: SWC Output Regulator Soft Stop Time After VR Disable[1] 3-bit encoding with {R44[4],R4C[1:0]}:
- Attribute: RW — Read/Write
- Default: 0
- Note: the codes below are wider than this 1-bit field; the encoding combines bits from more than one field/register (see Description).

| Code (bin) | Meaning |
|---|---|
| 0xx | Encoding determined by R4C[1:0] (Default) |
| 100 | 16 ms |
| 101 | 32 ms |
| 110 | 64 ms |
| 111 | Vendor-defined |

### [3:0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

**Notes**

- NOTE 1: This is the time it takes for buck regulator to go from steady state voltage to 0 V.

## R45 (0x45) — SWA_VOLTAGE_SETTING, SWA_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-6 Table 163, p.173

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:1 | SWA_VOLTAGE_SETTING | RWPE | 011 1100 |
| 0 | SWA_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING | RWPE | 0 |

### [7:1] SWA_VOLTAGE_SETTING

- Description: Switch Node A Output Regulator Voltage Setting[1]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 011 1100 → 1100 mV

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 0000000 | 0x00 | 800 mV |
| 0000001 | 0x01 | 805 mV |
| 0000010 | 0x02 | 810 mV |
| ... | ... | ... |
| 0111100 | 0x3C | 1100 mV |
| ... | ... | ... |
| 1111101 | 0x7D | 1425 mV |
| 1111110 | 0x7E | 1430 mV |
| 1111111 | 0x7F | 1435 mV |

### [0] SWA_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

- Description: Switch Node A Output Threshold Low Side Voltage For Power Good Status
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → - 5% from the setting in Table 163, Register 0x45 [7:1]
- Source correction: Field header says [1:0] but the Bits column shows [0]; the Bits column is used.

| Code (bin) | Meaning |
|---|---|
| 0 | - 5% from the setting in Table 163, Register 0x45 [7:1] |
| 1 | - 7.5% from the setting in Table 163, Register 0x45 [7:1] |

**Notes**

- NOTE 1: PMIC guarantees efficiency spec and all electrical characteristics spec within a range of 1050 mV to 1160 mV.

## R46 (0x46) — SWA_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING, SWA_OVER_VOLTAGE_THRESHOLD_SETTING, SWA_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING, SWA_OUTPUT_SOFT_STOP_TIME

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-6 Table 164, p.174

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWA_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING | RWPE | 01 |
| 5:4 | SWA_OVER_VOLTAGE_THRESHOLD_SETTING | RWPE | 10 |
| 3:2 | SWA_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING | RWPE | 00 |
| 1:0 | SWA_OUTPUT_SOFT_STOP_TIME | RWPE | 11 |

### [7:6] SWA_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING

- Description: Switch Node A Output Threshold High Side Voltage For Power Good Status
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 01 → +7.5% from the setting in Table 163, Register 0x45 [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +5% from the setting in Table 163, Register 0x45 [7:1] |
| 01 | +7.5% from the setting in Table 163, Register 0x45 [7:1] |
| 10 | +10% from the setting in Table 163, Register 0x45 [7:1] |
| 11 | Reserved |

### [5:4] SWA_OVER_VOLTAGE_THRESHOLD_SETTING

- Description: Switch Node A Output Regulator Threshold For Over Voltage Status[1]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 10 → +12.5% from the setting in Table 163, Register 0x45 [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +7.5% from the setting in Table 163, Register 0x45 [7:1] |
| 01 | +10% from the setting in Table 163, Register 0x45 [7:1] |
| 10 | +12.5% from the setting in Table 163, Register 0x45 [7:1] |
| 11 | Reserved |

### [3:2] SWA_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING

- Description: Switch Node A Output Regulator Threshold For Under Voltage Lockout Status
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 00 → -10% from the setting in Table 163, Register 0x45 [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | -10% from the setting in Table 163, Register 0x45 [7:1] |
| 01 | -12.5% from the setting in Table 163, Register 0x45 [7:1] |
| 10 | Reserved |
| 11 | Reserved |

### [1:0] SWA_OUTPUT_SOFT_STOP_TIME

- Description: SWA Output Regulator Soft Stop Time After VR Disable[2] 3
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 11 → 4 ms (Default)

| Code (bin) | Meaning |
|---|---|
| 00 | 0.5 ms |
| 01 | 1 ms |
| 10 | 2 ms |
| 11 | 4 ms (Default) |

**Notes**

- NOTE 1: The setting for the Over Voltage must be higher than Power Good High Side Voltage threshold in Table 164, Register 0x46[7:6].
- NOTE 2: This is the time it takes for buck regulator to go from steady state voltage to 0 V.
- NOTE 3: There is an extension to the SWA Soft Stop time in Table 162, Register 0x44[7].

## R47 (0x47) — Reserved

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-6 Table 165, p.174

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | RESERVED | RV | 0 |

### [7:0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

## R48 (0x48) — Reserved

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-6 Table 166, p.174

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | RESERVED | RV | 0 |

### [7:0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

## R49 (0x49) — SWB_VOLTAGE_SETTING, SWB_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-6 Table 167, p.175

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:1 | SWB_VOLTAGE_SETTING | RWPE | 011 1100 |
| 0 | SWB_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING | RWPE | 0 |

### [7:1] SWB_VOLTAGE_SETTING

- Description: Switch Node B Output Regulator Voltage Setting[1]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 011 1100 → 1100 mV

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 0000000 | 0x00 | 800 mV |
| 0000001 | 0x01 | 805 mV |
| 0000010 | 0x02 | 810 mV |
| ... | ... | ... |
| 0111100 | 0x3C | 1100 mV |
| ... | ... | ... |
| 1111101 | 0x7D | 1425 mV |
| 1111110 | 0x7E | 1430 mV |
| 1111111 | 0x7F | 1435 mV |

### [0] SWB_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

- Description: Switch Node B Output Threshold Low Side Voltage For Power Good Status
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → -5% from the setting in Table 167, Register 0x49 [7:1]

| Code (bin) | Meaning |
|---|---|
| 0 | -5% from the setting in Table 167, Register 0x49 [7:1] |
| 1 | -7.5 from the setting in Table 167, Register 0x49 [7:1] |

**Notes**

- NOTE 1: PMIC guarantees efficiency spec and all electrical characteristics spec within a range of 1050 mV to 1160 mV.

## R4A (0x4A) — SWB_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING, SWB_OVER_VOLTAGE_THRESHOLD_SETTING, SWB_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING, SWB_OUTPUT_SOFT_STOP_TIME

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-6 Table 168, p.176

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWB_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING | RWPE | 01 |
| 5:4 | SWB_OVER_VOLTAGE_THRESHOLD_SETTING | RWPE | 10 |
| 3:2 | SWB_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING | RWPE | 00 |
| 1:0 | SWB_OUTPUT_SOFT_STOP_TIME | RWPE | 11 |

### [7:6] SWB_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING

- Description: Switch Node B Output Threshold High Side Voltage For Power Good Status
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 01 → +7.5% from the setting in Table 167, Register 0x49 [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +5% from the setting in Table 167, Register 0x49 [7:1] |
| 01 | +7.5% from the setting in Table 167, Register 0x49 [7:1] |
| 10 | +10% from the setting in Table 167, Register 0x49 [7:1] |
| 11 | Reserved |

### [5:4] SWB_OVER_VOLTAGE_THRESHOLD_SETTING

- Description: Switch Node B Output Regulator Threshold For Over Voltage Status[2]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 10 → +12.5% from the setting in Table 167, Register 0x49 [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +7.5% from the setting in Table 167, Register 0x49 [7:1] |
| 01 | +10% from the setting in Table 167, Register 0x49 [7:1] |
| 10 | +12.5% from the setting in Table 167, Register 0x49 [7:1] |
| 11 | Reserved |

### [3:2] SWB_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING

- Description: Switch Node B Output Regulator Threshold For Under Voltage Lockout Status
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 00 → -10% from the setting in Table 167, Register 0x49 [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | -10% from the setting in Table 167, Register 0x49 [7:1] |
| 01 | -12.5% from the setting in Table 167, Register 0x49 [7:1] |
| 10 | Reserved |
| 11 | Reserved |

### [1:0] SWB_OUTPUT_SOFT_STOP_TIME

- Description: SWB Output Regulator Soft Stop Time After VR Disable[3] 4
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 11 → 4 ms (Default)

| Code (bin) | Meaning |
|---|---|
| 00 | 0.5 ms |
| 01 | 1 ms |
| 10 | 2 ms |
| 11 | 4 ms (Default) |

**Notes**

- NOTE 1: Only applicable if Table 173, Register 0x4F [0] = ‘0’.
- NOTE 2: The setting for the Over Voltage must be higher than Power Good High Side Voltage threshold in Table 168, Register 0x4A[7:6].
- NOTE 3: This is the time it takes for buck regulator to go from steady state voltage to 0 V.
- NOTE 4: There is an extension to the SWB Soft Stop time in Table 162, Register 0x44[5].

## R4B (0x4B) — SWC_VOLTAGE_SETTING, SWC_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-6 Table 169, p.177

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:1 | SWC_VOLTAGE_SETTING | RWPE | 011 1100 |
| 0 | SWC_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING | RWPE | 0 |

### [7:1] SWC_VOLTAGE_SETTING

- Description: Switch Node C Output Regulator Voltage Setting[2]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 011 1100 → 1800 mV

| Code (bin) | Field hex | Meaning |
|---|---|---|
| 0000000 | 0x00 | 1500 mV |
| 0000001 | 0x01 | 1505 mV |
| 0000010 | 0x02 | 1510 mV |
| ... | ... | ... |
| 0111100 | 0x3C | 1800 mV |
| ... | ... | ... |
| 1111101 | 0x7D | 2125 mV |
| 1111110 | 0x7E | 2130 mV |
| 1111111 | 0x7F | 2135 mV |

### [0] SWC_POWER_GOOD_THRESHOLD_LOW_SIDE_VOLTAGE_SETTING

- Description: Switch Node C Output Threshold Low Side Voltage For Power Good Status
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → -5% from the setting in Table 169, Register 0x4B [7:1]

| Code (bin) | Meaning |
|---|---|
| 0 | -5% from the setting in Table 169, Register 0x4B [7:1] |
| 1 | -7.5% from the setting in Table 169, Register 0x4B [7:1] |

**Notes**

- NOTE 1: Only applicable if Table 173, Register 0x4F [0] = ‘0’.
- NOTE 2: PMIC guarantees efficiency spec and all electrical characteristics spec within a range of 1750 mV to 1850 mV.

## R4C (0x4C) — SWC_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING, SWC_OVER_VOLTAGE_THRESHOLD_SETTING, SWC_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING, SWC_OUTPUT_SOFT_STOP_TIME

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-6 Table 170, p.178

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWC_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING | RWPE | 01 |
| 5:4 | SWC_OVER_VOLTAGE_THRESHOLD_SETTING | RWPE | 10 |
| 3:2 | SWC_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING | RWPE | 00 |
| 1:0 | SWC_OUTPUT_SOFT_STOP_TIME | RWPE | 11 |

### [7:6] SWC_POWER_GOOD_THRESHOLD_HIGH_SIDE_VOLTAGE_SETTING

- Description: Switch Node C Output Threshold High Side Voltage For Power Good Status
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 01 → +7.5% from the setting in Table 169, Register 0x4B [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +5% from the setting in Table 169, Register 0x4B [7:1] |
| 01 | +7.5% from the setting in Table 169, Register 0x4B [7:1] |
| 10 | Reserved |
| 11 | Reserved |

### [5:4] SWC_OVER_VOLTAGE_THRESHOLD_SETTING

- Description: Switch Node C Output Regulator Threshold For Over Voltage Status[1]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 10 → +12.5% from the setting in Table 169, Register 0x4B [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | +7.5% from the setting in Table 169, Register 0x4B [7:1] |
| 01 | +10% from the setting in Table 169, Register 0x4B [7:1] |
| 10 | +12.5% from the setting in Table 169, Register 0x4B [7:1] |
| 11 | Reserved |

### [3:2] SWC_UNDER_VOLTAGE_LOCKOUT_THRESHOLD_SETTING

- Description: Switch Node C Output Regulator Threshold For Under Voltage Lockout Status
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 00 → -10% from the setting in Table 169, Register 0x4B [7:1]

| Code (bin) | Meaning |
|---|---|
| 00 | -10% from the setting in Table 169, Register 0x4B [7:1] |
| 01 | -12.5% from the setting in Table 169, Register 0x4B [7:1] |
| 10 | Reserved |
| 11 | Reserved |

### [1:0] SWC_OUTPUT_SOFT_STOP_TIME

- Description: SWC Output Regulator Soft Stop Time After VR Disable[2] 3
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 11 → 8 ms (Default)

| Code (bin) | Meaning |
|---|---|
| 00 | 1 ms |
| 01 | 2 ms |
| 10 | 4 ms |
| 11 | 8 ms (Default) |

**Notes**

- NOTE 1: The setting for the Over Voltage must be higher than Power Good High Side Voltage threshold in Table 170, Register 0x4C[7:6].
- NOTE 2: This is the time it takes for buck regulator to go from steady state voltage to 0 V.
- NOTE 3: There is an extension to the SWC Soft Stop time in Table 162, Register 0x44[4].

## R4D (0x4D) — SWA_MODE_SELECT, SWA_SWITCHING_FREQ

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-6 Table 171, p.179

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWA_MODE_SELECT | RWPE | 10 |
| 5:4 | SWA_SWITCHING_FREQ | RWPE | 00 |
| 3:0 | RESERVED | RV | 0 |

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
| 11 | Vendor specific |

### [3:0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

## R4E (0x4E) — SWB_MODE_SELECT, SWB_SWITCHING_FREQ, SWC_MODE_SELECT, SWC_SWITCHING_FREQ

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-6 Table 172, p.179

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

- Description: Switch Node B Output Regulator Switching Frequency[1]
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

**Notes**

- NOTE 1: Only applicable if Table 173, Register 0x4F [0] = ‘0’. This bit is a don’t care when Table 173, Register 0x4F [0] = ‘1’.

## R4F (0x4F) — SWA_SWB_PHASE_MODE_SELECT

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-6 Table 173, p.180

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:1 | RESERVED | RV | 0 |
| 0 | SWA_SWB_PHASE_MODE_SELECT | RWPE | 0 |

### [7:1] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [0] SWA_SWB_PHASE_MODE_SELECT

- Description: Switch Node A and Switch Node B Phase Regulator Mode Selection.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Single Phase Regulator Mode

| Code (bin) | Meaning |
|---|---|
| 0 | Single Phase Regulator Mode |
| 1 | Dual Phase Regulator Mode |

## R50 (0x50) — SWA_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING, SWB_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING, SWC_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-6 Table 174, p.180

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | SWA_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING | RWPE | 01 |
| 5:4 | RESERVED | RV | 0 |
| 3:2 | SWB_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING | RWPE | 01 |
| 1:0 | SWC_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING | RWPE | 0 |

### [7:6] SWA_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING

- Description: Switch Node A Output Current Limiter Warning Threshold Setting For COT Mode, Ivalley_limit:
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 01 → 5.5 A

| Code (bin) | Meaning |
|---|---|
| 00 | 4.5 A |
| 01 | 5.5 A |
| 10 | 6.5 A |
| 11 | Vendor-Specific |

### [5:4] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [3:2] SWB_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING

- Description: Switch Node B Output Current Limiter Warning Threshold Setting[1] For COT Mode, Ivalley_limit:
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 01 → 5.5 A

| Code (bin) | Meaning |
|---|---|
| 00 | 4.5 A |
| 01 | 5.5 A |
| 10 | 6.5 A |
| 11 | Vendor-Specific |

### [1:0] SWC_OUTPUT_CURRENT_LIMITER_WARNING_THRESHOLD_SETTING

- Description: Switch Node C Output Current Limiter Warning Threshold Setting For COT Mode, Ivalley_limit:
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0

| Code (bin) | Meaning |
|---|---|
| 00 | 1.5 A |
| 01 | 2.0 A |
| 10 | Reserved |
| 11 | Vendor-Specific |

**Notes**

- NOTE 1: This register is applicable regardless of the setting in Table 173, Register 0x4F[0]. For dual phase operation, this register should be configured identically as Table 128, Register 0x20 [7:6].

## R51 (0x51) — VOUT_1.8V_VOLTAGE_SETTING, VOUT_1.0V_VOLTAGE_SETTING

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-6 Table 175, p.181

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:6 | VOUT_1.8V_VOLTAGE_SETTING | RWPE | 01 |
| 5:3 | RESERVED | RV | 0 |
| 2:1 | VOUT_1.0V_VOLTAGE_SETTING | RWPE | 01 |
| 0 | RESERVED | RV | 0 |

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

### [5:3] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

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

### [0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

**Notes**

- NOTE 1: The VOUT_1.8V Power Good threshold in register Table 122, Register 0x1A [2] is always fixed regardless of the setting in this register.

## R58 (0x58) — POWER_OFF_SEQUENCE_CONFIG0, POWER_OFF_SEQUENCE_CONFIG0_SWA_DISABLE, POWER_OFF_SEQUENCE_CONFIG0_SWB_DISABLE, POWER_OFF_SEQUENCE_CONFIG0_SWC_DISABLE, POWER_OFF_SEQUENCE_CONFIG0_IDLE

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-6 Table 176, p.182

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | POWER_OFF_SEQUENCE_CONFIG0 | RWPE | 0 |
| 6 | POWER_OFF_SEQUENCE_CONFIG0_SWA_DISABLE | RWPE | 0 |
| 5 | RESERVED | RV | 0 |
| 4 | POWER_OFF_SEQUENCE_CONFIG0_SWB_DISABLE | RWPE | 0 |
| 3 | POWER_OFF_SEQUENCE_CONFIG0_SWC_DISABLE | RWPE | 0 |
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

- Description: Disable Switch Node A Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Do Not Disable Switch Node A Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Disable Switch Node A Output Regulator |
| 1 | Disable Switch Node A Output Regulator |

### [5] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [4] POWER_OFF_SEQUENCE_CONFIG0_SWB_DISABLE

- Description: Disable Switch Node B Output Regulator.[3]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Do Not Disable Switch Node B Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Disable Switch Node B Output Regulator |
| 1 | Disable Switch Node B Output Regulator |

### [3] POWER_OFF_SEQUENCE_CONFIG0_SWC_DISABLE

- Description: Disable Switch Node C Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Do Not Disable Switch Node C Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Disable Switch Node C Output Regulator |
| 1 | Disable Switch Node C Output Regulator |

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

- NOTE 1: If more than one configuration register is used for power off sequence, first register must start at Table 176, Reg- ister 0x58 and it must go in sequential order to Table 178, Register 0x5A, to turn off all regulators. In other words, there must not be any gap of the register that is used for power off sequence.
- NOTE 2: If bit [7] = ‘0’, bits [6,4:3] must be programmed as ‘000’. If bit [7] = ‘1’, at least one of the bits [6,4:3] must be programmed as ‘1’.
- NOTE 3: Only applicable if Table 173, Register 0x4F [0] = ‘0’. This bit is a don’t care when Table 173, Register 0x4F [0] =’1’.
- NOTE 4: Idle time is the additional time after soft-stop time expires. The PMIC waits sum of soft stop time and idle time before it executes the next power off sequence configuration register. If more than one regulators are disabled, the PMIC uses the largest value of the soft stop time among the regulators that are disabled in this configuration register.

## R59 (0x59) — POWER_OFF_SEQUENCE_CONFIG1, POWER_OFF_SEQUENCE_CONFIG1_SWA_DISABLE, POWER_OFF_SEQUENCE_CONFIG1_SWB_DISABLE, POWER_OFF_SEQUENCE_CONFIG1_SWC_DISABLE, POWER_OFF_SEQUENCE_CONFIG1_IDLE

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-6 Table 177, p.183

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | POWER_OFF_SEQUENCE_CONFIG1 | RWPE | 0 |
| 6 | POWER_OFF_SEQUENCE_CONFIG1_SWA_DISABLE | RWPE | 0 |
| 5 | RESERVED | RV | 0 |
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
- Default: 0 → Do Not Disable Switch Node A Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Disable Switch Node A Output Regulator |
| 1 | Disable Switch Node A Output Regulator |

### [5] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [4] POWER_OFF_SEQUENCE_CONFIG1_SWB_DISABLE

- Description: Disable Switch Node B Output Regulator.[4]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Do Not Disable Switch Node B Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Disable Switch Node B Output Regulator |
| 1 | Disable Switch Node B Output Regulator |

### [3] POWER_OFF_SEQUENCE_CONFIG1_SWC_DISABLE

- Description: Disable Switch Node C Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Do Not Disable Switch Node C Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Disable Switch Node C Output Regulator |
| 1 | Disable Switch Node C Output Regulator |

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

- NOTE 1: If any regulators are disabled in Table 176, Register 0x58 [6,4:3], those regulators must be configured as ‘1’ in this sequence.
- NOTE 2: If more than one configuration register is used for power off sequence, first register must start at Table 176, Reg- ister 0x58 and it must go in sequential order to Table 178, Register 0x5A, to turn off all regulators. In other words, there must not be any gap of the register that is used for power off sequence.
- NOTE 3: If bit [7] = ‘0’, bits [6,4:3] must be programmed as ‘000’. If bit [7] = ‘1’, at least one of the bits [6,4:3] must be programmed as ‘1’.
- NOTE 4: Only applicable if Table 173, Register 0x4F [0] = ‘0’. This bit is a don’t care when Table 173, Register 0x4F [0] =’1’.
- NOTE 5: Idle time is the additional time after soft-stop time expires. The PMIC waits sum of soft stop time and idle time before it executes the next power off sequence configuration register. If more than one regulators are disabled, the PMIC uses the largest value of the soft stop time among the regulators that are disabled in this configuration register.

## R5A (0x5A) — POWER_OFF_SEQUENCE_CONFIG2, POWER_OFF_SEQUENCE_CONFIG2_SWA_DISABLE, POWER_OFF_SEQUENCE_CONFIG2_SWB_DISABLE, POWER_OFF_SEQUENCE_CONFIG2_SWC_DISABLE, POWER_OFF_SEQUENCE_CONFIG2_IDLE

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-6 Table 178, p.184

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7 | POWER_OFF_SEQUENCE_CONFIG2 | RWPE | 0 |
| 6 | POWER_OFF_SEQUENCE_CONFIG2_SWA_DISABLE | RWPE | 0 |
| 5 | RESERVED | RV | 0 |
| 4 | POWER_OFF_SEQUENCE_CONFIG2_SWB_DISABLE | RWPE | 0 |
| 3 | POWER_OFF_SEQUENCE_CONFIG2_SWC_DISABLE | RWPE | 0 |
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

- Description: Disable Switch Node A Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Do Not Disable Switch Node A Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Disable Switch Node A Output Regulator |
| 1 | Disable Switch Node A Output Regulator |

### [5] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

### [4] POWER_OFF_SEQUENCE_CONFIG2_SWB_DISABLE

- Description: Disable Switch Node B Output Regulator.[4]
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Do Not Disable Switch Node B Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Disable Switch Node B Output Regulator |
| 1 | Disable Switch Node B Output Regulator |

### [3] POWER_OFF_SEQUENCE_CONFIG2_SWC_DISABLE

- Description: Disable Switch Node C Output Regulator.
- Attribute: RWPE — Read/Write; Protected (writable only after the password is written); Persistent across power cycle, erasable by command
- Default: 0 → Do Not Disable Switch Node C Output Regulator

| Code (bin) | Meaning |
|---|---|
| 0 | Do Not Disable Switch Node C Output Regulator |
| 1 | Disable Switch Node C Output Regulator |

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

- NOTE 1: If any regulators are disabled in Table 176, Register 0x58 [6,4:3], and Table 177, Register 0x59, [6,4:3] those regulators must be configured as ‘1’ in this sequence.
- NOTE 2: If more than one configuration register is used for power off sequence, first register must start at Table 176, Reg- ister 0x58 and it must go in sequential order to Table 178, Register 0x5A, to turn off all regulators. In other words, there must not be any gap of the register that is used for power off sequence.
- NOTE 3: If bit [7] = ‘0’, bits [6,4:3] must be programmed as ‘000’. If bit [7] = ‘1’, at least one of the bits [6,4:3] must be programmed as ‘1’.
- NOTE 4: Only applicable if Table 173, Register 0x4F [0] = ‘0’. This bit is a don’t care when Table 173, Register 0x4F [0] = ‘1’.
- NOTE 5: Idle time is the additional time after soft-stop time expires. The PMIC waits sum of soft stop time and idle time before it executes the next power off sequence configuration register. If more than one regulators are disabled, the PMIC uses the largest value of the soft stop time among the regulators that are disabled in this configuration register.

## R5B (0x5B) — Reserved

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-6 Table 179, p.185

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:0 | RESERVED | RV | 0 |

### [7:0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

## R5D (0x5D) — SWA_OUTPUT_SOFT_START_TIME

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-6 Table 180, p.185

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:5 | SWA_OUTPUT_SOFT_START_TIME | RWPE | 001 |
| 4:0 | RESERVED | RV | 0 |

### [7:5] SWA_OUTPUT_SOFT_START_TIME

- Description: Switch Node A Output Regulator Soft Start Time After VR Enable[1]
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

### [4:0] RESERVED

- Description: Reserved
- Attribute: RV — Reserved (reads 0; host must not modify)
- Default: 0

**Notes**

- NOTE 1: This is the time it takes for buck regulator to go from 0 V to steady state voltage (the actual voltage varies based on pre-programmed voltage).

## R5E (0x5E) — SWB_OUTPUT_SOFT_START_TIME, SWC_OUTPUT_SOFT_START_TIME

Region: DIMM Vendor Region (NVM, password protected) | Source: JESD301-6 Table 181, p.185

| Bits | Field | Attribute | Default |
|---|---|---|---|
| 7:5 | SWB_OUTPUT_SOFT_START_TIME | RWPE | 001 |
| 4 | RESERVED | RV | 0 |
| 3:1 | SWC_OUTPUT_SOFT_START_TIME | RWPE | 001 |
| 0 | RESERVED | RV | 0 |

### [7:5] SWB_OUTPUT_SOFT_START_TIME

- Description: Switch Node B Output Regulator Soft Start Time After VR Enable[1] 2
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

- Description: Switch Node C Output Regulator Soft Start Time After VR Enable[1]
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
- NOTE 2: Only applicable if Table 173, Register 0x4F [0] = ‘0’. This bit is a don’t care when Table 173, Register 0x4F [0] = ‘1’. This page intentionally left blank Standard Improvement Form                                            JEDEC Standard JESD301-6 The purpose of this form is to provide the Technical Committees of JEDEC with input from the industry regarding usage of the subject standard. Individuals or companies are invited to submit comments to JEDEC. All comments will be collected and dispersed to the appropriate committee(s). If you can provide input, please complete this form and return to: JEDEC                                                 Email: angies@jedec.org Attn: Publications Department 3103 10th Street North Suite 240S Arlington, VA 22201 1. I recommend changes to the following: Requirement, clause number Test method number                       Clause number The referenced clause number has proven to be: Unclear          Too Rigid         In Error Other 2. Recommendations for correction: 3. Other suggestions for document improvement: Submitted by Name:                                                          Phone: Company:                                                       E-mail: Address: City/State/Zip:                                                Date:
