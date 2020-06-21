==============
Javascript FAQ
==============

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

Arrays
------

  .. code-block:: javascript

    // Adding elements to arrays using push.
    var array = [];
    array.push(5);

    //Flatten array of arrays.
    const arrays = [[1], ["2"], [3]];
    const merged = [].concat(arrays);

`Conditional operator (if and ?) <https://javascript.info/ifelse#:~:text=The%20so%2Dcalled%20%E2%80%9Cconditional%E2%80%9D,JavaScript%20which%20has%20that%20many.>`_
------

  .. code-block:: javascript
    // Check if object attribute exists.
    if (object.attribute) {
      console.log("exists");
    }

    // ? conditional operator.
    let result = condition ? value1 : value2;
    // The condition is evaluated: if it’s truthy then value1is returned, otherwise – value2, e.g:
    let accessAllowed = (age > 18) ? true : false;


`Classes <https://www.w3schools.com/Js/js_classes.asp>`_
-------

  .. code-block:: javascript

    // Constructor is similar to __init__ in python.
    class Car {
      constructor(brand) {
        this.carname = brand;
      }
      present(x) {
        return x + ", I have a " + this.carname;
      }
    }
    mycar = new Car("Ford");
    mycar.present('Hello');


`Objects <https://www.tutorialsteacher.com/javascript/javascript-object>`_
-------

  .. code-block:: javascript

    // Declaring new objects.
    // 1. Object literal.
    var emptyObject = {}; // object with no properties or methods
    var person = {
      firstName: "John",
      lastName : "Doe",
      id       : 5566,
      getFullName : function() {
        return this.firstName + " " + this.lastName;
      }
    // 2. Object constructor.
    var person = new Object();
    // Attach properties and methods to person object.
    person.firstName = "James";
    person["lastName"] = "Bond";
    person.age = 25;
    person.getFullName = function () {
            return this.firstName + ' ' + this.lastName;
    };

    // Accessing - objectName.propertyName
    person.firstName
    person["lastName"]

    // Accessing object methods - objectName.methodName()
    name = person.getFullName();

    // Find number of keys.
    Object.keys(person).length

    // List value of an object.
    Object.values(person)

    // Check if object attribute exists.
    if (object.attribute) {
      console.log("exists");
    }


Looping
-------

  .. code-block:: javascript

    // For each value in array.
    const foobar = [1, 2, 3];
    for (const value of foobar) {
      console.log(value, element);
    }
    // For each index and value in array.
    const foobar = ['A', 'B', 'C'];
    for (const [index, element] of foobar.entries()) {
      console.log(index, element);
    }

TypedArray
----------

  .. code-block:: javascript

    // Create a TypedArray with a size in bytes.
    const typedArray1 = new Int8Array(8);
    const typedArray2 = new Float32Array(11);

    // Set TypedArray values by direct assignment.
    typedArray1[0] = 32;
    typedArray2[0] = 32.34;

    // Set TypedArray values using set - typedarray.set(array[, offset])
    typedArray1.set([1, 2, 3], 3);

`ES6 Modules <https://medium.com/backticks-tildes/introduction-to-es6-modules-49956f580da>`_
-------

- Everything inside an ES6 module is private by default, and runs in strict mode (there’s no need for 'use strict').

- Public variables, functions and classes are exposed using export.

- Exposed modules are called into other modules using import

- Modules must be included in your HTML with type="module", which can be an inline or external script tag.

  .. code-block:: javascript

    <script type="module" src="main.js"></script>

    <script type="module">
      // or an inline script
    </script>

- Modules are deferred, and only run after a document is loaded