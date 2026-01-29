---
tags:
  - binary_exploitation
  - security
aliases:
  - tcache
---
Thread local caching in [[ptmalloc]] used to speed up repeated allocations in a single thread.
Implemented as a singly [[Linked List]]
```
typedef struct tcache_perthread_struct
{
	char counts[TCACHE_MAX_BINS];
	tcache_entry *entries[TCACHE_MAX_BINS];
} tcache_perthread_struct;
```