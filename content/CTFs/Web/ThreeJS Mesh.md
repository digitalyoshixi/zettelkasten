---
tags:
  - javascript
---
# Mesh(Geometry, Material)
Takes in a [[ThreeJS Geometry]] and [[ThreeJS Material]] data.
Returns a mesh object which can be added to other scene objects or the scene itself.
# Children Mesh
If for example, you have a child mesh `mesh2` that you want to inherit properties from the parent mesh `mesh1`, you can do:
```js
mesh1.add(mesh2);
```
