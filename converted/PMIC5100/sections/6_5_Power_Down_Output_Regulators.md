---
document: JESD301-2 (PMIC5100 Power Management IC Standard, Rev. 1.03, October 2022)
device: PMIC5100
application: client
section: 6.5
title: Power Down Output Regulators
pages: 36-46
---
# 6.5 Power Down Output Regulators

Regardless of how PMIC’s output regulators are turned on (with VR_EN pin or with VR Enable command on I2C/ I3C Basic bus), the PMIC’s output regulators are powered down as described below depending on PMIC’s mode of operation.

## 6.5.1 Programmable Mode Operation; R1A[4] = ‘0’

The PMIC allows host to power down any or all output regulators by any of the three methods below.

```text
1. The VR Disable command (Table 138, “Register 0x32” [7] = ‘0’ or VR_EN pin transitions to low).The PMIC
   executes power off sequence config0 (Table 167, “Register 0x58”) to power off sequence config2
   (Table 169, “Register 0x5A”) to preserve the appropriate voltage relationship as configured in the registers.
   The PMIC controls the PWR_GOOD signal as following in bullet a and bullet b:
         a.   If VR Disable command with a pin (i.e., VR_EN pin transitions to Low), PMIC asserts PWR_-
              GOOD signal Low. The host can re-enable the PMIC’s output regulators by VR_EN pin transition
              to High. The PMIC executes power on sequence config 0 to power on sequence config 2 registers
              and floats PWR_GOOD signal after tPMIC_PWR_GOOD_OUT timing parameter is satisfied. See
              Figure 26. The PMIC does not require power cycle.
         b.   If VR Disable command on a I2C/I3C Bus (i.e., Table 138, “Register 0x32” [7] = ‘0’), PMIC keeps
              the PWR_GOOD signal floating because this is an intentional command from the host and not a
              fault condition. The host can re-enable the PMIC’s output regulators by issuing VR_EN command
              on the I2C/I3C bus (i.e., Table 138, “Register 0x32” [7] = ‘1’). The PMIC executes power on
              sequence config 0 to power on sequence config 2 registers and continues to float the PWR_GOOD
              signal until tPMIC_PWR_GOOD_OUT time at which point, PMIC assumes normal control of

              PWR_GOOD signal. See Figure 27. The PMIC does not require power cycle.
         c.   The simultaneous usage of VR_EN pin and I2C/I3C bus command to turn on/off the PMIC is not

              allowed. If the VR_EN pin transitions to Low first, the PWR_GOOD signal follows as described in
              bullet a and PWR_GOOD signal remains low even if there is a subsequent I2C/I3C bus command

              as described in bullet b.
2. Configuring one or more bits in Table 135, “Register 0x2F” [6,4:3] to ‘0’ in any specific sequence that is
   desired by the host.The PMIC does not execute power off sequence config0 (Table 167, “Register 0x58”) to
   power off sequence config2 (Table 169, “Register 0x5A”) on its own. The PMIC keeps the PWR_GOOD
   signal floating because this is intentional command from the host and not a fault condition. Note that host
   can re-enable any of disabled output regulators by configuring one or more bits in Table 135, “Register
   0x2F” [6,4:3] to ‘1’ in any specific sequence that is desired by the host. The PMIC keeps the PWR_GOOD
   signal floating. The PWR_GOOD signal behavior is same as in Figure 27.
3. If Table 138, “Register 0x32” [5] = ‘1’, driving PWR_GOOD input low. The PMIC executes power off
   sequence config0 (Table 167, “Register 0x58”) to power off sequence config2 (Table 169, “Register 0x5A”)
   to preserve the appropriate voltage relationship as configured in the registers and drives PWR_GOOD signal
   low. The PMIC preserves all register contents including the MTP error log registers. If host re-enables
   PMIC’s output regulators by issuing VR_EN command on the I2C/I3C Basic bus (i.e., Table 138, “Register
   0x32” [7] = ‘1’), the PMIC executes power on sequence config 0 to power on sequence config 2 registers and
   floats PWR_GOOD output signal after tPMIC_PWR_GOOD_OUT timing parameter is satisfied. The PMIC
   does not require power cycle.
```

The PMIC, on its own, can generate internal VR Disable command at any time due to one or more events listed in Table 28 under column “Trigger VR Disable”. The PMIC executes power off sequence config0 (Table 167, “Register 0x58”) to power off sequence config2 (Table 169, “Register 0x5A”) to preserve the appropriate voltage relationship as configured in the registers. The PMIC asserts PWR_GOOD signal low. The host can re-enable PMIC’s output regulators with VR Enable command with either Table 138, “Register 0x32” [7] = ‘1’ or VR_EN pin transitions to high and PMIC turns on its output regulators and floats PWR_GOOD signal. The PMIC does not require power cycle.

```text
                                                R1A[4] = ‘0’
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

*Figure 26 — Power Down with VR_EN Pin; R1A[4]=0; Program Mode; PWR_GOOD Signal* (figure; any text below/above was extracted from the drawing)

```text
               High                                 R1A[4] = ‘0’
  VIN_Bulk

               High
 VOUT_1.8V

               High
  VOUT_1.0V

   I2C/I3C                   VR_DIS                                         VR_EN
               High
   VR_EN

       SWC

       SWB
    SWA

               High
PWR_GOOD
```

*Figure 27 — Power Down with VR_DIS; R1A[4]=0; Program. Mode; PWR_GOOD Signal* (figure; any text below/above was extracted from the drawing)

## 6.5.2 Programmable Mode Operation; R1A[4] = ‘1’

The PMIC allows host to power down any or all output regulators by any of the three methods below.

```text
1. The VR Disable command (Table 138, “Register 0x32” [7] = ‘0’ or VR_EN pin transitions to low).The PMIC
   executes power off sequence config0 (Table 167, “Register 0x58”) to power off sequence config2
   (Table 169, “Register 0x5A”) to preserve the appropriate voltage relationship as configured in the registers
   and enters in P1 state. The PMIC controls the PWR_GOOD signal as following in bullet a and bullet b:
            a.     If VR Disable command with a pin (i.e., VR_EN pin transitions to Low), PMIC asserts PWR_-
                   GOOD signal Low. The host can re-enable the PMIC’s output regulators by VR_EN pin transition
                   to High. The PMIC exits from P1 state and executes power on sequence config 0 to power on
                   sequence config 2 registers and floats PWR_GOOD signal after tPMIC_PWR_GOOD_OUT
                   timing parameter is satisfied. See Figure 28. The PMIC does not require power cycle.

         b.   If VR Disable command on a I2C/I3C Basic Bus (i.e., Table 138, “Register 0x32” [7] = ‘0’), PMIC
              keeps the PWR_GOOD signal floating because this is an intentional command from the host and
              not a fault condition. The PMIC exits from P1 state with only VR_EN pin transition to High. The
              host can re-enable the PMIC’s output regulators by VR_EN pin transition to High and PMIC
              executes power on sequence config 0 to power on sequence config 2 registers. The PMIC continues
              to float PWR_GOOD signal until tPMIC_PWR_GOOD_OUT timing parameter is satisfied and at
              that point PMIC assumes normal control of PWR_GOOD signal. See Figure 29. The PMIC does
              not require power cycle.
         c.   The simultaneous usage of VR_EN pin and I2C/I3C bus command to turn on/off the PMIC is not
              allowed. If the VR_EN pin transitions to Low first, the PWR_GOOD signal follows as described in
              bullet a and PWR_GOOD signal remains low even if there is a subsequent I2C/I3C bus command
              as described in bullet b.
2. Configuring one or more bits in Table 135, “Register 0x2F” [6,4:3] to ‘0’ in any specific sequence that is
   desired by the host.The PMIC does not execute power off sequence config0 (Table 167, “Register 0x58”) to
   power off sequence config2 (Table 169, “Register 0x5A”) on its own. The PMIC keeps the PWR_GOOD
   signal floating because this is intentional command from the host and not a fault condition. Note that host
   can re-enable any of disabled output regulators by configuring one or more bits in Table 135, “Register
   0x2F” [6,4:3] to ‘1’ in any specific sequence that is desired by the host. The PMIC keeps the PWR_GOOD
   signal floating. The PWR_GOOD signal behavior is same as in Figure 29.
3. If Table 138, “Register 0x32” [5] = ‘1’, driving PWR_GOOD input low. The PMIC executes power off
   sequence config0 (Table 167, “Register 0x58”) to power off sequence config2 (Table 169, “Register 0x5A”)
   to preserve the appropriate voltage relationship as configured in the registers and drives PWR_GOOD signal

   low. The PMIC preserves all register contents including the MTP error log registers. The PMIC does not
   enter in P1 state. If host re-enables PMIC’s output regulators by issuing VR_EN command on I2C/I3C Basic
   bus (i.e., Table 138, “Register 0x32” [7] = ‘1’), the PMIC executes power on sequence config 0 to power on

   sequence config 2 registers and floats PWR_GOOD signal after tPMIC_PWR_GOOD_OUT timing
   parameter is satisfied. The PMIC does not require power cycle.
```

The PMIC, on its own, can generate internal VR Disable command at any time due to one or more events listed in Table 28 under column “Trigger VR Disable”. The PMIC executes power off sequence config0 (Table 167, “Register 0x58”) to power off sequence config2 (Table 169, “Register 0x5A”) to preserve the appropriate voltage relationship as configured in the registers. The PMIC does not enter in P1 state. The PMIC assert PWR_GOOD signal low. The host can re-enable PMIC’s output regulators with VR Enable command with either Table 138, “Register 0x32” [7] = ‘1’ or VR_EN pin transitions to high and PMIC turns on its output regulators and floats PWR_GOOD signal. The PMIC does not require power cycle.

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

*Figure 28 — Power Down with VR_EN Pin; R1A[4]=1; Program. Mode; PWR_GOOD Signal* (figure; any text below/above was extracted from the drawing)

```text
               High                                          R1A[4] = ‘1’
   VIN_Bulk

               High
 VOUT_1.8V

               High
  VOUT_1.0V

   I2C/I3C                     VR_DIS

    VR_EN

       SWC

       SWB

       SWA

                High
PWR_GOOD
```

*Figure 29 — Power Down with VR_DIS; R1A[4]=1; Program. Mode; PWR_GOOD Signal* (figure; any text below/above was extracted from the drawing)

## 6.5.3 Secure Mode Operation; R1A[4] = ‘0’

The PMIC allows host to power down any or all output regulators by any of the two methods below.

```text
1. The VR Disable command with VR_EN pin transitions to low. The PMIC asserts PWR_GOOD signal Low.
   The PMIC executes power off sequence config0 (Table 167, “Register 0x58”) to power off sequence config2
   (Table 169, “Register 0x5A”) to preserve the appropriate voltage relationship as configured in the registers.
   The host can re-enable the PMIC’s output regulators by VR_EN pin transition to High. The PMIC executes
   power on sequence config 0 to power on sequence config 2 registers and floats PWR_GOOD signal after
   tPMIC_PWR_GOOD_OUT timing parameter is satisfied. See Figure 30. The PMIC does not require power
   cycle.
            a.      Note that VR Disable or Enable command on a I2C/I3C Basic Bus (i.e., Table 138, “Register 0x32”
                    [7] = ‘0’ or ‘1’) has no effect on the PMIC. Also, configuring one or more bits in
                    Table 135, “Register 0x2F” [6,4:3] to ‘0’ has no effect on the PMIC. See Figure 31.

2. If Table 138, “Register 0x32” [5] = ‘1’, driving PWR_GOOD input low. The PMIC executes power off
   sequence config0 (Table 167, “Register 0x58”) to power off sequence config2 (Table 169, “Register 0x5A”)
   to preserve the appropriate voltage relationship as configured in the registers; drives PWR_GOOD signal
   low and unlocks only Table 138, “Register 0x32” [7]. The PMIC preserves all register contents including the
   MTP error log registers and keeps all write protect registers locked except for the Table 138, “Register 0x32”
   [7]. When host issues VR Enable command by I2C/I3C Basic bus, the PMIC executes Power on sequence
   config 0 to Power on sequence config 2 registers, floats PWR_GOOD output signal after tPMIC_PWR_-
   GOOD_OUT timing parameter is satisfied and re-locks register Table 138, “Register 0x32” [7]. The PMIC
   does not require power cycle to re-enable PMIC’s output regulators.
```

The PMIC, on its own, can generate internal VR Disable command at any time due to one or more events listed in Table 28 under column “Trigger VR Disable”. The PMIC executes power off sequence config0 (Table 167, “Register 0x58”) to power off sequence config2 (Table 169, “Register 0x5A”) to preserve the appropriate voltage relationship as configured in the registers. The PMIC assert PWR_GOOD signal low. The PMIC requires power cycle. The VR Enable command with either Table 138, “Register 0x32” [7] = ‘1’ or VR_EN pin transitions to high has no effect on PMIC and PMIC keeps it PWR_GOOD signal low.

## 6.5.4 Secure Mode Operation; R1A[4] = ‘1’

The PMIC allows host to power down any or all output regulators by any of the two methods below.

```text
1. The VR Disable command with VR_EN pin transitions to low. The PMIC asserts PWR_GOOD signal Low.
   The PMIC executes power off sequence config0 (Table 167, “Register 0x58”) to power off sequence config2
   (Table 169, “Register 0x5A”) to preserve the appropriate voltage relationship as configured in the registers

   and enters in P1 state. The host can re-enable the PMIC’s output regulators by VR_EN pin transition to High.
   The PMIC exits from P1 state and executes power on sequence config 0 to config 2 registers and floats

   PWR_GOOD signal after tPMIC_PWR_GOOD_OUT timing parameter is satisfied. See Figure 32. The
   PMIC does not require power cycle.

         a.   Note that VR Disable or Enable command on a I2C/I3C Basic Bus (i.e., Table 138, “Register 0x32”
              [7] = ‘0’ or ‘1’) has no effect on the PMIC. Also, configuring one or more bits in
              Table 135, “Register 0x2F” [6,4:3] to ‘0’ has no effect on the PMIC. See Figure 31.
2. If Table 138, “Register 0x32” [5] = ‘1’, driving PWR_GOOD input low. The PMIC executes power off
   sequence config0 (Table 167, “Register 0x58”) to power off sequence config2 (Table 169, “Register 0x5A”)
   to preserve the appropriate voltage relationship as configured in the registers; drives PWR_GOOD signal
   low and unlocks only Table 138, “Register 0x32” [7]. The PMIC preserves all register contents including the
   MTP error log registers and keeps all write protect registers locked except for the Table 138, “Register 0x32”
   [7]. The PMIC does not enter in P1 state. When host issues VR Enable command by I2C/I3C Basic bus, the
   PMIC executes Power on sequence config 0 to Power on sequence config 2 registers, floats PWR_GOOD
   output signal after tPMIC_PWR_GOOD_OUT timing parameter is satisfied and re-locks register Table 138,
   “Register 0x32” [7]. The PMIC does not require power cycle to re-enable PMIC’s output regulators.
```

The PMIC, on its own, can generate internal VR Disable command at any time due to one or more events listed in Table 28 under column “Trigger VR Disable”. The PMIC executes power off sequence config0 (Table 167, “Register 0x58”) to power off sequence config2 (Table 169, “Register 0x5A”) to preserve the appropriate voltage relationship as configured in the registers. The PMIC does not enter in P1 state. The PMIC assert PWR_GOOD signal low. The PMIC requires power cycle. The VR Enable command with either Table 138, “Register 0x32” [7] = ‘1’ or VR_EN pin transitions to high has no effect on PMIC and PMIC keeps it PWR_GOOD signal low.

```text
                                                          R1A[4] = ‘0’
              High
  VIN_Bulk

              High
 VOUT_1.8V

              High
 VOUT_1.0V

              VR Dis or EN command on the Bus has no effect
  I2C/I3C

   VR_EN

    SWC

    SWB

    SWA

               High
PWR_GOOD
```

*Figure 30 — Power Down with VR_EN Pin; R1A[4]=0; Secure Mode; PWR_GOOD Signal* (figure; any text below/above was extracted from the drawing)

```text
              High                             R1A[4] = ‘0’ or ‘1’
  VIN_Bulk

              High
 VOUT_1.8V

              High
  VOUT_1.0V

                                        VR Dis or EN command on the Bus has no effect
   I2C/I3C                     VR_DIS
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

*Figure 31 — VR_DIS or VR_EN CMD on Bus; R1A[4]=x; Secure Mode; PWR_GOOD Signal* (figure; any text below/above was extracted from the drawing)

```text
                                                                 R1A[4] = ‘1’
             High
  VIN_Bulk

             High
 VOUT_1.8V

             High
 VOUT_1.0V

              VR Dis or EN command on the Bus has no effect
  I2C/I3C

   VR_EN

    SWC

    SWB

    SWA

              High
PWR_GOOD
```

*Figure 32 — Power Down with VR_EN Pin; R1A[4]=1; Secure Mode; PWR_GOOD Signal* (figure; any text below/above was extracted from the drawing)
