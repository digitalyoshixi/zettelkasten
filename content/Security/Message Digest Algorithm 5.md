---
tags:
  - security
aliases:
  - MD5
---
This is a [[Hashing]] algorithm that is most commonly used for image files.
- Input size 512-bits
- Output size 128-bits
- 64 rounds
- Collision resistance: $2^{18}$ operations - less than a second on modern computers
- Preimage resistance: $2^{123.4}$ operations
**Not Secure** for sensitive data.
Based off [[Merkle Damgard Construction]]
# Algorithm
![[Message Digest Algorithm 5-20260218210442609.webp]]
- Takes in 512-bit (64-byte) input (can be [[PKCS 7|Padded]])
- Returns 128-bit (16-byte) output
1. Given a 512-bit (64-byte) input, split it into 32-bit (4-byte) [[Binary|Words]], name the list $\text{plaintext}$
2. Given hardcoded starting state:
	1. $a= \text{0x67452301}$
	2. $b= \text{0xefcdab89}$
	3. $c= \text{0x98badcfe}$
	4. $d= \text{0x10325476}$
3. Loop 1: Run for entire list $\text{plaintext}$, (which is 16 times)
	1. Denote the next state $a',b',c',d'$
		1. $a' = d$
		2. $b' = \text{combine}(a,b,c,d) \oplus (\text{plaintext}[i])$
		3. $c' = a$
		4. $d' = c$
	2. Update the state $a=a'$, $b=b'$, $c=c'$, $d=d'$
	3. Update $i=i \% 16$
4. Loop 2: Run for entire list $\text{plaintext}$, (which is 16 times)
	1. Denote the next state $a',b',c',d'$
		1. $a' = d$
		2. $b' = \text{combine}(a,b,c,d) \oplus (\text{plaintext}[i])$
		3. $c' = a$
		4. $d' = c$
	2. Update the state $a=a'$, $b=b'$, $c=c'$, $d=d'$
	3. Update $i=(5i+1) \% 16$
5. Loop 3: Run for entire list $\text{plaintext}$, (which is 16 times)
	1. Same process as loop1/loop 2
	2. Update $i=(3i+5) \% 16$
6. Loop 3: Run for entire list $\text{plaintext}$, (which is 16 times)
	1. Same process as loop1/loop2/loop3
	2. Update $i=(7i) \% 16$
7. The final state $a,b,c,d$ is the result of the MD5 function ($\text{output} = a||b||c||d$)
### Combine Function
```python
def F(B,C,D,i):
	if 0 <= i <= 15:
		return (B & C) | ((~B) & D)
	if 16 <= i <= 31:
		return (D & B) | ((~D) & C)
	if 32 <= i <= 47:
		return B ^ C ^ D
	if 48 <= i <= 63:
		return C ^ (B | (~D))
def combine(A, plaintext, i)
	return redbox(XOR(XOR(A, F(B,C,D,i)), plaintext[i]))

def redbox(inp, i, b):
	return XOR(Rotate(XOR(inp, K[i]), r[i]), b)
```
![[Message Digest Algorithm 5-20260218171555993.webp]]
##### Redbox
![[Message Digest Algorithm 5-20260218181025373.webp]]
- MD5 has a constant array of 64 constants $K[64]$ for additions
- MD5 has a constant array of 64 constants $r[64]$ for rotations
- We take the input, XOR it with $K[i]$, rotate left by $r[i]$, XOR it with $B$
### K Array
```pascal
K[ 0.. 3] := { 0xd76aa478, 0xe8c7b756, 0x242070db, 0xc1bdceee }
K[ 4.. 7] := { 0xf57c0faf, 0x4787c62a, 0xa8304613, 0xfd469501 }
K[ 8..11] := { 0x698098d8, 0x8b44f7af, 0xffff5bb1, 0x895cd7be }
K[12..15] := { 0x6b901122, 0xfd987193, 0xa679438e, 0x49b40821 }
K[16..19] := { 0xf61e2562, 0xc040b340, 0x265e5a51, 0xe9b6c7aa }
K[20..23] := { 0xd62f105d, 0x02441453, 0xd8a1e681, 0xe7d3fbc8 }
K[24..27] := { 0x21e1cde6, 0xc33707d6, 0xf4d50d87, 0x455a14ed }
K[28..31] := { 0xa9e3e905, 0xfcefa3f8, 0x676f02d9, 0x8d2a4c8a }
K[32..35] := { 0xfffa3942, 0x8771f681, 0x6d9d6122, 0xfde5380c }
K[36..39] := { 0xa4beea44, 0x4bdecfa9, 0xf6bb4b60, 0xbebfbc70 }
K[40..43] := { 0x289b7ec6, 0xeaa127fa, 0xd4ef3085, 0x04881d05 }
K[44..47] := { 0xd9d4d039, 0xe6db99e5, 0x1fa27cf8, 0xc4ac5665 }
K[48..51] := { 0xf4292244, 0x432aff97, 0xab9423a7, 0xfc93a039 }
K[52..55] := { 0x655b59c3, 0x8f0ccc92, 0xffeff47d, 0x85845dd1 }
K[56..59] := { 0x6fa87e4f, 0xfe2ce6e0, 0xa3014314, 0x4e0811a1 }
K[60..63] := { 0xf7537e82, 0xbd3af235, 0x2ad7d2bb, 0xeb86d391 }
```
### r/s array
```pascal
s[ 0..15] := { 7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22 }
s[16..31] := { 5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20 }
s[32..47] := { 4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23 }
s[48..63] := { 6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21 }
```
