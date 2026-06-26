---
tags:
  - security
---
The process of turning references in [[Binary File]] code into back into [[Symbol|Symbols]].
Often done during instrumentation where you must differentiate which addresses have to be relocated and which dont need to:
- [[RData Section|rodata]]: must relocate
- [[x86 jmp]] point: must relocate
- File offset, hash, pixel value: must not update
- Integer constant: must not update