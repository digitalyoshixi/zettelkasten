---
tags:
  - memory
  - os
aliases:
  - Stack
---
*The stack grows up negatively*. This is because it must have finite space.
The stack has a size is:
- 1MB on [[Windows]]
- 4MB on [[Linux]]
https://www.youtube.com/watch?v=CRTR5ljBjPM
Organized memory where program data resides. Stores:
- Local variables of the active function
- Return address pointer
- Local variables of the caller function and its caller function, so on so forth
# Stack Representations
### C Initial Program Run Stack
![[Stack-20250126163956105.webp]]
### Function Stack
![[Drawing 2025-06-24 20.46.23.excalidraw]]
- Oftentimes, the return address is 4 bytes, so 4 bytes of junk are used as padding
# Concepts
- [[Stack|LIFO]]
- [[Stack Frame]]
- [[Python2 for Crafting Payloads]]