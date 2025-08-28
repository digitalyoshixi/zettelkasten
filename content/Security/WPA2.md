---
tags:
  - networking
aliases:
  - WPA2-PSK
  - IEEE 802.11i
---
A WPA protocol that:
- Uses [[Advanced Encryption Standard|AES-128]] encryption in [[Counter Mode with Cipher Block Chaining Message Authentication Code Protocol|CCMP]]
- Can be optionally backwards compatible to include [[Temporal Key Integrity Protocol|TKIP]], but its not recommended
- Uses a 4-way handshake to share the [[Pre-Shared Key|PSK]]
- Not secure
- Requires authentication with [[Remote Authentication Dial-In User Service|RADIUS]]
# PSK Problem (WPA2 Only)
1. Attacker listens to the 4 way handshake and steals the PSK hash
2. Attacker brute forces the hash to find the PSK
3. The PSK can be used to decrypt the network password