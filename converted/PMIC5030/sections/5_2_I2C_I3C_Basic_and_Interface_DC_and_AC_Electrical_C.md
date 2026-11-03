---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 5.2
title: I2C, I3C Basic and Interface DC and AC Electrical Characteristics
pages: 17-23
---
# 5.2 I2C, I3C Basic and Interface DC and AC Electrical Characteristics

**Table 13 — I2C, I3C and Interface DC Electrical Specification**

```text
                          Parameter                                    Symbol           Min            Max          Unit      Notes
Input Low Voltage (CAMP, SDA, SCL, VR_OE)                                VIL            -0.3            0.3           V
Input High Voltage (SDA, SCL)                                            VIH             0.7            3.6           V
Input High Voltage (CAMP)                                                VIH            1.26            3.6           V
Input High Voltage (VR_OE)                                               VIH            1.26             15           V
Output Low Voltage (SDA, GSI_n)                                          VOL              -             0.3           V         [1]

Output High Voltage (SDA)                                                VOH            0.75             -            V
Output Low Current (SDA, GSI_n, CAMP)                                    IOL              3                          mA
Output High Current (SDA)                                                IOH              -              -3          mA
Output Low Voltage (CAMP)                                             VOL_CAMP            -             0.3           V         [2]

Rising Output Slew Rate (SDA)                                        Slew_Rate           0.1             1          V/ns        [3]

Falling Output Slew Rate (SDA)                                                           0.1             3          V/ns
Input Leakage Current                                                     ILI             -             +5           μA
Output Leakage Current                                                   ILO              -             +5           μA
 NOTE 1      The pullup resistor for GSI_n signal may vary and is > 1K Ohm.
 NOTE 2     CAMP output is Open Drain output. There is an external pullup resistor to 3.3 V motherboard for standard DDR5
            RDIMM/MRDIMM. For other DIMM environments, the external pullup resistor may be pulled to either 1.8V or 2.5V or 3.3V
            on either DIMM or the motherboard.
 NOTE 3     Output slew rate is guaranteed by design and/or characterization. The output slew rate reference load is shown in Figure 7

            and Figure 8 shows the timing measurement points. For slew rate measurement, the VOH level shown in Figure 8 is a
            function of Ron value; VOH = {1.0/(Ron + 50)} * 50.
```

**Table 14 — CMOS Rail to Rail Input Levels for Reset_n**

```text
                          Parameter                                    Symbol           Min            Max          Unit      Notes

AC Input High Voltage                                                  VIH(AC)          0.88            1.1           V         [1]

DC Input High Voltage                                                  VIH(DC)          0.77            1.1           V         [2]

AC Input Low Voltage                                                   VIL(AC)          VSS            0.22           V         [3]

DC Input Low Voltage                                                   VIL(DC)          VSS            0.33           V         [4]

Input Rise Time                                                        tR_Reset           -             1.0          μs         [5]

Peak to Peak voltage of slope reversal which must be                                      -             100          mV         [5]
                                                                     tSLPR_p2p
suppressed

Peak to Peak width of slope reversal which must be suppressed          tSLPRPW            -             10           ns         [5]

Input Reset Pulse Width                                               tPW_Reset          1.0                         μs         [6]

 NOTE 1     The PMIC may experience overshoot. The overshoot is limited by the Absolute Maximum Ratings.
 NOTE 2     Once Reset_n is registered High, Reset_n level must be maintained above VIH(DC), otherwise, the PMIC operation may not
            be guaranteed until it is reset asserting Reset_n signal Low.
 NOTE 3     The PMIC may experience undershoot. The undershoot is limited by the Absolute Maximum Ratings
 NOTE 4     After Reset_n is registered Low, Reset_n level shall be maintained below VIL(DC) during tPW_Reset, otherwise the PMIC may
            not be reset.
 NOTE 5     The slope reversal (ringback) must remain below VSLPR_p2p with the pulse width below tSLPRPW.
 NOTE 6     Clears registers as noted in clause 6.11.

                                       tPW_Reset

      0.88V (VIHAC)

      0.77V (VIHDC)

      0.33V (VILDC)
      0.22V (VILAC)

                                                                      TR_Reset
```

*Figure 2 — Reset_n Input Slew Rate Definition* (figure; any text below/above was extracted from the drawing)

*Figure 3 — Reset_n Slope Reversal Definition* (figure; any text below/above was extracted from the drawing)

**Table 15 — Input Capacitance Spec**

```text
                      Parameter                      Symbol      Min             Max   Unit   Notes

Input Capacitance (CAMP, SCL, SDA, VR_OE, Reset_n)    CIN         -               5    pF
```

**Table 16 — Input Spike Filter Spec**

```text
             Parameter                  Symbol           Test Condition                Min            Max            Unit        Notes
Pulse width of spikes which must           tSP       Single glitch, f < 100 KHz            -            -            ns
be suppressed by the input filter in                                                                                               [1]
                                                     Single glitch, f > 100 KHz            0            50           ns
I2C mode
  NOTE 1     TA = 25 0C; f = 400 KHz. Verified by design and characterization only.
```

**Table 17 — Output Ron**

```text
                          Parameter                                  Symbol         Min                  Max            Unit         Notes
SDA Output Pullup and Pulldown Driver Impedance                        RON              20                100            Ω             [1]

GSI_n, CAMP Output Pulldown Driver Impedance                                            20                100            Ω                 1
  NOTE 1     Pulldown Ron = Vout/Iout. Pullup Ron = (VOUT_1.0V - Vout)/Iout.
```

**Table 18 — I2C and I3C Interface AC Characteristics**

```text
                                                                                                       I3C Basic

                                                                                 I2C Mode -              Mode
                                                                                 Open Drain           Push-Pull[1]

                     Parameter                                Symbol            Min        Max        Min          Max           Unit         Notes
Clock Frequency                                                 fSCL            0.01        1         0.01         12.5          MHz

Clock High Pulse Width Time                                     tHigh           260                   35                         ns
Clock Low Pulse Width Time                                      tLow            500                   35                         ns
Detect Clock Input Low Time                                  tTIMEOUT            10        50         10           50            ms
Rise Time                                                        tR              -         120         -            5            ns               [2],[3]

Fall time                                                        tF              -         120         0            5            ns                2,3
Data in Setup Time                                            tSU:DAT            50         -          8            -            ns               2,[4]
Data in Hold Time                                              tHD:DI            0          -          3            -            ns                2,4
Start Condition Setup Time                                    tSU:STA           260         -         12            -            ns                 2
Start Condition Hold Time                                     tHD:STA           260         -         30            -            ns                 2
Stop Condition Setup Time                                     tSU:STO           260         -         12            -            ns                 2
Time between Stop Condition and next Start                      tBUF            500         -         500           -            ns               2,[5]
Condition
SDA Data Out Hold Time                                        tHD:DAT           0.5        350        N/A          N/A           ns                [6]

SCL Falling Clock In to Valid SDA Data Out Time                tDOUT            N/A        N/A        0.5          12            ns               [7],[8]

SCL Rising Clock In to Target SDA Output Off                  tDOFFT            N/A        N/A        0.5          12            ns           7,8,[9]

SCL Rising Clock In to Controller SDA Output Off              tDOFFC            N/A        N/A        0.5          30            ns           7,8,[10]

SCL Rising Clock In to Controller Driving Data Signal       tCL_r_DAT_f         N/A        N/A        40            -            ns                [11]
Low

                                                                                                     I3C Basic
                                                                               I2C Mode -              Mode
                                                                               Open Drain          Push-Pull[1]
                     Parameter                                Symbol          Min       Max        Min       Max       Unit     Notes
Bus Available Time (no edges seen on SCL and                    tAVAL          N/A       N/A        1          -        μs
SDA)
Time to issue IBI after an event is detected when Bus        tIBI_ISSUE        N/A       N/A         -        15        μs
is available
Time from Clear Register Status to any I3C Basic           tCLR_I3C_CMD_       N/A       N/A        4          -        μs
operation with Start condition to avoid false IBI               Delay
generation; PEC disabled
Time from Clear Register Status to any I3C Basic                               N/A       N/A        15         -        μs
```

operation with Start condition to avoid false IBI generation; PEC enabled

```text
DEVCTRL CCC Followed by DEVCTRL CCC or                     tDEVCTRLCCC_         3         -         3          -        μs      [12],[13]
Register Read/Write Command Delay                                                                                                 ,[14]
                                                          DELAY_PEC_DIS
Register Write Command Followed by Register Read           tWR_RD_DELAY        N/A       N/A        8          -        μs      [15],[16]
Command Delay in PEC Enabled Mode                                                                                                 ,[17]
                                                              _PEC_EN
SETHID CCC or SETAASA CCC followed by any                  tI2C_CCC_Updat      2.5        -          -         -        μs
other CCC or Read/Write Command Delay                          e_Delay
RSTDAA CCC or ENEC CCC or DISEC CCC to any                 tI3C_CCC_Updat       -         -        2.5         -        μs
other CCC or Read/Write Command Delay                          e_Delay

Any CCC followed by RSTDAA CCC delay                         tCCC_Delay        N/A       N/A       2.5         -        μs
 NOTE 1      I3C mode with Open Drain operation follows timing values as shown in I2C Mode - Open Drain column.

 NOTE 2      See Figure 4 for PMIC’s input timing definition.
 NOTE 3      See Figure 9 for voltage threshold definition for rise and fall times.

 NOTE 4      The input setup time is referenced from SDA VIL or VIH threshold as shown in Figure to SCL VIH threshold as shown in
             Figure 4. The input hold time is referenced from SCL VIL threshold as shown in Figure 4 to SDA VIL or VIH threshold as
             shown in Figure 4.
 NOTE 5      If PEC is enabled, tWR_RD_DELAY_PEC_EN timing parameter applies.
 NOTE 6      The PMIC device guarantees tHD:DAT value in I2C mode of operation. See Figure 6 for PMIC’s output timing definitions as well
             as SCL clock input threshold level and SDA data output threshold levels.
 NOTE 7      The PMIC device must be configured in I3C Basic mode to guarantee tDOUT or tDOFFT or tDOFFC value. See Figure 5 for
             PMIC’s output timing definition as well as SCL clock input threshold level and SDA data output threshold levels.
 NOTE 8      This timing parameter is guaranteed into output timing reference load as shown in Figure 7.
 NOTE 9      The PMIC device must be configured in I3C Basic mode to guarantee tDOFFT value. See Figure 22.
 NOTE 10     The PMIC device must be configured in I3C Basic mode to guarantee tDOFFC value. See Figure 23.
 NOTE 11     See Figure 24.
 NOTE 12     From STOP condition of DEVCTRL CCC to START condition for Register Read or Register Write Command Data Packet
             delay.
 NOTE 13     The PMIC sends NACK if Host does not satisfy tDEVCTRLCCC_DELAY_PEC_DIS timing parameter.
 NOTE 14     This timing parameter restriction is only applicable when PEC function is disabled in PMIC. If PEC is enabled, this timing
             parameter does not apply.
 NOTE 15     From STOP condition for Register Write Command Data Packet to START condition for Register Read Command Data
             Packet delay.
 NOTE 16     This timing parameter restriction is only applicable when PEC function is enabled in PMIC. If PEC is disabled, this timing
             parameter does not apply.
 NOTE 17     The PMIC sends NACK if Host does not satisfy tWR_RD_DELAY_PEC_EN timing parameter.
```

The PMIC device follows the I2C or I3C Basic bus timing requirements. The Figure 4, Figure 5, and Figure 6 show the timing diagram for Data bus Input and Data Output parameters.

```text
                                         tR                  tHIGH
                                                tHD:DI
          P         S             tLOW                                               Sr                                               P
SCL
 VIHmin
 VILmax

                                                         tSU:DAT     tF   tSU:DAT         tSU:STA                           tSU:STO
                        tHD:STA
 VIHmin
 VILmax
SDA
                tBUF
```

*Figure 4 — I2C or I3C Basic Bus AC Input Timing Parameter Definition* (figure; any text below/above was extracted from the drawing)

```text
                                tDOUT                                                 tDOUT
SCL
                                                                                                           VIHmin

                                                                                                           VILmax

                                                     ACK                                                  VOHmin
SDA
                                                                                                          VOLmax
```

*Figure 5 — I3C Basic Bus AC Data Output Timing Parameter Definition* (figure; any text below/above was extracted from the drawing)

```text
                                      tHD:DAT                                               tHD:DAT
SCL
                                                                                                             VIHmin

                                                                                                             VILmax

                                                    ACK                                                      VOHmin
SDA
                                                                                                             VOLmax
```

*Figure 6 — I2C Bus AC Data Output Timing Parameter Definition* (figure; any text below/above was extracted from the drawing)

```text
               50 Ohm
SDA
        5 mm
```

*Figure 7 — Output Slew Rate and Output Timing Reference Load* (figure; any text below/above was extracted from the drawing)

```text
                         Delta tF
                                                            Delta tR
SDA                                                                            VOH
                                                                               70%*VOH

                                                                               30%*VOH
                                                            VOL
```

*Figure 8 — Output Slew Rate Measurement Points* (figure; any text below/above was extracted from the drawing)

```text
                       I2C                                                      I3C
                      tF                                                           tF

SCL,                                                        SCL,
SDA                                                         SDA

                                             0.7 V                                                0.7 V

                                             0.3 V                                                0.3 V

                           I2 C                                                 I3C
                      tR                                                           tR

                                             0.7 V                                                0.7 V

                                             0.3 V                                                0.3 V
 SCL,                                                        SCL,
 SDA                                                         SDA
```

*Figure 9 — Rise and Fall Timing Parameter Definition* (figure; any text below/above was extracted from the drawing)

**Table 19 — AC Measurement Conditions[1]**

```text
Symbol                     Parameter                               Min                    Max           Units

   CL      Load capacitance                                                                40             pF

           Input rise and Fall times - Open Drain                    -                   TBD              ns

           Input rise and fall times - Push Pull                     -                   TBD              ns

           Input signal swing levels                                       0.2 to 0.8                      V

           Input and Output timing reference levels                        0.3 to 0.7                      V
  NOTE 1     These AC measurement conditions (Table 19 and Figure 10) are only for lab test purposes.

      Input Signal                                                            Input Levels for
      Swing levels                                                            timing reference
 0.8 V                                                                                       0.7 V

                                                                                             0.3 V
 0.2 V
```

*Figure 10 — AC Measurement Waveform* (figure; any text below/above was extracted from the drawing)
