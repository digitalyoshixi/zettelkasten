---
tags:
  - web
aliases:
---
[[Web Cache Deception]] that involve the origin server parsing symbols as parameter delimiters, but the cache server does not:
- [[Spring Matrix Variable Delimiter]]
- [[Ruby on Rails Variable Delimiter]]
- [[Encoded Character Variable Delimiter]]
# Identification
- Use `GET`, `HEAD`, `OPTIONS` requests
- Identify discrepancies in how cache and origin servers parse the URL path
	- Start with a path with arbitrary string `/users/list` -> `/users/listaaa`
		- If same response, its being redirected, pick something else
	- Add delimiter characters, Try to find the standard that returns the same response:
		- [[Path Mapping]]
		- [[Rest Path Mapping]]
		- [[Spring Matrix Variable Delimiter]]
		- [[Ruby on Rails Variable Delimiter]]
		- [[Encoded Character Variable Delimiter]]
- Once standard found, test static extension `.css`, `.js`, `.ico`, `.exe`, see if they cache
# List
https://portswigger.net/web-security/web-cache-deception/wcd-lab-delimiter-list