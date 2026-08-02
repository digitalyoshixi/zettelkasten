---
tags:
  - web
  - security
---
[[Web Cache Deception|Cache Deception]] using files like:
- `robots.txt`
- `index.html`
- `favicon.ico`
# Identification
1. GET request to these files, see if its cached
2. Try [[Normalization Cache Deception]] to see if routing to that file will also cache
3. Exploitable only if web server normalizes, but origin does not
	1. Start with `/target_url`, end with parameter as the `/robots.txt`