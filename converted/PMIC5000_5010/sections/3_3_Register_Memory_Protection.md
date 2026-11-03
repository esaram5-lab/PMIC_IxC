---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 3.3
title: Register Memory Protection
pages: 103-191
---
# 3.3 Register Memory Protection

The PMIC DIMM vendors registers (0x40 - 0x6F) are password protected registers. Both Read and Write access to DIMM vendor registers are blocked unless it is unlocked by providing the correct password. The default password for

DIMM vendor registers is 0x9473. The PMIC offers DIMM vendors to select their own password for DIMM vendor registers.

## Subsections

- [3.3.1 Steps to Access DIMM Vendor Region Registers](3_3_1_Steps_to_Access_DIMM_Vendor_Region_Registers.md)
- [3.3.2 Steps to Change DIMM Vendor Region Password](3_3_2_Steps_to_Change_DIMM_Vendor_Region_Password.md)
- [3.3.3 Steps to Burn or Program DIMM Vendor Region Registers](3_3_3_Steps_to_Burn_or_Program_DIMM_Vendor_Region_Regist.md)
- [3.3.4 Host Region Register Map](3_3_4_Host_Region_Register_Map.md)
- [3.3.5 Host Region Registers](3_3_5_Host_Region_Registers.md)
- [3.3.6 DIMM Vendor Region Registers](3_3_6_DIMM_Vendor_Region_Registers.md)
