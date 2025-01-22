---
tags:
  - windows
  - win32api
---
https://learn.microsoft.com/en-us/windows/win32/api/memoryapi/nf-memoryapi-virtualalloc
The windows version of [[C malloc]].
```cpp
LPVOID VirtualAlloc(
  [in, optional] LPVOID lpAddress,
  [in]           SIZE_T dwSize,
  [in]           DWORD  flAllocationType,
  [in]           DWORD  flProtect
);
```
When you save this, it is saved as a [[Pointer|Void pointer]]. You just need the memory address, not the type.