---
tags:
  - programming
---
A syntax for programming with functions. Largely replaced by [[Expression]] created by [[John McCarthy]].
Used in [[MLisp]]
# Function Application
```
f[x;y] ; apply function f with args x, y
```
# Function Definition
```
label[square;lambda[[x];times[x;x]]] ; square function
```
# Conditional
```
[lessp[x;0]->minus[x];T->x] ; abs conditional
```