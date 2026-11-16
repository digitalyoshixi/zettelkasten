---
tags:
  - web
  - security
---
If a OAuth flow is missing a `state` CSRF token, then it is vulnerable to CSRF attacks.
![[OAuth Missing CSRF Protections-20261116012251927.webp]]
https://portswigger.net/web-security/oauth/lab-oauth-forced-oauth-profile-linking