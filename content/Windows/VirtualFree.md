---
tags:
  - windows
  - win32api
---
https://learn.microsoft.com/en-us/windows/win32/api/memoryapi/nf-memoryapi-virtualfree
The windows version of [[free()]]

```cpp
BOOL VirtualFree(
  [in] LPVOID lpAddress,
  [in] SIZE_T dwSize,
  [in] DWORD  dwFreeType
);
```
returns whether successful or not. it fails if there is a semaphore on the memory location