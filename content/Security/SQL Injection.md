---
tags:
  - security
aliases:
  - SQLI
---
A [[Security Vulnerability|Vulnerability]] that exists when input validation for [[Structured Query Language|SQL]] queries allows breaking of input to access sensitive databases.
https://book.hacktricks.wiki/en/pentesting-web/sql-injection/index.html
# Locations
- `UPDATE` statements within values of the `WHERE` clause
- `INSERT` statements within the inserted values
- `SELECT` statements within the table/column name
- `SELECT` statements within the `ORDER BY` clause
# Payloads
```
' OR '1'='1' --
```
# Techniques
- [[SQLI Comments]]
- [[Out-of-Bound Application Security Testing]]