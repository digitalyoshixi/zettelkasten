---
tags:
  - cpp
---
https://en.cppreference.com/w/cpp/language/types
# Void Types
##### void
- type with empty set of values
- incomplete data type that cannot be completed.
- Objects this type are not allowed
	- No arrays of void
	- No variables to void
- You are allowed:
	- Pointers to void
	- Functions returning void

# int Types

##### int
a number without fractional component
### Polarity
##### signed
signed representation. first bit is polarity
don't actually write this. all integers are signed by default
```cpp
signed int a = -20;
```
##### unsigned
unsigned representation
```cpp
unsigned int a = 20;
```
### Size
##### short
width of at least 16 bits
##### long
width of at least 32 bits
##### long long
width of atleast 64 bits

You can mix and match polarity and size eg. `unsigned long myanus = 20;`

# Extended Integer Types
##### bool
true or false
### char Types
##### char
character representation for values of 0-255
##### signed 
signed character
##### unsigned 
unsigned character
##### wchar_t 
type for wide characters. same size, polarity and alignment as the integer.
32bits of unix, 16bits on windows

# Floating-point types
##### float
single precision floating-type
##### double
double precision floating-type
##### long double
extended precision floating-type

Floating point types may support [[C++ Special Values]]

# Strings
[[C++ Strings]]
strings must be imported with the `#include <strings>` command.
additionally, `using namespace std;`
a string is the non-primitive version of a char[]. instead of a fixed length, you can create a string and have it automatically manage the memory for you.

# Null Pointer
`std::nullptr`
