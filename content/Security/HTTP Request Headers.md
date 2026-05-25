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
```
# HSTS & Strict-Transport-Security
Forces browsers to always use HTTPS for your domain
```
Strict-Transport-Security
max-age=3160000, includeSubDomains
```
# X-Content-Type-Options
```
X-Content-Type-Options: nosniff
```
# Referrer-Policy
Controls how much referrer information is sent with requests to improve privacy
# Content-Type
Can be:
- `application/x-www-form-urlencoded` for single parameter
- `multipart/form-data` for multiple fields, form data input, can add a [[Binary Large Object|BLOB]] too