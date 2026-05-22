---
tags:
  - networking
aliases:
  - PoE
---
The ability to use a [[Shielded Twisted Pair]] ethernet cable to power the device aswell.
# Power Sources
### Endspan
Power is given through the [[Switch]]
### PoE Injector (Midspan)
Placed between two cables, and provides power to the PoE cable.
Can also be used to: 
- Increase range of PoE cables
- Split PoE cables
- Provide power to non-POE switches
![[Power Over Ethernet-20240722164747216.webp]]

# Standards
### IEE 802.3af (PoE)
- 15.4W of DC power
- 350 mA max current
### IEE 802.3at (PoE+)
- 25.5W of DC power
- 600 mA max current
### IEE 802.3bt (PoE++ / 4PPoE)
##### Type 3
- 51W of DC power
- 600 mA max current
##### Type 4
- 71.3W of DC power
- 960 mA max current
- Works with [[Ethernet Speeds|10GBASE-T]]