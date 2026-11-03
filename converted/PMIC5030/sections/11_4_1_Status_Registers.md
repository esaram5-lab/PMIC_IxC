---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 11.4.1
title: Status Registers
pages: 132-146
---
# 11.4.1 Status Registers

The PMIC offers status registers that are grouped into four different categories.

1. Global History of Error Log Register (Table 108, Register 0x03 [7:0], Table 109, Register 0x04 [7:0])

2. Error Log Registers (Table 110, Register 0x05 [6:0], Table 111, Register 0x06[7:0], Table 112, Register

```text
0x07 [7:4,1:0].
```

3. Real time Status Registers (Table 113, Register 0x08 [7:0], Table 114, Register 0x09 [7:0], Table 115,

```text
Register 0x0A [7:1], Table 116, Register 0x0B [7:0], Table 157, Register 0x33 [4:2], Table 175, Register
0x108 [7:0], Table 176, Register 0x109 [7:6, 0], Table 177, Register 0x10A [7:4])
```

4. Periodic Status Registers (Table 117, Register 0x0C [7:0] to Table 120, Register 0x0F [7:0], Table 157,

```text
Register 0x33 [7:5], Table 167, Register 0x100 [7:0], Table 168, Register 0x101 [7:4, 2:0],Table 169,
Register 0x102 [7:0] to Table 174, Register 0x107 [7:0])
```

Global History of Error Log Registers (Table 108, Register 0x03 [7:0])

```text
▪ This register reports the cumulative error of MTP NVM check at each power on for DIMM vendor
  region and PMIC vendor region MTP. The PMIC writes the register bits [7:4] on its own when it
  detects mismatch in CRC code for DIMM vendor region and the register bits [3:0] when it detects an
  error for PMIC vendor region.
▪ The register bits Table 108, Register 0x03 [7:0] are not erasable by any command by the host and
  shall be preserved by the PMIC. See clause 6.30 for additional details.
```

Global History of Error Log Registers (Table 109, Register 0x04 [7:0])

```text
▪ This register records the PMIC state at each abnormal power down cycle. This register reports the
  cumulative error of each abnormal power down sequence. The PMIC writes this register on its own
  when it internally generates VR Disable command on its own due to failure.
▪ The host can erase the register bits Table 109, Register 0x04 [7:4] in MTP memory and clear the
  status register by writing the code 0x74 in Table 162, Register 0x39. The register bits Table 109,
  Register 0x04 [3:0] are not erasable by any command by the host and shall be preserved by the
  PMIC. See clause 6.29 for additional details.
```

Error Log Registers (Table 110, Register 0x05 [6:0], Table 111, Register 0x06 [7:0] to Table 112, Register 0x07 [7:4,1:0])

```text
       ▪ These registers record the PMIC state at each power down sequence. The PMIC may report
         abnormal power down sequence or normal power down sequence. The PMIC writes these registers
         and updates MTP when it internally generates a VR Disable command on its own due to failure. At
         next power up, the registers are restored from MTP to be read by the host and MTP is cleared by
         the PMIC. A value of ‘0’ in the register indicates no fault event occurred prior to last power down
         cycle.
       ▪ The host can clear the status registers and associated MTP by writing the code 0x74 in Table 162,
         Register 0x39. See Figure 35 for illustration. The top waveform illustrates how PMIC captures Error
         Log Registers (R05 to R07) when there is a fault and how PMIC reports error log registers when
         PMIC goes through power down cycle. The bottom waveform illustrates same as top waveform with
         one exception. It shows no fault condition when CAMP is asserted to turn off switch regulator
         outputs with power down sequence.
       ▪ The word Power Cycle is used interchangeably with Power Down Cycle as illustrated in both figures
         and it means both VIN_Bulk and VIN_Mgmt input supplies are removed and re-applied. Power
         Down Sequence means execution of Power Off Sequence configuration registers (Table 256,
         Register 0x58 to Table 260, Register 0x5C, Table 266, Register 0x62, Table 269, Register 0x65,
         and Table 270, Register 0x66).

                                               Power (Down) Cycle: Off + On

VIN_Bulk & VIN_Mgmt

            CAMP
                                                                                                                       No Fault
             VOUTx                                                                                                      event

                           VR                                                   VR                                                                     VR
                         Enable                                               Enable                                                                 Enable
                                  Fault                                                Fault                                                                  Fault
                                          R05, R06,                   Read                     R05, R06,     Read         No event        Read                        R05, R06,     Read
                                  event                                                event                                                                  event
                                           R07 Log                    Error                     R07 Log      Error           to           Error                        R07 Log      Error
                                           capture                     Log                      capture       Log         capture          Log                         capture       Log
                                                                    R05, R06,                              R05, R06,                     R05, R06,                                R05, R06,
                                                                       R07                                    R07                       R07 = 0x00                                   R07

                                               Power (Down) Cycle: Off + On

VIN_Bulk & VIN_Mgmt

             CAMP

             VOUTx

                           VR                                                   VR                                  VR                                 VR
                         Enable                                               Enable                              Enable                             Enable
                                  Fault                                                Fault                                                                  Fault
                                          R05, R06,                   Read                     R05, R06,     Read                         Read                        R05, R06,     Read
                                  event                                                event                                                                  event
                                           R07 Log                    Error                     R07 Log      Error                        Error                        R07 Log      Error
                                           capture                     Log                      capture       Log                          Log                         capture       Log
                                                                    R05, R06,                              R05, R06,         No Event    R05, R06,                                R05, R06,
                                                                      R07                                    R07                to      R07 = 0x00                                  R07
                                                                                                                             captu re
```

*Figure 35 — Error Log (R05 to R07) Registers Behavior with Power Cycle* (figure; any text below/above was extracted from the drawing)

Real Time Status Registers (Table 113, Register 0x08 [7:0], Table 114, Register 0x09 [7:0], Table 115, Register 0x0A [7:1], to Table 116, Register 0x0B [7:0], Table 157, Register 0x33 [4:2], Table 175, Register 0x108 [7:0], Table 176, Register 0x109 [7:6, 0], Table 177, Register 0x10A [7:4])

```text
▪ These registers are one time latched registers. Once the PMIC sets the register flag to ‘1’ based on
  the event that occurs, the host must explicitly clear the register appropriately. The PMIC does not
  automatically update the register on its own and the status registers remains at ‘1’ even if the event
  that triggered the status is no longer present. An exception is applied to Table 177, Register 0x10A
  [7:4] as it cannot be cleared by the host.
▪ Any switch regulator related status registers are only applicable after VR Enable command is
  registered by the PMIC. The PMIC updates switch regulators related status registers after VR
  Enable command is registered within tPMIC_PWR_GOOD_OUT time if there is any issue and host
  shall check these status registers after tPMIC_PWR_GOOD_OUT time. The PMIC updates these
  status registers if there is any event related to switch regulators in future. The GSI_n interrupt or
  PWR_GOOD interrupt may be generated by the PMIC at the same time depending on the type of
  event. The interrupts are only generated if they are not masked.
▪ The status registers Table 113, Register 0x08 [7] is only valid once valid VIN_Bulk input supply is
  reached at the PMIC input pin.
▪ The status registers Table 114, Register 0x09 [5], Table 115, Register 0x0A [3:1] and Table 157,
  Register 0x33 [2] are only valid once valid VIN_Mgmt input supply is reached at the PMIC input pin
  at first power on. These registers are also valid when PMIC switches over to VIN_Bulk input supply.
▪ The remaining status registers are valid after VR Enable command is registered.
```

Periodic Status Registers (Table 117, Register 0x0C [7:0] to Table 120, Register 0x0F [7:0], Table 157, Register 0x33 [7:5], Table 167, Register 0x100 [7:0], Table 168, Register 0x101 [7:4, 2:0], Table 169,

Register 0x102 [7:0] to Table 174, Register 0x107 [7:0])

```text
▪ These registers are updated periodically at certain frequency and they represent the status at that
  point. All these registers except for Table 157, Register 0x33 [7:5] are only valid after VR Enable
  command is registered by the PMIC.
▪ The register Table 157, Register 0x33 [7:5] is valid before and after VR Enable command.
```

**Table 108 — Register 0x03**: see [`registers/0x03.md`](../registers/0x03.md)

**Table 109 — Register 0x04**: see [`registers/0x04.md`](../registers/0x04.md)

**Table 110 — Register 0x05**: see [`registers/0x05.md`](../registers/0x05.md)

**Table 111 — Register 0x06**: see [`registers/0x06.md`](../registers/0x06.md)

**Table 112 — Register 0x07**: see [`registers/0x07.md`](../registers/0x07.md)

**Table 113 — Register 0x08**: see [`registers/0x08.md`](../registers/0x08.md)

**Table 114 — Register 0x09**: see [`registers/0x09.md`](../registers/0x09.md)

**Table 115 — Register 0x0A**: see [`registers/0x0A.md`](../registers/0x0A.md)

**Table 116 — Register 0x0B**: see [`registers/0x0B.md`](../registers/0x0B.md)

**Table 117 — Register 0x0C**: see [`registers/0x0C.md`](../registers/0x0C.md)

**Table 118 — Register 0x0D**: see [`registers/0x0D.md`](../registers/0x0D.md)

**Table 119 — Register 0x0E**: see [`registers/0x0E.md`](../registers/0x0E.md)

**Table 120 — Register 0x0F**: see [`registers/0x0F.md`](../registers/0x0F.md)
