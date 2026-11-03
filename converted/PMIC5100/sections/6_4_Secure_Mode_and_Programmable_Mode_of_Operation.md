---
document: JESD301-2 (PMIC5100 Power Management IC Standard, Rev. 1.03, October 2022)
device: PMIC5100
application: client
section: 6.4
title: Secure Mode and Programmable Mode of Operation
pages: 35-36
---
# 6.4 Secure Mode and Programmable Mode of Operation

Prior to issuing VR Enable command (either with VR_EN pin or on I2C/I3C Basic bus), the host must configure the register Table 135, “Register 0x2F” [2] appropriately as desired. The PMIC offers two modes of operation after VR Enable command (either with VR_EN pin or on I2C/I3C Basic bus) is registered.

```text
1. Programmable Mode - In this mode, independent of when host issues VR Enable command (either with
   VR_EN pin or on I2C/I3C Basic bus), the PMIC allows modification to any register in the host region as
   desired by the host and PMIC responds appropriately.
2. Secure Mode - In this mode, after host issues VR Enable command (either with VR_EN pin or on I2C/I3C
   Basic bus), the PMIC does not allow modification to registers Table 109, “Register 0x15” to Table 135,
   “Register 0x2F”, Table 138, “Register 0x32” [7,5:0] in the host region as well as Table 149, “Register 0x40”
   to Register 0x6F in the DIMM vendor region. These registers are write protected marked with RED color
   cells in “Register” column in Table 90, “Host Region - Register Map” and in Table 91, “DIMM Vendor
   Region - Register Map”. The PMIC simply ignores the host request. Throughout this entire standard, when it
   refers to as PMIC allows access to the registers, it refers to write operation to the registers that are not write
   protected in secure mode or programmable mode. There is no restriction for the read operation in secure
   mode or programmable mode. The host must power cycle the PMIC to make any modification. The PMIC
   power cycle is defined as complete removal of VIN_Bulk input supply to the PMIC and this definition is
   applied to the entire standard. The PMIC does allows to modification to any other remaining registers that
   are not marked in RED colored cells in “Register” column in Table 90, “Host Region - Register Map” with
   I2C or I3C Basic bus. The Secure Mode is only applicable once VR Enable command (either with VR_EN
   pin or on I2C/I3C Basic bus) is registered. This is important because by default Table 135, “Register 0x2F”
   [2] = ‘0’ when PMIC is first powered up. Prior to VR Enable command (either with VR_EN pin or on I2C/
   I3C Basic bus), PMIC allows modification to any registers in the host region.
```

Note that there is one exception in Secure mode of operation. The exception is for register Table 138, “Register 0x32” [7]. This register can get updated with VR_EN pin assertion/de-assertion or PWR_GOOD signal input assertion to low or when PMIC internally generates its own VR Disable command due to some fault condition. This register cannot be updated with I2C or I3C Basic bus command or with DEVCTRL CCC command.
