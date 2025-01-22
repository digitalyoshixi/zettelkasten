---
tags:
  - llvm
---
A [[C]] and [[C++]] compiler maintained by the [[Low Level Virtual Machine|LLVM]] team.
# Anatomy
![[Clang-20241228215430190.webp]]
# Commands
### Compile to LLVM IR to Executable
```
clang -emit-llvm -S <filename>.c
```
### Compile to Executable
```
clang <filename>.c
./a.out
```
### Compile LLVM IR to Native Assembly
```
clang++ -S <filename>.ll
```
### Compile Native Assembly to Executable
```
clang++ -o <filename> <filename>.s
```