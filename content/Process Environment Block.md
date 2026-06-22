---
tags:
  - windows
  - security
aliases:
  - PEB
---
The structure of a [[Windows Process]] being used by programs. Contains:
- Process name
- Current directory
- Loaded [[Dynamic Linked Library|DLL]]
- Memory regions
- Threads
# Struct
```c
typedef struct _PEB {
  BYTE                          Reserved1[2];
  BYTE                          BeingDebugged;
  BYTE                          Reserved2[1];
  PVOID                         Reserved3[2];
  PPEB_LDR_DATA                 Ldr;
  PRTL_USER_PROCESS_PARAMETERS  ProcessParameters;
  PVOID                         Reserved4[3];
  PVOID                         AtlThunkSListPtr;
  PVOID                         Reserved5;
  ULONG                         Reserved6;
  PVOID                         Reserved7;
  ULONG                         Reserved8;
  ULONG                         AtlThunkSListPtr32;
  PVOID                         Reserved9[45];
  BYTE                          Reserved10[96];
  PPS_POST_PROCESS_INIT_ROUTINE PostProcessInitRoutine;
  BYTE                          Reserved11[128];
  PVOID                         Reserved12[1];
  ULONG                         SessionId;
} PEB, *PPEB;
```
- `BeingDebugged` is a boolean indicating whether process is being debugged or not
- `Ldr` is a pointer to [[PEB_LDR_DATA]] that stores information about the process' [[Dynamic Linked Library|DLL]] modules
- `ProcessParameters` is a [[RTL_USER_PROCESS_PARAMETERS]] data structure containing command line arguments
- `AtlThunkSListPtr`/`AtlThunkSListPtr32` are used to point to a [[Linked List]] of [[Windows Thunking Functions]]
- `PostProcessRoutine` used to store a pointer called by the operating system
# Techniques
- [[Getting PEB Address]]
# Blogs
- https://ntopcode.wordpress.com/2018/02/26/anatomy-of-the-process-environment-block-peb-windows-internals/ 