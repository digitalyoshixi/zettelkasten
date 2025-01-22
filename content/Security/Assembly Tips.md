---
tags:
  - reverse_engineering
  - assembly
---
Some tricks to understand what some assembly instructions are doing.

# sub \_\_ , sp
subtract the esp by a value.
This allocates the subtracted value to the stack.
For example, making a argument 
```c
char balls[500];
```
to asm code, this would be `sub 0x1f4, esp` to allocate 500bytes.
Usually when you enter a function and stuff is added to call stack
# mov \_\_, sp

# sp = 0
clears the stack