---
tags:
  - security
---
# X-Frame Options
Prevents your site from being embedded in [[IFrame]] on malicious sites
```
X-Frame-Options: DENY
```
# Content-Security-Policy
Defines allowsed sources for scripts, styles and other resources
```
default-src 'self',
s
```
# HSTS
Forces browsers to always use HTTPS for your domain
```
Strict-Transport-Security
max-age=3160000, includeSubDomains
```
# X-Content-Type-Options
```
X-Content-Type-Options: nosniff
```
