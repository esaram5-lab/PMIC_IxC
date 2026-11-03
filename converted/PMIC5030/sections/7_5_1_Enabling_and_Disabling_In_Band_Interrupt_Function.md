---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 7.5.1
title: Enabling and Disabling In Band Interrupt Function
pages: 85-86
---
# 7.5.1 Enabling and Disabling In Band Interrupt Function

By default, IBI function is disabled. The PMIC device enables the IBI when it registers ENEC CCC. Once enabled, the PMIC device sends an IBI when an event occurs.

```text
▪ When Table 158, Register 0x34 [6] = ‘1’, the device sends the IBI at next available opportunity when
  any of the register bits in Table 113, Register 0x08 [7:0], Table 114, Register 0x09 [7:0], Table 115,
  Register 0x0A [7:2], Table 116, Register 0x0B [7:0], Table 157, Register 0x33 [4:2], Table 175,
  Register 0x108 [7:0] and Table 176, Register 0x109 [7:0] is set to ‘1’. The device also sets
  Table 115, Register 0x0A [1] to ‘1’ and updates Pending Interrupt Bits [3:0] = ‘0001’ for GETSTATUS
  CCC.
  ▪ When Table 158, Register 0x34 [6] = ‘0’, the device does not send the IBI regardless of the register
    bits in Table 113, Register 0x08 [7:0], Table 114, Register 0x09 [7:0], Table 115, Register 0x0A [7:2],
    Table 116, Register 0x0B [7:0], Table 157, Register 0x33 [4:2], Table 175, Register 0x108 [7:0] and
    Table 176, Register 0x109 [7:0]. However, the device set Table 115, Register 0x0A [1] to ‘1’ and
    updates Pending Interrupt Bits [3:0] = ‘0001’ for GETSTATUS CCC.
```
