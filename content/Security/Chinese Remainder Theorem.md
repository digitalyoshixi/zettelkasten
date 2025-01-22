---
tags:
  - cryptography
aliases:
  - CRT
---
A solution to the [[RSA Problem]] where n,e,c are given.
```python
#!/bin/python3
from Crypto.Util.number import *
from factordb.factordb import FactorDB

# ints:
n =    
e =  
c =  

f = FactorDB(n)
f.connect()
factors = f.get_factor_list()

phi = 1
for i in factors:
    phi *= (i-1)

d = inverse(e, phi)
m = pow(c, d, n)

flag = long_to_bytes(m).decode('UTF-8')
print(flag)
```