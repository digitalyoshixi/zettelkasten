---
tags:
  - cryptography
---
Say you have 3 nodes that you want to send your data through, like its the TOR network.
![[Commutative Encryption-20240127215346434.webp]]
It must go through node A, then node B, then node C.
Your data was encrypted with 3 keys. Key A, B and C.
When it reaches node A, node A decrypts, when it reaches node B, node B decrypts. so on, so forth.

**It must go through a specific order**

