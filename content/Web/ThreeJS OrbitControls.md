---
tags:
  - javascript
---
```js
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

const controls = new OrbitControls(camera,renderer.domElement);
```
# Damping
```js
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

const controls = new OrbitControls(camera,renderer.domElement);
controls.enableDamping = true;
controls.dampingFactor = 0.03;

// animate
function animate(t=0){
	requestAnimationFrame(animate);
	// your animation here
	renderer.render(scene, camera);
	controls.update();
}
```
