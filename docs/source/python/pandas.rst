Pandas FAQ
==========
   
.. toctree::
   :maxdepth: 2

.. `link <link>`_
.. --------------

Click on the links in the headings for more information.

`Create empty dataframe <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.empty.html>`_
---------

  .. code-block:: python

    df_empty = pd.DataFrame()


Creating & editing entries
--------------------------

  .. code-block:: python

    # Replacing pandas dataframe column values with another value.
    # Values to replace = ['ABC', 'AB']
    # Replacement value = 'A'
    df['BrandName'] = df['BrandName'].replace(['ABC', 'AB'], 'A')

    # Turn off warnings where overwriting dataframe values.
    pd.options.mode.chained_assignment = None  # default='warn'

`Concatenating dataframes <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.empty.html>`_
---------

  .. code-block:: python

    df_empty = pd.DataFrame()

`Renaming headers <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rename.html>`_
---------

  .. code-block:: python

    # Provide a dictionary with "before":"after" names of the items to be renamed.
    df.rename(columns={"A": "a", "B": "c"})


`Concatenating <https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html>`_
---------

  .. code-block:: python

    # Concatenating dataframes by row, ie appending rows with the same header.
    result = df1.append(df4, sort=False)
    # or
    result = pd.concat([df1, df4], axis=0, sort=False)

    # Concatenating dataframes by column, ie appending additional header columns.
    result = pd.concat([df1, df4], axis=1, sort=False)

This may require reindexing each dataframe that needs to be
appended - see this `Concatenating <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.reset_index.html>`_ for more information.

Find number of rows in dataframe
--------------------------------

  .. code-block:: python

    len(df)




Indexing data
-------------

  .. code-block:: python

    df.loc[row_indexer,column_indexer]
