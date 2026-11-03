---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 6.27
title: PMIC Address ID (PID)
pages: 58-58
---
# 6.27 PMIC Address ID (PID)

The PMIC has PID input pin which allows to assign up to three different unique ID for I2C and I3C Basic protocol. At first power on, when VIN_Mgmt input is applied, the PMIC automatically senses its ID as shown in Table 34.

**Table 34 — PMIC ID**

```text
PID Pin Connection on DIMM Board            PMIC ID                  Comment

           short to GND                    PID = 1001

             Floating                      PID = 1000

            short to 1.8                   PID = 1100    Connected to PMIC’s VOUT_1.8V Rail
```
