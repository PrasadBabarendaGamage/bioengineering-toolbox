# Javascript FAQ

Click on the links in the headings for more information.

## [var vs let vs const](https://dev.to/sarah_chima/var-let-and-const--whats-the-difference-69e)

`let` is preferred for variable declaration now. It's no surprise as it comes as an improvement to the `var` declarations.

### Scope

- ``var`` declarations are globally scoped or function scoped.

- ``let`` and ``const`` declarations are block scoped.

### Updating and re-declaring variables

- ``var`` variables can be updated and re-declared within its scope.

- ``let`` variables can be updated but not re-declared.

- ``const`` variables can neither be updated nor re-declared.

### Initialisation

- `var` variables are initialized with undefined.

- `let` and `const` variables are not initialized.

- `var` and `let` can be declared without being initialized.

- `const` must be initialized during declaration.

## Strings

### String concatenation
In javascript the `+` operator is used to add numbers or to concatenate strings. if one of the operands is a string `+` concatenates, and if it is only numbers it adds them, for example:
```javascript
1+2+3 == 6
"1"+2+3 == "123"
```

## Arrays
```javascript
// Adding elements to arrays using push.
var array = [];
array.push(5);

//Flatten array of arrays.
const arrays = [[1], ["2"], [3]];
const merged = [].concat(arrays);

// Get subset of values from an array without modifying original array.
const array  = [1, 2, 3, 4, 5];
// slice from 1..3 - add 1 as the end index is not included
const arraySubset = array.slice(1, 3 + 1);
console.log(arraySubset);

// Check if value is an array.
Array.isArray(your_array)
```

## [Converting between data types](https://gomakethings.com/converting-strings-to-numbers-with-vanilla-javascript/)

```javascript
// The parseInt() method converts a string into an integer (a whole number). 
// You can even pass in strings with random text in them, but the number needs
// to be the first part of the string.
var text = '42px';
var integer = parseInt(text, 10); // returns 42

// The parseFloat() method converts a string into a point number (a number 
// with decimal points). You can even pass in strings with random text in them,
// but the number needs to be the first part of the string.
var text = '3.14someRandomStuff';
var pointNum = parseFloat(text); // returns 3.14

// The Number() method converts a string to a number.
// Sometimes it’s an integer. Other times it’s a point number. And if you 
// pass in a string with random text in it, you’ll get NaN, an acronym for 
// “Not a Number.”
// Less safe than parseInt() and parseFloat()
Number('123'); // returns 123
Number('12.3'); // returns 12.3
Number('3.14someRandomStuff'); // returns NaN
Number('42px'); // returns NaN
```

## [Conditional operator (if and ?)](https://javascript.info/ifelse#:~:text=The%20so%2Dcalled%20%E2%80%9Cconditional%E2%80%9D,JavaScript%20which%20has%20that%20many.)

```javascript
// If statement.
if (condition1) {
  console.log("condition1 is true");
} else if (condition2) {
  console.log("condition2 is true");
} else {
  console.log("both conditions not true");
}

// Check if object attribute exists.
if (object.attribute) {
  console.log("exists");
}

// ? conditional operator.
let result = condition ? value1 : value2;
// The condition is evaluated: if it’s truthy then value1is returned, otherwise
// – value2, e.g:
let accessAllowed = (age > 18) ? true : false;
```


## [Classes](https://www.w3schools.com/Js/js_classes.asp)

```javascript
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
```

## [Objects](https://www.tutorialsteacher.com/javascript/javascript-object)

```javascript
// Declaring new objects.
// 1. Object literal.
// 1.a  Object with no properties or methods.
var emptyObject = {};
// 1.b  Object with properties and methods.
let person = {
  firstName: "John",
  lastName : "Doe",
  id       : 5566,
  getFullName : function() {
    return this.firstName + " " + this.lastName;
  }
}
// 2. Object constructor.
let person = new Object();
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
let name = person.getFullName();

// Find number of keys.
Object.keys(person).length

// List value of an object.
Object.values(person)

// Check if object attribute exists.
if (object.attribute) {
  console.log("exists");
}

/// Return first value of an object.
Object.values(person)[0]

// Looping - see looping section.
```

## Looping

```javascript
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

// Looping through object values.
const object = {'a': 1, 'b': 2, 'c' : 3};
for (const value of Object.values(object)) {
  console.log(value);
}

// Looping through object keys.
const object = {'a': 1, 'b': 2, 'c' : 3};
for (const key of Object.keys(object)) {
  console.log(key);
}

// Looping through objects keys and values.
const object = {'a': 1, 'b': 2, 'c' : 3};
for (const [key, value] of Object.entries(object)) {
  console.log(key, value);
}
```

## TypedArray

```javascript
// Create a TypedArray with a size in bytes.
const typedArray1 = new Int8Array(8);
const typedArray2 = new Float32Array(11);

// Set TypedArray values by direct assignment.
typedArray1[0] = 32;
typedArray2[0] = 32.34;

// Set TypedArray values using set - typedarray.set(array[, offset])
typedArray1.set([1, 2, 3], 3);
```

## [ES6 Modules](https://medium.com/backticks-tildes/introduction-to-es6-modules-49956f580da)

- Everything inside an ES6 module is private by default, and runs in strict mode (there’s no need for 'use strict').

- Public variables, functions and classes are exposed using export.

- Exposed modules are called into other modules using import

- Modules must be included in your HTML with type="module", which can be an inline or external script tag.

```javascript
// Define src in a different file;
<script type="module" src="main.js"></script>

// or an inline script.
<script type="module">
 
</script>
```
- Modules are deferred, and only run after a document is loaded

## [Fetching](https://dev.to/shoupn/javascript-fetch-api-and-using-asyncawait-47mp)
```javascript
addLandmarks() {
let server = '127.0.0.1:5000'
var module = this; // Allows variables to be accessed within then().
fetch(`http://${server}/return_landmarks?participant_id=${this.participant}`)
  .then(function (response) {
    return response.json();
  })
  .then(function (json) {
    console.log(json)
  });
}
```

## Adding and removing event listeners with access to 'this'
```javascript
class Test {
  constructor(){
    this.success = false;
    this.onMouseUp = () => {
      // Access attributes of this class.
      this.success = true;
    }
    document.addEventListener('mouseup', this.onMouseUp);
    document.removeEventListener('mouseup', this.onMouseUp);
  }
}
```
