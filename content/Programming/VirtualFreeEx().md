---
tags:
  - programming
  - windows
  - win32api
---
A remote counterpart of [[VirtualFree]]
```c
BOOL VirtualFreeEx(
  [in] HANDLE hProcess,
  [in] LPVOID lpAddress,
  [in] SIZE_T dwSize,
  [in] DWORD  dwFreeType
);
```