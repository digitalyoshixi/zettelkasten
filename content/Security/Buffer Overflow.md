---
tags:
  - c
  - binary_exploitation
aliases:
  - Stack Overflow
  - Stack Smashing
---
A security flaw in which buffers on the [[Stack]] have their data overwritten by improper input validation.
# Example
Arrays in C are given a set length.
When a program reads more data that can be fit into the array, it is tricked into overwriting **other data or code** and compromising an application.
# Prevention Methods
- [[Stack Canary]]
- [[Address Space Layout Randomization]]
- Input sanitization