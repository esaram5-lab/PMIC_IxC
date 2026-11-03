---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 4.9
title: Idle Condition and Quiescent Power State
pages: 47-50
---
# 4.9 Idle Condition and Quiescent Power State

Quiescent Power State definition: All circuits including PMIC switch output and LDO output regulators are off. VR_EN signal is at static low or high level. I2C or I3C Basic interface access is not allowed and is pulled high. PID signal is at static low or high level. Unlock input pin interface is turned off but the input pin level can be at static low or high. This state is only applicable if Table 130, Register 0x1A [4] = ‘1’. This state is labeled as P1 state in Figure 29. Idle Condition definition: All circuits including PMIC switch output and LDO output regulators are on with 0 A load. VR_EN signal is at static low or high level. I2C or I3C Basic interface access is allowed but bus is pulled high. PID signal is at static low or high level. Unlock input pin is at static low or high level. Figure 29 shows high level PMIC states and its definition. The state transitions from each state is defined in Table 25.

```text
                                                                    P0 State:
                                                                    -- VIN_Bulk invalid
                         Non-Event                  Event
                                                                    P1 State:
                                                                    -- R1A[4] = ‘1’
                                                                    -- Entry from P3 State Only
                          P2_A1                  P2_A2
                                                                    P2_B State:
                                                                    -- Transition from P0 or P1 State; Before VR Enable Command
                                                                    -- All Switch Regulators are Off
                                                                    -- All LDOs are on
                                                                    -- PWR_GOOD Output = L
                                                                    -- VR_EN Input = L
                                                                    -- R32[7] = ‘0’

                               P3                                   P2_A1 State (No Fault Event):
      VR_EN Pin                                                     -- Transition from P3; After VR Enable Command
      goes High                                                     -- All Switch Regulators are Off
                                                    DVFSQ           -- All LDOs are on
                                                                    -- PWR_GOOD Output = L or H
                                                                    -- VR_EN Input = L or H
                                                                    -- R32[7] = ‘0’
                         VR_EN CMD
                           On Bus
                                                                  ngP2_A2 State (Fault Event):
             P2_B                                                   -- Transition from P3; After VR Enable Command
                                                                    -- All Switch Regulators are Off
                                                                    -- All LDOs are ON

                                                 P1                 -- PWR_GOOD Output = L
                                                                    -- VR_EN Input = L or H
                                                                    -- R32[7] = ‘0’

P0                                                                  P3 State (Regulation Mode or Bulk Link Monitor Mode)

                                                                    -- All Switch Regulators are On
                                                                    -- R32[7] = ‘1’
```

*Figure 29 — State Definition and Transitions* (figure; any text below/above was extracted from the drawing)

**Table 25 — State Transitions**

```text
                                                     Register Setting                                                         Power
Start                                                                                                     PWR_GOO
                   Activity                                                            End State                               Cycle      Note
State                                       R2F[2]   R32[5]    R1A[4]     R2E[4]                          D Output[1]
                                                                                                                             Required?
 P0     Valid VIN_Bulk                       N/A      N/A           N/A    N/A            P2_B              Low                 N/A
 P1     VR_EN; High to Low                    X        X             X      X                               N/A
        VR_EN Pin; Low to High                X        X             0      X                               N/A
                                              X        X             1      X              P3               Hi-Z         No
        VR_DIS CMD on I2C/I3C Bus             X        X             1      X              P1           No Change        N/A
        VR_EN CMD on I2C/I3C Bus              X        X             1      X              P1           No Change        N/A
        DVFSQ_n; High to Low                  X        X             X      X             Illegal for system; PMIC ignores it
        DVFSQ_n; Low to High                  X        X             X      X              P1           No Change        N/A
P2_B    VR_EN Pin Transition to High          X        0             X      X              P3               Hi-Z         N/A
                                              X        1             X      X                      Illegal Configuration                   2
        VR_EN CMD on Bus                      X        X             X      X              P3               Hi-Z         N/A
        DVFSQ_n; High to Low                  X        X             X      X             Illegal for system; PMIC ignores it
        DVFSQ_n; Low to High                  X        X             X      X             P2_B          No Change        N/A

                                             Register Setting                                          Power
Start                                                                                  PWR_GOO
                  Activity                                               End State                      Cycle     Note
State                               R2F[2]   R32[5]   R1A[4]    R2E[4]                 D Output[1]
                                                                                                      Required?
 P3     VR_EN Pin; High to Low        X        0        0         X        P2_A1           Low
                                      X        0        1         X         P1             Low
                                      X        1        X         X               Illegal Configuration            [2]

        VR_EN Pin; Low to High        X        X        X         X          P3            Hi-Z           N/A      [3]

        VR_DIS CMD on I2C/I3C Bus     1        X        0         X        P2_A1           Hi-Z
                                      1        X        1         X          P1            Hi-Z
                                      0        X        X         X          P3            Hi-Z           N/A
        VR_EN CMD on I2C/I3C Bus      X        X        X         X          P3            Hi-Z           N/A      [4]

        PWR_GOOD Input Low            X        0        X         X          P3            Hi-Z           N/A     [5],[6]

                                      1        1        X         X        P2_A1           Low                      6
                                      0        1        X         X        P2_A1           Low                      6
        Internal VR Disable Event     0        X        X         X        P2_A2           Low            Yes
                                      1        X        X         X        P2_A2           Low            No       [7]

        VIN_Bulk Invalid              X        X        X         X          P0            N/A            N/A
        DVFSQ_n High to Low           X        X        X         0             No Change                 N/A
                                      X        X        X         1       DVFSQ        No Change          N/A
        DVFSQ_n Low to High           X        X        X         X      No Change     No Change          N/A
P2_A1   VR_EN Pin; High to Low        X        X        X         X      No Change     No Change          N/A      [8]

        VR_EN Pin; Low to High        X        1        X         X               Illegal Configuration             2

                                      X        0        0         X          P3            Hi-Z           No
                                      X        0        1         X                        N/A                     [9]

        VR_DIS CMD on I2C/I3C Bus     X        X        X         X      No Change     No Change          N/A      [10]

        VR_EN CMD on I2C/I3C Bus      0        0        0         X      No Change     No Change          N/A

                                      0        1        X         X          P3            Hi-Z           No
                                      0        0        1         X         N/A            N/A            N/A
                                      1        X        0         X          P3            Hi-Z           No
                                      1        1        1         X          P3            Hi-Z           No
                                      1        0        1         X                        N/A                      8
        Internal VR Disable Event     0        X        X         X        P2_A2           Low            Yes
                                      1        X        X         X        P2_A2           Low            No      7,[11]

        VIN_Bulk Invalid              X        X        X         X          P0            N/A            N/A
        DVFSQ_n High to Low           X        X        X         X               Illegal Configuration
        DVFSQ_n Low to High           X        X        X         X        P2_A1       No Change          N/A
P2_A2   VR_EN Pin; High to Low        X        X        X         X      No Change     No Change          N/A      [12]

        VR_EN Pin; Low to High        0        X        X         X        P2_A2           Low            Yes
                                      1        0        0         X          P3            Hi-Z           No
                                      1        0        1         X          P3            Hi-Z           No
                                      1        1        X         X               Illegal Configuration             2
        VR_EN CMD on I2C/I3C Bus      0        X        X         X        P2_A2           Low            Yes
                                      1        X        0         X          P3            Hi-Z           No
                                      1        0        1         X          P3            Hi-Z           No
                                      1        1        1         X          P3            Hi-Z           No
        Internal VR Disable Event     0        X        X         X      No Change     No Change          Yes
                                      1        X        X         X      No Change     No Change          No      7,11
        VIN_Bulk Invalid              X        X        X         X          P0            N/A            N/A
        DVFSQ_n High to Low           X        X        X         X               Illegal Configuration
        DVFSQ_n Low to High           X        X        X         X        P2_A2       No Change          N/A

                                                        Register Setting                                                Power
  Start                                                                                                PWR_GOO
                       Activity                                                         End State                        Cycle        Note
  State                                       R2F[2]    R32[5]    R1A[4]     R2E[4]                    D Output[1]
                                                                                                                       Required?
           VR_EN Pin High to Low                 X         0         0          1         P2_A1            Low
                                                 X         0         1          1          P1              Low
                                                 X         1         X          X                Illegal Configuration                     2
           VR_EN Pin Low to High                 X         X         X          1         DVFSQ            Hi-Z           N/A              3
           VR_DIS CMD on I2C/I3C Bus             1         X         0          1         P2_A1            Hi-Z
                                                 1         X         1          1           P1             Hi-Z
                                                 0         X         X          1         DVFSQ            Hi-Z           N/A
           VR_EN CMD on I2C/I3C Bus              X         X         X          1         DVFSQ            Hi-Z           N/A           4
           PWR_GOOD Input Low                    X         0         X          1         DVFSQ            Hi-Z           N/A          5,6
 DVFSQ
                                                 1         1         X          1         P2_A1            Low                          6
                                                 0         1         X          1         P2_A1            Low                          6
           Internal VR Disable Event             0         X         X          1         P2_A2            Low            Yes
                                                 1         X         X          1         P2_A2            Low            No               7
           VIN_Bulk Invalid                      X         X         X          X           P0             N/A            N/A
           DVFSQ_n High to Low                   X         X         X          0              N/A; Illegal Configuration
                                                 X         X         X          1         DVFSQ        No Change                       [13]
           DVFSQ_n Low to High                   X         X         X          0              N/A; Illegal Configuration
                                                 X         X         X          1           P3         No Change
NOTE 1 This represents PMIC’s PWR_GOOD output signal; all power is good; no fault event.

NOTE 2 Simultaneous usage of VR_EN pin and PWR_GOOD IO type (Table 154, Register 0x32 [5] = ‘1’) is not allowed and considered an
        illegal configuration. If VR_EN pin is intended to be used to turn on or off output rails, PWR_GOOD signal must be configured as

        O only (i.e., Table 154, Register 0x32 [5] = ‘0’). VR_EN pin must be tied to GND if PWR_GOOD signal is intended to be configured
        as IO (Table 154, Register 0x32 [5] = ‘1’).

NOTE 3 PMIC is already in P3 state. It assumes PMIC entered in P3 state with VR_EN command on I2C/I3C bus.
NOTE 4 PMIC is already in P3 state. It assumes PMIC entered in P3 state with VR_EN pin transition to High.
NOTE 5 PMIC PWR_GOOD IO Type is configured as Output Only.
NOTE 6 PMIC’s input of PWR_GOOD is Low. But internally, PMIC’s PWR_GOOD output signal is Hi-Z.
NOTE 7 PMIC allows to re-enable output regulators with VR Enable command (either with VR_EN pin or on I2C/I3C bus) assuming that
        event is no longer present and status registers are cleared.
NOTE 8 PMIC is already in P2_A1 state and so VR_EN pin transition has no meaning.
NOTE 9 Since Table 130, Register 0x1A [4] = ‘1’, the PMIC never enters into P2_A1 state if there is no event, PMIC always enters in P1
        state.
NOTE 10 PMIC is already in P2_A1 state with VR_EN pin. So VR_DIS command on the bus has no effect.
NOTE 11 Power cycle is always required if there is a thermal shutdown regardless of the register Table 151, Register 0x2F [2] setting.
NOTE 12 PMIC is already in P2_A2 state and so VR_EN pin transition has no meaning.
NOTE 13 PMIC is already in DVFSQ state and hence DVFSQ_n pin transition high to low has no meaning.
```
