---
tags:
  - windows
  - security
---
A function to open a thread based off its thread ID
```c
HANDLE OpenThread(
  [in] DWORD dwDesiredAccess,
  [in] BOOL  bInheritHandle,
  [in] DWORD dwThreadId
);
```