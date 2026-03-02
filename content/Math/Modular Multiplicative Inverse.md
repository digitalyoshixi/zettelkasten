---
tags:
  - math
  - cryptography
---
# Definition
$ax \equiv 1 (\mod m)$
- $a$ and $x$ are modular multiplicative inverses of eachother
# Algorithm using [[Division Algorithm for Integers|Extended Euclidean Algorithm]]
We must find integers $a, m$ where $\text{GCD}(a,m) = 1$. We do this with back substitution.
```python
import math
def xgcd(a, b, s1 = 1, s2 = 0, t1 = 0, t2 = 1):
   """ Calculates the gcd and Bezout coefficients, 
   using the Extended Euclidean Algorithm (recursive).
   (Source: extendedeuclideanalgorithm.com/code) 
   """
   if(b == 0):
      return abs(a), 1, 0
   
   q = math.floor(a/b)
   r = a - q * b
   s3 = s1 - q * s2
   t3 = t1 - q * t2
   
   #if r==0, then b will be the gcd and s2, t2 the Bezout coefficients
   return (abs(b), s2, t2) if (r == 0) else xgcd(b, r, s2, s3, t2, t3)

def multinv(b, n):
   """
   Calculates the multiplicative inverse of a number b mod n,
   using the Extended Euclidean Algorithm. If b does not have a
   multiplicative inverse mod n, then throw an exception.
   (Source: extendedeuclideanalgorithm.com/code)
   """
   
   #Get the gcd and the second Bezout coefficient (t)
   #from the Extended Euclidean Algorithm. (We don't need s)
   my_gcd, _, t = xgcd(n, b)
   
   #It only has a multiplicative inverse if the gcd is 1
   if(my_gcd == 1):
      return t % n
   else:
      raise ValueError('{} has no multiplicative inverse modulo {}'.format(b, n))
```