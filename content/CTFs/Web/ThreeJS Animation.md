---
tags:
  - javascript
  - web
---
in index.js:
```js
function animate(t=0){
	requestAnimationFrame(animate);
	// your animation here
	// heres an example
	mesh.scale.setScalar(Math.cos(t*0.001) + 1.0);
	//
	renderer.render(scene, camera);
}
```
