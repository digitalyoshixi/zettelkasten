---
tags:
  - hardware
---
![[Parallel Communication-20240526013855529.webp]]
A method of transmitting data by mapping each bit to a conductor. 
This means that for 32-bit chunks of data, you need 32 wires to carry each one bit.
Found commonly in [[Peripheral Component Interconnect|PCI]]
# Flaws
- Causes high delay
- Requires more physical space to implement
- [[Race Condition]]

This technology is inefficient and has been replaced with [[Serial Communication]] found in the [[Peripheral Component Interconnect Express|PCIE]]