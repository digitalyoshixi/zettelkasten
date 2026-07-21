---
tags:
  - windows
---
A table entry in [[PEB_LDR_DATA]]'s 
```
LDR_DATA_TABLE_ENTRY
├── InMemoryOrderLinks      (offset 0x00)  –  LIST_ENTRY (Flink, Blink)
├── ...
├── DllBase                 (offset 0x20)  –  base address of the module in memory
├── ...
├── BaseDllName             (offset 0x58)  –  UNICODE_STRING (file name)
└── ...
```