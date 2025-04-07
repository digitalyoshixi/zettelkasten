---
tags:
  - web
  - database
---
A [[MongoDB]] [[Middleware]].
# Boilerplate
```node
mongoose = require('mongoose')
mongoose.connect("mongodb+srv://<username>:<password>@cluster0.jae3r.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    .then( () => {
        console.log("connected to database");
    })
    .catch( () => {
        console.log("connectio nfailed");
    });
```

To have objects to store in the [[Document Object Database]], you need to create models.
# MongoDB Models
- [[Mongoose Models]]