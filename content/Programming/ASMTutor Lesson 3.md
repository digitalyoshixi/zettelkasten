---
tags:
  - ASMTutor
  - math
---

### Lesson 3 string length algorithm

Their goal is to figure out the length of a string. They do this by doing pointer arithmetic. Find the starting address of the string, then sift through all other addresses with higher address until you find an empty junk address like 00000000. Then subtract starting mem address with end mem address to find length.