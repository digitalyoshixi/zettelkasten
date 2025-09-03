---
tags:
  - os
---
This is the portion created between [[rbp]] and [[rsp]]
![[Stack-20231217010052509.webp]]
Used to encapsulate the scope during a function call.
Stores locals and saved registers.
![[Stack Frame-20250829230239682.webp]]
- Local variables are a negative offset from `ebp`
- Arguments are a positive offset from `ebp`