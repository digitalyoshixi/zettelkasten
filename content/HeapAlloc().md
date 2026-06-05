---
tags:
  - windows
---
```c
DECLSPEC_ALLOCATOR LPVOID HeapAlloc(
  [in] HANDLE hHeap,
  [in] DWORD  dwFlags,
  [in] SIZE_T dwBytes
);
```
# Example
```c
PVOID pAddress = HeapAlloc(GetProcessHeap(), 0, 100);
```
# Flags
- `HEAP_ZERO_MEMORY`: Causes memory allocated to be initialized to zero