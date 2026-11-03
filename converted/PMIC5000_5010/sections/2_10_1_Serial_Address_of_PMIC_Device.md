---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 2.10.1
title: Serial Address of PMIC Device
pages: 47-47
---
# 2.10.1 Serial Address of PMIC Device

The PMIC device 4-bit binary value (LID) is:

```text
• If PID pin is connected to GND on PCB: ‘1001’
• If PID pin is tied to 1.8 V on PCB: ‘1100’
• If PID pin is floating on PCB: ‘1000’
```

The PMIC device samples the status of the PID pin on power up. The sampled status of the PID pin is used to select one of the three possible unique LID code for the device. The selected LID code either ‘1001’ or ‘1100’ or ‘1000’ is merged with a 3 bit HID code Table 142, “Register 0x34” [3:1] to establish the 7-bit address code the device. For example, with the default setting in Table 142, “Register 0x34” [3:1] = ‘111’; if the PID pin is connected to GND, the device address shall be ‘1001 111’.

**Table 31 — 7-bit Address of PMIC Device**

```text
Bit 7        Bit 6     Bit 5        Bit 4      Bit 3       Bit 2       Bit 1      Bit 0
  1           x          0           x           1           1          1         R/W
                                                                                  Read/
        PMIC Device Type ID (LID)                      Host ID (HID)
                                                                                  Write
```
