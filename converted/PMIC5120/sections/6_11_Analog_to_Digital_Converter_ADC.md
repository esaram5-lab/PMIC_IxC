---
document: JESD301-6 (PMIC5120 Power Management IC Standard, Version 1.0, February 2025)
device: PMIC5120
application: client
section: 6.11
title: Analog to Digital Converter (ADC)
pages: 63-64
---
# 6.11 Analog to Digital Converter (ADC)

The PMIC supports analog to digital converter (ADC) to monitor input supply voltages (VIN_Bulk) as well as output voltage regulator voltage (SWA, SWB, SWC, VOUT_1.8V and VOUT_1.0V). Register 0x30 [7:3] allows to enable the ADC and select the desired input supply voltage or desired output supply voltage. Register 0x31 [7:0] provides the actual voltage measurement. The accuracy of the voltage measurement is as following:

```text
• Switch Output Voltage Regulator SWA, SWB (Output Voltage Range: 1050 mV to 1160 mV): + 1 LSB
• Switch Output Voltage Regulator SWA, SWB (Output Voltage Range outside of 1050 mV to 1160 mV): +
  3 LSB

 • Switch Output Voltage Regulator SWC (Output Voltage Range: 1750 mV to 1850 mV): + 1 LSB
 • Switch Output Voltage Regulator SWC (Output Voltage Range outside of 1750 mV to 1850 mV): + 3 LSB
 • VOUT_1.8V, VOUT_1.0V Output Voltage: + 3 LSB
 • VIN_Bulk Input Voltage: + 6 LSB
```

The PMIC also monitors output voltage regulator current or power (SWA, SWB, and SWC) and updates Register 0x0C [7:0] for SWA, Register 0x0E [7:0] for SWB, and Register 0x0F [7:0] for SWC. Register 0x1B [6] allows the host to select whether the PMIC should report current measurements or power measurements. The current or power measurement reported in this registers are an average measurement over time period defined in Register 0x30 [1:0]. If Register 0x1B [6] = ‘1’, Register 0x1A [1] allows host to select whether PMIC should report individual rail power or total power in Register 0x0C [7:0]. The register update frequency of this register is configured in Register 0x30 [1:0]. The internal sampling rate of the PMIC is vendor specific. Register 0x32 [1:0] allows the user to change the LSB step size for current or power measurements.

**Table 33 — PMIC ADC Current and Power Accuracy; R32[1:0] = 00**

```text
                                                                     SWA to SWC Rails -
                                      SWA to SWC Rails -                                               Total Power
      Load Current                                                   Corresponding Power
                                       Current Accuracy                                                 Accuracy
                                                                           Accuracy
       Less than 0.5A                       ±4 LSB                              ±7 LSB
                                                                                                           ±12 LSB
Greater than or equal to 0.5A               ±3 LSB                              ±6 LSB
```

**Table 34 — PMIC ADC Current and Power Accuracy; R32[1:0] = 01**

```text
                                                                          SWA to SWC Rails -
                                           SWA to SWC Rails -                                               Total Power
           Load Current                                                   Corresponding Power
                                            Current Accuracy                                                 Accuracy
                                                                                Accuracy
            Less than 0.5A                       ±9 LSB                             ±18 LSB
                                                                                                                 N/A1
     Greater than or equal to 0.5A               ±8 LSB                             ±16 LSB
NOTE 1       Register 0x32 [1:0] must be set to 00 when Register 0x1A [1] = 1.
```
