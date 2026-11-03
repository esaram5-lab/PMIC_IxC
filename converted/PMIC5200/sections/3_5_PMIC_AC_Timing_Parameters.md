---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 3.5
title: PMIC AC Timing Parameters
pages: 18-22
---
# 3.5 PMIC AC Timing Parameters

**Table 17 — PMIC Timing Parameters**

```text
              Parameter                                         Symbol                    Min      Typ             Max       Unit   Notes

Input Supply to GSI_n assertion               tInput_PWR_GOOD_GSI_Assertion                -           -           10        μs

Input supply over voltage condition to              tInput_OV_GSI_Assertion                -           -           10        μs
GSI_n assertion

Input over voltage condition to                      tInput_OV_VR_Disable                  -           -           20        μs
automatic PMIC VR Disable

Output Voltage Tolerance to GSI_n            tOutput_PWR_GOOD_GSI_Assertion                -           -           10        μs
assertion

Output over voltage condition to                    tOutput_OV_VR_Disable                  -           -           20        μs
automatic PMIC VR Disable

Output under voltage lockout condition              tOutput_UV_VR_Disable                  -           -           20        μs
to automatic PMIC VR Disable

Output current limiter warning to GSI_n              tOutput_Current_Limiter               -           -           10        μs
assertion

              Parameter                               Symbol                Min      Typ       Max    Unit    Notes

High temperature warning to GSI_n               tHigh_Temp_Warning           -         -       10      μs
assertion

Critical Temperature condition to                tShut_Down_Temp             -         -       10      μs
automatic PMIC shut down

VIN_Bulk input supply stable to VR            tVIN_Bulk_to_VR_Enable        6.5        -        -      ms
Enable Command

VIN_Bulk input supply stable to                     t1.8V_Ready              -         -       2.5     ms
VOUT_1.8V output stable

VOUT_1.8V output supply stable to                   t1.0V_Ready              -         -       1.0     ms       [1]
VOUT_1.0V output stable

VOUT_1.8V output supply to PMIC                 tManagement_Ready            -         -        3      ms
Management Ready

VR Enable Command to PMIC output               tPMIC_PWR_Good_Out                                      ms
regulator ready                                                                    Figure 15

VR Disable Command to PMIC Output                tPMIC_Output_Off                  Figure 21           ms
Regulators Off
PWR_GOOD, Unlock Input Low Pulse           tPWR_GOOD_Low_Pulse_Width         2         -        -      μs
Width

Minimum DVFSQ_n Input High or Input            tHigh_Pulse:DVFSQ_n           5         -        -      μs
                                                                                                              [2],[3]
Low Pulse Width                                 tLow_Pulse:DVFSQ_n

PWR_GOOD, Unlock, DVFSQ_n, Input         tPWR_GOOD_Low_Pulse_Width_Filter    -         -       0.35    μs

Low Pulse Width Input Filter

VR_EN Input High Pulse Width                 tVR_EN_High_Pulse_Width         2                         μs

VR_EN Input High Pulse Width Input         tVR_EN_High_Pulse_Width_Filter    -         -       0.35    μs
Filter

Output Voltage Adjustment in                           Δv/Δt                 -        1         -     mV/μs     [4]
Programmable Mode

PMIC Delay from DVFSQ_n input signal         tDelay_DVFSQ_HI_VSLEW           -         -        5      μs
reaching High threshold until SWB                                                                               [5]
output voltage begins to slew high

PMIC Delay from DVFSQ_n input signal         tDelay_DVFSQ_LO_VSLEW           -         -        5      μs
reaching Low threshold until SWB                                                                                [5]
output voltage begins to slew low

SWB output voltage slew rate upon          DVFSQ_VOLTAGE_SLEW_RATE          -10                +10    mV/μs    [5],
entry and exit from DVFSQ state                                                                               [6],[7],
                                                                                                                [8]

SWB_Disable setup time prior to               tSU:SWB_Disable_VR_EN         10         -        -      μs
VR_EN Pin Assertion to High

SWB_Disable hold time after VR_EN             tHD:SWB_Disable_VR_EN         10         -        -      μs
Pin Assertion to High

Unlock setup time prior to VR_EN                     tSU:Unlock             10         -        -      μs
assertion or I2C/I3C Bus command

              Parameter                                        Symbol                          Min        Typ       Max        Unit     Notes

 Unlock hold time after VR_EN assertion                       tHD:Unlock                        10         -          -         μs
 or I2C/I3C Bus command

 Minimum Unlock InputHigh or Input Low                   tHigh_Pulse:Unlock                     20                              μs
                                                                                                                                          [9]
 time pulse width                                        tLow_Pulse:Unlcok
NOTE 1   This time is added to t1.8V_Ready parameter to get total time from VIN_Bulk input supply.
NOTE 2   The controller is not permitted to change the status of the DVFSQ_n input signal while the SWB output voltage is slewing. The
         controller must assert the DVFSQ_n input signal longer than the sum of PMIC slew delay and the SWB output voltage transition
         time which is defined by the equation: tSignal_to_slew_delay + {SWB_Voltage_Setting -
         SWB_DVFSQ_Voltage_Setting}/0.9*SWB_DVFSQ_Voltage_Slew_Rate
NOTE 3   See Figure 10
NOTE 4   See footnote 4 for registers Table 137, “Register 0x21,” [7:1], Table 139, “Register 0x23,” [7:1], Table 141, “Register 0x25,” [7:1],
         and Table 143, “Register 0x27,” [7:1]. The accuracy is + 10%.
NOTE 5   See Figure 11
NOTE 6   Typical value as configured in Table 150, “Register 0x2E” [7:6].
NOTE 7   The SWB DVFSQ slew rate is measured from 20% to 80% of the output voltage swing as shown in Figure 11.
NOTE 8   During SWB output voltage transitions, once the output voltage crosses the programmed value, the output voltage must reside within
         the SWB output voltage tolerance limits.
NOTE 9   See Figure 12
```

*Figure 10 — DVFSQ_n Pin Minimum High and Low Pulse Width* (figure; any text below/above was extracted from the drawing)

*Figure 11 — Delay from DVFSQ_n Pin to SWB Output Regulator Begins to Slew* (figure; any text below/above was extracted from the drawing)

*Figure 12 — Unlock Pin Minimum High and Low Pulse Width* (figure; any text below/above was extracted from the drawing)
