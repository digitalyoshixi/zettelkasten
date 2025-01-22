---
tags:
  - llvm
aliases:
  - opt
---
The LLVM optimizer.

# mem2reg
```
opt -p mem2reg
```
Runs a single memory to register pass
Also, can be done with 
```
opt --O2
```
which is similar to [[Clang]]'s `clang -O2` optimization