---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 5.4.10.5
title: GETSTATUS CCC
pages: 108-109
---
# 5.4.10.5 GETSTATUS CCC

The GETSTATUS CCC is supported in I3C Basic mode. In I2C mode, this CCC is ignored (i.e., it is not executed internally and the Repeat Start byte arriving after the 0x90 GETSTATUS CCC code is not acknowledged and host must do STOP operation). Table 81 to Table 82 show an example of a single GETSTATUS CCC. In I3C mode only, if PEC function is enabled, the PEC calculation starts with Start or Repeat Start operation but does not include 7’h7E with W=0 byte in PEC calculation.

**Table 81 — GETSTATUS CCC - Direct**

```text
    Start        Bit 7      Bit 6      Bit 5       Bit 4         Bit 3    Bit 2      Bit 1      Bit 0      A/N/T        Stop

   S or Sr        1           1          1           1            1        1           0        W=0          A[1]
                                                    0x90 (Direct)                                             T

     Sr                                         DevID[6:0]                                       R=1         A1
               PEC_E          0          0           0            0        0           0          0         T=1

                 rr
                  0           0        P_Err         0                   Pending Interrupt                  T=0       Sr[2] or P
NOTE 1 The PMIC device NACKs if there is a parity error in a previous transaction when host performs consecutive transactions
       with Repeat Start.
NOTE 2 Repeat Start or Repeat Start with 7’h7E.
```

**Table 82 — GETSTATUS CCC - Direct with PEC**

```text
    Start        Bit 7      Bit 6      Bit 5       Bit 4         Bit 3    Bit 2      Bit 1      Bit 0      A/N/T        Stop
   S or Sr        1           1          1           1            1        1           0        W=0          A[1]
                                                    0x90 (Direct)                                             T
                                                           PEC                                                T
     Sr                                         DevID[6:0]                                       R=1         A1
               PEC_E          0          0           0            0        0           0          0         T=1
                 rr
                  0           0        P_Err         0                   Pending Interrupt                  T=1
                                                           PEC                                              T=0       Sr[2] or P
NOTE 1 The PMIC device NACKs if there is a parity or PEC error in a previous transaction when host performs consecutive
       transactions with Repeat Start.
NOTE 2 Repeat Start or Repeat Start with 7’h7E.
```

**Table 83 — GETSTATUS CCC Byte Encoding**

```text
     Bit                           Encoding                                             Notes
PEC_Err             0 = No Error                            This register is cleared when Host issues clear command
                    1 = PEC Error Occurred                  to Table 122, Register 0x12 [3]
    P_Err           0 = No Error                            This register is cleared when Host issues clear command
                    1 = Protocol Error; Parity Error        to Table 122, Register 0x12 [2].
                    Occurred
  Pending           0000 = No Pending Interrupt or No       This register is cleared when Host issues clear command
  Interrupt         New Global Status Event                 to any appropriate device status register that causes IBI
                    0001 = Pending Interrupt or New         Status register to get cleared.
                    Global Status Event
                    All other encodings are reserved
```

When the PMIC device responds to GETSTATUS CCC, after it completes the response, the PEC_Err, P_Err and Pending Interrupt Bits [3:0] do not automatically get cleared. The host must explicitly clear the appropriate status register through Clear command by writing ‘1’ to appropriate status or by issuing Global Clear command. Once device clears the appropriate status register, only then PEC_Err, P_Err and Pending Interrupt Bits [3:0] gets cleared.

After host issues clear command, if the condition is still present, the device will again set the appropriate status register, sets the IBI status register Table 114, Register 0x0A [1] to ‘1’ and Pending Interrupt Bits

[3:0] to ‘0001’.
