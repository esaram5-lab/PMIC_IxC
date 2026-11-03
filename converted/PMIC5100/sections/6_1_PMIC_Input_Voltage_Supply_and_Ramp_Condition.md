---
document: JESD301-2 (PMIC5100 Power Management IC Standard, Rev. 1.03, October 2022)
device: PMIC5100
application: client
section: 6.1
title: PMIC Input Voltage Supply and Ramp Condition
pages: 28-28
---
# 6.1 PMIC Input Voltage Supply and Ramp Condition

The DDR5 PMIC has one input supply from the platform: VIN_Bulk. The VIN_Bulk supply is used by the PMIC for all three switch (SWA, SWB, SWC) output regulators and two LDO outputs (VOUT_1.8V and VOUT_1.0V) regulators. Note that the VOUT_1.8V LDO output is separate and independent from SWC output, which is for the DRAM VPP rail. The VOUT_1.0V LDO output is separate and independent from SWA or SWB. At first power on, the VIN_Bulk input supply shall reach a minimum threshold voltage of 4.25 V before it can be detected as a valid input supply to the PMIC. Once the VIN_Bulk supply is valid and stable, the PMIC shall assert PWR_GOOD output low, drive VOUT_1.8V and VOUT_1.0V supply within t1.8V_Ready and t1.0V_Ready time respectively. The PMIC drives PWR_GOOD output signal low only when VIN_Bulk input supply reaches minimum of 4.25 V. The PWR_GOOD output is pulled up to either 1.8 V or 3.3 V on the platform or on the host controller. The PWR_GOOD pullup voltage (either 1.8 V or 3.3 V) can be available before or after VIN_Bulk is valid and stable. If PWR_GOOD pullup voltage is available before VIN_Bulk is applied, the PWR_GOOD signal is High and remains High with no leakage path or damage to the PMIC. When VIN_Bulk is applied to the PMIC, the PMIC asserts PWR_GOOD output low.

The PMIC shall enable I2C/I3C bus interface function within tManagement_Ready. The host shall not attempt to access the PMIC’s memory registers until tManagement_Ready timing requirement is satisfied.
