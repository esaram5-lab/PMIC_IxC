---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 5.1.5
title: PMIC AC Timing Parameters
pages: 16-17
---
# 5.1.5 PMIC AC Timing Parameters

**Table 12 — PMIC AC Timing Parameters**

```text
              Parameter                                      Symbol                        Min       Typ       Max       Unit      Notes
Input Supply to GSI_n assertion               tInput_PWR_GOOD_GSI_Assertion                                     10         μs
Input over voltage condition to GSI_n
                                                   tInput_OV_GSI_Assertion                  -          -        10         μs
assertion
Input over voltage condition to
                                                     tInput_OV_VR_Disable                   -          -        20         μs
automatic PMIC VR Disable
Output Voltage Tolerance to GSI_n
                                             tOutput_PWR_GOOD_GSI_Assertion                 -          -        10         μs
assertion
Output over voltage condition to
                                                    tOutput_OV_VR_Disable                   -          -        20        μs
automatic PMIC VR Disable
Output under voltage lockout condition
                                                    tOutput_UV_VR_Disable                   -          -        20        μs
to automatic PMIC VR Disable
Output current limiter Warning to GSI_n
                                                    tOutput_Current_Limiter                 -          -        10        μs
assertion
High Temperature Warning to GSI_n
                                                      tHigh_Temp_Warning                    -          -        10        μs
assertion
Critical Temperature condition to
                                                       tShut_Down_Temp                      -          -        10        μs
automatic PMIC shut down
VIN_Mgmt input supply stable to VR

                                                     tVIN_Mgmt_to_Enable                   6.5         -         -        ms
Enable Command
VIN_Bulk input supply stable to VR

                                                      tVIN_Bulk_to_Enable                  6.5         -         -        ms
Enable Command

VIN_Mgmt input supply stable to
                                                          t1.8V_Ready                       -          -        3.5       ms
VOUT_1.8V output stable
VOUT_1.8V output supply stable to                                                                                                    [1]
                                                          t1.0V_Ready                       -          -        1.0       ms
VOUT_1.0V output stable
VOUT_1.8V output supply to PMIC
                                                      tManagement_Ready                     -          -         3        ms
Management Ready
VR Enable Command to PMIC output
                                                    tPMIC_PWR_Good_Out                            Figure 16               ms
regulator ready
VR Disable Command to PMIC Output
                                                       tPMIC_Output_Off                           Figure 20               ms
Regulators Off
CAMP Input Low Pulse Width                         tCAMP_Low_Pulse_Width                    2                              μs
CAMP Input Low Pulse Width Input
                                                tCAMP_Low_Pulse_Width_Filter                -          -       0.35        μs
Filter
VR_OE Input High/Low Pulse Width               tVR_OE_High_Low_Pulse_Width                  2                              μs
VR_OE Input High/Low Pulse Width             tVR_OE_High_Low_Pulse_Width_Filt
                                                                                            -          -       0.35        μs
Filter                                                     er
Output Voltage Adjustment in non-write-                                                                                              [2]
                                                              Δv/Δt                         -         1          -      mV/μs
protect mode
 NOTE 1      This time is added to t_1.8V_Ready parameter to get total time from VIN_Mgmt input supply.
 NOTE 2      See footnote 4 for registers Table 138, Register 0x21 [7:1], Table 140, Register 0x23 [7:1], Table 142, Register 0x25 [7:1],
             Table 144, Register 0x27 [7:1]. The accuracy is + 10%.
```
