---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 3.1
title: Input Supply and Output Regulator Electrical Characteristics
pages: 7-11
---
# 3.1 Input Supply and Output Regulator Electrical Characteristics



## 3.1.1 Input Supply Electrical Characteristics

**Table 3 — Input Supply DC + AC Specification[1]**

```text
                    Parameter                                    Symbol                  Min        Typ         Max       Unit     Notes

 Bulk Input Supply Voltage                                      VIN_Bulk                 3.0         5.0        5.5         V        [2]

 Bulk Input Supply Maximum AC Voltage                        VIN_Bulk_AC                  -           -         6.5         V

 Maximum voltage on VIN_Bulk during soft stop          VIN_Bulk_Soft_Stop_Max             -           -         5.55        V       [3],[4]

 Bulk Input Supply Voltage Ramp Up Rate                   VIN_Bulk_Ramp_Up              0.01          -         3.0       V/ms       [5]

 Bulk Input Supply Voltage Ramp Down Rate               VIN_Bulk_Ramp_Down
                                                                         ng             0.01          -         1.0       V/ms       [6]

 Bulk Input Supply Voltage Start Up Overshoot          VIN_Bulk_OS_STARTUP                -           -         TBD       V*μs       [7]

 VIN_Bulk Input Supply Current                                   IVIN_Bulk              0.05          -         2.0         A        [8]

                                                              IVIN_Bulk_5.0V             5.2          -         7.5         A        [9]

                                                              IVIN_Bulk_3.3V             7.8          -         9.5         A        [9]

 VIN_Bulk Input Supply Quiescent Current                    IVIN_Bulk_Quiescent           -           -          25        μA        [10]

 VIN_Bulk Input Supply Idle Current                           IVIN_Bulk_Idle              -           -         TBD        μA        [11]

NOTE 1    Input supply is referred in this table are VIN_Bulk and VIN.
NOTE 2    During first power on, the input voltage supply must reach a minimum 3.0 V for PMIC to detect valid input supply.
NOTE 3    The maximum VIN_Bulk input supply voltage rise during soft stop for SWx soft stop operation.
NOTE 4    The maximum VIN_Bulk input supply voltage rise is tested with VIN_Bulk = 5.5 V, SWA = 1.05 V, SWB= 0.5 V, SWC = 1.8 V and
          SWD = 0.9 V and using the recommended setting from the “LPDDR5/5X PMIC5200 Register Setting for the Soft Stop” table in
          JESD318. The test condition assumes input VIN_Bulk supply is not capable of sinking current. The maximum VIN_Bulk input
          supply voltage rise is tested with module VIN_Bulk and output rail decoupling from the “LPDDR5/5X Decoupling guidelines” table
          in JESD318 and with bulk output capacitance for SWx listed in Section 6.1. This specification defines the DC component of the
          voltage during soft stop. AC noise that is less than 1μs can be ignored when testing against this spec. The maximum voltage rise
          is measured under 1MHz bandwidth limiting during soft stop shut down.
NOTE 5    The ramp up rate between 300 mV and 3.0 V.
NOTE 6    The ramp down rate between 3.0 V and 300 mV.
NOTE 7    The area under the curve above VIN_Bulk = TBD V. VIN_Bulk_AC spec must also be satisfied.
NOTE 8    The minimum input current requirement is to deliver the maximum rated output current on VOUT_1.8V, VOUT_1.0V LDO plus
          the current required by the PMIC for its own use. The maximum input current is what PMIC may see on its all VIN_Bulk input.
NOTE 9    The minimum input current requirement is to deliver the maximum rated output current on VOUT_1.8V, VOUT_1.0V LDO, all
          switch regulator outputs plus the current required by the PMIC for its own use. The maximum input current is what PMIC may
          see on its all VIN_Bulk input.
NOTE 10    VIN_Bulk = 5.0V. Measured at room temperature. All circuitry including output regulators and LDOs are off. VR_EN signal is
           static Low or High; I2C or I3C Basic interface access is not allowed and bus is pulled High. PID signal is pulled either High or
           Low.
NOTE 11    VIN_Bulk = 5.0 V. Measured at room temperature. All output regulators and LDOs are on with 0A output load. VR_EN signal is
           static Low or High. I2C or I3C Basic interface access is allowed and bus is pulled High. PID signal is pulled either High or Low.
```

## 3.1.2 Switch Regulator Output Electrical Characteristics

**Table 4 — SWA - Single Phase Regulator; DC + AC Specification**

```text
                    Parameter                                  Symbol              Min        Typ         Max        Unit      Notes

 Output Voltage                                                  Vout                        1.05                      V         [1]

 Maximum Continuous DC Current Load                              Itdc                0         -           7.5         A         [2]

 Maximum Peak Instantaneous Current                           Ipeakmax               -         -          11.5         A         [3]

 Maximum Load Transient                                          dI/dt               -         -           10        A/μs        [4]

 Regulator Output DC + AC Voltage Tolerance               Reg_DC_AC_Tol            -2.5                    2.5        %        [5],[6]

 Regulator Feedback Set Point Accuracy                     FB_Set_Point           -0.75                   0.75        %          [7]

NOTE 1   Typical voltage configured in the register Table 137, “Register 0x21,” [7:1].
NOTE 2   Measured over long period of time. Typically 1 second.
NOTE 3   Measured over short period of time. Typically > 20 μs but less than 50 μs.
NOTE 4   This parameter is applied to measure output voltage regulator DC+AC tolerance.
NOTE 5   The percentage applies to typical voltage configured in the register. The PMIC bulk input supply voltage VIN_Bulk can vary
         from minimum to maximum value specified in Table 3, “Input Supply DC + AC Specification”. The regulator output current load
         can vary maximum dI/dt value. The output ripple is inclusive in this parameter.
NOTE 6   Applies across entire PMIC operating temperature range.
NOTE 7   The percentage applies to typical voltage configured in the register and at a given temperature within operating temperature

         range. The PMIC bulk input supply voltage VIN_Bulk is fixed at nominal voltage of 5.0V. The regulator output current load Itdc
         = 0 A.
```

**Table 5 — SWD - Single Phase Regulator; DC + AC Specification**

```text
                    Parameter                                  Symbol              Min        Typ         Max        Unit      Notes

 Output Voltage                                                  Vout                         0.9                      V         [1]

 Maximum Continuous DC Current Load                              Itdc                0         -           1.2         A         [2]

 Maximum Peak Instantaneous Current                           Ipeakmax               -         -            2          A         [3]

 Maximum Load Transient                                          dI/dt               -         -            2        A/μs        [4]

 Regulator Output DC + AC Voltage Tolerance               Reg_DC_AC_Tol            -2.5                    2.5        %        [5],[6]

 Regulator Feedback Set Point Accuracy                     FB_Set_Point           -0.75                   0.75        %          [7]

NOTE 1   Typical voltage configured in the register Table 139, “Register 0x23,”[7:1].
NOTE 2   Measured over long period of time. Typically 1 second.
NOTE 3   Measured over short period of time. Typically > 20 μs but less than 50 μs.
NOTE 4   This parameter is applied for the measurement of the output voltage regulator accuracy.
NOTE 5   The percentage applies to typical voltage configured in the register. The PMIC bulk input supply voltage VIN_Bulk can vary
         from minimum to maximum value specified in Table 3, “Input Supply DC + AC Specification”. The regulator output current load
         can vary maximum dI/dt value. The output ripple is inclusive in this parameter.
NOTE 6   Applies across entire PMIC operating temperature range.
NOTE 7   The percentage applies to typical voltage configured in the register and at a given temperature within operating temperature
         range. The PMIC bulk input supply voltage VIN_Bulk is fixed at nominal voltage of 5.0V. The regulator output current load Itdc
         = 0 A.
```

**Table 6 — SWB - Single Phase Regulator; DC + AC Specification**

```text
                    Parameter                                  Symbol              Min        Typ         Max        Unit      Notes

 Output Voltage                                                  Vout                         0.5                      V         [1]

 Maximum Continuous DC Current Load                              Itdc                0         -           1.2         A         [2]

 Maximum Peak Instantaneous Current                           Ipeakmax               -         -            2          A         [3]

 Maximum Load Transient                                          dI/dt               -         -            2        A/μs        [4]

 Regulator Output DC + AC Voltage Tolerance               Reg_DC_AC_Tol            -2.5                    2.5        %        [5],[6]

 Regulator Feedback Set Point Accuracy                     FB_Set_Point           -0.75                   0.75        %          [7]

NOTE 1   Typical voltage configured in the register Table 141, “Register 0x25,”[7:1].
NOTE 2   Measured over long period of time. Typically 1 second.
NOTE 3   Measured over short period of time. Typically > 20 μs but less than 50 μs.
NOTE 4   This parameter is applied to measure output voltage regulator DC+AC tolerance.
NOTE 5   The percentage applies to typical voltage configured in the register. The PMIC bulk input supply voltage VIN_Bulk can vary
         from minimum to maximum value specified in Table 3, “Input Supply DC + AC Specification”. The regulator output current load
         can vary maximum dI/dt value. The output ripple is inclusive in this parameter.
NOTE 6   Applies across entire PMIC operating temperature range.
NOTE 7   The percentage applies to typical voltage configured in the register and at a given temperature within operating temperature
         range. The PMIC bulk input supply voltage VIN_Bulk is fixed at nominal voltage of 5.0V. The regulator output current load Itdc

         = 0 A.
```

**Table 7 — SWC - Single Phase Regulator; DC + AC Specification**

```text
                    Parameter                                  Symbol              Min        Typ         Max        Unit      Notes

 Output Voltage                                                  Vout                         1.8                      V         [1]

 Maximum Continuous DC Current Load                              Itdc                0         -            1          A         [2]

 Maximum Peak Instantaneous Current                           Ipeakmax               -         -            2          A         [3]

 Maximum Load Transient                                          dI/dt               -         -            2        A/μs        [4]

 Regulator Output DC + AC Voltage Tolerance               Reg_DC_AC_Tol            -2.5                    2.5        %        [5],[6]

 Regulator Feedback Set Point Accuracy                     FB_Set_Point           -0.75                   0.75        %          [7]

NOTE 1   Typical voltage configured in the register Table 143, “Register 0x27,” [7:1].
NOTE 2   Measured over long period of time. Typically 1 second.
NOTE 3   Measured over short period of time. Typically > 20 μs but less than 50 μs.
NOTE 4   This parameter is applied to measure output voltage regulator DC+AC tolerance.
NOTE 5   The percentage applies to typical voltage configured in the register. The PMIC bulk input supply voltage VIN_Bulk can vary
         from minimum to maximum value specified in Table 3, “Input Supply DC + AC Specification”. The regulator output current load
         can vary maximum dI/dt value. The output ripple is inclusive in this parameter.
NOTE 6   Applies across entire PMIC operating temperature range.
NOTE 7   The percentage applies to typical voltage configured in the register and at a given temperature within operating temperature
         range. The PMIC bulk input supply voltage VIN_Bulk is fixed at nominal voltage of 5.0V. The regulator output current load Itdc
         = 0 A.
```

## 3.1.3 LDO Output Regulator Characteristics

**Table 8 — LDO Output Regulator DC + AC Specification**

```text
                    Parameter                                  Symbol              Min       Typ       Max        Unit     Notes

 1.8 V LDO Output Voltage                                    VOUT_1.8V                        1.8                  V         [1]

 1.8 V LDO Output - Maximum Output Current                  Itdc_VOUT_1.8V           -         -        25        mA         [2]

 1.0 V LDO Output Voltage                                    VOUT_1.0V                        1.0                  V         [3]

 1.0 V LDO Output - Maximum Output Current                  Itdc_VOUT_1.0V           -         -        20        mA         [4]

NOTE 1   Typical voltage is configured in register Table 147, “Register 0x2B,” [7:6]. The min and max values are guaranteed to be
         within + 100 mV of programmed value.
NOTE 2   The maximum output current represents the external load only and excludes PMIC’s own internal current consumption. The
         specified maximum output current is only applicable after PMIC’s 1.8V LDO Power Good status is good (i.e., t1.8V_Ready
         timing parameter is satisfied). Prior to PMIC’s 1.8V LDO Power Good Status (i.e., while PMIC is still ramping up the 1.8V
         LDO), the maximum output current shall be limited to maximum of 10 mA.
NOTE 3   Typical voltage is configured in register Table 147, “Register 0x2B,” [2:1]. The min and max values are guaranteed to be
         within + 50 mV of programmed value.
NOTE 4   The maximum output current represents the external load only and excludes PMIC’s own internal current consumption. The
         specified maximum output current is only applicable after PMIC’s 1.0V LDO Power Good status is good (i.e., t1.0V_Ready
         timing parameter is satisfied). Prior to PMIC’s 1.0V LDO Power Good Status (i.e., while PMIC is still ramping up the 1.0V
         LDO), the maximum output current shall be limited to maximum of 5 mA.
```
