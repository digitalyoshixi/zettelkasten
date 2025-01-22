---
tags:
  - programming
  - esolang
---
An [[Esolang]] that is [[Turing Complete]] with only 8 commands
# Commands
```bf
> Increment the data pointer  
< Decrement the data pointer  
+ Increment the byte at the data pointer  
- Decrement the byte at the data pointer  
. Output the byte at the data pointer as a character  
, Input a character and store it in the byte at the data pointer  
[ Jump past the corresponding ] if the byte at the data pointer is 0  
] Jump back to the corresponding [ if the byte at the data pointer is nonzero 
```
# Visualizer
For visualizing memory blocks
https://ashupk.github.io/Brainfuck/brainfuck-visualizer-master/index.html#