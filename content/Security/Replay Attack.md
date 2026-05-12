---
tags:
  - security
  - redteam
aliases:
  - Repeat Attack
  - Playback Attack
---
![[Replay Attack-20240822212926969.webp]]
A [[Man-In-The-Middle|MITM]] attack that intercepts and replays private information meant to be sent from a client, thus impersonating the client.
Can be done with [[Burp Suite]] proxy.
# Prevention
### Time Stamps
Giving a timestamp to the packet prevents it from being repeated
### Packet Sequencing
### Challenge-Response
### Ephemeral Session Encryption