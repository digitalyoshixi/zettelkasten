---
tags:
  - programming
  - os
---
A [[Allocator]] that uses a list of same size slots.
- All allocations must be smaller than one slot
- Uses a [[Bitmap]] to represent available slots
- Frees by clearing a bit in the bitmap
- Slow if using a [[Linked List]]