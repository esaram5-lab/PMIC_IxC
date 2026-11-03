---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 2.3
title: I2C, I3C Basic and Interface DC and AC Electrical Characteristics
pages: 12-17
---
# 2.3 I2C, I3C Basic and Interface DC and AC Electrical Characteristics

**Table 15 — I2C, I3C, and Interface DC Electrical Specification**

```text
                      Parameter                                          Symbol              Min             Max           Unit      Notes
Input Low Voltage (CAMP, SDA, SCL)                                         VIL               -0.3             0.3           V
Input High Voltage (SDA, SCL)                                              VIH               0.7              3.6           V
Input High Voltage (CAMP)                                                  VIH               1.26             3.6           V
Output Low Voltage (SDA, GSI_n)                                           VOL                  -              0.3           V             1
Output High Voltage (SDA)                                                 VOH                0.75              -            V
Output Low Current (SDA, GSI_n, CAMP)                                      IOL                 3               -           mA
Output High Current (SDA)                                                  IOH                 -               3           mA
Output Low Voltage (CAMP)                                               VOL_CAMP               -              0.3           V             2
Rising Output Slew Rate (SDA)                                                                0.1               1           V/ns
                                                                        Slew_Rate                                                         3
Falling Output Slew Rate (SDA)                                                               0.1               3           V/ns
Input Leakage Current                                                        ILI               -              +5           μA
Output Leakage Current                                                       ILO               -              +5           μA
NOTE 1 The pullup resistor for GSI_n signal may vary and is typically 1K Ohm.
NOTE 2 CAMP output is Open Drain output. There is an external pullup resistor to 3.3 V motherboard for standard DDR5 RDIMM/LRDIMM.
       For other DIMM environment, the external pullup resistor may be pulled to either 1.8 V or 2.5 V or 3.3 V on either on DIMM or on
       the motherboard.
NOTE 3 Output slew rate is guaranteed by design and/or characterization. The output slew rate reference load is shown in Figure 4 and Figure 5
       shows the timing measurement points. For slew rate measurement, the VOH level shown in Figure 5 is a function of Ron value;
       VOH = {1.0/(Ron + 50)} * 50.
```

**Table 16 — Input Capacitance Spec**

```text
                     Parameter                                            Symbol             Min             Max           Unit      Notes
Input Capacitance (CAMP, SCL, SDA)                                          CIN                -               5            pF
```

**Table 17 — Input Spike Filter Spec**

```text
               Parameter                      Symbol            Test Condition                Min          Max          Unit      Notes
Pulse width of spikes which must                          Single glitch, f < 100 KHz              -           -          ns
be suppressed by the input filter in             tSP
                                                          Single glitch, f > 100 KHz              0          50          ns          1
I2C mode
 NOTE 1 TA = 25 0C; f = 400 KHz. Verified by design and characterization only.
```

**Table 18 — Output Ron**

```text
                     Parameter                                            Symbol             Min             Max           Unit      Notes
SDA Output Pullup and Pulldown Driver Impedance                                              20              100             Ω
                                                                            RON                                                           1
GSI_n, CAMP Output Pulldown Driver Impedance                                                 40              100             Ω
NOTE 1 Pulldown Ron = Vout/Iout. Pullup Ron = (VOUT_1.0V - Vout)/Iout.
```

**Table 19 — I2C and I3C Interface AC Characteristics**

```text
                                                              I2C Mode -    I3C Basic Mode
                                                              Open Drain      Push-Pull¹
                  Parameter                       Symbol      Min    Max     Min    Max      Unit    Notes
Clock Frequency                                       fSCL    0.01    1      0.01   12.5     MHz
Clock High Pulse Width Time                           tHigh   260             35              ns
Clock Low Pulse Width Time                            tLow    500             35              ns
Detect Clock Input Low Time                      tTIMEOUT      10    50       10     50      ms
Rise Time                                              tR       -    120       -      5       ns      2,3
Fall time                                               tF      -    120       0      5       ns      2,3
Data in Setup Time                                 tSU:DAT     50     -        8      -       ns      2,4
Data in Hold Time                                    tHD:DI     0     -        3      -       ns      2,4
Start Condition Setup Time                         tSU:STA    260     -       12      -       ns       2
Start Condition Hold Time                          tHD:STA    260     -       30      -       ns       2
Stop Condition Setup Time                          tSU:STO    260     -       12      -       ns       2
```

Time between Stop Condition and next Start

```text
                                                      tBUF    500     -      500      -       ns      2,5
Condition
SDA Data Out Hold Time                            tHD:DAT     0.5    350     N/A    N/A       ns       6
```

SCL Falling Clock In to Valid SDA Data Out

```text
                                                     tDOUT    N/A    N/A      0.5    12       ns      7,8
Time
```

SCL Rising Clock In to Target SDA Output

```text
                                                    tDOFFT    N/A    N/A      0.5    12       ns     7,8,9
Off

SCL Rising Clock In to Controller SDA
                                                   tDOFFC     N/A    N/A      0.5    30       ns     7,8,10
Output Off
```

SCL Rising Clock In to Controller Driving

```text
                                                tCL_r_DAT_f   N/A    N/A      40      -       ns      11
Data Signal Low
```

Bus Available Time (no edges seen on SCL

```text
                                                     tAVAL    N/A    N/A      1       -       μs
and SDA)
```

Time to issue IBI after an event is detected

```text
                                                 tIBI_ISSUE   N/A    N/A       -     15       μs
when Bus is available
```

Time from Clear Register Status to any I3C

```text
Basic operation with Start condition to avoid                 N/A    N/A      4       -       μs
false IBI generation; PEC disabled            tCLR_I3C_CMD_
Time from Clear Register Status to any I3C            Delay
Basic operation with Start condition to avoid                 N/A    N/A      15      -       μs
false IBI generation; PEC enabled
DEVCTRL CCC Followed by DEVCTRL
                                              tDEVCTRLCCC_
CCC or Register Read/Write Command                             3      -       3       -       μs    12,13,14
                                              DELAY_PEC_DIS
Delay

                                                                                   I2C Mode -                I3C Basic Mode
                                                                                   Open Drain                 Push-Pull¹
                Parameter                  Symbol                                  Min                 Max    Min    Max      Unit            Notes
Register Write Command Followed by
                                       tWR_RD_DELAY
Register Read Command Delay in PEC                                                 N/A                 N/A     8       -       μs        15,16,17
                                           _PEC_EN
Enabled Mode
SETHID CCC or SETAASA CCC followed
                                       t
by any other CCC or Read/Write Command I2C_CCC_Update                              2.5                  -      -       -       μs
                                            _Delay
Delay
RSTDAA CCC or ENEC CCC or DISEC
                                       tI3C_CCC_Update
CCC to any other CCC or Read/Write                                                  -                   -     2.5      -       μs
                                            _Delay
Command Delay
Any CCC followed by RSTDAA CCC delay      tCCC_Delay                               N/A                 N/A    2.5      -       μs
NOTE 1 I3C mode with Open Drain operation follows timing values as shown in I2C Mode - Open Drain column.
NOTE 2 See Figure 1 for PMIC’s input timing definition.
NOTE 3 See Figure 6 for voltage threshold definition for rise and fall times.
NOTE 4 The input setup time is referenced from SDA VIL or VIH threshold as shown in Figure 1 to SCL VIH threshold as shown in Figure 1.
       The input hold time is referenced from SCL VIL threshold as shown in Figure 1 to SDA VIL or VIH threshold as shown in Figure 1.
NOTE 5 If PEC is enabled, tWR_RD_DELAY_PEC_EN timing parameter applies.
NOTE 6 The PMIC device guarantees tHD:DAT value in I2C mode of operation. See Figure 3 for PMIC’s output timing definitions as well as
       SCL clock input threshold level and SDA data output threshold levels.
NOTE 7 The PMIC device must be configured in I3C Basic mode to guarantee tDOUT or tDOFFT or tDOFFC value. See Figure 2 for PMIC’s
       output timing definition as well as SCL clock input threshold level and SDA data output threshold levels.
NOTE 8 This timing parameter is guaranteed into output timing reference load as shown in Figure 4.

NOTE 9 The PMIC device must be configured in I3C Basic mode to guarantee tDOFFT value. See Figure 18.
NOTE 10 The PMIC device must be configured in I3C Basic mode to guarantee tDOFFC value. See Figure 19.

NOTE 11 See Figure 21.
NOTE 12 From STOP condition of DEVCTRL CCC to START condition for Register Read or Register Write Command Data Packet delay.

NOTE 13 The PMIC sends NACK if Host does not satisfy tDEVCTRLCCC_DELAY_PEC_DIS timing parameter.
NOTE 14 This timing parameter restriction is only applicable when PEC function is disabled in PMIC. If PEC is enabled, this timing parameter
        does not apply.
NOTE 15 From STOP condition for Register Write Command Data Packet to START condition for Register Read Command Data Packet delay.
NOTE 16 This timing parameter restriction is only applicable when PEC function is enabled in PMIC. If PEC is disabled, this timing parameter
        does not apply.
NOTE 17 The PMIC sends NACK if Host does not satisfy tWR_RD_DELAY_PEC_EN timing parameter.
```

The PMIC device follow the I2C or I3C Basic bus timing requirements. Figure 1, Figure 2, and Figure 3 show the timing diagram for Data bus Input and Data Output parameters.

```text
                                      tR                tHIGH
                                           tHD:DI
          P     S              tLOW                                                    Sr                                                      P
SCL
 VIHmin
 VILmax

                                                    tSU:DAT     tF      tSU:DAT             tSU:STA                                tSU:STO
                     tHD:STA
 VIHmin
 VILmax
SDA
              tBUF
```

*Figure 1 — I2C or I3C Basic Bus AC Input Timing Parameter Definition* (figure; any text below/above was extracted from the drawing)

```text
                 tDOUT                                       tDOUT
SCL
                                                                                    VIHmin

                                                                                    VILmax

                               ACK                                                 VOHmin
SDA
                                                                                   VOLmax
```

*Figure 2 — I3C Basic Bus AC Data Output Timing Parameter Definition* (figure; any text below/above was extracted from the drawing)

```text
                        tHD:DAT                                     tHD:DAT
SCL
                                                ng                                  VIHmin

                                                                                    VILmax

                                  ACK                                              VOHmin
SDA
                                                                                   VOLmax
```

*Figure 3 — I2C Bus AC Data Output Timing Parameter Definition* (figure; any text below/above was extracted from the drawing)

```text
               50 Ohm
SDA
        5 mm
```

*Figure 4 — Output Slew Rate and Output Timing Reference Load* (figure; any text below/above was extracted from the drawing)

```text
                         Delta tF
                                                        Delta tR
SDA                                                                           VOH
                                                                              70%*VOH

                                                                              30%*VOH
                                                        VOL
```

*Figure 5 — Output Slew Rate Measurement Points* (figure; any text below/above was extracted from the drawing)

```text
                      I2C                           ng                     I3C
                     tF                                                       tF
SCL,                                                    SCL,
SDA                                                     SDA

                                           0.7 V                                               0.7 V

                                           0.3 V                                               0.3 V

                         I2 C                                                I3C
                    tR                                                          tR

                                           0.7 V                                               0.7 V

                                           0.3 V                                               0.3 V
SCL,                                                    SCL,
SDA                                                     SDA
```

*Figure 6 — Rise and Fall Timing Parameter Definition* (figure; any text below/above was extracted from the drawing)

**Table 20 — AC Measurement Conditions1**

```text
 Symbol                      Parameter                              Min                   Max             Units
CL           Load capacitance                                                              40              pF
            Input rise and Fall times - Open Drain                    -                   TBD              ns
            Input rise and fall times - Push Pull                     -                   TBD              ns
            Input signal swing levels                                       0.2 to 0.8                     V
            Input and Output timing reference levels                        0.3 to 0.7                     V
 NOTE 1 This AC measurement condition (Table 20 and Figure 7) is only for the test purpose in lab.

       Input Signal                                                             Input Levels for
       Swing levels                                                             timing reference
  0.8 V                                                                                         0.7 V

                                                                                                0.3 V
  0.2 V
```

*Figure 7 — AC Measurement Waveform* (figure; any text below/above was extracted from the drawing)
