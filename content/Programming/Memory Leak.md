---
tags:
  - c
  - programming
---
A failing of optimization where unused memory is still allocated. 
Can cause programs to crash
# Cases
- [[Unfreed Pointer Memory Leak]]
- [[Invalid Pointer Access Memory Leak]]
- [[Dangling Pointer]]
- [[Handle Leak]]
# Finding Leaks
- [[Valgrind]]
- [[AddressSanitizer]]
- [[Static Application Security Testing|SAST]] (not as good as dynamic though)