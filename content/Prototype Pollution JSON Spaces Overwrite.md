---
tags:
  - web
  - security
---
A way to view if server-side prototype pollution works.
Modify the [[ExpressJS]] `json spaces` option that toggles indentation option in json response.
- View the message in burp suite's RAW tab to view the difference
- Fixed in express 4.17.4
```
Object.__proto__["json spaces"] = 10
```