---
tags:
  - javascript
  - react
aliases:
  - VDOM
  - DOM
---
Anything in the HTML or XML document can be accessed through a DOM
What every browser uses to model HTML elements on a webpage.
![[Document Object Model-20240918025614069.webp]]
# JS Interaction With DOM
- [[getElementByID]]
- [[querySelector]]
# Virtual DOM (VDOM)
The VDOM is handled with this function:
in main.jsx ([[Vite]]) 
![[Document Object Model-20241031213857214.webp]]
in index.js ([[Create React App|CRA]]):
![[Document Object Model-20241031213915172.webp]]
A virtual, temporary DOM to apply temporary changes that later get "diff"ed with the real DOM.
The most expensive thing you can do in the web-browser is update the DOM.
### Renders 
First render occurs in the root.render() function
All subsequent renders are called from [[ReactJS State]]
### Components
See ([[ReactJS Component Data]])
##### Reconciliation
If you replace a component with an entirely different component, ReactJS will completely make a new component
![[Document Object Model-20241112035729243.webp]]
