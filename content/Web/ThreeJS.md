---
tags:
  - javascript
aliases:
  - 3JS
---
A JavaScript library that allows rendering of 3D objects.
# Installation
1. `npm i three`
# Boilerplate
```js
as THREE from 'three'

const w = window.innerWidth;
const h = window.innerHeight;
console.log(w)
const renderer = new THREE.WebGLRenderer({antialias : true});
renderer.setSize(w,h)


document.body.appendChild(renderer.domElement);

const fov = 75;
const aspect = w/h;
const near = 0.1;
const far = 10;
const camera = new THREE.PerspectiveCamera(fov, aspect, near, far);
// move camera back a bit
camera.position.z = 2;

const scene = new THREE.Scene()
// create a sample object to put in the scene
const geo = new THREE.IcosahedronGeometry(1.0,2);
const mat = new THREE.MeshStandardMaterial({
    color : 0xffffff,
    flatShading : true
});
const mesh = new THREE.Mesh(geo,mat);
scene.add(mesh);

function animate(t=0){
	requestAnimationFrame(animate);
	// your animation here
	// heres an example
	mesh.scale.setScalar(Math.cos(t*0.001) + 1.0);
	//
	renderer.render(scene, camera);
}

animate();
```
# Concepts
- [[ThreeJS Animation]]
- [[ThreeJS Mesh]]
- [[ThreeJS Material]]
- [[ThreeJS Light Sources]]
- [[ThreeJS Import Object]]
- [[ThreeJS OrbitControls]]
- [[ThreeJS Fiber]]