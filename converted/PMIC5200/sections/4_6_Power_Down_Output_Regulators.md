---
document: JESD301-3 (PMIC5200 Power Management IC Standard, Version 1.0, October 2025)
device: PMIC5200
application: client
section: 4.6
title: Power Down Output Regulators
pages: 32-43
---
# 4.6 Power Down Output Regulators

Regardless of how PMIC’s output regulators are turned on (w/ VR_EN pin or w/ VR Enable command on I2C/I3C Basic bus), the PMIC’s output regulators are powered down as described below depending on PMIC’s mode of operation.

## Subsections

- [4.6.1 Normal Power Down Sequence](4_6_1_Normal_Power_Down_Sequence.md)
- [4.6.2 Programmable Mode Operation; R1A[4] = ‘0’](4_6_2_Programmable_Mode_Operation_R1A_4_0.md)
- [4.6.3 Programmable Mode Operation; R1A[4] = ‘1’](4_6_3_Programmable_Mode_Operation_R1A_4_1.md)
- [4.6.4 Secure Mode Operation; R1A[4] = ‘0’](4_6_4_Secure_Mode_Operation_R1A_4_0.md)
- [4.6.5 Secure Mode Operation; R1A[4] = ‘1’](4_6_5_Secure_Mode_Operation_R1A_4_1.md)
