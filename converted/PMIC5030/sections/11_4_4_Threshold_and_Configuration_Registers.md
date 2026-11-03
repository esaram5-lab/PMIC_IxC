---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 11.4.4
title: Threshold and Configuration Registers
pages: 158-186
---
# 11.4.4 Threshold and Configuration Registers

**Table 131 — Register 0x1A**: see [`registers/0x1A.md`](../registers/0x1A.md)

**Table 132 — Register 0x1B**: see [`registers/0x1B.md`](../registers/0x1B.md)

**Table 133 — Register 0x1C**: see [`registers/0x1C.md`](../registers/0x1C.md)

**Table 134 — Register 0x1D**: see [`registers/0x1D.md`](../registers/0x1D.md)

**Table 135 — Register 0x1E**: see [`registers/0x1E.md`](../registers/0x1E.md)

**Table 136 — Register 0x1F**: see [`registers/0x1F.md`](../registers/0x1F.md)

**Table 137 — Register 0x20**: see [`registers/0x20.md`](../registers/0x20.md)

**Table 138 — Register 0x21**: see [`registers/0x21.md`](../registers/0x21.md)

**Table 139 — Register 0x22**: see [`registers/0x22.md`](../registers/0x22.md)

**Table 140 — Register 0x23**: see [`registers/0x23.md`](../registers/0x23.md)

**Table 141 — Register 0x24**: see [`registers/0x24.md`](../registers/0x24.md)

**Table 142 — Register 0x25**: see [`registers/0x25.md`](../registers/0x25.md)

**Table 143 — Register 0x26**: see [`registers/0x26.md`](../registers/0x26.md)

**Table 144 — Register 0x27**: see [`registers/0x27.md`](../registers/0x27.md)

**Table 145 — Register 0x28**: see [`registers/0x28.md`](../registers/0x28.md)

**Table 146 — Register 0x29**: see [`registers/0x29.md`](../registers/0x29.md)

**Table 147 — Register 0x2A**: see [`registers/0x2A.md`](../registers/0x2A.md)

**Table 148 — Register 0x2B**: see [`registers/0x2B.md`](../registers/0x2B.md)

**Table 149 — Register 0x2C**: see [`registers/0x2C.md`](../registers/0x2C.md)

**Table 150 — Register 0x2D**: see [`registers/0x2D.md`](../registers/0x2D.md)

**Table 151 — Register 0x2E**: see [`registers/0x2E.md`](../registers/0x2E.md)

**Table 152 — Register 0x2F**: see [`registers/0x2F.md`](../registers/0x2F.md)

**Table 153 — Register 0x30**: see [`registers/0x30.md`](../registers/0x30.md)

**Table 154 — Register 0x31**: see [`registers/0x31.md`](../registers/0x31.md)

**Table 155 — Register 0x32**: see [`registers/0x32.md`](../registers/0x32.md)

**Table 156 — PMIC Action for Register R32[7,5] Setting**

```text
R32[7,5]        If Output Regulators are On              If Output Regulators are Off
  00                 Execute VR Disable                              No Action

  01                 Execute VR Disable                              No Action

  10         No Action; Regulators remains On                Regulators remains Off

   11                      No Action                           Execute VR Enable
```

**Table 157 — Register 0x33**: see [`registers/0x33.md`](../registers/0x33.md)

**Table 158 — Register 0x34**: see [`registers/0x34.md`](../registers/0x34.md)

**Table 159 — Register 0x35**: see [`registers/0x35.md`](../registers/0x35.md)
