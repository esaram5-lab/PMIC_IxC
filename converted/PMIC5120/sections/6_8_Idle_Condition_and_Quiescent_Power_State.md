---
document: JESD301-6 (PMIC5120 Power Management IC Standard, Version 1.0, February 2025)
device: PMIC5120
application: client
section: 6.8
title: Idle Condition and Quiescent Power State
pages: 53-56
---
# 6.8 Idle Condition and Quiescent Power State

Quiescent Power State definition: All circuits including PMIC switch output and LDO output regulators are off. VR_EN signal is at static low or high level. I2C or I3C Basic interface access is not allowed and is pulled high. PID signal is at static low or high level. This state is only applicable if Table 122, Register 0x1A [4] = ‘1’. This state is labeled as P1 state in Figure 33.

Idle Condition definition: All circuits including PMIC switch output and LDO output regulators are on with 0 A load. VR_EN signal is at static low or high level. I2C or I3C Basic interface access is allowed but bus is pulled high. PID signal is at static low or high level.

Figure 33 shows high level PMIC states and its definition. The state transitions from each state is defined in Table 29.

```text
                                                     P0 State:
                                                     -- VIN_Bulk invalid

                                                     P1 State:
                    Non-Event        Event
                                                     -- R1A[4] = ‘1’
                                                     -- Entry from P3 State Only

                     P2_A1          P2_A2            P2_B State:
                                                     -- Transition from P0 or P1 State; Before VR Enable Command
                                                     -- All Switch Regulators are Off
                                                     -- All LDOs are on
                                                     -- PWR_GOOD Output = L
                                                     -- VR_EN Input = L
                                                     -- R32[7] = ‘0’

                                                     P2_A1 State (No Fault Event):
                       P3
     VR_EN Pin                                       -- Transition from P3; After VR Enable Command
     goes High                                       -- All Switch Regulators are Off
                                                     -- All LDOs are on
                                                     -- PWR_GOOD Output = L or H
                                                     -- VR_EN Input = L or H
                    VR_EN CMD                        -- R32[7] = ‘0’
                      On Bus
            P2_B                                     P2_A2 State (Fault Event):
                                                     -- Transition from P3; After VR Enable Command
                                               ng    -- All Switch Regulators are Off
                                    P1
                                                     -- All LDOs are ON
                                (Quiescent)
                                                     -- PWR_GOOD Output = L

                                                     -- VR_EN Input = L or H
                                                     -- R32[7] = ‘0’
P0
                                                     P3 State (Regulation Mode or Bulk Link Monitor Mode)

                                                     -- All Switch Regulators are On
                                                     -- R32[7] = ‘1’
```

*Figure 33 — State Definition and Transitions* (figure; any text below/above was extracted from the drawing)

**Table 29 — State Transitions**

```text
                                                Register Setting                PWR_GOO     Power
Start State            Activity                                     End State                Cycle       Note
                                             R2F[2] R32[5] R1A[4]                D Output1 Required?
      P0           Valid VIN_Bulk             N/A     N/A     N/A     P2_B          Low           N/A
                 VR_EN; High to Low            X       X       X                     N/A
                                               X       X       0                     N/A
                VR_EN Pin; Low to High
      P1                                       X       X       1        P3         Hi-Z           No
                               2C/I3C Bus      X       X       1        P1       No Change        N/A
              VR_DIS CMD on I
              VR_EN CMD on I2C/I3C Bus         X       X       1        P1      No Change         N/A
                                               X       0       X        P3          Hi-Z          N/A
              VR_EN Pin Transition to High                                                                2
     P2_B                                      X       1       X            Illegal Configuration
                  VR_EN CMD on Bus             X       X       X        P3          Hi-Z          N/A
                                               X       0       0      P2_A1         Low
                VR_EN Pin; High to Low         X       0       1        P1          Low
                                               X       1       X            Illegal Configuration          2

                VR_EN Pin; Low to High         X       X       X        P3          Hi-Z          N/A     3

                                               1       X       0      P2_A1         Hi-Z
              VR_DIS CMD on I2C/I3C Bus        1       X       1        P1          Hi-Z
                                               0       X       X        P3          Hi-Z          N/A
      P3
              VR_EN CMD on I2C/I3C Bus         X       X       X        P3          Hi-Z          N/A     4

                                               X       0       X        P3          Hi-Z          N/A     5,6

                PWR_GOOD Input Low             1       1       X     P2_A1          Low                    6

                                               0       1       X     P2_A1          Low                    6

                                               0       X       X     P2_A2          Low           Yes

               Internal VR Disable Event                                                                  7
                                               1       X       X     P2_A2          Low           No
                  VIN_Bulk Invalid             X       X       X       P0           N/A           N/A
                VR_EN Pin; High to Low         X       X       X    No Change    No Change        N/A     8

                                               X       1       X              Illegal Configuration        2

                VR_EN Pin; Low to High         X       0       0        P3            Hi-Z          No
                                               X       0       1                       N/A                9

              VR_DIS CMD on I2C/I3C Bus        X       X       X    No Change    No Change        N/A     10

                                               0       0       0    No Change    No Change        N/A
     P2_A1                                     0       1       X       P3          Hi-Z           No
                                               0       0       1       N/A          N/A           N/A
              VR_EN CMD on I2C/I3C Bus         1       X       0       P3          Hi-Z           No
                                               1       1       1       P3          Hi-Z           No
                                               1       0       1                     N/A                   7

                                               0       X       X      P2_A2         Low           Yes
               Internal VR Disable Event                                                                 7,11
                                               1       X       X      P2_A2         Low           No
                   VIN_Bulk Invalid            X       X       X        P0          N/A           N/A

                                                Register Setting                   PWR_GOO     Power
Start State             Activity                                       End State                Cycle             Note
                                            R2F[2] R32[5] R1A[4]                    D Output1 Required?

                VR_EN Pin; High to Low         X       X        X      No Change No Change             N/A          12

                                               0       X        X       P2_A2          Low             Yes
                                               1       0        0         P3           Hi-Z            No
                VR_EN Pin; Low to High
                                               1       0        1         P3           Hi-Z            No
                                               1       1        X              Illegal Configuration                2

   P2_A2                                       0       X        X       P2_A2          Low             Yes
                                               1       X        0         P3           Hi-Z            No
              VR_EN CMD on I2C/I3C Bus
                                               1       0        1         P3           Hi-Z            No
                                               1       1        1         P3           Hi-Z            No
                                               0       X        X      No Change No Change             Yes
               Internal VR Disable Event
                                               1       X        X      No Change No Change             No          7,11
                   VIN_Bulk Invalid            X       X        X         P0           N/A             N/A
NOTE 1  This represents PMIC’s PWR_GOOD output signal; all power is good; no fault event.
NOTE 2  Simultaneous usage of VR_EN pin and PWR_GOOD IO type (Table 146, Register 0x32 [5] = ‘1’) is not allowed and
        considered an illegal configuration. If VR_EN pin is intended to be used to turn on or off output rails, PWR_GOOD
        signal must be configured as O only (i.e., Table 146, Register 0x32 [5] = ‘0’). VR_EN pin must be tied to GND if
        PWR_GOOD signal is intended to be configured as IO (Table 146, Register 0x32 [5] = ‘1’).
NOTE 3 PMIC is already in P3 state. It assumes PMIC entered in P3 state with VR_EN command on I2C/I3C bus.
NOTE 4 PMIC is already in P3 state. It assumes PMIC entered in P3 state with VR_EN pin transition to High.
NOTE 5 PMIC PWR_GOOD IO Type is configured as Output Only.
NOTE 6 PMIC’s input of PWR_GOOD is Low. But internally, PMIC’s PWR_GOOD output signal is Hi-Z.
NOTE 7 PMIC allows to re-enable output regulators with VR Enable command (either with VR_EN pin or on I2C/I3C bus)

        assuming that event is no longer present and status registers are cleared.
NOTE 8 PMIC is already in P2_A1 state and so VR_EN pin transition has no meaning.

NOTE 9 Since Table 122, Register 0x1A [4] = ‘1’, the PMIC never enters into P2_A1 state if there is no event, PMIC always
        enters in P1 state.

NOTE 10 PMIC is already in P2_A1 state with VR_EN pin. So VR_DIS command on the bus has no effect.
NOTE 11 Power cycle is always required if there is a thermal shutdown regardless of the register Table 143, Register 0x2F
        [2] setting.
NOTE 12 PMIC is already in P2_A2 state and so VR_EN pin transition has no meaning.
```
