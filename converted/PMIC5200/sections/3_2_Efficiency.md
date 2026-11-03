---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 3.2
title: Efficiency
pages: 11-13
---
# 3.2 Efficiency

The PMIC5200 efficiency spec is defined for the reference test board only and it is not applicable for any CAMM2 application board which varies from the reference test board. The reference test board includes the inductor and the PCB characteristics which complies with the footnote 1 in Table 9/Table 10. The efficiency spec is only measured for one switch regulator at a time; all other switch regulators must be disabled. The PMIC switching frequency must comply with the footnote 9 in Table 9/Table 10. The typical CAMM2 application environment which deviates from the reference test board, all buck regulators are turned on simultaneously, carries external load on LDOs and signal interface pins may not be held static will have lower efficiency than defined in Table 9/Table 10. The combination of all variation for application environment is not subject to the efficiency spec as defined in Table 9/Table 10.

## 3.2.1 VIN_Bulk = 5.0 V

**Table 9 — Efficiency Characteristics; VIN_Bulk = 5.0V[1]**

```text
                                                     Efficiency (% of Max Itdc Load)                       Unit           Notes

       Switch Node Output                  15%       20%        25%        50%        75%       100%

 SWA                                       > 85      > 86       > 86       > 88       > 84       > 82       %       [2],[3],[4],[5],[6],[7],
                                                                                                                      [8],[9],[10].[11]
 SWD                                       > 84      > 86       > 87       > 87       > 87       > 85       %
 SWB; Vout = 0.5V                          > 77      > 79       > 80       > 84       > 82       > 79       %

 SWB; Vout = 0.3V                          > 68      > 70       > 73       > 79       > 77       > 74       %

 SWC                                       > 86      > 88       > 90       > 89       > 87       > 85       %

NOTE 1    The efficiency numbers assume the inductor specification as noted in Section 7.2.
NOTE 2    The maximum Itdc as specified in Table 4 to Table 7 appropriately.

NOTE 3    When the efficiency of any given output regulator is being measured, all other switching output regulators are
          disabled.
NOTE 4    No external load on VOUT_1.8V, VOUT_1.0V LDO is applied.
NOTE 5    I2C/I3C Basic bus is pulled High and held static. PWR_GOOD signal is pulled High and held static.
NOTE 6    The efficiency includes the buck regulator loss, the PCB loss (< 2.5 mΩ from the SWx output pin of the PMIC to
          VOUTx bulk capacitors after inductor).
NOTE 7    Efficiency calculation equation: (VOUT * IOUT) / [(VIN_Bulk * IVIN_Bulk)+(VIN * IVIN)]; where VOUT, IOUT, VIN_Bulk, IVIN_Bulk,
           VIN, IVIN parameters are actual measured values.
NOTE 8    Applies at maximum ambient temperature of 65 0C (PMIC Junction temperature less than or equal to 105 0C). The
          inductor characteristics noted above applies inductor temperature of 105 0C.
NOTE 9    The output buck regulator switching frequency is set to 750 KHz for SWA/SWB/SWC/SWD. The device under test
          (DUT) must also comply with all PMIC’s electrical characteristics (DC+AC) specifications. The efficiency spec for
          switching frequency greater or different than 750 KHz for SWA/SWB/SWC/SWD is not specified and it is vendor
          specific.
NOTE 10     For input supply rail, probing is done at the input high frequency filter cap (0.1 μF) to PMIC pin. For output rail,
            probing is done at the output cap location at the inductor load side.
NOTE 11     Acoustic noise prevention control feature is disabled by setting Table 158, “Register 0x36” [3:1] = ‘000’.
```

## 3.2.2 VIN_Bulk = 3.3 V

**Table 10 — Efficiency Characteristics; VIN_Bulk = 3.3V[1]**

```text
                                                     Efficiency (% of Max Itdc Load)                       Unit           Notes

       Switch Node Output                  15%       20%        25%        50%        75%       100%

 SWA                                       > 86      > 87       > 86       > 86       > 81       > 78       %       [2],[3],[4],[5],[6],[7],
                                                                                                                      [8],[9],[10].[11]
 SWD                                       > 84      > 86       > 87       > 85       > 83       > 80       %

 SWB; Vout = 0.5V                          > 77      > 82       > 83       > 85       > 81       > 79       %

 SWB; Vout = 0.3V                          > 67      > 70       > 72       > 79       > 76       > 72       %

 SWC                                       > 87      > 89       > 90       > 89       > 84       > 83       %
NOTE 1    The efficiency numbers assume the inductor specification as noted in Section 7.2.
NOTE 2    The maximum Itdc as specified in Table 4 to Table 7 appropriately.
NOTE 3    When the efficiency of any given output regulator is being measured, all other switching output regulators are
          disabled.
NOTE 4    No external load on VOUT_1.8V, VOUT_1.0V LDO is applied.
NOTE 5    I2C/I3C Basic bus is pulled High and held static. PWR_GOOD signal is pulled High and held static.
NOTE 6    The efficiency includes the buck regulator loss, the PCB loss (< 2.5 mΩ from the SWx output pin of the PMIC to
          VOUTx bulk capacitors after inductor).
NOTE 7    Efficiency calculation equation: (VOUT * IOUT) / [(VIN_Bulk * IVIN_Bulk)+(VIN * IVIN)]; where VOUT, IOUT, VIN_Bulk, IVIN_Bulk,
           VIN, IVIN parameters are actual measured values.

NOTE 8    Applies at maximum ambient temperature of 65 0C (PMIC Junction temperature less than or equal to 105 0C). The
          inductor characteristics noted above applies inductor temperature of 105 0C.

NOTE 9    The output buck regulator switching frequency is set to 750 KHz. for SWA/SWB/SWC/SWD. The device under test
          (DUT) must also comply with all PMIC’s electrical characteristics (DC+AC) specifications. The efficiency spec for

          switching frequency greater or different than 750 KHz for SWA/SWB/SWC/SWD is not specified and it is vendor
          specific.
NOTE 10     For input supply rail, probing is done at the input high frequency filter cap (0.1 µF) to PMIC pin. For output rail,
            probing is done at the output cap location at the inductor load side.
NOTE 11     Acoustic noise prevention control feature is disabled by setting Table 158, “Register 0x36” [3:1] = ‘000’.
```
