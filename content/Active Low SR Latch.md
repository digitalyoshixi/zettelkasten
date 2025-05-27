---
tags:
  - hardware
  - electricity
---
A [[Set-Reset Latch|SR Latch]] where:
- Set = 0 -> Q = 1
- Reset = 0 -> Q = 0
Preferred because [[Nand|Nand Gate]] are cheaper.
Denoted as $\overline{SR}$ latch
# Circuit Diagram
![[Active Low SR Latch-20250527152458016.webp]]
# Truth Table

| $\overline S$ | $\overline R$ | $Q_{T}$ | $\overline Q_{T}$ | $Q_{T+1}$ | $\overline Q_{T+1}$ |
| ------------- | ------------- | ------- | ----------------- | --------- | ------------------- |
| 0             | 0             | X       | X                 | 1         | 1                   |
| 0             | 1             | X       | X                 | 1         | 0                   |
| 1             | 0             | X       | X                 | 0         | 1                   |
| 1             | 1             | 0       | 1                 | 0         | 1                   |
| 1             | 1             | 1       | 0                 | 1         | 0                   |
- Case $S:0, R:0$ is a forbidden case
- Case $S : 1, R: 1$ will not change anything