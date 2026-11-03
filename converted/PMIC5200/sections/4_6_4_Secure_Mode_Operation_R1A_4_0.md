---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 4.6.4
title: Secure Mode Operation; R1A[4] = ‘0’
pages: 39-40
---
# 4.6.4 Secure Mode Operation; R1A[4] = ‘0’

The PMIC allows host to power down any or all output regulators by any of the two methods below.

```text
1.       The VR Disable command with VR_EN pin transitions to low. The PMIC asserts PWR_GOOD signal
         Low. The PMIC executes power off sequence config0 (Table 200, Register 0x58) to power off
         sequence config3 (Table 203, Register 0x5B) to preserve the appropriate voltage relationship as
         configured in the registers. The host can re-enable the PMIC’s output regulators by VR_EN pin tran-
         sition to High. The PMIC executes power on sequence config 0 to power on sequence config 3 reg-
         isters and floats PWR_GOOD signal after tPMIC_PWR_GOOD_OUT timing parameter is satisfied.
         See Figure 25. The PMIC does not require power cycle.
                a. Note that VR Disable or Enable command on a I2C/I3C Basic Bus (i.e., Table 154, Regis-
                    ter 0x32 [7] = ‘0’ or ‘1’) has no effect on the PMIC. Also, configuring one or more bits in
                    Table 151, Register 0x2F [6:3] to ‘0’ has no effect on the PMIC. See Figure 26.

2.      If Table 154, Register 0x32 [5] = ‘1’, driving PWR_GOOD input low. The PMIC executes power off
        sequence config0 (Table 200, Register 0x58) to power off sequence config3 (Table 203, Register
        0x5B) to preserve the appropriate voltage relationship as configured in the registers; drives
        PWR_GOOD signal low and unlocks only Table 154, Register 0x32 [7]. The PMIC preserves all
        register contents including the MTP error log registers and keeps all write-protected registers locked
        except for the Table 154, Register 0x32 [7]. When host issues VR Enable command by I2C/I3C
        Basic bus, the PMIC executes Power on sequence config 0 to Power on sequence config 2
        registers, floats PWR_GOOD output signal after tPMIC_PWR_GOOD_OUT timing parameter is
        satisfied and re-locks register Table 154, Register 0x32 [7]. The PMIC does not require power cycle
        to re-enable PMIC’s output regulators.
```

The PMIC, on its own, can generate internal VR Disable command at any time due to one or more events listed in Table 27 under column “Trigger VR Disable”. The PMIC executes power off sequence config0 (Table 200, Register 0x58) to power off sequence config3 (Table 203, Register 0x5B) to preserve the appropriate voltage relationship as configured in the registers. The PMIC assert PWR_GOOD signal low. The PMIC requires power cycle. The VR Enable command with either Table 154, Register 0x32 [7] = ‘1’ or VR_EN pin transitions to high has no effect on PMIC and PMIC keeps it PWR_GOOD signal low.
