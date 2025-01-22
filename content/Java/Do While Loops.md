---
tags:
  - control_flow
aliases:
  - Bottom Tested Loops
---
```c
do{
// some actions
} while (condition)
```
Bottom tested loops.

It will do it once guaranteed.

The rule of using this:
- Running >=0 times, top test [[C While Loops]].
- Running >=1 times, bottom test [[Do While Loops]].

Used for very niche scenarios where you need to do the action once beforehand.

