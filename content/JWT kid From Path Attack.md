---
tags:
  - web
  - security
---
An attack wherein the [[JSON Web Token|JWT Token kid]] field is set to a file path. Can lead to using an arbitrary file as the verification key. Especially vulnerable if the signing algorithm is symmetric.

```
{ "kid": "../../../../../dev//null", "typ": "JWT", "alg": "HS256", "k": "asGsADas3421-dfh9DGN-AFDFDbasfd8-anfjkvc" }
```
- `/dev/null` is empty, then you can just sign with an empty signature