---
tags:
  - hardware
  - electricity
aliases:
  - D Latch
---
A [[Set-Reset Latch|SR Latch]] whos S and R signals are negations of eachother.
![[Delay Latch-20250527154827888.webp|432]]
Most common latch used. Just set $D$ as the value you want to store.
Prevents [[Set-Reset Latch|SR]] [[Unstable Behavior|Oscillation]] condition from happening. But has a timing issue with [[Feedback]] solved by the [[Master Slave Flip Flop]]
It is also [[Transparent]].
# Types
- [[Active Low D Latch]]
- [[Active High D Latch]]