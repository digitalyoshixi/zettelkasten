---
aliases:
  - CPP
tags:
  - c
  - cpp
  - programming
---
https://www.learncpp.com/

C++ or CPP is the advanced version of [[C]] which is primarily used for higher level, optimized object oriented programming.
**Honestly C++ is just better in every way opposed to C. C is primarily used for embedded devices which are not able to run C++**
# C++ Building
1. Create the .cpp program to solve a problem
2. [[Compiler|Compile]] the program using g++ or another compiler
3. [[Linker|Link]] object files
4. run the program and debug, alter the original cpp program and repeat.

Alternatively, you can use automated build tools such as `make` or `build2`, however it is often better to build from hand

### My compile command
`g++ -o myfile -g myfile.cpp`
-o makes a new object file
-g enables debugging symbols
##### Compiling with different directory includes
`g++ -o main -I/source/includes main.cpp`
# C++ File Extensions
.cpp <- recommended one
.cc
.cxx

# Common C++ Problems
- [[C++ Common C++ Problems]]
# Nomenclature
- [[Statements]]
- [[Compile-time]]
- [[Runtime]]
- [[Identifiers]]
- [[Initialization]]
- [[Assignment]]
- [[Buffered outputs]]
- [[Declaration vs Definition]]
# Philosophy
- [[Treat Warnings as Errors]]
- [[Always Initialize your Variables]]
- [[Readability vs Productivity]]
# Concepts
- [[C++ Boilerplate]]
- [[Insertation Operator]]
- [[Extraction Operator]]
- [[Exit Codes]]
- [[Comments]]
- [[C++ Objects]]
- [[C++ Variable]]
- [[C++ Datatypes]]
- [[C++ Special Values]]
- [[C++ Initialization]]
- [[maybe_unused]]
- [[iostream.h]]
- [[C++ Undefined Behaviors]]
- [[C++ Implementation Behaviors]]
- [[Whitespace]]
- [[C++ Concatenation]]
- [[C++ Keywords]]
- [[Literals]]
- [[C++ Operators]]
- [[C++ Functions]]
- [[Metasyntactic Variables]]
- [[Exit Enums]]
- [[C Conditional Statements]] 
- [[C++ While Loops]]
- [[C++ Forward Declaration]]
- [[C++ One Definition Rule]]
- [[C++ Programs]]
- [[C++ Translation]]
- [[Preprocessor]]
- [[Preprocessor Directives]]
- [[C++ Macros]]
- [[C++ Conditional Compilation]]
- [[Header Files]]
- [[Arithmetic Overflow]]
- [[Fixed Width Integers]]
- [[Floating Point Integers]]
- [[C++ Booleans]]
- [[C++ Typecasting]]
- [[C++ Constants]]
- [[Conditional Operator]]
- [[Inline Functions]]
- [[Inline Variables]]
- [[C++ Strings]]
- [[C++ Vectors]]
# Specific Functions
- [[sizeof()]]
- [[setw]]
# Cursed C++
- [[Unnamed Parameters]]