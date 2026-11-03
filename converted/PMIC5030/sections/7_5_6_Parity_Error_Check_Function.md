---
document: JESD301-5 (PMIC5030 Power Management IC Standard, Version 1.00, January 2026)
device: PMIC5030
application: server
section: 7.5.6
title: Parity Error Check Function
pages: 91-91
---
# 7.5.6 Parity Error Check Function

In I2C mode, parity error checking is not supported except for supported CCCs. Only I3C Basic mode supports parity error checking. By default, when PMIC device is put in I3C Basic mode, parity function is automatically enabled. The host can disable the function after it is enabled. Host can also disable the parity function with DEVCTRL CCC. When parity function is disabled, the PMIC device simply ignores the “T” bit information from the Host. The host may actually choose to compute the parity and send that information during “T” bit or simply drive static low or high in “T” bit. The PMIC device implements ODD parity. If an odd number of bits in the byte are ‘1’, the parity bit value is ‘0’. If even number of bits in the byte are ‘1’, the parity bit value is ‘1’. The host computes the parity and sends during “T” bit.
