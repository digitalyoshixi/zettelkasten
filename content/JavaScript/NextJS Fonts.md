---
tags:
  - web
---
# Fonts List
https://fonts.google.com/
# Adding Fonts
### Fonts from `next/font/google`
```js
import {Cormorant_Garamond} from "next/font/google"

const cormorantGaramond = Cormorant_Garamond({
	subsets : ["latin"],
	variable : "--font-cormorant-garamond",
	weight : ["400"]
})

export default function Main(){
	return (
		<body className={`${cormorantGarmond.variable}`}>
			Hello
		</body>	
	)
}
```
### Fonts from local directory
```js
import localFont from "next/font/local";
import "./globals.css";

const geistSans = localFont({
  src: "./fonts/GeistVF.woff",
  variable: "--font-geist-sans",
  weight: "100 900",
});

export default function Main(){
	return (
		<body className={`${geistSans.variable}`}>
			Hello
		</body>	
	)
}
```
Then modify `tailwind.config.js` to be:
```
module.exports = {
  theme: {
    extend: {
      fontFamily: {
        myfont: ['var(--font-myfont)'],
      },
    },
  },
}
```