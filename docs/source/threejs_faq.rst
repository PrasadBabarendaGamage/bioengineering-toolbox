============
Three.js FAQ
============

.. toctree::
   :maxdepth: 2

Click on the links in the headings for more information.

`var vs let vs const <https://dev.to/sarah_chima/var-let-and-const--whats-the-difference-69e>`_
-------------------

``let`` is preferred for variable declaration now. It's no surprise as it comes as an improvement to the ``var`` declarations.

*Scope*

- ``var`` declarations are globally scoped or function scoped.

- ``let`` and ``const`` declarations are block scoped.

*Updating and re-declaring variables*

- ``var`` variables can be updated and re-declared within its scope.

- ``let`` variables can be updated but not re-declared.

- ``const`` variables can neither be updated nor re-declared.

*Initialisation*

- ``var`` variables are initialized with undefined.

- ``let`` and ``const`` variables are not initialized.

- ``var`` and ``let`` can be declared without being initialized.

- ``const`` must be initialized during declaration.

`Vector to array conversion <https://github.com/mrdoob/three.js/blob/r114/src/math/Vector3.js#L688>`_
--------------------------

  .. code-block:: javascript

    vertex.toArray()


`View axes <https://threejs.org/docs/#api/en/helpers/AxesHelper>`_
-------

  .. code-block:: javascript

    var axesHelper = new THREE.AxesHelper( 5 );
    scene.add( axesHelper );

View point cloud
-------

View vertices of a point cloud.

  .. code-block:: javascript

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

View vertices of an existing geometry.

  .. code-block:: javascript

    var points = new THREE.Points(geometry, new THREE.PointsMaterial({
      size: 0.25,
      color: "yellow"
    }));
    scene.add(points);

`Create BufferGeometry <https://threejsfundamentals.org/threejs/lessons/threejs-custom-buffergeometry.html>`_
-------

Dynamic visualisations using BufferGeometry
-------

  .. code-block:: javascript

    // Setup a buffer attribute for position variable.
    const positionAttribute = new THREE.BufferAttribute(
      positions, positionNumComponents);
    // Mark positionAttribute as dynamic if its contents change often.
    positionAttribute.setUsage(THREE.DynamicDrawUsage);

Copying attributes for a buffer geometry
-------

  .. code-block:: javascript

    var nodeGeometry = new THREE.SphereBufferGeometry( 0.1, 32, 32 );
    const bufferedNodeGeometry = new THREE.InstancedBufferGeometry();

    // Method 1 (may not copy over all required attributes)
    bufferedNodeGeometry.index = nodeGeometry.index;
    bufferedNodeGeometry.attributes = nodeGeometry.attributes;

    // Method 2
    bufferedNodeGeometry.copy( nodeGeometry );


Duplicating objects using THREE.InstancedMesh
-------

  .. code-block:: javascript

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