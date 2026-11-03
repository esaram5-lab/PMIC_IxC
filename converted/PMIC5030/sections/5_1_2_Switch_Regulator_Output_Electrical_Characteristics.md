---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 5.1.2
title: Switch Regulator Output Electrical Characteristics
pages: 10-14
---
# 5.1.2 Switch Regulator Output Electrical Characteristics

**Table 6 — SWA, SWB, SWC, SWE, SWF - Single Phase Regulator; DC + AC Specification**

```text
                   Parameter                                 Symbol              Min          Typ         Max         Unit     Notes

Output Voltage                                                 Vout                           1.1                      V          [1]

Maximum Continuous DC Current Load                              Itdc               0            -          7.5         A          [2]

Maximum Peak Instantaneous Current                          Ipeakmax               -            -          9.5         A          [3]

Maximum Load Transient                                         dI/dt               -            -          7.5        A/μs        [4]

Regulator Output DC + AC Voltage Tolerance              Reg_DC_AC_Tol            -2.5                      2.5         %        [5],[6]

Regulator Feedback Set Point Accuracy                     FB_Set_Point           -0.75                    0.75         %          [7]

 NOTE 1     Typical voltage configured in appropriate register for SWA, SWB, SWC, SWE, and SWF.
 NOTE 2     Measured over long period of time. Typically 1 second.
 NOTE 3     Measured over short period of time. Typically > 20 μs but less than 50 μs.
 NOTE 4     This parameter is applied to measure output voltage regulator DC+AC tolerance.
 NOTE 5     The percentage applies to typical voltage configured in appropriate register. The PMIC bulk input supply voltage VIN_Bulk
            can vary from minimum to maximum value specified in Table 5. The regulator output current load can vary maximum dI/dt
            value. The output ripple is inclusive in this parameter.
 NOTE 6     Applies across entire PMIC operating temperature range.
 NOTE 7
            The percentage applies to typical voltage configured in the register and at a given temperature within operating temperature
            range. The PMIC bulk input supply voltage VIN_Bulk is fixed at nominal voltage of 12.0 V. The regulator output current load
            Itdc = 0 A.
```

**Table 7 — SWA+SWB or SWC+SWF - Dual Phase[1] Regulator; DC + AC Specification**

```text
                   Parameter                                 Symbol              Min          Typ         Max         Unit     Notes

Output Voltage                                                 Vout                           1.1                      V          [2]

Maximum Continuous DC Current Load                              Itdc               0            -          15          A          [3]

Maximum Peak Instantaneous Current                          Ipeakmax               -            -          19          A          [4]

Maximum Load Transient                                         dI/dt               -            -          15         A/μs        [5]

Regulator Output DC + AC Voltage Tolerance              Reg_DC_AC_Tol            -2.5                      2.5         %        [6],[7]

Regulator Feedback Set Point Accuracy                     FB_Set_Point           -0.75                    0.75         %          [8]

 NOTE 1     Only applicable if Register Table 247, Register 0x4F [5,0]= ‘01’ for SWA+SWB and Table 247, Register 0x4F [6] = ‘1’ for
            SWC+SWF. The register setting in SWB and SWF is ignored by the PMIC.
 NOTE 2     Typical voltage configured in register Table 138, Register 0x21 [7:1] for SWA+SWB and Table 142, Register 0x25[7:1] for
            SWC+SWF. The register setting in Table 140, Register 0x23 [7:1] and Table 187, Register 0x11F is ignored by PMIC for
            dual phase operation.
 NOTE 3     Measured over long period of time. Typically 1 second.
 NOTE 4     Measured over short period of time. Typically > 20 μs but less than 50 μs.
 NOTE 5     This parameter is applied for the measurement of the output voltage regulator accuracy.
 NOTE 6     The percentage applies to typical voltage configured in the register. The PMIC bulk input supply voltage VIN_Bulk can vary
            from minimum to maximum value specified in Table 5. The regulator output current load can vary maximum dI/dt value. The
            output ripple is inclusive in this parameter.
 NOTE 7     Applies across entire PMIC operating temperature range.

 NOTE 8     The percentage applies to typical voltage configured in the register and at a given temperature within operating temperature
            range. The PMIC bulk input supply voltage VIN_Bulk is fixed at nominal voltage of 12.0 V. The regulator output current load
            Itdc = 0 A.
```

**Table 8 — SWA+SWB+SWE - Triple Phase[1] Regulator; DC + AC Specification**

```text
                   Parameter                                 Symbol              Min          Typ         Max         Unit     Notes

Output Voltage                                                 Vout                           1.1                      V          [2]

Maximum Continuous DC Current Load                              Itdc               0            -         22.5         A          [3]

Maximum Peak Instantaneous Current                          Ipeakmax               -            -         28.5         A          [4]

Maximum Load Transient                                         dI/dt               -            -         22.5        A/μs        [5]

Regulator Output DC + AC Voltage Tolerance              Reg_DC_AC_Tol            -2.5                      2.5         %        [6],[7]

Regulator Feedback Set Point Accuracy                     FB_Set_Point           -0.75                    0.75         %          [8]

 NOTE 1     Only applicable if register Table 247, Register 0x4F [5] = ‘1’ for SWA+SWB+SWE; the register Table 247, Register 0x4F
            [0] is a don’t care.
 NOTE 2     Typical voltage configured in register Table 138, Register 0x21 [7:1] for SWA+SWB+SWE. The register setting in
            Table 140, Register 0x23 [7:1] and Table 185, Register 0x11D [7:1] is ignored by PMIC for triple phase operation.
 NOTE 3     Measured over long period of time. Typically 1 second.
 NOTE 4     Measured over short period of time. Typically > 20 μs but less than 50 μs.
 NOTE 5     This parameter is applied to measure output voltage regulator DC+AC tolerance.
 NOTE 6     The percentage applies to typical voltage configured in the register. The PMIC bulk input supply voltage VIN_Bulk can vary
            from minimum to maximum value specified in Table 5. The regulator output current load can vary maximum dI/dt value. The
            output ripple is inclusive in this parameter.
 NOTE 7     Applies across entire PMIC operating temperature range.
 NOTE 8     The percentage applies to typical voltage configured in the register and at a given temperature within operating temperature
            range. The PMIC bulk input supply voltage VIN_Bulk is fixed at nominal voltage of 12.0 V. The regulator output current load

            Itdc = 0 A.
```

**Table 9 — SWD - Single Phase Regulator; DC + AC Specification**

```text
                   Parameter                                 Symbol              Min          Typ         Max         Unit     Notes

Output Voltage                                                 Vout                           1.8                      V          [1]

Maximum Continuous DC Current Load                              Itdc               0            -           5          A          [2]

Maximum Peak Instantaneous Current                          Ipeakmax               -            -           6          A          [3]

Maximum Load Transient                                         dI/dt               -            -           5         A/μs        [4]

Regulator Output DC + AC Voltage Tolerance              Reg_DC_AC_Tol            -2.5                      2.5         %        [5], [6]

Regulator Feedback Set Point Accuracy                     FB_Set_Point           -0.75                    0.75         %          [7]

 NOTE 1     Typical voltage configured in register Table 144, Register 0x27 [7:1].
 NOTE 2     Measured over long period of time. Typically 1 second.
 NOTE 3     Measured over short period of time. Typically > 20 μs but less than 50 μs.
 NOTE 4     This parameter is applied to measure output voltage regulator DC+AC tolerance.
 NOTE 5     The percentage applies to typical voltage configured in the register. The PMIC bulk input supply voltage VIN_Bulk can vary
            from minimum to maximum value specified in Table 5. The regulator output current load can vary maximum dI/dt value. The
            output ripple is inclusive in this parameter.
 NOTE 6     Applies across entire PMIC operating temperature range.
 NOTE 7     The percentage applies to typical voltage configured in the register and at a given temperature within operating temperature
            range. T he PMIC bulk input supply voltage VIN_Bulk is fixed at nominal voltage of 12.0V. The regulator output current load
            Itdc = 0 A.
```
