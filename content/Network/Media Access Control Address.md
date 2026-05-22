---
tags:
  - networking
aliases:
  - MAC Address
  - MAC Addresses
  - Burned In Address
  - Ethernet Address
---
![[Media Access Control Address-20240801210646554.webp]]
A unique identifier for [[Network Interface]] (that require it). Made for [[Unicast]] networking.
They are binary numbers that are 48 bits long.
- First 24 bits are the [[Organizational Unique Identifier|OUI]] of which vendor the [[Network Interface Controller|NIC]] was made.
- Last 24 bits are the vendor's assigned identifier to the [[Network Interface Controller|NIC]].
They are usually represented with 12 hexadecimal characters.
![[Media Access Control Address-20240716022030745.webp]]
# Concepts
- [[MAC Address Spoofing]]
# 2 Devices Same MAC Address
Since MAC addresses are intended to be globally unique, if 2 devices have the same MAC address due to [[MAC Address Spoofing]], then traffic will be sent to both addresses.
This causes [[Address Resolution Protocol|ARP]] issues, however [[Cisco]] router's can handle this and will often delist the 2nd MAC address device.
Oftentimes, MAC addresses will be reused. For the most part, this does not cause issues as its very unlikely 2 of the same mac address devices are on at the exact same time, but for local area networks this may pose a problem if not using a [[Cisco]] router.