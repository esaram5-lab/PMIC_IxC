---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 5.1.3
title: Switch Regulator Efficiency
pages: 14-15
---
# 5.1.3 Switch Regulator Efficiency

The PMIC5030 efficiency spec is defined for the reference test board only and it is not applicable for any application board which varies from the reference test board. The reference test board includes the inductor and the PCB characteristics which complies with the footnote 1 in Table 10. The efficiency spec is only measured for one switch regulator at a time; all other switch regulators must be disabled. The PMIC switching frequency must comply with the footnote 9 in Table 10. The typical application environment which deviates from the reference test board, all buck regulator are turned on simultaneously, carries external load on LDOs and signal interface pins may not be held static will have lower efficiency than defined in Table 10. The combination of all variations for application environment is not subject to the efficiency spec as defined in Table 10.

**Table 10 — Efficiency Characteristics**

```text
                                                             Efficiency (% of Max Itdc Load)           Unit           Notes

               Switch Node Output                              25%           50%          100%

SWA or SWB or SWC or SWE or SWF                                > 87          > 91         > 89          %       [1],[2],[3],[4],[5],[6]
                                                                                                                  ,[7],[8],[9],[10]
(Single Phase Regulator Mode)

SWA + SWB or SWC + SWF                                         > 87          > 91         > 89          %
(Dual Phase Regulator Mode)
SWA + SWB + SWE                                                > 87          > 91         > 89
(Three Phase Regulator Mode_

SWD                                                            > 87          > 92         > 89          %
 NOTE 1     VIN_Bulk = 12 V; VIN_Mgmt = 3.3 V

 NOTE 2     The maximum Itdc as specified in appropriate Tables above.
 NOTE 3     When the efficiency of any given output regulator is being measured, all other switching output regulators are

            disabled.
  NOTE 4    No external load on VOUT_1.8V, VOUT_1.0V LDO is applied.
  NOTE 5    I2C/I3C Basic bus is pulled High and held static. CAMP and GSI_n signals are pulled High and held static.
  NOTE 6    The efficiency includes the buck regulator loss, the PCB loss (< 2.5 mΩ) and see Section 9 for inductor specification
            for DCR and ACR.
  NOTE 7    Efficiency calculation equation: (VOUT * IOUT) / [(VIN_Bulk * IVIN_Bulk) + (VIN_Mgmt * IIN_Mgmt)]; where VOUT, IOUT,
            VIN_Mgmt, IIN_Mgmt, VIN_Bulk, IVIN_Bulk parameters are actual measured values.
 NOTE 8     Applies at maximum ambient temperature of 65 0C (PMIC Junction temperature of 105 0C). The inductor
            characteristics noted above applies inductor temperature of 105 0C.
 NOTE 9     The output buck regulator switching frequency must be set to 500 KHz. For all efficiency qualification testing, the
            device under test (DUT) must also comply with all PMIC’s electrical characteristics (DC+AC) specifications.
 NOTE 10    For input supply rails, probing is done at the input high frequency filter cap (0.1 µF) to PMIC pin. For output rail,
            probing is done at the output cap location at the inductor load side.
```
