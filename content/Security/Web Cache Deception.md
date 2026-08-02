---
tags:
  - web
  - security
aliases:
  - Cache Deception
---
Tricking a [[Cache Server]] into storing sensitive user data so that attackers can access it later.
# Identification
- Test endpoints that support `GET`, `HEAD`, `OPTIONS`
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
# Types
- [[Path Mapping Discrepancies]]
# Tools
- [[Param Miner]]
- [[Web Cache Deception Scanner]]