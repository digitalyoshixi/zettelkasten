---
tags:
  - security
  - binary_exploitation
aliases:
  - PLT
---
A table used by a [[Dynamic Linking|Dynamic Linker]] to redirect [[Position Independent Executable|Position Independent]] function calls to their absolute locations within the [[Shared Object]].
Contains code necessary for dynamic linking
# Intuition
![[Procedure Linkage Table-20260127023735549.webp]]
A function will call into plt address of for thatt function
![[Procedure Linkage Table-20260127023720781.webp]]
plt contains the code required to search for this function in the library