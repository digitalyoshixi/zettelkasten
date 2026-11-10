---
tags:
  - security
aliases:
  - HTTP Basic Authentication
---
A method to send credentials with every request through [[Base64]].
- Server returns a Authorization token, subsequent requests have a header that is of the form: `Authorization: Basic base64(username:password)`
```
curl --basic user=pass
```
