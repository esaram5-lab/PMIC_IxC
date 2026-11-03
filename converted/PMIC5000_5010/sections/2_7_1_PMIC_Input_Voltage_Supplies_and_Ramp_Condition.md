---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 2.7.1
title: PMIC Input Voltage Supplies and Ramp Condition
pages: 23-23
---
# 2.7.1 PMIC Input Voltage Supplies and Ramp Condition

The DDR5 PMIC has two input supplies from the platform: VIN_Bulk and VIN_Mgmt. The VIN_Bulk supply is used by the PMIC for all output regulators except for the VOUT_1.8V and VOUT_1.0V LDO outputs regulators when not in switchover mode. The VIN_Bulk input supply may also be used to generate the internal bias voltage. Note that the VOUT_1.8V LDO output is separate and independent from SWD output, which is for the DRAM VPP rail. The VOUT_1.0V LDO output is separate and independent from SWA, SWB, or SWC. The PMIC internally generates on its own bias voltage (VBias). At first power on, the VIN_Bulk input supply shall reach a minimum threshold voltage value per register Table 116, “Register 0x1A” [7:5] plus 1.0V offset before it can be detected as a valid input supply to the PMIC. The PMIC filters any non-monotonic noise after this threshold. After power on, with valid VIN_Mgmt input supply while PMIC is operating in non write protect mode of operation, if VIN_Bulk input supply is removed and re-applied, it must reach the same threshold voltage value per Table 116, “Register 0x1A” [7:5] plus 1.0 V offset. The VIN_Mgmt supply is used to read out its internal non-volatile memory content and to supply VOUT_1.8V and VOUT_1.0V to other devices such as SPD, TS and RCD on the DIMM. At first power on, the VIN_Mgmt supply shall reach a minimum of 2.8V before it can be detected as a valid input supply to the PMIC. At power on, the PMIC floats CAMP signal and then drives CAMP output signal low only when VIN_Mgmt input supply reaches minimum of 2.8 V and PMIC VOUT_1.8V and VOUT_1.0V LDO outputs are valid. VIN_Bulk input supply does not trigger PMIC to drive CAMP output signal low at power on. The VIN_Mgmt supply is strictly a voltage input. The CAMP output is pulled up to either 1.8 V or 3.3 V on the platform or on the host controller. The CAMP pullup voltage (either 1.8 V or 3.3 V) can be available before or after either VIN_Bulk or VIN_Mgmt is valid and stable. If CAMP pullup voltage is available before VIN_Mgmt or VIN_Bulk is applied, the CAMP signal is high and remains

High with no leakage path or damage to the PMIC. When VIN_Mgmt is applied to the PMIC and after VOUT_1.8V and VOUT_1.0V LDO outputs are valid, the PMIC asserts CAMP output low.

Figure 11 and Figure 12 show PMIC power up sequence when power is first applied. The platform can power up VIN_Bulk and VIN_Mgmt supply in any sequence. Figure 11 shows VIN_Mgmt supply ramps up first prior to

VIN_Bulk supply. Figure 12 shows VIN_Bulk supply ramps up first prior to VIN_Mgmt supply. The PMIC does not mandate any specific timing relationship between VIN_Bulk and VIN_Mgmt supply. The PMIC updates register Table 98, “Register 0x08” [7] when VIN_Bulk input supply status is valid.
