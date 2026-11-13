---
tags:
  - web
  - security
---
```
{
	"__proto__" : {
		"evilProperty": "payload"
	}
}
```
When `JSON.parse()` is called, `__proto__` gets added as an attribute to the object.