---
tags:
  - programming
  - windows
---
A function in [[NTDLL]] that performs a blocking wait until the timeout expires.
# Example
```c
WaitForSingleObject((HANDLE)-1, 0x1000);
```
- Wait in current thread for 4 seconds