---
tags:
  - security
aliases:
  - CBC
---
This is a mode for typical [[Block-Cipher|Block Ciphers]] to work with larger plaintexts.
- Same key used for each block
- Previous output used in encryption process of next block
- Requires generation of a [[Initialization Vector]].
# Pros
- The [[Initialization Vector|IV]] can be used for authentication as it is given to the receiver aswell
# Cons
- No paralellism
- IV must be known
# Encryption
![[Cipher Block Chaining-20260211173344314.webp]]
![[Cipher Block Chaining-20260215233300254.webp]]
# Decryption
![[Cipher Block Chaining-20260215233217279.webp]]
# Attacks
- [[Padding Oracle Attack]]
- [[Security/Padding Oracle On Downgraded Legacy Encryption]]