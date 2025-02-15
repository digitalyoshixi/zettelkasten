---
tags:
  - javascript
---
A way to send requests using [[JavaScript]].
# Sending JSON Data
```js
const data = {
  url: "Hello World",
};

fetch("https://jsonplaceholder.typicode.com/posts", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify(data)
})
.then(response => response.json())
.then(result => console.log(result))
.catch(error => console.error('Error:', error));
```
# Sending Form Data
```js
const formdata = new FormData();
formdata.append("name" : "daniel");

fetch("https://localhost:3000/posts", {
  method: "POST",
  body: formdata
})
.then(response => response.json())
.then(result => console.log(result))
.catch(error => console.error('Error:', error));

```