---
tags:
  - web
  - security
---
An attack against OAuth providers that allow dynamic client registration. An attacker can register their own client application which can potentially:
- Lead to [[Server Side Request Forgery|SSRF]] in the whitelisted redirect URIs
- Overwrite an existing client's configuration