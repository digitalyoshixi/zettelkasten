---
tags:
  - web
---
This stores session information across multiple instances. They are stored client-side in the user's web browser.
Used for temporary information that doesn't matter too much.
# Cookie Security Flags
- `HTTPOnly`: Prevents javascript visibility ([[Cross Site Scripting|XSS]]), cookies are not stored
- `Secure`: Prevents cookies from being forwarded unless you use [[Hyper Text Transfer Protocol Secure|HTTPS]]
- `SameSite`: Prevents [[Cross Site Request Forgery|CSRF]]
	- None: No same site protection. Sites like desmos, google maps that want to be embedded into other sites usually have this setting
	- Lax: Allows cookies to be sent on some cross-site requests
	- Strict: Strict never allows cookie to be sent across sites