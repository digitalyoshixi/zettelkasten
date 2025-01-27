---
tags:
  - reverse_engineering
  - memory
---

### Part 15: Stack:

Functions are pivotal in software development. There's nothing that beats repeatable actions abstracted into one call. Do not Repeat Yourself holds true to assembly as well. When programs tend to repeat the same contiguous section of memory, we can say these are functions. These functions are stored in the stack where they can be easily repeated.

The way that the stack is built is very odd.

The stack pointer(ESP) will point to the smallest address that is not garbage. For example 0x00001110 is the stack limit, anything smaller than 0x00001110 is garbage. When we want to store a function into the stack, we pick a random address BIGGER than the stack limit, the addresses of the function are arranged so that it goes downwards. So the first starting address of function AddMe is 0x000AB112, the next address is 0x000AB10E.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivae_tmp_f93e37b734166082.png)

The stack bottom is actually the highest value in the stack. This is very fucked up, because its BOTTOM, NOT TOP but whatever.

If anything goes below the stack limit, we get a stack overflowwwwwwwwwwww. This can corrupt a program to allow an attacker to take control of the system. Malware attempts to go for stack overflows, but some current OS have measures that prevent this.

  

There are 2 operations used for stack: Push and pop. pushing is writing data, popping is copying data.

To push 1 or more registers, you must set the ESP to a smaller value. Usually, this smaller value is gotten by subtracting 4x the number of registeres to be pushed cause of 4bit yknow and then copying the registers to the stack.

To pop one or more registers, first copy the data from the stack to register, then add 4x the number of registers to the ESP.

  

The stack doesn’t just appear. When the program runs, functions get dynamically added to the stack. First is the return value, then the function actions, then at last the arguments.

  

If a function calls another function, we bring upon the existence of the FP(frame pointer). This pointer points to the original function, allowing the ESP to freely roam the newly called function. When ESP finishes, it goes back to the FP.

  

The stack has a LIFO mentality of last in first out. It makes lots of temporary variables that functions use, and then frees them when they are not needed anymore. Stack is very good in this regard for memory management. You don’t need to allocate memory and free it manually.

  
