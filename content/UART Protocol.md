---
tags:
  - hardware
  - networking
---
# Protocol
![[UART Protocol-20250624214228347.webp]]
1. The protocol starts (mark) when the wire transitions from high to low.
   ![[Pasted image 20250624174324.png|381]]
  2. The data is sent directly following Least Significant Bit
  3. Optional parity bits are sent after data
     ![[UART Protocol-20250624214603335.webp]]
  4. The protocol stops when the wire returns back to high, and remaining there for an optional bit-time.
     ![[UART Protocol-20250624214437056.webp|330]]