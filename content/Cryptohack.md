---
tags:
  - cryptography
---
A website teaching [[Cryptography]].
# Default Boilerplate Script
```python
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import requests
import os

def send_req(msg : str) -> str:
    r = requests.get(f'https://aes.cryptohack.org/ecbcbcwtf/decrypt/{msg}/')
    if r.status_code == 200:
        return r.json()['plaintext']
    else:
        return ""

def xor_bytes(one : bytes, two : bytes) -> bytes:
    return bytes(a ^ b for (a, b) in zip(one, two))

def hextobytes(hexstr : str) -> bytes:
    return bytes.fromhex(hexstr)

```