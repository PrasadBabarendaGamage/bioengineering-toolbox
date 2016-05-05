Python FAQ
==========
   
.. toctree::
   :maxdepth: 2

.. TEMPLATE: **text** `link <link>`_

**How do I manually throw/raise an exception?** `link <http://stackoverflow.com/questions/2052390/manually-raising-throwing-an-exception-in-python>`_

  .. code-block:: python

    raise ValueError('A very specific bad thing happened')

**How do I check if a variable is a list?** `link <http://stackoverflow.com/questions/12569452/how-to-identify-numpy-types-in-python>`_

  .. code-block:: python

    isinstance(variable, list)

**Creating dictionaries** `link <http://www.python-course.eu/dictionaries.php>`_

  .. code-block:: python

    results = {}
    results['Deformation Gradient Tensor'] = F

  or

  .. code-block:: python

    results = {'Deformation Gradient Tensor' : F,}
