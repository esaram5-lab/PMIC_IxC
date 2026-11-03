---
document: JESD301-2 (PMIC5100 Power Management IC Standard, Rev. 1.03, October 2022)
device: PMIC5100
application: client
section: 7.2.2
title: Memory Protection
pages: 106-106
---
# 7.2.2 Memory Protection

The PMIC DIMM vendors registers (0x40 - 0x6F) are password protected registers. Both Read and Write access to DIMM vendor registers are blocked unless it is unlocked by providing the correct password. The default password for DIMM vendor register is 0x9473. The PMIC offers each DIMM vendors to select their own password for DIMM vendor registers.
