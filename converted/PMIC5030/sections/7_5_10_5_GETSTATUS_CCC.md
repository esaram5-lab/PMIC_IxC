---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 7.5.10.5
title: GETSTATUS CCC
pages: 102-103
---
# 7.5.10.5 GETSTATUS CCC

The GETSTATUS CCC is supported in I3C Basic mode. In I2C mode, this CCC is ignored (i.e., it is not executed internally and the Repeat Start byte arriving after the 0x90 GETSTATUS CCC code is not acknowledged and host must do STOP operation. Table 82 through Table 83 show an example of a single GETSTATUS CCC. If PEC function is enabled, the PEC calculation starts with Start or Repeat Start operation but does not include 7’h7E with W=0 byte in PEC calculation.

**Table 82 — GETSTATUS CCC - Direct**

```text
 Start       Bit 7       Bit 6        Bit 5       Bit 4        Bit 3       Bit 2       Bit 1       Bit 0      A/N/T        Stop

S or Sr       1            1            1           1            1           1           0         W=0          A[1]

                                                   0x90 (Direct)                                                 T

   Sr                                         DevID[6:0]                                            R=1          A

           PEC_Err         0            0           0            0           0           0           0         T=1

              0            0         P_Err       R32[3]                   Pending Interrupt                    T=0       Sr[2] or P
  NOTE 1    The PMIC NACKs if there is a parity error in a previous transaction when host performs consecutive transactions with
            Repeat Start.
  NOTE 2    Repeat Start or Repeat Start with 7’h7E.
```

**Table 83 — GETSTATUS CCC - Direct with PEC**

```text
Start      Bit 7        Bit 6       Bit 5       Bit 4         Bit 3      Bit 2       Bit 1        Bit 0      A/N/T       Stop

  S          1            1           1           1            1           1           0          W=0         A[1]

                                                 0x90 (Direct)                                                 T

                                                        PEC                                                    T

  Sr                                         DevID[6:0]                                           R=1          A

          PEC_Err         0           0           0            0           0           0           0          T=1

             0            0        P_Err       R32[3]                   Pending Interrupt                     T=1

                                                        PEC                                                   T=0      Sr[2] or P
 NOTE 1     The PMIC NACKs if there is a parity or PEC error in a previous transaction when host performs consecutive transactions
            with Repeat Start.
 NOTE 2     Repeat Start or Repeat Start with 7’h7E.
```

**Table 84 — GETSTATUS CCC Byte Encoding**

```text
   Bit                            Encoding                                                      Notes

PEC_Err          0 = No Error                                        This register is cleared when Host issues clear command to
                 1 = PEC Error Occurred                              Table 123, Register 0x12 [3] for PEC error

 P_Err           0 = No Error                                        This register is cleared when Host issues clear command to
                 1 = Protocol Error; Parity Error occurred           Table 123, Register 0x12 [2] for Parity error.

 R32[3]          See Table 155, Register 0x32 for encoding.          PMIC reflects the register status of Table 155, Register
                                                                     0x32 [3] in this bit.

Pending          0000 = No Pending Interrupt or No New               This register is cleared when Host issues clear command to
Interrupt        Global Status Event                                 any appropriate device status register that causes IBI status
                 0001 = Pending Interrupt or New Global              register to get cleared.
                 Status Event
                 All other encodings are reserved
```

When the PMIC device responds to GETSTATUS CCC, after it completes the response, the PEC_Err, P_Err and Pending Interrupt Bits [3:0] do not automatically get cleared. The host must explicitly clear the appropriate status register through Clear command by writing ‘1’ to corresponding register or by issuing Global Clear command. Once the PMIC device clears the appropriate status register, only then PEC_Err, P_err and Pending Interrupt Bits [3:0] gets cleared.

After host issues clear command, if the condition is still present, the device will again set the appropriate status register, sets the IBI status register to ‘1’ and Pending Interrupt Bits [3:0] to ‘0001’.
