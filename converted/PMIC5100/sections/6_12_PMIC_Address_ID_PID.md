---
document: JESD301-2 (PMIC5100 Power Management IC Standard, Rev. 1.03, October 2022)
device: PMIC5100
application: client
section: 6.12
title: PMIC Address ID (PID)
pages: 61-61
---
# 6.12 PMIC Address ID (PID)

The DDR5 PMIC has PID input pin which allows to assign up to three different unique ID for I2C and I3C Basic protocol. At first power on, when VIN_Bulk input is applied, the PMIC automatically determines its ID. The PMIC offers three different ID as shown in Table 31.

**Table 31 — PMIC ID**

```text
PID Pin Connection on DIMM Board              PMIC ID                    Comment
            short to GND                      PID = 1001            PMIC can be configured
              Floating                        PID = 1000
             short to 1.8                     PID = 1100      Connected to PMIC’s VOUT_1.8V Rail
```
