---
tags:
  - security
---
Keys used for:
- Signing
- Authenticating
on unprotected networks.
# Creating A SSH Key
1. `ssh-keygen -t ed25519 -C "davidchenyuhe@proton.me"`. It is ok to not have a password
2. `cat ~/.ssh/<keyname>.pub`. This is your public SSH key
3. `cat ~/.ssh/<keyname>` This is your private key