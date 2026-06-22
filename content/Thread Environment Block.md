---
tags:
  - windows
  - security
aliases:
  - TEB
---
A data structure that stores information about [[Process Control Thread|Threads]] in [[Windows Process]].
```c
typedef struct _TEB {
  PVOID Reserved1[12];
  PPEB  ProcessEnvironmentBlock;
  PVOID Reserved2[399];
  BYTE  Reserved3[1952];
  PVOID TlsSlots[64];
  BYTE  Reserved4[8];
  PVOID Reserved5[26];
  PVOID ReservedForOle;
  PVOID Reserved6[4];
  PVOID TlsExpansionSlots;
} TEB, *PTEB;
```
- `ProcessEnvironmentBlock` is a pointer to [[Process Environment Block|PEB]]
- `TlsSlots` is a collection of writable [[Thread Local Storage|TLS]] slots
- `TlsExpansionSlots` is a collection of [[Thread Local Storage|TLS]] slots reserved for system dlls