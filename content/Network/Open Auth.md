---
tags:
  - security
aliases:
  - OAuth
  - OAuth Grant
  - OAuth Flow
---
A way for applications to provide other applications limitated information about a user like:
- Username
- Email contacts
- ...
Seen in services like:
- Discord
- Github
Proper user authentication is provided by [[OpenID]]
# Process
1. Client application requests access to subset of user data through a URI that points to the providers website
2. User clicks the prompt and logs into the OAuth service and provide consent
3. Application recieves:
	1. A access token for API calls (short-lived)
	2. A refresh token for renewal (long-lived)
# Requesting OAuth
- You go to the providers website
- The provider gives you a redirect URI that you can set after authentication to redirect to your own site
- Provider gives you a link for their own OAuth portal + info about your site, you can put this link in a button and say 'Login with X'
# Concepts
- [[OAuth Scope]]
- [[OpenID]]
### Grant Types
- [[OAuth Authorization Code]]
- [[OAuth Implicit Grants]]
# Recon
On the OAuth provider server:
- `/.well-known/oauth-authorization-server`
- `/.well-known/openid-configuration`
# Vulnerabilities
- [[OAuth Authentication Bypass via OAuth Implicit Grants]]
- [[OAuth Missing CSRF Protections]]
- [[OAuth redirect_uri Hijacking]]
- Open redirect [[Universal Resource Locator|URI]], somebody does [[Cross Site Scripting|XSS]] and changes the redirect [[Universal Resource Locator|URI]] to the attacker's server. Ensure there is a whitelist of URIs
- Leaked client secrets in github repo, etc
- Improper token storage in local Storage
- No refresh token rotation