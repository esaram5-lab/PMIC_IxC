---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 7.1
title: Device Interface - Protocol
pages: 62-63
---
# 7.1 Device Interface - Protocol

The 7-bit serial address of the PMIC device applies to both I2C and I3C Basic mode of operation identically.

## 7.1.1 PMIC Management Bus

The PMIC supports two different protocols on its management bus.

```text
▪ I2C Target Protocol - Speed Up to 1 MHz
▪ I3C Basic Target Protocol - Speed Up to 12.5 MHz
```

The PMIC’s 7-bit target address [7:1] is composed of 4-bit LID address [7:4] and 3-bit HID address [3:1].

**Table 35 — 7-bit Address of PMIC Device**

```text
        Bit 7      Bit 6        Bit 5        Bit 4       Bit 3        Bit 2       Bit 1        Bit 0

         1           x            0             x          1           1            1          R/W

                PMIC Device Type ID (LID)                         Host ID (HID)             Read/Write

The PMIC’s 4-bit [7:4] LID address is:
    ▪ If PID pin is connected to GND on PCB: ‘1001’
    ▪ If PID pin is tied to 1.8 V on PCB: ‘1100’
    ▪ If PID pin is floating on PCB: ‘1000’
```

The PMIC’s 3-bit [3:1] HID address is per Table 158, Register 0x34 [3:1].

The PMIC device samples the status of the PID pin on power up. The sampled status of the PID pin is used to select one of the three possible unique LID code for the device. The selected LID code either ‘1001’ or ‘1100’ or ‘1000’ is merged with a 3 bit HID code from Table 158, Register 0x34 [3:1] to establish the 7-bit address code the device. For example, with the default setting in Table 158, Register 0x34 [3:1] = ‘111’; if the PID pin is connected to GND, the device address shall be ‘1001 111’.

## 7.1.2 Switch from I2C Mode to I3C Basic Mode

By default when PMIC first powers on, it operates in legacy I2C mode. The PMIC device shall operate in I2C mode until put into I3C Basic mode via command. In I2C mode, the host is allowed to issue only 3 CCCs (DEVCTRL, SETHID, SETAASA). All other CCCs are not supported and the PMIC device may simply ignore it. The Host must issue DEVCTRL and SETHID CCC first (if required) followed by SETAASA CCC.

The Host puts the PMIC device in I3C Basic mode by issuing SETAASA CCC.

When SETAASA CCC is registered by the PMIC device, it updates the Table 155, Register 0x32 [6] to ‘1’. When SETHID CCC is registered by the PMIC device, it updates the Table 158, Register 0x34 [3:1].

## 7.1.3 Switch from I3C Basic Mode to I2C Mode

The Host can put the PMIC device back in I2C mode from I3C Basic mode at any time by issuing RSTDAA CCC. When RSTDAA CCC is registered by the PMIC device, it updates the Table 155, Register 0x32 [6] to ‘0’.
