---
tags:
  - memory
  - os
---
*The stack grows up negatively*
https://www.youtube.com/watch?v=CRTR5ljBjPM
Organized memory where program data resides. ALL data is stored in the stack excluding those that are in registers(will eventually go to the stack).
# Stack Frame
Portion created between ebp and esp
![[Stack-20231217010052509.webp]]

# LIFO(Last in First out)
Stack is like this
![[Stack-20231217005252673.webp]]
If we add(push):
- ESP decreases, a value is added to the stack
![[Stack-20231217005435298.webp|555]]
If we remove(pop):
- ESP increases, effectively forgetting about the highest value
![[Stack-20231217005550288.webp]]






