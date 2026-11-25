---
tags:
  - web
  - security
---
Content-Length to trigger HTTP request smuggling.
```
POST /search HTTP/1.1
Host: normal-website.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 11

q=smuggling
```
Specify more or less content in the request.