---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 5.1.4
title: LDO Output Regulator Characteristics
pages: 15-16
---
# 5.1.4 LDO Output Regulator Characteristics

**Table 11 — LDO Output Regulator DC + AC Specification**

```text
                 Parameter                                 Symbol               Min       Typ       Max       Unit      Notes

1.8 V LDO Output Voltage                                 VOUT_1.8V                         1.8                  V         [1]

1.8 V LDO Output - Maximum Output Current               Itdc_VOUT_1.8V            -         -        25        mA         [2]

1.0 V LDO Output Voltage                                 VOUT_1.0V                         1.0                  V         [3]

1.0 V LDO Output - Maximum Output Current               Itdc_VOUT_1.0V            -         -        20        mA         [4]

  NOTE 1   Typical voltage is configured in register Table 148, Register 0x2B [7:6]. The min and max values are guaranteed to be
           within + 100 mV of programmed value.
  NOTE 2   The maximum output current represents the external load and excludes PMIC’s own internal current consumption. The
           specified maximum output current is only applicable after PMIC’s 1.8V LDO Power Good status is good (i.e.,
           t1.8V_Ready timing parameter is satisfied). Prior to PMIC’s 1.8V LDO Power Good status (i.e., while PMIC is still
           ramping up the 1.8 V LDO, the maximum output current load shall be limited to maximum of 10 mA.
  NOTE 3   Typical voltage is configured in register Table 148, Register 0x2B [2:1]. The min and max values are guaranteed to be
           within + 50 mV of programmed value.
  NOTE 4   The maximum output current represents the external load and excludes PMIC’s own internal current consumption. The
           specified maximum output current is only applicable after PMIC’s 1.0V LDO Power Good status is good (i.e.,
           t1.0V_Ready timing parameter is satisfied). Prior to PMIC’s 1.0V LDO Power Good status (i.e., while PMIC is still
           ramping up the 1.0V LDO), the maximum output current load shall be limited to maximum of 5 mA.
```
