---
tags:
  - security
  - web
aliases:
  - Server Side Parameter Pollution
---
A [[Server Side Request Forgery|SSRF]] vulnerability where request's HTTP parameters end up overwriting parameters the server inserts. Can be used to:
- Break access control
- Modify application data
# Example
Original request is of the format:
```
GET /userSearch?name=peter&back=/home
```
Server then sends this request to backend
```
GET /users/search?name=peter&publicProfile=true
```
# Testing
- Use query characters (`#`, `&`, `=`) and see if anything breaks
	- `#` [[Fragment Identifier]] truncates the request (make sure to url encode this)
	- `&` [[URL Query Parameter]] to add new parameters (make sure to url encode this)