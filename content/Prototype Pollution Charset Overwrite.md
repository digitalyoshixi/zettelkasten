---
tags:
  - web
  - security
---
A way to view if server-side prototype pollution worked.
In [[ExpressJS]] `body-parser` module, you can pollute a `content-type` field in a request.
```
{
    "sessionId":"0123456789",
    "username":"wiener",
    "role":"default",
    "__proto__":{
        "content-type": "application/json; charset=utf-7"
    }
}
```
You can use this to overwrite original `Content-Type` in the request