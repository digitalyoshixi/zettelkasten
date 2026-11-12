---
tags:
  - javascript
aliases:
  - Javascript Object
---
A javascript object. Its a collection of properties (key:value pairs)
```json
{
	"myval" : 20,
	"mylist" : [20,20]
}
```
All javascript objects have:
- Properties
- One [[Prototype]]
# Example
```js
const user = {
	username : "daniel",
	userId : 01234,
	isAdmin: false
}
```
Accessing:
```js
user.username // "daniel"
user['userId'] // 01234
```
### Json With Methods
```js
const user = {
	username: "daniel",
	userId: 01234,
	exampleMethod: function() {
	}
}
```