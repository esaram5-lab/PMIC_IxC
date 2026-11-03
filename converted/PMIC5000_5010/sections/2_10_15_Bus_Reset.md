---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 2.10.15
title: Bus Reset
pages: 89-90
---
# 2.10.15 Bus Reset

To prevent a malfunctioning device from locking up the I2C bus or I3C Basic bus, a bus reset mechanism is defined. It uses a timeout mechanism on SCL as shown in Figure 25 to force a device bus reset. All devices on a I2C or I3C Basic bus reset simultaneously. Bus reset operation works same way regardless of whether device is operating in I2C or I3C Basic mode.

To guarantee the device resets I2C bus or I3C Basic bus, the SCL clock input Low time has to be greater than or equal to tTIMEOUT(Max).

The PMIC device does not reset I2C bus or I3C Basic bus if the SCL clock input Low time is less than tTIMEOUT(Min). If the SCL clock input Low time is between tTIMEOUT(Min) and tTIMEOUT(Max), the PMIC device does not guarantee and it may or may not reset the I2C bus or I3C Basic bus. When RESET, the PMIC device takes following action.

```text
1. Interface and any pending command or transactions are cleared
2. All internal register values are preserved unless noted otherwise in item # 3 below.
3.    Device returns to I2C mode of operation; Table 142, “Register 0x34” [3:1] resets to ‘111’;
   Table 142, “Register 0x34” [7:5] resets to ‘000’; Table 140, “Register 0x32” [6] to ‘0’;
   Table 100, “Register 0x0A” [3:2] to ‘00’.
4. Device does not re-sample PID pin.
5. Device floats the SDA pin such that it gets pulled High by external/other device pullup.
6. Device treats bus reset as STOP operation.

                                       tTIMEOUT(Max)

SCL                              tTIMEOUT(Min)

                                                                            Resets I2C/I3C Interface
               VIL

SCL
                                                                              Does Not Reset I2C/I3C Interface
               VIL

SCL
                                                                           May or May Not Reset I2C/I3C Interface
               VIL
```

*Figure 25 — I2C or I3C Basic Bus Reset - PMIC Device* (figure; any text below/above was extracted from the drawing)
