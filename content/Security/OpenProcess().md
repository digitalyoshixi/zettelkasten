---
tags:
  - windows
  - security
---
Used to open an existing process [[Handle]] by its [[Process ID|PID]].
```c
HANDLE OpenProcess(
  [in] DWORD dwDesiredAccess,
  [in] BOOL  bInheritHandle,
  [in] DWORD dwProcessId
);
```