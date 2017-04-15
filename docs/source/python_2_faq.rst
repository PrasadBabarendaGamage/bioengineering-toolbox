Python 2 FAQ
============
   
.. toctree::
   :maxdepth: 2

.. TEMPLATE: `link <link>`_

Click on the links in the headings for more information.

Displaying docstrings to see function arguments and info
---------------------------------------------------------
  .. code-block:: python

    help(function)

See `Doc string conventions (PEP257) <https://www.python.org/dev/peps/pep-0257/>`_ for information about how to write docstrings

`Manually throw/raise an exception? <http://stackoverflow.com/questions/2052390/manually-raising-throwing-an-exception-in-python>`_
-----------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: python

    raise ValueError('A very specific bad thing happened')

`Check if a variable is a list? <http://stackoverflow.com/questions/12569452/how-to-identify-numpy-types-in-python>`_
---------------------------------------------------------------------------------------------------------------------

  .. code-block:: python

    isinstance(variable, list)

`Creating dictionaries <http://www.python-course.eu/dictionaries.php>`_
-----------------------------------------------------------------------

  .. code-block:: python

    results = {}
    results['Deformation Gradient Tensor'] = F

  or

  .. code-block:: python

    results = {'Deformation Gradient Tensor' : F,}

Common IO functions 
-------------------
See `os.path <https://docs.python.org/2/library/os.path.html>`_, `shutil <https://docs.python.org/2/library/shutil.html>`_ for more information.

  .. code-block:: python

    import os
    os.path.exists(path)
    os.path.isfile(path)
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




