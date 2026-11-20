---
tags:
  - web
aliases:
  - JWT Token
  - Json Web Signature
  - JWS
---
Tokens used as signatures for asserting certain claims.
For example, a server could generate a token that claims "logged in as administrator" and provide that to a client. The client uses this token to claim that they are logged in as administrator.
![[JSON Web Token-20250426010314700.webp]]
JWT claims can be passed around as identification to bypass authentication by identity providers or service providers.
- Cant be revoked
# Structure
### Header
- `alg`: the hashing algorithm
	- `HS256`: [[Hash-based Message Authentication Code|HMAC]] + [[SHA256]]
	- `RS256`: 
	- `none` : not signed at all
- `typ`: If its JWT or JWE
##### JOSE Headers
- `jwk` ([[JSON Web Key]]): Embedded JSON object representing the key
- `jku` ([[JSON Web Key Set URL]]): URL from which servers can fetch a set of keys containing the correct key
- `kid` (Key ID): ID that servers can use to identify the correct key
### Payload
##### Claims (User Data)
- `sub`: user identifier - `exp`: token expiry
- `iat`: when token was created (issued at)
- `aud`: indended recipient API, service
- `iss`: who issued the token
# Token Lifecycle
Since JWT does not update session for client, the client must frequently get new tokens. It has an identity token (refresh token) and access token.
### Access Tokens
- Used for API requests, short expiry limits exposure (15mins)
- Usually, you define role, perms, everything required
- When access token used up, call the refresh endpoint which returns a new access token
### Refresh Tokens
- Used to get access to new tokens, rotated on each use (7 days)
- Contains the sub, expirty date, issued at, etc
# JWT Common Pitfalls
Non-implemented security things in JWT:
- Missing exp claim
- Stored in [[Javascript Local Storage]]
- No refresh rotation, no new tokens are generated
- Not invalidated on logout
# Concepts
- [[JSON Web Encryption]]
- [[jsonwebtoken]]
### Security
- [[JWT Editor]]
- [[JWT Bypass via Missing Signature Validation]]
- [[JWT Bypass via none Signature Acceptance]]
- [[JWT Cracking Guide]]
- [[JWT Embedded JWK Attack]]
- [[JWT Owned JKU Domain Attack]]
- [[JWT kid From Path Attack]]