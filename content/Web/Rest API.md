---
tags:
  - web
aliases:
  - HTTP Request
---
Most common API. Rest style apis are restful.
- Stateless. Server doesn't remember anything about client - Standard HTTP methods
- Often uses [[JSON]]
- Single-request, may cause over-fetching or under-fetching
Use a program to send a http protocol to a server. 
![[Application Program Interface-20240802031924334.webp]]
1. Send HTTP request
2. Fetch data from database
3. Return data in JSON format
[[Open Auth]] is commonly required to access an API functionality
# Constraints
- Client-server architecture
- Statelessness
- Layered system
- Cacheability
- Uniform design 
- Code on demand
# HTTP Requests
### GET
Retrieving data from the server.
- Used for non-sensitive data
- Not protected with site redirects
### POST
Send data to the server
- Used for authentication
- Used to create things
- Protected further with [[Cross Origin Resource Sharing|CORS]]
### PUT
Updating information
- SQL
- Protected further with [[Cross Origin Resource Sharing|CORS]]
### DELETE
Delete a resource on the server
### HEAD
Retrieve resource headers without the resource itself.
Similar to GET, but has no resource body
# Concepts
- [[HTTP Request Headers]]
- [[HTTP Response Headers]]