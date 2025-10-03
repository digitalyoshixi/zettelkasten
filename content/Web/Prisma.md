---
tags:
  - programming
  - database
---
This is a modern [[Object Relational Mapping|ORM]] for [[PostgreSQL]].
# Installation
```
npm install prisma typescript tsx @types/node --save-dev
```
Globally:
```
sudo npm i -g prisma
```
# Setup
```
npx prisma
```
Make sure to follow [[Prisma Initialization Guide]] afterwards.
### Initialization
```
npx prisma init --db --output ../generated/prisma
```
Save the database string it provides, and modify the [[Prisma Schema]] file accordingly
### Migration
```
npx prisma migrate dev --name "mymigraitonmessage"
```
# Concepts
- [[Prisma Schema]]
- [[Prisma Generator]]
- [[prisma-client-js]]
# Guides
- [[Prisma Initialization Guide]]
- [[Prisma CRUD Guide]]