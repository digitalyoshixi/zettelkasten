---
tags:
  - security
aliases:
  - Directory Traversal
---
A [[Web Security]] vulnerability targets webservers who's paths allow direct traversal with unregulated logic.
# Common Paths
- `/etc/passwd`
- `/etc/shadow`
- `/etc`
- `/var/www/html`
- `../`
- `/root`
# Prevention
- Setup input sanitization
- Setup [[Stored Procedures]]