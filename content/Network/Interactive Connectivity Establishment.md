---
tags:
  - networking
aliases:
  - ICE
---
A networking protocol that allows for [[Peer to Peer|P2P]] connections between two devices on the public internet.
- Finds the best route to your peer
# Process
1. Check if peer on local network, then initiate route there
2. Check if peer on different network, negotiate [[Session Traversal Utilities for NAT|STUN]] to get their NAT address
3. Check if NAT issues, then negotiate [[Traversal Using Relays around NAT|TURN]] to do communication with middleman
# ICE Candidates
A [[Network Address Translation|NAT Address]] (IP:Port) each candidate can use to communicate with eachother
Gathered from [[Session Traversal Utilities for NAT|STUN]]