---
aliases: 
tags:
  - memory
  - cpp
---
When a program is ran, the OS loads the program into RAM. Additional memory for the program is also reserved. In some older programming languages, you were able to access RAM directly, writing statements like "go get the value located at address 0x00120FF2". 
In C++ however, direct memory access is discouraged. Instead, we get memory indirectly through objects.

### The object is an umbrella term
An object is used to store a value in memory. A variable is an object that has a name (identifier).
Naming our objects let us refer to them again later in the program.

the [[C++ Variable]] is a type of object with a name and value only.