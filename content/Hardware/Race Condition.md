---
tags:
  - os
aliases:
  - Time of Check to Time of Use
  - TOC/TOU
---
A moment of unpredictable behavior that occurs when multiple inputs act on the same resource without any protection for access control.

Can cause:
- Breaking limits (apply multiple coupons)
- Data overwriting of other variables in use
- Modifying state right after checking but before processing
- [[Partial Construction Race Condition]]
- Revealing of data affected by time (i.e password reset tokens)

Can be solved by implementing [[Queue]].
# Techniques
- [[Last Byte Synchronization]]
- [[Single Packet Attack|SPA]]
- [[Connection Warming]]
# Protections
- [[Request Locking]]
# Web Exploitation
- [[Burp Suite Turbo Intruder]]
