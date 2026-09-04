---
tags:
  - web
aliases:
  - SameSite
  - HTTPOnly
  - Ssecure
  - Cookie Flags
---
This stores session information across multiple instances. They are stored client-side in the user's web browser.
Used for temporary information that doesn't matter too much.
# Cookie Security Flags
- `HTTPOnly`: Prevents javascript visibility ([[Cross Site Scripting|XSS]]), cookies are not stored
- `Secure`: Prevents cookies from being forwarded unless you use [[Hyper Text Transfer Protocol Secure|HTTPS]]
- `SameSite`: Prevents [[Cross Site Request Forgery|CSRF]]
	- None: No same site protection. Sites like desmos, google maps, tracking cookies that want to be embedded into other sites usually have this setting
	- Lax: Allows cookies to be sent on some cross-site requests (Automatic by chrome)
		- Only if request uses GET
		- Only if request resulted from top-level navigation such as clicking a link
		- Can still be exfiltrated if you force a GET request. ([[CSRF SameSite Bypass with GET Request]])
	- Strict: Strict never allows cookie to be sent across sites
		- Client side redirects issued by the site (not server issued 300 responses) can still include these cookies ([[CSRF Gadget]])
	- Defined for the domain, and one subdomain above (not all subdomains)
# Same Site vs Same Origin
![[Cookies-20260903005418963.webp]]