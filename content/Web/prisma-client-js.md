---
tags:
  - programming
  - database
aliases:
---
A [[Prisma Generator]] target.
Can be imported within [[TypeScript]] files with:
```ts
import {PrismaClient} from "@prisma/client"
const prisma = new PrismaClient()

async function adduser(){
	// will depend on what models you have defined in your schema
	const user = prisma.user.create({data : { name : "Kyle" }});
	console.log(user);
}
async function getusers(){
	const users = await prism.user.findMany();
	console.log(users);
}
```