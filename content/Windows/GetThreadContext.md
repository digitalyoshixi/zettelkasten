---
tags:
  - windows
  - win32api
---
Retrieves thread context of specified thread.
```c
BOOL GetThreadContext(
  [in]      HANDLE    hThread,
  [in, out] LPCONTEXT lpContext
);
```