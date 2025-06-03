---
tags:
  - programming
  - hardware
---
A [[Parallel Communication]] [[Register]]. 
This is a [[Register]] that feeds each data into each flip-flop.
Only takes one clock cycle to load all data.
![[Load Register-20250603183042018.webp]]
# Load Register with [[Multiplexer|MUX]]
Adding a [[Multiplexer|MUX]] and [[Feedback]] to a load register, allows you to have modes:
- $EN = 1$ -> D2 is what D is (load D)
- $EN = 0$ ->D2 is what Q is (maintain Q)
![[Load Register-20250603183101081.webp]]