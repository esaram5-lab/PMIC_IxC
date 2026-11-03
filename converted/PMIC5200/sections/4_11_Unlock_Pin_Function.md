---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 4.11
title: Unlock Pin Function
pages: 51-58
---
# 4.11 Unlock Pin Function

Unlock is an asynchronous, active high, input signal. The voltage level on the Unlock input pin is identified in Table 155, Register 0x33 [0]. By default at power on, the Unlock input pin function is enabled and the input receiver is active. The host can disable the Unlock input pin function by writing Table 150, Register 0x2E [3] = ‘0’ when PMIC is in the P2_B state prior to assertion of the first VR_EN command (either by I2C/I3C bus or via VR_EN input pin). The PMIC turns off the input receiver for Unlock pin when the input pin function is disabled. After exiting the P2_B power state, Unlock_Pin_Enable (Table 150, Register 0x2E [3]) can only be cleared by writing secure mode (Table 151, Register 0x2F [2]) = ‘0’, which forces the PMIC to operate in the locked security states. The values of the registers Table 150, Register 0x2E [3], Table 151, Register 0x2F [2], and Table 155, Register 0x33 [0] define the register security state status as identified by the Table 26 and Figure 30. Sub-state transitions between P1, P2_A1, P2_A2, P3, and DVFSQ for each security state are defined by Table 26 and Figure 30. If Table 150, Register 0x2E [3] = ‘0’ in the P2_B power state at the time VR_EN command (either by I2C/I3C bus or VR_EN input pin), the Unlock pin is disabled and register security is determined by the status of Table 151, Register 0x2F [2].

```text
▪ If Table 151, Register 0x2F [2] = ‘0’, the PMIC enters the locked security states and operates in
  secure mode. A power cycle is required to enable Unlocked or Configurable_lock security states.
▪ If Table 151, Register 0x2F [2] = ‘1’. the PMIC enters in the unlocked security states and operates in
  programmable mode. The PMIC transitions from unlocked to locked security states when

  Table 151, Register 0x2F [2] = ‘0’ is written at which point PMIC disables the Unlock pin by setting
  Table 150, Register 0x2E [3] = ‘0’ and places the registers in secure mode. A power cycle is

  required to enable Unlocked or Configurable_lock security states.
```

When Table 150, Register 0x2E [3] = ‘1’, the register Table 151, Register 0x2F [2] follows the input voltage level applied to the Unlock pin at the time or after VR_EN command (either by I2C/I3C bus or VR_EN input pin). Note that prior to first VR_EN command (i.e., when PMIC is in P2_B state), Table 151, Register 0x2F [2] does not follow the Unlock pin.

```text
▪ When Unlock pin is high then Table 155, Register 0x33 [0] = ‘1’ and Table 151, Register 0x2F [2] =
  ‘1’.
▪ When Unlock pin is low then Table 155, Register 0x33 [0] = ‘0’ and Table 151, Register 0x2F [2] =
  ‘0’.
```

When Table 150, Register 0x2E [3] = ‘1’, if Unlock pin is low in the P2_B power state at the time VR_EN command (either by I2C/I3C bus or VR_EN input pin), the PMIC enters the locked security states with registers operating in secure mode, sets Table 151, Register 0x2F [2] = ‘0’ and disables Unlock pin by setting Table 150, Register 0x2E [3] = ‘0’. A power cycle is required to enable Unlocked or Configurable_lock security states.

When Table 150, Register 0x2E [3] = ‘1’, if Unlock pin is high in the P2_B power state at the time VR_EN command (either by I2C/I3C bus or VR_EN input pin), the PMIC enters Configurable lock security states where registers are in programmable mode when Unlock pin is high and in secure mode when Unlock pin is low. The PMIC transitions from configurable lock to locked security states when Table 151, Register 0x2F [2] = ‘0’ is written at which point PMIC disables the Unlock pin by setting Table 150, Register 0x2E [3] = ‘0’ and places the registers in secure mode. A power cycle is required to enable Unlocked or Configurable_lock security states.

```text
                                                                                                 Locked Security State
                                                                                                 PMIC operates in Secure Mode until power cycle
                     P0                                                                          R2F[2] = 0, R2E[3] = 0
                                                                                                                                                              P1_Locked
                                                                                                 Unlock pin status ignored                         I2C/I3C, Lock/Unlock interface is Off
                                          VIN_Bulk = Invalid

                   P2_B                                                                                                                                    DVFSQ_Locked
                                                                                                                 P3_Locked
           Programmable mode
                                      Configuration State
                                      VIN_Bulk = Valid
                                      VR_EN = 0

                                                                                                               P2_A1_Locked                                P2_A2_Locked

          P2_A1_Unlocked                                       P2_A2_Unlocked                         P2_A1_Configurable_Lock                       P2_A2_Configurable_Lock

             P3_Unlocked                                       DVFSQ_Unlocked                            P3_Configurable_Lock                       DVFSQ_Configurable_Lock

                                                                                                 Configuration Lock Security State
Unlocked Security State                                                                          R2E[3] = 1
R2E[3] = 0, R2F[2] = 1                                            P1_Unlocked                    R2F[2] tracks status of Unlock pin
                                                                                                 Programmable mode when Unlock pin = 1
                                                                                                                                                       P1_Configurable_Lock
PMIC operates in programmable mode
Unlock pin status ignored                                I2C/I3C, Lock/Unlock interface is Off   Secure mode when Unlock pin = 0                    I2C/I3C, Lock/Unlock interface is Off
I2C/I3C Bus write R 2F [2] = 0  PMIC transition                                                 I2C/I3C Bus write R2F [2] = 0  PMIC transition
to Locked Security State                                                                         to Locked Security State
```

*Figure 30 — Security State Flow Diagram* (figure; any text below/above was extracted from the drawing)

**Table 26 — PMIC Security State Transition**

```text
                     Start State                                                          End State

                        Unlock                              Event
                                            Register                                                       Register
  State       R2E[3]     Input     R2F[2]                                     State      R2E[3]   R2F[2]              Notes
                                             Status                                                         Status
                          Pin

   P0          N/A        N/A       N/A       N/A       Valid VIN_Bulk        P2_B         1          0    Program
                                                                                                            mable

  P2_B          0         X          0      Program       VR_EN = 1         P3_Locked      0          0    Secure     [1]
                                             mable                                                                    [2]
                                     1                                      P3_Unlock      0          1    Program
                                                                               ed                           mable

                1          0         X      Program      VR_EN = 1[3]       P3_Locked      0          0    Secure     [1],[4]
                                             mable                                                                    [5]
                           1                                                P3_Configr     1          1    Program
                                                                            able_Lock                       mable

P3_Locked       0         X          0      Secure      Write to R2F[2]     P3_Locked      0          0    Secure
                                                       or R2E[3] is don’t
                                                             care

P3_Unlock       0         X          1      Program    Write R2F[2] = ‘0’   P3_Locked      0          0    Secure

   ed                                        mable                                                                    [6]
                0         X          1                 Write R2E[3] = ‘0’   P3_Unlock      0          1    Program
                                                                               ed                           mable

P3_Configu      1          1         1      Program     Unlock --> Low      P3_Configu     1          0    Secure
rable_Lock                                   mable                          rable_Lock

                                                       Write R2E[3] = ‘0’                  1          1    Program    [7]
                                                                                                            mable

                                                       Write R2F[2] = ‘0’   P3_Locked      0          0    Secure

                1          0         0      Secure     Unlock --> High      P3_Configu     1          1    Program
                                                                            rable_Lock                      mable

                                                       Write R2E[3] = ‘0’                  1          0    Secure     [7]

P3_Unlock       0         X          1      Program      See Table 25        DVFSQ         0          1    Program
   ed                                        mable                           Unlocked                       mable

                0         X          1      Program    VR_EN --> Low        P2_A1_Unl      0          1    Program    [8],[9]
                                             mable                            ocked                         mable     [8],[10]
                                                       Write R32[7] = ‘0’

                                                       PWR_GOOD -->                                                   [9],[11]
                                                           Low

                                                          Internal VR       P2_A2_Unl      0          1    Program    [9],[11]
                                                         Disable Fault        ocked                         mable

                                                       VR_EN --> Low        P1_Unlock      0          1      N/A      [9],[12]
                                                                               ed                                     [10],[12]
                                                       Write R32[7] = ‘0’

                   Start State                                                           End State

                       Unlock                             Event
                                          Register                                                        Register
  State      R2E[3]     Input    R2F[2]                                     State       R2E[3]   R2F[2]              Notes
                                           Status                                                          Status
                         Pin

P3_Locked      0         X          0     Secure       See Table 25        DVFSQ          0          0    Secure
                                                                           Locked

               0         X          0     Secure     VR_EN --> Low        P2_A1_Loc       0          0    Secure     [8],[9]
                                                                             ked                                     [9],[11]
                                                     PWR_GOOD -->
                                                         Low

                                                        Internal VR       P2_A2_Loc       0          0    Secure     [9],[11]
                                                       Disable Fault         ked

                                                     VR_EN --> Low        P1_Locked       0          0      N/A      [9],[12]

P3_Configu     1         1          1     Program      See Table 25         DVFSQ         1          1    Program
rable_Lock                                 mable                          Configurabl                      mable
                                                                           e Locked

               1         1          1     Program    VR_EN --> Low        P2_A1_Co        1          1    Program    [8],[9]
                                           mable                          nfigurable_                      mable
                                                     Write R32[7] = ‘0’                                              [8],[10]
                                                                              Lock
                                                     PWR_GOOD -->                                                    [9],[11]

                                                         Low

                                                        Internal VR       P2_A2_Co        1          1    Program    [9],[11]

                                                       Disable Fault      nfigurable_                      mable
                                                                              Lock

                                                     VR_EN --> Low        P1_Configu      1          1      N/A      [9],[12]
                                                                          rable_Lock                                 [10],[12]
                                                     Write R32[7] = ‘0’

               1         0          0     Secure       See Table 25         DVFSQ         1          0    Secure
                                                                          Configurabl
                                                                           e Locked

               1         0          0     Secure     VR_EN --> Low        P2_A1_Co        1          0    Secure     [8],[9]
                                                                          nfigurable_                                [9],[11]
                                                     PWR_GOOD -->
                                                                              Lock
                                                         Low

                                                        Internal VR       P2_A2_Co        1          0    Secure     [9],[11]
                                                       Disable Fault      nfigurable_
                                                                              Lock

                                                     VR_EN --> Low        P1_Configu      1          0      N/A      [9],[12]
                                                                          rable_Lock

                    Start State                                                           End State

                        Unlock                             Event
                                           Register                                                        Register
  State       R2E[3]     Input    R2F[2]                                     State       R2E[3]   R2F[2]              Notes
                                            Status                                                          Status
                          Pin

P2_A1_Unl       0         X          1     Program    Write R2F[2] = ‘0’   P2_A1_Loc       0          0    Secure
  ocked                                     mable                             ked

                                                      Write R2E[3] = ‘1’   P2_A1_Unl       0          1    Program    [6]
                                                                             ocked                          mable

                0         X          1     Program    VR_EN --> High       P3_Unlock       0          1    Program    [10]
                                            mable                                                           mable     [10]
                                                      Write R32[7] = ‘1’

                                                        Internal Fault     P2_A2_Unl                                  [9]
                                                      (e.g., LDO fault)      ocked

P2_A2_Unl       0         X          1     Program      See Table 25       P3_Unlock       0          1    Program
  ocked                                     mable                             ed                            mable

                0         X          1     Program    Write R2F[2] = ‘0’   P2_A2_Loc       0          0    Secure
                                            mable                  ng         ked

                                                      Write R2E[3] = ‘1’   P2_A2_Unl       0          1    Program    [6]
                                                                             ocked                          mable

P2_A1_Loc       0         X          0     Secure     VR_EN --> High       P3_Locked       0          0    Secure     [10]
   ked
                                                        Internal Fault     P2_A2_Loc       0          0    Secure

                                                      (e.g., LDO fault)       ked

P2_A2_Loc       0         X          0     Secure            N/A           P2_A2_Loc       0          0    Secure     [13]

   ked                                                                        ked

P2_A1_Co        1         1          1     Program     Unlock --> Low      P2_A1_Co        1          0    Secure
nfigurable_                                 mable                          nfigurable_                                [7]
                                                      Write R2E[3] = ‘0’                   1          1    Program
    Lock                                                                       Lock
                                                                                                            mable

                                                      Write R2F[2] = ‘0’   P2_A1_Loc       0          0    Secure
                                                                              ked

                1         1          1     Program    VR_EN --> High       P3_Configu      1          1    Program
                                            mable                          rable_Lock                       mable
                                                      Write R32[7] = ‘1’

                                                        Internal Fault     P2_A2_Co                                   [9]
                                                      (e.g., LDO fault)    nfigurable_
                                                                               Lock

                1         0          0     Secure     Unlock --> High      P2_A1_Co        1          1    Program
                                                                           nfigurable_                      mable
                                                                               Lock                                   [7]
                                                      Write R2E[3] = ‘0’                   1          0    Secure

                1         0          0     Secure     VR_EN --> High       P3_Configu      1          0    Secure
                                                                           rable_Lock

                                                        Internal Fault     P2_A2_Co        1          0    Secure
                                                      (e.g., LDO fault)    nfigurable_
                                                                               Lock

                    Start State                                                           End State

                        Unlock                             Event
                                           Register                                                        Register
  State       R2E[3]     Input    R2F[2]                                     State       R2E[3]   R2F[2]              Notes
                                            Status                                                          Status
                          Pin

P2_A2_Co        1         1          1     Program      See Table 25       P3_Configu      1          1    Program
nfigurable_                                 mable                          rable_Lock                       mable
    Lock
                1         1          1     Program     Unlock --> Low      P2_A2_Co        1          0    Secure
                                            mable                          nfigurable_                                [7]
                                                      Write R2E[3] = ‘0’                   1          1    Program
                                                                               Lock
                                                                                                            mable

                                                      Write R2F[2] = ‘0’   P2_A2_Loc       0          0    Secure
                                                                              ked

                1         0          0     Secure       See Table 25       P3_Configu      1          0    Secure
                                                                           rable_Lock

                1         0          0     Secure     Unlock --> High      P2_A2_Co        1          1    Program
                                                                           nfigurable_                      mable
                                                                               Lock                                   [7]
                                                      Write R2E[3] = ‘0’
                                                                 ng                        1          0    Secure

DVFSQ_Lo        0         X          0     Secure       See Table 25       P3_Locked       0          0    Secure
  cked
                                                        See Table 25       P2_A2_Loc       0          0    Secure

                                                                              ked

                                                        See Table 25       P2_A1_Loc       0          0    Secure

                                                                              ked

                                                        See Table 25       P1_Locked       0          0      N/A

                0         X          0     Secure     Write R2E[3] = ‘1’   DVFSQ_Lo        0          0    Secure
                                                                             cked

DVFSQ_Un        0         X          1     Program      See Table 25       P3_Unlock       0          1    Program
  locked                                    mable                             ed                            mable

                                                        See Table 25       P2_A2_Unl       0          1    Program
                                                                             ocked                          mable

                                                        See Table 25       P2_A1_Unl       0          1    Program
                                                                             ocked                          mable

                                                        See Table 25       P1_Locked       0          1      N/A

                0         X          1     Program    Write R2F[2] = ‘0’   DVFSQ_Lo        0          0    Secure
                                            mable                            cked

                                                      Write R2E[3] = ‘1’   DVFSQ_Un        0          1    Program    [6]
                                                                             locked                         mable

                      Start State                                                                    End State

                         Unlock                                    Event
                                                Register                                                                Register
  State        R2E[3]     Input      R2F[2]                                           State        R2E[3]    R2F[2]                   Notes
                                                 Status                                                                  Status
                           Pin

DVFSQ_Co          1          1          1       Program        See Table 25        P3_Configu         1          1       Program
nfigurable_                                      mable                             rable_Lock                             mable
    Lock                                                                               ed

                                                               See Table 25        P2_A2_Co           1          1       Program
                                                                                   nfigurable_                            mable
                                                                                       Lock

                                                               See Table 25        P2_A1_Co           1          1       Program
                                                                                   nfigurable_                            mable
                                                                                       Lock

                                                               See Table 25        P1_Configu         1          1       Program
                                                                                   rable_Lock                             mable

                  1          1          1       Program       Unlock --> Low       DVFSQ_Co           1          0       Secure
                                                 mable                             nfigurable_                                        [7]
                                                             Write R2E[3] = ‘0’                       1          1       Program
                                                                                       Lock
                                                                                                                          mable

                                                             Write R2F[2] = ‘0’    DVFSQ_Lo           0          0       Secure

                                                                                     cked

                  1          0          0        Secure        See Table 25        P3_Configu         1          0       Secure
                                                                                   rable_Lock

                                                                                       ed

                                                               See Table 25        P2_A2_Co           1          0       Secure
                                                                                   nfigurable_
                                                                                       Lock

                                                               See Table 25        P2_A1_Co           1          0       Secure
                                                                                   nfigurable_
                                                                                       Lock

                                                               See Table 25        P1_Configu         1          0       Secure
                                                                                   rable_Lock

                  1          0          0        Secure       Unlock --> High      DVFSQ_Co           1          1       Program
                                                                                   nfigurable_                            mable
                                                                                       Lock                                           [7]
                                                             Write R2E[3] = ‘0’                       1          0       Secure
   NOTE 1 The PMIC requires power cycle to enable P2_B, P3_Unlocked, or P3_Configurable_lock security states.
   NOTE 2 The PMIC operates in unlocked state where all registers are in programmable mode. The host can write R2F[2] to ‘0’ and
          PMIC enters in secure mode. Power cycle is required to enable P2_B, P3_Unlocked or P3_Configurable_lock states. Note:
          After VR_EN command, if host writes R2E[3] = 1 to enable the Unlock input pin receiver and then writes R2F[2] = ‘0’, the
          PMIC still enters secure mode but keeps the R2E[3] = ‘0’ and keeps the Unlock input pin receiver disabled.
   NOTE 3 The PMIC samples the Unlock input pin in conjunction with VR_EN command.
   NOTE 4 The PMIC updates R2F[2] register to ‘0’ and operates in P3_Locked state where all registers are secure (i.e., locked),
          updates R2E[3] register to ‘0’ and hence disables the Unlock input pin receiver.
   NOTE 5 The PMIC operates in P3_Configurable lock states where register R2F[2] = ‘1’.
   NOTE 6 The R2E[3] register is unique. The write ‘1’ operation to this register is ignored and PMIC keeps the Unlock input pin receiver
          disabled.

NOTE 7 The R2E[3] register is unique. The write ‘0’ operation to this register is ignored and PMIC keeps the Unlock input pin receiver
       enabled. The R2E[3] = ‘0’ write operation is only allowed while PMIC is in P2_B state.
NOTE 8 R1A[4] = ‘0’
NOTE 9 PWR_GOOD output = Low
NOTE 10 PWR_GOOD output = Float
NOTE 11 R1A[4] = X (either ‘0’ or ‘1’)
NOTE 12 R1A[4] = ‘1’
NOTE 13 Requires power cycle.
```
