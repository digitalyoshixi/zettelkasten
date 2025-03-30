---
tags:
  - c
  - reverse_engineering
---
A function called before main is ran in a [[C]] program.
It will:
- Save registers
- Move arguments 
- Setup stack frame
- Store address of main
- Register a cxa_atexit
- dl_audit_preinit for dynamic linking