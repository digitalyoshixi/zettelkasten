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
typedef struct _PEB_LDR_DATA
{
     ULONG Length;									// offset 0x00
     UCHAR Initialized;								// offset 0x04
     PVOID SsHandle;								// offset 0x08
     LIST_ENTRY InLoadOrderModuleList;				// offset 0x10
     LIST_ENTRY InMemoryOrderModuleList;			// offset 0x20
     LIST_ENTRY InInitializationOrderModuleList;	// offset 0x30
     PVOID EntryInProgress;							// offset 0x40
} PEB_LDR_DATA, *PPEB_LDR_DATA;

```
# Module Lists
Each list is a [[Embedded Doubly Linked Lists]].
- InLoadOrderModuleList : Order modules are loaded by the module loader. Program is often first, then [[NTDLL]]
- InMemoryOrderModuleList : Modules ordered by actual placement in RAM address space
- InInitializationOrderModuleList: Modules ordered by ones initialized with [[DLLMain]]