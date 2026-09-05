---
tags:
  - security
  - web
aliases:
  - CSP
---
A standard that can be set by websites to prevent attacks like [[Cross Site Scripting|XSS]] by restricting sources of content a browser can load.
# Example
```
script-src 'self'
```
- Ensures script only load from same origin as self
```
script-src http://scripts.normal-website.com
```
- Ensures script can load from alternate origin
```
script-src 'self' 'unsafe-inline' 'unsafe-eval'
```
- Allows execution of unsafe in page scripts,unsafe into DOM APIs like [[Javascript eval()]]
# Secure CSP
```
default-src 'self';
form-action 'self';
base-uri 'self';
object-src 'none';
frame-ancestors 'none';
upgrade-insecure-requets;
block-all-mixed-content;
```