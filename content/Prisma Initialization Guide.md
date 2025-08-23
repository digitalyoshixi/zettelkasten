---
tags:
  - programming
  - database
---
1. Initialize from template
```
npx prisma init --datasource-provider postgresql
```
2. Setup `tsconfig.json`
```js
{
	"compilerOptions" : {
		"sourceMap" : true,
		"outDir" : "dist",
		"strict" : true,
		"lib" : ["esnext"],
		"esModuleInterop" : true
	}
}
```
3. In a `.env`, write your remote database URL
```
DATABASE_URL="postgresql://johndoe:randompassword@localhost:5432/mydb?schema=public"
```
4. Setup a [[Prisma Schema]]
5. Then, do a migration to update your database