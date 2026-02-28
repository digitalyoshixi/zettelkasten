---
tags:
  - python
aliases:
  - CORS
---
The list of sites that can access your [[Application Program Interface|API]].
Allows access of resources from remote hosts. It allows resources that live in one URL to be loaded into another URL.
It is part of the [[Browser Origin Policy]].
# Installation
`npm install cors`
# Cross Origin Request Process
1. ![[Pasted image 20241013171253.png]]Request sent from a origin, and is received by a different origin
2. Server adds an access control origin header to the top of the response
   ![[Cross Origin Resource Sharing-20241013211520113.webp]]
   It must match the origin in the request, or it can be a wildcard `*` to allow sharing with any origin

If the origins in the response and the request are mismatched, then the browser will respond with a CORS error
![[Cross Origin Resource Sharing-20241013211820665.webp]]
# Allowing CORS in [[ExpressJS]]
Enable the CORS [[Middleware]]
```js
...
import cors from 'cors'
app.use(cors({ origin : "http://somerequestedweb.com"}))
...
```
# Auxilliary Concepts
- [[CORS Preflight]]