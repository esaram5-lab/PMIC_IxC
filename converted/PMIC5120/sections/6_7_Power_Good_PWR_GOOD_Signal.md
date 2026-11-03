---
document: JESD301-6 (PMIC5120 Power Management IC Standard, Version 1.0, February 2025)
device: PMIC5120
application: client
section: 6.7
title: Power Good (PWR_GOOD) Signal
pages: 50-53
---
# 6.7 Power Good (PWR_GOOD) Signal

The PWR_GOOD output signal type can be configured as either output only or input and output through register Table 146, Register 0x32 [5]. By default, PWR_GOOD is an output signal. The PWR_GOOD signal can only be configured once, at power on, before issuing VR Enable command (either with VR_EN pin or on I2C/I3C Basic bus). The PWR_GOOD signal configuration applies to both secure mode or programmable mode of operation.

Section 6.7.1, Section 6.7.2, Table 27, and Table 28 describe PMIC’s behavior.

**Table 27 — PMIC Operation; PWR_GOOD Type: Input and Output**

```text
External PWR_GOOD              PMIC’s Internal
                                                                        PMIC Operation                          Notes
        Input                   PWR_GOOD
            High                      High                   High (Power Good); Normal Operation
                                                      Low (Power Not Good); PMIC Communicates its Status;         1,2
            High                      Low
                                                             See Section 6.7.1 for more information
   Transition from High to                               Low(Power Good); PMIC Executes VR Disable                 3
                                      High
             Low                                                           Command
                                                      Low (Power Not Good); PMIC Internally Generates VR
            Low                       Low
                                                                       Disable Command
NOTE 1      The PMIC indicates its own internal status and it may shut down on its own by following Power Off Config0 to
            Power Off Config2 sequence.
NOTE 2      This is a transient state and the net results of the PWR_GOOD signal is Low.
NOTE 3      The PMIC shuts down based on external command by following Power Off Config0 to Power Off Config2
            sequence.
```

**Table 28 — PMIC Operation; PWR_GOOD Type: Output Only**

```text
External PWR_GOOD              PMIC’s Internal
                                                                        PMIC Operation                          Notes
        Input                   PWR_GOOD

      X (High or Low)                 High                      (Power Good); Normal Operation
                                                       (Power Not Good); PMIC communicates its status; See         1
      X (High or Low)                 Low

                                                                Section 6.7.1 for more information
NOTE 1      The PMIC indicates its own internal status and it may shut down on its own by following Power Off Config0 to

            Power Off Config2 sequence.
```

## 6.7.1 PWR_GOOD as Output Only Signal

When Table 146, Register 0x32 [5] = ‘0’, the PWR_GOOD signal type is output only; the input of PWR_GOOD signal is ignored.

The PMIC PWR_GOOD pin indicates status of VIN_Bulk input supply and all output regulators (VOUT_A, VOUT_B, VOUT_C, VOUT_1.8V, VOUT_1.0V). The PMIC floats PWR_GOOD pin when VIN_Bulk input supply is valid and all enabled output regulator’s (VOUT_A, VOUT_B, VOUT_C, VOUT_1.8V, VOUT_1.0V) tolerances are maintained as configured in the appropriate register space.

At first power up, when input supply VIN_Bulk is ramped up and stable, the PMIC keeps PWR_GOOD pin asserted to low; however PMIC updates corresponding status register. By default, the register Table 146, Register 0x32 [5] = ‘0’. Once PMIC receives VR Enable command (either with VR_EN pin or on I2C/I3C Basic bus) from the host, the PMIC enables all appropriate output regulators and updates corresponding status registers and enters into operating state called as “Regulation”. At this point, PMIC floats PWR_GOOD pin and the external board pullup resistor pulls the pin high as there may be other PMIC on different DIMM may be driving the PWR_GOOD pin low. Once the PWR_GOOD pin is pulled high (i.e., no other PMIC is driving the PWR_GOOD pin low), the PMIC remains in “Regulation” state.

Once the PWR_GOOD pin is high, if PMIC detects any condition either on VIN_Bulk input supply or any of the output regulators (VOUT_A, VOUT_B, VOUT_C, VOUT_1.8V, VOUT_1.0V) that causes the PMIC to update its status registers to indicate the power status is not good, then PMIC asserts PWR_GOOD pin low and keeps it asserted until the host explicitly takes a specific action corresponding to it. The PMIC does not automatically let the PWR_GOOD pin float (i.e., get High) even if the condition that triggered the PMIC to assert the PWR_GOOD pin no longer exists. In other words, the PMIC’s PWR_GOOD pin is latched and once latched, it must be explicitly addressed by the host.

If PMIC is operating in Secure mode of operation, see Section 6.5.4 and Section 6.5.5 for additional information.

If PMIC is in Programmable mode of operation, see Section 6.5.2 and Section 6.5.3 for additional information.

## 6.7.2 PWR_GOOD as Input and Output Signal

When Table 146, Register 0x32 [5] = ‘1’, the PWR_GOOD signal type is both input and output and is only applicable after host issues VR Enable command (either with VR_EN pin or on I2C/I3C Basic bus). Also note that simultaneous usage of the PWR_GOOD pin as IO and the VR_EN pin is not allowed and considered an illegal configuration. In other words, if the VR_EN pin is intended to be used to turn on and turn off output rails, the PWR_GOOD pin must be configured as output only. If the PWR_GOOD pin is intended to be used as IO, the VR_EN pin must be connected to GND on the board.

The PMIC PWR_GOOD pin indicates status of VIN_Bulk input supply and all output regulators (VOUT_A, VOUT_B, VOUT_C, VOUT_1.8V, VOUT_1.0V). The PMIC floats the PWR_GOOD pin when VIN_Bulk input supply is valid and all enabled output regulator’s (VOUT_A, VOUT_B, VOUT_C, VOUT_1.8V, VOUT_1.0V) tolerances are maintained as configured in the appropriate register space.

At first power up, when input supply VIN_Bulk is ramped up and stable, the PMIC keeps the PWR_GOOD pin asserted to low; however PMIC updates corresponding status register. The host, prior to issuing VR Enable command on I2C/I3C Basic bus, can configure the register Table 146, Register 0x32 [5] = ‘1’. When host issues VR Enable command on I2C/I3C Basic bus, the PMIC turns on its output regulators and updates corresponding status registers and enters into operating state called “Regulation”. At this point, the PMIC floats the PWR_GOOD pin and waits for the external board pullup resistor to pull the pin high as there may be other PMICs on different DIMMs that may be driving the PWR_GOOD pin low. Once the PWR_GOOD pin is pulled high (i.e., no other PMIC is driving the PWR_GOOD pin low), the PMIC automatically enters in to operating state called “Bulk Control Link Monitor”.

Once the PWR_GOOD pin is high, if PMIC detects any condition either on VIN_Bulk input supply or any of the output regulators (VOUT_A, VOUT_B, VOUT_C, VOUT_1.8V, VOUT_1.0V) that causes the PMIC to update its status registers to indicate the power status is not good, then the PMIC asserts the PWR_GOOD pin low and keeps it asserted until the host explicitly takes a specific action corresponding to it. The PMIC does not automatically let the PWR_GOOD pin float (i.e., get High) even if the condition that triggered the PMIC to assert the PWR_GOOD pin no longer exists. In other words, the PMIC’s PWR_GOOD pin is latched and once latched, it must be explicitly addressed by the host.

In this “Bulk Control Link Monitor” operating state, the PMIC’s behavior is as follows:

If the PMIC is operating in Secure mode of operation, see Section 6.5.4 and Section 6.5.5 for additional information.

```text
• The PMIC allows the PWR_GOOD input signal low at any time. The host must keep the PWR_GOOD
  signal low for a minimum of tPWR_GOOD_Low_Pulse_Width to issue a command to the PMIC to exe-
  cute VR Disable. When the PMIC detects the PWR_GOOD signal low, the PMIC internally triggers a VR
  Disable command, shuts off all output regulators (the PMIC executes power off sequence config0
  (Table 176, Register 0x58) to power off sequence config2 (Table 178, Register 0x5A,)), drives the
  PWR_GOOD signal low, and unlocks only Table 146, Register 0x32 [7].

• The PMIC preserves all register contents including the MTP error log registers and keeps all write-
  protected registers locked except for the Table 146, Register 0x32 [7]. As long as there is a valid
  VIN_Bulk input supply, the PMIC allows read access to all its configuration registers. The PMIC allows
  write access to non-locked configuration registers and register Table 146, Register 0x32 [7]. If the host
  issues a VR Enable command on the I2C/I3C bus, the PMIC executes the Power on sequence config0 to
  Power on sequence config2 registers, floats the PWR_GOOD signal and re-locks register Table 146, Reg-
  ister 0x32 [7].
```

If the PMIC is in Programmable mode of operation, see Section 6.5.4 and Section 6.5.5 for additional information.

```text
• The PMIC allows the PWR_GOOD input signal low at any time. The host must keep the PWR_GOOD
  signal low for a minimum of tPWR_GOOD_Low_Pulse_Width to issue a command to the PMIC to exe-
  cute VR Disable. When the PMIC detects the PWR_GOOD signal low, the PMIC internally triggers a VR
  Disable command, shuts off all output regulators (the PMIC executes power off sequence config0
  (Table 176, Register 0x58) to power off sequence config2 (Table 178, Register 0x5A,)), and drives the
  PWR_GOOD signal low. The PMIC preserves all register contents including the MTP error log registers.
  As long as there is a valid VIN_Bulk input supply, the PMIC allows read and write access to all its config-
  uration registers. The host can issue a VR_EN command on the I2C/I3C Basic bus (i.e., Table 146, Regis-
  ter 0x32 [7] = ‘1’) again to turn on the PMIC’s output regulator, and the PMIC will execute the Power On
  Config0 to Config2 registers and float the PWR_GOOD signal.
```
