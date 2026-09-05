---
tags:
  - web
  - security
---
A method to prevent data corruption of HTTP requests overwriting in-use variables by processing one request at a time.

Can be identified if all requests with the same session appear to be processed sequentially, responses are one after another.