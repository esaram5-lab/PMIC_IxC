---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 3.1
title: Register Attribute Definition
pages: 102-103
---
# 3.1 Register Attribute Definition

All volatile registers have Base Attributes as defined in Table 89. Some register attributes are further modified with Attribute Modifiers, as defined in Table 90.

**Table 89 — Register Base Attributes**

```text
Attribute       Abbreviation                                        Description
Read Only       RO                This bit can be read by software. Writes have no effect.
Read/Write      RW                This bit can be read or written by host.
Write Only      W                 This bit can only be written by host. Read from this bit returns ‘0’.
Reserved        RV                This bit is reserved for future expansion and its value must not be
                                  modified by host. The bit will return ‘0’ when read. Write has no effect.
```

**Table 90 — Register Attribute Modifier**

```text
Attribute        Abbreviation                                       Description
Write ‘1’        1O                This bit can only be set (i.e., write ‘1’) but not reset (i.e., write ‘0’). Write
Only                               ‘0’ has no effect.

Protected        P                 This bit is protected by the password registers. This bit cannot be written
                                   to unless the password code has been written into the password registers.

Persistent       E                 This bit is persistent during power cycle.
```
