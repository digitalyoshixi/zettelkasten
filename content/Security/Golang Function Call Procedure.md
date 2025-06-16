---
tags:
  - go
  - reverse_engineering
---
Golang does not work with arguments, parameters, or variables in functions. Everything is directly loaded onto the stack and the compiler keeps track.
# Calling Function
Golang directly loads the function arguments to the correct position on the stack.
![[Golang Function Call Procedure-20250614193230280.webp]]
# Running Function
When you run the function, the function directly reads each argument from the stack aswell.
![[Golang Function Call Procedure-20250614193305771.webp|319]]
Return values are also directly pushed back onto the stack.