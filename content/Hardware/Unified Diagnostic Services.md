---
tags:
  - hardware
aliases:
  - UDS
---
A protocol used by [[Vehicle Control Unit|ECU]] over [[Controller Area Network Bus|CAN]] to provide diagnostic information. Can be programmed.
![[Unified Diagnostic Services-20260516025435953.webp]]
# Protocol
This is a request/response protocol.
### Request
- First byte : ServiceID
- Second byte : often times sub-function of service
- Rest of bytes are parameter of service
