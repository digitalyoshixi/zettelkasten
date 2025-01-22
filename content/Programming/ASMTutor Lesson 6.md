---
tags:
  - x86
  - ASMTutor
---
### Lesson 6 null terminators

Certain times, when we make a variable in the .data, they will have their memory addresses right beside eachother. This is bad if we are pointer arithmetic since we dont know when one ends and the other beings. Thus, we need to add a null terminator to the end of a string. The null terminator is same as 00000000 or 0x0.