---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 4.18
title: Error Injection
pages: 70-71
---
# 4.18 Error Injection

The PMIC5200 offers error injection function for the purpose of debug, test, and validation at various stages.

## 4.18.1 Error Injection - Prior to VR Enable (either via VR_EN Pin or I2C/I3C Bus)

Prior to VR Enable command, the Error injection function may be invoked by setting error injection enable bit Table 157, Register 0x35 [7] = ‘1’ during the configuration state. If any of either VIN_Bulk UV/OV or SWx OV/UV or Critical Temp Shutdown error is injected prior to VR Enable command, the PMIC shall not execute power on sequence and shall not enable PMIC output regulators when PMIC receives VR Enable command. The PMIC shall not update error log registers (Table 108, Register 0x04 to Table 110, Register 0x06). The PMIC shall update appropriate status registers (Table 112, Register 0x08 to Table 115, Register 0x0B, Table 155, Register 0x33) accordingly. The PMIC shall enter in secure mode if Table 151, Register 0x2F [2] = ‘0’ and programmable mode if Table 151, Register 0x2F [2] = ‘1’.

## 4.18.2 Error Injection - After VR Enable (either via VR_EN pin or I2C/I3C Bus)

After PMIC output regulators are enabled with VR Enable command and if PMIC is in programmable mode, the error injection function may be invoked by setting error injection enable bit Table 157, Register 0x35 [7] = ‘1’. If any of either VIN_Bulk UV/OV or SWx OV/UV or Critical Temp Shutdown error is injected the PMIC shall execute Power Off Sequence to disable PMIC output regulators and shall update the error log registers (Table 108, Register 0x04 to Table 110, Register 0x06) as well as status registers (Table 112, Register 0x08 to Table 115, Register 0x0B, Table 155, Register 0x33) accordingly. Note that if any of the output rails are not enabled through power on sequence configuration registers, the error injection on those output rails do not apply. After PMIC output regulators are enabled with VR Enable command and if PMIC is in secure mode, the error injection enabling Table 157, Register 0x35 [7] = ‘1’ is disallowed. The PMIC shall ignore any attempts to inject any error and shall not execute Power Off Sequence to disable PMIC output regulators and shall not update any error log or status registers. To exit the error injection function, the host shall power cycle VIN_Bulk input supply.
