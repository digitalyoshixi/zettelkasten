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
- Cant be revoked
# Structure
### Header
- alg: the hashing algorithm
- typ: the JWT type
### Payload
##### Claims (User Data)
- sub: user identifier
- exp: token expirt
- iat: when token was created (issued at)
- aud: indended recipient API, service
- iss: who issued the token
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
# Cracking
- [[JWT Cracking Guide]]