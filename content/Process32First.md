---
tags:
  - programming
  - win32api
  - windows
---
```c
BOOL Process32First(
  [in]      HANDLE           hSnapshot,
  [in, out] LPPROCESSENTRY32 lppe
);
```
- `hSnapshot` can be gotten from [[CreateToolhelp32Snapshot]]
- `lppe` requires a empty [[PROCESSENTRY32]] structure to populate