---
tags:
  - networking
aliases:
  - Router Forwarding
---
A functionality of [[Router|Routers]] to communicate across multiple [[Local Area Network|LANs]]
# Path Determination
For data to be sent to a computer not within the same LAN, a path must be determined so that the data can pass through several [[Router|Routers]] as efficiently as possible to meet its destination.
![[Internet Protocol-20240716215920034.webp]]
### Hopping
Used to forward packets to other routers.
1. Receive packets through ports
2. Read the packet and see the destination
3. Read the routing table 
4. Forward it to the next router a router in the routing table