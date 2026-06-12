---
tags:
  - security
  - web
---
A [[Site Generator]]
- All file uploads go to `/wp-content/uploads/*`
# Getting Version
```
curl -s https://domain.com | grep -i '<meta name="generator"' | grep -o 'WordPress[^"]*'
```
# Endpoints
- `/wp-json/wp/v2/users` (list all users)
- `/wp-json/wp/v2/users/1` (list all users)
- `/wp-content/uploads` (directory listing)
- `/wp-content/themes/default/404.php`
- `/wp-login.php`
- `/wp-login`
- `/wp-login.php?reauth=1&redirect_to=`
- `/wp-admin`
- `/wp-admin.php`
- `/login`
- `/license.txt`
- `/wp-activate.php`
- `/wp-includes`
- Login page enumeration
- `/xmlrpc.php`
# Common Vulnerabilities
- [[Hyperlink Injection]]
- [[Server Side Request Forgery|SSRF]] with `xmlrpc.php`
```http
POST /xmlrpc.php HTTP/1.1
HOST: ...
User-Agent: ...
Content-Length: 68
<methodCall><methodName>system.listMethods</methodName></methodCall>
```
- Brute force with [[Hydra]]