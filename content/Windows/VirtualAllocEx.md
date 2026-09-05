---
tags:
  - windows
---
VirtualAlloc that is able to allocate memory into a different [[Process]].
Requires a [[Handle]] to that different process.
```c
LPVOID VirtualAllocEx(
  [in]           HANDLE hProcess,
  [in, optional] LPVOID lpAddress,
  [in]           SIZE_T dwSize,
  [in]           DWORD  flAllocationType,
  [in]           DWORD  flProtect
);
```