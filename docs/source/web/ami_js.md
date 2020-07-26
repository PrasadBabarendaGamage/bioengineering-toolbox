# AMI.js FAQ

## [Installing with node/webpack.](https://github.com/FNNDSC/ami/issues/366)
```bash
npm i --save ami.js@next
```

```javascript
var THREE = require('three');
// Import AMI.
import {stackHelperFactory, VolumeLoader} from 'ami.js';

// Within your code:
const StackHelper = stackHelperFactory(THREE);
const stackHelper = new StackHelper(stack);
scene.add(stackHelper)
```

## [Freeing memory](https://stackoverflow.com/questions/51149960/memory-keep-growing-if-i-load-a-new-dicom-file/51150318)

```javascript
let loader = new LoadersVolume();
loader.free(); // Free memory
loader = null;

let stackHelper = new HelpersStack();
stackHelper.dispose(); // Free memory
stackHelper = null;
```

## [Preventing selecting objects behind dat.gui with eventListner](https://discourse.threejs.org/t/avoid-mouse-interactions-listener-when-hover-gui/12315)

```javascript
//Instead of defining the eventListener on document:
document.addEventListener("mouseup", onMouseUp, false);

// Define the eventListener on the renderer.domElement.
renderer.domElement.addEventListener("mouseup", onMouseUp, false);
```