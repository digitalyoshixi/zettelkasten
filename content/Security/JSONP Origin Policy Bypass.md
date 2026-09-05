---
tags:
  - security
  - web
---
A method to bypass [[Same Origin Policy]]:
1. Use a [[JSON With Padding|JSONP]] endpoint as script source
2. Endpoint accept user supplied function via callback and returns JSON payload as function parameter
# Example
```
GET https://mysite/api/v1/tools/actions?=callback=alert(1); HTTP2
```
For this endpoint that accepts JSONP