---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 2.7.7
title: CAMP Signal
pages: 31-33
---
# 2.7.7 CAMP Signal

The CAMP (Control AND Monitor Port) signal provides three different functions.

```text
1. Register write protect function
2. Fail_n function
3. Status function
```

## 2.7.7.1 Register Write Protect Function

By default, PMIC register write protect function is enabled (i.e., Table 137, “Register 0x2F” [2] = ‘0’). The CAMP input signal level determines when PMIC enters or exits the write protect mode. The PMIC enters the write protect mode when CAMP signal is at logic level High and Table 137, “Register 0x2F” [2] = ‘0’. PMIC exits the write protect mode when CAMP signal is at logic level Low. When PMIC is in write protect mode, the PMIC does not allow to modify registers Table 111, “Register 0x15” to Table 137, “Register 0x2F”, Table 140, “Register 0x32”, and Table 143, “Register 0x35” in the host region as well as Table 152, “Register 0x40” to Register 0x6F in the DIMM vendor region. These registers are write protected marked with RED color cells in “Register” column in Table 93, “Host Region - Register Map”. The PMIC simply ignores the host request for write operation in write protect mode. PMIC allows all register read access in write protect mode. Once PMIC is in write protect mode, there are 3 ways PMIC can exit write protect mode:

```text
1. PMIC sees CAMP input signal Low (clause 2.7.7.2)
2. PMIC triggers internal fault event (VIN_Bulk OV, VIN_Bulk UV, SWx_OV, SWx_UV) and asserts CAMP
   signal low.
3. PMIC goes through power cycle or power down cycle (i.e., simultaneous removal of VIN_Bulk and
   VIN_Mgmt input supplies)
```

If Table 137, “Register 0x2F” [2] = ‘1’, the PMIC does not enter write protect mode. The PMIC CAMP input signal has no effect on write protect function. The PMIC allows write and read access to all registers. Caution: The operation of non-write protect mode should be limited to lab and debug environment instead of normal system operation.

## 2.7.7.2 Fail_n Function

By default, PMIC Fail_n function is enabled (Table 140, “Register 0x32” [4] = ‘0’). When PMIC CAMP input signal transitions from High to Low, the PMIC executes VR Disable command (i.e., execute power off sequence config0 to config3 registers), asserts CAMP signal low (if Table 140, “Register 0x32” [3] = ‘0’), exits the write protect mode and clears Table 140, “Register 0x32” [7] to ‘0’. If Table 140, “Register 0x32” [4] = ‘1’, the PMIC Fail_n function is disabled. When CAMP signal transition from High to Low, The PMIC does not execute VR Disable command (i.e., does not execute power off sequence config0 to config3 registers), does not assert CAMP signal low, exits the write protect mode and does not clear Table 140, “Register 0x32” [7] to ‘0’. The Fail_n function is independent of PMIC’s write protect function.

## 2.7.7.3 Status Function

The PMIC CAMP PWR_GOOD output signal indicates status of VIN_Bulk input supply and all output regulators (VOUT_A, VOUT_B, VOUT_C, VOUT_D, VOUT_1.8V, VOUT_1.0V, VBias). Once PMIC receives VR Enable command, the PMIC floats CAMP pin when VIN_Bulk input supply is valid and all enabled output regulator’s (VOUT_A, VOUT_B, VOUT_C, VOUT_D, VOUT_1.8V, VOUT_1.0V, VBias) tolerances are maintained as configured in the appropriate register space. Note that CAMP pin is not affected based on VIN_Mgmt input supply. At first power up, with stable and valid input supply VIN_Mgmt as well as VOUT_1.8V and VOUT_1.0V LDO outputs, the PMIC asserts CAMP pin low however PMIC updates corresponding status register. Once PMIC receives VR Enable command from the host, the PMIC enables all appropriate output regulators and updates corresponding status registers and enters state called as “Regulation”. At this point, PMIC floats CAMP PWR_GOOD output and the external board pullup resistor pulls the CAMP pin high. Once the CAMP pin is pulled high (i.e., no other PMIC is driving the CAMP pin low), the PMIC enters state stated called as “online” state.

Once the CAMP pin is high, if PMIC detects any condition either on VIN_Bulk input supply or any of the output regulators (VOUT_A, VOUT_B, VOUT_C, VOUT_D, VOUT_1.8V, VOUT_1.0V, VBias) that causes the PMIC to update it status registers to indicate the power status is not good, then PMIC asserts CAMP pin low and keeps it asserted until the host explicitly takes a specific action corresponding to it. The PMIC does not automatically let the CAMP pin float even if the condition that triggered the PMIC to assert the CAMP pin no longer exists. In other words, the PMIC’s CAMP pin is latched and once latched, it must be explicitly addressed by the host. Regardless of whether PMIC is operating in write protect mode or not, the PMIC always asserts CAMP signal low to indicate the status if there is a fault event.
