---
tags:
  - security
aliases:
  - SQLI
---
A [[Security Vulnerability|Vulnerability]] that exists when input validation for [[Structured Query Language|SQL]] queries allows breaking of input to access sensitive databases.
- https://book.hacktricks.wiki/en/pentesting-web/sql-injection/index.html
- https://portswigger.net/web-security/sql-injection/cheat-sheet
# Locations
- `UPDATE` statements within values of the `WHERE` clause
- `INSERT` statements within the inserted values
- `SELECT` statements within the table/column name
- `SELECT` statements within the `ORDER BY` clause
# Example
```
' OR '1'='1' --
```
# Techniques
### Returned SQL
- [[SQLI Comments]]
- [[SQLI UNION Attack]]
- [[SQLI Determining Number of Columns]]
- [[SQLI Determining Column Data Type]]
- [[SQLI Concatenation]]
- [[SQLI Determining Database Type]]
- [[SQLI View Tables]]
### Blind SQL
Unable to see query results, but results change behavior of the site
- [[Blind SQLI Conditional Triggering]]