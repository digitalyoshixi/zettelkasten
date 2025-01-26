---
tags:
  - networking
  - security
aliases:
  - WPA
---
A security policy for [[Access Point|WAPs]] using [[WI-FI|IEE 802.11]]. Designed to replace [[Wireless Equivalent Privacy|WEP]]
# WPA Versions
### WPA
- Uses [[Temporal Key Integrity Protocol|TKIP]] encryption specially designed for WPA.
### WPA2
- Uses [[Advanced Encryption Standard|AES-128]] encryption in [[Counter Mode with Cipher Block Chaining Message Authentication Code Protocol|CCMP]]
- Can be optionally backwards compatible to include [[Temporal Key Integrity Protocol|TKIP]], but its not recommended
- Uses a 4-way handshake to share the PSK
### WPA3
- Uses [[Advanced Encryption Standard|AES-256]] encryption in [[Galois Counter Mode Protocol|GCMP]] or [[Counter Mode with Cipher Block Chaining Message Authentication Code Protocol|CCMP]]
- Does not allow [[Temporal Key Integrity Protocol|TKIP]]
- Uses [[Diffie Hellman Key Exchange]] in [[Simultaneous Authentication of Equals|SAE]]
# Security Modes
### Personal
Everybody has the same pre-shared key (PSK)
### Enterprise 
Requires the setup of a [[Remote Authentication Dial-In User Service|RADIUS]] or [[Terminal Access Controller Access-Control System Plus|TACACS+]] authentication server 
# PSK Problem (WPA2 Only)
1. Attacker listens to the 4 way handshake and steals the PSK hash
2. Attacker brute forces the hash to find the PSK
3. The PSK can be used to decrypt the network password