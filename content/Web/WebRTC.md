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
1. Establish an initial connection via websocket
2. Uses [[Interactive Connectivity Establishment]] to create the session
	1. Uses a [[Session Traversal Utilities for NAT|STUN]] for [[Network Address Translation|NAT]] traversal
	2. Optionally uses [[Traversal Using Relays around NAT]] to workaround [[Symmetric Network Address Translation|Symmetric NAT]] issues
3. After session established, share [[Session Description Protocol|SDP]] payloads.
![[WebRTC-20260315001434650.webp]]