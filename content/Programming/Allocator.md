---
tags:
  - programming
---
Methods that manage memory for a program.
- Allocation
- Deallocation
Often handles an [[Arena]].
Can be wrapped in a [[Container Allocator]]
# Custom Allocator Benefits
- Cheaper Allocation/Free cost (malloc over allocates)
- Custom [[Locality of Reference|Memory Locality]] logic (CPU cache rather than RAM)
- Reduced [[Fragmentation]]
# List
- [[Linear Allocator]]
- [[Heap Allocator]]
- [[Stack Allocator]]
- [[Pool Allocator]]
- [[Buddy Allocator]]
- [[Slab Allocator]]
# Resources
- https://www.youtube.com/watch?v=TDCwoAuL5jc
- https://gamedev.net/blogs/entry/2271578-introduction-to-allocators-and-arenas/
- https://wiki.osdev.org/Page_Frame_Allocation