# Python FAQ
   
General tips can be found here:
http://book.pythontips.com/en/latest/index.html


Click on the links in the headings for more information.

## Python virtual environments
- [Data camp tutorial](https://www.datacamp.com/community/tutorials/virtual-environment-in-python)
- [Real Python tutorial](https://realpython.com/python-virtual-environments-a-primer/)

## Strings
```python
# Replace substring in string (where the item in [] is an optional argument.
str.replace(old_substring, new_substring [, count])
```

## Displaying docstrings to see function arguments and info
```python
help(function)
```

See [Doc string conventions (PEP257)](https://www.python.org/dev/peps/pep-0257/) for information about how to write docstrings.

## Comparisons
[Check if variable is a certain type](http://stackoverflow.com/questions/12569452/how-to-identify-numpy-types-in-python)
```python
# Check if a local variable exists.
if 'myVar' in locals():
    pass  # myVar exists.
# Check if a global variable exists.
if 'myVar' in globals():
    pass  # myVar exists.
# Is variable a list?
isinstance(variable, list)
# Check if variable is a function.
callable(obj)
```
  
## Objects
```python
# Check if an object has an attribute.
if hasattr(obj, 'attr_name'):

# Set an attribute.
setattr(obj, 'attr_name', 'attr_value')

# Set an attribute within a class.
setattr(self, 'attr_name', 'attr_value')
```
  
## [Dictionaries](http://www.python-course.eu/dictionaries.php)
```python
# Creating dictionaries.
dict = {}
# The key is 'color', the item is 'blue'.
dict['color'] = 'blue'
# or
dict = {'color': 'blue'}

# Iterating through keys.
for key in dict:
  print(key)

# Listing items (as a tuple).
items = a_dict.items()
#prints: dict_items([('color', 'blue')])

# Iterating through items.
for item in dict.items():
  print(item)

# Iterating through key-item pairs.
for key, value in dict.items():
  print(key, '->', value)
```

## Path and IO functions

See [os.path](https://docs.python.org/2/library/os.path.html) and [shutil](https://docs.python.org/2/library/shutil.html) for more information.
```python
import os
os.path.exists(path) # Returns true for directories.
os.path.isfile(path) # Returns false for directories.
os.path.isdir(path)
os.path.join(path, *paths)
os.path.split(path) # Returns (head, tail) where tail is the last pathname component
os.path.dirname(path) # Returns the head of the path.
os.path.basename(path) # function returns the tail of the path.
# Get file extension.
filename, file_extension = os.path.splitext('/path/to/somefile.ext')

# Check if a directory exists and create it if necessary
if not os.path.exists(directory):
    os.makedirs(directory)

import shutil
shutil.copyfile(src, dst) # dst must be the complete target file name.
shutil.copy(src, dst) # dst can be a directory.
shutil.rmtree() # will delete a directory and all its contents.

# Find module directory.
import my_module
module_path = os.path.dirname(my_module.__file__)
```

## [Load/save json](http://stackoverflow.com/questions/12309269/how-do-i-write-json-data-to-a-file-in-python)
```python
# Load.
import json
with open('strings.json') as json_data:
    d = json.load(json_data)
    print(d)

# Save.
import json
with open('data.txt', 'w') as outfile:
    json.dump(data, outfile, indent=4)
```

## [Understanding decorators](https://ains.co/blog/things-which-arent-magic-flask-part-1.html)

## [Manually throw/raise an exception](http://stackoverflow.com/questions/2052390/manually-raising-throwing-an-exception-in-python)
```python
raise ValueError('A very specific bad thing happened')
```

The class hierarchy for built-in exceptions is:
```python
    BaseException
     +-- SystemExit
     +-- KeyboardInterrupt
     +-- GeneratorExit
     +-- Exception
          +-- StopIteration
          +-- StopAsyncIteration
          +-- ArithmeticError
          |    +-- FloatingPointError
          |    +-- OverflowError
          |    +-- ZeroDivisionError
          +-- AssertionError
          +-- AttributeError
          +-- BufferError
          +-- EOFError
          +-- ImportError
               +-- ModuleNotFoundError
          +-- LookupError
          |    +-- IndexError
          |    +-- KeyError
          +-- MemoryError
          +-- NameError
          |    +-- UnboundLocalError
          +-- OSError
          |    +-- BlockingIOError
          |    +-- ChildProcessError
          |    +-- ConnectionError
          |    |    +-- BrokenPipeError
          |    |    +-- ConnectionAbortedError
          |    |    +-- ConnectionRefusedError
          |    |    +-- ConnectionResetError
          |    +-- FileExistsError
          |    +-- FileNotFoundError
          |    +-- InterruptedError
          |    +-- IsADirectoryError
          |    +-- NotADirectoryError
          |    +-- PermissionError
          |    +-- ProcessLookupError
          |    +-- TimeoutError
          +-- ReferenceError
          +-- RuntimeError
          |    +-- NotImplementedError
          |    +-- RecursionError
          +-- SyntaxError
          |    +-- IndentationError
          |         +-- TabError
          +-- SystemError
          +-- TypeError
          +-- ValueError
          |    +-- UnicodeError
          |         +-- UnicodeDecodeError
          |         +-- UnicodeEncodeError
          |         +-- UnicodeTranslateError
          +-- Warning
               +-- DeprecationWarning
               +-- PendingDeprecationWarning
               +-- RuntimeWarning
               +-- SyntaxWarning
               +-- UserWarning
               +-- FutureWarning
               +-- ImportWarning
               +-- UnicodeWarning
               +-- BytesWarning
               +-- ResourceWarning
```