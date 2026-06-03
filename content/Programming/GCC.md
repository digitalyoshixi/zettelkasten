---
tags:
  - c
  - compilers
---
The gnu compiler for languages like:
- [[C]]
- [[Go]]
- [[C++]]
- [[Ada]]
# Process
![[GCC-20250820034839184.webp]]
- [[Preprocessor]]
- [[Compiler]]
- [[Assembler]]
- [[Linker]]
# Flags
### `-o`
sets the output name
### `-c filename.c`
Compiles without linking  to make `filename.o`
### `-S filename.c`
Assembles program and creates `.s` file to `filename.s`
### `-D MACRO=val`
Passes in a custom macro with a custom value
### `-g`
adds debugger symbols
### `-wall`
Shows all the warnings
### `-lm`
For linking [[math.h]] library
### `-std=c++20`
For setting the current version to c++ 20
# Compiler Flags
- `-O0` : No optimizations
- `-O1` : Default optimizations
- `-O2` : Optimize that does not involve a speed-space tradeoff
- `O3` : Maximum optimization
# Compiling a [[Dynamic Linked Library|DLL]]
```
gcc -c myfile.c && gcc -shared -o myfile.dll myfile.o
```