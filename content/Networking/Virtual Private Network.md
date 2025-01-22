---
tags:
  - web
  - networking
  - security
aliases:
  - VPN
---
For creating a secure connection to a remote network.
![[Virtual Private Network-20240723033937909.webp]]
A tunnel is created that so that all packets are encrypted and sent to a VPN server, which is relayed to the router on their network.
# Encryption Process
1. Encrypt packet
2. Encapsulate
# VPN Backbone Technologies
### [[Layer 2 Tunneling Protocol|L2TP]] & [[IPsec]]
- Requires a client software
- Must be opened on packet-filtering devices
- When connected, you are in their network and can do regular [[Local Area Network|LAN]] activities
### [[Secure Sockets Layer|SSL]] & [[Transport Layer Security|TLS]]
- Does not require much configuration
- Requires an access portal to do [[Local Area Network|LAN]] activities