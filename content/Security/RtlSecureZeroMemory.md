---
tags:
  - programming
  - windows
  - security
---
A function to memset memory to zero. Cannot be optimized by compiler unlike other functions.
```c
PVOID RtlSecureZeroMemory(
  [in, out] PVOID  Ptr,
  [in]      SIZE_T cnt
);
```
