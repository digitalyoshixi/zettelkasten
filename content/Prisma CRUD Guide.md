---
tags:
  - programming
  - database
---
Assuming we are using [[prisma-client-js]]
# Schema Layout
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
# Create
```ts
import {PrismaClient} from "@prisma/client"
const prisma = new PrismaClient()

async function adduser(){
	// will depend on what models you have defined in your schema
	const user = prisma.user.create({data : { name : "Kyle" }});
	console.log(user);
}
```
# Read
```ts
import {PrismaClient} from "@prisma/client"
const prisma = new PrismaClient()

async function readallusers(){
	// will depend on what models you have defined in your schema
	const users = await prism.user.findMany();
	console.log(users);
}

async function readsingleuser(){
	// will depend on what models you have defined in your schema
	const user = await prisma.user.findUnique({
	  where: {
	    id: 1,
	  },
	})
	console.log(user);
}
```
# Update
```ts
import {PrismaClient} from "@prisma/client"
const prisma = new PrismaClient()

async function updateuser(){
	const updateUser = await prisma.user.update({
	  where: {
	    id: 1,
	  },
	  data: {
	    name: 'Viola the Magnificent',
	  },
	})
	console.log(updateUser);
}
```
# Delete
```ts
import {PrismaClient} from "@prisma/client"
const prisma = new PrismaClient()

async function deleteuser(){
	const deleteUser = await prisma.user.delete({
	  where: {
	    name: 'Kyle',
	  },
	})
	console.log(deleteUser);
}
```