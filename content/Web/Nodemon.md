---
tags:
  - node
---
Automatically reloads the web server after js files change.
# Installation
`npm install nodemon`
nodemon will be in the dev dependencies in [[package.json]]
Then edit package.json to have the `dev` script:
![[Nodemon-20241027185332332.webp]]
```
npm run dev
```
Will serve the app at http://localhost:5000