---
tags:
  - web
  - security
aliases:
  - ETag
---
A HTTP response header indicating an ID of a file on the server.
Used for optimization purposes in pair with [[If-None-Match]]
```
Etag: W/"3683-IwLoHx9rejeu5pzfs+mllFidepk"
```
# Information Leaks
- ETag contains [[Inode]] size ([[CVE-2003-1418]])