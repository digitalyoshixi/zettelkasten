---
tags:
  - security
aliases:
  - HTTP Request Smuggling
  - HTTP Response Splitting
  - HRS
cssclasses:
---
A usage of  `\r\n` to add additional requests to be executed by a bad HTTP parser.
Can also be used to forward requests for multi-proxy setups.
As a HTTP header:
```
foo: bar\r\nGET / HTTP/1.1\r\nHost: www.yoshixi.net
```
![[HTTP Smuggling-20260628202910913.webp]]
![[HTTP Smuggling-20260628202927834.webp]]