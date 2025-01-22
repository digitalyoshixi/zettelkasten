---
tags:
  - ASMTutor
  - x86
---
### Passing Arguments

When the program is run, all arguments are added to the stack. The last two stack items, and lowest address are the name of the program, and number of passed arguments.

So we do this:

1. Pop first item off the stack. This is number of arguments given
    
2. For loop with range of number arguments given. Keep popping and printing these arguments or store them in a variable or heap. Just not the stack.