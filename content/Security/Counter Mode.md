---
tags:
  - security
  - cryptography
aliases:
  - CTR
  - CTM
---
A [[Block-Cipher]] mode that uses a counter and [[Initialization Vector|IV]]. Does not encrypt plaintext, but encrypts counter.
Used to generate a stream of [[Pseudorandom]] blocks.
Does not require padding.
# Pros
- Allows for [[Parallelism]]
# Cons
- Does not have any checks for [[Integrity]]
# Encrypt
![[Counter Mode-20250823165245450.webp]]
# Decrypt
![[Counter Mode-20250823165317618.webp]]