---
tags:
  - networking
aliases:
  - Router Forwarding
  - Host Forwarding
---
A functionality of [[Router|Routers]] to communicate across multiple [[Local Area Network|LANs]]
# Path Determination
For data to be sent to a computer not within the same LAN, a path must be determined so that the data can pass through several [[Router|Routers]] as efficiently as possible to meet its destination.
![[Internet Protocol-20240716215920034.webp]]
### Hopping Process
Used to forward packets to other routers.
1. Receive packets through ports
2. Use [[Frame Check Sequence|FCS]] in data-link frame to ensure no errors. If an error occured, discard frame
3. Read the [[IP Header|IP Frame]] and see the destination
4. Read the [[Routing Table]]
5. Forward it to the next router a router in the routing table
![[Path Determination-20260530144837511.webp]]
