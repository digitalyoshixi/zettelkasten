---
tags:
  - linux
  - security
---
Abusing [[OpenSSH]] on linux systems for persistence.
```
/etc/ssh
```
- Attackers add their own [[Secure Shell Protocol|SSH]] keys
- Attackers change authentication methods allowed
# Checking Connected Hosts
```
~/.ssh
```
contains list of all known hosts that have connected in the past that are hashed.