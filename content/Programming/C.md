---
tags:
  - programming
  - c
---
This is the low level language used to write operating systems.
For in-depth C knowledge, consult [[C History]]
### My build command
`gcc -o myfile -g myfile.c -lm`
-o makes a new object file
-g enables debugging symbols
-lm links modules
### Building as DLL
`gcc -c mydll.c`
`gcc -shared -o mydll.dll mydll.o`
-c compiles to object file
-shared tells it to make a dll
-o points it to its result file
### Linking an executable to DLL
- If you are in the same directory as your DLL, then you can just build like normal. `gcc -o myfile -g myfile.c`
- If the DLL is somewhere else, consult: https://opensource.com/article/22/5/compile-code-ldlibrarypath
## C++ Compile Process
you need 3 tools: 
- [[Compiler]]
- [[Linker]]
- [[Archiver]]
From these, you can make an
- [[Executable]]
- [[Dynamic Linked Library]]
# Boilerplate
- [[C Boilerplate]]
# Concepts
- [[C Declarations]]
- [[C Initialization]]
- [[Undefined Behaviors]]
- [[Preprocessor]]
- [[C Command Line Arguments]]
### Datatypes & Special Datatypes
- [[C Datatypes]]
- [[Integer Division]]
- [[End of File|EOF]]
- [[C String]]
- [[C Typecasting]]
- [[C Escape Codes]]
- [[Pointer]]
- [[C Arrays]]
- [[C Matrices]]
- [[C Structures]]
- [[C Unions]]
##### Variable Types
- [[C Macro]]
##### Scope
- [[Local Variables]]
- [[Global Variables]]
##### Pertinence
- [[Automatic Variables]]
- [[Static Variables]]
- [[Extern Variables]]
- [[Register Variables]]
### Control Flow
- [[C While Loops]]
- [[C For Loops]]
- [[C Conditional Statements]]
- [[C Switch Statements]]
- [[Do While Loops]]
- [[Break]]
- [[C goto]]
- [[Loop Testing]]
##### Expressions
- [[Operator Precedence|Expression Precedence]]
- [[C Operators]]
- [[C Bitwise Logical Operators]]
### Functions/Program
- [[main]]
- [[Void Arguments]]
- [[C Functions]]
- [[Pass by Value]]
- [[C Programs]]
- [[Pass by Reference]]
- [[C Function Pointers]]
### Memory
- [[Fragmenting]]
- [[Garbage Collection]]
- [[Shallow Copy]]
- [[Deep Copy]]
- [[C Memory Model]]
- [[C malloc|malloc]]
- [[C calloc]]
- [[C realloc]]
- [[C memalign]]
- [[free()]]
### In-line [[Assembly]]
- [[C asm]]
### Other
- [[2's Complement]]
# Experienced C Tricks
- [[Assignments = Expressions]]
- [[Several Conditions Inside For Loops]]
- [[Typecasting Parameters]]
- [[i++ and ++i return usage]]
- [[Static Name Collision Avoidance]]
- [[Array Of Pointers]]
# Methods
- [[i++ vs ++i]]
# [[Standard Library]]
# Cursed C
- [[char restraints]]