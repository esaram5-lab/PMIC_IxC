---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 6.7
title: Combinations to Turn On and Turn Off PMIC Regulators
pages: 35-35
---
# 6.7 Combinations to Turn On and Turn Off PMIC Regulators

The PMIC allows to use a combination of VR Enable/Disable command via I2C/I3C bus, VR_OE pin, Auto Power On and CAMP input signal to turn on and turn off output buck regulators. All valid combinations are shown in Table 25.

**Table 25 — Valid Combinations to Turn On and Turn Off Regulators**

```text
       Register Setting

R2F[2]     R5F[6]     R5F[5]        Turn On Regulator Command Method                       Turn Off Regulator Command Method

   0          0           0      VR Enable Command (I2C/I3C Write or                    1. Drive CAMP Input Low
                                 DEVCTRL CCC)[1]                                        2. Driving VR_OE pin Low[2]

   1          0           0                                                             1. Drive CAMP Input Low
                                                                                        2. VR Disable Command (I2C/I3C Write or
                                                                                           DEVCTRL CCC)
                                                                                        3. Configure R2F[6:3], R123[1:0] = ‘0’
                                                                                        4. Driving VR_OE Low[1]

   0          0           1      VR_OE pin Low to High[3]                               1. Driving CAMP input Low[4]
                                                                                        2. Driving VR_OE pin High to Low

   1          0           1                                                             1. Driving CAMP input Low[4]
                                                                                        2. VR Disable Command (I2C/I3C Write or
                                                                                           DEVCTRL CCC)[4]

                                                                                        3. Configure R2F[6:3], R123[1:0] = ‘0’[4]
                                                                                        4. Driving VR_OE pin High to Low

   0          1           0      First time, PMIC automatically powers up[1]            1. Drive CAMP Input Low
                                 Next time: VR Enable Command (I2C/I3C                  2. Driving VR_OE pin Low[1]

                                 Write or DEVCTRL CCC)[1]
   1          1           0                                                             1. Driving CAMP input Low
                                                                                        2. VR Disable Command (I2C/I3C Write or
                                                                                           DEVCTRL CCC)
                                                                                        3. Configure R2F[6:3], R123[1:0] = ‘0’
                                                                                        4. Driving VR_OE pin High to Low

  X           1           1      Illegal configuration                                  Illegal configuration
  NOTE 1      If VR_OE pin is High.
  NOTE 2      Assuming that VR_OE pin was High.
  NOTE 3      After VR OE pin Low to High, PMIC turns on the regulator. Subsequently, if CAMP input signal is driven low while VR_OE
              pin is high or if there is an internal fault that triggers VR Disable command, the PMIC turns off the regulator. At this point,
              PMIC allows VR Enable command via I2C or I3C bus command to turn on the regulators.
  NOTE 4      Even if VR_OE pin remains High.
```
