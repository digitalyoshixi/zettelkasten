---
tags:
  - web
---
This stores session information across multiple instances. They are stored client-side in the user's web browser.
Used for temporary information that doesn't matter too much.
# Cookie Security Flags
- HTTPOnly: Prevents javascript visibility ([[Cross Site Scripting|XSS]]), cookies are not stored
- Secure: Prevents cookies from being forwarded unless you use [[Hyper Text Transfer Protocol Secure|HTTPS]]
- CSRF: Prevents cross site request forgery
	- Sites like desmos, google maps that want to be embedded into other sites usually have this disabled