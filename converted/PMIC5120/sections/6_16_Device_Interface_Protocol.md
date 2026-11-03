---
document: JESD301-6 (PMIC5120 Power Management IC Standard, Version 1.0, February 2025)
device: PMIC5120
application: client
section: 6.16
title: Device Interface - Protocol
pages: 66-67
---
# 6.16 Device Interface - Protocol



## 6.16.1 Management Bus

The PMIC supports two different protocol on its management bus.

```text
• I2C Target Protocol - Speed Up to 1 MHz

• I3C Basic Target Protocol - Speed Up to 12.5 MHz
```

The PMIC’s 7-bit target address [7:1] is composed of 4-bit device address [7:4] and 3-bit HID address [3:1].

The PMIC’s 4-bit device address [7:4] is:

```text
• If PID pin is tied to GND on PCB: ‘1001’
• If PID pin is tied to 1.8 V on PCB: ‘1100’
• If PID pin floating on PCB: ‘1000’
```

The PMIC’s 3-bit HID address [3:1] is per Table 148, Register 0x34 [3:1].

## 6.16.2 Switch from I2C Mode to I3C Basic Mode

By default when PMIC first powers on, it operates in I2C mode. The PMIC device shall operate in I2C mode until put into I3C Basic mode via command.

In I2C mode, the host is allowed to issue only 3 CCCs (DEVCTRL, SETHID, SETAASA). All other CCC are not supported and the PMIC device simply ignores it. The host must issue DEVCTRL and SETHID CCC first (if required) followed by SETAASA CCC. The host puts the PMIC device in I3C Basic mode by issuing SETAASA CCC. See also Section 6.18.10.4. When SETHID CCC is registered by the PMIC, it updates the Table 148, Register 0x34 [3:1]. When SETAASA CCC is registered by the PMIC, it updates the Table 146, Register 0x32 [6] to ‘1’.

## 6.16.3 Switch from I3C Basic Mode to I2C Mode

The host can put the PMIC device back in I2C mode from I3C Basic mode at any time by issuing RSTDAA CCC.

When RSTDAA CCC is registered by the PMIC, it updates Table 146, Register 0x32 [6] to ‘0’. See also Section 6.18.10.3.
