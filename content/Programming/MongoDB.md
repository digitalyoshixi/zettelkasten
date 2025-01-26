---
tags:
  - web
  - database
---
A [[No-SQL]] database.
# Creating In Cloud
1. https://www.mongodb.com/products/platform/atlas-database
2. Create the database local user and password
3. Copy the connection string 
   ![[MongoDB-20241013222308416.webp]]
4. Allow any device to access this database (For testing purposes)
   ![[MongoDB-20241027190742138.webp]]
1. Make an [[Environment Variables|.env]] storing your `MONGO_USERNAME` and `MONGO_PASSWORD`
```js
import mongodb from 'mongodb'
const MongoClient = mongodb.MongoClient
const mongo_username = process.env["MONGO_USERNAME"]
const mongo_password = process.env["MONGO_PASSWORD"]
const uri = "<connection string you copied>"
// Example: const uri = "mongodb+srv://${mongo_username}:${mongo_password}@cluster0.jae3r.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

```
# Installation [[NodeJS]]
`npm install mongodb`
# Concepts
- [[Mongoose]]