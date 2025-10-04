---
tags:
  - programming
  - web
---
https://vite-pwa-org.netlify.app/guide/
# Guide
1. Setup [[Vite]]
2. 
```
npm install -D workbox-window vite-plugin-pwa
```
3. Modify `Vite.config.js` as:
```js
import { defineConfig } from 'vite'
import { VitePWA } from "vite-plugin-pwa";
import react from '@vitejs/plugin-react'
// https://vite.dev/config/
export default defineConfig({
base: "./",
plugins: [react(),
VitePWA({
registerType: 'autoUpdate' ,
devOptions: {
enabled: true
}
})
],
})
```
3. `npm run dev` and then grab [[Web Application Manifest]], and the service workers in `./dev-dist/`