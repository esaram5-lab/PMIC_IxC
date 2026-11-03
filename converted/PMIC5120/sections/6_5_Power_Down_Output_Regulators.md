---
document: JESD301-6 (PMIC5120 Power Management IC Standard, Version 1.0, February 2025)
device: PMIC5120
application: client
section: 6.5
title: Power Down Output Regulators
pages: 38-49
---
# 6.5 Power Down Output Regulators

Regardless of how PMIC’s output regulators are turned on (with VR_EN pin or with VR Enable command on I2C/ I3C Basic bus), the PMIC’s output regulators are powered down as described below depending on PMIC’s mode of operation.

## Subsections

- [6.5.1 Normal Power Down Sequence](6_5_1_Normal_Power_Down_Sequence.md)
- [6.5.2 Programmable Mode Operation; R1A[4] = ‘0’](6_5_2_Programmable_Mode_Operation_R1A_4_0.md)
- [6.5.3 Programmable Mode Operation; R1A[4] = ‘1’](6_5_3_Programmable_Mode_Operation_R1A_4_1.md)
- [6.5.4 Secure Mode Operation; R1A[4] = ‘0’](6_5_4_Secure_Mode_Operation_R1A_4_0.md)
- [6.5.5 Secure Mode Operation; R1A[4] = ‘1’](6_5_5_Secure_Mode_Operation_R1A_4_1.md)
