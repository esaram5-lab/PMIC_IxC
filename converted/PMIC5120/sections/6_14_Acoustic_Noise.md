---
document: JESD301-6 (PMIC5120 Power Management IC Standard, Version 1.0, February 2025)
device: PMIC5120
application: client
section: 6.14
title: Acoustic Noise
pages: 65-66
---
# 6.14 Acoustic Noise

The PMIC5120 buck regulators normally operates in DCM (Discontinuous Current Mode). The buck regulator’s switching frequency is a function of a current load on its output regulator. At light load (typically < 50mA), the buck regulator’s switching frequency may approach to less than 100 KHz. The human ear audible frequency range is 20 Hz to 20 KHz. If buck regulator switching frequency falls within the human ear audible frequency range, then human ear can experience the acoustic noise. To prevent the acoustic noise to human ear, the PMIC offers a feature which prevents the buck regulator switching frequency to go below the threshold frequency that is configured in register R36[3:1]. When the feature is enabled, the PMIC ensures that its switching frequency stays above the threshold frequency regardless of how low the output load current may be.

The acoustic noise prevention control feature is in Table 150, Register 0x36 [3:1]. The control register applies to all three buck regulators. This feature is not applicable to any buck regulator that is configured to operate as Forced CCM (Continuous Current Mode). If PMIC is configured such that one or more buck regulators is configured as DCM and other buck regulator is configured as Forced CCM, when this feature is enabled, it applies to any buck regulators that are configured as DCM.

At light load, when this feature is enabled, there may be a slight difference in efficiency. However, the difference in efficiency may be insignificant and may be within the measurement noise.
