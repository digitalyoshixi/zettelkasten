---
tags:
  - os
  - memory
  - programming
  - c
---
Memory that is allocated during compile time. During execution, this memory cannot be increased or decreased. There are a few problems. 
- Memory will be wasted if allocated memory is more then is stored
- Adding more than stored may lead to program crashes or [[Stack Overflow]]

the alternative to this is [[Dynamic Memory Allocation]]