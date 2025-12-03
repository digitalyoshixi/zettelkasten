---
tags:
  - programming
  - compilers
aliases:
  - TAC
  - 3AC
---
An [[Intermediate Representation|IR]] used for [[Compiler Optimization]] to improve transformations.
Has a structure like:
```
t1 := t2 + t3
```
# Example
```
y := 4*x*x - 2*x + 1
```
converts to
```
x1 := x * x;
x2 := 4 * x1;
x3 := 2 * x;
x4 := x2 - x3;
y := x4 + 1;
```
