---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 4.2
title: Power Up Initialization Sequence
pages: 25-30
---
# 4.2 Power Up Initialization Sequence

During power on, the host shall:

```text
1.    Ramp up VIN_Bulk supply.
2.    Hold VIN_Bulk supply stable for a minimum of tVIN_Bulk_to_VR_Enable time.
3.    Hold VR_EN pin to static low or high. There is no timing relationship required on VR_EN pin with
      respect to VIN_Bulk input supply ramp up as long as VR_EN pin is held to static level to either low
      or high.
4.    During VIN_Bulk ramp, if VR_EN signal is held low, it can transition to high only once for normal
      operation. Once high, it shall remain high. The VR_EN signal is not allowed to transition to low
      during VIN_Bulk ramp up. An exception is allowed when the platform suffers unexpected power loss
      during VIN_Bulk ramp. For this exception case, the PMIC shall guarantee normal operation at
      subsequent successful power up ramp. There is no limit how many times this exceptional condition
      can occur at the platform level and hence PMIC shall be responsible to guarantee normal operation
      at subsequent successful power up ramp.
5.    If VR_EN pin is held High during VIN_Bulk ramp up or transitions to High during VIN_Bulk ramp up,
      the PMIC turns on its output rails.
6.    If VR_EN pin is held Low during VIN_Bulk Ramp, assert VR_EN signal High to turn on PMIC output
      rails. Alternatively, host can issue VR Enable command by setting register Table 154, Register 0x32
      [7] = ‘1’ via I2C/I3C Basic bus or via DEVCTRL CCC to turn on PMIC output rails.
```

## 4.2.1 Power Up Sequence

Figure 14 to Figure 17 show examples of PMIC power up initialization sequence. Note that the specific sequence of ramping the output regulators (SWA, SWB, SWC, SWD) is for example purpose only. The specific ramp up sequence is configurable through power on sequence configuration registers.

After VR Enable command is registered on the I2C or I3C Basic bus or VR_EN pin is registered high, the PMIC shall complete the following steps within tPMIC_PWR_GOOD_OUT:

```text
1.        Check VIN_Bulk Power Good status is valid.
2.        Power up itself - PMIC executes Power On Sequence Config 0 (Table 182, Register 0x40) to Power
          On Sequence Config 3 (Table 185, Register 0x43) registers and configures PMIC internal registers
          as programmed in PMIC5200 vendor memory space registers.
3.        Power up all enabled output switch regulators and ready for normal operation
4.        Update status registers Table 112, Register 0x08 [5:2] and floats PWR_GOOD signal within
          maximum of tPMIC_PWR_GOOD_OUT time.
```

If PMIC PWR_GOOD signal is not floated within tPMIC_PWR_GOOD_OUT time, the host can access the PMIC status registers for detailed information after tPMIC_PWR_GOOD_OUT time. The PMIC may NACK for any host request on I2C or I3C Basic bus after VR Enable command (either with VR_EN pin high or on I2C/I3C Basic Bus) until tPMIC_PWR_GOOD_OUT time expires.

```text
                                                   tManagement_Ready

                                    t1.8V_Ready

                                                  t1.0V_Ready
                                                                              tPMIC_PWR_GOOD_OUT
  VIN_Bulk

 VOUT_1.8V

 VOUT_1.0V
                                                     tVIN_Bulk_to_VR_Enable

              No VR En command on the Bus
  I2 C/I3C

  VR_EN

    SWD

    SWC

    SWB

    SWA

PWR_GOOD
```

*Figure 14 — Power Up Sequence; VR_EN Pin High after VIN_Bulk Ramp; No Bus Command* (figure; any text below/above was extracted from the drawing)

```text
                                                 tManagement_Ready
                                  t1.8V_Ready

                                                t1.0V_Ready
 VIN_Bulk

 OUT_1.8V

VOUT_1.0V
                                                               tVIN_Bulk_to_PMIC_PWR_GOOD_OUT

            No VR En command on the Bus
 I2 C/I3C

 VR_EN

   SWD

   SWC

   SWB

  SWA

WR_GOOD
```

*Figure 15 — Power Up Sequence; VR_EN Pin High before VIN_Bulk Ramp; No Bus Command* (figure; any text below/above was extracted from the drawing)

```text
                                                 tManagement_Ready
                                  t1.8V_Ready

                                                t1.0V_Ready
 VIN_Bulk

VOUT_1.8V

VOUT_1.0V
                                                               tVIN_Bulk_to_PMIC_PWR_GOOD_OUT

            No VR En command on the Bus
 I2 C/I3C

 VR_EN

   SWD

   SWC

   SWB

  SWA

WR_GOOD
```

*Figure 16 — Power Up Sequence; VR_EN Pin High during VIN_Bulk Ramp; No Bus Command* (figure; any text below/above was extracted from the drawing)

```text
                                                 tManagement_Ready
                                  t1.8V_Ready

                                                t1.0V_Ready
                                                                                    tPMIC_PWR_GOOD_OUT
 VIN_Bulk

VOUT_1.8V

VOUT_1.0V
                                                   tVIN_Bulk_to_VR_Enable

            VR En Command on the Bus
 I2 C/I3C                                                                   VR_EN

                                                                                     Input Pin Going High has no
                                                                                        effect in operation
  VR_EN
   SWD

   SWC

   SWB

   SWA

WR_GOOD
```

*Figure 17 — PMIC Power Up Sequence; with Bus Command* (figure; any text below/above was extracted from the drawing)

```text
                                                  tManagement_Ready
                                   t1.8V_Ready

                                                 t1.0V_Ready
                                                                                tPMIC_PWR_GOOD_OUT
 VIN_Bulk

VOUT_1.8V

VOUT_1.0V
                                                    tVIN_Bulk_to_VR_Enable       VR_EN command after VR_EN
                                                                               pin high has no effect in operatin
 2          VR En Command on the Bus
 I C/I3C                                                                               VR_EN

 VR_EN

     SWD

     SWC

     SWB

     SWA

WR_GOOD
```

*Figure 18 — PMIC Power Up Sequence; with VR_EN Pin followed by Bus Command* (figure; any text below/above was extracted from the drawing)
