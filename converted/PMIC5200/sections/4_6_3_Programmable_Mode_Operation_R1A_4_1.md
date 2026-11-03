---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 4.6.3
title: Programmable Mode Operation; R1A[4] = ‘1’
pages: 36-39
---
# 4.6.3 Programmable Mode Operation; R1A[4] = ‘1’

The PMIC allows host to power down any or all output regulators by any of the three methods below.

```text
1.       The VR Disable command (Table 154, Register 0x32 [7] = ‘0’ or VR_EN pin transitions to low).The
         PMIC executes power off sequence config0 (Table 200, Register 0x58) to power off sequence
         config3 (Table 203, Register 0x5B) to preserve the appropriate voltage relationship as configured in
         the registers and enters in P1 state. The PMIC retains the Table 152, Register 0x30 [2] value when
         entering in P1 state and restores the setting when it exits the P1 state. The PMIC controls the
         PWR_GOOD signal as follows in bullet a and bullet b:
               a. If VR Disable command with a pin (i.e., VR_EN pin transitions to Low), PMIC asserts
                   PWR_GOOD signal Low. The host can re-enable the PMIC’s output regulators by VR_EN
                   pin transition to High. The PMIC exits from P1 state and executes power on sequence
                   config 0 to power on sequence config 2 registers and floats PWR_GOOD signal after
                   tPMIC_PWR_GOOD_OUT timing parameter is satisfied. See Figure 23. The PMIC does
                   not require power cycle.

            b. If VR Disable command on a I2C/I3C Basic Bus (i.e., Table 154, Register 0x32 [7] = ‘0’),
               PMIC keeps the PWR_GOOD signal floating because this is an intentional command from
               the host and not a fault condition. The PMIC exits from P1 state with only VR_EN pin
               transition to High. The host can re-enable the PMIC’s output regulators by VR_EN pin
               transition to High and PMIC executes power on sequence config 0 to power on sequence
               config 3 registers. The PMIC continues to float PWR_GOOD signal until tPMIC_PWR_-
               GOOD_OUT timing parameter is satisfied and at that point PMIC assumes normal control
               of PWR_GOOD signal. See Figure 24. The PMIC does not require power cycle.
            c.   The simultaneous usage of VR_EN pin and I2C/I3C bus command to turn on/off the PMIC
                 is not allowed. If the VR_EN pin transitions to Low first, the PWR_GOOD signal follows as
                 described in bullet a and PWR_GOOD signal remains low even if there is a subsequent
                 I2C/I3C bus command as described in bullet b.
2.    Configuring one or more bits in Table 151, Register 0x2F [6:3] to ‘0’ in any specific sequence that is
      desired by the host. The PMIC does not execute power off sequence config0 (Table 200, Register
      0x58) to power off sequence config3 (Table 203, Register 0x5B) on its own. The PMIC keeps the
      PWR_GOOD signal floating because this is intentional command from the host and not a fault
      condition. Note that host can re-enable any of disabled output regulators by configuring one or more
      bits in Table 151, Register 0x2F [6:3] to ‘1’ in any specific sequence that is desired by the host. The
      PMIC keeps the PWR_GOOD signal floating. The PWR_GOOD signal behavior is same as in
      Figure 24.

3.    If Table 154, Register 0x32 [5] = ‘1’, driving PWR_GOOD input low. The PMIC executes power off
      sequence config0 (Table 200, Register 0x58) to power off sequence config3 (Table 203, Register

      0x5B) to preserve the appropriate voltage relationship as configured in the registers and drives
      PWR_GOOD signal low. The PMIC preserves all register contents including the MTP error log

      registers. The PMIC does not enter in P1 state. If host re-enables PMIC’s output regulators by
      issuing VR_EN command on I2C/I3C Basic bus (i.e., Table 154, Register 0x32 [7] = ‘1’), the PMIC
      executes power on sequence config 0 to power on sequence config 3 registers and floats
      PWR_GOOD signal after tPMIC_PWR_GOOD_OUT timing parameter is satisfied. The PMIC does
      not require power cycle.
```

The PMIC, on its own, can generate internal VR Disable command at any time due to one or more events listed in Table 27 under column “Trigger VR Disable”. The PMIC executes power off sequence config0 (Table 200, Register 0x58) to power off sequence config3 (Table 203, Register 0x5B) to preserve the appropriate voltage relationship as configured in the registers. The PMIC does not enter in P1 state. The PMIC assert PWR_GOOD signal low. The host can re-enable PMIC’s output regulators with VR Enable command with either Table 154, Register 0x32 [7] = ‘1’ or VR_EN pin transitions to high and PMIC turns on its output regulators and floats PWR_GOOD signal. The PMIC does not require power cycle.

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

PWR_GOOD
```

*Figure 23 — Power Down with VR_EN Pin; R1A[4]=1; Program. Mode; PWR_GOOD Signal* (figure; any text below/above was extracted from the drawing)

```text
                High                                   R1A[4] = ‘1’
     VIN_Bulk

                High
    VOUT_1.8V

                High
    VOUT_1.0V

     I2C/I3C                 VR_DIS

      VR_EN

       SWC

       SWB

       SWA

                 High
PWR_GOOD
```

*Figure 24 — Power Down with VR_DIS; R1A[4]=1; Program. Mode; PWR_GOOD Signal* (figure; any text below/above was extracted from the drawing)
