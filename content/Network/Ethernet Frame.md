---
tags:
  - networking
---
# Ethernet Frame
Before [[Bit Transmission]] on a [[RJ-45]] starts, Data is encapsulated in the [[TCP & IP Data Layer|Data Layer]] using the Ethernet Protocol Encapsulation.
![[Ethernet Frame-20250605153927860.webp]]
# Ethernet Jargon
Ethernet protocol uses [[Frame Check Sequence|FCS]] which has different jargon than [[Network Messages|Frames]] that use [[Cyclic Redundancy Check|CRC]]
![[Pasted image 20230910191248.png]]
# Structure
### Header
- **Premable:** Used for synchronization
- **Start Frame Delimitter:** Signifies that next byte is start of destination address
- **Destination MAC address:** Signifies destination
- **Source MAC address:** Signifies source
- **Ethernet Type:** [[IPv4]],[[IPv6]],[[Systems Network Architecture|SNA]],[[DECnet]],[[AppleTalk]],etc...
### Payload
The middle is the payload data
### Trailer
- [[Frame Check Sequence]] :  The [[Cyclic Redundancy Check|CRC Checksum]]