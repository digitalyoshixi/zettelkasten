---
tags:
  - web
  - security
  - php
---
A outdated security that introduces a function `addslashes` to [[Input Escaping|Escape]]:
- Single quote
- Double quote
- Null
# Problems
Developers used this as a silver bullet, but it neglected certain escape rules:
- Databases need a different escaping method
	- `my_sql_real_escape_string` for [[MySQL]]
	- `pg_escape_string` for [[PostgreSQL]]
- SQL is not the only thing needed to escape