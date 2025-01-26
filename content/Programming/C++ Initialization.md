---
tags:
  - cpp
---
There are 6 ways to initialize in c++
1. [[Default Initialization]]
2. [[Copy Initialization]]
3. [[Direct Initialization]]
4. [[Direct list Initialization]]
5. [[Copy list initialization]]
6. [[Value initialization]]

```cpp
int a;         // no initializer (default initialization)
int b = 5;     // initializer after equals sign (copy initialization)
int c( 6 );    // initializer in parenthesis (direct initialization)

// List initialization methods (C++11) (preferred)
int d { 7 };   // initializer in braces (direct list initialization)
int e = { 8 }; // initializer in braces after equals sign (copy list initialization)
int f {};      // initializer is empty braces (value initialization)
```
# List initialization vs Non-list
List initializtion's benefit is that it disallows "narrowing conversions" meaning that the compiler will catch if you try to brace a variable using a value that the variable cannot safely hold.
so if you try:
```cpp
int width {4.5} // error: a number with a fractional value can't fit into an int
```
it would send out an error in compilation.
If you didnt do this with list initialization, then it would have just rounded the number down, possibly unintended behavior. list initializtion is rust-ified before rust happened

# Best Practices
It is best to use [[Direct list Initialization]] or [[Value initialization]]

# Multiple Variable Initialization
```cpp
int a,b; // default initialization
int a = 5, b = 6;          // copy initialization
int c( 7 ), d( 8 );        // direct initialization
int e { 9 }, f { 10 };     // direct brace initialization
int g = { 9 }, h = { 10 }; // copy brace initialization
int i {}, j {};            // value initialization
```
