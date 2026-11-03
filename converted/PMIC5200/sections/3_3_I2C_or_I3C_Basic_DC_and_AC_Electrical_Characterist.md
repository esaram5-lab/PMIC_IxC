---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 3.3
title: I2C or I3C Basic DC and AC Electrical Characteristics
pages: 13-18
---
# 3.3 I2C or I3C Basic DC and AC Electrical Characteristics

**Table 11 — I2C, I3C Basic and Logic Interface DC Electrical Specification**

```text
                          Parameter                                 Symbol            Min            Max          Unit     Notes

 Input Low Voltage (PWR_GOOD, SDA, SCL, VR_EN,                         VIL            -0.3            0.3           V
 Unlock, DVFSQ_n, SWB_Disable)

 Input High Voltage (SDA, SCL)                                         VIH            0.7             3.6           V

 Input High Voltage (PWR_GOOD, VR_EN, Unlock,                                         1.26            3.6           V
 DVFSQ_n,)

 Input High Voltage (SWB_Disable)                                                     1.26            5.5           V

 Output Low Voltage (SDA)                                             VOL               -             0.3           V

 Output Low Voltage (PWR_GOOD, GSI_n)                                                   -             0.3           V         [1]

 Output High Voltage (SDA)                                            VOH             0.75             -            V

 Output Low Current (SDA)                                              IOL             3               -           mA

 Output Low Current (PWR_GOOD, GSI_n)                               ng                 3               -           mA

 Output High Current (SDA)                                             IOH              -             -3           mA

 Rising Output Slew Rate (SDA)                                     Slew_Rate          0.1              1          V/ns        [2]

 Falling Output Slew Rate (SDA)                                                       0.1              3          V/ns

 Input Leakage Current                                                 ILI              -             +5           μA

 Output Leakage Current                                                ILO              -             +5           μA

NOTE 1   PWR_GOOD output is Open Drain output. There is an external pullup resistor to 1.8 V or 3.3 V on the board or other device.
NOTE 2   Output slew rate is guaranteed by design and/or characterization. The output slew rate reference load is shown in Figure 6.
         Figure 7 shows the timing measurement points. For slew rate measurement, the VOH level shown in Figure 7 is a function
         of Ron value; VOH = {1.0/(Ron + 50)} * 50.
```

**Table 12 — Input Capacitance**

```text
                         Parameter                                 Symbol            Min            Max          Unit     Notes

Input Capacitance (PWR_GOOD, SCL, SDA, VR_EN,                         CIN              -              5           pF
Unlock, DVFSQ_n, SWB_Disable)
```

**Table 13 — Input Spike Filter**

```text
                                                Symb
               Parameter                                        Test Condition              Min       Max        Unit     Notes
                                                  ol

Pulse width of spikes which must be               tSP      Single glitch, f < 100 KHz         -            -      ns
```

suppressed by the input filter in I2C mode

```text
                                                            Single glitch, f > 100 KHz         -           50      ns         [1]

NOTE 1    TA = 25 0C; f = 400 KHz. Verified by design and characterization only.
```

**Table 14 — Output Ron**

```text
                           Parameter                                 Symbol         Min         Max          Unit        Notes
 SDA Output Pullup and Pulldown Driver Impedance                       RON          20          100           Ω           [1]

 GSI_n, PWR_GOOD Output Pulldown Driver Impedance                                   20          100           Ω           [2]

NOTE 1     Pulldown Ron = Vout/Iout. Pullup Ron = (VOUT_1.0V - Vout)/Iout.
NOTE 2     Pulldown Ron = Vout/Iout
```

**Table 15 — I2C and I3C Interface AC Characteristics**

```text
                                                                                              I3C Basic
                                                                                I2C Mode -      Mode
                     Parameter                               Symbol             Open Drain   Push-Pull[1]           Unit      Notes

                                                                       ng      Min     Max   Min        Max

Clock Frequency                                                fSCL            0.01     1    0.01       12.5        MHz

Clock High Pulse Width Time                                    tHigh           260           35                     ns

Clock Low Pulse Width Time                                     tLow            500           35                     ns

Detect Clock Input Low Time                                 tTIMEOUT            10     50    10         50          ms

Rise Time                                                       tR               -     120    -          5          ns            [2],[3]

Fall time                                                       tF               -     120    0          5          ns             2,3

Data in Setup Time                                           tSU:DAT            50      -     8          -          ns            2,[4]

Data in Hold Time                                             tHD:DI            0       -     3          -          ns             2,4

Start Condition Setup Time                                   tSU:STA           260      -    12          -          ns              2

Start Condition Hold Time                                    tHD:STA           260      -    30          -          ns              2

Stop Condition Setup Time                                    tSU:STO           260      -    12          -          ns              2

Time between Stop Condition and next Start Condition           tBUF            500      -    500         -          ns            2,[5]

SDA Data Out Hold Time                                       tHD:DAT            0.5    350   N/A        N/A         ns             [6]

SCL Falling Clock In to Valid SDA Data Out Time               tDOUT            N/A     N/A   0.5        12          ns            [7],[8]

SCL Rising Clock In to Target SDA Output Off                 tDOFFT            N/A     N/A   0.5        12          ns            8,[9]

SCL Rising Clock In to Controller SDA Output Off             tDOFFC            N/A     N/A   0.5        30          ns            8,[10]

SCL Rising Clock In to Controller Driving Data Signal      tCL_r_DAT_f         N/A     N/A   40          -          ns             [11]
Low

Bus Available Time (no edges seen on SCL and SDA)             tAVAL            N/A     N/A    1          -          μs

Time to issue IBI after an event is detected when Bus       tIBI_ISSUE         N/A     N/A    -         15          μs
is available

                                                                                                          I3C Basic
                                                                                    I2C Mode -              Mode
                        Parameter                                  Symbol           Open Drain           Push-Pull[1]        Unit     Notes

                                                                                   Min       Max        Min       Max

 Time from Clear Register Status to any I3C operation           tCLR_I3C_CMD_      N/A        N/A         4         -         μs
 with Start condition to avoid false IBI generation; PEC             Delay
 disabled

 Time from Clear Register Status to any I3C operation                              N/A        N/A        15         -         μs
```

with Start condition to avoid false IBI generation; PEC enabled

```text
 DEVCTRL CCC Followed by DEVCTRL CCC or                         tDEVCTRLCCC_         3         -          3         -         μs      [12],[13]
 Register Read/Write Command Delay                                                                                                      ,[14]
                                                                DELAY_PEC_DIS

 Register Write Command Followed by Register Read               tWR_RD_DELAY       N/A        N/A         8         -         μs      [15],[16]
 Command Delay in PEC Enabled Mode                                                                                                      ,[17]
                                                                   _PEC_EN

 SETHID CCC or SETAASA CCC followed by any other                tI2C_CCC_Updat      2.5        -        N/A        N/A        μs
 CCC or Read/Write Command Delay                                    e_Delay

 RSTDAA CCC or ENEC CCC or DISEC CCC to any                     tI3C_CCC_Updat       -         -         2.5        -         μs
 other CCC or Read/Write Command Delay                              e_Delay

 Any CCC followed by RSTDAA CCC Delay                             tCCC_Delay       N/A        N/A        2.5        -         μs

NOTE 1    I3C Basic mode with Open Drain operation follows timing values as shown in I2C Mode - Open Drain column.
NOTE 2    See Figure 3 for PMIC’s input timing definition.

NOTE 3    See Figure 8 for voltage threshold definition for rise and fall times.
NOTE 4    The input setup time is referenced from SDA VIL or VIH threshold as shown in Figure 3 to SCL VIH threshold as shown in Figure 3.

          The input hold time is referenced from SCL VIL threshold as shown in Figure 3 to SDA VIL or VIH threshold as shown in Figure 3.
NOTE 5    If PEC is enabled, tWR_RD_DELAY_PEC_EN timing parameter applies.
NOTE 6    The PMIC device guarantees tHD:DAT value in I2C mode of operation. See Figure 5 for PMIC’s output timing definitions as well as
          SCL clock input threshold level and SDA data output threshold levels.
NOTE 7    The PMIC device must be configured in I3C Basic mode to guarantee tDOUT value. See Figure 4 for PMIC’s output timing definition
          as well as SCL clock input threshold level and SDA data output threshold levels.
NOTE 8    This timing parameter is guaranteed into output timing reference load as shown in Figure 6.
NOTE 9    The PMIC device must be configured in I3C Basic mode to guarantee tDOFFT value. See Figure 32.
NOTE 10    The PMIC device must be configured in I3C Basic mode to guarantee tDOFFC value. See Figure 33.
NOTE 11    See Figure 34.
NOTE 12    From STOP condition of DEVCTRL CCC to START condition for Register Read or Register Write Command Data Packet delay.
NOTE 13    The PMIC sends NACK if Host does not satisfy tDEVCTRLCCC_DELAY_PEC_DIS timing parameter.
NOTE 14   This timing parameter restriction is only applicable when PEC function is disabled in PMIC. If PEC is enabled, this timing parameter
          does not apply.
NOTE 15    From STOP condition for Register Write Command Data Packet to START condition for Register Read Command Data Packet
           delay.
NOTE 16    This timing parameter restriction is only applicable when PEC function is enabled in PMIC. If PEC is disabled, this timing parameter
           does not apply.
NOTE 17    The PMIC sends NACK if Host does not satisfy tWR_RD_DELAY_PEC_EN timing parameter.
```

The PMIC follows the I2C bus and I3C Basic bus input timing requirements as shown in Figure 3 and Table 15 and output timing requirement as shown in Figure 4.

```text
                                        tR                 tHIGH
                                              tHD:DI
          P     S                tLOW                                              Sr                                           P
SCL
 VIHmin
 VILmax

                                                       tSU:DAT     tF   tSU:DAT         tSU:STA                       tSU:STO
                       tHD:STA
 VIHmin
 VILmax
SDA
              tBUF
```

*Figure 3 — I2C or I3C Basic Bus AC Input Timing Parameter Definition* (figure; any text below/above was extracted from the drawing)

```text
                         tDOUT                                          tDOUT
 SCL
                                                              ng                         VIHmin

                                                                                         VILmax

                                             ACK                                        VOHmin

SDA
                                                                                        VOLmax
```

*Figure 4 — I3C Basic Bus AC Output Timing Parameter Definition* (figure; any text below/above was extracted from the drawing)

```text
                                   tHD:DAT                                        tHD:DAT
 SCL
                                                                                            VIHmin

                                                                                            VILmax

                                                 ACK                                        VOHmin
SDA
                                                                                            VOLmax
```

*Figure 5 — I2C Bus AC Output Timing Parameter Definition* (figure; any text below/above was extracted from the drawing)

```text
                50 Ohm
SDA
SCL
         5 mm
```

*Figure 6 — Output Slew Rate and Output Timing Reference Load* (figure; any text below/above was extracted from the drawing)

*Figure 7 — Output Slew Rate Measurement Points* (figure; any text below/above was extracted from the drawing)

```text
                      I2 C                                          I3C

                     tF                                                tF
SCL,                                                 SCL,
SDA                                                  SDA
                                     0.7 V                                        0.7 V

                                     0.3 V                                        0.3 V

                          I2 C                                       I3C
                     tR                                                 tR

                                      0.7 V                                       0.7 V

                                      0.3 V                                       0.3 V
SCL,                                                  SCL,
SDA                                                   SDA
```

*Figure 8 — Input Rise and Fall Timing Parameter Definition* (figure; any text below/above was extracted from the drawing)
