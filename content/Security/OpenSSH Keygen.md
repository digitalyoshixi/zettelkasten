---
tags:
  - cryptography
  - security
---
# Generating Key
```
ssh-keygen -t rsa -b 4096
```
This will be saved at: `~/.ssh/keyname.pub`
### Generating ECDSA
```
ssh-keygen -t ed25519 -b 384 -C "digitalyoshixi@proton.me"
```