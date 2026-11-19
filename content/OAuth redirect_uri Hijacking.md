---
tags:
  - web
  - security
---
An attack against OAuth systems where the redirect_uri can overwritten to be a user defined value.
- The subsequent OAuth token is then sent directly to the attacker's machine
# Filter Bypass Techniques
- Add or remove paths, query parameters, [[Fragment Identifier]]
- Try [[HTTP Parameter Pollution|Server Side Parameter Pollution]]
- Path traversal `https://client-app.com/oauth/callback/../../example/path`
- Look for open redirects if it restricts specific domains
# Example
A request allows setting your own redirect_uri.
![[OAuth redirect_uri Hijacking-20261119012223491.webp]]