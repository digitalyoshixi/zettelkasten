---
tags:
  - security
  - web
aliases:
  - CGI
---
A interface to allow [[Web Server]] to execute programs to process [[Hyper Text Transfer Protocol|HTTP]] requests.
Often used with [[PHP]].
- Forking a process from disk is slow, this is fixed with [[FastCGI]]
![[Common Gateway Interface-20260927185154405.webp|380]]
# Process
1. Fork the webserver process so it has context of environment variables
2. Read request body
3. Return response in script's stdouit
4. Kill process