---
tags:
  - programming
aliases:
  - Software Glue
---
Software used to provide non-default services for other software.
Most of the time, they are libraries that allow for communication of different types or connectivity between applications.
# Examples
### Creating Middleware
food.js
```js
const food = "burger";
module.exports = food;
```
### Using Middleware
In [[ExpressJS]],
```js
const foodmodule = require("food")
app.use(foodmodule)
```
allows the use of communication via [[JSON]] files