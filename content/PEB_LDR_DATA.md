---
tags:
  - security
  - windows
---
A data structure that notes down:
- DLLs loaded
- DLL loaded addresses
- Size of module
```c
typedef struct _PEB_LDR_DATA {
  BYTE       Reserved1[8];
  PVOID      Reserved2[3];
  LIST_ENTRY InMemoryOrderModuleList;
} PEB_LDR_DATA, *PPEB_LDR_DATA;
```