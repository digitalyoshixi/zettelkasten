---
tags:
  - react
  - javascript
---
React rendering decisions come from [[Document Object Model|VDOM]]
# Process
![[ReactJS Rendering-20240918030726618.webp]]
1. If state is changed, then update [[Document Object Model|VDOM]]
2. "diff" the [[Document Object Model|VDOM]] with the real [[Document Object Model|DOM]]
3. Once it sees the "diff", if it exists, react updates the real [[Document Object Model|DOM]]