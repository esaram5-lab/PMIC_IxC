---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 7.8
title: Bus Reset
pages: 112-113
---
# 7.8 Bus Reset

To prevent a malfunctioning device from locking up the I2C bus or I3C Basic bus, a bus reset mechanism is defined. It uses a timeout mechanism on SCL as shown in Figure 29 to force a device bus reset. All devices on a I2C or I3C Basic bus reset simultaneously. Bus reset operation works same way regardless of whether device is operating in I2C or I3C Basic mode. To guarantee the device resets I2C bus or I3C Basic bus, the SCL clock input Low time has to be greater than or equal to tTIMEOUT(Max).

The PMIC device does not reset I2C bus or I3C Basic bus if the SCL clock input Low time is less than tTIMEOUT(Min).

If the SCL clock input Low time is between tTIMEOUT(Min) and tTIMEOUT(Max), the PMIC device does not guarantee and it may or may not reset the I2C bus or I3C Basic bus. When RESET, the PMIC device takes following actions.

1. Interface and any pending command or transactions are cleared

2. All internal register values are preserved unless noted otherwise in item # 3 below.

3. Device returns to I2C mode of operation; resets Table 115, Register 0x0A [3:2] to ‘00’, Table 153, Register 0x30 [2] to ‘0’, Table 155, Register 0x32 [6] to ‘0’, Table 158, Register 0x34 [7:5] resets to ‘000’, Table 158, Register 0x34 [3:1] resets to ‘111’.

4. Device does not re-sample PID pin.

5. Device floats the SDA pin such that it gets pulled High by external/other device pullup.

6. Device treats bus reset as STOP operation.

```text
                                        tTIMEOUT(Max)

SCL                             tTIMEOUT(Min)
                                                                     Resets I2C/I3C Interface
            VIL

SCL
                                                                       Does Not Reset I2C/I3C Interface
             VIL

SCL
                                                                     May or May Not Reset I2C/I3C Interface
             VIL
```

*Figure 29 — I2C or I3C Basic Bus Reset - PMIC Device* (figure; any text below/above was extracted from the drawing)
