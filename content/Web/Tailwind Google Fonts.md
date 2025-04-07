---
tags:
  - web
---
1. add the CDN into your `index.html` file
```js
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500&display=swap" rel="stylesheet">
```
2. Edit `tailwind.config.js` to include the following:
```js
module.exports = {
  theme: {
    extend: {
      fontFamily: {
        poppins: ["Poppins", "sans-serif"],
      },
    },
  },
  // ... other configurations
};
```
3. Use in your component
```js
<div className="font-poppins">
  This text uses the Poppins font
</div>
```