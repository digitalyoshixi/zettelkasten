---
aliases: 
tags:
  - c
  - programming
---
Translates one [[High-Level Language]] into a [[Low-Level Language]]
Compiling does **2** things:
1. Checks the code if it follows the rules of C++, checking syntax and possible memory leaks.
2. Turns code into [[Abstract Syntax Tree|AST]]
3. Optimizes code
4. Converts to a lower-level [[Intermediate Representation|IR]]
5. It is the responsibility of an external tool (CPU, another interpreter, etc) to either convert the IR into an object file or interpret it.
![[Pasted image 20231119135642.png]]

After the compiler, we optionally pass the program to a [[Linker]]
# Compiler Types
- [[Ahead-of-time Compilation]]
- [[Just-in-time Compilation|JIT Compilation]]
- [[AST Transformers|Transpilers]]
# The As-If Rule #redteam 
The compiler can modify a program any way it likes to produce more optimized code, so long as the modifications do not affect the program's observable behavior.
There is such thing as an https://www.awelm.com/posts/evil-compiler
evil compiler

### Example optimizations
- 3+4 -> 7 every time. we dont need to calculate every compile.
- Replacing constant values with literals