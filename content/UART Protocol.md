---
tags:
  - hardware
  - networking
---
# Protocol
![[UART Protocol-20250624214228347.webp]]
1. The protocol starts (mark) when the wire transitions from high to low.
  ![[Pasted image 20250624174324.png]]
  2. The data is sent directly
  3. The protocol stops when the wire returns back to high, and remaining there for an optional bit-time.
     ![[UART Protocol-20250624214437056.webp]]