---
tags:
  - cryptography
  - networking
aliases:
  - SSH
---
A protocol to open a shell in a remote device.
Found on port `tcp/22`.
- Establishes secure sessions with cryptographic algorithms. Commonly [[RSA]]
# Protocol

# SSH Encryption
SSH is secure because it uses public/private keys to encrypt and decrypt data.
### SSH Key
An SSH key is often a 256 byte file that contains symbols used to encrypt/decrypt data.
You can create a key with [[OpenSSH]]
- [[OpenSSH Keygen]]
# Guides
- [[OpenSSH Keygen]]
- [[SSH Port Forwarding]]
- [[OpenSSH SOCKS5 Proxy]]