---
tags:
  - web
  - security
---
A solution to [[Cross Site Request Forgery|CSRF]].
Everytime a request is sent. a randomly generated code is attached to the request.
Anything that the webpage is sent back then must have the same randomly generated code to verify that it came from the same origin.