---
tags:
  - c
aliases:
  - Declared
---
Declarations is when you tell the compiler I want a symbolic name of this variable, but you **dont** give it a value.
# Example
```c
int myballs;
```
# Multiple Declarations at once
If multiple variables/functions have the same datatype, they can be declared at the same time
### Multiple variables
```c
int a , b;
```
### Variables and functions
```c
double sum, atof();
```
You are not able to declare multiple functions on one line!
# Garbage Values
if [[Automatic Variables]] or [[Register Variables]] are declared and not [[C Initialization|Initialized]], then you get garbage values [[Undefined Behaviors]]