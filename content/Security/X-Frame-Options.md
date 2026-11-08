---
tags:
  - security
  - web
---
HTTP server response header to indicate how other sites can use your site in an [[IFrame]]. 
```
X-Frame-Options: deny
```
- `deny`: Prevent use as an iframe in another site
- `sameorigin`: Allow only if the origin is the same
- `allow-from https://normal-website.com`: Allow only from specific site (not supported in all broswers)