---
tags:
  - security
  - cryptography
aliases:
  - ECB
---
A [[Advanced Encryption Standard|AES]] scheme that is not recommended.
Each block is encrypted separately with the same key.
# Pros
+ Can be [[Parallelism|Parallelised]]
+ Good for short messages
# Cons
- Reveals structural information about original data ([[Homomorphic]])
- ![[Electronic Code Book-20260215225520054.webp]]
# Encrypt
![[Electronic Code Block-20250823164639992.webp]]
# Decrypt
![[Electronic Code Block-20250823164700792.webp]]