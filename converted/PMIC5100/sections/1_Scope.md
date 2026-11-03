---
document: JESD301-2 (PMIC5100 Power Management IC Standard, Rev. 1.03, October 2022)
device: PMIC5100
application: client
section: 1
title: Scope
pages: 1-3
---
# 1 Scope

This standard defines the specification of interface parameters, signaling protocols, and features for PMIC devices used for memory module applications. The designation PMIC5100 refers to the device specified by this document. The purpose is to provide a standard for the PMIC5100 device for uniformity, multiplicity of sources, elimination of confusion, ease of device specification, and ease of use. Unless otherwise noted in the document, any illegal operation is not allowed and device operation is not guaranteed.

```text
NOTE: The designation PMIC5100 refers to a portion of the part number designation of a series of commercial
```

logic devices common in the industry. This number is normally preceded by a series of manufacturer specific characters to make up a complete part designation.

## 1.1 Device Standard



### 1.1.1 Description

The PMIC5100 is designed for typical DDR5 SODIMM as well as DDR5 UDIMM. The PMIC features three step down switching regulators and two LDO regulators.

The PMIC is designed to support approximately TBD Watts of power. The PMIC is powered from VIN_Bulk input for the entire PMIC including the switching regulators and LDO output regulators. The PMIC supports selectable interface (I2C or I3C Basic) to fit various application environment. The PMIC device is intended to operate up to 12.5 MHz on a 1.0 V I3C Basic bus or up to 1 MHz on 1.0 V to 3.3 V I2C bus.

### 1.1.2 Common Feature Summary

• VIN_Bulk input supply range: 4.25 V to 5.5 V

• Three step down switching regulators: SWA, SWB, and SWC

• Programmable dual phase and single phase regulator for SWA and SWB

• 2 LDO regulators: VOUT_1.8V, VOUT_1.0V

• Error injection capability

• Persistent error log registers

• Secure mode and programmable mode of operation

• Independently programmable output voltages, power up and power down sequence for switch regulators

• Output power good status reporting mechanism

• VIN_Bulk input supply protection feature: Input over voltage

• Output switch regulators protection features: Output over voltage, output under voltage, output current

```text
limiter
```

• Output current and power measurement, output current threshold mechanism

• Temperature measurement, temperature warning threshold, critical temperature shutdown

• Multi Time Programmable (MTP) Non-Volatile Memory

• Programmable and DIMM specific registers for customization

• General Status Interrupt (GSI) function

• Flexible Open Drain IO (I2C) and Push Pull (I3C Basic) IO support

• Flexible mechanism to enable switch regulators (with VR_EN pin or VR Enable command on I2C or I3C Basic

```text
  interface)
• Idle Power State (P1 State)
```
