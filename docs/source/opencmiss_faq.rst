OpenCMISS FAQ
=============

.. toctree::
   :maxdepth: 2

.. TEMPLATE: `link <link>`_

Using python bindings on hpc3
-----------------------------
  .. code-block:: python

    # To use it, open a terminal and log in​to​ the hpc3 machine:
    ssh hpc3 # or
    ssh upi@hpc3​

    # Make sure you are running the bash shell
    bash

    # Setup environmental variables for OpenCMISS
    source /people/cmiss/develop_opencmiss.sh

    # Tell python where the OpenCMISS libraries are located
    source /people/cmiss/opencmiss/install/x86_64_linux/gnu-C4.4-gnu-F4.4/openmpi_release/virtual_environments/bin/activate

    # Go to the directory where the Laplace example is located (if needed, download from the OpenCMISS-examples repo)
    cd python/example/location/

    # Run the OpenCMISS example.
    python LaplaceExample.py


Debugging OpenCMISS examples
----------------------------

Set diagnostics on and off before/after the line of interest.

Use Totalview.
