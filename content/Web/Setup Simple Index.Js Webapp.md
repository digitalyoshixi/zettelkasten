---
tags:
  - node
---
1. `npm init -y`
2. `touch index.js`
3. Edit `package.json`
   ```json
   ...
   scripts {
   ...
	  'serve' : "node index.js"
   }
```
4. `npm i express`
5. `npm i nodemon`
6. edit `package.json`
```json
   scripts {
   ...
	  'dev' : "nodemon index.js"
   }
```
7. Add boilerplate code in `index.js`:
```node
const express = require('express')
const app = express()

app.listen(3000, () => {
    console.log("server is running");
});
