---
tags:
  - llvm
aliases:
  - SSA
---
A [[Intermediate Representation|IR]] property that requires:
- Each variable/register be alloted a value only once
- Every variable/register is defined before its use
# Implications
### No Recursive Definitions - Use Versioning Instead
You cannot mutate a variable in terms of itself.
`%i = add i32 %i, 1` is an illegal operation. it is a recursive definition
Instead, SSA requires you to do something like this **pseudocode**:
`%i.version2 = add i32 %i.version1, 1`
##### Clang's Solution to this Problem (`clang -O2`)
All variables are turned to [[LLVM alloca]]. They are stored on the stack where they can be freely manipulated with:
- [[LLVM load]]
- [[LLVM store]]
Example of initializaing:
```llvm
%var = alloca i32        ; Allocate space
store i32 10, i32* %var  ; Initialize with value 10
```
Example of reading and modifying:
```llvm
%val = load i32, i32* %var  ; Read value
%new_val = add i32 %val, 5  ; Modify value
store i32 %new_val, i32* %var  ; Store new value
```