# Three.js FAQ


## Tips and tricks
- [General tips](https://discoverthreejs.com/tips-and-tricks/)
- [Optimising performance](https://attackingpixels.com/tips-tricks-optimizing-three-js-performance/)

## [Vector to array conversion](https://github.com/mrdoob/three.js/blob/r114/src/math/Vector3.js#L688)
```javascript
vertex.toArray()
```

## [View axes](https://threejs.org/docs/#api/en/helpers/AxesHelper)
```javascript
var axesHelper = new THREE.AxesHelper( 5 );
scene.add( axesHelper );
```
## [Find absolute position of a vertex](https://stackoverflow.com/questions/11495089/how-to-get-the-absolute-position-of-a-vertex-in-three-js)

## View point cloud
View vertices of a point cloud.
```javascript
// Get vertex point cloud.
var getPointsObject = function (points) {
  let geometry = new THREE.Geometry();
  for (const point of points) {
    geometry.vertices.push(point);
  }
  let material = new THREE.PointsMaterial({
    color: "white",
    size: 3,
    sizeAttenuation: false
  });
  return new THREE.Points(geometry, material);
};

// Generate points.
var cube = new THREE.BoxGeometry(1, 1, 1);
const points = cube.vertices

// Get point object and add to scene. ;
scene.add(getPointsObject(points));
```

## View vertices of an existing geometry
```javascript
var points = new THREE.Points(geometry, new THREE.PointsMaterial({
  size: 0.25,
  color: "yellow"
}));
scene.add(points);
```

## [Create BufferGeometry](https://threejsfundamentals.org/threejs/lessons/threejs-custom-buffergeometry.html)

## Dynamic visualisations using BufferGeometry

```javascript
// Setup a buffer attribute for position variable.
const positionAttribute = new THREE.BufferAttribute(
  positions, positionNumComponents);
// Mark positionAttribute as dynamic if its contents change often.
positionAttribute.setUsage(THREE.DynamicDrawUsage);
```

## Copying attributes for a buffer geometry
```javascript
var nodeGeometry = new THREE.SphereBufferGeometry( 0.1, 32, 32 );
const bufferedNodeGeometry = new THREE.InstancedBufferGeometry();

// Method 1 (may not copy over all required attributes)
bufferedNodeGeometry.index = nodeGeometry.index;
bufferedNodeGeometry.attributes = nodeGeometry.attributes;

// Method 2
bufferedNodeGeometry.copy( nodeGeometry );
```

## Duplicating objects using THREE.InstancedMesh
```javascript
// Add mesh nodes as spheres.
var nodeGeometry = new THREE.SphereBufferGeometry( 0.1, 32, 32 );
var transform = new THREE.Object3D();
// Define a new material instance for the spheres (required)
var nodeMaterial = new THREE.MeshNormalMaterial();
var nodeMesh = new THREE.InstancedMesh( nodeGeometry, nodeMaterial, numVertices );
posNdx = 0;
for (const vertex of unbufferedGeometry.vertices) {
    transform.position.set( vertex.x, vertex.y, vertex.z );
    transform.updateMatrix();
    nodeMesh.setMatrixAt( posNdx ++, transform.matrix );
}
scene.add( nodeMesh );
```

## [Add stats.js](https://github.com/mrdoob/stats.js/)
```javascript
// Import stats.
import * as Stats from 'stats.js';
```

## [Get camera world coordinates](https://stackoverflow.com/questions/15696963/three-js-set-and-read-camera-look-vector/)
```javascript
let vector = camera.getWorldDirection();
```

## Enable or disable orbit controls
```javascript
orbitControls.enabled = false;
orbitControls.enabled = true;
```