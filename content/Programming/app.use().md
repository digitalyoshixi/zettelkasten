---
tags:
  - express
aliases:
  - Express Middleware
---
# Middleware Routing Speifications
### Middleware For Specified Routes
```js
app.use(path, middleware)
```
Used for loading [[Middleware]] into your [[ExpressJS]] file.
- path : the path for which the middleware function is invoked
- middleware : the middleware function 
### Middleware For all Routes
```js
app.use(middleware)
```
If the path is not provided, then the middleware function applies to all routes
Equivalent to saying:
```js
app.use("/", middleware)
```
### Middleware For Wildcard Routes
```js
// ... other app.use() statements above ...
app.use("*", fallbackfunction)
```
This will run a fallback function if a browser sends a request to a route that was not previously defined with middleware behavior.
Most commonly, this wildcard should be:
```js
app.use("*", (req, res) => res.status(404).json({error: "not found"}))
```
# Middleware For Allowing JSON requests
```js
app.use(express.json());
```
# Middleware For Allowing Form Requests
```js
app.use(express.urlencoded({extended : false}));
```
# Creating Specific Middleware
- [[ExpressJS Router()]]