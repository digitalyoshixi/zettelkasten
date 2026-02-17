---
tags:
  - networking
---
A [[Operational Technology|OT]] protocol for use with [[Programmable Logic Controllers|PLC]].
Uses [[Serial Communication]] with [[Serial Cable|DB-9]]
- Designed for [[Air Gapped Network]], allows arbitrary read/write commands without validation
# Modes
- [[Modbus RTU]]
- [[Modbus TCP]]
- [[Modbus ASCII]]
- [[Modbus Plus]]
- [[Enron Modbus]]
# Protocol
- Uses coil registers numbered for specific data transfers
![[Modbus-20260217192236567.webp]]
- Each server is assigned a server ID from 1-247
- Second bytes sent use a function code
![[Modbus-20260217192327998.webp]]
