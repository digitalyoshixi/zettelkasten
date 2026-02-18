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
import binascii
from datetime import datetime, timedelta

def send_req(msg : str) -> str:
    r = requests.get(f'https://aes.cryptohack.org/ecbcbcwtf/decrypt/{msg}/')
    if r.status_code == 200:
        return r.json()['plaintext']
    else:
        return ""

def xor_bytes(one : bytes, two : bytes) -> bytes:
    return bytes(a ^ b for (a, b) in zip(one, two))

def bytes_to_bitstring(b : bytes) -> str:
	return ''.join(f"{byte:08b}" for byte in b)

def bitstring_to_bytes(s):
    integer_value = int(s, 2)
    byte_length = (len(s) + 7) // 8
    return integer_value.to_bytes(byte_length, byteorder='big')

def hexstring_to_bytes(hexstr : str) -> bytes:
    return bytes.fromhex(hexstr)

def bytes_to_hexstring(b : bytes) -> str:
    return binascii.hexlify(b).decode('utf-8')
    
def xor_hexstring(one : str, two : str) -> str:
    return bytes_to_hexstring(xor_bytes(hexstring_to_bytes(one), hexstring_to_bytes(two)))

```