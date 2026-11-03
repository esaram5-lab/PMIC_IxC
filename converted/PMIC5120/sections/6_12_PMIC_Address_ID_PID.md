---
document: JESD301-6 (PMIC5120 Power Management IC Standard, Version 1.0, February 2025)
device: PMIC5120
application: client
section: 6.12
title: PMIC Address ID (PID)
pages: 64-65
---
# 6.12 PMIC Address ID (PID)

The DDR5 PMIC has PID input pin which allows to assign up to three different unique ID for I2C and I3C Basic protocol. At first power on, when VIN_Bulk input is applied, the PMIC automatically determines its ID. The PMIC offers three different ID as shown in Table 35.

**Table 35 — PMIC ID**

```text
PID Pin Connection on DIMM Board                PMIC ID                          Comment
              Short to GND                      PID = 1001                PMIC can be configured
                Floating                        PID = 1000
               Short to 1.8                     PID = 1100          Connected to PMIC’s VOUT_1.8V Rail
```
