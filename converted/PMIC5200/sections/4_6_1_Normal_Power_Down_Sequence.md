---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 4.6.1
title: Normal Power Down Sequence
pages: 32-34
---
# 4.6.1 Normal Power Down Sequence

Under normal operating conditions with valid VIN_Bulk input supply, to disable the PMIC output regulators, the PMIC allows following three methods for normal power down sequence.

```text
▪ VR_EN pin de-assertion from High to Low
▪ VR Disable command on I2C or I3C bus (if PMIC registers are not in secure mode)
▪ PWR_GOOD input from High to Low (if PWR_GOOD pin is configured as IO)
```

All three methods triggers the PMIC to generate internal VR Disable command and the PMIC executes the normal power down sequence as programmed in Power Off Sequence Config0 to Power Off Sequence Config3 registers (Table 200, Register 0x58 [7:0] to Table 203, Register 0x5B [7:3]) in DIMM vendor region MTP memory.

The PMIC requires valid VIN_Bulk input supply (i.e., minimum of 3.0 V) to execute normal power down sequence. In a platform where VIN_Bulk input supply ramp down rate is very slow (starting from VIN_Bulk nominal condition of 5 V until it ramps down to 3.0 V), the PMIC may be able to execute normal power down sequence before VIN_Bulk input supply is completely removed depending on the ramp down rate and programmed soft stop time and delay time in Power Off Sequence Config registers. If the VIN_Bulk ramp down is very fast (e.g., instantaneous with 0 ns), the PMIC cannot execute normal power down sequence to turn off all buck regulators. Figure 20 shows one example of normal power down sequence where PMIC regulators are turned off by de-asserting VR_EN pin from high to low. The PMIC executes Power Off Sequence Config0 to Power Off Sequence Config3 registers (Table 200, Register 0x58 to Table 203, Register 0x5B). The example shows the power down sequence spread out over all four Power Off Sequence Config (0 to 3) registers where only one buck regulator is turned off in each Power Off Sequence Config register. The sequence shows the order where SWA is turned off first followed by delay, then SWB is turned off followed by delay, then SWC is turned off followed by delay, and at last SWD is turned off. Each buck regulator follows its own timing for soft stop time as configured. The PMIC allows any combination where all four buck regulators can be turned off only in first Power Off Sequence Config0 registers or one or more buck regulators are turned off in any given Power Off Sequence Config registers. The PMIC also allows where no buck regulator is turned off in any Power Off Sequence Config to insert additional delay between Power Off Sequence Config registers.

See additional details about PMIC register status, PWR_GOOD signal as noted in Section 4.6.2 to Section 4.6.5 depending on how PMIC is configured to operate in normal mode.

```text
   VIN_Bulk

 Input Supply                                                High;
                                                   Valid VIN_Bulk Input Suplly
                                                                                                                                                               Low;
                                                                                                                                                   Invalid VIN_Bulk Input Suplly
 VR_EN Pin
High to Low

      SWA

                   SWA Soft
                   Stop Time
                               Power Off Config0
                                Delay R58[2:0]
                                                   SWB Soft
                                                   Stop Time
       SWB

                                                               Power Off Config1
                                                                Delay R59[2:0]

      SWC                                                                          SWC Soft
                                                                                   Stop Time

                                                                                                                         SWD Soft
      SWD                                                                                                                Stop Time
                                                                                                  Power Off Config3
                                                                                                   Delay R5A[2:0]

  PWR_GOOD

                Power Off Sequence Config0         Power Off Sequence              Power Off Sequence Config2         Power Off Sequence Config3
                                                        Config1
```

*Figure 20 — Normal Power Down Sequence with VR Disable Command* (figure; any text below/above was extracted from the drawing)
