---
tags:
  - programming
  - database
---
This is a modern [[Object Relationship Model|ORM]] for [[PostgreSQL]].
# Installation
```
npm install prisma typescript tsx @types/node --save-dev
```
# Setup
```
npx prisma
```
### Initialization
```
npx prisma init --db --output ../generated/prisma
```
### Migration
```
npx prisma migrate dev
```