---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 6.11
title: Reset_n Pin Function
pages: 41-41
---
# 6.11 Reset_n Pin Function

PMIC5030 has Reset_n input pin. By default, the Reset_n input pin receiver is disabled at power on. The controller can enable the Reset_n input pin (CMOS input pin receiver) via Table 192, Register 0x12E [7:6].

If Reset_n input pin is enabled, the PMIC resets only the bus interface (I2C or I3C) as if it was a power on reset. The PMIC keeps all output regulators running if they are enabled and there should be no change in

PMIC CAMP signal behavior. When Reset_n input pin is asserted, the PMIC always returns to I2C mode (Table 155, Register 0x32 [6] = ‘0’, Table 153, Register 0x30 [2] = ‘0’), clears the Table 115, Register 0x0A [3:2] = ‘00’, Table 158, Register 0x34 [7:5] = ‘000’ and Table 158, Register 0x34 [3:1] = ‘111’ and floats the SDA signal and clears appropriate state machine if it was previously stuck. The PMIC interface stays in reset as long as Reset_n input pin is asserted. The controller is expected to de-assert the Reset_n input pin followed by SETHID and SETAASA CCC to ensure all components on the module are aligned to same mode of operation. The controller also updates the Table 153, Register 0x30 [2] = ‘1’ for 2 byte address mode. The PMIC ignores any I2C or I3C bus command while Reset_n input is asserted (i.e., PMIC may NACK or may ACK. If PMIC ACKs it, it must return 0x00 data for read and ignore write data).
