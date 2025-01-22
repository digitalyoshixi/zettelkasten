---
tags:
  - web
---
For non-standard requests ([[Rest API|HTTP Request]] that is not GET) like:
- PUT
- PATCH
- DELETE
The browser will first send a preflight check to ask if the server allows that type of request
# Preflight Process
1. The client sends a preflight request asking the server if the request method is allowed
2. The server responds, with a message indicating:
   - If the request method is allowed
   - The Access-Control-Max-Age time so that this preflight response status can be cached in the browser
![[CORS Preflight-20241013212738579.webp]]
   
