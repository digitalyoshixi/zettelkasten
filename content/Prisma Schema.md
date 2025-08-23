---
tags:
  - programming
  - database
---
This is the main file prisma uses to create a [[Database Schema]].
Comprised of:
- [[Prisma Model]]
- [[Prisma Generator]]
# Boilerplate
```js
generator client {
	provider = "prisma-client-js"
	output = "../generated/prisma"
}

datasource db {
	provider = "postgresql"
	url = env("DATABASE_URL")
}
model User {
	id Int @id @default(autoincrement())
	name String 
}
```