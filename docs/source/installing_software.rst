Installing software
===================

.. toctree::
   :maxdepth: 2

.. TEMPLATE: `link <link>`_

Click on the links in the headings for more information.

`Manually building h5py bindings with local version of hdf5`_
-----------------------------------------------------------------------------------------------------------------------------------

  .. code-block:: bash

    python setup.py build_ext --include-dirs=/hpc/psam012/usr/hdf5/hdf5-1.8.12/include/ --library-dirs=/hpc/psam012/usr/hdf5/hdf5-1.8.12/lib/
    python setup.py install --home=/hpc/psam012/opt/summer-projects/2017/python-modules/
