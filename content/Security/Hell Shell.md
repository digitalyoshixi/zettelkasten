---
tags:
  - malware
  - security
aliases:
  - HellShell
---
A tool to automatically encrypt and encode payloads.
- Supports [[XOR cipher|XOR Encryption]], [[Rivest Cipher 4|RC4]], [[Advanced Encryption Standard|AES]]
- Supports [[IPv4 Obfuscation|IPv4Fuscation]], [[IPv6 Obfuscation|IPv6Fuscation]], [[MAC Obfuscation]], [[UUID Obfuscation]]
# Usage
```
HellShell.exe <Input Payload FileName> <Enc/Obf Method>
```
### Encryption Obfuscation Methods
- `"mac"`
- `"ipv4"`
- `"ipv6"`
- `"uuid"`
- `"aes"`
- `"rc4"`