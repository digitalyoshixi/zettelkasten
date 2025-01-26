---
tags:
  - javascript
  - express
---
A backend framework for [[NodeJS]] backends.
Used to make http endpoints.
# Installation
`npm install express`
you will see express dependency in [[package.json]] and a `express` folder in node-modules.
### Importing
```js
import express from 'express'
```
# Boilerplate
```node
const express = require('express')
const app = express()

app.listen(3000, () => {
    console.log("server is running");
});

app.get('/', (req, res) => {
    res.send("Hello From node API")
});
```
# Concepts
- [[Express app]]
- [[app.use()]]
- [[ExpressJS Router()]]
- [[ExpressJS Response]]
- [[ExpressJS static()]]
# App Anatomy
![[Drawing 2024-10-28 00.26.43.excalidraw]]
