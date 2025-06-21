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
Save the database string it provides, and modify the [[Prisma Schema]] file accordingly

### Migration
```
npx prisma migrate dev
```