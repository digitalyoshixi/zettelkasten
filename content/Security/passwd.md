---
tags:
  - linux
aliases:
  - /etc/passwd
---
This is the file that stores user information.
```
username:x:uid:gid:useridinfo:homedir:shelldir
```
- First field is username
- Second field is encrypted flag, `x` indicates encrypted and stored in [[shadow|etc/shadow]]
- Third field is [[UID]]
- Fourth field is [[Group ID]]
- Fifth field is [[UID]] info
	- Full name, phone numer, etc used by [[finger]]
- Sixth field is home directory
- 7th field is path for shell