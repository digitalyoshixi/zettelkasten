---
tags:
  - memory
  - os
  - security
aliases:
  - PAGE_NOACCESS
  - PAGE_EXECUTE_READWRITE
  - PAGE_READONLY
---
A 4KB segment of memory.
Often talked about in context to [[Virtual Memory Space]]
# States
- Free: Page is not in use, not accessible to process, can be committed or reserved in the future.
- Reserved: Page reserved for future use. Waiting to be committed.
- Committed: Memory is tied to disk or RAM and can be used. When process terminates, these pages are freed.
# Page Protection Options
- `PAGE_NOACCESS`: Disable access to committed region of pages. Read, write, execute of this page will result in an access violation
- `PAGE_EXECUTE_READWRITE`: Enables read, write, execute, often [[Indicator of Compromise|IOC]]
- `PAGE_READONLY`: Enables read-only access to commited region, writing will cause an access violation