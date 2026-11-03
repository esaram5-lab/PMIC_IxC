---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 2.8
title: Analog to Digital Converter (ADC)
pages: 45-46
---
# 2.8 Analog to Digital Converter (ADC)

The PMIC supports analog to digital converter (ADC) to monitor input supply voltages (VIN_Bulk and VIN_Mgmt) as well as output voltage regulator voltage (SWA, SWB, SWC, SWD, VBias, VOUT_1.8V and VOUT_1.0V). The register Table 138, “Register 0x30” [7:3] allows to enable the ADC and select the desire input supply voltage or output supply voltage. The register Table 139, “Register 0x31” [7:0] provides the actual voltage measurement. The accuracy of the voltage measurement is as following:

```text
• Switch Output Voltage Regulator SWA, SWB, SWC (Output Voltage Range: 1050 mV to 1160 mV): + 1 LSB
• Switch Output Voltage Regulator SWA, SWB, SWC (Output Voltage Range outside of 1050 mV to 1160
  mV): + 3 LSB
• Switch Output Voltage Regulator SWD (Output Voltage Range: 1750 mV to 1850 mV): + 1 LSB
• Switch Output Voltage Regulator SWD (Output Voltage Range outside of 1750 mV to 1850 mV): + 3 LSB
• VOUT_1.8V, VOUT_1.0V: + 3 LSB
• VBias Output Voltage, VIN_Bulk, VIN_Mgmt Input Voltage: + 6 LSB
```

The PMIC also monitors output voltage regulator current or power (SWA, SWB, SWC and SWD) and updates registers Table 102, “Register 0x0C” [7:0] for SWA, Table 103, “Register 0x0D” [5:0] for SWB, Table 104, “Register 0x0E” [5:0] for SWC and Table 105, “Register 0x0F” [5:0] for SWD. The register Table 117, “Register 0x1B” [6] allows host to select whether PMIC should report current measurements or power measurements. The current or power measurement reported in this registers are an average measurement over time period defined in register Table 138, “Register 0x30” [1:0]. If Table 117, “Register 0x1B” [6] = ‘1’, the register Table 116, “Register 0x1A” [1] allows host to select whether PMIC should report individual rail power or total power in Table 102, “Register 0x0C” [7:0]. The register update frequency of this register is configured in Table 138, “Register 0x30” [1:0]. The internal sampling rate of the PMIC is vendor specific. The accuracy of the current (> 0.5 A) or corresponding power measurement is + 3 LSB or + 6 LSB respectively. The accuracy of the current measurement (< 0.5 A) is + 4 LSB or corresponding power measurement is + 7 LSB, respectively.

If register Table 116, “Register 0x1A” [1] = ‘1’, the accuracy of total power reported in register Table 102, “Register 0x0C” = + 12 LSB.

## 2.8.1 PMIC Address ID (PID)

The PMIC has PID input pin which allows to assign up to three different unique ID for I2C and I3C Basic protocol. The PID input pin is shared with SWD_FB_N pin. At first power on, when VIN_Mgmt input is applied, the PMIC automatically senses its ID. The PMIC also checks the configuration register Table 166, “Register 0x4F” [1]. If SWD output regulator is enabled and intended to operate in a single ended remote sensing mode, the PMIC offers three different ID as shown in Table 30. If SWD output regulator is not enabled, the PMIC still offers three different ID as shown in Table 30. If SWD output regulator is enabled and intended to operate in a differential remote sensing mode, there is only one default ID for the PMIC as shown in Table 30. This means, there can be only one PMIC on the DIMM (or I2C and I3C Basic bus).

**Table 30 — PMIC ID**

```text
R4F [1] =       PID Pin Connection on DIMM Board              PMIC ID                     Comment
                              short to GND                    PID = 1001            PMIC can be configured
   ‘0’                          Floating                      PID = 1000
                               short to 1.8                   PID = 1100      Connected to PMIC’s VOUT_1.8V Rail
   ‘1’             Connect to Differential Sensing GND        PID = 1001            SWD differential sensing
```

## 2.8.2 Error Injection

The PMIC offers error injection function for the purpose of debug, test and validation at various stages. Error Injection Function Usage prior to VR Enable:

```text
• Prior to VR Enable command, the Error injection function may be invoked by setting error injection enable bit
  Table 143, “Register 0x35” [7] = ‘1’ during the configuration state. If any of either VIN_Bulk UV/OV or SWx
  OV/UV or Critical Temp Shutdown error is injected prior to VR Enable command, the PMIC shall not execute
  power on sequence and shall not enable PMIC output regulators when PMIC receives VR Enable command.
  The PMIC shall not update error log registers (Table 94, “Register 0x04” to Table 96, “Register 0x06”). The
  PMIC shall update appropriate status registers accordingly when error is injected.
```

Error Injection Function Usage after VR Enable:

```text
• After PMIC output regulators are enabled with VR Enable command and PMIC is in non write protect mode,
  the error injection function may be invoked by setting error injection enable bit Table 143, “Register 0x35” [7]
  = ‘1’. If any of either VIN_Bulk UV/OV or SWx OV/UV or Critical Temp Shutdown error is injected the
  PMIC shall execute Power Off Sequence to disable PMIC output regulators and shall update the error log
  registers (Table 94, “Register 0x04” to Table 96, “Register 0x06”) as well as status registers accordingly. Note
  that if any of the output rails are not enabled through power on sequence configuration registers, the error
  injection on that output rail does not apply.
• After PMIC output regulators are enabled with VR Enable command and PMIC is in write protect mode, the
  error injection enabling Table 143, “Register 0x35” [7] = ‘1’ is disallowed. The PMIC shall ignore any
  attempts to inject any error and shall not execute Power Off Sequence to disable PMIC output regulators and
  shall not update any error log or status registers.
```

To exit the error injection function, the host shall power cycle VIN_Bulk and VIN_Mgmt input supply.
