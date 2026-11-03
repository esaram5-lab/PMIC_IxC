---
document: JESD301-2 (PMIC5100 Power Management IC Standard, Rev. 1.03, October 2022)
device: PMIC5100
application: client
section: 3.2
title: Switch Regulator Output Electrical Characteristics
pages: 10-11
---
# 3.2 Switch Regulator Output Electrical Characteristics

**Table 3 — SWA, SWB1 - Single Phase Regulator; DC + AC Specification**

```text
               Parameter                                    Symbol               Min          Typ          Max         Unit       Notes
Output Voltage                                               Vout                             1.1                       V          2
Maximum Continuous DC Current Load                            Itdc                 0           -             4          A          3
Maximum Peak Instantaneous Current                         Ipeakmax                -           -             5          A          4
Maximum Load Transient                                       dI/dt                 -           -             7         A/μs
Regulator Output DC + AC Voltage
                                                      Reg_DC_AC_Tol              -2.5                       2.5          %         5,6
Tolerance
Regulator Feedback Set Point Accuracy                    FB_Set_Point            -0.75                      0.75         %           7
NOTE 1 Only applicable if Table 164, “Register 0x4F” [0], = ‘0’.
NOTE 2 Typical voltage configured in the register Table 121, “Register 0x21” [7:1] for SWA and Table 125, “Register 0x25” [7:1] for
       SWB.
NOTE 3 Measured over long period of time. Typically 1 second.
NOTE 4 Measured over short period of time. Typically > 20 μs but less than 50 μs.
NOTE 5 The percentage applies to typical voltage configured in the register. The PMIC bulk input supply voltage VIN_Bulk can vary from
       minimum to maximum value specified in Table 2, “Input Supply DC + AC Specification1”. The regulator output current load can
       vary maximum dI/dt value. The output ripple is inclusive in this parameter and not to exceed TBD mV.
NOTE 6 Applies across entire PMIC operating temperature range.
NOTE 7 The percentage applies to typical voltage configured in the register and at a given temperature within operating temperature range.
       The PMIC bulk input supply voltage VIN_Bulk is fixed at nominal voltage of 5.0V. The regulator output current load Itdc = 0 A.
```

**Table 4 — SWA + SWB1 - Dual Phase Regulator; DC + AC Specification**

```text
               Parameter                                    Symbol               Min          Typ          Max         Unit       Notes

Output Voltage                                               Vout                             1.1                       V          2
Maximum Continuous DC Current Load                            Itdc                 0           -             8          A          3

Maximum Peak Instantaneous Current                         Ipeakmax                -           -             10         A          4
Maximum Load Transient                                       dI/dt                 -           -             14        A/μs
Regulator Output DC + AC Voltage
                                                      Reg_DC_AC_Tol              -2.5                       2.5          %         5,6
Tolerance
Regulator Feedback Set Point Accuracy                    FB_Set_Point            -0.75                      0.75         %           7
NOTE 1 Only applicable if Table 164, “Register 0x4F” [0], = ‘1’.
NOTE 2 Typical voltage configured in the register Table 121, “Register 0x21” [7:1].
NOTE 3 Measured over long period of time. Typically 1 second.
NOTE 4 Measured over short period of time. Typically > 20 μs but less than 50 μs.
NOTE 5 The percentage applies to typical voltage configured in the register. The PMIC bulk input supply voltage VIN_Bulk can vary from
       minimum to maximum value specified in Table 2, “Input Supply DC + AC Specification1”. The regulator output current load can
       vary maximum dI/dt value. The output ripple is inclusive in this parameter and not to exceed TBD mV.
NOTE 6 Applies across entire PMIC operating temperature range.
NOTE 7 The percentage applies to typical voltage configured in the register and at a given temperature within operating temperature range.
       The PMIC bulk input supply voltage VIN_Bulk is fixed at nominal voltage of 5.0 V. The regulator output current load Itdc = 0 A.
```

**Table 5 — SWC1 - Single Phase Regulator; DC + AC Specification**

```text
                    Parameter                               Symbol               Min           Typ         Max         Unit       Notes
Output Voltage                                               Vout                              1.8                      V          2
Maximum Continuous DC Current Load                            Itdc                 0            -            1          A          3
Maximum Peak Instantaneous Current                         Ipeakmax                -            -            2          A          4
Maximum Load Transient                                       dI/dt                 -            -           2.5        A/μs
Regulator Output DC + AC Voltage
                                                      Reg_DC_AC_Tol              -2.5                       2.5          %         5,6
Tolerance
Regulator Feedback Set Point Accuracy                    FB_Set_Point            -0.75                      0.75         %           7
NOTE 1 There is no note. This is intentional.
NOTE 2 Typical voltage configured in the register Table 127, “Register 0x27” [7:1].
NOTE 3 Measured over long period of time. Typically 1 second.
NOTE 4 Measured over short period of time. Typically > 20 μs but less than 50 μs.
NOTE 5 The percentage applies to typical voltage configured in the register. The PMIC bulk input supply voltage VIN_Bulk can vary from
       minimum to maximum value specified in Table 2, “Input Supply DC + AC Specification1”. The regulator output current load can
       vary maximum dI/dt value. The output ripple is inclusive in this parameter and not to exceed TBD mV.
NOTE 6 Applies across entire PMIC operating temperature range.
NOTE 7 The percentage applies to typical voltage configured in the register and at a given temperature within operating temperature range.
       The PMIC bulk input supply voltage VIN_Bulk is fixed at nominal voltage of 5.0 V. The regulator output current load Itdc = 0 A.
```
