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

Alternative is to set the HDF5_DIR environmental variable

  .. code-block:: bash

    export HDF5_DIR=/hpc/psam012/usr/hdf5/hdf5-1.8.12/

Then update your ~/.bashrc

  .. code-block:: bash

    #export PYTHONPATH="/hpc/psam012/opt/summer-projects/2017/python-modules/lib/python:$PYTHONPATH"
    
    
NLopt and HPC
-------------------------

To install NLopt on hpc, create a new folder and change to it. 
For example:

  .. code-block:: bash
  
    mkdir nlopt
    cd nlopt/


Download the .tar.gz file,

  .. code-block:: bash
  
    wget http://ab-initio.mit.edu/nlopt/nlopt-2.4.2.tar.gz

and unpack it.

  .. code-block:: bash
  
    tar -zxvf nlopt-2.4.2.tar.gz

Change to the unpacked folder and configer the make file.

  .. code-block:: bash
  
    cd nlopt-2.4.2
    ./configure --prefix=/hpc/upi/usr/nlopt/nlopt-2.4.2 --enable-shared --without-matlab


Finish the installation with

  .. code-block:: bash
  
    make

and

  .. code-block:: bash
  
    make install

Update to your ~/.bashrc

  .. code-block:: bash

    export PYTHONPATH=/hpc/upi/usr/nlopt/nlopt-2.4.2/lib64/python2.7/site-packages/:$PYTHONPATH
    export LD_LIBRARY_PATH="/hpc/upi/usr/nlopt/nlopt-2.4.2/lib/:$LD_LIBRARY_PATH"
