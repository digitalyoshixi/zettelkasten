---
tags:
  - express
  - javascript
  - node
---
For automatically finding [[MIME]] types and returning them with the HTML that needs them.
```js
app.use(express.static(path.join(__dirname, "client")));
```