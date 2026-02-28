---
tags:
  - web
  - security
aliases:
  - IDOR
---
A vulnerability wherein web applications allow users to modify objects by manipulating identifiers without proper [[Authorization]] control checks
# Solution
API endpoints must check that user is allowed authorization
```js
if (req.user ** order.userid === req.user.id){
	return order;
}
```