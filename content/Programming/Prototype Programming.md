---
tags:
  - programming
---
A twist on [[Object Oriented Programming]] that removes [[Class]] definitions, and allows [[Object|Objects]] to directly inherit from other objects.
![[Prototype Programming-20250630195832389.webp|355]]
- Prototype of all objects can be directly modified at runtime. You can give all strings a new method like `removeWhitespace()`
# Example Prototype Method Additions
```
String.prototype.removeWhitespace = function(){
    // remove leading and trailing whitespace
}

let searchTerm = "  example ";
searchTerm.removeWhitespace();    // "example"
```
# List of Prototype Languages
- [[JavaScript]]
- [[Lua]]