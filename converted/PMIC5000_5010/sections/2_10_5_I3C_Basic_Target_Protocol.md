---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 2.10.5
title: I3C Basic Target Protocol
pages: 49-62
---
# 2.10.5 I3C Basic Target Protocol

The PMIC device operate on a standard I3C Basic serial interface. Transactions where the PMIC device is the targeted target device begin with the Host issuing a START condition followed by a 7-bit PMIC device address then a read or write bit, RW. All data are transmitted with the most significant bit MSB first. During the address followed by R/W bit transmission, the PMIC device typically replies with an ACK unless there are exceptional conditions when it may passively assert a NACK. See Table 35. The “T” bit carries Parity information from the Host for each byte. The PMIC device host region registers that are write protected in write protect mode of operation, the PMIC does not execute the operation internally. Similarly, regardless of write protect mode or non write protect mode of operation, without the correct password, all DIMM vendor and vendor specific region registers are write protected and PMIC does not execute the operation internally. The Packet Error Code (PEC) function is disabled by default when the PMIC device is put in I3C Basic mode. The host may optionally enable this function through Table 142, “Register 0x34” [7] or DEVCTRL CCC. If enabled, the PEC is appended at the end of all transactions. If PEC is enabled, the host must complete the burst length as indicated in CMD field. In other words, the host must not interrupt the burst length prematurely for Write operation.

## Subsections

- [2.10.5.1 Write Operation - Data Packet](2_10_5_1_Write_Operation_Data_Packet.md)
- [2.10.5.2 Read Operation - Data Packet](2_10_5_2_Read_Operation_Data_Packet.md)
- [2.10.5.3 Default Read Address Pointer Mode](2_10_5_3_Default_Read_Address_Pointer_Mode.md)
