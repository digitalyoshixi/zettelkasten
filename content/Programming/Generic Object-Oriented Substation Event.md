---
tags:
  - networking
aliases:
  - GOOSE
---
A way to exchange data under [[IEC 61850]] standard.
Enables high-speed [[Peer to Peer]] messaging used for [[Trip Signals]]
# Security Issues
- Messages unencrypted
- [[MAC Address Spoofing]]
- [[Replay Attack]]
# Security Mitigations
- [[Virtual Local Area Network|VLAN]]
- [[IEC 62351]]
- [[Network Access Control|NAC]]
- Time-stamping and anti-replay monitoring