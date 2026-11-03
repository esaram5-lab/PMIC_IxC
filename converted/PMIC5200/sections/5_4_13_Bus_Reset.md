---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 5.4.13
title: Bus Reset
pages: 118-119
---
# 5.4.13 Bus Reset

To prevent a malfunctioning device from locking up the I2C bus or I3C Basic bus, a bus reset mechanism is defined. It uses a timeout mechanism on SCL as shown in Figure 38 to force a device bus reset. All devices on a I2C or I3C Basic bus reset simultaneously. Bus reset operation works same way regardless of whether device is operating in I2C or I3C Basic mode. To guarantee the PMIC resets I2C bus or I3C Basic bus, the SCL clock input Low time has to be greater than or equal to tTIMEOUT(Max).

The PMIC does not reset I2C bus or I3C Basic bus if the SCL clock input Low time is less than tTIMEOUT(Min). If the SCL clock input Low time is between tTIMEOUT(Min) and tTIMEOUT(Max), the PMIC does not guarantee and it may or may not reset the I2C bus or I3C Basic bus. When RESET, the PMIC device takes the following actions:

```text
1.     Interface and any pending command or transactions are cleared
2.     All internal register values are preserved unless noted otherwise in item # 3 below.
3.     Device returns to I2C mode of operation; resets Table 114, Register 0x0A [3:2] = ‘00; resets
       Table 152, Register 0x30 [2] = ‘0’; resets Table 154, Register 0x32 [6] = ‘0’; resets Table 156,
       Register 0x34 [7:5] = ‘000’; and resets Table 156, Register 0x34 [3:1] = ‘111’.
4.     Device does not resample PID pin.

5.     Device floats the SDA pin such that it gets pulled High by the external or Hub device pullup resistor.
6.     Device treats bus reset as STOP operation.

                                        tTIMEOUT(Max)

     SCL                           tTIMEOUT(Min)
                                                                          Resets I2C or I3C Interface
                  VIL

     SCL
                                                                            Does Not Reset I2C or I3C Interface
                  VIL

     SCL
                                                                          May or May Not Reset I2C or I3C Interface
                  VIL
```

*Figure 38 — I2C or I3C Basic Bus Reset of PMIC* (figure; any text below/above was extracted from the drawing)
