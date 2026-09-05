---
tags:
  - windows
---
A [[NTDLL]] function for registering a work item in the thread pool.
```c
NTSTATUS NTAPI TpAllocWork(
    PTP_WORK* ptpWrk,
    PTP_WORK_CALLBACK pfnwkCallback,
    PVOID OptionalArg,
    PTP_CALLBACK_ENVIRON CallbackEnvironment
);
```
- Has a maximum of 9 arguments that you can use