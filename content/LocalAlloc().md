---
tags:
  - windows
---
```
DECLSPEC_ALLOCATOR HLOCAL LocalAlloc(
  [in] UINT   uFlags,
  [in] SIZE_T uBytes
);
```
# Example
```c
PVOID pAddress = LocalAlloc(LPTR, 100);
```