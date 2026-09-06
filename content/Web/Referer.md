---
tags:
  - web
---
A [[HTTP Request Header]] often used to denote which website sent the request.
- Misspelled in the original RFC
Used as a primative defense against [[Cross Site Request Forgery|CSRF]].
- Referer can often be spoofed
- Some sites only check substrings of Referer (attacker includes the domain as a subdomain)
- Some sites omit referer validation if not included
# Dropping Referrer With HTML
```
<meta name="referrer" content="never">
```
- Client side requests from this page will never include the `Referer` header