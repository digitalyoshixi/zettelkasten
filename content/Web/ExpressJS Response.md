---
tags:
  - express
  - node
  - javascript
---
```js
app.get("/", (req, res) => {
	// send text
	res.status(200).send("hello");
	// send json
	res.status(200).json({"hello" : "world"});
	// send file
	res.sendFile(path.join(__dirname, 'index.html'));
});
```