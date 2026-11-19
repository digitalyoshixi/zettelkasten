---
tags:
  - web
  - security
---
An attack where a custom [[JSON Web Key]] is embedded as a header representing the public key to verify as. If the server accepts this public key, then you can sign any JSON web token.
# Attack with [[JWT Editor]]
Embedded JWK attack
![[JWT Embedded JWK Attack-20261119034838445.webp|713]]
Then make sure to sign it with your key