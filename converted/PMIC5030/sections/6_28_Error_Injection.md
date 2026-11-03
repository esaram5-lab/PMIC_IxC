---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 6.28
title: Error Injection
pages: 58-59
---
# 6.28 Error Injection

The PMIC offers error injection function for the purpose of debug, test and validation at various stages. Error Injection Function Usage prior to VR Enable:

```text
▪ Prior to VR Enable command, the Error injection function may be invoked by setting error injection
  enable bit Table 159, Register 0x35 [7] = ‘1’ during the configuration state. If any of either VIN_Bulk
  UV/OV or SWx OV/UV or Critical Temp Shutdown or MTP (DIMM vendor or PMIC vendor) error is

  injected prior to VR Enable command, the PMIC shall not execute power on sequence and shall not
  enable PMIC output regulators when PMIC receives VR Enable command. The PMIC shall not

  update error log registers (Table 108, Register 0x03 to Table 112, Register 0x07). The PMIC shall
  update appropriate status registers accordingly when error is injected.
```

Error Injection Function Usage after VR Enable:

```text
▪ After PMIC output regulators are enabled with VR Enable command and PMIC is in non write-
  protect mode, the error injection function may be invoked by setting error injection enable bit
  Table 159, Register 0x35 [7] = ‘1’. If any of either VIN_Bulk UV/OV or SWx OV/UV or Critical Temp
  Shutdown error is injected the PMIC shall execute Power Off Sequence to disable PMIC output
  regulators and shall update the error log registers (Table 109, Register 0x04 [7:4] Table 110,
  Register 0x05 to Table 112, Register 0x07) as well as status registers accordingly. Note that if any of
  the output rails are not enabled through power on sequence configuration registers, the error
  injection on that output rail does not apply. The PMIC shall not update Table 108, Register 0x03
  [7:0], Table 109, Register 0x04 [3:0] and Table 201, Register 0x140 [7:0] to Table 230, Register
  0x15D [7:0]. The MTP (DIMM vendor or PMIC vendor error injection feature) is not allowed after VR
  Enable command.
▪ After PMIC output regulators are enabled with VR Enable command and PMIC is in write-protect
  mode, the error injection enabling Table 159, Register 0x35 [7] = ‘1’ is disallowed. The PMIC shall
  ignore any attempts to inject any error and shall not execute Power Off Sequence to disable PMIC
  output regulators and shall not update any error log or status registers.
```

To exit the error injection function, the host shall power cycle VIN_Bulk and VIN_Mgmt input supply.
