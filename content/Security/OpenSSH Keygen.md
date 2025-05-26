---
tags:
  - cryptography
  - security
---
# Generating Key
### RSA (Dont Use)
```
ssh-keygen -t rsa -b 4096
```
### Generating ECDSA
```
ssh-keygen -t ed25519
```

# Signing a Certificate
```
ssh-keygen -s id_ed25519 -I my-ca.pem -h -V +52w id_ed25519.pub
```