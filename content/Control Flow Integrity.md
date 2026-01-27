---
tags:
  - security
aliases:
  - CFI
---
A mitigation against [[Return Oriented Programming|ROP]].
Checks indirect jumps, returns that use registers as arguments (something an attacker could in theory control) and sees if their value is what they are supposed to be at runtime
# Counter CFI Techiques
- [[Block Oriented Programming]]
- [[Jump Oriented Programming]]
- [[Call Oriented Programming]]
- [[Sigreturn Programming]]
- [[Data Programming]]
# Implementations
- [[Control Flow Enforcement Technology]]