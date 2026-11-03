---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 10
title: Application Notes
pages: 120-122
---
# 10 Application Notes



## 10.1 Identify and Map Out DIMM with a PMIC Fault in a Shared CAMP Topology

```text
Topology
```

Typical DDR5 server platform may have up to 32 DDR5 DIMM sockets. Server platform implementation may vary however it is possible to have up to 8 DDR5 DIMMs may share CAMP signal. The exact number of DDR5 DIMMs that share CAMP signal is beyond the scope of this application note. It is assumed that CAMP signal is pulled up on the platform or on the controller via 1K Ohm pullup resistor to either 3.3 V or 1.8 V. In a DDR5 server platform, it is possible that one or more DDR5 DIMM may have encountered a PMIC fault, as listed below, that has generated VR Disable event. Also refer to Table 27.

```text
▪ SWx Over Voltage
▪ SWx Under Voltage
▪ VIN_Bulk Over Voltage
▪ VIN_Bulk Under Voltage
▪ Critical Temperature
```

In this environment, it is desired to let the platform continue to power up and that faulty PMIC does not interfere with the platform operation. This application note describes a BIOS or appropriate software method to identify the faulty PMIC/DDR5 DIMM and then to map out the faulty PMIC/DDR5 DIMM from the memory subsystem. The fault scenario noted here is one example of fault scenario. Note that initial failure may occur during operation, hence BIOS needs to determine and log fault condition and then execute the map out routine.

Faulty PMIC Identification:

1. Power up the platform (i.e., DDR5 DIMMs) by applying VIN_Bulk and VIN_Mgmt input supplies.

2. Broadcast VR Enable command to all PMICs.

3. If all PMICs power up the their regulators successfully, all PMICs float the CAMP signal and the pullup resistor pulls the CAMP signal high indicating that all PMICs (i.e., DDR5 DIMMs) have powered up successfully.

4. However, if one or more PMIC fails to power up their regulators then that PMIC continues to hold the CAMP signal low while other PMICs that do power up their regulators successfully floats the CAMP signal. The net effect is CAMP signal remains low.

5. BIOS eventually times out as the CAMP signal is not pulled up high and interrogates all PMIC’s status registers one at a time. The interrogation process of PMIC status registers allows BIOS to identify which PMICs regulators are successfully powered up and which PMICs are faulty. Once BIOS identifies faulty PMIC, BIOS stores the faulty PMIC (DDR5 DIMM) identification in its non-volatile memory Isolating and Securing Faulted PMIC:

```text
10.1    Identify and Map Out DIMM with a PMIC Fault in a Shared CAMP Topology
        (cont’d)
```

1. Once the faulty PMIC is identified, the platform may re-cycle the power by simultaneously removing VIN_Bulk and VIN_Mgmt input supplies and then re-applying VIN_Bulk and VIN_Mgmt input supplies. This puts PMIC in configuration mode, a. The BIOS reads PMIC error log registers to determine ‘bad’ PMIC. The BIOS also has a prior

```text
knowledge of a faulty PMIC.
```

2. BIOS performs following steps to the faulty PMIC. a. Write R32 = 0x08 (Floats CAMP signal; prevents PMIC interference by writing R32[5] = ‘0’) b. Ensure R2F[2] = ‘0’.

3. Broadcast VR Enable command to all PMICs.

4. All good PMIC executes Power On Sequence and floats the CAMP signal. The faulty PMIC is already floating the CAMP signal and does not execute Power On Sequence.

5. At this point, BIOS sees CAMP signal is pulled High and moves to the next operation.

6. By the above process, the faulty PMIC is mapped out of the memory system in a secure state and it does not interfere with platform operation. The good PMICs allow server system to power up normally and operate in a secure state.

## 10.2 Error Injection Test Methodology

The PMIC error injection feature can be used many ways to test the PMIC at either component level or at the module level or at the system level. The error injection feature can be used to debug the PMIC component itself or to simulate the DIMM module behavior in a standalone ATE environment or in the system environment or to develop/simulate the system software to ensure PMIC and DIMM component hardware and system software works in a harmonious way if there is an actual fault event in the system.

The combination matrix to test each type of error injection is very large and it is the responsibility of the PMIC provider to ensure that all combinations are tested. The PMIC component specification does not provide the list in entirety but rather provides one possible general test method for error injection feature. At all times, the PMIC specification must be followed. The test methodology does not alter or change the meaning of the PMIC specification. The test methodology may add, remove or modify steps in any sequence as long as the PMIC component specification is followed. The test results will vary depending on the starting condition and the sequence of steps. It is the responsibility of PMIC component provider to ensure results are checked against the specific condition and sequence while following the PMIC component specification. One example of Error injection test after VR Enable command:

1. Power cycle the PMIC; Issue R39 = 0x74 command; observe CAMP and GSI_n signal.

2. Read the PMIC registers R04 to R0B, R33, R108 to R10A (checks all memory and status registers are

```text
cleared).
```

3. Issue the VR Enable command; read the PMIC registers R04 to R0B and R33 (check PMIC successfully

```text
turned on the rails without any fault); observe CAMP and GSI_n signal.
```

4. Inject error via R35, R12F and select desired error type.

5. Check PMIC regulators are turned off; read the PMIC registers R04 to R0B, R33, R108 to R10A (Check

```text
appropriate error log and status registers are set); observe CAMP and GSI_n signal.
```

6. Power cycle the PMIC.

7. Read the PMIC registers R04 to R07 (checks all memory).

8. Issue R39 = 0x74 command.

9. Read the PMIC registers R04 to R0B, R33, R108 to R10A.

10. Repeat another error injection test starting step # 3.
