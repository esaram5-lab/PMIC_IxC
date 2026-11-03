---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 5.4.3
title: Default Read Address Pointer Mode
pages: 87-93
---
# 5.4.3 Default Read Address Pointer Mode

This mode works the same exact way as explained in clause 5.3.3. Table 56 and Table 57 show the read command data packet for PEC function disabled and enabled, respectively. When PEC function is enabled, Table 162, Register 0x3A [3:2] sets the number of bytes that PMIC sends out, followed by the PEC calculation. If PEC is enabled, the host must complete the burst length as indicated in Table 162, Register 0x3A [3:2] register. In other words, the host must not interrupt the burst length prematurely for Default Address Pointer Read operation.

**Table 56 — Read Command Data Packet with Address Pointer Mode; PEC Disabled**

```text
    Start          Bit 7        Bit 6     Bit 5     Bit 4       Bit 3    Bit 2     Bit 1      Bit 0      A/N/T          Stop
   S or Sr           1            X         0         X                   HID                 R=1         A/N[1]
                                                       Data                                                T=1
                                                          ...                                              T=1
                                                       Data                                             T=1[2],[3]    Sr[4] or P
NOTE 1 The PMIC device NACKs if there is a parity error in a previous transaction when host performs consecutive
       transactions with Repeat Start.
NOTE 2 See Figure 34 to see how Host ends target device operation.
NOTE 3 When device reaches last byte within the region (either Host region or CAMM2 Vendor region), it will continue to
       return data but returned data will be 0x00 if there is no valid password for CAMM2 Vendor region or Vendor Specific
       region. Once the address counter reaches 0x1FF, it will reset to address 0x00 and it will continue to return the data.
       Only host can perform the STOP operation.
NOTE 4 Repeat Start or Repeat Start with 7’h7E.
```

**Table 57 — Read Command Data Packet with Address Pointer Mode; PEC Enabled**

```text
    Start          Bit 7        Bit 6     Bit 5     Bit 4       Bit 3    Bit 2     Bit 1      Bit 0      A/N/T          Stop
   S or Sr           1            X         0         X                   HID                 R=1         A/N[1]

                                                       Data                                                T=1
                                                          ...                                              T=1

                                                       Data                                                T=1
                                                       PEC                                               T=0[2]       Sr[3] or P

NOTE 1 The PMIC device NACKs if there is a parity or PEC error in a previous transaction when host performs consecutive
       transactions with Repeat Start.
NOTE 2 See Figure 35 to see how Host ends target device operation followed by Host STOP operation.
NOTE 3 Repeat Start or Repeat Start with 7’h7E.
```

**Table 58 — Read CMD Data Packet with Address Pointer Mode and IBI Header; PEC Disabled**

```text
    Start          Bit 7        Bit 6     Bit 5     Bit 4       Bit 3    Bit 2     Bit 1      Bit 0      A/N/T          Stop
      S              1            1         1         1          1         1         0        W=0         A[1],2
     Sr              1            X         0         X                   HID                 R=1       A/N[2],[3]
                                                       Data                                                T=1
                                                          ...                                              T=1
                                                       Data                                             T=1[4],[5]    Sr[6] or P
NOTE 1 See Figure 31 to see how the transition occurs from Target Open Drain (ACK) to Host Push Pull operation (Repeat Start).
NOTE 2 The PMIC device NACKs if there is a parity error in a previous transaction when host performs consecutive
       transactions with Repeat Start.
NOTE 3 See Figure 33 to see how the transition occurs from Host Push Pull Operation to Target Open Drain (ACK).
NOTE 4 See Figure 34 to see how Host ends target device operation.
NOTE 5 When device reaches last byte within the region (either Host region or CAMM2 Vendor region), it will continue to
       return data but returned data will be 0x00 if there is no valid password for CAMM2 Vendor region or Vendor Specific
       region. Once the address counter reaches 0x1FF, it will reset to address 0x00 and it will continue to return the data.
       Only host can perform the STOP operation.
NOTE 6 Repeat Start or Repeat Start with 7’h7E.
```

**Table 59 — Read Command Data Packet with Address Pointer Mode and IBI Header; PEC Enabled**

```text
    Start             Bit 7          Bit 6         Bit 5        Bit 4         Bit 3      Bit 2       Bit 1         Bit 0             A/N/T               Stop
      S                1               1             1              1          1          1             0          W=0                A[1],2
     Sr                1               X             0              X                    HID                       R=1              A/N[2],[3]
                                                                    Data                                                              T=1
                                                                        ...                                                           T=1
                                                                    Data                                                              T=1
                                                                    PEC                                                              T=0[4]            Sr[5] or P
NOTE 1 See Figure 31 to see how the transition occurs from Target Open Drain (ACK) to Host Push Pull operation (Repeat Start).
NOTE 2 The PMIC device NACKs if there is a parity or PEC error in a previous transaction when host performs consecutive
       transactions with Repeat Start.
NOTE 3 See Figure 33 to see how the transition occurs from Host Push Pull Operation to Target Open Drain (ACK).
NOTE 4 See Figure 35 to see how Host ends target device operation followed by Host STOP operation.
NOTE 5 Repeat Start or Repeat Start with 7’h7E.
                                    tDOUT                tDOFFT

               HSCL

                   VIHmin
                   VILmax

                                                  ACK
            HSDA                                                                                      Bit 7                                    Bit 6

                   Target Drives SDA Bus                                                    Controller Drives SDA Bus – Push Pull
                       – Open Drain

                                            Target Drives SDA Bus
                                                – Open Drain

                                               Both Controller & Target Drives SDA Bus
                                                       Overlap – Open Drain
```

*Figure 31 — Target Open Drain (ACK) to Controller Push Pull Hand Off Operation* (figure; any text below/above was extracted from the drawing)

```text
                          tDOUT                 tDOFFC

  HSCL
         VIHmin
         VILmax

                                         ACK
HSDA                                                                                    Bit 7                     Bit 6

       Controller Drives SDA Bus                                              Target Drives SDA Bus – Push Pull
             – Open Drain

                                   Target Drives SDA Bus
                                       – Open Drain

                                   Both Controller & Target Drives SDA Bus

                                           Overlap – Open Drain
```

*Figure 32 — Controller Open Drain (ACK) to Target Push Pull Hand Off Operation* (figure; any text below/above was extracted from the drawing)

```text
                                                              tDOFFC                tDOFFT

         VIHmin
 HSCL
         VILmax

                                                                             ACK
HSDA    Bit 1                 Bit 0; W=0                                                                                           Bit 7          Bit 6

                                                                                                               Controller Drives SDA Bus – Push
                           Controller Drives SDA Bus
                                                                                                                              Pull
                                  – Push Pull

                                                                       Target drives SDA Bus
                                                                            Open Drain

                                                       Both Controller & Target
                                                           Drives SDA Bus       Both Controller & Target Drives SDA Bus

                                                                                        Overlap – Open Drain

                                                              tDOFFC
                                                                                               tHIGH_OD
                                                                       tLOW_OD

         VIHmin
 HSCL
         VILmax

                                                                             ACK
HSDA    Bit 1                 Bit 0; R=1                                                                                           Bit 7          Bit 6

                       Controller Drives SDA Bus
                              – Push Pull
                                                                                                          Target drives SDA Bus
                                                                                                                Push Pull

                                                       Both Controller & Target
                                                           Drives SDA Bus
```

*Figure 33 — Controller Push Pull to Target Open Drain Hand Off Operation* (figure; any text below/above was extracted from the drawing)

```text
                          tDOUT              tDOFFT

                                                                   Repeat
                                                                                                        STOP
                                                                    Start
  HSCL
       VIHmin
       VILmax

                                                       tCL_r_Dat_f

HSDA                                  T=1

                  Target Drives SDA Bus                                     Controller Drives SDA Bus

                                            Controller Pullup Resistor

                                              Keeps SDA Bus High
```

*Figure 34 — T=1; Controller Ends Read with Repeated START and STOP Waveform* (figure; any text below/above was extracted from the drawing)

```text
                       tDOUT                 tDOFFT

                                                                                             STOP

   HSCL
  VIHmin
  VILmax

                                       T=0
HSDA

               Target Drives SDA Bus                             Controller Drives SDA Bus

                               Both Controller & Target Drives SDA Bus

                                               Overlap
```

*Figure 35 — T=0; Target Ends Read; Controller Generates STOP* (figure; any text below/above was extracted from the drawing)
