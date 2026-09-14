---
tags:
  - programming
  - win32api
  - windows
  - malware
  - security
---
# Code

# Explanation
1. Call [[CreateToolhelp32Snapshot]] to get the snapshot of processes currently running on the system
```c
// Takes a snapshot of the currently running processes 
hSnapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);

if (hSnapshot == INVALID_HANDLE_VALUE)
{
    printf("[!] CreateToolhelp32Snapshot Failed With Error: %lu\n", GetLastError());
    return FALSE;
}
```
2. [[Process32First]] is used to get the first process in the snapshot, [[Process32Next]] is used to get the next processes
3. Parse the [[PROCESSENTRY32]] fields
	1. `th32ProcessID` : PID
	2. `th32ParentProcessID` : PID of parent process
