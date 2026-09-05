---
tags:
  - networking
---
The protocol that each router uses to create their [[Routing Table]].
- Sharing routes with peers
- Determining best route to forward
# Basic Process
1. Router adds each connected [[Subnet]] to its [[Routing Table]]
2. Router shares its [[Routing Table]] with its peers, this [[Routing Table]] includes routes given by other neighbours previously
3. Router listens to messages from neighbors and learns new routes. Sets Next-Hop field to be that neighbour
![[Routing Protocol-20260530150346291.webp]]
# Protocol List
- [[Routing Information Protocol]]
- [[Enhanced Interior Gateway Routing Protocol]]
- [[Open Shortest Path First|OSPF]]
- [[Intermediate System to Intermediate System]]
- [[Border Gateway Protocol]]