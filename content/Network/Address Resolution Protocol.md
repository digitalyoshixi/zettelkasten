---
tags:
  - networking
aliases:
  - ARP
---
Protocol to get [[Media Access Control Address|MAC Address]] from [[IP Address]]
# Process
1. Device needs to find the [[Media Access Control Address|MAC Address]] corresponding to a specific [[IP Address]] 
2. Device sends a [[Broadcast Frame]] to all devices asking which device has this [[IP Address]]
3. Corresponding device replies with their [[Media Access Control Address|MAC Address]]
4. The first device stores this [[IP Address]] : [[Media Access Control Address|MAC Address]] mapping in a ARP cache
# Vulnerabilities
- [[ARP Poisoning]]
- [[ARP Spoofing]]