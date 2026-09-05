---
tags:
  - security
---
A [[SQLI UNION Attack]] that involves finding the data type of the column that allows a successful union.
# Example
```
' UNION SELECT 'a', NULL, NULL, NULL--
' UNION SELECT NULL, 'a', NULL, NULL--
```
Will error something like: `Conversion failed when converting the varchar value 'a' to data type int`