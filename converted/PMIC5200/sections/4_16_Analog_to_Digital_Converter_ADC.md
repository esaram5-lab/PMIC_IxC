---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 4.16
title: Analog to Digital Converter (ADC)
pages: 68-70
---
# 4.16 Analog to Digital Converter (ADC)

The PMIC supports analog to digital converter (ADC) to monitor input supply voltages (VIN_Bulk), as well as output voltage regulator voltage (SWA, SWD, SWB, SWC, VOUT_1.8V, and VOUT_1.0V). The register Table 152, Register 0x30 [7:3] allows to enable the ADC and select the input supply voltage or desired output supply voltage. The register Table 153, Register 0x31 [7:0] provides the actual voltage measurement. The accuracy of the voltage measurement is shown in Table 30 and Table 31.

**Table 30 — PMIC Output Voltage ADC Accuracy**

```text
                                                                                           1.8V LDO
   Output Regulator; Voltage Range         SWA         SWD          SWB         SWC                      VBIAS
                                                                                           1.0V LDO

1050 mV to 1160 mV                        + 1 LSB       N/A         N/A          N/A          N/A         N/A

Less than 1050 mV; greater than 1160 mV   + 3 LSB       N/A         N/A          N/a          N/A         N/A

                                                                                                      1.8V LDO
   Output Regulator; Voltage Range               SWA            SWD         SWB              SWC                   VBIAS
                                                                                                      1.0V LDO

850 mV to 950 mV                                  N/A          + 1 LSB       N/A             N/A        N/A         N/A

Less than 850 mV; greater than 950 mV             N/A          + 3 LSB       N/A             N/A        N/A         N/A

450 mV to 550 mV                                  N/A           N/A        + 3 LSB           N/A        N/A         N/A

Less than 450 mV; greater than 550 mV             N/A           N/A        + 5 LSB           N/A        N/A         N/A

1750 mV to 1850 mV                                N/A           N/A          N/A         + 1 LSB        N/A         N/A

Less than 1750 mV; greater than 1850 mV           N/A           N/A          N/A         + 3 LSB        N/A         N/A

1.8V LDO, 1.0V LDO                                N/A           N/A          N/A             N/A      + 3 LSB       N/A

VBIAS                                             N/A           N/A          N/A             N/A        N/A        + 6 LSB
```

**Table 31 — PMIC Input Voltage ADC Accuracy**

```text
             Input Voltage
VIN_Bulk                                      + 6 LSB
```

The PMIC also monitors output voltage regulator current or power for SWA, SWD, SWB and SWC. The

PMIC updates registers Table 116, Register 0x0C [7:0] to Table 119, Register 0x0F [7:0] for SWA to SWD respectively if Table 154, Register 0x32 [1:0] = ‘00’ or Table 168, Register 0x100 [7:0] to Table 172,

Register 0x105 [7:0] for SWA to SWD respectively if Table 154, Register 0x32 [1:0] = ‘01’. The register Table 131, Register 0x1B [6] allows host to select whether PMIC should report current measurements or power measurements. The current or power measurement reported in these registers are an average measurement over vendor specific time period. If Table 131, Register 0x1B [6] = ‘1’, the register Table 130, Register 0x1A [1] allows host to select whether PMIC should report individual rail power or total power in Table 116, Register 0x0C [7:0] if Table 154, Register 0x32 [1:0] = ‘00’ or in Table 169, Register 0x102 [7:0] if Table 154, Register 0x32 [1:0] = ‘01’. The register update frequency of this register is configured in Table 152, Register 0x30 [1:0]. The internal sampling rate of the PMIC is vendor specific.

**Table 32 — PMIC ADC Current and Power Accuracy; R32[1:0] = 00**

```text
                                                                      SWA to SWD Rails -
                                            SWA to SWD Rails -
           Load Current                                              Corresponding Power       Total Power Accuracy
                                             Current Accuracy
                                                                           Accuracy

Less than 0.5 A                                  + 4 LSB                   + 7 LSB                  + 12 LSB

Greater than or equal to 0.5 A                   + 3 LSB                   + 6 LSB
```

**Table 33 — PMIC ADC Current and Power Accuracy; R32[1:0] = 01**

```text
                                                               SWA to SWD Rails -
                                     SWA to SWD Rails -
           Load Current                                       Corresponding Power   Total Power Accuracy
                                      Current Accuracy
                                                                    Accuracy

Less than 0.5 A                           + 9 LSB                  + 15 LSB               + 25 LSB

Greater than or equal to 0.5 A            + 8 LSB                  + 12 LSB
```
