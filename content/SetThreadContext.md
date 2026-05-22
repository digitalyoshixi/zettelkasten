---
tags:
  - windows
  - win32api
  - programming
---
Sets the context of a particular thread
```c
BOOL SetThreadContext(
  [in] HANDLE        hThread,
  [in] const CONTEXT *lpContext
);
```