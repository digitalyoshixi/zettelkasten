---
tags:
  - c
  - binary_exploitation
aliases:
  - Stack Smashing
---
A security flaw in which buffers on the [[OS Stack]] have their data overwritten by improper input validation.
# Example
Arrays in C are given a set length.
When a program reads more data that can be fit into the array, it is tricked into overwriting **other data or code** and compromising an application.
Can be used to:
- Change a code pointer
	- Modifying the return address of a function to point to some other region of memory
- Overwrite a variable's data
- Change the read pointer or offset allowing us to access arbitrary memory
- Change a write pointer allowing us to overwrite arbitrary memory
# Prevention Methods
- [[Stack Canary]]
- [[Address Space Layout Randomization]]
- Input sanitization
# Example Uses
- [[Slammer Worm]]