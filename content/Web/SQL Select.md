---
tags:
  - database
aliases:
  - SQL UNION
  - SQL Union
---
![[SQL Select-20241003040502356.webp]]
selects and gets an item from a table
![[Structured Query Language-20240802195210682.webp]]
# Union Select
```
SELECT a,b FROM table1 UNION SELECT c, d FROM table2
```
Returns a single result set of both select queries.
- Both queries must return same number of columns
- Returned items must be the same comparable data type
![[SQL Select-20260501213509908.webp]]