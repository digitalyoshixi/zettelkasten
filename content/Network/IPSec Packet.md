---
tags:
  - networking
---
### Authenticated Header (AH)
Generated from [[SHA-1]] or [[Message Digest Algorithm 5|MD5]] algorithms.
Provides data integrity to ensure packet data is not tampered with.
### Encapsulated Security Payload (ESP)
The section of the IPSec packet where a data is stored.
Often encrypted through:
- [[Data Encryption Standard|DES]]
- [[Triple DES|3DES]]
- [[Advanced Encryption Standard|AES]]
Contains:
- Header
- Payload data
- ESP Trailer (optional) : data for padding or integrity checks