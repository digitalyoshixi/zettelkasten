---
tags:
  - web
  - security
---
A way to see if server-side prototype pollution vulnerabilities worked.
Involves rewriting custom json error mesages.
![[Prototype Pollution Status Code Overwrite-20261115214234997.webp]]
# http-errors library
On a page where status is returned, you can pollute the fields as status is often not set by default. Pollute:
- `status`
- `statusCode`
Use a status code in the 400-599 range otherwise node defaults to 500 status.

```
{
    "sessionId":"0123456789",
    "username":"wiener",
    "role":"default",
    "__proto__":{
        "status": 420
    }
}
```
![[Prototype Pollution Status Code Overwrite-20261115220023771.webp]]