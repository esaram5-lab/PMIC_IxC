---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 2.1
title: Description
pages: 1-3
---
# 2.1 Description

The PMIC5000 and PMIC5010 are designed for typical DDR5 RDIMM, DDR5 LRDIMM as well as various types of DDR5 NVDIMM application. The PMIC features four step down switching regulators and three LDO regulators.

The PMIC is designed to support approximately 15 Watts of power. The PMIC is powered from VIN_Bulk input for switching regulators and VIN_Mgmt input for the rest of the PMIC. The PMIC supports selectable interface (I2C or I3C Basic) to fit various application environment. The PMIC device is intended to operate up to 12.5 MHz on a 1.0 V I3C Basic bus or up to 1 MHz on a 1.0 V to 3.3 V I2C bus.

## 2.1.1 Common Features Summary

**Table 1 — PMIC Device Type Summary**

```text
             Device Type                       SWA           SWB          SWC          SWD        Unit
PMIC5000 - Current Capability per Phase         5             5            5            5          A
PMIC5010 - Current Capability per Phase         3             3            3            3          A
```

• VIN_Bulk input supply range: 4.25 V to 15.0 V

• VIN_Mgmt input supply range: 3.0 V to 3.6 V

• Four step down switching regulators: SWA, SWB, SWC and SWD

• Programmable dual phase and single phase regulator for SWA and SWB

• 3 LDO regulators: VBias, VOUT_1.8V, VOUT_1.0V

• Automatic switchover from VIN_Mgmt input supply to VIN_Bulk input supply

• Error injection capability

• Persistent Error log registers

• Write protect mode and programmable of operation

• Independently programmable output voltages, power up and power down sequence for switch regulators

• Input and output power good status reporting mechanism

• VIN_Bulk input supply protection feature: Input over voltage

• Output switch regulators protection feature: Output over voltage, output under voltage, output current

```text
limiter
```

• Output current and power measurement, output current threshold mechanism

• Temperature measurement, temperature warning threshold, critical temperature shutdown

• Multi Time Programmable Non-Volatile Memory

• Programmable and DIMM specific registers for customization

• General Status Interrupt Function

• Flexible Open Drain IO (I2C) and Push Pull (I3C Basic) IO Support
