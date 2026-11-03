---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 4.1
title: PMIC Input Voltage Supply and Ramp Condition
pages: 25-25
---
# 4.1 PMIC Input Voltage Supply and Ramp Condition

The PMIC5200 has one input supply from the platform: VIN_Bulk. The VIN_Bulk supply is used by the PMIC for all four switch (SWA, SWB, SWC, SWD) output regulators and two LDO outputs (VOUT_1.8V and VOUT_1.0V) regulators. Note that the VOUT_1.8V LDO output is separate and independent from SWC output, which is for the DRAM VPP rail. The VOUT_1.0V LDO output is separate and independent from SWA or SWB. At first power on, the VIN_Bulk input supply shall reach a minimum threshold voltage of 3.0V before it can be detected as a valid input supply to the PMIC. Once the VIN_Bulk supply is valid and stable (i.e., above 3.0 V), the PMIC shall assert PWR_GOOD output low, drive VOUT_1.8V and VOUT_1.0V supply within t1.8V_Ready and t1.0V_Ready time respectively. The PMIC drives PWR_GOOD output signal low only when VIN_Bulk input supply reaches minimum of 3.0V. The PWR_GOOD output is pulled up to either 1.8 V or 3.3 V on the platform or on the host controller. The PWR_GOOD pullup voltage (either 1.8 V or 3.3 V) can be available before or after VIN_Bulk is valid and stable. If PWR_GOOD pullup voltage is available before VIN_Bulk is applied, the PWR_GOOD signal is High and remains High with no leakage path or damage to the PMIC. When VIN_Bulk is applied to the PMIC, the PMIC asserts PWR_GOOD output low. The platform should pay attention to timing relationship between PWR_GOOD pullup voltage and VIN_Bulk ramp to prevent undesired glitches on PWR_GOOD signal.

The PMIC shall enable I2C/I3C bus interface function within tManagement_Ready. The host shall not attempt to access the PMIC’s memory registers until tManagement_Ready timing requirement is satisfied.
