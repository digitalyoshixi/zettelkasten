---
tags:
  - math
  - cryptography
---
A step in [[Advanced Encryption Standard|AES]]
# Process
1. Given a $4 \times 4$ matrix representing the state 
2. Each column of bytes treated as a polynomial $b_{3}x^{3} + b_{2}x^{2}+b_{1}x+b_{0}$ with each byte in the [[Finite Field|Galois Field]] $128$, coefficients in prime sub-[[Finite Field|Galois Field]] $2$
3. Each column is multiplied with fixed polynomial $a(x)=3x^{3}+x^2+x+2$ module $x^{4}+1$
# Video
- https://invidious.yoshixi.net/watch?v=Tpq8X3ZibZA
# Implementation
```python
def mix_single_column(a):
    # see Sec 4.1.2 in The Design of Rijndael
    t = a[0] ^ a[1] ^ a[2] ^ a[3]
    u = a[0]
    a[0] ^= t ^ xtime(a[0] ^ a[1])
    a[1] ^= t ^ xtime(a[1] ^ a[2])
    a[2] ^= t ^ xtime(a[2] ^ a[3])
    a[3] ^= t ^ xtime(a[3] ^ u)


def mix_columns(s):
    for i in range(4):
        mix_single_column(s[i])


def inv_mix_columns(s):
    # see Sec 4.1.3 in The Design of Rijndael
    for i in range(4):
        u = xtime(xtime(s[i][0] ^ s[i][2]))
        v = xtime(xtime(s[i][1] ^ s[i][3]))
        s[i][0] ^= u
        s[i][1] ^= v
        s[i][2] ^= u
        s[i][3] ^= v

    mix_columns(s)
```