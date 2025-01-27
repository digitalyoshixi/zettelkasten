---
tags:
  - reverse_engineering
  - GDB
---
### Part 39 fuck with the eip

Eip is the pointer to the next line. We will fuck with it to allow us to move to memory addresses out of bounds and break the program to spew

out garbage. Simply “set $eip = address” and then step in and you will see the world crumble