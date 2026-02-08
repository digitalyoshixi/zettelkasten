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
# C++ Building
1. Create the .cpp program to solve a problem
2. [[Compiler|Compile]] the program using g++ or another compiler
3. [[Linker|Link]] object files
4. run the program and debug, alter the original cpp program and repeat.

Alternatively, you can use automated build tools such as `make` or `build2`, however it is often better to build from hand

### My compile command
`g++ -o myfile -g -std=c++20 myfile.cpp`
-o makes a new object file
-g enables debugging symbols
##### Compiling with different directory includes
`g++ -o main -I/source/includes main.cpp`
# C++ File Extensions
.cpp <- recommended one
.cc
.cxx
# Boilerplate
- [[C++ Boilerplate]]
```cpp
#include <iostream>
using namespace std;
int main(int argc, char const *argv[])
{
	// your items
	return 0;
}
```
# Common C++ Problems
- [[C++ Common C++ Problems]]
# Nomenclature
- [[Programming/Statements]]
- [[Compile-time]]
- [[Runtime]]
- [[Identifiers]]
- [[Initialization]]
- [[Assignment]]
- [[Buffered outputs]]
- [[Declaration vs Definition]]
- [[C++ Versions]]
# Philosophy
- [[Treat Warnings as Errors]]
- [[Always Initialize your Variables]]
- [[Readability vs Productivity]]
# Concepts
- [[Insertation Operator]]
- [[Extraction Operator]]
- [[Exit Codes]]
- [[C++ Comments]]
- [[C++ Objects]]
- [[C++ Variable]]
- [[C++ Datatypes]]
- [[C++ Special Values]]
- [[C++ Initialization]]
- [[maybe_unused]]
- [[C++ iostream]]
- [[C++ string]]
- [[C++ Undefined Behaviors]]
- [[C++ Implementation Behaviors]]
- [[Whitespace]]
- [[C++ Concatenation]]
- [[C++ Keywords]]
- [[Literal]]
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
- [[C++ Map]]
- [[C++ Unordered Map]]
- [[C++ Set]]
- [[C++ Unordered Set]]
- [[C++ Queue]]
- [[C++ Style Guides]]
- [[C++ Class]]
	- [[C++ Virtual]]
	- [[C++ Constructor]]
	- [[C++ Destructor]]
	- [[C++ Public]]
	- [[C++ Private]]
	- [[C++ Protected]]
	- [[C++ Override]]
- [[C++ delete]]
- [[C++ Variant]]
- [[C++ Stack]]
- [[C++ Iterator]]
- [[C++ transform]]
# Guides
- [[C++ Vector Slice]]
# Specific Functions
- [[sizeof()]]
- [[setw]]
# Cursed C++
- [[Unnamed Parameters]]