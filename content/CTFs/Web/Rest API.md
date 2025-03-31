---
tags:
  - web
aliases:
  - HTTP Request
---
Most common API. Rest style apis are restful
Use a program to send a http protocol to a server. 
This is stateless, so **server doesn't remember anything about the client.** 
![[Application Program Interface-20240802031924334.webp]]
1. Send HTTP request
2. Fetch data from database
3. Return data in JSON format
[[OAuth]] is commonly required to access an API functionality
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
### POST
Send data to the server
- Used for authentication
- Used to create things
### PUT
Updating information
- SQL
### DELETE
Delete a resource on the server
### HEAD
Retrieve resource headers without the resource itself.
Similar to GET, but has no resource body
