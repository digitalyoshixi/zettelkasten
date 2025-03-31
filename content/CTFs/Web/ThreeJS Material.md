---
tags:
  - javascript
---
# Material Types
### Basic
![[ThreeJS Material-20241124044558752.webp|207]]
Just a simple color, no shaders
### Standard
![[ThreeJS Material-20241124044537071.webp|205]]
Allows shaders and colors and textures
### Normal
![[ThreeJS Material-20241124044627219.webp|219]]
Does not allow colors, but allows shaders
# Properties
### Flat Shading
```js
const mat = new THREE.MeshStandardMaterial({
    color : 0xffffff,
    flatShading : true
});
```
### Wireframe
```js
const mat = new THREE.MeshStandardMaterial({
    color : 0xffffff,
    wireframe : true
});
```