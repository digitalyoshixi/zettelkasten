---
tags:
  - networking
  - link_layer
  - networking_model
---
# Ethernet Frame
Before [[Bit Transmission]] on a [[RJ-45]] starts, Data is encapsulated in the [[TCP & IP Data Layer|Data Layer]] using the Ethernet Protocol Encapsulation.
![[Pasted image 20230910185226.png]]
The Ethernet Frame looks as such. 
The header contains:
- Destination MAC address
- Source MAC address 
- Ethernet Type
The middle is the payload
The tail is the [[Cyclic Redundancy Check|CRC Checksum]]
