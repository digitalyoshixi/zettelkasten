---
tags:
  - os
  - memory
---
The segments of the heap that can be used.
```c
struct malloc_chunk {
  INTERNAL_SIZE_T      mchunk_prev_size;  /* Size of previous chunk, if it is free. */
  INTERNAL_SIZE_T      mchunk_size;       /* Size in bytes, including overhead. */
  struct malloc_chunk* fd;                /* double links -- used only if this chunk is free. */
  struct malloc_chunk* bk;
  /* Only used for large blocks: pointer to next larger size.  */
  struct malloc_chunk* fd_nextsize; /* double links -- used only if this chunk is free. */
  struct malloc_chunk* bk_nextsize;
};

typedef struct malloc_chunk* mchunkptr;
```
# Types
### In-use Chunk
The current program segment is being used
![[Heap Chunk-20260123035540957.webp]]
### Free Chunk
The current program segment has been freed
![[Heap Chunk-20260129044607261.webp]]