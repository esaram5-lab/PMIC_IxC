---
document: JESD301-6 (PMIC5120 Power Management IC Standard, Version 1.0, February 2025)
device: PMIC5120
application: client
section: 6.5.5
title: Secure Mode Operation; R1A[4] = ‘1’
pages: 46-49
---
# 6.5.5 Secure Mode Operation; R1A[4] = ‘1’

The PMIC allows host to power down any or all output regulators by any of the two methods below.

```text
1.   The VR Disable command with VR_EN pin transitions to low. The PMIC asserts PWR_GOOD signal

     Low. The PMIC executes power off sequence config0 (Table 176, Register 0x58) to power off sequence
     config2 (Table 178, Register 0x5A,) to preserve the appropriate voltage relationship as configured in
     the registers and enters in P1 state. The host can re-enable the PMIC’s output regulators by VR_EN pin

     transition to High. The PMIC exits from P1 state and executes power on sequence config 0 to config 2

     registers and floats PWR_GOOD signal after tPMIC_PWR_GOOD_OUT timing parameter is satisfied.
     See Figure 29. The PMIC does not require power cycle.
     a.   Note that VR Disable or Enable command on a I2C/I3C Basic Bus (i.e., Table 146, Register 0x32
          [7] = ‘0’ or ‘1’) has no effect on the PMIC. Also, configuring one or more bits in Table 143, Regis-
          ter 0x2F [6,4:3] to ‘0’ has no effect on the PMIC. See Figure 30.
2.   If Table 146, Register 0x32 [5] = ‘1’, driving PWR_GOOD input low. The PMIC executes power off
     sequence config0 (Table 176, Register 0x58) to power off sequence config2 (Table 178, Register
     0x5A,) to preserve the appropriate voltage relationship as configured in the registers; drives PWR_-
     GOOD signal low and unlocks only Table 146, Register 0x32 [7]. The PMIC preserves all register
     contents including the MTP error log registers and keeps all write-protected registers locked except for
     the Table 146, Register 0x32 [7]. The PMIC does not enter in P1 state. When host issues VR Enable
     command by I2C/I3C Basic bus, the PMIC executes Power on sequence config 0 to Power on sequence
     config 2 registers, floats PWR_GOOD output signal after tPMIC_PWR_GOOD_OUT timing
     parameter is satisfied and re-locks register Table 146, Register 0x32 [7]. The PMIC does not require
     power cycle to re-enable PMIC’s output regulators.
```

The PMIC, on its own, can generate internal VR Disable command at any time due to one or more events listed in Table 30 under column “Trigger VR Disable”. The PMIC executes power off sequence config0 (Table 176, Register 0x58) to power off sequence config2 (Table 178, Register 0x5A,) to preserve the appropriate voltage relationship as configured in the registers. The PMIC does not enter in P1 state. The PMIC assert PWR_GOOD signal low. The PMIC requires power cycle. The VR Enable command with either Table 146, Register 0x32 [7] = ‘1’ or VR_EN pin transitions to high has no effect on PMIC and PMIC keeps it PWR_GOOD signal low.

```text
                                                         R1A[4] = ‘0’
              High
  VIN_Bulk

              High
VOUT_1.8V

              High
 VOUT_1.0V

   2         VR Dis or EN command on the Bus has no effect
  I C/I3C

   VR_EN

       SWC

       SWB
       SWA

              High
PWR_GOOD
```

*Figure 29 — Power Down with VR_EN Pin; R1A[4]=0; Secure Mode; PWR_GOOD Signal* (figure; any text below/above was extracted from the drawing)

```text
             High                             R1A[4] = ‘0’ or ‘1’
  VIN_Bulk

             High
 VOUT_1.8V

             High
 VOUT_1.0V

   2                                   VR Dis or EN command on the Bus has no effect
  I C/I3C                     VR_DIS
             High
   VR_EN

             On; switching
       SWC

              On; switching
       SWB
             On; switching
       SWA

              High
PWR_GOOD
```

*Figure 30 — VR_DIS or VR_EN CMD on Bus; R1A[4]=x; Secure Mode; PWR_GOOD Signal* (figure; any text below/above was extracted from the drawing)

```text
                                                    R1A[4] = ‘1’
              High
  VIN_Bulk

              High
 VOUT_1.8V

              High
 VOUT_1.0V

             No VR Dis command on the Bus
  I2C/I3C

   VR_EN

    SWC

    SWB

    SWA

               High
PWR_GOOD
```

*Figure 31 — Power Down with VR_EN Pin; R1A[4]=1; Secure Mode; PWR_GOOD Signal* (figure; any text below/above was extracted from the drawing)
