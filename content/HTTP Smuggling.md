---
tags:
  - security
aliases:
  - HTTP Request Smuggling
  - HTTP Response Splitting
---
A usage of  `\r\n` to add additional requests to be executed by a bad HTTP parser.
As a HTTP header:
```
foo: bar\r\nGET / HTTP/1.1\r\nHost: www.yoshixi.net
```