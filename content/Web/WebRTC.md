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
![[WebRTC-20260315021014634.webp]]
1. Establish an initial connection via websocket
2. Find your peer using [[Session Description Protocol|SDP]] to negotiate supported protocols and additional codec info
3. Uses [[Interactive Connectivity Establishment|ICE]] to create the session
	1. Direct link if local network
	2. Uses a [[Session Traversal Utilities for NAT|STUN]] for [[Network Address Translation|NAT]] traversal
	3. Uses [[Traversal Using Relays around NAT|TURN]] to workaround [[Symmetric Network Address Translation|Symmetric NAT]] issues
4. Once session established, send [[Datagram Transport Layer Security|DTLS]] packets for payload data
![[WebRTC-20260315001434650.webp]]