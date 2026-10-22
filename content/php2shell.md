---
tags:
  - security
---
A remote code execution vulnerability in PHP versions >5.4.0
# Exploit
- Allocate excessive memory to exceed memory limit leaving stale states that leak memory
- Heap groom to allocate heap of size
- Abuse [[Out of Memory Killer|OOMKiller]]