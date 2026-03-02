---
tags:
  - programming
  - python
  - cryptography
aliases:
  - Python PyCryptodome
  - Python Cryptography
---
A cryptography library for python
# Installation
```
pip install PyCryptodome
```
# Usage
```python
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

KEY = ?
FLAG = ?

def encrypt(plaintext):
    plaintext = bytes.fromhex(plaintext)

    padded = pad(plaintext + FLAG.encode(), 16)
    cipher = AES.new(KEY, AES.MODE_ECB)
    try:
        encrypted = cipher.encrypt(padded)
    except ValueError as e:
        return {"error": str(e)}

    return {"ciphertext": encrypted.hex()}

```
# Common Conversions
- [[Python Convert Hexstring to ASCII Stirng]]
- [[Python XOR Bytes]]
- [[Python Bytes to Hexstring]]
- [[Python Bytes to Bits]]