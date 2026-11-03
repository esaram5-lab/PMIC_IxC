---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 2.13
title: Application Notes
pages: 100-102
---
# 2.13 Application Notes

2.13.1 Method to Identify and Map Out DIMM with a PMIC Fault in Shared CAMP

```text
Topology
```

Typical DDR5 server platform may have up to 32 DDR5 DIMM sockets. Server platform implementation may vary however it is possible to have up to 8 DDR5 DIMMs may share CAMP signal. The exact number of DDR5 DIMMs that share CAMP signal is beyond the scope of this application note. It is assumed that CAMP signal is pulled up on the platform or on the controller via 1K Ohm pullup resistor to either 3.3 V or 1.8 V. In a DDR5 server platform, it is possible that one or more DDR5 DIMM may have encountered a PMIC fault, as listed below, that has generated VR Disable event. Also refer to Table 27.

```text
• SWx Over Voltage
• SWx Under Voltage
• VIN_Bulk Over Voltage
• VIN_Bulk Under Voltage
• Critical Temperature
```

In this environment, it is desired to let the platform continue to power up and that faulty PMIC does not interfere with the platform operation. This application note describes a BIOS or appropriate software method to identify the faulty PMIC/DDR5 DIMM and then to map out the faulty PMIC/DDR5 DIMM from the memory subsystem. The fault scenario noted here is one example of fault scenario. Note that initial failure may occur during operation, hence BIOS needs to determine and log fault condition and then execute the map out routine.

Faulty PMIC Identification:

```text
1. Power up the platform (i.e., DDR5 DIMMs) by applying VIN_Bulk and VIN_Mgmt input supplies.
2. Broadcast VR Enable command to all PMICs.
3.   If all PMICs power up the their regulators successfully, all PMICs float the CAMP signal and the pullup
     resistor pulls the CAMP signal high indicating that all PMICs (i.e., DDR5 DIMMs) have powered up
     successfully.
4. However, if one or more PMIC fails to power up their regulators then that PMIC continues to hold the CAMP
   signal low while other PMICs that do power up their regulators successfully floats the CAMP signal. The net
   effect is CAMP signal remains low.
5.    BIOS eventually times out as the CAMP signal is not pulled up high and interrogates all PMIC’s status
     registers one at a time. The interrogation process of PMIC status registers allows BIOS to identify which
     PMICs regulators are successfully powered up and which PMICs are faulty.
```

Once BIOS identifies faulty PMIC, BIOS stores the faulty PMIC (DDR5 DIMM) identification in its non-volatile memory.Isolating and Securing Faulted PMIC:

```text
1. Once the faulty PMIC is identified, the platform may re-cycle the power by simultaneously removing
   VIN_Bulk and VIN_Mgmt input supply and then re-applying VIN_Bulk and VIN_Mgmt input supplies.
   This puts PMIC in configuration mode,
         a.   The BIOS reads PMIC error log registers to determine ‘bad’ PMIC. The BIOS also has a prior
              knowledge of a faulty PMIC.
2. BIOS performs following steps to the faulty PMIC.

         a.   Write R32 = 0x08 (Floats CAMP signal; prevents PMIC interference)

         b.   Ensure R2F[2] = ‘0’.

3. Broadcast VR Enable command to all PMICs.
4. All good PMIC executes Power On Sequence and floats the CAMP signal. The faulty PMIC is already
   floating the CAMP signal and does not execute Power On Sequence.
5. At this point, BIOS sees CAMP signal is pulled High and moves to the next operation.
6. By the above process, the faulty PMIC is mapped out of the memory system in a secure state and it does not
   interfere with platform operation. The good PMICs allow server system to power up normally and operate in
   a secure state.
```
