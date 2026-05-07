---
tags:
  - security
aliases:
  - SQLI View Columns
---
# View Tables [[MySQL]], [[PostgreSQL]], Microsoft
```
SELECT * FROM information_schema.tables
```
# View Columns [[MySQL]], [[PostgreSQL]], Microsoft
```
SELECT * FROM information_schema.columns WHERE table_name = 'users'
```
