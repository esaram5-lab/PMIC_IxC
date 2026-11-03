---
document: JESD301-2 (PMIC5100 Power Management IC Standard, Rev. 1.03, October 2022)
device: PMIC5100
application: client
section: 6.11
title: Analog to Digital Converter (ADC)
pages: 60-61
---
# 6.11 Analog to Digital Converter (ADC)

The PMIC supports analog to digital converter (ADC) to monitor input supply voltages (VIN_Bulk) as well as output voltage regulator voltage (SWA, SWB, SWC, VOUT_1.8V and VOUT_1.0V). The register Table 136, “Register 0x30” [7:3] allows to enable the ADC and select the input supply voltage or desired output supply voltage. The register Table 137, “Register 0x31” [7:0] provides the actual voltage measurement. The accuracy of the voltage measurement is as following:

```text
• Switch Output Voltage Regulator SWA, SWB (Output Voltage Range: 1050 mV to 1160 mV): + 1 LSB
• Switch Output Voltage Regulator SWA, SWB (Output Voltage Range outside of 1050 mV to 1160 mV): + 3

  LSB
• Switch Output Voltage Regulator SWD (Output Voltage Range: 1750 mV to 1850 mV): + 1 LSB

• Switch Output Voltage Regulator SWD (Output Voltage Range outside of 1750 mV to 1850 mV): + 3 LSB
• VOUT_1.8V, VOUT_1.0V Output Voltage: + 3 LSB
• VIN_Bulk Input Voltage: + 6 LSB
```

If register Table 114, “Register 0x1A” [1] = ‘1’, the accuracy of total power reported in register Table 100, “Register 0x0C” = + 12 LSB. The PMIC also monitors output voltage regulator current or power (SWA, SWB and SWC) and updates registers Table 100, “Register 0x0C” [7:0] for SWA, Table 102, “Register 0x0E” [5:0] for SWB and Table 103, “Register 0x0F” [5:0] for SWC. The register Table 115, “Register 0x1B” [6] allows host to select whether PMIC should report current measurements or power measurements. The current or power measurement reported in this registers are an average measurement over time period defined in register Table 136, “Register 0x30” [1:0]. If Table 115, “Register 0x1B” [6] = ‘1’, the register Table 114, “Register 0x1A” [1] allows host to select whether PMIC should report individual rail power or total power in Table 100, “Register 0x0C” [7:0]. The register update frequency of this register is configured in Table 136, “Register 0x30” [1:0]. The internal sampling rate of the PMIC is vendor specific. The accuracy of the current (> 0.5 A) or corresponding power measurement is + 3 LSB or + 6 LSB respectively. The accuracy of the current measurement (< 0.5 A) is + 4 LSB or corresponding power measurement is + 7 LSB, respectively.
