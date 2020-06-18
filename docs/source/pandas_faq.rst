Pandas FAQ
==========
   
.. toctree::
   :maxdepth: 2

.. `link <link>`_
.. --------------

General tips can be found here:
http://book.pythontips.com/en/latest/index.html


Click on the links in the headings for more information.

Creating & editing entries
--------------------------

  .. code-block:: python

    # Replacing pandas dataframe column values with another value.
    # Values to replace = ['ABC', 'AB']
    # Replacement value = 'A'
    df['BrandName'].replace(['ABC', 'AB'], 'A')

