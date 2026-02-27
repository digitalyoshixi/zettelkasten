---
tags:
  - cryptography
---
A method to decrypt [[RSA]].
It is used when the $d$ private key is very small.
# Script
```python
import math

def continued_fraction_expansion(numerator, denominator):
    cf = []
    while denominator:
        a = numerator // denominator
        cf.append(a)
        numerator, denominator = denominator, numerator - a * denominator
    return cf
def convergents_from_cf(cf):
    convergents = []
    for i in range(len(cf)):
        if i == 0:
            convergents.append((cf[0], 1))
        elif i == 1:
            h = cf[0] * cf[1] + 1
            k = cf[1]
            convergents.append((h, k))
        else:
            h1, k1 = convergents[i - 1]
            h2, k2 = convergents[i - 2]
            h = cf[i] * h1 + h2
            k = cf[i] * k1 + k2
            convergents.append((h, k))
    return convergents
def is_perfect_square(n):
    if n < 0:
        return None
    root = int(math.isqrt(n))
    return root if root * root == n else None

def wiener_attack(e, n):
    cf = continued_fraction_expansion(e, n)
    convs = convergents_from_cf(cf)
    for k, d_candidate in convs:
        if k == 0:
            continue
        if (e * d_candidate - 1) % k != 0:
            continue
        phi_candidate = (e * d_candidate - 1) // k
        a = 1
        b = -(n - phi_candidate + 1)
        c = n
        discriminant = b * b - 4 * a * c
        sqrt_discriminant = is_perfect_square(discriminant)
        if sqrt_discriminant is None:
            continue
        x1 = (-b + sqrt_discriminant) // 2
        x2 = (-b - sqrt_discriminant) // 2
        if x1 * x2 == n:
            return d_candidate  # Found the private key!
    return None  # Attack failed
```
