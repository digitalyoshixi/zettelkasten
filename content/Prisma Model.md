---
tags:
  - programming
  - database
---
These are representation of entities to be stored within your [[Relational Database]].
It defines the [[C Structures|Struct]] of the data to be stored.
# Boilerplate
```js
model User {
	id Int @id @default(autoincrement())
	name String 
}
```