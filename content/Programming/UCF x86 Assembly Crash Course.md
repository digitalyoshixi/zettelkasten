---
tags:
  - assembly
---
[https://www.youtube.com/watch?v=75gBFiFtAb8](https://www.youtube.com/watch?v=75gBFiFtAb8)

Very good video. **But not for x86 assembly**

### Mov

mov operation will take 2 arguments.

mov arg1,arg2

The value at arg1 will be the value at arg2

If you want to move a value from a memory address, you must provide the address with [] to dereference. Eg:

mov eax,[ebp-0x8] will move the value at ebp-0x8 into eax.