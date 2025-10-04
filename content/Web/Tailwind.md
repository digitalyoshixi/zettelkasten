---
tags:
  - web
  - programming
---
![[Tailwind-20240802035802173.webp]]
A [[Cascading Style Sheet|CSS]] framework that uses modular utility components to create intricate designs very fast.
All of the css will be classes inside of your HTML tags.
Should be used with [[ReactJS]]
# Installation (With [[ReactJS]])
1. `npm i tailwindcss postcss autoprefixer`
2. `npx tailwindcss init -p`
3. Change `tailwind.config.js` to have:
```js
/** @type {import('tailwindcss').Config} */
export default {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {},
  },
  plugins: [],
}
```
4. Clear the contents of `index.css` and `app.css` 
5. In your `index.css`, add the following to the top:
```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```
6. in package.json, add the command:
```js
    "start" : "npx tailwindcss -i ./src/index.css -o ./src/output.css --watch"
```
7. Run `npm run start`
8. in `main.jsx`, make the course `output.css` instead of `index.css`
9. in app.jsx , make the main div:
```js
function App() {
  const [count, setCount] = useState(0)
  return (
    <>
    <div className="h-screen w-screen">
    </div>
    </>
  )
}
```
### CDN Installation
index.html
```html
<head>
	...
	<link href="https://unpkg.com/tailwindcss@^2/dist/tailwind.min.css" rel="stylesheet">
</head>
```
# Concepts
- [[Tailwind Sizing]]
- [[Tailwind Google Fonts]]