# Dat.Gui FAQ

## Accessing object methods and attributes inside an event callback.
Use the following es6 style functions. It will allow accessing all attributes 
and methods from class that creates the event callback. 
```javascript
class Modules {
  constructor() {
    this.showModel = true;
  }
  addGui(gui) {
    this.showModelControl = gui.add(this, 'showModel').listen();

    this.showModelControl.onChange((showModel) => {
      if (showModel) {
        this.showModel = false;
      } else {
        this.showModel = true;
      }
    });
  }
}
```
