---
tags:
  - IT
  - software
---
A real-time communication protocol. Often used to allow browser-to-browser applications:
- Voice call
- Video chat 
- File sharing
# Protocol
### Signalling
![[WebRTC-20260315021014634.webp]]
Establish connection to share [[Session Description Protocol|SDP]].
1. Establish an initial connection via websocket
2. Uses [[Interactive Connectivity Establishment]]
3. Uses a [[STUN Server]] for [[Network Address Translation|NAT]] traversal
![[WebRTC-20260315001434650.webp]]

4. Setup an initial connection via websocket