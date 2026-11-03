---
document: JESD301-6 (PMIC5120 Power Management IC Standard, Version 1.0, February 2025)
device: PMIC5120
application: client
section: 6.13
title: Error Injection
pages: 65-65
---
# 6.13 Error Injection

The DDR5 PMIC offers error injection function for the purpose of debug, test and validation at various stages.

6.13.1 Error Injection Function Usage prior to VR Enable (either via VR_EN Pin or I2C/

```text
I3C Bus)
```

Prior to VR Enable command, the Error injection function may be invoked by setting error injection enable bit Table 149, Register 0x35 [7] = ‘1’ during the configuration state. If any of either VIN_Bulk UV/OV or SWx OV/UV or Critical Temp Shutdown error is injected prior to VR Enable command, the PMIC shall not execute power on sequence and shall not enable PMIC output regulators when PMIC receives VR Enable command. The PMIC shall not update error log registers (Table 100, Register 0x04 to Table 102, Register 0x06). The PMIC shall update appropriate status registers (Table 104, Register 0x08 to Table 107, Register 0x0B, Table 147, Register 0x33) accordingly. The PMIC shall enter in secure mode if Table 143, Register 0x2F [2] = ‘0’ and programmable mode if Table 143, Register 0x2F [2] = ‘1’.

6.13.2 Error Injection Function Usage after VR Enable (either via VR_EN Pin or I2C/I3C

```text
Bus)
```

After PMIC output regulators are enabled with VR Enable command and PMIC is in programmable mode, the error injection function may be invoked by setting error injection enable bit Table 149, Register 0x35 [7] = ‘1’. If any of either VIN_Bulk UV/OV or SWx OV/UV or Critical Temp Shutdown error is injected the PMIC shall execute Power Off Sequence to disable PMIC output regulators and shall update the error log registers (Table 100, Register 0x04 to Table 102, Register 0x06) as well as status registers (Table 104, Register 0x08 to Table 107, Register 0x0B, Table 147, Register 0x33) accordingly. Note that if any of the output rails are not enabled through power on sequence configuration registers, the error injection on that output rail does not apply.

After PMIC output regulators are enabled with VR Enable command and PMIC is in secure mode, the error injection enabling Table 149, Register 0x35 [7] = ‘1’ is disallowed. The PMIC shall ignore any attempts to inject any error and shall not execute Power Off Sequence to disable PMIC output regulators and shall not update any error log or status registers.

To exit the error injection function, the host shall power cycle VIN_Bulk input supply.
