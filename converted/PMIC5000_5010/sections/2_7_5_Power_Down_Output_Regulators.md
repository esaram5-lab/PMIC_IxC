---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 2.7.5
title: Power Down Output Regulators
pages: 30-31
---
# 2.7.5 Power Down Output Regulators

Regardless of how PMIC’s output regulators are turned on, the PMIC’s output regulators are powered down as described below depending on mode of operation. In non write protect mode of operation, the PMIC allows host to power down any or all output regulators in non write protect mode. The host can disable PMIC’s any or all output regulators by any of the three methods below.

```text
1. The VR Disable command (Table 140, “Register 0x32” [7] = ‘0’).The PMIC executes power off sequence
   config0        (Table 169,       “Register     0x58”)       to      power      off      sequence     config3
   (Table 172, “Register 0x5B”) to preserve the appropriate voltage relationship as configured by the DIMM
   vendors. The PMIC keeps the CAMP signal floating (i.e., it remains High) because this is an intentional
   command from the host and not a fault condition. Note that host can re-enable the PMIC’s output regulator
   by issuing VR Enable command. The PMIC executes power on sequence config 0 to config 3 registers and
   keeps the CAMP signal floating (i.e it remains High).
2. Configuring one or more bits in Table 137, “Register 0x2F” [6:3] to ‘0’ in any specific sequence that is
   desired by the host.The PMIC does not execute power off sequence config0 (Table 169, “Register 0x58”) to
   power off sequence config3 (Table 172, “Register 0x5B”) on its own. The PMIC keeps the CAMP signal
   floating (i.e it remains High) because this is intentional command from the host and not a fault condition.
   Note that host can re-enable any of disabled output regulators by configuring one or more bits in Table 137,
   “Register 0x2F” [6:3] to ‘1’ in any specific sequence that is desired by the host. The PMIC keeps the CAMP
   signal floating (i.e., it remains High).
3.          By driving CAMP input low. The PMIC executes power off sequence config0
   (Table 169, “Register 0x58”) to power off sequence config3 (Table 172, “Register 0x5B”) to preserve the
   appropriate voltage relationship as configured by the DIMM vendors.
```

In write protect mode of operation, the host can disable PMIC’s all enabled output regulators by any of the two methods below.

```text
1. Power cycle the PMIC.

2. By driving CAMP input low. The PMIC executes power off sequence config0 (Table 169, “Register 0x58”)
   to power off sequence config3 (Table 172, “Register 0x5B”) to preserve the appropriate voltage relationship

   as configured by the DIMM vendors.
```

Regardless of the either mode of the operation, the PMIC, on its own, can generate VR Disable command at any time due to one or more events listed in Table 27 under column “Trigger VR Disable”. The PMIC executes power off sequence config0 (Table 169, “Register 0x58”) to power off sequence config3 (Table 172, “Register 0x5B”) to preserve the appropriate voltage relationship as configured by the DIMM vendors. The PMIC may also reset its Vbias LDO regulator. Figure 16 shows the timing relationship once the PMIC registers VR Disable command internally due to fault. The waveform shows each buck regulator output soft stop time and delay time once the soft stop time expires from each power off sequence config0 to power off sequence config3 registers. Note that if more than one regulators are disabled in a power off sequence config register and if those regulators have different soft stop time programmed, then the larger value of that soft stop time is used as a reference for delay timer to start. Each regulator will still follow different soft stop time to turn off the buck regulator. The specific example in Figure 16 uses only three power off sequence config0 to config2 registers and only one buck regulator is disabled in power off sequence config 1 register and power off sequence config 2 register. The power off sequence config 0 register disables dual phase regulator for SWA and SWB.

```text
VR Disable

  SWAB

                 SWAB_Soft_Stop
                   R22 [1:0]
                                   Power_Off
                                  Config0_Delay
                                    R58 [2:0]   SWC_Soft_Stop
    SWC                                           R26 [1:0]

                                                                 Power_Off
                                                                Config1_Delay
                                                                  R59 [2:0]
   SWD                                                                            SWD_Soft_Stop
                                                                                    R28 [1:0]

 CAMP

                    Power Off Sequence           Power Off Sequence Power Off Sequence
                         Config0
                                                    ngConfig1            Config2
```

*Figure 16 — PMIC Power Off Timing Due to Internal Fault Condition* (figure; any text below/above was extracted from the drawing)
