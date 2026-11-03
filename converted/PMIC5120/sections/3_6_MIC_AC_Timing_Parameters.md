---
document: JESD301-6 (PMIC5120 Power Management IC Standard, Version 1.0, February 2025)
device: PMIC5120
application: client
section: 3.6
title: MIC AC Timing Parameters
pages: 18-19
---
# 3.6 MIC AC Timing Parameters

**Table 14 — PMIC AC Timing Parameters**

```text
           Parameter                               Symbol                      Min            Typ    Max      Unit   Notes
Input Supply to GSI_n assertion         tInput_PWR_GOOD_GSI_Asserti
                                                                                                      10       μs
                                                     on
Input over voltage condition to
                                     tInput_OV_GSI_Assertion                       -           -      10       μs
GSI_n assertion
Input over voltage condition to
                                        tInput_OV_VR_Disable                       -           -      20       μs
automatic PMIC VR Disable
```

Output Voltage Tolerance to GSI_n tOutput_PWR_GOOD_GSI_Asser

```text
                                                                                   -           -      10       μs
assertion                                         tion
Output over voltage condition to
                                      tOutput_OV_VR_Disable                        -           -      20       μs
automatic PMIC VR Disable
Output under voltage lockout
condition to automatic PMIC VR        tOutput_UV_VR_Disable                        -           -      20       μs
Disable
Output current limiter Warning to
                                       tOutput_Current_Limiter                     -           -      10       μs
GSI_n assertion
High Temperature Warning to
                                         tHigh_Temp_Warning                        -           -      10       μs
GSI_n assertion
Critical Temperature condition to
                                           tShut_Down_Temp                         -           -      10       μs
automatic PMIC shut down
VIN_Bulk input supply stable to
                                     tVIN_Bulk_to_VR_Enable                       6.5          -          -   ms
VR Enable Command
VIN_Bulk input supply stable to
                                              t1.8V_Ready                          -           -      2.5     ms
VOUT_1.8V output stable

             Parameter                               Symbol                     Min       Typ         Max     Unit     Notes
VOUT_1.8V output supply stable                                                                                              1
                                                  t1.0V_Ready                     -         -         1.0      ms
to VOUT_1.0V output stable
VOUT_1.8V output supply to
                                             tManagement_Ready                    -         -          3       ms
PMIC Management Ready
VR Enable Command to PMIC
                                           tPMIC_PWR_Good_Out                          Figure 23               ms
output regulator ready
VR Disable Command to PMIC
                                              tPMIC_Output_Off                         Figure 25               ms
Output Regulators Off
PWR_GOOD Input Low Pulse
                                      tPWR_GOOD_Low_Pulse_Width                   2         0          0       μs
Width
PWR_GOOD Input Low Pulse              tPWR_GOOD_Low_Pulse_Width
                                                                                  -         -         0.35     μs
Width Input Filter                               _Filter
VR_EN_Input High Pulse Width             tVR_EN_High_Pulse_Width                  2         0          0       μs
VR_EN Input High Pulse Width            tVR_EN_High_Pulse_Width_
                                                                                  -         -         0.35     μs
Input Filter                                     Filter
Output Voltage Adjustment in                                                                                                2
                                                      Δv/Δt                       -         1          -     mV/μs
Programmable Mode
NOTE 1    This time is added to t1.8V_Ready parameter to get total time from VIN_Bulk input supply.
NOTE 2    See footnote 4 for registers Table 129, Register 0x21, [7:1], Table 133, Register 0x25, [7:1] and Table 135, Register
          0x27, [7:1]. The accuracy is + 10%.
```
