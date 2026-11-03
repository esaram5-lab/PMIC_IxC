---
document: JESD301-2 (PMIC5100 Power Management IC Standard, Rev. 1.03, October 2022)
device: PMIC5100
application: client
section: 6.7
title: Power Good (PWR_GOOD) Signal
pages: 47-50
---
# 6.7 Power Good (PWR_GOOD) Signal

The PWR_GOOD output signal type can be configured as either output only or input and output through register Table 138, “Register 0x32” [5]. By default, PWR_GOOD is an output signal. The PWR_GOOD signal can only be configured once, at power on, before issuing VR Enable command (either with VR_EN pin or on I2C/I3C Basic bus). The PWR_GOOD signal configuration applies to both secure mode or programmable mode of operation. Clause 6.7.1, Clause 6.7.2, Table 25, and Table 26 describe PMIC behavior.

**Table 25 — PMIC Operation; PWR_GOOD Type: Input and Output**

```text
    External                    PMIC’s Internal
 PWR_GOOD Input                  PWR_GOOD                                   PMIC Operation                              Notes
          High                 High                      High (Power Good) Normal Operation
                                                          Low (Power Not Good) PMIC Communicates its
          High                         Low                                                                                1,2
                                                                      Status; Clause 6.7.1
Transition from High to                                   Low; (PMIC Good) PMIC Executes VR Disable
                                       High                                                                                3
          Low                                                            Command
                                                           Low; (PMIC Power Not Good) PMIC Internally
          Low                          Low
                                                                  Generates VR Disable Command
NOTE 1 The PMIC indicates its own internal status and it may shut down on its own by following Power Off Config0 to Power Off
       Config2 sequence.
NOTE 2 This is a transient state and the net results of the PWR_GOOD signal is Low.

NOTE 3 The PMIC shuts down based on external command by following Power Off Config0 to Power Off Config2 sequence.
```

**Table 26 — PMIC Operation; PWR_GOOD Type: Output Only**

```text
    External                    PMIC’s Internal
 PWR_GOOD Input                  PWR_GOOD                                   PMIC Operation                              Notes
   X (High or Low)             High                      Normal Operation
   X (High or Low)                     Low                   PMIC communicates its status; Clause 6.7.1                    1
NOTE 1 The PMIC indicates its own internal status and it may shut down on its own by following Power Off Config0 to Power Off
       Config2 sequence.
```

## 6.7.1 PWR_GOOD as Output Only Signal

When Table 138, “Register 0x32” [5] = ‘0’, the PWR_GOOD signal type is output only; the input of PWR_GOOD signal is ignored. The PMIC PWR_GOOD pin indicates status of VIN_Bulk input supply and all output regulators (VOUT_A, VOUT_B, VOUT_C, VOUT_1.8V, VOUT_1.0V). The PMIC floats PWR_GOOD pin when VIN_Bulk input supply is valid and all enabled output regulator’s (VOUT_A, VOUT_B, VOUT_C, VOUT_1.8V, VOUT_1.0V) tolerances are maintained as configured in the appropriate register space. At first power up, when input supply VIN_Bulk is ramped up and stable, the PMIC keeps PWR_GOOD pin asserted to low; however PMIC updates corresponding status register. By default, the register Table 138, “Register 0x32” [5] = ‘0’. Once PMIC receives VR Enable command (either with VR_EN pin or on I2C/I3C Basic bus) from the host, the PMIC enables all appropriate output regulators and updates corresponding status registers and enters into operating state called as “Regulation”.

At this point, PMIC floats PWR_GOOD pin and the external board pullup resistor pulls the pin high as there may be other PMIC on different DIMM may be driving the PWR_GOOD pin low. Once the PWR_GOOD pin is pulled high (i.e., no other PMIC is driving the PWR_GOOD pin low), the PMIC remains in “Regulation” state. Once the PWR_GOOD pin is high, if PMIC detects any condition either on VIN_Bulk input supply or any of the output regulators (VOUT_A, VOUT_B, VOUT_C, VOUT_1.8V, VOUT_1.0V) that causes the PMIC to update it status registers to indicate the power status is not good, then PMIC asserts PWR_GOOD pin low and keeps it asserted until the host explicitly takes a specific action corresponding to it. The PMIC does not automatically let the PWR_GOOD pin float (i.e., get High) even if the condition that triggered the PMIC to assert the PWR_GOOD pin no longer exists. In other words, the PMIC’s PWR_GOOD pin is latched and once latched, it must be explicitly addressed by the host. If PMIC is operating in Secure mode of operation, see Clause 6.5.3 and Clause 6.5.4 for additional information. If PMIC is in Programmable mode of operation, see Clause 6.5.1 and Clause 6.5.2 for additional information.

## 6.7.2 PWR_GOOD as Input and Output Signal

When Table 138, “Register 0x32” [5] = ‘1’, the PWR_GOOD signal type is both input and output and is only applicable after host issues VR Enable command (either with VR_EN pin or on I2C/I3C Basic bus). Also note that simultaneous usage of PWR_GOOD pin as IO and VR_EN pin is not allowed and considered an illegal configuration. In other words, if VR_EN pin is intended to be used to turn on and turn off output rails, the PWR_GOOD pin must be configured as output only. If PWR_GOOD pin is intended to be used as IO, the VR_EN pin must be connected to GND on the board. The PMIC PWR_GOOD pin indicates status of VIN_Bulk input supply and all output regulators (VOUT_A,

VOUT_B, VOUT_C, VOUT_1.8V, VOUT_1.0V). The PMIC floats PWR_GOOD pin when VIN_Bulk input supply is valid and all enabled output regulator’s (VOUT_A, VOUT_B, VOUT_C, VOUT_1.8V, VOUT_1.0V) tolerances are maintained as configured in the appropriate register space. At first power up, when input supply VIN_Bulk is ramped up and stable, the PMIC keeps PWR_GOOD pin asserted to low; however PMIC updates corresponding status register. The host, prior to issuing VR Enable command on I2C/I3C Basic bus, can configure the register Table 138, “Register 0x32” [5] = ‘1’.When host issues VR Enable command on I2C/I3C Basic bus, the PMIC turns on its output regulators and updates corresponding status registers and enters into operating state called “Regulation”. At this point, the PMIC floats PWR_GOOD pin and waits for external board pullup resistor to pull the pin high as there may be other PMIC on different DIMM may be driving the PWR_GOOD pin low. Once the PWR_GOOD pin is pulled high (i.e., no other PMIC is driving the PWR_GOOD pin low), the PMIC automatically enters in to operating state called “Bulk Control Link Monitor”. Once the PWR_GOOD pin is high, if PMIC detects any condition either on VIN_Bulk input supply or any of the output regulators (VOUT_A, VOUT_B, VOUT_C, VOUT_1.8V, VOUT_1.0V) that causes the PMIC to update it status registers to indicate the power status is not good, then PMIC asserts PWR_GOOD pin low and keeps it asserted until the host explicitly takes a specific action corresponding to it. The PMIC does not automatically let the PWR_GOOD pin float (i.e., get High) even if the condition that triggered the PMIC to assert the PWR_GOOD pin no longer exists. In other words, the PMIC’s PWR_GOOD pin is latched and once latched, it must be explicitly addressed by the host.

In this “Bulk Control Link Monitor” operating state, the PMIC behavior is as follows: If PMIC is operating in Secure mode of operation, see Clause 6.5.3 and Clause 6.5.4 for additional information.

```text
• PMIC allows PWR_GOOD input signal low at any time. The host must keep the PWR_GOOD signal low for
  minimum tPWR_GOOD_Low_Pulse_Width to issue command to PMIC to execute VR Disable. When PMIC
  detects PWR_GOOD signal low, the PMIC internally triggers VR Disable command and shuts off all output
  regulators (the PMIC executes power off sequence config0 (Table 167, “Register 0x58”) to power off sequence
  config2 (Table 169, “Register 0x5A”)); drives PWR_GOOD signal low and unlocks only Table 138, “Register
  0x32” [7]. The PMIC preserves all register contents including the MTP error log registers and keeps all write
  protect registers locked except for the Table 138, “Register 0x32” [7]. As long as there is valid VIN_Bulk
  input supply, the PMIC allows read access to all its configuration registers. The PMIC allows write access to
  non-locked configuration registers and register Table 138, “Register 0x32” [7]. If host issues VR Enable
  command by I2C/I3C bus, the PMIC executes Power on sequence config 0 to Power on sequence config 2
  registers, floats PWR_GOOD output signal and re-locks register Table 138, “Register 0x32” [7].
```

If PMIC is in Programmable mode of operation, see Clause 6.5.3 and Clause 6.5.4 for additional information.

```text
• PMIC allows PWR_GOOD input signal low at any time. The host must keep the PWR_GOOD signal low for
  minimum tPWR_GOOD_Low_Pulse_Width to issue command to PMIC to execute VR Disable. When PMIC
  detects PWR_GOOD signal low, the PMIC internally triggers VR Disable command and shuts off all output
  regulators (the PMIC executes power off sequence config0 (Table 167, “Register 0x58”) to power off sequence
  config2 (Table 169, “Register 0x5A”)); drives PWR_GOOD signal low. The PMIC preserves all register
  contents including the MTP error log registers. As long as there is valid VIN_Bulk input supply, the PMIC
  allows read and write access to all its configuration registers. The host can issue VR Enable command with

  VR_EN command on I2C/I3C Basic bus (i.e., Table 138, “Register 0x32” [7] = ‘1’) again to turn on the
  PMIC’s output regulator and PMIC will execute Power On Config0 to Config2 registers and floats

  PWR_GOOD output signal.
```
