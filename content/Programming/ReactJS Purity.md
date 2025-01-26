---
tags:
  - react
  - javascript
---
How react components should work
Purity in this sense is similar to how we refer to [[Math Purity]]

Pure react components mean that for all inputs, the [[ReactJS Component|Component]] should return the same output.
To keep the react component pure, it must:
- Only return [[JSX]]
- Don't change stuff that has existed before rendering
# Non-Pure Code Example (Bad Example)
![[ReactJS Purity-20240918032935589.webp|385]]