---
tags:
  - web
  - security
---
A technique for SQLI that involves setting the next part of the query to be a comment:
```
SELECT * FROM products WHERE category = 'Gifts'--' AND released = 1
```