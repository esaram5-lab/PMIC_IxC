---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 5.1
title: Device Interface - Protocol
pages: 72-73
---
# 5.1 Device Interface - Protocol



## 5.1.1 Management Bus

The PMIC supports two different protocol on its management bus.

```text
• I2C Target Protocol - Speed Up to 1 MHz
• I3C Basic Target Protocol - Speed Up to 12.5 MHz
```

The PMIC’s 7-bit target address [7:1] is composed of 4-bit device address [7:4] and 3-bit HID address [3:1]. The PMIC’s 4-bit device address [7:4] is:

```text
• If PID pin is tied to GND on PCB: ‘1001’
• If PID pin is tied to 1.8 V on PCB: ‘1100’
• If PID pin floating on PCB: ‘1000’
```

The PMIC’s 3-bit HID address [3:1] is per Table 156, Register 0x34 [3:1].

## 5.1.2 Switch from I2C mode to I3C Basic Mode

By default, when PMIC first powers on, it operates in I2C mode. The PMIC shall operate in I2C mode until put into I3C Basic mode via command. In I2C mode, the host is allowed to issue only 3 CCCs (DEVCTRL, SETHID, and SETAASA). All other CCC are not supported and the PMIC device simply ignores it. The host must issue DEVCTRL or SETHID CCC first (if required) followed by SETAASA CCC.

The host puts the PMIC in I3C Basic mode by issuing SETAASA CCC. See also Section 5.4.10.4. When SETHID CCC is registered by the PMIC, it updates Table 156, Register 0x34 [3:1]. When SETAASA CCC is registered by the PMIC, it updates Table 154, Register 0x32 [6] to ‘1’.

## 5.1.3 Switch from I3C Basic Mode to I2C mode

The host can put the PMIC back in I2C mode from I3C Basic mode at any time by issuing RSTDAA CCC. When RSTDAA CCC is registered by the PMIC, it updates Table 154, Register 0x32 [6] to ‘0’. See also Clause 5.4.10.3.
