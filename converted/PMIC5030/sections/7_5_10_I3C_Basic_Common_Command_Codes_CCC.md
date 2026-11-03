---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 7.5.10
title: I3C Basic Common Command Codes (CCC)
pages: 96-111
---
# 7.5.10 I3C Basic Common Command Codes (CCC)

The I3C Basic spec lists large number of Common Command Codes (CCC). Not all CCC are required to be supported. The PMIC device NACKs for all unsupported CCC. The PMIC supports CCC as listed in

Table 68. The PMIC device requires STOP operation in between when switching from CCC operation to private device specific Write or Read or Default Read Address Pointer mode operation and vice versa. In other words, any CCC operation must be followed by STOP operation before continuing to any device specific Write or Read or Default Read Address Pointer mode operation. Similarly, any device specific Write or Read or Default Read Address Pointer mode operation must be followed by STOP operation before continuing to any CCC operation. The PMIC device also requires STOP operation between any direct CCC to broadcast CCC. The PMIC device does allow Repeat Start operation between any direct CCC to any other direct CCC or between any broadcast CCC to any other broadcast CCC or between any private Write or Read or Default Read Address Pointer mode operation to any other private Write or Read or Default Read Address Pointer mode operation.

**Table 68 — PMIC CCC Support Requirement**

```text
   CCC               Mode             Code                             Description                             Note

  ENEC           Broadcast            0x00                        Enable Event Interrupts

                     Direct           0x80

  DISEC          Broadcast            0x01                        Disable Event Interrupts

                     Direct           0x81

 RSTDAA          Broadcast            0x06           Put the device in I2C Mode (aka: Reset Dynamic
                                                                  Address Assignment)

 SETAASA         Broadcast            0x29            Put the device in I3C Basic Mode (aka: Set All
                                                               Addresses to Static Address)

GETSTATUS            Direct           0x90                           Get Device Status

 DEVCAP              Direct           0xE0                         Get Device Capability                        [1]

 SETHID          Broadcast            0x61                      PMIC updates 3-bit HID field                    1

DEVCTRL          Broadcast            0x62           Configure SPD Hub and all devices behind Hub               1
NOTE 1     JEDEC-specific CCC.
```

## Subsections

- [7.5.10.1 ENEC CCC](7_5_10_1_ENEC_CCC.md)
- [7.5.10.2 DISEC CCC](7_5_10_2_DISEC_CCC.md)
- [7.5.10.3 RSTDAA CCC](7_5_10_3_RSTDAA_CCC.md)
- [7.5.10.4 SETAASA CCC](7_5_10_4_SETAASA_CCC.md)
- [7.5.10.5 GETSTATUS CCC](7_5_10_5_GETSTATUS_CCC.md)
- [7.5.10.6 DEVCAP CCC](7_5_10_6_DEVCAP_CCC.md)
- [7.5.10.7 SETHID CCC](7_5_10_7_SETHID_CCC.md)
- [7.5.10.8 DEVCTRL CCC](7_5_10_8_DEVCTRL_CCC.md)
