---
tags:
  - security
  - binary_exploitation
---
A heap attack that uses [[Use After Free|UAF]] to overwrite metadata of a [[Tcache Bin]] to point to a stack address that we can retrieve from a subsequent [[C malloc|malloc]]
# Example
1. Malloc two times to get [[Heap Chunk]]
   ![[Tcache Poisoning-20260129051910303.webp]]
2. Free these two chunks to get them into the [[Tcache Bin]] free list
   ![[Tcache Poisoning-20260129051941734.webp]]
3. Use [[Use After Free|UAF]] to corrupt B's metadata
   ![[Tcache Poisoning-20260129051959742.webp]]
4. Allocate a chunk, and get B, allocate another chunks and you get the stack's address
   ![[Tcache Poisoning-20260129052024198.webp]]
# Defenses
- [[Safe Linking]]