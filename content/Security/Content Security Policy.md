---
tags:
  - security
  - web
aliases:
  - CSP
  - Content-Security-Policy
---
A standard that sets content security settings for the browser to use.
- Can prevent attacks like [[Cross Site Scripting|XSS]] by restricting sources of content a browser can load
- Can limit [[IFrame]] settings to prevent [[Clickjacking]]
# frame-ancestors
```
frame-ancestors 'none';
```
- All websites can embed this site as an iframe
```
frame-ancestors 'self';
```
- Only the current origin can embed this site as an iframe
```
frame-ancestors normal-website.com;
```
- Only the origin normal-website.com can embed this site as an iframe
# script-src
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