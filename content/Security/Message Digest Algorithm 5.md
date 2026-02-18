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