---
tags:
  - networking
aliases:
  - NDP
---
An [[IPv6]] protocol that functions similarly to [[Address Resolution Protocol|ARP]] and [[Internet Control Message Protocol|ICMP]] in the sense that it responsible for giving the current device data on:
- The [[Router]] gateway
- [[Domain Name Server]]
- Local connections
# Router Linking
![[Neighbor Discovery Protocol-20240717170701301.webp]]
1. All computers connected to a network will send a Router Solicitation (RS) message
2. The router on the network replies with a Router Advertisement (RA) message and gives that device its global IP address.