---
document: JESD301-6 (PMIC5120 Power Management IC Standard, Version 1.0, February 2025)
device: PMIC5120
application: client
section: 7.2.2
title: Memory Protection
pages: 112-112
---
# 7.2.2 Memory Protection

The PMIC DIMM vendors registers (0x40 - 0x6F) are password protected registers. Both Read and Write access to

DIMM vendor registers are blocked unless it is unlocked by providing the correct password. The default password for DIMM vendor register is 0x9473. The PMIC offers each DIMM vendors to select their own password for DIMM vendor registers.
