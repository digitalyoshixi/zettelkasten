---
tags:
  - cpu
  - security
aliases:
  - NX
  - DEP
---
Memory permissions for segments of memory.
The operating system will mark certain addresses as non-executable meaning that the CPU will not be able to execute these parts of memory.
- NX (linux)
- DEP (windows)
# Permissions
- `PROT_READ` : allows process to read memory
- `PROT_WRITE` : allows process to write memory
- `PROT_EXEC` : allows process to execute memory
# Bypasses
- [[mprotect]]
- [[JIT Spraying]]