Python FAQ
==========
   
.. toctree::
   :maxdepth: 2

.. `link <link>`_
.. --------------

General tips can be found here:
http://book.pythontips.com/en/latest/index.html


Click on the links in the headings for more information.

Displaying docstrings to see function arguments and info
---------------------------------------------------------
  .. code-block:: python

    help(function)

See `Doc string conventions (PEP257) <https://www.python.org/dev/peps/pep-0257/>`_ for information about how to write docstrings

`Check if a variable is a list? <http://stackoverflow.com/questions/12569452/how-to-identify-numpy-types-in-python>`_
---------------------------------------------------------------------------------------------------------------------

  .. code-block:: python

    isinstance(variable, list)


`Check the existence of a local variable <http://stackoverflow.com/questions/843277/how-do-i-check-if-a-variable-exists>`_
---------------------------------------

  .. code-block:: python

    if 'myVar' in locals():
        # myVar exists.

`Check the existence of a global variable <http://stackoverflow.com/questions/843277/how-do-i-check-if-a-variable-exists>`_
----------------------------------------

  .. code-block:: python

    if 'myVar' in globals():
        # myVar exists.

Objects
-------

  .. code-block:: python

    # Check if an object has an attribute.
    if hasattr(obj, 'attr_name'):

    # Set an attribute.
    setattr(obj, 'attr_name', 'attr_value')

    # Set an attribute within a class.
    setattr(self, 'attr_name', 'attr_value')


`Check if variable is a function <http://stackoverflow.com/questions/624926/how-to-detect-whether-a-python-variable-is-a-function>`_
---------------------------------------------------------
  .. code-block:: python

    callable(obj)

`Dictionaries <http://www.python-course.eu/dictionaries.php>`_
------------

  .. code-block:: python

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


Common IO functions 
-------------------
See `os.path <https://docs.python.org/2/library/os.path.html>`_, `shutil <https://docs.python.org/2/library/shutil.html>`_ for more information.

  .. code-block:: python

    import os
    os.path.exists(path) # returns true for directories
    os.path.isfile(path) # returns false for directories
    os.path.isdir(path)
    os.path.join(path, *paths)
    os.path.split(path) # returns (head, tail) where tail is the last pathname component
    
    # Check if a directory exists and create it if necessary
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    import shutil
    shutil.copyfile(src, dst) # dst must be the complete target file name
    shutil.copy(src, dst) # dst can be a directory
    shutil.rmtree() # will delete a directory and all its contents.



`Load/save json <http://stackoverflow.com/questions/12309269/how-do-i-write-json-data-to-a-file-in-python>`_
-----------------------------------------------------------------------

  .. code-block:: python

    import json
    with open('strings.json') as json_data:
        d = json.load(json_data)
        print(d)

  .. code-block:: python

    import json
    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile, indent=4)

`Manually throw/raise an exception <http://stackoverflow.com/questions/2052390/manually-raising-throwing-an-exception-in-python>`_
-----------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: python

    raise ValueError('A very specific bad thing happened')

The class hierarchy for built-in exceptions is:

  .. code-block:: bash

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

`Tutorials for for plotting in python using matplotlib <https://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html>`_
-------------------------------------------------------------------------------
