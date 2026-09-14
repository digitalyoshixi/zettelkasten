---
tags:
  - programming
  - web
---
# Installation
`npm install cors`
# Allowing CORS in [[ExpressJS]]
Enable the CORS [[Middleware]]
```js
...
import cors from 'cors'
app.use(cors({ origin : "http://somerequestedweb.com"}))
...
```