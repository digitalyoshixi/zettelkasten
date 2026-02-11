---
tags:
  - math
  - cryptography
---
A step in [[Advanced Encryption Standard|AES]]
# Implementation
```python
state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


def add_round_key(s, k):
    retmat = []
    for l in range(len(s)):
        retls = []
        for v in range(len(s[l])):
            retls.append(s[l][v] ^ k[l][v])
        retmat.append(retls)
    return retmat

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    retlist = []
    for l in matrix:
        retlist.extend(l)
    return retlist


print("".join(chr(x) for x in matrix2bytes(add_round_key(state, round_key))))


```