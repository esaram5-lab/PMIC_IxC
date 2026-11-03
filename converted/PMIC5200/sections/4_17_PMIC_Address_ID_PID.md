---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 4.17
title: PMIC Address ID (PID)
pages: 70-70
---
# 4.17 PMIC Address ID (PID)

The PMIC5200 has PID input pin which allows to assign up to three different unique ID for I2C and I3C Basic protocol. At first power on, when VIN_Bulk input is applied, the PMIC automatically determines its ID. The PMIC offers three different ID as shown in Table 34.

**Table 34 — PMIC ID**

```text
PID Pin Connection on CAMM2 Board            PMIC ID                   Comment

              short to GND                PID = 1001

                Floating                  PID = 1000

               short to 1.8               PID = 1100       Connected to PMIC’s VOUT_1.8V Rail
```
