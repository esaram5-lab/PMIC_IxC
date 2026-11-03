---
document: JESD301-1A.03 (PMIC5000/PMIC5010 Power Management IC Standard, Rev. 1.8.5, February 2025)
device: PMIC5000/PMIC5010
application: server
section: 2.10.14
title: Bus Clear
pages: 88-89
---
# 2.10.14 Bus Clear

The PMIC device supports the following described Bus Clear feature in I2C mode only. Any attempt by host to perform I2C Bus clear on a target device in I3C mode may result in an active drive bus contention on the SDA data line.

There may be abnormal circumstances when the host abruptly stops clocking SCL while the target device is in the middle of outputting data for read operation. For these type of events, the SDA data line may appear as stuck low as the device is expecting to receive more clock pulses from the host. Eventually when the host has control of the SCL clock, the host may optionally clear the device that is stuck low on the SDA data line by sending continuous 18 clock pulses without driving the SDA data line followed by STOP operation. The device floats the SDA line within 18 clock pulses and returns to the Idle state. The device is ready for normal new transaction with Start condition.
