---
tags:
  - security
aliases:
  - OAuth
---
Similar to [[OpenID]].
When a user logs in with OAuth, they recieve a token to use for verification against SSO services.
- Github OAuth
- Discord sign-in
# Process
1. Access token for API calls (short-lived)
2. Refresh token for renewal (long-lived)
# Requesting OAuth
- You go to the providers website
- The provider gives you a redirect URI that you can set after authentication to redirect to your own site
- Provider gives you a link for their own OAuth portal + info about your site, you can put this link in a button and say 'Login with X'
# Security Pitfalls
- Open redirect [[Universal Resource Locator|URI]], somebody does [[Cross Site Scripting|XSS]] and changes the redirect [[Universal Resource Locator|URI]] to the attacker's server. Ensure there is a whitelist of URIs
- Leaked client secrets in github repo, etc
- Improper token storage in local Storage
- No refresh token rotation