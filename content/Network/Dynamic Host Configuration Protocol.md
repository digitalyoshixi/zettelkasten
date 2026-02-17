---
tags:
  - networking
aliases:
  - DHCP
  - Dynamic IP
---
Protocol that is responsible for giving and removing [[IP Address|IP Addresses]].
Devices use this for obtaining dynamic [[IP Address]]
Conventionally seen on port `udp/67` and `udp/68`.
It is recommended to **disable** DHCP to prevent unknown devices from entering the network. All known devices should have a static IP.
If you really need DHCP, allot a minimum of DHCP addresses
# Dynamic Address Protocol
![[Dynamic Host Configuration Protocol-20240717175525201.webp|532]]
DISCOVER > OFFER > REQUEST > ACK (DORA)
1. New device enters the network and notifies to the DHCP server
2. DHCP server sends a [[Broadcast Frame]] containing all possible IP addresses device can have. These IP's are given on a lease meaning they can expire if the device is unable to renew it automatically.
3. The device picks one and notifies the DHCP server so that it may not be assigned again
4. DHCP assigns the address and sends an acknowledgement reply
# Concepts
- [[DHCP Reservation]]
- [[DHCP Leasing]]
- [[DHCP Pool]]
- [[DHCP Starvation]]