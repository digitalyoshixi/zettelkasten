---
tags:
  - hardware
aliases:
  - Asynchronous Counter
---
This is a [[Counter|Counter]] that will only change based off of previous [[Toggle Flip-Flop|T Flip-Flop]] gates.
It is a [[Asynchronous Circuit]].
# Circuit Diagram
![[Ripple Counter-20250603183324907.webp]]
# Timing Diagram
With Input as 1, the total byte will increase. Note that with $Q_{3}$ as the MSB, $Q_{3},Q_{2},Q_{1},Q_{0}$ is the byte that increases.
![[Ripple Counter-20250603183445678.webp]]
# Example Video
https://invidious.yoshixi.net/watch?v=_0kGZhUE5D0