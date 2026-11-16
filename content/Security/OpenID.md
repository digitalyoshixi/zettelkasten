---
tags:
  - security
  - networking
aliases:
  - OpenID Connect
---
![[OpenID-20250825000059666.webp|226]]
A [[Decentralized]] protocol used for authentication between cooperating sites. Based off [[Open Auth|OAuth]].
Defines:
- A standard for OAuth scopes
- An additional `id_token` passed between applications
# Terminology
- `Relying party`: Client application that is requesting authentication of a user
- `End user`: User being authenticated
- `OpenID Provider`: OAuth service that supports OpenID Connect
# Concepts
- [[OpenID Claim]]
- [[OpenID Scope]]
- [[OpenID ID Token]]
- [[OpenID Client Registration]]
# Fingerprinting
- Check if OAuth requests include a `openid` scope
- Check route `/.well-known/openid-configuration`
# Vulnerabilities
- [[OpenID Unprotected Client Registration]]
- [[OpenID Unprotected Referenced Scope Requests]]