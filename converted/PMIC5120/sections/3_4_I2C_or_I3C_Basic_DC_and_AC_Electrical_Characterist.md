---
document: JESD301-6 (PMIC5120 Power Management IC Standard, Version 1.0, February 2025)
device: PMIC5120
application: client
section: 3.4
title: I2C or I3C Basic DC and AC Electrical Characteristics
pages: 13-18
---
# 3.4 I2C or I3C Basic DC and AC Electrical Characteristics

**Table 8 — I2C, I3C Basic and Logic Interface DC Electrical Specification**

```text
                      Parameter                                  Symbol             Min            Max        Unit   Notes
Input Low Voltage (PWR_GOOD, SDA, SCL, VR_EN)                      VIL              -0.3           0.3         V
Input High Voltage (SDA, SCL)                                      VIH              0.7            3.6         V
Input High Voltage (PWR_GOOD, VR_EN)                                                1.26           3.6         V
Output Low Voltage (SDA)                                                              -            0.3         V       1
                                                                   VOL
Output Low Voltage (PWR_GOOD, GSI_n)                                                 -              0.3        V      1 2

Output High Voltage (SDA)                                          VOH              0.75             -         V       3
Output Low Current (SDA)                                                             3               -        mA       4
                                                                   IOL
Output Low Current (PWR_GOOD, GSI_n)                                                 3               -        mA       4

Output High Current (SDA)                                          IOH                              -3        mA       5
Rising Output Slew Rate (SDA)                                                       0.1              1        V/ns     6
                                                               Slew_Rate
Falling Output Slew Rate (SDA)                                                      0.1              3        V/ns
Input Leakage Current                                              ILI               -              ±5        μA
Output Leakage Current                                             ILO               -              ±5        μA
NOTE 1     3 mA sink current.
NOTE 2     PWR_GOOD, GSI_n output is Open Drain output. There is an external pullup resistor to 1.8 V or 3.3 V on the board
           or other device.
NOTE 3     3 mA source current.
NOTE 4     VOL = 0.3 V.
NOTE 5     VOH = VDDIO - 0.3 V.

NOTE 6     Output slew rate is guaranteed by design and/or characterization. The output slew rate reference load is shown in
           Figure 9 and Figure 10 shows the timing measurement points. For slew rate measurement, the VOH level shown in
           Figure 10 is a function of Ron value; VOH = {1.0/(Ron + 50)} * 50.
```

**Table 9 — Input Capacitance Spec**

```text
                     Parameter                                   Symbol             Min            Max        Unit   Notes
Input Capacitance (PWR_GOOD, SCL, SDA, VR_EN)                      CIN               -              5          pF
```

**Table 10 — Input Spike Filter Spec**

```text
             Parameter                     Symbol          Test Condition                  Min      Max       Unit   Notes
Pulse width of spikes which must be                   Single glitch, f < 100 KHz            -        -         ns
suppressed by the input filter in I2C         tSP                                                                      1
                                                      Single glitch, f > 100 KHz            0            50    ns
mode
NOTE 1     TA = 25 °C; f = 400 KHz. Verified by design and characterization only.
```

**Table 11 — Output Ron**

```text
                     Parameter                                   Symbol             Min            Max        Unit   Notes
SDA Output Pullup and Pulldown Driver Impedance                                     20             100         Ω       1
                                                                   RON
GSI_n, PWR_GOOD Output Pulldown Driver Impedance                                    20             100         Ω       2

NOTE 1     Pulldown Ron = Vout/Iout. Pullup Ron = (VOUT_1.0V - Vout)/Iout.
NOTE 2     Pulldown Ron = Vout/Iout
```

**Table 12 — I2C and I3C Interface AC Characteristics**

```text
                                                                I2C Mode -   I3C Basic Mode
                                                                Open Drain     Push-Pull1
                 Parameter                       Symbol         Min    Max    Min    Max      Unit   Notes
Clock Frequency                                   fSCL          0.01    1     0.01   12.5     MHz
Clock High Pulse Width Time                       tHigh         260            35              ns
Clock Low Pulse Width Time                        tLow          500            35              ns
Detect Clock Input Low Time                       tTIMEOUT       10     50     10     50      ms
Rise Time                                               tR        -    120      -     5        ns      2,3
Fall time                                                tF       -    120     0      5        ns      2,3
Data in Setup Time                                  tSU:DAT      50      -     8       -       ns      2,4
Data in Hold Time                                     tHD:DI     0       -     3       -       ns      2,4
Start Condition Setup Time                          tSU:STA     260      -     12      -       ns       2
Start Condition Hold Time                           tHD:STA     260      -     30      -       ns       2
Stop Condition Setup Time                           tSU:STO     260      -     12      -       ns       2
```

Time between Stop Condition and next Start

```text
                                                       tBUF     500     -     500      -       ns      2,5
Condition
SDA Data Out Hold Time                             tHD:DAT      0.5    350    N/A    N/A       ns       6
```

SCL Falling Clock In to Valid SDA Data Out

```text
                                                      tDOUT     N/A    N/A     0.5    12       ns      7,8

Time
```

SCL Rising Clock In to Target SDA Output

```text
                                                     tDOFFT     N/A    N/A     0.5    12       ns      8,9
Off

SCL Rising Clock In to Controller SDA
                                                    tDOFFC      N/A    N/A     0.5    30       ns      8,10
Output Off
```

SCL Rising Clock In to Controller Driving

```text
                                                 tCL_r_DAT_f    N/A    N/A     40      -       ns      11
Data Signal Low
```

Bus Available Time (no edges seen on SCL

```text
                                                      tAVAL     N/A    N/A     1       -       μs
and SDA)
```

Time to issue IBI after an event is detected

```text
                                                  tIBI_ISSUE    N/A    N/A      -     15       μs
when Bus is available
```

Time from Clear Register Status to any I3C

```text
Basic operation with Start condition to avoid                   N/A    N/A     4       -       μs
false IBI generation; PEC disabled            tCLR_I3C_CMD_
Time from Clear Register Status to any I3C             Delay
Basic operation with Start condition to avoid                   N/A    N/A     15      -       μs
false IBI generation; PEC enabled
DEVCTRL CCC Followed by DEVCTRL               tDEVCTRLCCC_                                           12,13,14
                                                                 3      -      3       -       μs
```

CCC or Register Read/Write Command Delay DELAY_PEC_DIS Register Write Command Followed by

```text
                                              tWR_RD_DELAY                                           15,16,17
Register Read Command Delay in PEC                              N/A    N/A     8       -       μs
                                                   _PEC_EN
Enabled Mode
SETHID CCC or SETAASA CCC followed
                                              t
by any other CCC or Read/Write Command I2C_CCC_Update           2.5     -     N/A    N/A       μs
                                                      _Delay
Delay
RSTDAA CCC or ENEC CCC or DISEC
                                              tI3C_CCC_Update
CCC to any other CCC or Read/Write                               -      -      2.5     -       μs
                                                      _Delay
Command Delay

                                                                      I2C Mode -        I3C Basic Mode
                                                                      Open Drain          Push-Pull1
              Parameter                               Symbol          Min       Max       Min       Max       Unit     Notes
Any CCC followed by RSTDAA CCC Delay                tCCC_Delay        N/A       N/A       2.5        -         μs
NOTE 1    I3C Basic mode with Open Drain operation follows timing values as shown in I2C Mode - Open Drain column.
NOTE 2    See Figure 6 for PMIC’s input timing definition.
NOTE 3    See Figure 11 for voltage threshold definition for rise and fall times.
NOTE 4    The input setup time is referenced from SDA VIL or VIH threshold as shown in Figure 6 to SCL VIH threshold as
          shown in Figure 6. The input hold time is referenced from SCL VIL threshold as shown in Figure 6 to SDA VIL or
          VIH threshold as shown in Figure 6.
NOTE 5    If PEC is enabled, tWR_RD_DELAY_PEC_EN timing parameter applies.
NOTE 6    The PMIC device guarantees tHD:DAT value in I2C mode of operation. See Figure 8 for PMIC’s output timing
          definitions as well as SCL clock input threshold level and SDA data output threshold levels.
NOTE 7    The PMIC device must be configured in I3C Basic mode to guarantee tDOUTvalue. See Figure 7 for PMIC’s output
          timing definition as well as SCL clock input threshold level and SDA data output threshold levels.
NOTE 8    This timing parameter is guaranteed into output timing reference load as shown in Figure 9.
NOTE 9    The PMIC device must be configured in I3C Basic mode to guarantee tDOFFT value. See Figure 34.
NOTE 10     The PMIC device must be configured in I3C Basic mode to guarantee tDOFFC value. See Figure 35.
NOTE 11     See Figure 37.
NOTE 12     From STOP condition of DEVCTRL CCC to START condition for Register Read or Register Write Command Data
          Packet delay.
NOTE 13     The PMIC sends NACK if Host does not satisfy tDEVCTRLCCC_DELAY_PEC_DIS timing parameter.
NOTE 14     This timing parameter restriction is only applicable when PEC function is disabled in PMIC. If PEC is enabled, this
          timing parameter does not apply.
NOTE 15     From STOP condition for Register Write Command Data Packet to START condition for Register Read Command

          Data Packet delay.
NOTE 16     This timing parameter restriction is only applicable when PEC function is enabled in PMIC. If PEC is disabled, this

          timing parameter does not apply.
NOTE 17     The PMIC sends NACK if Host does not satisfy tWR_RD_DELAY_PEC_EN timing parameter.
```

The PMIC device follows the I2C bus and I3C Basic bus input timing requirements as shown in Figure 6 and Table 12 and output timing requirement as shown in Figure 7.

```text
                                        tR                   tHIGH
                                                tHD:DI
            P     S              tLOW                                                        Sr                                        P
 SCL
  VIHmin
  VILmax

                                                         tSU:DAT     tF         tSU:DAT           tSU:STA                    tSU:STO
                       tHD:STA
 VIHmin
 VILmax
SDA
                tBUF
```

*Figure 6 — I2C or I3C Basic Bus AC Input Timing Parameter Definition* (figure; any text below/above was extracted from the drawing)

```text
                                 tDOUT                                                          tDOUT
SCL
                                                                                                              VIHmin

                                                                                                              VILmax

                                                                              ng                              VOHmin
                                                       ACK
SDA
                                                                                                              VOLmax
```

*Figure 7 — I3C Basic Bus AC Data Output Timing Parameter Definition* (figure; any text below/above was extracted from the drawing)

```text
                                       tHD:DAT                                                      tHD:DAT
SCL
                                                                                                              VIHmin

                                                                                                              VILmax

                                                       ACK                                                    VOHmin
SDA
                                                                                                              VOLmax
```

*Figure 8 — I2C Bus AC Data Output Timing Parameter Definition* (figure; any text below/above was extracted from the drawing)

```text
                50 Ohm
SDA
SCL
        5 mm
```

*Figure 9 — Output Slew Rate and Output Timing Reference Load* (figure; any text below/above was extracted from the drawing)

```text
                         Delta tF
                                                       Delta tR
SDA                                                                          VOH
                                                                             70%*VOH

                                                                             30%*VOH
                                                       VOL
```

*Figure 10 — Output Slew Rate Measurement Points* (figure; any text below/above was extracted from the drawing)

```text
                          I2C                                                   I3C
                         tF                                                        tF
SCL,                                                      SCL,
SDA                                                       SDA

                                               0.7 V                                              0.7 V

                                               0.3 V                                              0.3 V

                             I2 C                                               I3C
                        tR                                                         tR

                                               0.7 V                                              0.7 V

                                               0.3 V                                              0.3 V
    SCL,                                                   SCL,
    SDA                                                    SDA
```

*Figure 11 — Input Rise and Fall Timing Parameter Definition* (figure; any text below/above was extracted from the drawing)
