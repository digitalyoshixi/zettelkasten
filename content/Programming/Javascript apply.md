---
tags:
  - programming
  - javascript
---
Applies a function to a list of arguments.
```js
const person1 = { name: "John" };
const person2 = { name: "Paul" };
const person3 = { name: "Ringo" };

function greet(greeting) {
  return greeting + " " + this.name;
}

greet.apply(person3, ["Hello"]);
```