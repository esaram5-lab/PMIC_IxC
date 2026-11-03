---
document: JESD301-2 (PMIC5100 Power Management IC Standard, Rev. 1.03, October 2022)
device: PMIC5100
application: client
section: 6.13
title: Error Injection
pages: 61-61
---
# 6.13 Error Injection

The DDR5 PMIC offers error injection function for the purpose of debug, test and validation at various stages. Error Injection Function Usage prior to VR Enable (either via VR_EN pin or I2C/I3C Bus):

```text
• Prior to VR Enable command, the Error injection function may be invoked by setting error injection enable bit
  Table 141, “Register 0x35” [7] = ‘1’ during the configuration state. If any of either VIN_Bulk UV/OV or SWx
  OV/UV or Critical Temp Shutdown error is injected prior to VR Enable command, the PMIC shall not execute
  power on sequence and shall not enable PMIC output regulators when PMIC receives VR Enable command.

  The PMIC shall not update error log registers (Table 92, “Register 0x04” to Table 94, “Register 0x06”). The
  PMIC shall update appropriate status registers accordingly. The PMIC shall enter in secure mode if Table 135,

  “Register 0x2F” [2] = ‘0’ and programmable mode if Table 135, “Register 0x2F” [2] = ‘1’.
```

Error Injection Function Usage after VR Enable (either via VR_EN pin or I2C/I3C Bus):

After PMIC output regulators are enabled with VR Enable command and PMIC is in programmable mode, the error injection function may be invoked by setting error injection enable bit Table 141, “Register 0x35” [7] = ‘1’. If any of either VIN_Bulk UV/OV or SWx OV/UV or Critical Temp Shutdown error is injected the PMIC shall execute Power Off Sequence to disable PMIC output regulators and shall update the error log registers (Table 92, “Register 0x04” to Table 94, “Register 0x06”) as well as status registers accordingly. Note that if any of the output rails are not enabled through power on sequence configuration registers, the error injection on that output rails does not apply.

```text
• After PMIC output regulators are enabled with VR Enable command and PMIC is in secure mode, the error
  injection enabling Table 141, “Register 0x35” [7] = ‘1’ is disallowed. The PMIC shall ignore any attempts to
  inject any error and shall not execute Power Off Sequence to disable PMIC output regulators and shall not
  update any error log or status registers.
```

To exit the error injection function, the host shall power cycle VIN_Bulk input supply.
