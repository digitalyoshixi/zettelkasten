---
tags:
  - web
---
A [[Web Server]] or [[Reverse Proxy]] for exposing local web servers to the internet.
- High performant
- Stable
- Efficient
# Configuration File Setup
1. `vim /etc/nginx/nginx.conf` to change which sites to use
2. `vim /etc/nginx/sites-avaiable/default` to change the default site
# Viewing Errors
```
tail -f /var/log/nginx/error.log
```
# Concepts
- [[nginx.conf]]
# Guides
- [[nginx Serve Website]]
# Reverse Proxy Configuration
![[nginx-20250429211000212.webp]]