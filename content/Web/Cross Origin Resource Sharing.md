---
tags:
  - python
aliases:
  - CORS
---
The list of sites that can access your [[Application Program Interface|API]].
Allows access of resources from remote hosts. It allows resources that live in one URL to be loaded into another URL.
It is part of the [[Browser Origin Policy]].
# Cross Origin Request Process
1. ![[Pasted image 20241013171253.png]]Request sent from a origin, and is received by a different origin
2. Server adds an access control origin header to the top of the response
   ![[Cross Origin Resource Sharing-20241013211520113.webp]]
   It must match the origin in the request, or it can be a wildcard `*` to allow sharing with any origin
# CORS Testing
1. Change [[Origin]] header to an arbitrary value or `True`
2. If there are any known origins (i.e the site itself), try modifying origin header to modify it to find regex issues
	1. Whitelisted: `normalwebsite.com`
	2. Try `hackernormalwebsite.com`
	3. Try `normalwebsite.com.hackerwebsite.com`
3. Change [[Origin]] header to `null`
# Guides
- [[Allowing CORS in ExpressJS]]
- [[CORS Access-Control-Allow-Credentials Exploit Payload]]
- [[CORS Access-Control-Allow-Origin Null Exploit Payload]]
# Auxilliary Concepts
- [[CORS Preflight]]