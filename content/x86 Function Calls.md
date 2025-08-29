---
tags:
  - x86
  - assembly
  - programming
---
# Process
1. Arguments are placed onto the stack
2. Function is called with `call <location>`
3. Space is allocated onto the stack for local variables
4. Function does work
5. Stack is restored
6. Returns by calling `ret`
7. Stack adjusted to remove arguments