---
tags:
  - hardware
  - electricity
aliases:
  - JK Flip-Flop
---
A modified [[Delay Flip-Flop|D Flip-Flop]] that attempts to replicate the [[Master Slave Flip Flop|SR Flip Flop]].
- Set $(J)$
- Reset $(K)$
![[Jack Kilby Flip-Flop-20250507024347410.webp|215]]
Can be set as:
- synchronous mode (controled by [[Clock Signal]])
- asynchronous mode (state is independent of clock)
# Circuit Diagram
![[Jack Kilby Flip-Flop-20250527182638015.webp]]
# Truth Table

| $J$ | $K$ | Output                       |
| --- | --- | ---------------------------- |
| 0   | 0   | maintain output              |
| 0   | 1   | 0                            |
| 1   | 0   | 1                            |
| 1   | 1   | [[Toggle Flip-Flop\|Toggle]] |
