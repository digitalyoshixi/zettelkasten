---
tags:
  - memory
aliases:
---
A mapping of physical memory in [[Random Access Memory|RAM]] to virtual memory spaces.
- Allows for [[Page File|Swap]]
- Prevents processes from accessing other process memory
- Allows for segmenting of memory to give to processes that wouldn't fit contiguously
![[Virtual Memory-20260322222928240.webp]]
# Aligning via Frames
- Memory is broken into frames which are usually 4KB in size, these are then mapped to virtual memory
![[Virtual Memory-20260322223119855.webp]]