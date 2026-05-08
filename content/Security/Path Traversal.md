---
tags:
  - security
aliases:
  - Directory Traversal
  - File Inclusion
  - Local File Inclusion
---
A [[Web Security]] vulnerability targets webservers who's paths allow direct traversal with unregulated logic.
# Common Paths
- `/etc/passwd`
- `/etc/shadow`
- `/etc`
- `/var/www/html`
- `../`
- `/root`
- `%00` : null byte
- `%2f` : `/`
- `%2e` : `.`
# Prevention
- Setup input sanitization
- Setup [[Stored Procedures]]