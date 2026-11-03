---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 3.3.5.2
title: Clear Registers
pages: 123-128
---
# 3.3.5.2 Clear Registers

For each Real Time Status Registers (Table 98, “Register 0x08” [7:0], Table 99, “Register 0x09” [7:0], Table 100, “Register 0x0A” [7:1], Table 101, “Register 0x0B” [7:0] and Table 141, “Register 0x33” [4:2]), the PMIC offers a way to clear the status of each event. The clear registers are Table 106, “Register 0x10” [7,5:0], Table 107, “Register 0x11” [7:0], Table 108, “Register 0x12” [7:2], Table 109, “Register 0x13” [7:0] and to Table 110, “Register 0x14” [4:2,0], respectively. All clear registers are Write ‘1’ only registers. When ‘1’ is written to any of the clear registers, the PMIC updates the status registers to default state and removes the interrupt condition on GSI_n and PWR_GOOD output signal assuming that event is no longer present. If the failing condition is still present, the status register will still remain at ‘1’. Note that GSI_n and PWR_GOOD interrupt is only applicable if that event is not masked. GSI_n output signal can be disabled.

When ‘1’ is written to any of the clear registers, there are three categories of response by the PMIC.

```text
1.  PMIC removes GSI_n interrupt (PWR_GOOD interrupt is not applicable. Related status registers are:
   Table 106, “Register 0x10” [1], Table 107, “Register 0x11” [7,4:0], Table 109, “Register 0x13” [7:4],
   Table 110, “Register 0x14” [4].
2. PMIC removes GSI_n and PWR_GOOD interrupt. Related status registers are: Table 106, “Register 0x10”
   [7,5:2], Table 107, “Register 0x11” [6:5], Table 110, “Register 0x14” [2].
3. PMIC only removes GSI_n interrupt and does not remove PWR_GOOD interrupt. Related status registers
   are: Table 106, “Register 0x10” [0], Table 108, “Register 0x12” [7:4], Table 109, “Register 0x13” [3:0],
   Table 110, “Register 0x14” [3]. The host is expected to either power cycle the PMIC or re-issue the
   VR Enable command if PMIC is in non write protect mode.
```

The PMIC offers a Global Clear command by writing ‘1’ to registers Table 110, “Register 0x14” [0]. This command works same way as individual clear command. This command can alternatively be used by the host if more than one clear command is required to different registers.

**Table 106 — Register 0x10**: see [`registers/0x10.md`](../registers/0x10.md)

**Table 107 — Register 0x11**: see [`registers/0x11.md`](../registers/0x11.md)

**Table 108 — Register 0x12**: see [`registers/0x12.md`](../registers/0x12.md)

**Table 109 — Register 0x13**: see [`registers/0x13.md`](../registers/0x13.md)

**Table 110 — Register 0x14**: see [`registers/0x14.md`](../registers/0x14.md)
