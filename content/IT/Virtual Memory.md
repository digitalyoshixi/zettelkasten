---
tags:
  - memory
aliases:
  - Swap
---
When [[Random Access Memory|RAM]] capacity is at its limit, a portion of [[Hard Drive|HDD]]/[[Solid State Drive|SSD]] space is used to store volatile data.
Swap should almost never be used as it is slow and can cause excessive hard drive usage known as disk thrashing. Just get more RAM
# Process
![[Virtual Memory-20240524053746233.webp|665]]
1. A new process wants to load, but there is not enough free RAM for it
2. A offscreen process(es) are unloaded from RAM and copied into a [[Page File]] saved to the hard drive
3. When you need the offscreen process(es) they are loaded into memory quickly, then unloaded, then reloaded. This is the swap

