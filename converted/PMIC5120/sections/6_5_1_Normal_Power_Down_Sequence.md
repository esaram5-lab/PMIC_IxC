---
document: JESD301-6 (PMIC5120 Power Management IC Standard, Version 1.0, February 2025)
device: PMIC5120
application: client
section: 6.5.1
title: Normal Power Down Sequence
pages: 38-39
---
# 6.5.1 Normal Power Down Sequence

Under normal operating condition with valid VIN_Bulk input supply, to disable the PMIC output regulators, the PMIC allows the following three methods for normal power down sequence.

```text
• VR_EN pin de-assertion from High to Low

• VR Disable command on I2C or I3C bus (if PMIC registers are not in secure mode)

• PWR_GOOD input from High to Low (if PWR_GOOD pin is configured as IO)
```

All three methods trigger the PMIC to generate an internal VR Disable command, after which the PMIC executes the normal power down sequence as programmed in Power Off Sequence Config0 to Power Off Sequence Config2 (Table 176, Register 0x58 to Table 178, Register 0x5A,), in DIMM vendor region MTP memory.

The PMIC requires a valid VIN_Bulk input supply (i.e., minimum of 4.25V) to execute the normal power down sequence. In a platform where the VIN_Bulk input supply ramp down rate is very slow (starting from VIN_Bulk nominal condition of 5V until it ramps down to 4.25V), the PMIC may be able to execute the normal power down sequence before the VIN_Bulk input supply is completely removed, depending on the ramp down rate, programmed soft stop time, and the delay time in the Power Off Sequence Config registers. If the VIN_Bulk ramp down is very fast (e.g. instantaneous with 0ns), the PMIC cannot execute the normal power down sequence to turn off all buck regulators.

Figure 24 shows one example of a normal power down sequence where PMIC regulators are turned off by de-asserting the VR_EN pin from high to low. The PMIC executes Power Off Sequence Config0 to Power Off Sequence Config2 (Table 176, Register 0x58 to Table 178, Register 0x5A,). The example shows the power down sequence spread out over all three Power Off Sequence Config (0 to 2) registers where only one buck regulator is turned off in each Power Off Sequence Config register. The sequence shows the order where SWA is turned off first followed by delay. Then SWB is turned off followed by delay. Lastly. SWC is turned off followed by delay. Each buck regulator follows its own timing for soft stop time, as configured.

The PMIC allows any combination where all three buck regulators can be turned off only in the first Power Off Sequence Config0 register, or one or more buck regulators can be turned off in any given Power Off Sequence Config register.

See additional details about PMIC register status, PWR_GOOD signal, as noted in Section 6.5.2 to Section 6.5.5, depending on how the PMIC is configured to operate in normal mode.

```text
  VIN_Bulk
Input Supply                                                          High;
                                                           Valid VIN_Bulk Input Supply
                                                                                                                              Low
 VR_EN Pin                                                                                                        Invalid VIN_Bulk Input Supply

     SWA

                    SWA_Soft_Stop
                   {R37[7],R22 [1:0]}
                                         Power_Off
                                        Con fig0_Delay
                                          R58 [2:0]     SWB_Soft_Sto p
                                                       {R36[5],R26 [1:0]}
     SWB

                                                                              Power_Off
                                                                            Con fig1_Delay
                                                                               R59 [2:0]      SWC_Soft_Sto p
     SWC
                                                                                             {R36[4],R28 [1:0]}

PWR_GOOD

                       Power Off Sequence                  Power Off Sequence Power Off Sequence

                            Config0                             Config1            Config2
```

*Figure 24 — Normal Power Down Sequence with VR Disable Command* (figure; any text below/above was extracted from the drawing)
