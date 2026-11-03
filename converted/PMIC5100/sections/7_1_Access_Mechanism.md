---
document: JESD301-2 (PMIC5100 Power Management IC Standard, Rev. 1.03, October 2022)
device: PMIC5100
application: client
section: 7.1
title: Access Mechanism
pages: 105-106
---
# 7.1 Access Mechanism



## 7.1.1 Register Attribute Definition

All volatile registers have Base Attributes as defined in Table 86. Some register attributes are further modified with Attribute Modifiers, as defined in Table 87.

**Table 86 — Register Base Attributes**

```text
Attribute      Abbreviation                                             Description
Read Only      RO             This bit can be read by host. Writes have no effect.
Read/Write     RW             This bit can be read or written by host.
Write Only     W              This bit can only be written by host. Read from this bit returns ‘0’.
Reserved       RV             This bit is reserved for future expansion and its value must not be modified by host. The
                              bit will return ‘0’ when read. Write has no effect.
```

**Table 87 — Register Attribute Modifier**

```text
Attribute      Abbreviation                                             Description
Write 1 Only   1O             This bit can only be set (i.e., write ‘1’) but not reset (i.e., write ‘0’). Write ‘0’ has no

                              effect.
Protected      P              This bit is protected by the password. This bit cannot be written to unless the password

                              code has been written into the password registers.
Persistent     E              This bit is persistent during power cycle.
```
