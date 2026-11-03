---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 2.10.12
title: I3C Basic Common Command Codes (CCC)
pages: 72-87
---
# 2.10.12 I3C Basic Common Command Codes (CCC)

The I3C Basic spec lists large number of Common Command Codes (CCC). Not all CCC are required to be supported. The PMIC device NACKs for all unsupported CCC. The PMIC supports CCC as listed in Table 54. The PMIC device requires STOP operation in between when switching from CCC operation to private device specific Write or Read or Default Read Address Pointer mode operation and vice versa. In other words, any CCC operation must be followed by STOP operation before continuing to any device specific Write or Read or Default Read Address Pointer mode operation. Similarly, any device specific Write or Read or Default Read Address Pointer mode operation must be followed by STOP operation before continuing to any CCC operation. The PMIC device also requires STOP operation between any direct CCC to broadcast CCC. The PMIC device does allow Repeat Start operation between any direct CCC to any other direct CCC or between any broadcast CCC to any other broadcast CCC or between any private Write or Read or Default Read Address Pointer mode operation to any other private Write or Read or Default Read Address Pointer mode operation.

**Table 54 — PMIC CCC Support Requirement**

```text
    CCC               Mode             Code                           Description                               Note
                   Broadcast           0x00       Enable Event Interrupts
   ENEC
                      Direct           0x80
                   Broadcast           0x01       Disable Event Interrupts
   DISEC
                      Direct           0x81

  RSTDAA           Broadcast           0x06       Put the device in I2C Mode (aka: Reset Dynamic
                                                  Address Assignment)
                                                  Put the device in I3C Basic Mode (aka: Set All
 SETAASA           Broadcast           0x29
                                                  Addresses to Static Address)
GETSTATUS             Direct           0x90       Get Device Status
  DEVCAP              Direct           0xE0       Get Device Capability                                           1
  SETHID           Broadcast           0x61       PMIC updates 3-bit HID field                                    1
 DEVCTRL           Broadcast           0x62       Configure SPD Hub and all devices behind Hub                    1
NOTE 1 JEDEC specific CCC.
```

## Subsections

- [2.10.12.1 ENEC CCC](2_10_12_1_ENEC_CCC.md)
- [2.10.12.2 DISEC CCC](2_10_12_2_DISEC_CCC.md)
- [2.10.12.3 RSTDAA CCC](2_10_12_3_RSTDAA_CCC.md)
- [2.10.12.4 SETAASA CCC](2_10_12_4_SETAASA_CCC.md)
- [2.10.12.5 GETSTATUS CCC](2_10_12_5_GETSTATUS_CCC.md)
- [2.10.12.6 DEVCAP CCC](2_10_12_6_DEVCAP_CCC.md)
- [2.10.12.8 DEVCTRL CCC](2_10_12_8_DEVCTRL_CCC.md)
