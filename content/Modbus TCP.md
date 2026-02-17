---
tags:
  - networking
aliases:
  - Modbus/TCP
---
A [[Modbus RTU]] wrapped in [[Ethernet Flavours|802.3]] connection.
- `tcp/502` for Modbus/TCP
- `tcp/802` for Modbus/TCP-Secure
# Specification
- 6-byte header to allow for routing
- Multiple clients - allows for 32-devices max
- Requires a [[Switch]] to connect devices together
# Insecurity
- Any host can send function codes