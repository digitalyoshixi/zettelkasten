---
tags:
  - security
  - web
---
A way to detect server-side prototype pollution if the server uses a for loop to return properties like such:
```
for (const propertyKey in myObject) {
	console.log(propertyKey, myObject[propertyKey]);
}
```
# Example Vulnerable Service
![[Prototype Pollution Property Reflection-20261115193820839.webp]]
