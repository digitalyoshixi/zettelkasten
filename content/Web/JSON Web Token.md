---
tags:
  - web
aliases:
  - JWT Token
---
Tokens used as signatures for asserting certain claims.
For example, a server could generate a token that claims "logged in as administrator" and provide that to a client. The client uses this token to claim that they are logged in as administrator.
![[JSON Web Token-20250426010314700.webp]]
JWT claims can be passed around as identification to bypass authentication by identity providers or service providers.
# Cracking
- [[JWT Cracking Guide]]