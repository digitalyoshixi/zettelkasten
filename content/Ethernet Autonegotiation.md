---
tags:
  - IT
  - networking
aliases:
  - IEE 802.3u
---
A mechanism for two nodes to exchange messages to choose the same [[Ethernet Protocol|Ethernet]] standard.
![[Ethernet Autonegotiation-20260620152634579.webp]]
# Protocol
- Device 1 declares capabilities by sending [[Fast Link Pulses|FLP]]
- Device 2 declares capabilities by sending [[Fast Link Pulses|FLP]]
- Two devices pick the fastest common speed
# One-Sided Autonegotiation
![[Ethernet Autonegotiation-20260620153427975.webp]]
If only one-side chooses to send a [[Fast Link Pulses|FLP]], then autonegotiation will default to the speed the other uses, and automatically pick the [[Point-to-point Communication|Duplex]]
- Can cause [[Duplex Mismatch Issue]]
# Autonegotiation on LAN Hubs
Since [[Hub|LAN Hub]] requires no collisions, it defaults to the lowest settings for their devices.
![[Ethernet Autonegotiation-20260620153656886.webp]]
Often results in devices using the slowest 10 Half duplex communication