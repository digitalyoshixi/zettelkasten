---
tags:
  - x86
  - ASMTutor
---

### Lesson 5 modules

You know those include, import that some languages use to grab functions from other files? We can do that aswell, just for general organization.

What we do is we must create our assembly program in a way that it is self contained for the most part. We don't need to return anything, memory is shared so whatever changes in this file, changes for the others as well.

The important thing to creating a self contained program that doesn’t interfere with others is by doing the following:

- Push registers and pop them back if you are using multiple temporary values
    

- For those modules that ‘return’ a value, like storing string length in eax, you dont want to push or pop eax
    
- Remember FIFO, this is incredibly important. Pop only the one you just pushed
    

- Make a main label or split into several labels. The other script will call this label, so you must make one for them to call
    
- Have a ret at the very end
    

  

To use functions from the module in other programs, you must:

1. %include “filename.asm”
    
2. call labelname
    
