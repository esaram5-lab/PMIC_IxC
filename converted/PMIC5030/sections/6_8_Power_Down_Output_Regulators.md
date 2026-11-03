---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 6.8
title: Power Down Output Regulators
pages: 35-39
---
# 6.8 Power Down Output Regulators

Regardless of how PMIC’s output regulators are turned on, the PMIC’s output regulators are powered down as described below depending on mode of operation.

## 6.8.1 Normal Power Down Sequence

Under normal operating condition with valid VIN_Bulk input supply, to disable the PMIC output regulators, the PMIC allows following three methods for normal power down sequence.

```text
▪ VR_OE pin de-assertion to Low
▪ VR Disable command on I2C or I3C bus (if PMIC is non-write-protect mode)
▪ CAMP input from High to Low
```

All three methods trigger the PMIC to generate internal VR Disable command and the PMIC executes the normal power down sequence as programmed in Power Off Sequence Config0 to Power Off Sequence Config5 registers (Table 256, Register 0x58 to Table 260, Register 0x5C, Table 266, Register 0x62) in DIMM vendor region MTP memory. The PMIC requires valid VIN_Bulk input supply (i.e., minimum of 4.25 V) to execute normal power down sequence. In a platform where VIN_Bulk input supply ramp down rate is very slow (starting from VIN_Bulk nominal condition of 12 V until it ramps down to 4.25 V), the PMIC may be able to execute normal power down sequence before VIN_Bulk input supply is completely removed depending on the ramp down rate and programmed soft stop time and delay time in Power Off Sequence Config registers. If VIN_Bulk ramp down is very fast (e.g., instantaneous with 0ns), the PMIC cannot execute normal power down sequence to turn off the buck regulators. Figure 19 shows one example of normal power down sequence where PMIC regulators are turned off by VR Disable command (PMIC is in non-write-protect mode) on I2C bus. The PMIC executes Power Off Sequence Config0 to Power Off Sequence Config3 registers (Table 256, Register 0x58 to Table 259, Register 0x5B). The example shows the power down sequence spread out over four Power Off Sequence Config (0 to 3) registers where only one buck regulator is turned off in each Power Off Sequence Config registers. The sequence shows the order where SWA is turned off first followed by delay, then SWB is turned off followed by delay, then SWC is turned off followed by delay and at last SWD is turned off. Each buck regulator follows its own timing for soft stop time as configured. The example assumes only four buck regulators were turn on in Power On Sequence Config registers.

The PMIC allows any combination where all regulators can be turned off only in first Power Off Sequence Config0 registers or one or more buck regulators are turned off in any given Power Off Sequence Config registers. The PMIC also allows where no buck regulators are turned off in any Power Off Sequence Config to insert additional delay between Power Off Sequence Config registers.

VIN_Bulk

```text
 Input Supply                                                      High;
                                                         Valid VIN_Bulk Input Suplly                                                                                 Low;
                                                                                                                                                         Invalid VIN_Bulk Input Suplly
                       High
    VR_OE

I2C/I3C Bus     VR Disable
   CMD          (R32[7] =0)

      SWA

                         SWA Sof t
                         Stop Time
                                     Power Off Config0
                                      Delay R58[2:0]
                                                         SWB Soft
                                                         Stop Time
       SWB

                                                                     Power Off Config1
                                                                      Delay R59[2:0]

      SWC                                                                                SWC Soft
                                                                                         Stop Time

                                                                                                                               SWD Soft
     SWD                                                                                                                       Stop Time
                                                                                                        Power Off Config2
                                                                                                         Delay R5A[2 :0]
                       High
    CAMP
                      Power Off Sequence Config0         Power Off Sequence              Power Off Sequence Config2         Power Off Sequence Config3
                                                              Config1
```

*Figure 19 — Normal Power Down Sequence with VR Disable Command* (figure; any text below/above was extracted from the drawing)

## 6.8.2 Non Write-Protect Mode - Turning Off Buck Regulators

In non write-protect mode of operation, the PMIC allows host to power off any or all output regulators. The host can disable PMIC’s any or all output regulators by any of the four methods below.

1. The VR Disable command (Table 155, Register 0x32 [7] = ‘0’). The PMIC executes power off sequence config0 to power off sequence config5 (Table 256, Register 0x58 to Table 260, Register 0x5C, Table 266, Register 0x62) to preserve the appropriate voltage relationship as configured by the DIMM vendors. The PMIC keeps the CAMP signal floating (i.e., it remains High) because this is an intentional command from the host and not a fault condition. Note that host can re-enable the PMIC’s output regulator by issuing VR Enable command. The PMIC executes power on sequence config 0 to config 5 registers and keeps the CAMP signal floating (i.e., it remains High).

2. Configuring one or more bits in Table 152, Register 0x2F [6:3],Table 191, Register 0x123 [1:0] to ‘0’ in any specific sequence that is desired by the host. The PMIC does not execute power off sequence config0 (Table 256, Register 0x58) to power off sequence config5 (Table 260, Register 0x5C, Table 266, Register 0x62) on its own. The PMIC keeps the CAMP signal floating (i.e., it remains High) because this is intentional command from the host and not a fault condition. Note that host can re-enable any of disabled output regulators by configuring one or more bits in Table 152, Register 0x2F [6:3],Table 191, Register 0x123 [1:0] to ‘1’ in any specific sequence that is desired by the host. The PMIC keeps the CAMP signal floating (i.e., it remains High).

3. By driving CAMP input low. The PMIC executes power off sequence config0 to power off sequence config5 (Table 256, Register 0x58 to Table 260, Register 0x5C, Table 266, Register 0x62) to preserve the appropriate voltage relationship as configured by the DIMM vendors.

4. By driving VR_OE input low. The PMIC executes power off sequence config0 to power off sequence config5 (Table 256, Register 0x58 to Table 260, Register 0x5C, Table 266, Register 0x62) to preserve the appropriate voltage relationship as configured by the DIMM vendors and asserts CAMP signal Low.

## 6.8.3 Write-Protect Mode - Turning Off Regulators

In write-protect mode of operation, the host can disable PMIC’s all enabled output regulators by any of the three methods below.

1. Power cycle the PMIC.

2. By driving CAMP input low. The PMIC executes power off sequence config0 to power off sequence config5 (Table 256, Register 0x58 to Table 259, Register 0x5B, Table 266, Register 0x62) to preserve the appropriate voltage relationship as configured by the DIMM vendors.

3. By driving VR_OE input low (if Table 263, Register 0x5F [5] = ‘1’). The PMIC executes power off sequence config0 to power off sequence config5 (Table 256, Register 0x58 to Table 259, Register 0x5B, Table 266, Register 0x62) to preserve the appropriate voltage relationship as configured by the DIMM vendors and asserts CAMP signal Low.

## 6.8.4 Power Down Output Regulators Due to Fault Condition

Regardless of the either mode of the operation, the PMIC, on its own, can generate VR Disable command at any time due to one or more events listed in Table 27 under column “Trigger VR Disable”. The PMIC executes power off sequence config0 to power off sequence config5 (Table 256, Register 0x58 to

Table 259, Register 0x5B, Table 266, Register 0x62) to preserve the appropriate voltage relationship as configured by the DIMM vendors and asserts CAMP signal Low. The PMIC may also reset its Vbias LDO regulator. Figure 20shows the timing relationship once the PMIC registers VR Disable command internally due to fault. The waveform shows each buck regulator output soft stop time and delay time once the soft stop time expires from each power off sequence config0 to power off sequence config5 registers. Note that if more than one regulators are disabled in a power off sequence config register and if those regulators have different soft stop time programmed, then the larger value of that soft stop time is used as a reference for delay timer to start. Each regulator will still follow different soft stop time to turn off the buck regulator. The specific example in Figure 20 uses only three power off sequence config0 to config2 registers and only one buck regulator is disabled in power off sequence config 2 register. The power off sequence config 0 register disables three phase regulator for SWA, SWB and SWE and power off sequence config2 register disables dual phase regulator SWC and SWF.

```text
VR Disable

  SWABE

                SWAB_So ft_Stop
                   R22 [1:0]
                                    Power_Off
                                  Config0_Delay
                                     R58 [2:0]  SWC_Soft_Sto p
   SWCF                                           R26 [1:0]

                                                                   Power_Off
                                                                 Config1_Delay
                                                                    R59 [2:0]
   SWD                                                                           SWD_Soft_Stop
                                                                                   R28 [1:0]

 CAMP
                   Power Off Sequence             Power Off Sequence Power Off Sequence
                        Config0                        Config1            Config2
```

*Figure 20 — PMIC Power Off Timing Due to Internal Fault Condition* (figure; any text below/above was extracted from the drawing)

## 6.8.5 Power Down Output Regulators During Power On Sequence

During power on as described in clause 6.2 it is possible that PMIC can trigger VR Disable command on its own as described in Table 27, Events Interrupt Summary when one or more regulators are already turned on even while other remaining output regulators are not yet turned on because PMIC has not completed the power on sequence config registers. For these types of cases, the PMIC will not execute the remaining power on sequence config registers and will immediately jump to executing the power off sequence config0 to power off sequence config5 registers. The PMIC will update the status registers and error log registers appropriately as normal because it generated VR Disable command on its own. The CAMP output signal would remain low.
