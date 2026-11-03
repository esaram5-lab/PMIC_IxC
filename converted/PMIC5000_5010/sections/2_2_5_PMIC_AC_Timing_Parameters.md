---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 2.2.5
title: PMIC AC Timing Parameters
pages: 11-12
---
# 2.2.5 PMIC AC Timing Parameters

**Table 14 — PMIC AC Timing Parameters**

```text
           Parameter                                   Symbol                        Min        Typ        Max        Unit      Notes
Input Supply to GSI_n assertion               tInput_PWR_GOOD_GSI_
                                                                                                            10         μs
                                                      Assertion
Input over voltage condition to
                                    tInput_OV_GSI_Assertion                            -          -         10         μs
GSI_n assertion
Input over voltage condition to
                                       tInput_OV_VR_Disable                            -          -         20         μs
automatic PMIC VR Disable
```

Output Voltage Tolerance to GSI_n tOutput_PWR_GOOD_GSI_

```text
                                                                                       -          -         10         μs
assertion                                      Assertion
Output over voltage condition to
                                     tOutput_OV_VR_Disable                             -          -         20         μs
automatic PMIC VR Disable
Output under voltage lockout
condition to automatic PMIC VR       tOutput_UV_VR_Disable                             -          -         20         μs
Disable
Output current limiter Warning to
                                      tOutput_Current_Limiter                          -          -         10         μs
GSI_n assertion
High Temperature Warning to
                                        tHigh_Temp_Warning                             -          -         10         μs
GSI_n assertion
Critical Temperature condition to
                                          tShut_Down_Temp                              -          -         10         μs
automatic PMIC shut down
VIN_Mgmt input supply stable to
                                       tVIN_Mgmt_to_Enable                            6.5         -          -         ms

VR Enable Command
VIN_Bulk input supply stable to
                                        tVIN_Bulk_to_Enable                           6.5         -          -         ms
VR Enable Command

VIN_Mgmt input supply stable to
                                             t1.8V_Ready                               -          -         3.5        ms

VOUT_1.8V output stable
VOUT_1.8V output supply stable
                                             t1.0V_Ready                               -          -         1.0        ms          1
to VOUT_1.0V output stable
VOUT_1.8V output supply to
                                         tManagement_Ready                             -          -          3         ms
PMIC Management Ready
VR Enable Command to PMIC
                                      tPMIC_PWR_Good_Out                                                               ms
output regulator ready                                                                       Figure 15
VR Disable Command to PMIC
                                          tPMIC_Output_Off                                   Figure 16                 ms
Output Regulators Off
CAMP Input Low Pulse Width         tCAMP_Low_Pulse_Width                               2                               μs
CAMP Input Low Pulse Width        tCAMP_Low_Pulse_Width_
                                                                                       -          -        0.35        μs
Input Filter                                     Filter
Output Voltage Adjustment in non
                                                 Δv/Δt                                 -          1          -       mV/μs         2
write protect mode
NOTE 1 This time is added to t_1.8V_Ready parameter to get total time from VIN_Mgmt input supply.
NOTE 2 See footnote 4 for registers Table 123, “Register 0x21” [7:1], Table 125, “Register 0x23” [7:1], Table 127, “Register 0x25” [7:1],
       and Table 129, “Register 0x27” [7:1]. The accuracy is + 10%
```
