---
tags:
  - hardware
aliases:
  - PCIe
---
![[Peripheral Component Interconnect Express-20240526013516178.webp]]
A faster and more efficient remodel of [[Peripheral Component Interconnect|PCI]], [[Peripheral Component Interconnect eXtended|PCI-X]] and [[Accelerated Graphics Port|AGP]] buses.
It utilizes [[Serial Communication]] to transfer data between peripherals.
# Specs
### Lanes
![[Peripheral Component Interconnect Express-20240526014539255.webp]]
The PCIE uses one wire for sending and another for recieving data.
This pair of these wires is called a lane.
![[Peripheral Component Interconnect Express-20240526015542416.webp|429]]
PCIE can have 1, 2, 4, 8, 12, 16 or 32 lanes.
The max amount of lanes PCIE can have is 32, reaching a theoretical bandwidth of up to $512_{\frac{GT}{s}}$or $64_{\frac{GB}{s}}$ 
### PCIE Transfer Speeds
Lane speed for each model is as follows:
- PCIE 1.x: $2.5_{\frac{GT}{s}}$
- PCIE 2.x: $5_{\frac{GT}{s}}$ 
- PCIE 3.x: $8_{\frac{GT}{s}}$
- PCIE 4.x: $16_{\frac{GT}{s}}$
### Spec Ambiguity
Certain times, PCIE lanes and models will not accurately represent its potential. Manufacturers may:
- Wire up a x16 slot to only work with 4 or 8 lanes
- [[Motherboard]] may artifically throttle data transfer because it was not made to handle the maximum data transfer.
- Older PCIe is worse
- PCIe speed can be affected by other slots in use
# 'Backwards' Compatability
Oftentimes on 8-pin PCIe power connections, you can detach 2 pins off and make it 6-pin