---
tags:
  - javascript
  - java
---
An interface is the general [[C Structures|Structure]] of datatype.

It defines what properties the variable will have and the datatypes for each property.
```ts
interface Person {
	first : string;
	last : string;
	[key : string] : any; //any other property you want
}

const person : Person = {
	first : "Daniel",
	last : "Humbrey"
}
```