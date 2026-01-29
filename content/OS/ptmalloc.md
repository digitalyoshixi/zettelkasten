---
tags:
  - memory
aliases:
  - pthreads malloc version 2
---
[[Heap Allocator]] used in some versions of [[C]], derived from [[dlmalloc]].
Uses a [[Data Segment]] with [[brk()]] and [[sbrk()]] to manage memory

# Allocating
ptmalloc slices off bits of the [[Data Segment]] for small allocations and uses [[mmap()]] for large allocations

# Freeing
- ptmalloc checks its mutliple [[Bin|BIns]] (free lists) for their sizes
- When a [[Heap Chunk]] is freed, we don't immediately want to [[Chunk Coalescing|Coalesce]] it, we move it to a [[Tcache Bin]], [[Fast Bin]] or a [[Unsorted Bin]] if none of the others match
- Malloc waits to see if you immediately reuse this chunk, if not, it will sort it into a small or large bin
# Concepts
- [[Bin]]