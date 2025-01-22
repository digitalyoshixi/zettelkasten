---
tags:
  - hardware
aliases:
  - System Crystal
  - System Clock
---
![[System Crystal-20240516013121595.webp]]
Used by the [[Clock Signal|Clock Wire]] to provide constant frequency.
When the PC is turned on, the quartz constantly fires electric pulses to the clock wire. The [[Central Processing Unit|CPU]] constantly needs to be performing tasks while the computer is active.
### Crystal Breakage
In the old days, these crystals would break, and you would have to buy a new one or manually synchronize the clock wire with the crystal.
These days, the motherboard sends the latency to the CPU, and the CPU adjusts automatically, thereby removing the need to manual fixes.
# Clock Speed
The clock speed is based off the crystal oscillator, the CPU multiplies the crystal frequency by a coefficient to get the clock speed.
# CLK Wire
Every device in your PC is matched to the speed of the system crystal.
![[Crystal Oscillator-20240526012451882.webp|358]]
The CLK wire is the wire that connects the system crystal to all other devices in your PC