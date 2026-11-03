---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 2.2.2
title: Switch Regulator Output Electrical Characteristics
pages: 4-9
---
# 2.2.2 Switch Regulator Output Electrical Characteristics

**Table 3 — SWA, SWB1 - Single Phase Regulator; PMIC5000; DC + AC Specification**

```text
                     Parameter                                 Symbol              Min          Typ          Max         Unit      Notes
Output Voltage                                                   Vout                            1.1                       V          2
Maximum Continuous DC Current Load                               Itdc                0            -            5           A          3
Maximum Peak Instantaneous Current                          -  Ipeakmax                           -            6          A           4
Maximum Load Transient                          dI/dt       -                                     -            5         A/μs
Regulator Output DC + AC Voltage Tolerance Reg_DC_AC_Tol -2.5%                                               2.5%                     5
Regulator Feedback Set Point Accuracy       FB_Set_Point -0.75%                                             0.75%                     6
 NOTE 1 Only applicable if Table 166, “Register 0x4F” [0] = ‘0’.
 NOTE 2 Typical voltage configured in the register Table 123, “Register 0x21” [7:1] for SWA and Table 125, “Register 0x23” [7:1] for SWB.
 NOTE 3 Measured over long period of time. Typically 1 second.
 NOTE 4 Measured over short period of time. Typically > 20 μs but less than 50 μs.
 NOTE 5 The percentage applies to typical voltage configured in the register. Applies across entire PMIC operating temperature range. The
        PMIC bulk input supply voltage VIN_Bulk can vary from minimum to maximum value specified in Table 2, “Input Supply DC + AC
        Specification”. The regulator output current load can vary maximum dI/dt value. The output ripple is inclusive in this parameter and
        not to exceed TBD mV.
 NOTE 6 The percentage applies to typical voltage configured in the register and at a given temperature within operating temperature range.
        The PMIC bulk input supply voltage VIN_Bulk is fixed at nominal voltage of 12.0 V. The regulator output current load Itdc = 0 A.
```

**Table 4 — SWA + SWB1 - Dual Phase Regulator; PMIC5000; DC + AC Specification**

```text
                    Parameter                                 Symbol              Min          Typ          Max         Unit      Notes
Output Voltage                                                  Vout                            1.1                       V          2
Maximum Continuous DC Current Load                              Itdc                0            -            10          A          3
Maximum Peak Instantaneous Current                          - Ipeakmax                           -           12          A           4
Maximum Load Transient                          dI/dt       -                                    -           10         A/μs
Regulator Output DC + AC Voltage Tolerance Reg_DC_AC_Tol -2.5%                                              2.5%                     5
Regulator Feedback Set Point Accuracy       FB_Set_Point -0.75%                                            0.75%                     6
NOTE 1 Only applicable if Table 166, “Register 0x4F” [0], = ‘1’.
NOTE 2 Typical voltage configured in the register Table 123, “Register 0x21” [7:1].
NOTE 3 Measured over long period of time. Typically 1 second.
NOTE 4 Measured over short period of time. Typically > 20 μs but less than 50 μs.
NOTE 5 The percentage applies to typical voltage configured in the register. Applies across entire PMIC operating temperature range. The
       PMIC bulk input supply voltage VIN_Bulk can vary from minimum to maximum value specified in Table 2, “Input Supply DC + AC
       Specification”. The regulator output current load can vary maximum dI/dt value. The output ripple is inclusive in this parameter and
       not to exceed TBD mV.
NOTE 6 The percentage applies to typical voltage configured in the register and at a given temperature within operating temperature range.
       The PMIC bulk input supply voltage VIN_Bulk is fixed at nominal voltage of 12.0 V. The regulator output current load Itdc = 0 A.
```

**Table 5 — SWA, SWB1 - Single Phase Regulator; PMIC5010; DC + AC Specification**

```text
                    Parameter                                 Symbol              Min          Typ          Max         Unit      Notes

Output Voltage                                                  Vout                            1.1                       V          2
Maximum Continuous DC Current Load                              Itdc                0            -            3           A          3

Maximum Peak Instantaneous Current             Ipeakmax     -                                    -           3.5         A           4

Maximum Load Transient                           dI/dt      -                                    -            5         A/μs
Regulator Output DC + AC Voltage Tolerance Reg_DC_AC_Tol -2.5%                                              2.5%                     5
Regulator Feedback Set Point Accuracy       FB_Set_Point -0.75%                                            0.75%                     6
NOTE 1 Only applicable if Table 166, “Register 0x4F” [0], = ‘1’.
NOTE 2 Typical voltage configured in the register Table 123, “Register 0x21” [7:1] for SWA and Table 125, “Register 0x23” [7:1] for SWB.
NOTE 3 Measured over long period of time. Typically 1 second.
NOTE 4 Measured over short period of time. Typically > 20 μs but less than 50 μs.
NOTE 5 The percentage applies to typical voltage configured in the register. Applies across entire PMIC operating temperature range. The
       PMIC bulk input supply voltage VIN_Bulk can vary from minimum to maximum value specified in Table 2, “Input Supply DC + AC
       Specification”. The regulator output current load can vary maximum dI/dt value. The output ripple is inclusive in this parameter and
       not to exceed TBD mV.
NOTE 6 The percentage applies to typical voltage configured in the register and at a given temperature within operating temperature range.
       The PMIC bulk input supply voltage VIN_Bulk is fixed at nominal voltage of 12.0 V. The regulator output current load Itdc = 0 A.
```

**Table 6 — SWA + SWB1 - Dual Phase Regulator; PMIC5010; DC + AC Specification**

```text
                     Parameter                                 Symbol              Min          Typ          Max         Unit      Notes
Output Voltage                                                   Vout                            1.1                       V          2
Maximum Continuous DC Current Load                               Itdc                0            -            6           A          3
Maximum Peak Instantaneous Current                          -  Ipeakmax                           -            7          A           4
Maximum Load Transient                          dI/dt       -                                     -           10         A/μs
Regulator Output DC + AC Voltage Tolerance Reg_DC_AC_Tol -2.5%                                               2.5%                     5
Regulator Feedback Set Point Accuracy       FB_Set_Point -0.75%                                             0.75%                     6
 NOTE 1 Only applicable if Table 166, “Register 0x4F” [0], = ‘1’.
 NOTE 2 Typical voltage configured in the register Table 123, “Register 0x21” [7:1].
 NOTE 3 Measured over long period of time. Typically 1 second.
 NOTE 4 Measured over short period of time. Typically > 20 μs but less than 50 μs.
 NOTE 5 The percentage applies to typical voltage configured in the register. Applies across entire PMIC operating temperature range. The
        PMIC bulk input supply voltage VIN_Bulk can vary from minimum to maximum value specified in Table 2, “Input Supply DC + AC
        Specification”. The regulator output current load can vary maximum dI/dt value. The output ripple is inclusive in this parameter and
        not to exceed TBD mV.
 NOTE 6 The percentage applies to typical voltage configured in the register and at a given temperature within operating temperature range.
        The PMIC bulk input supply voltage VIN_Bulk is fixed at nominal voltage of 12.0 V. The regulator output current load Itdc = 0 A.
```

**Table 7 — SWC1 - Single Phase Regulator; PMIC5000; DC + AC Specification**

```text
                     Parameter                                 Symbol              Min          Typ          Max         Unit      Notes
Output Voltage                                                   Vout                            1.1                       V          2

Maximum Continuous DC Current Load                               Itdc                0            -            5           A          3

Maximum Peak Instantaneous Current                          -  Ipeakmax                           -            6          A           4
Maximum Load Transient                          dI/dt       -                                     -            5         A/μs
Regulator Output DC + AC Voltage Tolerance Reg_DC_AC_Tol -2.5%                                               2.5%                     5
Regulator Feedback Set Point Accuracy       FB_Set_Point -0.75%                                             0.75%                     6
 NOTE 1 There is no note. This is intentional.
 NOTE 2 Typical voltage configured in the register Table 127, “Register 0x25” [7:1].
 NOTE 3 Measured over long period of time. Typically 1 second.
 NOTE 4 Measured over short period of time. Typically > 20 μs but less than 50 μs.
 NOTE 5 The percentage applies to typical voltage configured in the register. Applies across entire PMIC operating temperature range. The
        PMIC bulk input supply voltage VIN_Bulk can vary from minimum to maximum value specified in Table 2, “Input Supply DC + AC
        Specification”. The regulator output current load can vary maximum dI/dt value. The output ripple is inclusive in this parameter and
        not to exceed TBD mV.
 NOTE 6 The percentage applies to typical voltage configured in the register and at a given temperature within operating temperature range.
        The PMIC bulk input supply voltage VIN_Bulk is fixed at nominal voltage of 12.0 V. The regulator output current load Itdc = 0 A.
```

**Table 8 — SWC1 - Single Phase Regulator; PMIC5010; DC + AC Specification**

```text
                     Parameter                                 Symbol              Min          Typ          Max         Unit      Notes
Output Voltage                                                   Vout                            1.1                       V          2
Maximum Continuous DC Current Load                               Itdc                0            -            3           A          3
Maximum Peak Instantaneous Current             Ipeakmax     -                                     -           3.5         A           4
Maximum Load Transient                           dI/dt      -                                     -            5         A/μs
Regulator Output DC + AC Voltage Tolerance Reg_DC_AC_Tol -2.5%                                               2.5%                     5
Regulator Feedback Set Point Accuracy       FB_Set_Point -0.75%                                             0.75%                     6
 NOTE 1 There is no note. This is intentional.
 NOTE 2 Typical voltage configured in the register Table 127, “Register 0x25” [7:1].
 NOTE 3 Measured over long period of time. Typically 1 second.
 NOTE 4 Measured over short period of time. Typically > 20 μs but less than 50 μs.
 NOTE 5 The percentage applies to typical voltage configured in the register. Applies across entire PMIC operating temperature range. The
        PMIC bulk input supply voltage VIN_Bulk can vary from minimum to maximum value specified in Table 2, “Input Supply DC + AC
        Specification”. The regulator output current load can vary maximum dI/dt value. The output ripple is inclusive in this parameter and
        not to exceed TBD mV.
 NOTE 6 The percentage applies to typical voltage configured in the register and at a given temperature within operating temperature range.
        The PMIC bulk input supply voltage VIN_Bulk is fixed at nominal voltage of 12.0 V. The regulator output current load Itdc = 0 A.
```

**Table 9 — SWD1 - Single Phase Regulator; PMIC5000; DC + AC Specification**

```text
                     Parameter                                 Symbol              Min          Typ          Max         Unit      Notes
Output Voltage                                                   Vout                            1.8                       V          2

Maximum Continuous DC Current Load                               Itdc                0            -            5           A          3
Maximum Peak Instantaneous Current                             Ipeakmax

                                                            -                                     -            6          A           4
Maximum Load Transient                          dI/dt       -                                     -            5         A/μs
Regulator Output DC + AC Voltage Tolerance Reg_DC_AC_Tol -2.5%                                               2.5%                     5
Regulator Feedback Set Point Accuracy       FB_Set_Point -0.75%                                             0.75%                     6
 NOTE 1 There is no note. This is intentional.
 NOTE 2 Typical voltage configured in the register Table 129, “Register 0x27” [7:1].
 NOTE 3 Measured over long period of time. Typically 1 second.
 NOTE 4 Measured over short period of time. Typically > 20 μs but less than 50 μs.
 NOTE 5 The percentage applies to typical voltage configured in the register. Applies across entire PMIC operating temperature range. The
        PMIC bulk input supply voltage VIN_Bulk can vary from minimum to maximum value specified in Table 2, “Input Supply DC + AC
        Specification”. The regulator output current load can vary maximum dI/dt value. The output ripple is inclusive in this parameter and
        not to exceed TBD mV.
 NOTE 6 The percentage applies to typical voltage configured in the register and at a given temperature within operating temperature range.
        The PMIC bulk input supply voltage VIN_Bulk is fixed at nominal voltage of 12.0 V. The regulator output current load Itdc = 0 A.
```

**Table 10 — SWD1 - Single Phase Regulator; PMIC5010; DC + AC Specification**

```text
                     Parameter                                 Symbol              Min          Typ          Max         Unit      Notes
Output Voltage                                                   Vout                            1.8                       V          2
Maximum Continuous DC Current Load                               Itdc                0            -            3           A          3
Maximum Peak Instantaneous Current                          -  Ipeakmax                           -           3.5         A           4
Maximum Load Transient                          dI/dt       -                                     -            5         A/μs
Regulator Output DC + AC Voltage Tolerance Reg_DC_AC_Tol -2.5%                                               2.5%                     5
Regulator Feedback Set Point Accuracy       FB_Set_Point -0.75%                                             0.75%                     6
 NOTE 1 There is no note. This is intentional.
 NOTE 2 Typical voltage configured in the register Table 129, “Register 0x27” [7:1].
 NOTE 3 Measured over long period of time. Typically 1 second.
 NOTE 4 Measured over short period of time. Typically > 20 μs but less than 50 μs.
 NOTE 5 The percentage applies to typical voltage configured in the register. Applies across entire PMIC operating temperature range. The
        PMIC bulk input supply voltage VIN_Bulk can vary from minimum to maximum value specified in Table 2, “Input Supply DC + AC
        Specification”. The regulator output current load can vary maximum dI/dt value. The output ripple is inclusive in this parameter and
        not to exceed TBD mV.
 NOTE 6 The percentage applies to typical voltage configured in the register and at a given temperature within operating temperature range.
        The PMIC bulk input supply voltage VIN_Bulk is fixed at nominal voltage of 12.0 V. The regulator output current load Itdc = 0 A.
```
