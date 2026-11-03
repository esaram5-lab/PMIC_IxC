---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 6.26
title: Analog to Digital Converter (ADC)
pages: 56-58
---
# 6.26 Analog to Digital Converter (ADC)

The PMIC supports analog to digital converter (ADC) to monitor input supply voltages (VIN_Bulk and VIN_Mgmt) as well as output voltage regulator voltage (SWA, SWB, SWC, SWD, SWE, SWF, VBias1 or VBias2, VOUT_1.8V and VOUT_1.0V). The register Table 153, Register 0x30 [7:3] allows to enable the ADC and select the desired input supply voltage or output supply voltage. The register Table 154, Register 0x31 [7:0] provides the actual voltage measurement. The accuracy of the voltage measurement is shown in Table 30 and Table 31.

**Table 30 — PMIC Output ADC Voltage Accuracy**

```text
                                             SWA, SWB,                               1.8V LDO            VBIAS1 or
   Output Regulator: Voltage Range         SWC, SWE, SWF            SWD              1.0V LDO             VBIAS2
1050mV to 1160mV                               + 1 LSB               N/A                N/A                 N/A
Less than 1050mV; greater than 1160mV          + 3 LSB               N/A                N/A                 N/A
1750mV to 1850mV                                 N/A               + 1 LSB              N/A                 N/A
Less than 1750mV; greater than 1850mV            N/A               + 3 LSB              N/A                 N/A
1.8V LDO, 1.0V LDO                               N/A                 N/A              + 3 LSB               N/A
VBIAS1 or VBIAS2 LDO                             N/A                 N/A                N/A               + 6 LSB
```

**Table 31 — PMIC Input ADC Voltage Accuracy**

```text
              Input Voltage

VIN_Bulk                                               + 6 LSB

VIN_Mgmt                                               + 6 LSB
```

The PMIC also monitors output voltage regulator current or power for SWA, SWB, SWC, SWD, SWE and SWF. The PMIC updates registers Table 117, Register 0x0C [7:0] to Table 120, Register 0x0F [7:0] for SWA to SWD respectively if Table 155, Register 0x32 [1:0] = ‘00’ or register Table 167, Register 0x100 [7:0] to Table 174, Register 0x107 [7:0] for SWA to SWF respectively if Table 155, Register 0x32 [1:0] = ‘01’. The register Table 132, Register 0x1B [6] allows host to select whether PMIC should report current measurements or power measurements. The current or power measurement reported in this registers are an average measurement over vendor specific time period. If Table 132, Register 0x1B [6] = ‘1’, the register Table 131, Register 0x1A [1] allows host to select whether PMIC should report individual rail power or total power in Table 117, Register 0x0C [7:0] if Table 155, Register 0x32 [1:0] = ‘00’ or in Table 168, Register 0x101 [2:0] and Table 169, Register 0x102 [7:0] if Table 155, Register 0x32 [1:0] = ‘01’. The register update frequency of this register is configured in Table 153, Register 0x30 [1:0]. The internal sampling rate of the PMIC is vendor specific. The accuracy of the current or power measurement is shown in Table 32 and Table 33 depending on the setting of Table 155, Register 0x32 [1:0].

**Table 32 — PMIC ADC Current and Power Accuracy; R32[1:0] = 00**

```text
                                                                          SWA to SWD Rails -

                                        SWA to SWD Rails -               Corresponding Power
         Load Current                   Current Accuracy[1]                   Accuracy[1]                 Total Power Accuracy

Less than 0.5A                                  + 4 LSB                          + 7 LSB                          + 12 LSB

Greater than or equal to 0.5A                   + 3 LSB                          + 6 LSB
 NOTE 1     These specs are per rail only.
```

**Table 33 — PMIC ADC Current and Power Accuracy; R32[1:0] = 01**

```text
                                                                          SWA to SWF Rails -
                                        SWA to SWF Rails -               Corresponding Power
         Load Current                   Current Accuracy[1]                   Accuracy[1]                 Total Power Accuracy

Less than 0.5A                                  + 9 LSB                         + 15 LSB                         + 25 LSB[2]

Greater than or equal to 0.5A                   + 8 LSB                         + 12 LSB
 NOTE 1     These specs are per rail only.
 NOTE 2     This accuracy is guaranteed if the total power is less than or equal to 23 W. If the total power is greater than 23 W, the
            accuracy is + 5% of total power.
```
