---
tags:
  - c
---
Code is not always evaluated from left to right.

For example:
```c
push(pop() - pop());
```
we have no guarantee whether the left pop or right pop will occur first.
This may lead to unintentional results.

To circumvent this, make sure to abuse `;` chronology.
```c
op2 = pop();
push(pop() - op2);
```
this way it will always do the same thing 100% of the time

The danger of forgetting the K&R Rearrangement license proves itself deadly when working with [[Extern Variables]] that have sequential effects for its shared actions.