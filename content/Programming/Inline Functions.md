---
tags:
  - cpp
---
before, they keyword `inline` it was meant to allow for function calls to be replaced with the actual code of the function.

nowadays, its used to signal that this definition of the function can take many forms, those other forms being provided through other files.
The same function written in different files will not cause a linkage error if that function is inline.
These inline functions are popularly used in [[Header Files]] for this purpose

# Requirements 
- Full definition must be written in function definition
- Every definition for an inline function must be identical   *but bro, youre defining it in the header file, why must you define it again?*
 