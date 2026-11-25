---
tags:
  - web
  - security
---
A header indicating that the HTTP request is chunked.
Each chunk starts of the chunk size in hexadecimal followed by a newline, followed by chunk contents, message is terminated by chunk size 0
```
POST /search HTTP/1.1
Host: normal-website.com
Content-Type: application/x-www-form-urlencoded
Transfer-Encoding: chunked

b
q=smuggling
0
```