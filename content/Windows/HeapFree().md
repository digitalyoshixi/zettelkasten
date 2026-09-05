---
tags:
  - windows
  - win32api
---
```c
BOOL HeapFree(
  [in] HANDLE                 hHeap,
  [in] DWORD                  dwFlags,
  [in] _Frees_ptr_opt_ LPVOID lpMem
);
```
Frees a allocated memory region.