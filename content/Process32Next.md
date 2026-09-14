---
tags:
  - programming
  - cpp
  - windows
---
```c
BOOL Process32Next(
  [in]  HANDLE           hSnapshot,
  [out] LPPROCESSENTRY32 lppe
);
```
- `hSnapshot` can be gotten from [[CreateToolhelp32Snapshot]]
- `lppe` requires a the previous [[PROCESSENTRY32]] structure (first one is gotten from [[Process32First]])