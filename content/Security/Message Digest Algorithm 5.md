---
tags:
  - security
aliases:
  - MD5
---
This is a [[Hashing]] algorithm that is most commonly used for image files.
**Not Secure** for sensitive data.
# Algorithm
- Takes in 512-bit (64-byte) input (can be [[PKCS 7|Padded]])
- Returns 128-bit (16-byte) output
1. Given a 512-bit (64-byte) input
2. Given hardcoded starting state:
	1. $a= \text{0x67452301}$
	2. $b= \text{0xefcdab89}$
	3. $c= \text{0x98badcfe}$
	4. $d= \text{0x10325476}$
3. Denote the next state $a',b',c',d'$
	1. $a' = d$
	2. $b' = \text{combine}(a,b,c,d)$
	3. $c' = a$
	4. $d' = c$