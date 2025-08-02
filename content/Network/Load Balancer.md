---
tags:
  - networking
---
![[Load Balancer-20240730024847156.webp|451]]
A software or hardware process on the [[Local Area Network|LAN]] that manages multiple servers to:
- Provide redundancy. if one is taken offline, their load is directed to another server
- Distribute load evenly across all servers
- Manage TCP connections
- Manage [[Secure Sockets Layer|SSL]] encryption and decryption
- Cache requests
- Prioritization to establish [[Quality of Service]]
- Content switching to direct certain application traffic to different server
# Types
- [[Layer 4 Load Balancer]]
- [[Layer 7 Load Balancer]]
# Concepts
- [[Least Utilized Host]]
- [[Affinity]]
- [[DNS Round Robin]]
- [[Load Balancer Configuration]]