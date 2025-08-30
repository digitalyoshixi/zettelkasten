---
tags:
  - security
  - linux
---
Linux uses [[Application Binary Interface|ABI]]
# Process
1. Arguments are saved into general purpose registers
2. Function is called with `call <location>`
3. Arguments are pushed onto the stack
4. Space is allocated onto the stack for local variables
5. Function does work
6. Stack is restored
7. Returns by calling `ret`
8. Stack adjusted to remove arguments