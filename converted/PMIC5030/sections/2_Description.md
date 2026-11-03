---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 2
title: Description
pages: 1-3
---
# 2 Description

The PMIC5030 is designed for typical DDR5 RDIMM and DDR5 MRDIMM as well as various types of CXL module application. The PMIC features six step down switching regulators and two LDO regulators (1.8V

LDO and 1.0V LDO) for external usage and either one or two LDO regulators (VBIAS1 and VBIAS2) for

PMIC’s own internal consumption. The PMIC is designed to support approximately 25 to 30 Watts of power. The PMIC is powered from VIN_Bulk input for switching regulators and VIN_Mgmt input for the rest of the PMIC. The PMIC supports selectable interface (I2C or I3C Basic) to fit various application environment. The PMIC device is intended to operate up to 12.5 MHz on a 1.0 V I3C Basic bus or up to 1 MHz on a 1.0 V to 3.3 V I2C bus.

## 2.1 Common Features Summary

**Table 1 — PMIC Device Type Summary**

```text
       Device Type             SWA          SWB         SWC          SWD         SWE          SWF         Unit

Current Capability per Phase    7.5          7.5         7.5          5           7.5          7.5          A

    ▪ VIN_Bulk input supply range: 4.25 V to 15.0 V
    ▪ VIN_Mgmt input supply range: 3.0 V to 3.6 V
    ▪ Six step down switching regulators: SWA, SWB, SWC, SWD, SWE, and SWF
    ▪ Programmable one three phase, two dual phase and six single phase regulator
    ▪ Three or Four LDO regulators: One or Two VBias (VBIAS1, VBIAS2), VOUT_1.8V, VOUT_1.0V
```

▪ Automatic switchover from VIN_Mgmt input supply to VIN_Bulk input supply

▪ Error injection capability

▪ Persistent Error log registers with detail information

▪ Write-protect mode and programmable of operation

▪ Independently programmable output voltages, power up and power down sequence for switch

```text
regulators
```

▪ Input and output power good status reporting mechanism

▪ VIN_Bulk input supply protection feature: Input over voltage

▪ Output switch regulators protection feature: Output over voltage, output under voltage, output

```text
current limiter
```

▪ Output current and power measurement, output current threshold mechanism

▪ Temperature measurement, temperature warning threshold, critical temperature shutdown

▪ Multi Time Programmable Non-Volatile Memory

▪ MTP Error Check capability

▪ Unique serial Number for traceability

▪ Programmable and DIMM specific registers for customization

▪ General Status Interrupt Function

▪ Reset input pin to reset various aspects of PMIC

▪ Auto Power On to turn on the regulators

▪ VR Output Enable Pin to turn on the regulators

▪ Flexible Open Drain IO (I2C) and Push Pull (I3C Basic) IO Support
