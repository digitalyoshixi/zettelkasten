---
tags:
  - memory
aliases:
  - ASLR
---
Processes will always be assigned a random address in memory.
- [[Base Address]] will be randomized
- Library addresses will be randomized
- Heap and Stack locations will be randomized
- Main program address is randomized if [[Position Independent Executable|PIE]] is enabled.

This is to avoid predictable memory reading to leak undesired information.

![[Address Space Layout Randomization-20250207215342425.webp]]
# Workarounds
- Leak the addresses that you require
- Use forks to brute force
- [[Overwriting Page Offsets]] 

