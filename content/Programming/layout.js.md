---
tags:
  - react
---
![[layout.js-20241128015404140.webp]]
The file that nextjs automatically generates from `page.js` files in the same folder.
Everything else is imported in here and added as children to this layout.
The layout can differ between routes
# Boilerplate
```js
export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>
        {children}
      </body>
    </html>
  );
}
```