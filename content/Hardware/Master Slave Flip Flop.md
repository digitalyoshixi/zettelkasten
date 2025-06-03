---
tags:
  - hardware
  - electricity
aliases:
  - Leader Follower Flip Flop
  - SR Flip Flop
---
This is a [[Flip-Flop]] that involves two [[Set-Reset Latch|SR Latch]] that operate on different clocks.
![[Master Slave Flip Flop-20250527155534691.webp]]
Many instances use a [[Clock Edge|Falling Edge]] triggered flip-flop for speed.
# Process
The data is only changed once per clock cycle.
- The SR leader latch changes the follower latch on [[Clock Edge|Rising Edge]]
- The follower latch outputs changes on [[Clock Edge|Falling Edge]]