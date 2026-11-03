---
document: JESD301-6 (PMIC5120 Power Management IC Standard, Version 1.0, February 2025)
device: PMIC5120
application: client
section: 6.19
title: Application Notes
pages: 109-111
---
# 6.19 Application Notes



## 6.19.1 Error Injection Test Methodology

The PMIC error injection feature can be used many ways to test the PMIC at either component level or at the module level or at the system level. The error injection feature can be used to debug the PMIC component itself or to simulate the DIMM module behavior in a standalone ATE environment or in the system environment or to develop/simulate the system software to ensure PMIC and DIMM component hardware and system software works in a harmonious way if there is an actual fault event in the system.

The combination matrix to test each type of error injection is very large and it is the responsibility of the PMIC provider to ensure that all combinations are tested. The PMIC component specification does not provide the list in entirety but rather provides one possible general test method for error injection feature.

At all time, the PMIC specification must be followed. The test methodology does not alter or change the meaning of the PMIC specification. The test methodology may add, remove or modify steps in any sequence as long as the PMIC component specification is followed. The test results will vary depending on the starting condition and the sequence of steps. It is the responsibility of PMIC component provider to ensure results are checked against the specific condition and sequence while following the PMIC component specification.

One example of Error injection test after VR Enable command:

```text
1. Power cycle the PMIC; Issue R39 = 0x74 command; observe PWR_GOOD and GSI_n signal.
2. Read the PMIC registers R04 to R0B & R33 (checks all memory and status registers are cleared).
3. Issue the VR Enable command; read the PMIC registers R04 to R0B & R33 (check PMIC successfully
    turned on the rails without any fault); observe PWR_GOOD and GSI_n signal.
4. Inject error via R35 and select desired error type.
5. Check PMIC regulators are turned off; read the PMIC registers R04 to R0B & R33 (Check appropriate
    error log and status registers are set); observe PWR_GOOD and GSI_n signal.
6. Power cycle the PMIC.
7. Read the PMIC registers R04 to R07 (checks all memory).
8. Issue R39 = 0x74 command.
9. Read the PMIC registers R04 to R0B & R33.
10. Repeat another error injection test starting step # 3.
```
