---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 2.2.3
title: Switch Regulator Efficiency
pages: 9-10
---
# 2.2.3 Switch Regulator Efficiency

**Table 11 — Efficiency Characteristics; PMIC5000**

```text
                                                                   Efficiency (% of Max Itdc Load)               Unit           Notes
                   Switch Node Output
                                                                      25%            50%           100%
SWA or SWB (Single Phase Regulator Mode)                              > 87           > 92           > 89          %
SWA + SWB (Dual Phase Regulator Mode)                                 > 87           > 92           > 89          %          1,2,3,4,5,
SWC                                                                   > 87           > 92           > 89          %          6,7,8,9,10
SWD                                                                   > 87           > 92           > 89          %
NOTE 1 VIN_Bulk = 12 V; VIN_Mgmt = 3.3 V
NOTE 2 The maximum Itdc as specified in appropriate Tables above.
NOTE 3 When the efficiency of any given output regulator is being measured, all other switching output regulators are disabled.
NOTE 4 No external load on VOUT_1.8V, VOUT_1.0V LDO is applied.
NOTE 5 I2C/I3C Basic bus is pulled High and held static. CAMP and GSI_n signals are pulled High and held static.
NOTE 6 The efficiency includes the buck regulator loss, the PCB loss (< 2.5 mΩ) and see clause 2.12 for inductor specification assumption
        for DCR and ACR.
NOTE 7 Efficiency calculation equation: (VOUT * IOUT) / [(VIN_Bulk * IVIN_Bulk) + (VIN_Mgmt * IIN_Mgmt)]; where VOUT, IOUT, VIN_Mgmt,
        IIN_Mgmt, VIN_Bulk, IVIN_Bulk parameters are actual measured values.
NOTE 8 Applies at maximum ambient temperature of 65 0C (PMIC Junction temperature of 105 0C). The inductor characteristics noted
        above applies inductor temperature of 105 0C.
NOTE 9 The output buck regulator switching frequency can be set to anywhere within 500 KHz to 1000 KHz. For all efficiency qualification
        testing, the device under test (DUT) must also comply with all PMIC’s electrical characteristics (DC+AC) specifications.
NOTE 10 For input supply rails, probing is done at the input high frequency filter cap (0.1uF) to PMIC pin. For output rail, probing is done
          at the output cap location at the inductor load side.
```

**Table 12 — Efficiency Characteristics; PMIC5010**

```text
                                                                   Efficiency (% of Max Itdc Load)               Unit           Notes
                   Switch Node Output

                                                                      25%            50%           100%
SWA or SWB (Single Phase Regulator Mode)                              > 85           > 90           > 87          %
SWA + SWB (Dual Phase Regulator Mode)                                 > 85           > 90           > 87          %          1,2,3,4,5,
SWC                                                                   > 85           > 90           > 87          %          6,7,8,9,10
SWD                                                                   > 85           > 90           > 87          %
NOTE 1 VIN_Bulk = 12 V; VIN_Mgmt = 3.3 V
NOTE 2 The maximum Itdc as specified in appropriate Tables above.
NOTE 3 When the efficiency of any given output regulator is being measured, all other switching output regulators are disabled.
NOTE 4 No external load on VOUT_1.8 V, VOUT_1.0 V LDO is applied.
NOTE 5 I2C/I3C Basic bus is pulled High and held static. CAMP and GSI_n signals are pulled High and held static.
NOTE 6 The efficiency includes the buck regulator loss, the PCB loss (< 2.5 mΩ) and see clause 2.12 for inductor specification.assumption
        for DCR and ACR.
NOTE 7 Efficiency calculation equation: (VOUT * IOUT) / [(VIN_Bulk * IVIN_Bulk) + (VIN_Mgmt * IIN_Mgmt)]; where VOUT, IOUT, VIN_Mgmt,
        IIN_Mgmt, VIN_Bulk, IVIN_Bulk parameters are actual measured values.
NOTE 8 Applies at maximum ambient temperature of 65 0C (PMIC Junction temperature of 105 0C). The inductor characteristics noted
        above applies inductor temperature of 105 0C.
NOTE 9 The output buck regulator switching frequency can be set to anywhere within 500 KHz to 1000 KHz. For all efficiency qualification
        testing, the device under test (DUT) must also comply with all PMIC’s electrical characteristics (DC+AC) specifications.
NOTE 10 For input supply rails, probing is done at the input high frequency filter cap (0.1 uF) to PMIC pin. For output rail, probing is done
          at the output cap location at the inductor load side.
```
