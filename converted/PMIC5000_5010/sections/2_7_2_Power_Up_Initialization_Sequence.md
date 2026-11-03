---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 2.7.2
title: Power Up Initialization Sequence
pages: 23-25
---
# 2.7.2 Power Up Initialization Sequence

During power on, the host shall:

```text
1. Ramp up VIN_Mgmt supply; Ramp up VIN_Bulk supply; (No timing relationship between two supplies)
2. Hold VIN_Mgmt supply stable for a minimum of tVIN_Mgmt_to_Enable time
3. Hold VIN_Bulk supply stable for a minimum of tVIN_Bulk_to_Enable time
4. Query the status of the PMIC status register to determine if it is safe to enable VR.
5. If it is safe to enable, send VR Enable command by setting register Table 140, “Register 0x32” [7] = ‘1’ or by
    issuing DEVCTRL CCC.
```

Once the VIN_Mgmt supply is valid and stable, the PMIC shall drive VOUT_1.8V and VOUT_1.0V supply within t1.8 _Ready and t1.0V_Ready time. The PMIC shall enable I2C/I3C Basic bus interface function within tManagement_Ready. The host shall not attempt to access the PMIC’s memory registers until tManagement_Ready timing requirement is satisfied. Further the host shall not attempt to issue VR Enable command until tVIN_Mgmt_to_Enable and tVIN_Bulk_to_Enable timing requirement is satisfied. In Figure 11, the PMIC allows access to its memory registers for indefinite period of time as long as VIN_Mgmt input supply is valid and PMIC does not require VIN_Bulk input supply. The host may read PMIC's own internal memory content prior to ramping VIN_Bulk supply. The host, prior to issuing VR Enable command, must keep VIN_Mgmt input supply valid as long as VOUT_1.8V and VOUT_1.0V LDO output are required. If VIN_Mgmt input supply is removed or drops below 2.8 V, the PMIC does not guarantee any operation including VOUT_1.8V and VOUT_1.0V LDO output as well as access to its I2C/ I3C Basic interface regardless of VIN_Bulk input supply status. After host issues VR Enable command to the PMIC, the PMIC offers the input supply switchover function. The PMIC has an automatic internal input supply switchover function from VIN_Mgmt input supply to VIN_Bulk input supply. The PMIC triggers the switchover to VIN_Bulk input supply when VIN_Mgmt input supply drops below the threshold set in register Table 137, “Register 0x2F” [7]. The internal input supply switchover is for PMIC’s VOUT_1.8V and VOUT_1.0V LDO output. The PMIC’s I2C/I3C Basic interfaces (SCL/SDA) are kept alive when PMIC switches over to VIN_Bulk input supply. Figure 13 shows automatic internal switchover function when VIN_Mgmt input supply drops below the threshold while maintaining its LDO outputs as well as I2C/I3C Basic interfaces. Under the switchover conditions VIN_Mgmt back-feed voltage shall be less than 0.2 V. While PMIC is in switchover mode to VIN_Bulk, the VIN_Mgmt input supply can re-power backup at any time and PMIC switches back to VIN_Mgmt input supply for its LDO outputs and I2C/I3C interface continues to operate as normal.

The PMIC shall power up its output switch regulators when it registers VR Enable command.

```text
After VR Enable command is registered, the PMIC shall complete the following                       steps within
tPMIC_PWR_GOOD_OUT:

    1. Check VIN_Bulk, VIN_Mgmt and VBias Power Good status is valid.
    2. Power up itself - PMIC executes Power On Sequence Config 0 to Power On Sequence Config 3 registers and
       configures PMIC internal registers as programmed in DIMM vendor memory space registers.
    3. Power up all enabled output switch regulators and ready for normal operation
    4. Update status registers Table 98, “Register 0x08” [5:2] and floats CAMP signal.
```

If PMIC CAMP signal is not pulled High within tPMIC_PWR_GOOD_OUT time, the host can access the PMIC status registers for detailed information after tPMIC_PWR_GOOD_OUT time. The PMIC may NACK for any host request on I2C or I3C bus after VR Enable command until tPMIC_PWR_GOOD_OUT time expires. Note that in Figure 11 and Figure 12 the specific sequence of ramping the output regulators (VOUT_A, VOUT_B, VOUT_C, and VOUT_D) is for example purpose only. The specific ramp up sequence is configurable through the registers. Once PMIC’s output regulators are running, the PMIC allows VIN_Bulk input supply to vary. Figure 14 shows that VIN_Bulk can go as low as VIN_Bulk Min value (4.25 V) and PMIC output regulators will continue to operate as normal. The VIN_Mgmt input supply can drop and may re-power back up at any time.
