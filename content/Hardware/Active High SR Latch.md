---
tags:
  - hardware
  - electricity
---
A [[Set-Reset Latch|SR Latch]] wherein:
- Set = 1 -> Q = 1
- Reset = 1 -> Q = 1
Denoted as $SR$ latch.
# Diagram
![[Active High SR Latch-20250527152429564.webp]]
# Truth Table

| $S$ | $R$ | $Q_{T}$ | $\overline Q_{T}$ | $Q_{T+1}$ | $\overline Q_{T+1}$ |
| --- | --- | ------- | ----------------- | --------- | ------------------- |
| 0   | 0   | 0       | 1                 | 0         | 1                   |
| 0   | 0   | 1       | 0                 | 1         | 0                   |
| 0   | 1   | X       | X                 | 0         | 1                   |
| 1   | 0   | X       | X                 | 1         | 0                   |
| 1   | 1   | X       | X                 | 0         | 0                   |
- Cases $S:1, R:1$ is a forbidden case
- Case $S : 0, R: 0$ will not change anything