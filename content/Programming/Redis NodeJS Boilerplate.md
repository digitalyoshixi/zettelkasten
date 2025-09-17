---
tags:
  - database
---
```js
const Redis = require('redis')
const redisClient = Redis.createClient({url : "http://127.0.0.1:6379"})

// set some values
redisClient.setex("name", 3600, "daniel") // set for 1hr
redisClient.get("name" (error, value) => {
	if (error) console.error(error)
	if (value != null){
		return value
		//return res.json(JSON.parse(photos))
	}
}) 
// all other redis commands work
```