---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 4.5
title: Secure Mode and Programmable Mode of Operation
pages: 31-32
---
# 4.5 Secure Mode and Programmable Mode of Operation

Prior to issuing VR Enable command (either with VR_EN pin or on I2C/I3C Basic bus), the host must configure the register Table 151, Register 0x2F [2] appropriately as desired. The PMIC offers two modes of operation after VR Enable command (either with VR_EN pin or on I2C/I3C Basic bus) is registered.

```text
1.      Programmable Mode - In this mode, independent of when host issues VR Enable command (either
        with VR_EN pin or on I2C/I3C Basic bus), the PMIC allows modification to any register in the host
        region as desired by the host and PMIC responds appropriately.
2.      Secure Mode - In this mode, after host issues VR Enable command (either with VR_EN pin or on
        I2C/I3C Basic bus), the PMIC does not allow modification to registers Table 125, Register 0x15 to
        Table 151, Register 0x2F, Table 154, Register 0x32 [7,5:0] in the host region as well as Table 182,
        Register 0x40 to Register 0x6F in the CAMM2 vendor region. These registers are write-protected
        and marked with RED color cells in “Register” column in Table 107, Host Region - Register Map and
        in Table 181, CAMM2 Vendor Region - Register Map. The PMIC simply ignores the host request.
        Throughout this entire specification, when it refers to PMIC allowing access to the registers, it refers
        to write operation to the registers that are not write protected in secure mode or programmable
        mode. There is no restriction for the read operation in secure mode or programmable mode. The
        host must power cycle the PMIC to make any modification. The PMIC power cycle is defined as
        complete removal of VIN_Bulk input supply to the PMIC and this definition is applied to the entire
        specification. The PMIC does allows to modification to any other remaining registers that are not
        marked in RED color cells in “Register” column in Table 107, Host Region - Register Map with I2C or
        I3C Basic bus. The Secure Mode is only applicable once VR Enable command (either with VR_EN
        pin or on I2C/I3C Basic bus) is registered. This is important because by default Table 151, Register
        0x2F [2] = ‘0’ when PMIC is first powered up. Prior to VR Enable command (either with VR_EN pin
        or on I2C/I3C Basic bus), PMIC allows modification to any registers in the host region.
```

Note that there is one exception in Secure mode of operation. The exception is for register Table 154, Register 0x32 [7]. This register can get updated with VR_EN pin assertion/de-assertion or PWR_GOOD signal input assertion to low or when PMIC internally generates its own VR Disable command due to some fault condition. This register cannot be updated with I2C or I3C Basic bus command or with DEVCTRL

CCC command.
