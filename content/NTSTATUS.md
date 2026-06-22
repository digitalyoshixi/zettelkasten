---
tags:
  - windows
---
A 32-bit unsigned integer used to represent the status of a system call or function.
- `0` : `STATUS_SUCCESS`
- Non-zero values, refer to https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-erref/596a1078-e883-4972-9bbc-49e60bebca55
# NT_SUCCESS Macro
```c
#define NT_SUCCESS(Status) (((NTSTATUS)(Status)) >= 0)
```

# Checking
```c
NTSTATUS STATUS = NativeSyscallExample(...);
if (!NT_SUCCESS(STATUS)){
    // printing the error in unsigned integer hexadecimal format
    printf("[!] NativeSyscallExample Failed With Status : 0x%0.8X \n", STATUS); 
}

// NativeSyscallExample succeeded
```