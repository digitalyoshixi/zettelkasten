---
tags:
  - web
  - javascript
  - react
---
# Setup
1. `npm install @next/mdx @mdx-js/loader @mdx-js/react tailwindcss/typography`
2. `nvim next.config.mjs`
```js
import createMDX from '@next/mdx'
 
/** @type {import('next').NextConfig} */
const nextConfig = {
  // Configure `pageExtensions` to include markdown and MDX files
  pageExtensions: ['js', 'jsx', 'md', 'mdx', 'ts', 'tsx'],
  // Optionally, add any other Next.js config below
}
 
const withMDX = createMDX({
  // Add markdown plugins here, as desired
})
 
// Merge MDX config with Next.js config
export default withMDX(nextConfig)
```
3. Create a file called: `mdx-components.js` with contents:
```js
export function useMDXComponents(components) {
  return {
    ...components,
    h2 : ({ children }) => <h2 className="text-2xl">{children}</h2>,
    h1 : ({ children }) => <h1 className="text-3xl">{children}</h1>
  }
}   
```
you can add more custom styles if needed. Ensure this file is at the root directory at the same level as `/app` and `package.json`
4. Edit `tailwind.config.mjs` to be:
```js
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
    "./mdx-components.js"
  ],
  theme: {
    extend: {
      ...
    },
  },
  plugins: [require("@tailwindcss/typography")],
};

```
5. Create 2 files inside `/app`
   ![[NextJS Markdown-20241223015612843.webp]]
5. Edit `page.js` to be:
```js
import MyMDXContent from './pagecontent.mdx';

export default function Page() {
  return (
    <div className="prose dark:prose-invert">
      <MyMDXContent/>
    </div>
  );
}
```
6. Edit `pagecontent.mdx` to be:
```md
# Hi there
How is it
```
Now, run and navigate to `localhost:3000/test` and you should see:
![[NextJS Markdown-20241223015726448.webp]]
# Frontmatter support with next-mdx-remote
