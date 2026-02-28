---
tags:
  - web
---
For non-standard requests ([[Rest API|HTTP Request]] that is not GET) like:
- Has cookies
- Has non-standard content type
- Has custom headers (Authorization, X-\*)
The browser will first send a preflight check to ask if the server allows that type of request
# Preflight Process
1. The client sends a [[Rest API|OPTIONS]] request asking the server if the origin server is within the server's whitelist
2. The server responds, with a message indicating:
   - If the request method is allowed
   - The Access-Control-Max-Age time so that this preflight response status can be cached in the browser
![[CORS Preflight-20241013212738579.webp]]
   
