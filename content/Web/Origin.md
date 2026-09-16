---
tags:
  - web
aliases:
  - Origin Header
---
A pairing of the [[Website]] and the subdomain and port.
![[Origin-20260903004457776.webp]]
# HTTP Request Header
- An optional used by the browser for cross-origin requests to indicate to the server the originating host
- `Origin: null` is often associated with:
	- Cross-origin redirects
	- Requests from serialized data
	- Request using the `file:` protocol
	- Sandboxed cross-origin requests ([[IFrame]])