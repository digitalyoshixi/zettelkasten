---
tags:
  - node
  - javascript
---
1. Make `home.html`
```html
<html>
<<body>
 <<h1>
   HELLO WORLD!!!
 </h1> 
</body>
</html>
```
1. Make `index.js`
```js
app.get('/' (request, response) => {

	readFile('./home.html', 'utf8', (err,html) => {
		if (err) {
			response.status(500).send('sorry out of order')
		}
		// no error
		response.send(html);
	
	})
// set app to run on port 3000
app.listen(process.env.PORT || 3000, () => console.log("app is available on http://localhost:3000"))

})
```
3. 